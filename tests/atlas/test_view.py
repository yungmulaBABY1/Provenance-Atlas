"""Evidence view (atlas.view): the page and report are renderings of verified records.

Checks recording and presentation rules only: nothing renders from an unverified
bundle, every item resolves to a record, only public quotes are shown, labels keep
their native form, and no score or verdict is produced.
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
from atlas.extraction import output  # noqa: E402
from atlas.extraction.build import jsonl  # noqa: E402
from atlas.view import labels  # noqa: E402
from atlas.view.model import build_view, verify, view_json  # noqa: E402
from atlas.view.render import html_page, text_report  # noqa: E402

RECEIPT = ROOT / "tests/atlas/extraction/s2-run1/receipt"
VIEW_DIR = ROOT / "docs/atlas/views/s2-run1"
REDACTED = ROOT / "tests/atlas/extraction/s2-run1/output-redacted.md"


class CommittedViewTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.view = build_view(verify(RECEIPT, ROOT), ROOT)
        cls.page = html_page(cls.view)

    def test_committed_files_are_a_fresh_render(self):
        self.assertEqual((VIEW_DIR / "view.json").read_bytes(), view_json(self.view))
        self.assertEqual((VIEW_DIR / "index.html").read_text(encoding="utf-8"), self.page)
        self.assertEqual((VIEW_DIR / "report.txt").read_text(encoding="utf-8"), text_report(self.view))

    def test_only_public_quotes_are_shown(self):
        published = {normalize(a["quote"]["text"]) for a in output.parse(REDACTED.read_text(encoding="utf-8"))["anchors"]
                     if a["quote"]}
        shown = [normalize(html.unescape(q)) for q in re.findall(r"<blockquote[^>]*><p>(.*?)</p>", self.page, re.S)]
        self.assertEqual(len(shown), 5)
        self.assertTrue(set(shown) <= published)
        self.assertIn("43 quoted passages were checked", self.view["paper_says_note"])

    def test_claim_is_attributed_to_the_run_not_the_paper(self):
        self.assertIn("Not the paper's words", self.view["claim"]["written_by"])
        self.assertTrue(all(f["written_by"] == self.view["claim"]["written_by"] for f in self.view["run_findings"]))

    def test_every_translated_label_keeps_its_native_form(self):
        def walk(node):
            if isinstance(node, dict):
                if set(node) == {"native", "plain", "table"}:
                    yield node
                for value in node.values():
                    yield from walk(value)
            elif isinstance(node, list):
                for item in node:
                    yield from walk(item)
        found = list(walk(self.view))
        self.assertGreater(len(found), 20)
        for item in found:
            self.assertEqual(item["table"], labels.TABLE_ID)
            self.assertIn(html.escape(item["native"]), self.page)

    def test_no_score_or_verdict(self):
        keys = set()
        def walk(node):
            if isinstance(node, dict):
                keys.update(node)
                for v in node.values():
                    walk(v)
            elif isinstance(node, list):
                for v in node:
                    walk(v)
        walk(self.view)
        self.assertFalse({"score", "verdict", "credibility", "rating", "confidence"} & keys)
        self.assertIn("does not say whether this claim is true", self.page)

    def test_disagreement_and_missing_evidence_are_visible(self):
        dispositions = sorted(r["disposition"]["native"] for r in self.view["reviews"])
        self.assertEqual(dispositions, ["SUPPORTS", "SUPPORTS_WITH_QUALIFICATION"])
        missing = " ".join(m["item"] for m in self.view["missing"])
        for phrase in ("Supplemental Material", "not searched", "could not confirm", "not match the paper",
                       "No person has reviewed"):
            self.assertIn(phrase, missing)
        self.assertEqual([r["identity"]["native"] for r in self.view["related"]], ["NOT_THE_SAME_AUDIT_TARGET"])

    def test_page_links_resolve(self):
        targets = set(re.findall(r'href="#(rec-[^"]+)"', self.page))
        ids = set(re.findall(r'id="(rec-[^"]+)"', self.page))
        self.assertTrue(targets)
        self.assertEqual(targets - ids, set())

    def test_page_is_self_contained(self):
        hosts = set(re.findall(r'(?:src|href)="https?://([^/"]+)', self.page))
        self.assertEqual(hosts, {"fonts.googleapis.com"})
        self.assertNotIn("<img", self.page)


class GuardTests(unittest.TestCase):
    def test_tampered_bundle_renders_nothing(self):
        records = [load_json(l) for l in (RECEIPT / "records.jsonl").read_bytes().splitlines()]
        next(r for r in records if r["type"] == "EvidenceCheck")["result"] = "INCONSISTENT"
        manifest = next(r for r in records if r["type"] == "ExtractionManifest")
        manifest["records_before_manifest_sha256"] = sha256(jsonl([r for r in records if r is not manifest]))
        with tempfile.TemporaryDirectory() as directory:
            receipt = Path(directory) / "receipt"
            receipt.mkdir()
            shutil.copyfile(RECEIPT / "manifest.json", receipt / "manifest.json")
            (receipt / "records.jsonl").write_bytes(jsonl(records))
            with self.assertRaisesRegex(ContractError, "NOT_VERIFIED"):
                verify(receipt, ROOT)
            out = Path(directory) / "out"
            run = subprocess.run([sys.executable, "-m", "atlas.view", "build", str(receipt), str(out)],
                                 cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertFalse(out.exists())

    def test_stale_committed_view_is_detected(self):
        with tempfile.TemporaryDirectory() as directory:
            out = Path(directory)
            for name in ("view.json", "index.html", "report.txt"):
                shutil.copyfile(VIEW_DIR / name, out / name)
            (out / "report.txt").write_text("edited\n", encoding="utf-8")
            run = subprocess.run([sys.executable, "-m", "atlas.view", "check", str(RECEIPT), str(out)],
                                 cwd=ROOT, capture_output=True, text=True)
            self.assertNotEqual(run.returncode, 0)
            self.assertIn("VIEW_STALE", run.stderr)

    def test_untranslated_label_is_an_error(self):
        with self.assertRaisesRegex(ContractError, "UNTRANSLATED_LABEL"):
            labels.plain("SAME_CLAIM")
        with self.assertRaisesRegex(ContractError, "UNTRANSLATED_LABEL"):
            labels.plain("SUPPORTS", "independence")

    def test_unresolved_reference_is_an_error(self):
        from atlas.view.model import check_refs
        with self.assertRaisesRegex(ContractError, "VIEW_REF_UNRESOLVED"):
            check_refs({"claim": {"refs": ["urn:atlas:nowhere"]}}, {"urn:atlas:somewhere"})

    def test_content_is_escaped(self):
        view = build_view(verify(RECEIPT, ROOT), ROOT)
        hostile = copy.deepcopy(view)
        hostile["claim"]["text"] = "<script>alert(1)</script>"
        hostile["paper_says"][0]["text"] = "</p><img src=x onerror=alert(1)>"
        page = html_page(hostile)
        self.assertNotIn("<script>alert", page)
        self.assertNotIn("<img src=x", page)
        self.assertIn("&lt;script&gt;alert(1)&lt;/script&gt;", page)


if __name__ == "__main__":
    unittest.main()
