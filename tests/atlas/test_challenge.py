"""atlas.challenge: attributed decisions on the review items an imported audit leaves open.

The committed case is the AJR 2001 citation-network run, whose checker leaves three
items for human review. The committed receipt holds one challenge per item by each of
two separately run model reviewers, ChatGPT/Codex and ChatGPT (GPT-6), transcribed from
their pinned answers. They disagree on item 1; both outcomes are kept. Challenges
built in a temp tree below are synthetic: they exercise the record rules and are not
decisions about AJR 2001.
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
        by = {r["id"]: r for r in self.bundle["records"]}
        self.assertEqual([(i["item_number"], i["item_code"], i["challenge_state"],
                           [(by[o["challenge_id"]]["challenger"]["identity"], o["outcome"], o["decision_by"])
                            for o in i["outcomes"]]) for i in self.items],
                         [(1, "SOURCE_LOCK_TRUTH", "CHALLENGED",
                           [("ChatGPT/Codex", "CANNOT_DETERMINE", "MODEL_AGENT"),
                            ("ChatGPT (GPT-6)", "CONDITION_MET_WITH_QUALIFICATION", "MODEL_AGENT")]),
                          (2, "DIRECT_ADJUDICATION_SUBSTANCE", "CHALLENGED",
                           [("ChatGPT/Codex", "CONDITION_MET_WITH_QUALIFICATION", "MODEL_AGENT"),
                            ("ChatGPT (GPT-6)", "CONDITION_MET_WITH_QUALIFICATION", "MODEL_AGENT")]),
                          (3, "NESTING_SUBSTANCE", "CHALLENGED",
                           [("ChatGPT/Codex", "CONDITION_NOT_MET", "MODEL_AGENT"),
                            ("ChatGPT (GPT-6)", "CONDITION_NOT_MET", "MODEL_AGENT")])])
        run = next(r for r in self.bundle["records"] if r["type"] == "ChallengeRun")
        self.assertEqual(run["counts"], {
            "items": 3, "items_not_challenged": 0, "items_with_a_decision_by_a_person": 0, "challenges": 6,
            "challenges_detached": 0, "attached_by_outcome": {"CANNOT_DETERMINE": 1,
                                                              "CONDITION_MET_WITH_QUALIFICATION": 3,
                                                              "CONDITION_NOT_MET": 2}})
        self.assertEqual(run["checker"]["status"], "PASS-WITH-REVIEW")

    def test_the_reviewers_answers_are_transcribed_verbatim(self):
        sources = {"ChatGPT/Codex": ("chatgpt-codex-answer-2026-11-04.txt",
                                     "36dbb0c359c06794ef8eadce43f67c904fe0b2cc44cf5c14ce263e20d9c92e26"),
                   "ChatGPT (GPT-6)": ("chatgpt-gpt6-answer-2026-11-04.txt",
                                       "09267a8fc6422579c5a64312f694b8b92cb381e07575f279295754e34c66696d")}
        for name, digest in sources.values():
            self.assertEqual(sha256((CASE / "challenges/source" / name).read_bytes()), digest)
        challenges = [r for r in self.bundle["records"] if r["type"] == "Challenge"]
        self.assertEqual(len(challenges), 6)
        for c in challenges:
            name, digest = sources[c["challenger"]["identity"]]
            self.assertEqual(c["transcription"]["state"], "TEXT_FIELDS_FOUND_VERBATIM_IN_SOURCE")
            self.assertEqual(c["transcription"]["source"]["sha256"], digest)
            self.assertEqual(c["decision_by"], "MODEL_AGENT")
            self.assertEqual((c["relation_to_run"]["producer"], c["relation_to_run"]["atlas_code_author"]),
                             ("NO", "NO"))
            # Every outcome is a label on the reviewer's own first line for it.
            token = r"(?<![A-Z_]){}(?![A-Z_])"
            for part in c["parts"]:
                self.assertRegex(part["reasons"][0], token.format(part["outcome"]))
            self.assertRegex(c["reasons"][0], token.format(c["outcome"]))
        # GPT-6 gave per-part outcomes only for item 2; none are invented for items 1 and 3.
        gpt6 = {c["target"]["item_number"]: c for c in challenges if c["challenger"]["identity"] == "ChatGPT (GPT-6)"}
        self.assertEqual({n: len(c["parts"]) for n, c in gpt6.items()}, {1: 0, 2: 6, 3: 0})

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
        self.ctx["challenges"] = []  # the temp tree starts with no challenge on record
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
    def test_blank_tree_matches_a_blank_build_of_the_repository(self):
        self.assertEqual(content(self.blank["records"]), content(challenge.build(self.ctx, ROOT)["records"]))
        self.assertEqual({r["challenge_state"] for r in self.blank["records"] if r["type"] == "ReviewItem"},
                         {"NOT_CHALLENGED"})

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
                 "evidence kind": {"evidence": [{"kind": "OPINION", "text": "x"}]},
                 "file evidence fields": {"evidence": [{"kind": "FILE", "path": "x", "sha256": "0" * 64,
                                                        "verdict": "ok"}]}}
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

    def test_transcription_must_be_verbatim(self):
        source = self.root / "answers/source.txt"
        source.parent.mkdir()
        source.write_text("Reviewer says: the item text.\nreason one,\n  stated plainly.\nNONE_STATED\n", encoding="utf-8")
        pin = {"path": "answers/source.txt", "sha256": sha256(source.read_bytes())}
        bundle = self.add(self.artifact(1, reasons=["reason one, stated plainly."], transcribed_from=pin))
        c = next(r for r in bundle["records"] if r["type"] == "Challenge")
        self.assertEqual(c["transcription"]["state"], "TEXT_FIELDS_FOUND_VERBATIM_IN_SOURCE")
        self.assertEqual(c["transcription"]["checked_fields"], 3)
        self.ctx["challenges"] = []
        with self.assertRaisesRegex(ContractError, "TRANSCRIPTION_NOT_VERBATIM"):
            self.add(self.artifact(1, reasons=["reason one, stated clearly."], transcribed_from=pin))
        self.ctx["challenges"] = []
        bundle = self.add(self.artifact(1))
        self.assertEqual(next(r for r in bundle["records"] if r["type"] == "Challenge")["transcription"],
                         {"state": "NOT_A_TRANSCRIPTION"})

    def test_external_evidence_is_recorded_not_resolved(self):
        bundle = self.add(self.artifact(1, evidence=[{"kind": "EXTERNAL", "identifier": "NBER WP 9490",
                                                     "note": "Tables 1-2"}]))
        c = next(r for r in bundle["records"] if r["type"] == "Challenge")
        self.assertTrue(c["evidence"][0]["resolved"].startswith("NOT_RESOLVED_IN_BUILD"))

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

    def test_show_states_each_items_challenge(self):
        code, out, _ = self.run_cli("show", str(RECEIPT / "records.jsonl"), "--root", str(ROOT))
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("VERIFIED RENDERING"))
        self.assertEqual(out.count("[CHALLENGED]"), 3)
        self.assertIn("0 not challenged; 0 with a decision by a person", out)
        self.assertEqual(out.count("transcription: TEXT_FIELDS_FOUND_VERBATIM_IN_SOURCE"), 6)
        self.assertEqual(out.count("Challengers' outcomes differ:"), 1)

    def test_show_refuses_tampered_records(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "records.jsonl"
            path.write_bytes((RECEIPT / "records.jsonl").read_bytes().replace(b'"CONDITION_NOT_MET"', b'"CONDITION_MET"'))
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
