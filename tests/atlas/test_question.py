"""Research questions (atlas.question) and the question page (atlas.view.question).

These tests check recording and presentation rules only. The question bundle adds no
judgment: no record may carry a score, verdict, stance or position; every count is
recomputed from the member records with its denominator; a passage is attributed to
the source whose text it is, and a description of one source by another never appears
as the described source's own words; claim identity across sources may only be
declared and attributed. The page shows no source text and resolves every reference.
"""

import copy
import html
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from atlas.contract import ContractError, load_json, normalize, sha256  # noqa: E402
from atlas.question.build import build, jsonl, replay, validate  # noqa: E402
from atlas.view.pages import render_all  # noqa: E402

CONTEXT = ROOT / "tests/atlas/question/power-posing/context.json"
RECEIPT = ROOT / "tests/atlas/question/power-posing/receipt"
PAGES = ROOT / "docs/atlas/views/views.json"
QUESTION_OUT = "docs/atlas/views/power-posing"
PAPER_OUT = "docs/atlas/views/s2-run1"


def context() -> dict:
    return load_json(CONTEXT.read_bytes())


def stored() -> list[dict]:
    return [load_json(line) for line in (RECEIPT / "records.jsonl").read_bytes().splitlines() if line.strip()]


def rehash(records: list[dict]) -> list[dict]:
    manifest = next(r for r in records if r["type"] == "QuestionManifest")
    manifest["records_before_manifest_sha256"] = sha256(jsonl([r for r in records if r is not manifest]))
    return records


class BundleTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bundle = build(context(), ROOT)
        cls.by_type = {}
        for r in cls.bundle["records"]:
            cls.by_type.setdefault(r["type"], []).append(r)
        cls.members = {m["label"]: m for m in cls.by_type["QuestionMember"]}

    def test_committed_receipt_replays_and_build_is_deterministic(self):
        result = replay((RECEIPT / "manifest.json").read_bytes(), (RECEIPT / "records.jsonl").read_bytes(), ROOT,
                        "content")
        self.assertEqual(result["replay"], "PASS")
        self.assertEqual(build(context(), ROOT)["jsonl"], self.bundle["jsonl"])
        self.assertEqual((RECEIPT / "records.jsonl").read_bytes(), self.bundle["jsonl"])

    def test_counts_carry_their_denominator_and_recompute(self):
        cov = self.by_type["QuestionCoverage"][0]
        self.assertEqual(cov["denominator"], 4)
        counts = {r["id"]: (r["count"], r["members"]) for r in cov["rows"]}
        self.assertEqual(counts, {"retrieved": (2, ["S2", "S4"]), "passages": (2, ["S2", "S4"]),
                                  "described": (1, ["S3"]), "extraction": (1, ["S2"]),
                                  "imported-audit-target": (1, ["S1"]), "human": (0, [])})
        records = stored()
        next(r for r in records if r["type"] == "QuestionCoverage")["rows"][0]["count"] = 3
        with self.assertRaisesRegex(ContractError, "INVALID_COUNT"):
            validate(rehash(records), self.bundle["external_ids"])

    def test_no_judgment_field_can_be_recorded(self):
        for key, where in (("stance", "QuestionMember"), ("score", "QuestionCoverage"),
                           ("verdict", "ResearchQuestion"), ("position", "QuestionClaim")):
            records = stored()
            next(r for r in records if r["type"] == where)[key] = "SUPPORTS"
            with self.assertRaisesRegex(ContractError, "JUDGMENT_FIELD_NOT_ALLOWED"):
                validate(rehash(records), self.bundle["external_ids"])
        records = stored()
        next(r for r in records if r["type"] == "QuestionMember")["passages"][:0] = []
        member = next(r for r in records if r["type"] == "QuestionMember" and r["passages"])
        member["passages"][0]["rating"] = 5
        with self.assertRaisesRegex(ContractError, "JUDGMENT_FIELD_NOT_ALLOWED"):
            validate(rehash(records), self.bundle["external_ids"])

    def test_unretrieved_sources_are_metadata_only(self):
        for label in ("S1", "S3"):
            m = self.members[label]
            self.assertFalse(m["retrieved"])
            self.assertEqual(m["record_state"], "METADATA_ONLY")
            self.assertEqual(m["passages"], [])
            self.assertTrue(all(c["eligibility"] == "INELIGIBLE_MISSING_EVIDENCE" for c in m["checks"]))
        records = stored()
        next(r for r in records if r.get("label") == "S1")["record_state"] = "PASSAGES_ON_RECORD"
        with self.assertRaisesRegex(ContractError, "INVALID_LABEL"):
            validate(rehash(records), self.bundle["external_ids"])

    def test_described_by_another_source_is_never_the_described_source_own_words(self):
        s3, s4 = self.members["S3"], self.members["S4"]
        self.assertEqual(s3["passages"], [])
        self.assertEqual([(d["native_id"], d["speaker"]) for d in s3["described_in"]], [("S4-E2", "S4")])
        e2 = next(p for p in s4["passages"] if p["native_id"] == "S4-E2")
        self.assertEqual((e2["speaker"], e2["about"], e2["about_basis"]), ("S4", "S3", "S4-describes-S3"))
        # Moving S4's passage under S3 as if it were S3's text is rejected.
        records = stored()
        r4 = next(r for r in records if r.get("label") == "S4")
        r3 = next(r for r in records if r.get("label") == "S3")
        moved = next(p for p in r4["passages"] if p["native_id"] == "S4-E2")
        r3["passages"].append(copy.deepcopy(moved))
        with self.assertRaisesRegex(ContractError, "MISATTRIBUTED_PASSAGE"):
            validate(rehash(records), self.bundle["external_ids"])
        # Relabelling who wrote a passage, without moving it, is rejected.
        records = stored()
        r4 = next(r for r in records if r.get("label") == "S4")
        next(p for p in r4["passages"] if p["native_id"] == "S4-E3")["speaker"] = "S3"
        with self.assertRaisesRegex(ContractError, "MISATTRIBUTED_PASSAGE"):
            validate(rehash(records), self.bundle["external_ids"])
        # Dropping the subject on S4's side leaves S3's described_in unsupported.
        records = stored()
        r4 = next(r for r in records if r.get("label") == "S4")
        next(p for p in r4["passages"] if p["native_id"] == "S4-E2")["about"] = None
        with self.assertRaisesRegex(ContractError, "MISATTRIBUTED_PASSAGE"):
            validate(rehash(records), self.bundle["external_ids"])

    def test_passage_subject_needs_a_check_that_requires_that_passage(self):
        ctx = context()
        ctx["passage_subjects"][0]["basis_check"] = "S4-evidential-value"
        with self.assertRaisesRegex(ContractError, "SUBJECT_BASIS_INVALID"):
            build(ctx, ROOT)

    def test_claims_are_attributed_to_the_runs_that_wrote_them(self):
        claims = self.by_type["QuestionClaim"]
        self.assertEqual(sorted(c["target_member"] for c in claims), ["S1", "S2"])
        for c in claims:
            self.assertEqual(c["written_by"]["kind"], "MODEL_RUN")
            self.assertEqual([i["claim_identity"] for i in c["identity_records"]], ["NOT_THE_SAME_AUDIT_TARGET"])
        self.assertEqual(self.by_type["ResearchQuestion"][0]["claim_links"], [])

    def test_cross_source_claim_identity_must_be_declared_and_attributed(self):
        claim_ids = self.by_type["ResearchQuestion"][0]["claim_ids"]
        link = {"from_claim_id": claim_ids[0], "to_claim_id": claim_ids[1], "identity": "SAME_TEXT",
                "declared_by": "a reviewer", "basis": "looks the same"}
        ctx = context()
        ctx["claim_links"] = [link]
        with self.assertRaisesRegex(ContractError, "UNSUPPORTED_IDENTITY"):
            build(ctx, ROOT)
        ctx["claim_links"] = [{**link, "identity": "DECLARED_BY_REFERENCE", "declared_by": " "}]
        with self.assertRaisesRegex(ContractError, "declared_by|UNATTRIBUTED_CLAIM_LINK"):
            build(ctx, ROOT)
        ctx["claim_links"] = [{**link, "identity": "UNRESOLVED_REQUIRES_REVIEW"}]
        self.assertEqual(len([r for r in build(ctx, ROOT)["records"] if r["type"] == "ResearchQuestion"]), 1)

    def test_question_wording_is_attributed(self):
        q = self.by_type["ResearchQuestion"][0]
        self.assertEqual((q["wording"]["origin"], q["wording"]["operator_confirmation"]),
                         ("DRAFTED_BY_ASSISTANT", "NOT_CONFIRMED"))
        ctx = context()
        ctx["question"]["wording"]["origin"] = "DECLARED_BY_OPERATOR"
        with self.assertRaisesRegex(ContractError, "operator-declared wording"):
            build(ctx, ROOT)

    def test_members_must_come_from_the_pinned_import(self):
        ctx = context()
        ctx["corpus"]["members"][0]["work_id"] = "doi:10.0000/not-in-import"
        with self.assertRaisesRegex(ContractError, "MEMBER_NOT_IN_IMPORT"):
            build(ctx, ROOT)
        ctx = context()
        ctx["corpus"]["members"][0]["label"], ctx["corpus"]["members"][1]["label"] = "S2", "S1"
        with self.assertRaisesRegex(ContractError, "MEMBER_LABEL_MISMATCH"):
            build(ctx, ROOT)

    def test_pins_are_enforced(self):
        ctx = context()
        ctx["dependencies"]["extraction_receipts"][0]["records"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ContractError, "INPUT_HASH_MISMATCH"):
            build(ctx, ROOT)
        # A different file with a correct hash is still not the context the import run recorded.
        other = "tests/atlas/power-sources.json"
        ctx = context()
        ctx["dependencies"]["import_context"] = {"path": other, "sha256": sha256((ROOT / other).read_bytes())}
        with self.assertRaisesRegex(ContractError, "IMPORT_CONTEXT_MISMATCH"):
            build(ctx, ROOT)


class PageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = render_all(PAGES, ROOT)
        cls.view = json.loads(cls.files[QUESTION_OUT]["view.json"])
        cls.page = cls.files[QUESTION_OUT]["index.html"].decode("utf-8")
        cls.report = cls.files[QUESTION_OUT]["report.txt"].decode("utf-8")
        cls.paper = cls.files[PAPER_OUT]["index.html"].decode("utf-8")

    def test_committed_pages_are_a_fresh_render(self):
        for name, data in self.files[QUESTION_OUT].items():
            self.assertEqual((ROOT / QUESTION_OUT / name).read_bytes(), data, name)

    def test_no_source_text_is_shown(self):
        bundle = load_json((ROOT / "tests/atlas/power-sources-reviewed.json").read_bytes())
        text = normalize(html.unescape(re.sub(r"<[^>]+>", " ", self.page)))
        for p in bundle["passages"]:
            words = normalize(p["quote"]).split()
            for i in range(0, max(1, len(words) - 7)):
                self.assertNotIn(" ".join(words[i:i + 8]), text, p["id"])
        self.assertIn("not shown here", self.view["passage_text_note"])

    def test_counts_on_the_page_name_their_denominator(self):
        for row in self.view["coverage"]:
            self.assertEqual(row["denominator"], 4)
            self.assertIn(f"{row['count']} of 4", self.page)

    def test_described_passage_sits_under_its_speaker(self):
        s3 = next(s for s in self.view["sources"] if s["label"] == "S3")
        self.assertEqual(s3["passages"], [])
        self.assertEqual([(d["native_id"], d["speaker"]) for d in s3["described_in"]], [("S4-E2", "S4")])
        self.assertIn("S4’s words about S3, not S3’s own.", self.page)

    def test_no_score_or_verdict_and_labels_keep_native_form(self):
        keys = set()
        labels = []
        def walk(node):
            if isinstance(node, dict):
                keys.update(node)
                if set(node) == {"native", "plain", "table"}:
                    labels.append(node)
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)
        walk(self.view)
        self.assertFalse({"score", "verdict", "credibility", "rating", "stance", "position"} & keys)
        self.assertGreater(len(labels), 30)
        for item in labels:
            self.assertIn(html.escape(item["native"]), self.page)
        self.assertIn("Atlas does not answer this question", self.page)

    def test_links_resolve(self):
        targets = set(re.findall(r'href="#((?:rec|src)-[^"]+)"', self.page))
        ids = set(re.findall(r'id="((?:rec|src)-[^"]+)"', self.page))
        self.assertTrue(targets)
        self.assertEqual(targets - ids, set())
        pages = set(re.findall(r'href="(\.\./[^"#]+)"', self.page))
        self.assertEqual(pages, {"../s2-run1/index.html"})
        for target in pages:
            self.assertTrue((ROOT / QUESTION_OUT / target).resolve().is_file())

    def test_drill_down_keeps_the_declared_corpus(self):
        self.assertIn('href="../power-posing/index.html"', self.paper)
        self.assertIn("one of 4 declared sources", self.paper)
        paper_view = json.loads(self.files[PAPER_OUT]["view.json"])
        self.assertEqual(paper_view["context"]["denominator"], len(self.view["sources"]))
        self.assertEqual(paper_view["context"]["member_label"], "S2")

    def test_page_is_self_contained(self):
        hosts = set(re.findall(r'(?:src|href)="https?://([^/"]+)', self.page))
        self.assertEqual(hosts, {"fonts.googleapis.com"})
        self.assertNotIn("<img", self.page)


class GuardTests(unittest.TestCase):
    def test_tampered_question_receipt_renders_nothing(self):
        records = stored()
        member = next(r for r in records if r.get("label") == "S1")
        member["retrieved"] = True
        member["record_state"] = "RETRIEVED_NO_PASSAGES"
        cov = next(r for r in records if r["type"] == "QuestionCoverage")
        row = next(r for r in cov["rows"] if r["id"] == "retrieved")
        row.update(count=3, members=["S1", "S2", "S4"])
        row["refs"] = [f"urn:atlas:question:power-posing:1/member/{m}" for m in row["members"]]
        rehash(records)
        with tempfile.TemporaryDirectory() as directory:
            receipt = Path(directory) / "receipt"
            receipt.mkdir()
            shutil.copyfile(RECEIPT / "manifest.json", receipt / "manifest.json")
            (receipt / "records.jsonl").write_bytes(jsonl(records))
            spec = load_json(PAGES.read_bytes())
            for page in spec["pages"]:
                page["out"] = str(Path(directory) / "out" / page["id"])
                if page["kind"] == "question":
                    page["receipt"] = str(receipt)
            pages = Path(directory) / "views.json"
            pages.write_text(json.dumps(spec), encoding="utf-8")
            run = subprocess.run([sys.executable, "-m", "atlas.view", "build-all", str(pages)],
                                 cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn("NOT_VERIFIED", run.stderr)
            self.assertFalse((Path(directory) / "out").exists())

    def test_link_to_a_record_no_member_holds_is_an_error(self):
        with tempfile.TemporaryDirectory() as directory:
            spec = load_json(PAGES.read_bytes())
            spec["pages"][0]["links"] = {"urn:atlas:nowhere": "s2-run1"}
            pages = Path(directory) / "views.json"
            pages.write_text(json.dumps(spec), encoding="utf-8")
            with self.assertRaisesRegex(ContractError, "VIEW_LINK_UNRESOLVED"):
                render_all(pages, ROOT)


if __name__ == "__main__":
    unittest.main()
