"""Claim links (atlas.claims): mechanical controls for M1 Increment A.

These check recording behavior: exact spans, text comparisons, review bindings,
dependency pins and replay. They do not check that any audit, claim or review
is scientifically correct, and no test decides whether two differently worded
statements are the same claim.
"""

import copy
import json
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from atlas.adapter import build as import_build  # noqa: E402
from atlas.claims import standalone  # noqa: E402
from atlas.claims.link import build, replay, validate  # noqa: E402
from atlas.contract import ContractError, canonical, load_json, sha256  # noqa: E402

CONTEXT = json.loads((ROOT / "tests/atlas/claims/power-posing-reviewed.json").read_text())
REVIEWED = json.loads((ROOT / "tests/atlas/power-sources-reviewed.json").read_text())
BASELINE = json.loads((ROOT / "atlas/baseline.json").read_text())
RECEIPT = ROOT / "tests/atlas/claims/receipts/power-posing-reviewed"
CONTRACT = "prompts/1-claim-extraction.txt"
DEP_RUN = "urn:atlas:import:power-posing-sources:3"
FIELD_6 = ("The cited literature independently establishes that briefly adopting expansive\n"
           "  power poses produces reliable behavioral and physiological benefits.")
TARGET = ("The cited literature independently establishes reliable behavioral and physiological "
          "benefits from brief expansive power poses.")


def of_type(bundle, kind):
    return [r for r in bundle["records"] if r["type"] == kind]


def alignment(bundle, number):
    return next(r for r in of_type(bundle, "TargetAlignment") if r["finding_number"] == str(number))


def by_id(bundle):
    return {r["id"]: r for r in bundle["records"]}


def receipt_context(name, run_id, receipt):
    base = ROOT / "tests/atlas/receipts" / receipt
    ctx = copy.deepcopy(CONTEXT)
    ctx["run"]["id"] = f"urn:atlas:claimlink:{name}:1"
    ctx["dependency"] = {
        "audit_run_id": run_id,
        "manifest": {"path": f"tests/atlas/receipts/{receipt}/manifest.json",
                     "sha256": sha256((base / "manifest.json").read_bytes())},
        "records": {"path": f"tests/atlas/receipts/{receipt}/records.jsonl",
                    "sha256": sha256((base / "records.jsonl").read_bytes())}}
    return ctx


class CommittedCaseTests(unittest.TestCase):
    """The committed power-posing development case, built from committed inputs."""

    @classmethod
    def setUpClass(cls):
        cls.bundle = build(copy.deepcopy(CONTEXT), ROOT)

    def test_committed_receipt_replays_at_content_level(self):
        result = replay((RECEIPT / "manifest.json").read_bytes(), (RECEIPT / "records.jsonl").read_bytes(),
                        ROOT, "content")
        self.assertEqual(result["replay"], "PASS")

    def test_claim_map_is_the_outputs_own_partial_fallback(self):
        cmap = of_type(self.bundle, "ClaimMap")[0]
        self.assertEqual(cmap["state"], "PRESENT")
        self.assertEqual(cmap["producer"]["mode"], "DEGRADED_STANDALONE")
        self.assertFalse(cmap["producer"]["claim_extraction_output"])
        self.assertEqual(cmap["fields_present"], ["1", "3", "6"])
        self.assertEqual(cmap["fields_usable"], ["1", "3", "6"])
        self.assertEqual(sorted(cmap["fields_absent"]), ["2", "4", "5A", "5B"])
        self.assertTrue(all(v.startswith("NOT_IN_STANDALONE_FALLBACK") for v in cmap["fields_absent"].values()))
        self.assertEqual(cmap["claim_inventory"], "NOT_PRODUCED")
        self.assertTrue(cmap["reconciliation"].startswith("NOT_PERFORMED"))

    def test_statements_are_exact_spans_of_the_output(self):
        # The output text stays in the dependency bundle; it is referenced, not copied.
        self.assertNotIn(DEP_RUN, by_id(self.bundle))
        records = [load_json(line) for line in (ROOT / CONTEXT["dependency"]["records"]["path"]).read_bytes().splitlines()]
        raw = next(r for r in records if r["id"] == DEP_RUN)["raw_output_text"]
        for item in of_type(self.bundle, "ClaimStatement"):
            anchor = item["anchor"]
            self.assertEqual(raw[anchor["char_start"]:anchor["char_end"]], item["exact_text"])
            self.assertEqual(anchor["output_sha256"], sha256(raw.encode("utf-8")))
            self.assertEqual(item["statement_kind"], "AUDIT_OUTPUT_TEXT")
        field6 = next(s for s in of_type(self.bundle, "ClaimStatement") if s["role"] == "MAP_FIELD_6")
        self.assertEqual(field6["exact_text"], FIELD_6)

    def test_finding_target_is_not_linked_as_the_designated_claim(self):
        for number in (1, 2):
            al = alignment(self.bundle, number)
            results = {by_id(self.bundle)[by_id(self.bundle)[c]["object_id"]]["role"]: by_id(self.bundle)[c]["result"]
                       for c in al["comparison_ids"]}
            self.assertEqual(results, {"MAP_FIELD_6": "MISMATCH", "CONFIRMATION_FIELD_6": "NORMALIZED_MATCH_ONLY"})
            self.assertEqual(al["claim_identity"], "UNRESOLVED_REQUIRES_REVIEW")
            self.assertEqual(al["finding_import_status"], "QUARANTINED")
        for item in of_type(self.bundle, "TextComparison"):
            if not item["exact_match"]:
                self.assertEqual(item["semantic_equivalence"], "UNASSESSED")

    def test_output_assertion_about_field_6_is_kept_separate(self):
        mentions = alignment(self.bundle, 1)["native_field_6_mentions"]
        self.assertEqual([m["field"] for m in mentions], ["Scope loss if NARROWS"])
        self.assertTrue(mentions[0]["basis"].startswith("DOCUMENTED_IN_OUTPUT"))
        self.assertEqual(alignment(self.bundle, 1)["claim_identity"], "UNRESOLVED_REQUIRES_REVIEW")

    def test_restatement_drift_within_the_run_is_recorded(self):
        results = {c["id"].split("/compare/")[1]: c["result"] for c in of_type(self.bundle, "TextComparison")}
        for n in ("1", "3", "6"):
            self.assertEqual(results[f"map-field-{n}~confirmation-field-{n}"], "MISMATCH")

    def test_reviews_are_bound_to_the_evidence_clause_not_the_claim(self):
        scopes = {s["review_id"].rsplit("/", 1)[1]: s for s in of_type(self.bundle, "ReviewScope")}
        self.assertEqual(sorted(scopes), ["F1-S2-review-A", "F1-S2-review-B"])
        for scope in scopes.values():
            self.assertEqual(scope["binding"], "MATCH")
            self.assertEqual((scope["reviewed_field"], scope["reviewed_span"]), ("Evidence", [0, 80]))
            self.assertEqual(scope["relation_to_finding_target"], "DOES_NOT_REVIEW_TARGET_CLAIM")
            self.assertEqual(scope["independence"], "NOT_ESTABLISHED")
            self.assertEqual(scope["human_adjudication"], "NOT_RECORDED")
        # The disagreement is preserved as two records; nothing reconciles it.
        self.assertEqual(scopes["F1-S2-review-A"]["disposition"], "SUPPORTS_WITH_QUALIFICATION")
        self.assertEqual(scopes["F1-S2-review-B"]["disposition"], "SUPPORTS")
        self.assertEqual(sorted(alignment(self.bundle, 1)["reviewer_decomposition_ids"]),
                         sorted(s["id"] for s in scopes.values()))
        self.assertEqual(alignment(self.bundle, 2)["reviewer_decomposition_ids"], [])

    def test_paper_statement_is_reported_missing(self):
        run = of_type(self.bundle, "ClaimLinkRun")[0]
        self.assertEqual(run["source_statement"]["state"], "NOT_AVAILABLE")
        self.assertTrue(any("RETRIEVAL_FAILED" in r for r in run["source_statement"]["reasons"]))

    def test_import_receipts_code_identity_is_unaffected(self):
        manifest = json.loads((ROOT / "tests/atlas/receipts/power-sources-reviewed/manifest.json").read_text())
        current = {p.name: sha256(p.read_bytes()) for p in sorted((ROOT / "atlas").glob("*.py"))}
        self.assertEqual(manifest["adapter"]["code_sha256"], current)
        self.assertNotIn("link.py", current)

    def test_cli_build_show_replay(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory) / "out"
            def cli(*args):
                return subprocess.run([sys.executable, "-m", "atlas.claims", *args], cwd=ROOT,
                                      capture_output=True, text=True)
            self.assertEqual(cli("build", "tests/atlas/claims/power-posing-reviewed.json", "--out", str(out)).returncode, 0)
            shown = cli("show", str(out / "records.jsonl"))
            self.assertEqual(shown.returncode, 0, shown.stderr)
            self.assertTrue(shown.stdout.startswith("VERIFIED RENDERING"))
            self.assertIn("claim identity: UNRESOLVED_REQUIRES_REVIEW", shown.stdout)
            self.assertIn("DOES_NOT_REVIEW_TARGET_CLAIM", shown.stdout)
            for level in ("strict", "content"):
                self.assertEqual(cli("replay", str(out / "manifest.json"), str(out / "records.jsonl"),
                                     "--level", level).returncode, 0)


class RealControlTests(unittest.TestCase):
    """Other committed outputs: different formats and target styles, no new data."""

    def test_unreviewed_import_has_no_decomposition(self):
        bundle = build(receipt_context("power-unreviewed", "urn:atlas:import:power-posing-sources:1",
                                       "power-sources"), ROOT)
        self.assertEqual(of_type(bundle, "ReviewScope"), [])
        self.assertEqual(alignment(bundle, 1)["reviewer_decomposition_ids"], [])

    def test_sub_claim_targets_stay_unresolved(self):
        bundle = build(receipt_context("case12", "urn:atlas:import:case12-healthy:1", "case12-healthy"), ROOT)
        self.assertEqual(of_type(bundle, "ClaimMap")[0]["state"], "PRESENT")
        for al in of_type(bundle, "TargetAlignment"):
            self.assertEqual(al["target_kind"], "TEXT")
            self.assertEqual(al["claim_identity"], "UNRESOLVED_REQUIRES_REVIEW")

    def test_reference_targets_map_gap_and_unrecognized_confirmation(self):
        bundle = build(receipt_context("shen", "urn:atlas:import:shen-known-bad:1", "shen-known-bad"), ROOT)
        cmap = of_type(bundle, "ClaimMap")[0]
        self.assertEqual(cmap["state"], "ABSENT")
        self.assertEqual(cmap["confirmation"]["state"], "UNRECOGNIZED_FORMAT")
        self.assertEqual({v for v in cmap["fields_absent"].values()}, {"NO_CLAIM_MAP_IN_OUTPUT"})
        identities = {int(a["finding_number"]): (a["target_kind"], a["claim_identity"])
                      for a in of_type(bundle, "TargetAlignment")}
        self.assertEqual(identities, {
            1: ("FIELD_6_REFERENCE", "DECLARED_BY_REFERENCE"),
            2: ("FIELD_6_REFERENCE", "DECLARED_BY_REFERENCE"),
            3: ("FIELD_6_REFERENCE", "DECLARED_BY_REFERENCE"),
            4: ("FIELD_6_REFERENCE", "UNRESOLVED_REQUIRES_REVIEW"),   # "... as transmitted"
            5: ("MAP_GAP_DECLARED", "DECLARED_NOT_ON_MAP"),
            6: ("FIELD_6_REFERENCE", "UNRESOLVED_REQUIRES_REVIEW")})  # "... explanatory model"
        self.assertTrue(all(a["designated_target_state"] == "FIELD_6_TEXT_NOT_IN_INPUTS"
                            for a in of_type(bundle, "TargetAlignment")))


class MutationTests(unittest.TestCase):
    """Mutated copies of the committed output, imported and linked in a temp tree."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        paths = set(BASELINE["files"]) | {REVIEWED["output"]["path"], CONTRACT}
        paths.update(a["path"] for a in REVIEWED["declared_inputs"])
        paths.update(r["artifact"]["path"] for r in REVIEWED["reviews"])
        for path in paths:
            dest = self.root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / path, dest)
        self.output = (ROOT / REVIEWED["output"]["path"]).read_text(encoding="utf-8")

    def link(self, output_text, ctx_change=None):
        """Import a (mutated) output, write it as a dependency bundle, link it."""
        path = self.root / REVIEWED["output"]["path"]
        path.write_text(output_text, encoding="utf-8")
        ctx = copy.deepcopy(REVIEWED)
        ctx["output"]["sha256"] = sha256(path.read_bytes())
        dep = import_build(ctx, self.root)
        out = self.root / "dep"
        out.mkdir(exist_ok=True)
        (out / "manifest.json").write_bytes((canonical(dep["manifest"]) + "\n").encode("utf-8"))
        (out / "records.jsonl").write_bytes(dep["jsonl"])
        link_ctx = copy.deepcopy(CONTEXT)
        link_ctx["dependency"]["manifest"] = {"path": "dep/manifest.json",
                                              "sha256": sha256((out / "manifest.json").read_bytes())}
        link_ctx["dependency"]["records"] = {"path": "dep/records.jsonl",
                                             "sha256": sha256((out / "records.jsonl").read_bytes())}
        if ctx_change:
            ctx_change(link_ctx)
        return build(link_ctx, self.root), link_ctx

    def single_line_field_6(self, text):
        """Field 6 rewritten as one line, so a table cell can match it exactly."""
        self.assertEqual(self.output.count(FIELD_6), 1)
        return self.output.replace(FIELD_6, text)

    def test_identical_target_text_is_same_text_only(self):
        bundle, _ = self.link(self.single_line_field_6(TARGET))
        al = alignment(bundle, 1)
        self.assertEqual(al["claim_identity"], "SAME_TEXT")
        first = by_id(bundle)[al["comparison_ids"][0]]
        self.assertEqual((first["result"], first["semantic_equivalence"]), ("MATCH", "NOT_ASSESSED_IDENTICAL_TEXT"))

    def test_wrapped_identical_text_is_normalized_match_only(self):
        bundle, _ = self.link(self.single_line_field_6(
            "The cited literature independently establishes reliable behavioral and\n"
            "  physiological benefits from brief expansive power poses."))
        self.assertEqual(alignment(bundle, 1)["claim_identity"], "SAME_TEXT_AFTER_NORMALIZATION")

    def test_polarity_change_gets_distinct_identity_and_breaks_the_link(self):
        same, _ = self.link(self.single_line_field_6(TARGET))
        flipped, _ = self.link(self.single_line_field_6(TARGET.replace("establishes", "does not establish")))
        old = next(s for s in of_type(same, "ClaimStatement") if s["role"] == "MAP_FIELD_6")
        new = next(s for s in of_type(flipped, "ClaimStatement") if s["role"] == "MAP_FIELD_6")
        self.assertNotEqual(old["id"], new["id"])
        self.assertEqual(alignment(flipped, 1)["claim_identity"], "UNRESOLVED_REQUIRES_REVIEW")
        # Records with stable IDs that depend on the statement change content: merging
        # the two bundles would be an ID/content conflict, never a silent update.
        old_cmp = {c["id"]: c for c in of_type(same, "TextComparison")}
        new_cmp = {c["id"]: c for c in of_type(flipped, "TextComparison")}
        shared = [i for i in old_cmp if i in new_cmp and "map-field-6" in i]
        self.assertTrue(shared)
        self.assertTrue(all(canonical(old_cmp[i]) != canonical(new_cmp[i]) for i in shared))

    def test_scope_change_in_field_3_gets_distinct_identity(self):
        before, _ = self.link(self.output)
        after, _ = self.link(self.output.replace("may increase self-reported", "may decrease self-reported", 1))
        role = lambda b: next(s for s in of_type(b, "ClaimStatement") if s["role"] == "MAP_FIELD_3")["id"]
        self.assertNotEqual(role(before), role(after))

    def test_changed_output_detaches_reviews(self):
        bundle, _ = self.link(self.single_line_field_6(TARGET))
        scopes = of_type(bundle, "ReviewScope")
        self.assertEqual(len(scopes), 2)
        for scope in scopes:
            self.assertEqual(scope["binding"], "TARGET_MISMATCH")
            self.assertIsNone(scope["finding_id"])
        al = alignment(bundle, 1)
        self.assertEqual(al["reviewer_decomposition_ids"], [])
        self.assertEqual(sorted(al["detached_review_ids"]), sorted(s["id"] for s in scopes))

    def assert_no_designated_target(self, bundle, state):
        records = by_id(bundle)
        for al in of_type(bundle, "TargetAlignment"):
            self.assertIsNone(al["designated_target_id"])
            self.assertEqual(al["designated_target_state"], state)
            self.assertEqual(al["claim_identity"], "UNRESOLVED_REQUIRES_REVIEW")
            roles = {records[records[c]["object_id"]]["role"] for c in al["comparison_ids"]}
            self.assertNotIn("MAP_FIELD_6", roles)
        self.assertFalse(any("/compare/map-field-6~" in c["id"] for c in of_type(bundle, "TextComparison")))

    def test_field_6_with_another_fields_label_is_not_a_target(self):
        # Wrong label, and text identical to the finding target: must not become SAME_TEXT.
        original = "- Field 6 — Claim under audit:\n  " + FIELD_6
        self.assertEqual(self.output.count(original), 1)
        bundle, _ = self.link(self.output.replace(original, "- Field 6 — Weaker defensible claim: " + TARGET))
        cmap = of_type(bundle, "ClaimMap")[0]
        self.assertEqual(cmap["state"], "PRESENT_WITH_DEFECTS")
        self.assertEqual(cmap["field_status"]["6"], "LABEL_MISMATCH")
        self.assertNotIn("6", cmap["fields_usable"])
        issue = next(i for i in cmap["parse_issues"] if i["code"] == "FIELD_LABEL_MISMATCH")
        self.assertEqual(issue["native_labels"], ["Weaker defensible claim"])
        kept = by_id(bundle)[cmap["field_statement_ids"]["6"][0]]
        self.assertEqual((kept["exact_text"], kept["field_status"], kept["native_label"]),
                         (TARGET, "LABEL_MISMATCH", "Weaker defensible claim"))
        self.assert_no_designated_target(bundle, "FIELD_6_LABEL_MISMATCH")

    def test_contradictory_duplicate_field_6_is_not_a_target(self):
        # A second Field 6 entry whose text is identical to the finding target.
        bundle, _ = self.link(self.output.replace(FIELD_6, FIELD_6 + "\n- Field 6 — Claim under audit: " + TARGET))
        cmap = of_type(bundle, "ClaimMap")[0]
        self.assertEqual(cmap["state"], "PRESENT_WITH_DEFECTS")
        self.assertEqual(cmap["field_status"]["6"], "DUPLICATE_ENTRIES")
        kept = [by_id(bundle)[i] for i in cmap["field_statement_ids"]["6"]]
        self.assertEqual([k["exact_text"] for k in kept], [FIELD_6, TARGET])
        self.assertEqual(len({k["id"] for k in kept}), 2)
        self.assert_no_designated_target(bundle, "FIELD_6_DUPLICATE_ENTRIES")
        self.assertEqual(sorted(alignment(bundle, 1)["designated_target_candidate_ids"]),
                         sorted(k["id"] for k in kept))
        # Neither order may let the first entry win.
        reordered = self.output.replace(FIELD_6, TARGET + "\n- Field 6 — Claim under audit: " + FIELD_6.replace("\n  ", " "))
        self.assert_no_designated_target(self.link(reordered)[0], "FIELD_6_DUPLICATE_ENTRIES")

    def test_duplicate_confirmation_line_is_not_compared(self):
        line = "- Claim under audit (map field 6): The cited literature independently establishes"
        self.assertEqual(self.output.count(line), 1)
        bundle, _ = self.link(self.output.replace(line, "- Claim under audit (map field 6): " + TARGET + "\n" + line))
        cmap = of_type(bundle, "ClaimMap")[0]
        self.assertEqual(cmap["confirmation"]["item_status"]["field_6"], "DUPLICATE_ENTRIES")
        records = by_id(bundle)
        for al in of_type(bundle, "TargetAlignment"):
            self.assertEqual({records[records[c]["object_id"]]["role"] for c in al["comparison_ids"]}, {"MAP_FIELD_6"})

    def test_dependency_byte_change_without_new_pin_is_rejected(self):
        _, ctx = self.link(self.output)
        records = self.root / "dep/records.jsonl"
        records.write_bytes(records.read_bytes().replace(b"QUARANTINED", b"QUARANTINEd", 1))
        with self.assertRaisesRegex(ContractError, "INPUT_HASH_MISMATCH"):
            build(ctx, self.root)

    def test_repinned_tampered_dependency_is_rejected(self):
        _, ctx = self.link(self.output)
        records = self.root / "dep/records.jsonl"
        lines = records.read_bytes().splitlines()
        edited = []
        for line in lines:
            item = json.loads(line)
            if item["type"] == "AuditFinding" and item["id"].endswith("/finding/1"):
                item["native"]["fields"]["Target claim"] = FIELD_6.replace("\n  ", " ")
            edited.append(canonical(item).encode("utf-8"))
        records.write_bytes(b"\n".join(edited) + b"\n")
        ctx["dependency"]["records"]["sha256"] = sha256(records.read_bytes())
        with self.assertRaisesRegex(ContractError, "DEPENDENCY_INVALID"):
            build(ctx, self.root)

    def test_manifest_from_another_bundle_is_rejected(self):
        def swap(ctx):
            other = ROOT / "tests/atlas/receipts/power-sources/manifest.json"
            dest = self.root / "dep/other-manifest.json"
            shutil.copyfile(other, dest)
            ctx["dependency"]["manifest"] = {"path": "dep/other-manifest.json", "sha256": sha256(dest.read_bytes())}
        with self.assertRaisesRegex(ContractError, "DEPENDENCY_MANIFEST_MISMATCH"):
            self.link(self.output, swap)

    def test_contract_without_its_table_is_rejected(self):
        def gut(ctx):
            path = self.root / CONTRACT
            path.write_text(path.read_text(encoding="utf-8").replace("| 2. Source's strongest claim |", "| 2. |"),
                            encoding="utf-8")
            ctx["claim_extraction_contract"]["sha256"] = sha256(path.read_bytes())
        with self.assertRaisesRegex(ContractError, "CONTRACT_TABLE_MISMATCH"):
            self.link(self.output, gut)


class TamperTests(unittest.TestCase):
    def setUp(self):
        self.bundle = build(copy.deepcopy(CONTEXT), ROOT)
        self.ids = self.bundle["dependency_ids"]

    def tampered(self, change):
        records = json.loads(json.dumps(self.bundle["records"]))
        change(records)
        return records

    def test_match_label_without_exact_match_is_rejected(self):
        def change(records):
            item = next(r for r in records if r["type"] == "TextComparison" and r["result"] == "MISMATCH")
            item["result"] = "MATCH"
        with self.assertRaisesRegex(ContractError, "INVALID_LABEL"):
            validate(self.tampered(change), self.ids)

    def test_statement_text_edit_is_rejected(self):
        def change(records):
            next(r for r in records if r["type"] == "ClaimStatement")["exact_text"] += " reliably"
        with self.assertRaisesRegex(ContractError, "STATEMENT_HASH_MISMATCH"):
            validate(self.tampered(change), self.ids)

    def test_consistent_relabel_fails_replay(self):
        # Labels the static validator cannot check against anything in the bundle.
        def change(records):
            al = next(r for r in records if r["type"] == "TargetAlignment")
            al["finding_import_status"] = "IMPORTED_UNADJUDICATED"
            al["claim_identity"] = "DECLARED_BY_REFERENCE"
        records = self.tampered(change)
        manifest = next(r for r in records if r["type"] == "ClaimLinkManifest")
        body = [r for r in records if r is not manifest]
        from atlas.claims.link import jsonl
        manifest["records_before_manifest_sha256"] = sha256(jsonl(body))
        validate(records, self.ids)  # internally consistent after re-hashing ...
        with self.assertRaisesRegex(ContractError, "REPLAY_MISMATCH"):  # ... but not re-derivable
            replay((canonical(manifest) + "\n").encode("utf-8"), jsonl(records), ROOT, "content")

    def test_designating_an_ineligible_statement_is_rejected(self):
        def change(records):
            st = next(r for r in records if r["type"] == "ClaimStatement" and r["role"] == "MAP_FIELD_6")
            st["field_status"] = "DUPLICATE_ENTRIES"
        with self.assertRaisesRegex(ContractError, "INELIGIBLE_LINK_TARGET"):
            validate(self.tampered(change), self.ids)

    def test_same_text_without_backing_comparison_is_rejected(self):
        def change(records):
            next(r for r in records if r["type"] == "TargetAlignment")["claim_identity"] = "SAME_TEXT"
        with self.assertRaisesRegex(ContractError, "UNSUPPORTED_IDENTITY"):
            validate(self.tampered(change), self.ids)

    def test_unknown_label_is_rejected(self):
        def change(records):
            next(r for r in records if r["type"] == "TargetAlignment")["claim_identity"] = "SAME_CLAIM"
        with self.assertRaisesRegex(ContractError, "INVALID_LABEL"):
            validate(self.tampered(change), self.ids)

    def test_dangling_reference_is_rejected(self):
        def change(records):
            next(r for r in records if r["type"] == "ReviewScope")["refs"].append("urn:atlas:missing")
        with self.assertRaisesRegex(ContractError, "UNRESOLVED_REFERENCE"):
            validate(self.tampered(change), self.ids)


class ViewerTests(unittest.TestCase):
    """show verifies before rendering; --unverified renders under a banner."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        from atlas.claims.link import jsonl
        records = [load_json(line) for line in (RECEIPT / "records.jsonl").read_bytes().splitlines()]
        # Plausible false upgrades, re-hashed so the file is internally consistent.
        scope = next(r for r in records if r["type"] == "ReviewScope")
        scope["relation_to_finding_target"] = "REVIEWS_TARGET_CLAIM_FIELD"
        link = next(r for r in records if r["type"] == "ClaimLinkRun")
        link["dependency"]["syntax"] = "PASS"
        manifest = next(r for r in records if r["type"] == "ClaimLinkManifest")
        manifest["records_before_manifest_sha256"] = sha256(jsonl([r for r in records if r is not manifest]))
        self.tampered = Path(self.temp.name) / "records.jsonl"
        self.tampered.write_bytes(jsonl(records))
        self.records = records

    def cli(self, *args):
        return subprocess.run([sys.executable, "-m", "atlas.claims", "show", *args], cwd=ROOT,
                              capture_output=True, text=True)

    def test_tampered_file_still_passes_static_validation(self):
        validate(self.records, build(copy.deepcopy(CONTEXT), ROOT)["dependency_ids"])

    def test_verified_view_refuses_a_tampered_file(self):
        shown = self.cli(str(self.tampered))
        self.assertNotEqual(shown.returncode, 0)
        self.assertIn("NOT_VERIFIED", shown.stderr)
        self.assertIn("REPLAY_MISMATCH", shown.stderr)
        self.assertEqual(shown.stdout, "")

    def test_unverified_view_puts_its_banner_before_any_stored_label(self):
        shown = self.cli(str(self.tampered), "--unverified")
        self.assertEqual(shown.returncode, 0, shown.stderr)
        out = shown.stdout
        self.assertTrue(out.startswith("=" * 10))
        banner = out.index("UNVERIFIED RENDERING OF STORED ASSERTIONS")
        for label in ("syntax PASS", "REVIEWS_TARGET_CLAIM_FIELD", "native projection VERIFIED"):
            self.assertLess(banner, out.index(label), label)
        self.assertFalse(out.startswith("VERIFIED RENDERING"))
        self.assertNotIn("\nVERIFIED RENDERING", out)

    def test_verified_view_of_committed_receipt(self):
        shown = self.cli(str(RECEIPT / "records.jsonl"))
        self.assertEqual(shown.returncode, 0, shown.stderr)
        self.assertTrue(shown.stdout.startswith("VERIFIED RENDERING"))
        self.assertNotIn("UNVERIFIED", shown.stdout)

    def test_bundle_without_manifest_is_not_rendered_as_verified(self):
        path = Path(self.temp.name) / "no-manifest.jsonl"
        path.write_text("".join(canonical(r) + "\n" for r in self.records if r["type"] != "ClaimLinkManifest"),
                        encoding="utf-8")
        shown = self.cli(str(path))
        self.assertNotEqual(shown.returncode, 0)
        self.assertIn("NOT_VERIFIED", shown.stderr)
        self.assertEqual(shown.stdout, "")


class ParserTests(unittest.TestCase):
    def test_same_line_and_wrapped_text_with_each_dash(self):
        text = ("CLAIM MAP MISSING: x\n\nCLAIM MAP: SELF-GENERATED – PROVISIONAL\n"
                "- Field 1 - Measured: a b\n- Field 3 — Weaker:\n  c\n  d\n- Field 6 – Claim: e\n\nNEXT\n")
        parsed = standalone.parse(text)
        # Spans are exact, but these labels are not the instrument's, so each is reported.
        self.assertEqual({i["code"] for i in parsed["issues"]}, {"FIELD_LABEL_MISMATCH"})
        entries = {k: v[0] for k, v in parsed["map"]["entries"].items()}
        self.assertEqual({k: v["text"] for k, v in entries.items()}, {"1": "a b", "3": "c\n  d", "6": "e"})
        for item in entries.values():
            self.assertEqual(text[item["char_start"]:item["char_end"]], item["text"])
        good = ("CLAIM MAP MISSING: x\nCLAIM MAP: SELF-GENERATED — PROVISIONAL\n"
                "- Field 1 – What was literally measured: a\n- Field 3 - weaker defensible  claim:\n  c\n"
                "- Field 6 — Claim under audit: e\n")
        parsed = standalone.parse(good)
        self.assertEqual((parsed["map"]["state"], parsed["issues"]), ("PRESENT", []))
        self.assertEqual(parsed["map"]["entries"]["3"][0]["label_match"], "CASE_OR_SPACE_ONLY")

    def test_each_field_number_requires_its_own_label(self):
        labels = ("What was literally measured", "Weaker defensible claim", "Claim under audit")
        for number in ("1", "3", "6"):
            for label in labels:
                text = f"CLAIM MAP MISSING: x\nCLAIM MAP: SELF-GENERATED - PROVISIONAL\n- Field {number} - {label}: t\n"
                status = standalone.parse(text)["map"]["field_status"][number]
                expected = "USABLE" if standalone.EXPECTED_LABELS[number] == label else "LABEL_MISMATCH"
                self.assertEqual(status, expected, (number, label))

    def test_duplicates_keep_every_entry_in_order(self):
        text = ("CLAIM MAP MISSING: x\nCLAIM MAP: SELF-GENERATED - PROVISIONAL\n"
                "- Field 6 - Claim under audit: A\n- Field 6 - Claim under audit: not A\n")
        parsed = standalone.parse(text)
        self.assertEqual(parsed["map"]["field_status"]["6"], "DUPLICATE_ENTRIES")
        self.assertEqual([e["text"] for e in parsed["map"]["entries"]["6"]], ["A", "not A"])
        self.assertEqual(parsed["map"]["state"], "PRESENT_WITH_DEFECTS")

    def test_invented_field_and_missing_field_are_reported(self):
        text = ("CLAIM MAP MISSING: x\nCLAIM MAP: SELF-GENERATED - PROVISIONAL\n"
                "- Field 1 - What was literally measured: a\n- Field 2 - S: b\n")
        parsed = standalone.parse(text)
        self.assertEqual({i["code"] for i in parsed["issues"]}, {"FIELD_OUTSIDE_FALLBACK", "FALLBACK_FIELD_MISSING"})
        self.assertEqual(parsed["map"]["state"], "PRESENT_WITH_DEFECTS")

    def test_table_rows_are_not_headings(self):
        text = "| PRE-AUDIT CLAIM CONFIRMATION | yes |\n| CLAIM MAP: SELF-GENERATED - PROVISIONAL |\n"
        parsed = standalone.parse(text)
        self.assertEqual((parsed["map"]["state"], parsed["confirmation"]["state"]), ("ABSENT", "ABSENT"))

    def test_duplicate_heading_is_malformed(self):
        text = "CLAIM MAP: SELF-GENERATED - PROVISIONAL\n\nCLAIM MAP: SELF-GENERATED - PROVISIONAL\n"
        self.assertEqual(standalone.parse(text)["map"]["state"], "MALFORMED")

    def test_unicode_offsets_are_code_points(self):
        text = ("\U0001F600 CLAIM MAP MISSING: x\nCLAIM MAP: SELF-GENERATED - PROVISIONAL\n"
                "- Field 1 - M: µ a\n- Field 3 - W: b\n- Field 6 - C: c\n")
        item = standalone.parse(text)["map"]["entries"]["1"][0]
        self.assertEqual(text[item["char_start"]:item["char_end"]], "µ a")


if __name__ == "__main__":
    unittest.main()
