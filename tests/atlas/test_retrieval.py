"""Locked queries recorded by code (atlas.retrieval): X1 controls.

These check recording: spec validation, canonical requests, digests, agreement
between declaration, executor log and committed response, sample redraws, live
attempt recording (with a fake opener; no network), drift and credential
handling. They do not check that any query was well chosen or that any result is
relevant.
"""

import copy
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
import urllib.error

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT))

from atlas.contract import ContractError  # noqa: E402
from atlas.retrieval import core, drift, live, sets  # noqa: E402

SET = ROOT / "tests/atlas/retrieval/baumeister-batch2/set.json"
SPEC = ROOT / "tests/atlas/retrieval/baumeister-batch2/specs/adj1-Q1.json"
SECRET = "test-key-0123456789abcdef"


def provenance14_search_digest(data) -> str:
    """Copy of search_digest in Provenance #14 (build_live_v2cand_fixture.py)."""
    def without(value):
        if isinstance(value, dict):
            return {k: without(v) for k, v in value.items() if k != "abstract_inverted_index"}
        if isinstance(value, list):
            return [without(v) for v in value]
        return value
    text = json.dumps(without(data), sort_keys=True, separators=(",", ":"), ensure_ascii=False)
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def spec():
    return json.loads(SPEC.read_text(encoding="utf-8"))


def response(ids, count=None, page=1):
    return {"meta": {"count": count if count is not None else len(ids), "page": page,
                     "per_page": 10, "db_response_time_ms": 5},
            "results": [{"id": f"https://openalex.org/{i}", "display_name": f"Title {i}",
                         "publication_year": 2000} for i in ids], "group_by": []}


class FakeOpener:
    def __init__(self, replies):
        self.replies = list(replies)
        self.calls = []

    def __call__(self, url, headers, timeout):
        self.calls.append((url, dict(headers)))
        reply = self.replies.pop(0)
        if isinstance(reply, Exception):
            raise reply
        status, body = reply
        return status, body if isinstance(body, bytes) else json.dumps(body).encode()


def run(replies, **kwargs):
    opener = FakeOpener(replies)
    record, data = live.run_live(spec(), "0" * 64, opener=opener, clock=lambda: "2026-11-05T00:00:00Z",
                                 sleep=lambda s: None, **kwargs)
    return record, data, opener


class SpecValidation(unittest.TestCase):
    def test_committed_specs_valid(self):
        data = sets.load_set(SET)
        self.assertEqual(len(sets.specs(SET, data)), 14)

    def reject(self, mutate, code="INVALID_SPEC"):
        s = spec()
        mutate(s)
        with self.assertRaises(ContractError) as ctx:
            core.validate_spec(s)
        self.assertIn(code, str(ctx.exception))

    def test_rejects_credentials(self):
        self.reject(lambda s: s["params"].append(["api_key", "x"]))
        self.reject(lambda s: s["params"].append(["mailto", "a@b.c"]))

    def test_rejects_paging_beyond_first(self):
        self.reject(lambda s: s["params"].append(["page", "2"]))
        self.reject(lambda s: s["params"].append(["cursor", "*"]))
        self.reject(lambda s: s.update(pages="all"))

    def test_rejects_bad_per_page(self):
        def drop(s):
            s["params"] = [p for p in s["params"] if p[0] != "per-page"]
        self.reject(drop)
        self.reject(lambda s: s["params"].append(["per_page", "10"]))
        def big(s):
            s["params"] = [[k, "500" if k == "per-page" else v] for k, v in s["params"]]
        self.reject(big)

    def test_rejects_other_hosts_and_missing_declaration(self):
        self.reject(lambda s: s.update(endpoint="https://example.org/works"))
        self.reject(lambda s: s["declared"].update(requires=[]))
        self.reject(lambda s: s.update(provenance="unknown"))


class CanonicalRequest(unittest.TestCase):
    def test_order_independent_and_credentials_excluded(self):
        s = spec()
        a = core.canonical_query(s["params"])
        b = core.canonical_query(list(reversed(s["params"])) + [["mailto", "x@y"], ["api_key", SECRET]])
        self.assertEqual(a, b)
        self.assertNotIn(SECRET, b)
        self.assertNotIn("mailto", b)

    def test_url_params_round_trip(self):
        s = spec()
        endpoint, params, creds = core.url_params(core.canonical_request(s) + "&mailto=a%40b")
        self.assertEqual(endpoint, s["endpoint"])
        self.assertEqual(sorted(map(tuple, params)), sorted(map(tuple, s["params"])))
        self.assertEqual(creds, ["mailto"])


class Digests(unittest.TestCase):
    def test_matches_provenance14_convention(self):
        data = json.loads((ROOT / "examples/research/baumeister-ego-depletion/citation-network-v2cand3/raw/"
                           "adj1_Q1.json").read_text(encoding="utf-8"))
        self.assertEqual(core.response_digest(data), provenance14_search_digest(data))

    def test_stripping_abstract_keeps_digest(self):
        a = response(["W1", "W2"])
        b = copy.deepcopy(a)
        a["results"][0]["abstract_inverted_index"] = {"word": [0]}
        b["results"][0]["abstract_inverted_index"] = "[abstract removed 2026-11-05; 1 words]"
        self.assertEqual(core.response_digest(a), core.response_digest(b))
        self.assertEqual(core.abstract_state(a), "PRESENT")
        self.assertEqual(core.abstract_state(b), "STRIPPED")
        self.assertEqual(core.abstract_state(response(["W1"])), "ABSENT")

    def test_results_digest_ignores_meta(self):
        a, b = response(["W1"]), response(["W1"])
        b["meta"]["db_response_time_ms"] = 999
        self.assertNotEqual(core.response_digest(a), core.response_digest(b))
        self.assertEqual(core.results_digest(a), core.results_digest(b))


class SavedRecords(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        run_dir = "examples/research/baumeister-ego-depletion"
        shutil.copytree(ROOT / run_dir, self.tmp / run_dir)
        shutil.copytree(SET.parent, self.tmp / "set")
        self.set = self.tmp / "set/set.json"

    def build(self):
        records, samples = sets.build_saved(self.tmp, self.set)
        return {r["id"].split("/")[1]: r for r in records}, samples

    def test_committed_outputs_current(self):
        self.assertEqual(sets.check(ROOT, SET), [])

    def test_all_consistent_and_one_reexecution(self):
        records, samples = self.build()
        self.assertTrue(all(r["status"] == "CONSISTENT" for r in records.values()))
        reexec = [k for k, r in records.items() if r["executor_log"]["re_executed_after_success"]]
        self.assertEqual(reexec, ["secE-F2"])
        self.assertTrue(samples[0]["positions_match_declared"] and samples[0]["ids_match_declared"])
        for r in records.values():
            self.assertEqual(r["retrieval_performed_by"], "executor")
            self.assertNotIn("grokbot", json.dumps(r))

    def test_changed_response_byte_detected(self):
        path = self.tmp / "examples/research/baumeister-ego-depletion/citation-network-v2cand3/raw/secE_F3.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["results"].reverse()
        path.write_text(json.dumps(data, indent=1), encoding="utf-8")
        records, _ = self.build()
        self.assertEqual(records["secE-F3"]["status"], "INCONSISTENT")
        self.assertIn("file_matches_logged_sha256", records["secE-F3"]["failed_checks"])

    def test_changed_declaration_detected(self):
        path = (self.tmp / "examples/research/baumeister-ego-depletion/citation-network-v2cand3/lock/"
                "ADJUDICATION-1_search_record.md")
        path.write_text(path.read_text(encoding="utf-8").replace("glucose", "fructose"), encoding="utf-8")
        records, _ = self.build()
        q3 = records["adj1-Q3"]
        self.assertIn("declared_file_sha256_matches", q3["failed_checks"])
        self.assertIn("declared_terms_in_declaration", q3["failed_checks"])
        self.assertIn("declared_file_sha256_matches", records["adj1-Q1"]["failed_checks"])

    def test_request_differing_from_declaration_detected(self):
        path = self.tmp / "set/specs/adj1-Q2.json"
        s = json.loads(path.read_text(encoding="utf-8"))
        s["params"] = [[k, v.replace("small-study", "small study") if k == "filter" else v]
                       for k, v in s["params"]]
        path.write_text(json.dumps(s), encoding="utf-8")
        records, _ = self.build()
        q2 = records["adj1-Q2"]
        self.assertIn("declared_terms_in_request", q2["failed_checks"])
        self.assertIn("request_matches_logged", q2["failed_checks"])

    def test_sample_redraw_with_other_seed_fails(self):
        data = json.loads(self.set.read_text(encoding="utf-8"))
        data["sample_checks"][0]["seed"] = 1
        self.set.write_text(json.dumps(data), encoding="utf-8")
        _, samples = self.build()
        self.assertFalse(samples[0]["positions_match_declared"])

    def test_stale_output_detected(self):
        report = self.tmp / "set/REPORT.txt"
        report.write_text(report.read_text(encoding="utf-8") + "x", encoding="utf-8")
        problems = sets.check(self.tmp, self.set)
        self.assertEqual(len(problems), 1)
        self.assertIn("STALE_OUTPUT", problems[0])

    def test_missing_log_entry_is_an_error(self):
        data = json.loads(self.set.read_text(encoding="utf-8"))
        data["items"][0]["log_file_key"] = "raw/not_there.json"
        self.set.write_text(json.dumps(data), encoding="utf-8")
        with self.assertRaises(ContractError):
            self.build()


class LiveRecording(unittest.TestCase):
    def test_success_on_first_attempt(self):
        record, data, opener = run([(200, response(["W1", "W2"]))])
        self.assertEqual(record["status"], "OK")
        self.assertEqual(record["retrieval_performed_by"].split()[0], "atlas.retrieval")
        self.assertEqual([r["id"] for r in record["response"]["ranked"]], ["W1", "W2"])
        self.assertEqual(len(opener.calls), 1)
        self.assertNotIn("mailto", opener.calls[0][0])
        self.assertNotIn("Authorization", opener.calls[0][1])

    def test_retries_only_429_and_5xx(self):
        record, _, opener = run([(429, b"slow"), (503, b"down"), (200, response(["W1"]))])
        self.assertEqual([a["status"] for a in record["attempts"]], [429, 503, 200])
        self.assertEqual(record["status"], "OK")
        record, _, opener = run([(403, b"no")])
        self.assertEqual(len(opener.calls), 1)
        self.assertEqual(record["status"], "FAILED")

    def test_policy_or_network_error_not_retried(self):
        record, _, opener = run([urllib.error.URLError("Tunnel connection failed: 403 Forbidden")])
        self.assertEqual(len(opener.calls), 1)
        self.assertEqual(record["attempts"][0]["outcome"], "NETWORK_ERROR")
        self.assertEqual(record["status"], "FAILED")
        self.assertIsNone(record["response"])

    def test_exhausted_retries_give_failure_record(self):
        record, _, opener = run([(429, b""), (429, b""), (429, b"")])
        self.assertEqual(len(opener.calls), 3)
        self.assertEqual(record["failed_checks"], ["no_successful_attempt"])

    def test_key_only_in_header_and_never_recorded(self):
        record, _, opener = run([urllib.error.URLError(f"failed with {SECRET}")], api_key=SECRET)
        url, headers = opener.calls[0]
        self.assertNotIn(SECRET, url)
        self.assertEqual(headers["Authorization"], f"Bearer {SECRET}")
        self.assertNotIn(SECRET, json.dumps(record))
        self.assertIn("value not recorded", record["request"]["credentials"])

    def test_invalid_json_recorded(self):
        record, _, _ = run([(200, b"<html>")])
        self.assertEqual(record["attempts"][0]["outcome"], "INVALID_JSON")
        self.assertEqual(record["status"], "FAILED")

    def test_page_policy_checked(self):
        record, _, _ = run([(200, response(["W%d" % i for i in range(11)]))])
        self.assertEqual(record["status"], "INCONSISTENT")
        self.assertIn("within_per_page", record["failed_checks"])


class Drift(unittest.TestCase):
    def saved(self):
        records, _ = sets.build_saved(ROOT, SET)
        return next(r for r in records if r["id"].endswith("adj1-Q1"))

    def live_from(self, ids):
        base = self.saved()
        record, _, _ = run([(200, response(ids, count=150))])
        record["spec_sha256"] = base["spec_sha256"]
        return base, record

    def test_unchanged_reordered_changed(self):
        base = self.saved()
        ids = [r["id"] for r in base["response"]["ranked"]]
        _, same = self.live_from(ids)
        self.assertEqual(drift.compare(base, same)["status"], "UNCHANGED")
        _, swapped = self.live_from([ids[1], ids[0]] + ids[2:])
        d = drift.compare(base, swapped)
        self.assertEqual(d["status"], "REORDERED")
        self.assertEqual(len(d["moved"]), 2)
        _, new = self.live_from(ids[:-1] + ["W999"])
        d = drift.compare(base, new)
        self.assertEqual(d["status"], "CHANGED")
        self.assertEqual(d["entered"][0]["id"], "W999")
        self.assertEqual(d["left"][0]["id"], ids[-1])
        self.assertIn("CHANGED", drift.render([d]))

    def test_failed_live_not_compared(self):
        base = self.saved()
        record, _, _ = run([(429, b""), (429, b""), (429, b"")])
        record["spec_sha256"] = base["spec_sha256"]
        self.assertEqual(drift.compare(base, record)["status"], "NOT_COMPARED")

    def test_different_specs_refused(self):
        base = self.saved()
        _, other = self.live_from(["W1"])
        other["spec_sha256"] = "1" * 64
        with self.assertRaises(ContractError):
            drift.compare(base, other)

    def test_live_set_writes_no_secret(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        n = len(sets.load_set(SET)["items"])
        opener = FakeOpener([(200, response(["W1"]))] * n)
        files = sets.run_live_set(ROOT, SET, tmp, api_key=SECRET, opener=opener,
                                  clock=lambda: "2026-11-05T00:00:00Z", sleep=lambda s: None)
        self.assertEqual(len(opener.calls), n)
        for data in files.values():
            self.assertNotIn(SECRET.encode(), data)
        sets_written = {p.name for p in files}
        self.assertEqual(sets_written, {"live-records.jsonl", "drift.json", "DRIFT.txt"})


if __name__ == "__main__":
    unittest.main()
