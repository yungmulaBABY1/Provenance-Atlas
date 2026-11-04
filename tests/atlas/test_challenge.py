"""atlas.challenge: attributed decisions on the review items an imported audit leaves open.

The committed case is the AJR 2001 citation-network run, whose checker leaves three
items for human review. No challenge has been made, so the committed receipt records
all three as NOT_CHALLENGED. Challenges in these tests are synthetic artifacts written
into a temp tree: they exercise the record rules and are not decisions about AJR 2001.
"""

from __future__ import annotations

import copy
import io
import json
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path
import shutil
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from atlas.challenge import build as challenge  # noqa: E402
from atlas.challenge.__main__ import main as cli, template  # noqa: E402
from atlas.contract import ContractError, canonical, load_json, sha256  # noqa: E402

CASE = ROOT / "tests/atlas/challenge/ajr2001"
RECEIPT = CASE / "receipt"


def context() -> dict:
    return load_json((CASE / "context.json").read_bytes())


def stored() -> list[dict]:
    return [load_json(line) for line in (RECEIPT / "records.jsonl").read_bytes().splitlines() if line.strip()]


def content(records: list[dict]) -> dict:
    return {r["id"]: challenge.without_environment(r) for r in records}


def rehash(records: list[dict]) -> list[dict]:
    manifest = next(r for r in records if r["type"] == "ChallengeManifest")
    manifest["records_before_manifest_sha256"] = sha256(challenge.jsonl([r for r in records if r is not manifest]))
    return records


class ReceiptTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundle = challenge.build(context(), ROOT)
        cls.items = [r for r in cls.bundle["records"] if r["type"] == "ReviewItem"]

    def test_committed_receipt_replays_and_build_is_deterministic(self):
        result = challenge.replay((RECEIPT / "manifest.json").read_bytes(), (RECEIPT / "records.jsonl").read_bytes(),
                                  ROOT, "content")
        self.assertEqual(result["replay"], "PASS")
        self.assertEqual(challenge.build(context(), ROOT)["jsonl"], self.bundle["jsonl"])
        self.assertEqual(content(stored()), content(self.bundle["records"]))
        self.assertEqual(not result["environment_delta"],
                         (RECEIPT / "records.jsonl").read_bytes() == self.bundle["jsonl"])

    def test_three_items_each_with_a_stated_state(self):
        self.assertEqual([(i["item_number"], i["item_code"], i["challenge_state"]) for i in self.items],
                         [(1, "SOURCE_LOCK_TRUTH", "NOT_CHALLENGED"),
                          (2, "DIRECT_ADJUDICATION_SUBSTANCE", "NOT_CHALLENGED"),
                          (3, "NESTING_SUBSTANCE", "NOT_CHALLENGED")])
        run = next(r for r in self.bundle["records"] if r["type"] == "ChallengeRun")
        self.assertEqual(run["counts"], {"items": 3, "items_not_challenged": 3, "items_with_a_decision_by_a_person": 0,
                                         "challenges": 0, "challenges_detached": 0, "attached_by_outcome": {}})
        self.assertEqual(run["checker"]["status"], "PASS-WITH-REVIEW")

    def test_items_are_the_checkers_own_lines(self):
        for item in self.items:
            self.assertTrue(item["text"].startswith(f"REVIEW_ITEM_{item['item_number']}\t{item['item_code']} — "))
            self.assertEqual(sha256(item["text"].encode("utf-8")), item["text_sha256"])


class TreeCase(unittest.TestCase):
    """A temp copy of exactly what the import replay and the checker need, plus artifacts."""

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.ctx = context()
        pins = self.ctx["import_bundle"]
        imported = load_json((ROOT / pins["manifest"]["path"]).read_bytes())["input_context"]
        baseline = load_json((ROOT / "atlas/baseline.json").read_bytes())
        paths = {pins["manifest"]["path"], pins["records"]["path"], imported["output"]["path"],
                 *[a["path"] for a in imported["declared_inputs"]], *baseline["files"]}
        for path in paths:
            dest = self.root / path
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / path, dest)
        self.blank = challenge.build(self.ctx, self.root)

    def artifact(self, number=1, **changes) -> dict:
        art = template(self.blank, number)
        art.update(challenge_id=f"test-item-{number}", challenger={
            "identity": "Test Person", "kind": "PERSON", "context": "unit test; not a decision about AJR 2001"},
            relation_to_run={"producer": "NO", "atlas_code_author": "NO", "basis": "DECLARED_BY_CHALLENGER"},
            recorded_by="unit test", performed_at="2026-11-04",
            exposure={"seen_before_deciding": ["the item text"], "prior_position": "NONE_STATED"},
            outcome="CANNOT_DETERMINE", reasons=["synthetic reason"])
        for key, value in changes.items():
            art[key] = value
        return art

    def add(self, *arts) -> dict:
        for index, art in enumerate(arts):
            path = self.root / f"challenges/{index}-{art['challenge_id']}.json"
            path.parent.mkdir(exist_ok=True)
            path.write_text(json.dumps(art, ensure_ascii=False, indent=1), encoding="utf-8")
            self.ctx["challenges"].append({"path": str(path.relative_to(self.root)), "sha256": sha256(path.read_bytes())})
        return challenge.build(self.ctx, self.root)


class ChallengeTests(TreeCase):
    def test_blank_tree_matches_the_committed_receipt(self):
        self.assertEqual(content(self.blank["records"]), content(stored()))

    def test_a_matching_challenge_attaches_and_changes_nothing_else(self):
        bundle = self.add(self.artifact(2, outcome="CONDITION_MET_WITH_QUALIFICATION",
                                        parts=[{"part": "source A", "outcome": "CONDITION_NOT_MET", "reasons": ["r"]}]))
        by = {r["id"]: r for r in bundle["records"]}
        item = by[f"{self.ctx['run']['id']}/item/2"]
        self.assertEqual(item["challenge_state"], "CHALLENGED")
        self.assertEqual(item["outcomes"][0]["outcome"], "CONDITION_MET_WITH_QUALIFICATION")
        for n in (1, 3):
            self.assertEqual(by[f"{self.ctx['run']['id']}/item/{n}"]["challenge_state"], "NOT_CHALLENGED")
        run = next(r for r in bundle["records"] if r["type"] == "ChallengeRun")
        self.assertEqual(run["counts"]["items_with_a_decision_by_a_person"], 1)
        # The import's own records are not in this bundle and are not altered.
        self.assertFalse(any(r["type"] in ("AuditRun", "AuditFinding") for r in bundle["records"]))

    def test_two_disagreeing_challenges_are_both_kept(self):
        bundle = self.add(self.artifact(1, outcome="CONDITION_MET"),
                          self.artifact(1, challenge_id="test-item-1-b", outcome="CONDITION_NOT_MET",
                                        challenger={"identity": "Other", "kind": "MODEL_AGENT", "context": "test"}))
        item = next(r for r in bundle["records"] if r["type"] == "ReviewItem" and r["item_number"] == 1)
        self.assertEqual(sorted(o["outcome"] for o in item["outcomes"]), ["CONDITION_MET", "CONDITION_NOT_MET"])

    def test_changed_target_detaches_but_is_kept(self):
        art = self.artifact(3)
        art["target"]["item_text_sha256"] = "0" * 64
        bundle = self.add(art)
        item = next(r for r in bundle["records"] if r["type"] == "ReviewItem" and r["item_number"] == 3)
        self.assertEqual(item["challenge_state"], "NOT_CHALLENGED")
        self.assertEqual(len(item["detached_challenge_ids"]), 1)
        c = next(r for r in bundle["records"] if r["type"] == "Challenge")
        self.assertEqual((c["binding"], c["mismatched"]), ("TARGET_MISMATCH", ["item_text"]))

    def test_producer_cannot_decide(self):
        for rel, identity in (({"producer": "YES", "atlas_code_author": "NO", "basis": "x"}, "Someone"),
                              ({"producer": "NO", "atlas_code_author": "NO", "basis": "x"}, "Grok Bot (executor subagent)")):
            with self.subTest(identity=identity), self.assertRaisesRegex(ContractError, "PRODUCER_CANNOT_CHALLENGE"):
                self.ctx["challenges"] = []
                self.add(self.artifact(1, relation_to_run=rel, challenger={
                    "identity": identity, "kind": "MODEL_AGENT", "context": "test"}))

    def test_code_author_cannot_decide(self):
        for rel, identity in (({"producer": "NO", "atlas_code_author": "YES", "basis": "x"}, "Someone"),
                              ({"producer": "NO", "atlas_code_author": "NO", "basis": "x"}, self.ctx["code_author"]["identity"])):
            with self.subTest(identity=identity), self.assertRaisesRegex(ContractError, "CODE_AUTHOR_CANNOT_DECIDE"):
                self.ctx["challenges"] = []
                self.add(self.artifact(1, relation_to_run=rel, challenger={
                    "identity": identity, "kind": "MODEL_AGENT", "context": "test"}))

    def test_artifact_rules(self):
        cases = {"INVALID_LABEL": {"outcome": "SURVIVES"},
                 "at least one stated reason": {"reasons": []},
                 "JUDGMENT_FIELD_NOT_ALLOWED": {"parts": [{"part": "p", "outcome": "CONDITION_MET", "reasons": ["r"],
                                                           "score": 3}]},
                 "performed_at": {"performed_at": "yesterday"},
                 "evidence kind": {"evidence": [{"kind": "OPINION", "text": "x"}]}}
        for pattern, change in cases.items():
            with self.subTest(pattern=pattern), self.assertRaisesRegex(ContractError, pattern):
                self.ctx["challenges"] = []
                self.add(self.artifact(1, **change))

    def test_evidence_must_resolve(self):
        with self.assertRaisesRegex(ContractError, "EVIDENCE_UNRESOLVED"):
            self.add(self.artifact(1, evidence=[{"kind": "RECORD", "id": "urn:atlas:nothing"}]))
        self.ctx["challenges"] = []
        path = "examples/research/acemoglu-colonial-origins/citation-network/lock/section_E_lock_time.txt"
        bundle = self.add(self.artifact(1, evidence=[
            {"kind": "FILE", "path": path, "sha256": sha256((self.root / path).read_bytes()), "lines": [1, 1]},
            {"kind": "RECORD", "id": self.ctx["import_bundle"]["audit_run_id"]}]))
        c = next(r for r in bundle["records"] if r["type"] == "Challenge")
        self.assertEqual([e["resolved"] for e in c["evidence"]], ["FILE_PINNED", "RECORD_IN_IMPORT_BUNDLE"])

    def test_artifact_is_pinned(self):
        bundle = self.add(self.artifact(1))
        path = self.root / self.ctx["challenges"][0]["path"]
        path.write_text(path.read_text(encoding="utf-8").replace("CANNOT_DETERMINE", "CONDITION_MET"), encoding="utf-8")
        with self.assertRaisesRegex(ContractError, "INPUT_HASH_MISMATCH"):
            challenge.build(self.ctx, self.root)
        self.assertTrue(bundle)

    def test_import_receipt_is_replayed_not_trusted(self):
        path = self.root / self.ctx["import_bundle"]["records"]["path"]
        path.write_bytes(path.read_bytes().replace(b'"PASS-WITH-REVIEW"', b'"PASS"', 1))
        self.ctx["import_bundle"]["records"]["sha256"] = sha256(path.read_bytes())
        with self.assertRaisesRegex(ContractError, "IMPORT_RECEIPT_NOT_VERIFIED"):
            challenge.build(self.ctx, self.root)


class ValidateTests(TreeCase):
    def setUp(self):
        super().setUp()
        self.bundle = self.add(self.artifact(2), self.artifact(3, challenge_id="test-item-3-detached"))
        detached = self.root / self.ctx["challenges"][1]["path"]
        art = json.loads(detached.read_text(encoding="utf-8"))
        art["target"]["checker_sha256"] = "0" * 64
        detached.write_text(json.dumps(art), encoding="utf-8")
        self.ctx["challenges"][1]["sha256"] = sha256(detached.read_bytes())
        self.bundle = challenge.build(self.ctx, self.root)

    def rejects(self, pattern, change):
        records = copy.deepcopy(self.bundle["records"])
        change({r["id"]: r for r in records})
        with self.assertRaisesRegex(ContractError, pattern):
            challenge.validate(rehash(records), self.bundle["external_ids"])

    def item(self, by, n):
        return by[f"{self.ctx['run']['id']}/item/{n}"]

    def test_state_must_follow_challenges(self):
        self.rejects("challenge state", lambda by: self.item(by, 1).update(challenge_state="CHALLENGED"))
        self.rejects("challenge state", lambda by: self.item(by, 2).update(challenge_state="NOT_CHALLENGED"))

    def test_detached_challenge_cannot_be_attached(self):
        def change(by):
            item = self.item(by, 3)
            item["challenge_ids"] = item["detached_challenge_ids"]
            item["challenge_state"] = "CHALLENGED"
        self.rejects("DETACHED_CHALLENGE_ATTACHED", change)

    def test_item_outcome_must_be_the_challengers_own(self):
        def change(by):
            self.item(by, 2)["outcomes"][0]["outcome"] = "CONDITION_MET"
        self.rejects("outcomes are not its challenges", change)

    def test_counts_recompute(self):
        def change(by):
            run = by[self.ctx["run"]["id"]]
            run["counts"]["items_with_a_decision_by_a_person"] = 3
        self.rejects("INVALID_COUNT", change)

    def test_a_challenge_only_appends(self):
        def change(by):
            c = next(r for r in by.values() if r["type"] == "Challenge" and r["binding"] == "MATCH")
            c["effect"] = "REPLACES the finding"
        self.rejects("only appends", change)

    def test_relation_and_kind(self):
        def author(by):
            c = next(r for r in by.values() if r["type"] == "Challenge" and r["binding"] == "MATCH")
            c["relation_to_run"]["atlas_code_author"] = "YES"
        self.rejects("CODE_AUTHOR_CANNOT_DECIDE", author)

        def kind(by):
            c = next(r for r in by.values() if r["type"] == "Challenge" and r["binding"] == "MATCH")
            c["decision_by"] = "MODEL_AGENT"
        self.rejects("decision_by|outcomes are not its challenges", kind)

    def test_judgment_field(self):
        self.rejects("JUDGMENT_FIELD_NOT_ALLOWED", lambda by: self.item(by, 1).update(verdict="FINE"))


class CliTests(unittest.TestCase):
    def run_cli(self, *args):
        out, err = io.StringIO(), io.StringIO()
        with redirect_stdout(out), redirect_stderr(err):
            code = cli(list(args))
        return code, out.getvalue(), err.getvalue()

    def test_show_states_not_challenged(self):
        code, out, _ = self.run_cli("show", str(RECEIPT / "records.jsonl"), "--root", str(ROOT))
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("VERIFIED RENDERING"))
        self.assertEqual(out.count("[NOT_CHALLENGED]"), 3)
        self.assertIn("0 with a decision by a person", out)

    def test_show_refuses_tampered_records(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "records.jsonl"
            path.write_bytes((RECEIPT / "records.jsonl").read_bytes().replace(b'"NOT_CHALLENGED"', b'"CHALLENGED"', 1))
            code, out, err = self.run_cli("show", str(path), "--root", str(ROOT))
        self.assertEqual((code, out), (2, ""))
        self.assertIn("NOT_VERIFIED", err)

    def test_template_binds_the_exact_item(self):
        code, out, _ = self.run_cli("template", str(CASE / "context.json"), "2", "--root", str(ROOT))
        self.assertEqual(code, 0)
        target = json.loads(out)["target"]
        item = next(r for r in stored() if r["type"] == "ReviewItem" and r["item_number"] == 2)
        self.assertEqual((target["item_code"], target["item_text_sha256"]), (item["item_code"], item["text_sha256"]))


if __name__ == "__main__":
    unittest.main()
