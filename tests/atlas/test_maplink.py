"""atlas.maplink: findings of an imported audit linked to a separately produced Stage-1 map.

The committed case is the AJR 2001 citation-network run: its output names an upstream
map (01_claim_extraction.md) instead of carrying one, so atlas.claims records CLAIM MAP
ABSENT. These tests check that the map is linked by text only, that its provenance is
stated as it is (no run prompt, no run receipt), and that nothing here can turn a text
difference, a mention or a MAP GAP into a claim identity.
"""

from __future__ import annotations

import copy
import io
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from atlas.contract import ContractError, canonical, load_json, sha256  # noqa: E402
from atlas.extraction import output as stage1  # noqa: E402
from atlas.maplink import build as maplink  # noqa: E402
from atlas.maplink.__main__ import main as cli  # noqa: E402

CASE = ROOT / "tests/atlas/maplink/ajr2001"
RECEIPT = CASE / "receipt"
AJR = "examples/research/acemoglu-colonial-origins"
POWER_CLAIMS = "tests/atlas/claims/receipts/power-posing-reviewed"


def context() -> dict:
    return load_json((CASE / "context.json").read_bytes())


def stored() -> list[dict]:
    return [load_json(line) for line in (RECEIPT / "records.jsonl").read_bytes().splitlines() if line.strip()]


def rehash(records: list[dict]) -> list[dict]:
    manifest = next(r for r in records if r["type"] == "MapLinkManifest")
    manifest["records_before_manifest_sha256"] = sha256(maplink.jsonl([r for r in records if r is not manifest]))
    return records


def content(records: list[dict]) -> dict:
    return {r["id"]: maplink.without_environment(r) for r in records}


class ReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundle = maplink.build(context(), ROOT)
        cls.by_id = {r["id"]: r for r in cls.bundle["records"]}
        cls.alignments = {r["finding_number"]: r for r in cls.bundle["records"] if r["type"] == "TargetAlignment"}
        cls.upstream = next(r for r in cls.bundle["records"] if r["type"] == "UpstreamMap")

    def test_committed_receipt_replays_and_build_is_deterministic(self):
        result = maplink.replay((RECEIPT / "manifest.json").read_bytes(), (RECEIPT / "records.jsonl").read_bytes(),
                                ROOT, "content")
        self.assertEqual(result["replay"], "PASS")
        self.assertEqual(maplink.build(context(), ROOT)["jsonl"], self.bundle["jsonl"])
        self.assertEqual(content(stored()), content(self.bundle["records"]))
        self.assertEqual(not result["environment_delta"],
                         (RECEIPT / "records.jsonl").read_bytes() == self.bundle["jsonl"])

    def test_findings_against_the_map(self):
        identities = {n: a["claim_identity"] for n, a in self.alignments.items()}
        self.assertEqual(identities, {"1": "DECLARED_NOT_FIELD_6", "2": "DECLARED_NOT_FIELD_6",
                                      "3": "UNRESOLVED_REQUIRES_REVIEW", "4": "DECLARED_NOT_FIELD_6",
                                      "5": "UNRESOLVED_REQUIRES_REVIEW", "6": "DECLARED_NOT_FIELD_6",
                                      "7": "UNRESOLVED_REQUIRES_REVIEW"})
        self.assertEqual(self.alignments["3"]["map_gap_form"], "WORDING_DIFFERS_FROM_INSTRUMENT_FORMS")
        for n in ("5", "7"):
            comps = [self.by_id[c] for c in self.alignments[n]["comparison_ids"]]
            self.assertEqual([c["result"] for c in comps], ["MISMATCH"])
            self.assertEqual(comps[0]["semantic_equivalence"], "UNASSESSED")
        # atlas.claims' own labels are carried, not rewritten.
        self.assertEqual({a["claim_link_identity"] for n, a in self.alignments.items() if n not in ("5", "7")},
                         {"DECLARED_NOT_ON_MAP"})

    def test_a_field_mention_is_never_the_target(self):
        mentions = self.alignments["4"]["field_mentions"]
        self.assertEqual([m["field"] for m in mentions], ["4"])
        self.assertEqual(self.alignments["4"]["claim_identity"], "DECLARED_NOT_FIELD_6")
        self.assertNotIn(mentions[0]["map_statement_id"], self.alignments["4"]["comparison_ids"])

    def test_reconciliation_is_text_only(self):
        recs = [r for r in self.bundle["records"] if r["type"] == "Reconciliation"]
        self.assertEqual({r["field"]: (r["state"], r["claim_identity"]) for r in recs},
                         {f: ("TEXT_COMPARED", "UNRESOLVED_REQUIRES_REVIEW") for f in ("1", "3", "6")})

    def test_provenance_is_stated_as_it_is(self):
        prov = self.upstream["provenance"]
        self.assertEqual((prov["run_prompt"], prov["run_receipt"]), ("NOT_RECORDED", "NONE"))
        self.assertEqual(prov["producer"]["verification"], "SELF_REPORTED_NOT_INDEPENDENTLY_VERIFIED")
        self.assertEqual(self.upstream["audit_output_reference"]["state"], "PATH_NAMED_IN_AUDIT_OUTPUT")
        self.assertEqual(self.upstream["audit_output_reference"]["lines"], [5])
        self.assertEqual(self.upstream["preflight"]["blob_named"], "NAMED_MATCHES_PINNED_INSTRUMENT")
        self.assertTrue(self.upstream["anchors"]["verification"].startswith("NOT_VERIFIED_IN_ATLAS"))
        run = next(r for r in self.bundle["records"] if r["type"] == "MapLinkRun")
        self.assertEqual(run["source_statement"]["state"], "MAP_PRODUCER_RESTATEMENT_ONLY")
        for st in (r for r in self.bundle["records"] if r["type"] == "MapStatement"):
            self.assertEqual(st["statement_kind"], "UPSTREAM_MAP_TEXT")
            self.assertEqual(st["written_by"]["producer"]["kind"], "MODEL_AGENT")
            self.assertEqual(st["written_by"]["run_receipt"], "NONE")

    def test_source_anchor_quotes_are_not_copied(self):
        text = (ROOT / AJR / "01_claim_extraction.md").read_text(encoding="utf-8")
        quotes = [a["quote"]["text"] for a in stage1.parse(text)["anchors"] if a["quote"]]
        self.assertEqual(len(quotes), 18)
        payload = self.bundle["jsonl"].decode("utf-8")
        for quote in quotes:
            self.assertNotIn(quote, payload)

    def test_no_judgment_field_anywhere(self):
        self.assertEqual([maplink.forbidden_keys(r) for r in self.bundle["records"] if maplink.forbidden_keys(r)], [])


class ValidateTests(unittest.TestCase):
    """Edited copies of the committed records, re-hashed so only the edit is under test."""

    def edit(self, change):
        records = stored()
        change({r["id"]: r for r in records})
        return rehash(records)

    def external(self):
        return maplink.build(context(), ROOT)["external_ids"]

    def rejects(self, pattern, change):
        with self.assertRaisesRegex(ContractError, pattern):
            maplink.validate(self.edit(change), self.external())

    def test_text_difference_cannot_become_same_text(self):
        self.rejects("UNSUPPORTED_IDENTITY", lambda by: by[f"{context()['run']['id']}/alignment/finding-5"]
                     .update(claim_identity="SAME_TEXT"))

    def test_variant_gap_wording_cannot_be_read_as_a_form(self):
        self.rejects("UNSUPPORTED_IDENTITY", lambda by: by[f"{context()['run']['id']}/alignment/finding-3"]
                     .update(claim_identity="DECLARED_NOT_FIELD_6"))

    def test_mention_cannot_be_promoted_to_target(self):
        def change(by):
            by[f"{context()['run']['id']}/alignment/finding-4"]["field_mentions"][0]["relation"] = "TARGET"
        self.rejects("INVALID_LABEL", change)

    def test_reconciliation_identity_must_follow_its_comparison(self):
        self.rejects("UNSUPPORTED_IDENTITY", lambda by: by[f"{context()['run']['id']}/reconciliation/field-6"]
                     .update(claim_identity="SAME_TEXT"))

    def test_designated_target_must_be_the_field_6_section(self):
        rid = context()["run"]["id"]
        self.rejects("INELIGIBLE_LINK_TARGET", lambda by: by[f"{rid}/alignment/finding-5"]
                     .update(designated_target_id=f"{rid}/map-statement/table-field-6"))

    def test_provenance_cannot_claim_a_receipt(self):
        def change(by):
            by[f"{context()['run']['id']}/upstream-map"]["provenance"]["run_receipt"] = "urn:atlas:extraction:x"
        self.rejects("INVALID_LABEL", change)

    def test_map_statement_must_be_attributed(self):
        def change(by):
            st = by[f"{context()['run']['id']}/map-statement/table-field-2"]
            st["written_by"] = {"basis": "SOURCE"}
        self.rejects("UNATTRIBUTED_MAP_STATEMENT", change)

    def test_no_judgment_field(self):
        self.rejects("JUDGMENT_FIELD_NOT_ALLOWED", lambda by: by[f"{context()['run']['id']}/alignment/finding-1"]
                     .update(verdict="SURVIVES"))

    def test_consistent_relabel_is_caught_by_replay(self):
        rid = context()["run"]["id"]
        records = self.edit(lambda by: by[f"{rid}/alignment/finding-1"].update(
            map_gap_form="NOT_ON_MAP", claim_identity="DECLARED_NOT_ON_MAP"))
        maplink.validate(records, self.external())
        manifest = next(r for r in records if r["type"] == "MapLinkManifest")
        with self.assertRaisesRegex(ContractError, "REPLAY_MISMATCH"):
            maplink.replay((canonical(manifest) + "\n").encode("utf-8"), maplink.jsonl(records), ROOT, "content")


class GapFormTests(unittest.TestCase):
    def test_instrument_forms_match_as_written(self):
        self.assertTrue(maplink.GAP_NOT_ON_MAP.fullmatch(
            "MAP GAP: this finding concerns X, which does not appear on the claim map. The map may be incomplete."))
        self.assertTrue(maplink.GAP_NOT_FIELD_6.fullmatch("MAP GAP: this finding targets X, not map field 6."))
        self.assertIsNone(maplink.GAP_NOT_FIELD_6.fullmatch(
            "MAP GAP: this finding targets X, not map field 6 itself."))


class GuardTests(unittest.TestCase):
    """Inputs changed in a temp copy of exactly the files the receipt depends on."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        ctx = context()
        claims = load_json((ROOT / ctx["claim_link_bundle"]["manifest"]["path"]).read_bytes())
        dep = claims["input_context"]["dependency"]
        for path in (ctx["claim_link_bundle"]["manifest"]["path"], ctx["claim_link_bundle"]["records"]["path"],
                     dep["manifest"]["path"], dep["records"]["path"], ctx["upstream_map"]["output"]["path"],
                     ctx["upstream_map"]["instrument"]["path"]):
            dest = self.root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / path, dest)
        self.ctx = ctx
        self.map_path = self.root / ctx["upstream_map"]["output"]["path"]

    def build(self, root=None):
        return maplink.build(self.ctx, root or self.root)

    def test_temp_tree_builds_the_committed_records(self):
        self.assertEqual(content(self.build()["records"]), content(stored()))

    def test_receipted_run_belongs_in_atlas_extraction(self):
        self.ctx["upstream_map"]["run_prompt"] = {"path": "prompts/1-claim-extraction.txt", "sha256": "0" * 64}
        with self.assertRaisesRegex(ContractError, "RECEIPTED_RUN_NOT_SUPPORTED"):
            self.build()

    def test_map_must_match_its_pin(self):
        self.map_path.write_text(self.map_path.read_text(encoding="utf-8") + "\n", encoding="utf-8")
        with self.assertRaisesRegex(ContractError, "INPUT_HASH_MISMATCH"):
            self.build()

    def test_claim_link_receipt_is_replayed_not_trusted(self):
        path = self.root / self.ctx["claim_link_bundle"]["records"]["path"]
        path.write_bytes(path.read_bytes().replace(b'"DECLARED_NOT_ON_MAP"', b'"UNRESOLVED_REQUIRES_REVIEW"', 1))
        self.ctx["claim_link_bundle"]["records"]["sha256"] = sha256(path.read_bytes())
        with self.assertRaisesRegex(ContractError, "CLAIM_LINK_RECEIPT_NOT_VERIFIED"):
            self.build()

    def test_map_must_be_about_the_audit_target(self):
        self.ctx["upstream_map"]["work_id"] = "doi:10.1257/aer.102.6.3077"
        with self.assertRaisesRegex(ContractError, "UPSTREAM_MAP_TARGET_MISMATCH"):
            self.build()

    def test_map_instrument_must_be_the_contract_the_links_used(self):
        other = self.root / "prompts/other-claim-extraction.txt"
        other.write_bytes((self.root / "prompts/1-claim-extraction.txt").read_bytes() + b"\n")
        self.ctx["upstream_map"]["instrument"] = {"path": "prompts/other-claim-extraction.txt",
                                                  "sha256": sha256(other.read_bytes())}
        with self.assertRaisesRegex(ContractError, "CONTRACT_PIN_MISMATCH"):
            self.build()

    def test_output_with_its_own_map_is_out_of_scope(self):
        manifest = ROOT / POWER_CLAIMS / "manifest.json"
        records = ROOT / POWER_CLAIMS / "records.jsonl"
        run_id = next(load_json(l)["id"] for l in records.read_bytes().splitlines() if b'"ClaimLinkRun"' in l)
        self.ctx["claim_link_bundle"] = {
            "claim_link_run_id": run_id,
            "manifest": {"path": f"{POWER_CLAIMS}/manifest.json", "sha256": sha256(manifest.read_bytes())},
            "records": {"path": f"{POWER_CLAIMS}/records.jsonl", "sha256": sha256(records.read_bytes())}}
        with self.assertRaisesRegex(ContractError, "OUTPUT_HAS_ITS_OWN_MAP"):
            self.build(ROOT)

    def test_unnamed_map_is_labelled_declared_only(self):
        moved = self.root / "elsewhere/map.md"
        moved.parent.mkdir()
        shutil.copyfile(self.map_path, moved)
        self.ctx["upstream_map"]["output"] = {"path": "elsewhere/map.md", "sha256": sha256(moved.read_bytes())}
        up = next(r for r in self.build()["records"] if r["type"] == "UpstreamMap")
        self.assertEqual(up["audit_output_reference"]["state"], "NOT_NAMED_LINK_DECLARED_IN_CONTEXT_ONLY")
        self.assertTrue(up["audit_output_reference"]["basis"].startswith("DECLARED by "))

    def test_identical_text_is_recorded_as_same_text(self):
        """If the map's Field 6 statement were the audit's restatement word for word."""
        claims = [load_json(l) for l in (self.root / self.ctx["claim_link_bundle"]["records"]["path"])
                  .read_bytes().splitlines() if l.strip()]
        restated = next(r["exact_text"] for r in claims if r.get("role") == "CONFIRMATION_FIELD_6")
        text = self.map_path.read_text(encoding="utf-8")
        old = stage1.parse(text)["field_6_section"]["text"]
        self.assertEqual(text.count(old), 1)
        self.map_path.write_text(text.replace(old, restated), encoding="utf-8")
        self.ctx["upstream_map"]["output"]["sha256"] = sha256(self.map_path.read_bytes())
        records = self.build()["records"]
        by_number = {r["finding_number"]: r for r in records if r["type"] == "TargetAlignment"}
        self.assertEqual((by_number["5"]["claim_identity"], by_number["7"]["claim_identity"]),
                         ("SAME_TEXT", "SAME_TEXT"))
        rec6 = next(r for r in records if r["type"] == "Reconciliation" and r["field"] == "6")
        self.assertEqual(rec6["claim_identity"], "SAME_TEXT")
        self.assertEqual(by_number["1"]["claim_identity"], "DECLARED_NOT_FIELD_6")


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = cli(list(args))
        return code, out.getvalue(), err.getvalue()

    def test_show_verifies_before_rendering(self):
        code, out, _ = self.run_cli("show", str(RECEIPT / "records.jsonl"), "--root", str(ROOT))
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("VERIFIED RENDERING"))
        for needle in ("PATH_NAMED_IN_AUDIT_OUTPUT", "run prompt NOT_RECORDED; run receipt NONE",
                       "the audit output's restatement (line 13):", "not a score"):
            self.assertIn(needle, out)

    def test_show_refuses_tampered_records(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "records.jsonl"
            path.write_bytes((RECEIPT / "records.jsonl").read_bytes().replace(b"DECLARED_NOT_FIELD_6",
                                                                              b"DECLARED_NOT_ON_MAP", 1))
            code, out, err = self.run_cli("show", str(path), "--root", str(ROOT))
        self.assertEqual(code, 2)
        self.assertEqual(out, "")
        self.assertIn("NOT_VERIFIED", err)


if __name__ == "__main__":
    unittest.main()
