"""atlas.view audit page: one imported audit (AJR 2001), from verified map-link and challenge bundles.

The page must show no source text, must keep model-written text attributed, must show
every challenger's outcome where they disagree, must state its counts from the records,
and must render nothing when a bundle it relies on does not re-verify.
"""

from __future__ import annotations

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

from atlas.contract import ContractError, load_json, normalize  # noqa: E402
from atlas.view.labels import TABLE_ID  # noqa: E402
from atlas.view.pages import render_all  # noqa: E402

PAGES = ROOT / "docs/atlas/views/views.json"
OUT = "docs/atlas/views/ajr2001"
IMPORT = ROOT / "examples/research/acemoglu-colonial-origins/citation-network/atlas-receipt/records.jsonl"
CHALLENGE = ROOT / "tests/atlas/challenge/ajr2001/receipt"


def text_of(page: str) -> str:
    return normalize(html.unescape(re.sub(r"<[^>]+>", " ", page)))


class AuditPageTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.files = render_all(PAGES, ROOT)
        cls.view = json.loads(cls.files[OUT]["view.json"])
        cls.page = cls.files[OUT]["index.html"].decode("utf-8")
        cls.report = cls.files[OUT]["report.txt"].decode("utf-8")

    def test_committed_page_is_a_fresh_render(self):
        for name, data in self.files[OUT].items():
            self.assertEqual((ROOT / OUT / name).read_bytes(), data, name)

    def test_no_source_text_is_shown(self):
        passages = [load_json(l) for l in IMPORT.read_bytes().splitlines() if b'"Passage"' in l]
        self.assertEqual(len(passages), 20)
        for rendering in (text_of(self.page), normalize(self.report)):
            for p in passages:
                words = normalize(p["quote"]).split()
                for i in range(0, max(1, len(words) - 7)):
                    self.assertNotIn(" ".join(words[i:i + 8]), rendering, p["id"])
        self.assertTrue(self.view["passage_text_note"].startswith("No source text is shown."))

    def test_model_text_quoting_a_source_passage_is_withheld(self):
        from atlas.view.audit import Withholder
        self.assertEqual(self.view["withheld"], [{"where": "finding 4", "passages": ["NS-E1"]}])
        self.assertTrue(self.view["findings"][3]["title"].startswith("[Withheld here:"))
        self.assertIn("finding 4 (NS-E1)", self.view["passage_text_note"])
        guard = Withholder([{"native_id": "X-1", "quote": "one two three four five six seven eight nine"}])
        self.assertEqual(guard('He wrote "two three four five six seven eight nine".', "t")[:15], "[Withheld here:")
        self.assertEqual(guard("two three four five six seven eight", "t"), "two three four five six seven eight")
        self.assertEqual(guard.withheld, [{"where": "t", "passages": ["X-1"]}])

    def test_disagreement_shows_every_outcome(self):
        item1 = next(i for i in self.view["items"] if i["number"] == 1)
        self.assertTrue(item1["differ"])
        self.assertEqual({(c["challenger"], c["outcome"]["native"]) for c in item1["challenges"]},
                         {("ChatGPT/Codex", "CANNOT_DETERMINE"), ("ChatGPT (GPT-6)", "CONDITION_MET_WITH_QUALIFICATION")})
        self.assertEqual(self.page.count("The reviewers disagree on this item."), 1)
        self.assertEqual([i["differ"] for i in self.view["items"]], [True, False, False])

    def test_counts_come_from_the_records(self):
        run = next(load_json(l) for l in (CHALLENGE / "records.jsonl").read_bytes().splitlines()
                   if b'"ChallengeRun"' in l)
        c = run["counts"]
        page = text_of(self.page)
        self.assertIn(f"{c['items_with_a_decision_by_a_person']} of {c['items']} have a decision by a person", page)
        self.assertIn("20 of 20 match their retrieved copy word for word", page)
        self.assertIn("4 of 7 say they target something other than the claim under audit", page)
        self.assertEqual(len(self.view["findings"]), 7)
        self.assertEqual(len(self.view["sources"]), 12)

    def test_model_text_is_attributed_and_labels_are_declared(self):
        self.assertIn("Written by the claim map's producer, a model. Not the paper's words.", text_of(self.page))
        self.assertEqual(self.page.count("Written by a model run. Not the paper&#x27;s words."), 7)
        labels, keys = [], set()

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
        self.assertGreater(len(labels), 60)
        self.assertEqual({l["table"] for l in labels}, {TABLE_ID})
        for label in labels:
            self.assertIn(html.escape(label["native"]), self.page)

    def test_paper_page_says_no_question_record_exists(self):
        self.assertIn("No research question record exists for this paper yet. This page is a paper page.",
                      text_of(self.page))

    def test_links_resolve_and_page_is_self_contained(self):
        targets = set(re.findall(r'href="#(rec-[^"]+)"', self.page))
        ids = set(re.findall(r'id="(rec-[^"]+)"', self.page))
        self.assertTrue(targets)
        self.assertEqual(targets - ids, set())
        self.assertEqual(set(re.findall(r'(?:src|href)="https?://([^/"]+)', self.page)), {"fonts.googleapis.com"})
        self.assertNotIn("<script", self.page)
        self.assertNotIn("<img", self.page)


class AuditGuardTests(unittest.TestCase):
    def test_tampered_challenge_receipt_renders_nothing(self):
        with tempfile.TemporaryDirectory() as directory:
            receipt = Path(directory) / "receipt"
            receipt.mkdir()
            shutil.copyfile(CHALLENGE / "manifest.json", receipt / "manifest.json")
            data = (CHALLENGE / "records.jsonl").read_bytes()
            (receipt / "records.jsonl").write_bytes(data.replace(b'"CANNOT_DETERMINE"', b'"CONDITION_MET"'))
            spec = load_json(PAGES.read_bytes())
            for page in spec["pages"]:
                page["out"] = str(Path(directory) / "out" / page["id"])
                if page["kind"] == "audit":
                    page["challenge_receipt"] = str(receipt)
            pages = Path(directory) / "views.json"
            pages.write_text(json.dumps(spec), encoding="utf-8")
            run = subprocess.run([sys.executable, "-m", "atlas.view", "build-all", str(pages)],
                                 cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn("NOT_VERIFIED", run.stderr)
            self.assertFalse((Path(directory) / "out").exists())

    def test_bundles_must_pin_the_same_import(self):
        from atlas.view.audit import import_pins
        maplink = load_json((ROOT / "tests/atlas/maplink/ajr2001/receipt/manifest.json").read_bytes())
        challenge = load_json((CHALLENGE / "manifest.json").read_bytes())
        pins, _ = import_pins(maplink, challenge, ROOT)
        self.assertEqual(pins["records"]["sha256"], "5e8b7c167c3e41b1671223885a0b74d8f4e9817d104c3f8cef08b5da66e61a81")
        challenge["input_context"]["import_bundle"]["records"]["sha256"] = "0" * 64
        with self.assertRaisesRegex(ContractError, "AUDIT_RECEIPTS_DISAGREE"):
            import_pins(maplink, challenge, ROOT)

if __name__ == "__main__":
    unittest.main()
