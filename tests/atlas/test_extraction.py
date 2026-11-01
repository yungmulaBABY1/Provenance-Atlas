"""Recorded claim extraction (atlas.extraction): M1 Increment B controls.

These check recording: pins, source-light publication, anchor bookkeeping, links,
and the arithmetic of the declared evidence check. They do not check that the
extraction, the paper or any review is correct. Tests needing the private full
output and the source PDF run only when ATLAS_PRIVATE_S2_OUTPUT and
ATLAS_PRIVATE_S2_PDF point at them; CI does not have them.
"""

import copy
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from atlas.contract import ContractError, canonical, load_json, normalize, sha256  # noqa: E402
from atlas.extraction import anchors, output, stats  # noqa: E402
from atlas.extraction import local  # noqa: E402
from atlas.extraction.build import build, check_public_files, jsonl, replay, validate  # noqa: E402

RUN = ROOT / "tests/atlas/extraction/s2-run1"
CONTEXT = json.loads((RUN / "context.json").read_text(encoding="utf-8"))
RECEIPT = RUN / "receipt"
RID = CONTEXT["run"]["id"]


def of_type(bundle, kind):
    return [r for r in bundle["records"] if r["type"] == kind]


def one(bundle, kind):
    items = of_type(bundle, kind)
    assert len(items) == 1, kind
    return items[0]


class CommittedRunTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundle = build(copy.deepcopy(CONTEXT), ROOT)

    def test_receipt_replays_at_content_level(self):
        result = replay((RECEIPT / "manifest.json").read_bytes(), (RECEIPT / "records.jsonl").read_bytes(),
                        ROOT, "content")
        self.assertEqual(result["replay"], "PASS")

    def test_run_facts_keep_their_basis(self):
        run = one(self.bundle, "ExtractionRun")
        self.assertEqual((run["runner"]["basis"], run["runner"]["verification"]), ("OPERATOR_STATED", "NOT_ESTABLISHED"))
        self.assertEqual(run["preflight"]["run_disposition"], "INSTRUMENT VERSION UNVERIFIED")
        self.assertIn("attestation, not a verification", run["preflight"]["note"])
        self.assertEqual(run["exposure"]["independence"], "NOT_ESTABLISHED")
        self.assertIn("PRIVATE", run["output"]["retention"])

    def test_claim_map_has_all_seven_rows_with_label_deviations_recorded(self):
        cmap = one(self.bundle, "ExtractedClaimMap")
        self.assertEqual(cmap["fields_present"], ["1", "2", "3", "4", "5A", "5B", "6"])
        self.assertTrue(cmap["producer"]["claim_extraction_output"])
        self.assertEqual({f: r["label_status"] for f, r in cmap["fields"].items() if r["label_status"] != "EXACT"},
                         {"5A": "SHORTENED", "5B": "SHORTENED"})
        self.assertEqual(cmap["claim_inventory"], "PRESENT")

    def test_field_6_restatements_are_compared_not_merged(self):
        results = {c["id"].split("/compare/")[1]: c["result"] for c in of_type(self.bundle, "TextComparison")}
        self.assertEqual(results, {"field-6-section~field-6-table-cell": "MISMATCH",
                                   "field-6-section~summary-claim-under-audit": "MISMATCH"})

    def test_anchor_bookkeeping(self):
        run = one(self.bundle, "ExtractionRun")
        self.assertEqual(run["counts"]["by_state"], {"ABSENCE": 5, "MATCH": 8, "MISMATCH": 4,
                                                     "NORMALIZED_MATCH_ONLY": 36, "RECONSTRUCTION": 1, "SAME_AS": 6})
        located = [a for a in of_type(self.bundle, "SourceAnchor") if a["verification"].get("found_page")]
        self.assertEqual(len(located), 44)
        self.assertTrue(all(a["verification"]["page_consistent"] for a in located))
        mismatched = sorted(a["anchor_id"] for a in of_type(self.bundle, "SourceAnchor")
                            if a["verification"].get("state") == "MISMATCH")
        self.assertEqual(mismatched, ["A1.2", "A1.4", "A2.11", "A2.8"])
        for a in of_type(self.bundle, "SourceAnchor"):
            if a["verification"].get("state") == "MISMATCH":
                self.assertTrue(a["verification"]["diagnostic"]["basis"].startswith("DIAGNOSTIC_ONLY"))
                self.assertIsNone(a["verification"]["extraction_span"])

    def test_source_light_publication(self):
        text = (RUN / "output-redacted.md").read_text(encoding="utf-8")
        parsed = output.parse(text)
        published = sorted(a["id"] for a in parsed["anchors"] if a["quote"])
        withheld = [a for a in parsed["anchors"] if a["withheld"]]
        self.assertEqual(published, ["A2.10", "A2.2", "A2.3", "A2.6", "A2.7"])
        self.assertEqual(len(withheld), 43)
        self.assertEqual(check_public_files(copy.deepcopy(CONTEXT), ROOT)["published_quotes_rechecked"], 5)

    def test_passage_links_preserve_review_disagreement(self):
        links = of_type(self.bundle, "PassageLink")
        self.assertEqual(sorted(l["id"].split("/passage-link/")[1] for l in links),
                         ["A2.10~S2-E2", "A2.2~S2-E2", "A2.6~S2-E3", "A2.7~S2-E3"])
        for link in links:
            self.assertEqual(link["relation"], "ANCHOR_WITHIN_IMPORTED_PASSAGE")
            self.assertIn("says nothing about support", link["relation_basis"])
            self.assertEqual(sorted(r["disposition"] for r in link["reviews"]), ["SUPPORTS", "SUPPORTS_WITH_QUALIFICATION"])
            self.assertTrue(all(r["human_adjudication"] == "NOT_RECORDED" for r in link["reviews"]))

    def test_historical_map_is_a_different_target_and_unchanged(self):
        cross = one(self.bundle, "CrossMapAlignment")
        self.assertEqual((cross["relation"], cross["claim_identity"]), ("DIFFERENT_TARGET_WORKS", "NOT_THE_SAME_AUDIT_TARGET"))
        self.assertEqual(cross["historical_target_work_id"], "doi:10.1177/0956797610383437")
        pin = CONTEXT["links"]["provisional_map_bundle"]["records"]
        self.assertEqual(sha256((ROOT / pin["path"]).read_bytes()), pin["sha256"])

    def test_evidence_check_on_the_designated_claim(self):
        check = one(self.bundle, "EvidenceCheck")
        self.assertEqual(check["result"], "CONSISTENT")
        subs = {s["sub_check"]: s for s in check["detail"]["sub_checks"]}
        self.assertEqual({k: v["result"] for k, v in subs.items()},
                         {"TRANSCRIPTION": "CONSISTENT", "P_FROM_T": "CONSISTENT", "T_FROM_CI": "CONSISTENT"})
        self.assertEqual(subs["P_FROM_T"]["df"], 196)
        self.assertEqual(check["target_statement_id"], one(self.bundle, "ExtractedClaimMap")["designated_field_6_id"])
        self.assertIn("does not reanalyse data", check["scope"])

    def test_cli_show_verified_and_refuses_tampering(self):
        def cli(*args):
            return subprocess.run([sys.executable, "-m", "atlas.extraction", "show", *args], cwd=ROOT,
                                  capture_output=True, text=True)
        shown = cli(str(RECEIPT / "records.jsonl"))
        self.assertEqual(shown.returncode, 0, shown.stderr)
        self.assertTrue(shown.stdout.startswith("VERIFIED RENDERING"))
        records = [load_json(l) for l in (RECEIPT / "records.jsonl").read_bytes().splitlines()]
        next(r for r in records if r["type"] == "EvidenceCheck")["detail"]["not_checked"] = []
        manifest = next(r for r in records if r["type"] == "ExtractionManifest")
        manifest["records_before_manifest_sha256"] = sha256(jsonl([r for r in records if r is not manifest]))
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "records.jsonl"
            path.write_bytes(jsonl(records))
            refused = cli(str(path))
            self.assertNotEqual(refused.returncode, 0)
            self.assertIn("NOT_VERIFIED", refused.stderr)
            self.assertEqual(refused.stdout, "")
            unverified = cli(str(path), "--unverified")
            self.assertTrue(unverified.stdout.startswith("=" * 10))
            self.assertIn("UNVERIFIED RENDERING OF STORED ASSERTIONS", unverified.stdout.split("\n")[1])


class PublicStageMutationTests(unittest.TestCase):
    """Copies of the committed files in a temp tree, edited and re-pinned."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        paths = [CONTEXT["run"]["method"]["instrument"]["path"], CONTEXT["run"]["method"]["run_prompt"]["path"],
                 CONTEXT["source"]["sources_json"]["path"], CONTEXT["public"]["anchor_verification"]["path"],
                 CONTEXT["public"]["redacted_output"]["path"],
                 *[e["path"] for e in CONTEXT["public"]["evidence_excerpts"]]]
        for bundle in CONTEXT["links"].values():
            paths += [bundle["manifest"]["path"], bundle["records"]["path"]]
        for path in paths:
            dest = self.root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / path, dest)
        self.ctx = copy.deepcopy(CONTEXT)

    def av(self):
        return load_json((self.root / self.ctx["public"]["anchor_verification"]["path"]).read_bytes())

    def write_av(self, av):
        path = self.root / self.ctx["public"]["anchor_verification"]["path"]
        path.write_bytes((canonical(av) + "\n").encode("utf-8"))
        self.ctx["public"]["anchor_verification"]["sha256"] = sha256(path.read_bytes())

    def edit_redacted(self, old, new, repin_av=True):
        path = self.root / self.ctx["public"]["redacted_output"]["path"]
        text = path.read_text(encoding="utf-8")
        self.assertEqual(text.count(old), 1, old)
        path.write_text(text.replace(old, new), encoding="utf-8")
        self.ctx["public"]["redacted_output"]["sha256"] = sha256(path.read_bytes())
        if repin_av:
            av = self.av()
            av["redacted_output_sha256"] = self.ctx["public"]["redacted_output"]["sha256"]
            self.write_av(av)

    def edit_excerpt(self, old, new):
        entry = self.ctx["public"]["evidence_excerpts"][0]
        path = self.root / entry["path"]
        text = path.read_text(encoding="utf-8")
        self.assertEqual(text.count(old), 1, old)
        text = text.replace(old, new)
        path.write_text(text, encoding="utf-8")
        entry["sha256"] = sha256(path.read_bytes())
        av = self.av()
        excerpt = next(e for e in av["public_excerpts"] if e["id"] == f"evidence:{entry['anchor_id']}")
        excerpt["sha256"], excerpt["end"] = entry["sha256"], excerpt["start"] + len(text)
        self.write_av(av)

    def test_redacted_output_change_without_repin_is_rejected(self):
        self.edit_redacted("p = .162, Cohen's d = −0.200).\n\n- **Target type", "p = .062, Cohen's d = −0.200).\n\n- **Target type",
                           repin_av=False)
        with self.assertRaisesRegex(ContractError, "ANCHOR_VERIFICATION_PIN_MISMATCH"):
            build(self.ctx, self.root)

    def test_misreported_claim_statistic_fails_transcription(self):
        self.edit_redacted("p = .162, Cohen's d = −0.200).\n\n- **Target type", "p = .062, Cohen's d = −0.200).\n\n- **Target type")
        check = one(build(self.ctx, self.root), "EvidenceCheck")
        self.assertEqual(check["result"], "INCONSISTENT")
        rows = {r["statistic"]: r["result"] for r in check["detail"]["sub_checks"][0]["rows"]}
        self.assertEqual(rows["p"], "DIFFERENT")
        self.assertEqual({k for k, v in rows.items() if v != "SAME"}, {"p"})

    def test_internally_inconsistent_source_numbers_fail(self):
        self.edit_excerpt("t(196) = −1.405, p = .162", "t(196) = −1.405, p = .062")
        self.edit_redacted("p = .162, Cohen's d = −0.200).\n\n- **Target type", "p = .062, Cohen's d = −0.200).\n\n- **Target type")
        av = self.av()
        a23 = next(a for a in av["anchors"] if a["id"] == "A2.3")
        a23["published_verbatim"], a23["within_public_excerpts"] = False, []
        self.write_av(av)
        quote = output.parse((self.root / self.ctx["public"]["redacted_output"]["path"]).read_text())["anchors"]
        line = next(a for a in quote if a["id"] == "A2.3")["quote"]["text"]
        self.edit_redacted("> " + line, output.withheld_line(line))
        av = self.av()
        a23 = next(a for a in av["anchors"] if a["id"] == "A2.3")
        a23["match"]["quote_sha256"] = sha256(line.encode("utf-8"))
        self.write_av(av)
        check = one(build(self.ctx, self.root), "EvidenceCheck")
        subs = {s["sub_check"]: s["result"] for s in check["detail"]["sub_checks"]}
        self.assertEqual(subs, {"TRANSCRIPTION": "CONSISTENT", "P_FROM_T": "INCONSISTENT", "T_FROM_CI": "CONSISTENT"})
        self.assertEqual(check["result"], "INCONSISTENT")

    def test_withheld_placeholder_hash_must_match(self):
        av = self.av()
        target = next(a for a in av["anchors"] if a["match"] and not a["published_verbatim"])
        target["match"]["quote_sha256"] = "0" * 64
        self.write_av(av)
        with self.assertRaisesRegex(ContractError, "WITHHELD_QUOTE_MISMATCH"):
            build(self.ctx, self.root)

    def test_published_quote_must_be_the_recorded_quote(self):
        self.edit_redacted("> However, we found no significant effect", "> However, we found no effect")
        with self.assertRaisesRegex(ContractError, "PUBLISHED_QUOTE_MISMATCH"):
            build(self.ctx, self.root)

    def test_published_quote_must_lie_in_the_excerpt_it_names(self):
        av = self.av()
        next(a for a in av["anchors"] if a["id"] == "A2.2")["within_public_excerpts"] = ["S2-E3"]
        self.write_av(av)
        with self.assertRaisesRegex(ContractError, "PUBLISHED_QUOTE_NOT_IN_EXCERPT"):
            build(self.ctx, self.root)

    def test_pinned_provisional_map_cannot_change(self):
        path = self.root / self.ctx["links"]["provisional_map_bundle"]["records"]["path"]
        path.write_bytes(path.read_bytes().replace(b"MISMATCH", b"MATCH", 1))
        with self.assertRaisesRegex(ContractError, "INPUT_HASH_MISMATCH"):
            build(self.ctx, self.root)


class TamperTests(unittest.TestCase):
    def setUp(self):
        self.bundle = build(copy.deepcopy(CONTEXT), ROOT)

    def tampered(self, change):
        records = json.loads(json.dumps(self.bundle["records"]))
        change(records)
        return records

    def test_same_claim_across_different_works_is_rejected(self):
        def change(records):
            next(r for r in records if r["type"] == "CrossMapAlignment")["claim_identity"] = "SAME_TEXT"
        with self.assertRaisesRegex(ContractError, "UNSUPPORTED_IDENTITY"):
            validate(self.tampered(change), self.bundle["external_ids"])

    def test_check_on_unusable_statement_is_rejected(self):
        def change(records):
            next(r for r in records if r["type"] == "FieldStatement" and r["role"] == "FIELD_6_SECTION")["status"] = "NOT_USABLE"
        with self.assertRaisesRegex(ContractError, "INELIGIBLE_CHECK_TARGET"):
            validate(self.tampered(change), self.bundle["external_ids"])

    def test_consistent_relabel_fails_replay(self):
        def change(records):
            next(r for r in records if r["type"] == "EvidenceCheck")["result"] = "INCONSISTENT"
        records = self.tampered(change)
        manifest = next(r for r in records if r["type"] == "ExtractionManifest")
        manifest["records_before_manifest_sha256"] = sha256(jsonl([r for r in records if r is not manifest]))
        validate(records, self.bundle["external_ids"])
        with self.assertRaisesRegex(ContractError, "REPLAY_MISMATCH"):
            replay((canonical(manifest) + "\n").encode("utf-8"), jsonl(records), ROOT, "content")


class MatcherTests(unittest.TestCase):
    TEXT = "Alpha beta\ngamma delta.\fSecond page: power-­posing works here.\nEnd. Alpha beta gamma."

    def match(self, quote):
        return anchors.match(quote, self.TEXT, anchors.NormalizedIndex(self.TEXT))

    def test_exact_normalized_mismatch(self):
        self.assertEqual(self.match("Second page")["state"], "MATCH")
        result = self.match("beta gamma delta.")
        self.assertEqual((result["state"], result["location"]), ("NORMALIZED_MATCH_ONLY", "UNIQUE"))
        start, end = result["extraction_span"]
        self.assertEqual(normalize(self.TEXT[start:end]), "beta gamma delta.")
        missing = self.match("power-posing works")
        self.assertEqual(missing["state"], "MISMATCH")
        codes = [d["extraction"].get("code_points") for d in missing["diagnostic"]["first_differences"]]
        self.assertIn(["U+00AD"], codes)

    def test_pages_and_ambiguity(self):
        self.assertEqual(self.match("Second page")["found_page"], 2)
        self.assertEqual(self.match("Alpha beta gamma")["found_page"], 2)
        ambiguous = self.match("Alpha beta")
        self.assertEqual((ambiguous["location"], ambiguous["extraction_span"]), ("AMBIGUOUS_MULTIPLE_OCCURRENCES", None))

    def test_non_nfc_extraction_is_refused(self):
        with self.assertRaises(ValueError):
            anchors.NormalizedIndex("é")


class OutputParserTests(unittest.TestCase):
    def test_redaction_round_trip(self):
        text = ("## SOURCE ANCHORS\n\n**A1.1** · x · p. 1, Method\n> quoted one\n\n"
                "**A1.2** · y · p. 2, Results\n> quoted two\n\n## READ RECORD\n")
        redacted = output.redact(text, {"A1.2"})
        parsed = output.parse(redacted)["anchors"]
        self.assertEqual(parsed[0]["withheld"]["quote_sha256"], sha256(b"quoted one"))
        self.assertEqual(parsed[1]["quote"]["text"], "quoted two")
        self.assertNotIn("quoted one", redacted)

    def test_anchor_kinds_and_duplicates(self):
        text = ("## SOURCE ANCHORS\n\n**A1.1** · gone · no passage. Absence finding.\n"
                "**A3.1** · author reconstruction from Field 1.\n**A6.1** · same passage as A2.3.\n"
                "**A6.1** · same passage as A2.4.\n\n## READ RECORD\n")
        parsed = output.parse(text)
        self.assertEqual([a["kind"] for a in parsed["anchors"]], ["ABSENCE", "RECONSTRUCTION", "SAME_AS", "DUPLICATE_ID"])
        self.assertIn("DUPLICATE_ANCHOR_ID", {i["code"] for i in parsed["issues"]})

    def test_table_label_status(self):
        text = "| 5A. Within-source | x | y |\n| 6. Claim under audit | c | s |\n| 2. Strongest | z | w |\n"
        table = output.parse(text)["table"]
        self.assertEqual({f: r["label_status"] for f, r in table.items()},
                         {"5A": "SHORTENED", "6": "EXACT", "2": "DIFFERENT"})


class StatsTests(unittest.TestCase):
    # Reference values from scipy.stats (1.18.1), recorded here so CI needs no scipy.
    P = [(1.405, 196, 0.16160420036488735), (2.0, 10, 0.07338803477074037), (0.5, 3, 0.651447964848151),
         (3.2, 1, 0.19282249595845916), (4.5, 30, 9.519359392112443e-05), (2.399, 193, 0.017391551162534293)]
    CRIT = [(1, 12.706204736174694), (10, 2.228138851986274), (196, 1.9721412216620415)]

    def test_t_distribution_matches_reference(self):
        for t, df, p in self.P:
            self.assertAlmostEqual(stats.p_two_tailed(t, df), p, delta=1e-10 * max(1, p) + 1e-15)
        for df, crit in self.CRIT:
            self.assertAlmostEqual(stats.t_critical(df), crit, places=9)

    def test_extract_forms_and_ambiguity(self):
        short = stats.extract("(mean difference = −4.077, 95% CI [−9.801, 1.647], t(196) = −1.405, p = .162, d = −0.200)")
        self.assertEqual(short["ci"]["lower"]["reported"], "−9.801")
        self.assertEqual(short["t"]["df"], 196)
        two = stats.extract("t(198) = −1.245, p = .215 and t(196) = −1.405, p = .162")
        self.assertEqual(two["t"]["status"], "AMBIGUOUS")

    def test_interval_logic(self):
        clean = "mean difference = −4.077, 95% CI = [−9.801, 1.647]), t(196) = −1.405, p = .162, d = −0.200"
        self.assertEqual(stats.check(clean, clean)["result"], "CONSISTENT")
        shifted = clean.replace("[−9.801, 1.647]", "[−9.801, 2.647]")
        self.assertEqual(stats.t_from_ci(stats.extract(shifted))["result"], "INCONSISTENT")


@unittest.skipUnless(os.environ.get("ATLAS_PRIVATE_S2_OUTPUT") and os.environ.get("ATLAS_PRIVATE_S2_PDF"),
                     "private inputs not available (full output and source PDF are not redistributed)")
class LocalStageTests(unittest.TestCase):
    def test_local_verify_reproduces_committed_public_files(self):
        result = local.verify(copy.deepcopy(CONTEXT), ROOT,
                              Path(os.environ["ATLAS_PRIVATE_S2_OUTPUT"]).read_bytes(),
                              Path(os.environ["ATLAS_PRIVATE_S2_PDF"]).read_bytes())
        self.assertEqual(result["local_verify"], "PASS")


if __name__ == "__main__":
    unittest.main()
