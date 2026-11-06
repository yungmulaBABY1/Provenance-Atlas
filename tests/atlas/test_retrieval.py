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
OSTER = ROOT / "tests/atlas/retrieval/oster-batch1/set.json"
PROBE = ROOT / "tests/atlas/retrieval/probe-relevance-2026-11-05/set.json"
ALL_SETS = sorted((ROOT / "tests/atlas/retrieval").glob("*/set.json"))
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
        self.assertEqual(len(ALL_SETS), 3)
        for path in ALL_SETS:
            self.assertEqual(sets.check(ROOT, path), [], path)

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


class CommittedReplay(unittest.TestCase):
    """The 2026-11-05 replay from GitHub Actions run 42131614466, committed unchanged."""

    LIVE = SET.parent / "live-20261105T234403Z"

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        run_dir = "examples/research/baumeister-ego-depletion"
        shutil.copytree(ROOT / run_dir, self.tmp / run_dir)
        shutil.copytree(SET.parent, self.tmp / "set")
        self.set = self.tmp / "set/set.json"
        self.live = self.tmp / "set" / self.LIVE.name

    def problems(self):
        return sets.check_live_dir(self.tmp, self.set, self.live)

    def rehash(self, name):
        prov = json.loads((self.live / "PROVENANCE.json").read_text(encoding="utf-8"))
        prov["files_sha256"][name] = hashlib.sha256((self.live / name).read_bytes()).hexdigest()
        (self.live / "PROVENANCE.json").write_text(json.dumps(prov), encoding="utf-8")

    def test_committed_replay_checks(self):
        self.assertEqual(sets.check_live_dir(ROOT, SET, self.LIVE), [])

    def test_replay_facts(self):
        records = [json.loads(line) for line in
                   (self.LIVE / "live-records.jsonl").read_text(encoding="utf-8").splitlines()]
        self.assertEqual(len(records), 14)
        self.assertTrue(all(r["status"] == "OK" and len(r["attempts"]) == 1 for r in records))
        self.assertTrue(all(r["request"]["credentials"] == "none" for r in records))
        drifts = json.loads((self.LIVE / "drift.json").read_text(encoding="utf-8"))
        statuses = {d["id"].split("/")[1]: d["status"] for d in drifts}
        self.assertEqual(sorted(k for k, v in statuses.items() if v == "REORDERED"),
                         ["adj1-Q4", "adj1-Q5", "adj1-Q6"])
        self.assertEqual(sum(v == "UNCHANGED" for v in statuses.values()), 11)
        self.assertTrue(all(d["overlap"] == d["before"]["n"] == d["after"]["n"] for d in drifts))

    def test_changed_file_detected(self):
        path = self.live / "DRIFT.txt"
        path.write_text(path.read_text(encoding="utf-8").replace("REORDERED", "UNCHANGED"), encoding="utf-8")
        self.assertIn("CHANGED_REPLAY_FILE", self.problems()[0])

    def test_edited_record_with_new_hash_detected_by_recompute(self):
        path = self.live / "live-records.jsonl"
        lines = path.read_text(encoding="utf-8").splitlines()
        record = json.loads(lines[3])
        ranked = record["response"]["ranked"]
        ranked[6], ranked[7] = ranked[7], ranked[6]
        lines[3] = json.dumps(record)
        path.write_text("\n".join(lines) + "\n", encoding="utf-8")
        self.rehash("live-records.jsonl")
        self.assertTrue(any("STALE_OUTPUT" in p for p in self.problems()))

    def test_spec_change_detected(self):
        path = self.tmp / "set/specs/secE-F1.json"
        s = json.loads(path.read_text(encoding="utf-8"))
        s["notes"] = ["edited after the replay"]
        path.write_text(json.dumps(s), encoding="utf-8")
        self.assertIn("SPEC_CHANGED_SINCE_REPLAY: baumeister-1998-batch2/secE-F1", self.problems())

    def test_credential_field_checked(self):
        path = self.live / "live-records.jsonl"
        text = path.read_text(encoding="utf-8").replace('"credentials":"none"', '"credentials":"key abc"', 1)
        path.write_text(text, encoding="utf-8")
        self.rehash("live-records.jsonl")
        self.assertTrue(any("UNEXPECTED_CREDENTIAL_FIELD" in p for p in self.problems()))

    def test_missing_provenance_detected(self):
        (self.live / "PROVENANCE.json").unlink()
        self.assertIn("MISSING_PROVENANCE", self.problems()[0])


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
        names = {p.relative_to(tmp).as_posix() for p in files}
        self.assertTrue({"live-records.jsonl", "drift.json", "DRIFT.txt"} <= names)
        self.assertEqual(len([n for n in names if n.startswith("responses/")]), n)


class OsterSet(unittest.TestCase):
    """Batch 1 (Oster 2005): reconstructed specs checked against the run's own declarations."""

    def setUp(self):
        records, self.samples = sets.build_saved(ROOT, OSTER)
        self.records = {r["id"].split("/")[1]: r for r in records}

    def test_corpus_declarations_differ_textually_from_requests(self):
        bad = sorted(k for k, r in self.records.items() if r["status"] == "INCONSISTENT")
        self.assertEqual(bad, ["recent1-top25", "reception1-top50"])
        for k in bad:
            r = self.records[k]
            self.assertEqual(r["failed_checks"], ["declared_terms_in_request"])
            self.assertTrue(r["checks"]["declared_response_sha256_matches"])
            self.assertTrue(any("referenced_works" in t for t in r["missing_terms"]["request"]))

    def test_lock_and_first_attempt_in_same_second(self):
        self.assertEqual(self.records["secE-F1"]["executor_log"]["declared_vs_first_attempt"], "same-second")
        self.assertEqual(self.records["secE-F1"]["executor_log"]["statuses"].count(429), 11)
        self.assertEqual(self.records["adj1-Q1"]["executor_log"]["declared_vs_first_attempt"], "before")

    def test_samples_reproduce(self):
        self.assertEqual([sets.sample_reproduces(s) for s in self.samples], [True, True])
        self.assertEqual(self.samples[1]["rule"], "census: every ranked member")

    def test_malformed_log_line_reported(self):
        from atlas.retrieval.saved import read_log
        _, malformed = read_log(ROOT / "examples/research/oster-hepatitis-b/logs/retrieval_log.jsonl")
        self.assertEqual(malformed, [25])
        self.assertIn("malformed lines [25]", (OSTER.parent / "REPORT.txt").read_text(encoding="utf-8"))

    def test_reconstruction_reproduces_committed_specs(self):
        for name in ("baumeister-batch2", "oster-batch1"):
            tmp = Path(tempfile.mkdtemp())
            self.addCleanup(shutil.rmtree, tmp)
            src = ROOT / "tests/atlas/retrieval" / name
            shutil.copytree(src, tmp / "tests/atlas/retrieval" / name)
            for d in ("atlas", "examples"):
                (tmp / d).symlink_to(ROOT / d)
            import subprocess
            subprocess.run([sys.executable, "-I", str(tmp / "tests/atlas/retrieval" / name / "reconstruct_specs.py")],
                           check=True, cwd=tmp)
            for path in sorted((src / "specs").glob("*.json")) + [src / "set.json"]:
                rebuilt = tmp / "tests/atlas/retrieval" / name / path.relative_to(src)
                self.assertEqual(rebuilt.read_bytes(), path.read_bytes(), path)


class RankingAndBodies(unittest.TestCase):
    def test_ranking_basis(self):
        s = spec()
        self.assertEqual(core.ranking_basis(s), {"basis": "provider default (relevance for a search)",
                                                 "sort_key": "relevance_score", "checkable": False})
        sorted_spec = json.loads((SET.parent / "specs/secE-F1.json").read_text(encoding="utf-8"))
        self.assertTrue(core.ranking_basis(sorted_spec)["checkable"])
        probe = json.loads((PROBE.parent / "specs/q4-default-scored.json").read_text(encoding="utf-8"))
        self.assertTrue(core.ranking_basis(probe)["checkable"])

    def test_score_kept_in_ranked_rows(self):
        data = response(["W1", "W2"])
        data["results"][0]["relevance_score"] = 12.5
        rows = core.ranked(data)
        self.assertEqual(rows[0]["score"], 12.5)
        self.assertNotIn("score", rows[1])

    def test_provider_error_text_recorded_and_not_retried(self):
        record, _, opener = run([(400, b'{"error":"relevance_score is not a valid select field"}')])
        self.assertEqual(len(opener.calls), 1)
        self.assertIn("not a valid select field", record["attempts"][0]["detail"])

    def test_unsaved_spec_not_compared(self):
        tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, tmp)
        opener = FakeOpener([(200, response(["W1"]))] * 4)
        files = sets.run_live_set(ROOT, PROBE, tmp, opener=opener, clock=lambda: "2026-11-05T00:00:00Z",
                                  sleep=lambda s: None)
        drifts = json.loads(files[tmp / "drift.json"])
        self.assertEqual({d["status"] for d in drifts}, {"NOT_COMPARED"})
        self.assertIn("no saved record", drifts[0]["reason"])


class KeptBodies(unittest.TestCase):
    """A replay that keeps response bodies, built with a fake opener from the saved files."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.addCleanup(shutil.rmtree, self.tmp)
        run_dir = "examples/research/baumeister-ego-depletion"
        shutil.copytree(ROOT / run_dir, self.tmp / run_dir)
        shutil.copytree(SET.parent, self.tmp / "set")
        self.set = self.tmp / "set/set.json"
        self.live = self.tmp / "set/live-test"
        replies = []
        for item in sets.load_set(self.set)["items"]:
            body = json.loads((self.tmp / item["response"]).read_text(encoding="utf-8"))
            if item["spec"].endswith("adj1-Q1.json"):
                body["results"][0]["cited_by_count"] += 5
                body["results"][0]["abstract_inverted_index"] = {"secret": [0]}
            replies.append((200, body))
        files = sets.run_live_set(self.tmp, self.set, self.live, opener=FakeOpener(replies),
                                  clock=lambda: "2026-11-05T00:00:00Z", sleep=lambda s: None)
        for path, data in files.items():
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(data)
        self.pin()

    def pin(self):
        pinned = {p.relative_to(self.live).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                  for p in self.live.rglob("*") if p.is_file() and p.name != "PROVENANCE.json"}
        (self.live / "PROVENANCE.json").write_text(json.dumps({"files_sha256": pinned}), encoding="utf-8")

    def test_bodies_kept_without_abstracts_and_checked(self):
        self.assertEqual(sets.check_live_dir(self.tmp, self.set, self.live), [])
        kept = (self.live / "responses/adj1-Q1.json").read_text(encoding="utf-8")
        self.assertNotIn("abstract_inverted_index", kept)

    def test_field_changes_reported(self):
        drifts = {d["id"].split("/")[1]: d for d in
                  json.loads((self.live / "drift.json").read_text(encoding="utf-8"))}
        self.assertEqual(drifts["adj1-Q1"]["field_changes"], {"cited_by_count": 1})
        self.assertEqual(drifts["adj1-Q2"]["field_changes"], {})
        self.assertIn("cited_by_count 1", (self.live / "DRIFT.txt").read_text(encoding="utf-8"))

    def test_edited_body_detected(self):
        path = self.live / "responses/adj1-Q2.json"
        data = json.loads(path.read_text(encoding="utf-8"))
        data["results"].reverse()
        path.write_text(json.dumps(data), encoding="utf-8")
        self.pin()
        self.assertIn("BODY_DOES_NOT_MATCH_RECORD: baumeister-1998-batch2/adj1-Q2",
                      sets.check_live_dir(self.tmp, self.set, self.live))

    def test_unpinned_file_detected(self):
        (self.live / "responses/extra.json").write_text("{}", encoding="utf-8")
        self.assertTrue(any("UNPINNED_FILE" in p for p in sets.check_live_dir(self.tmp, self.set, self.live)))


class ProbeFindings(unittest.TestCase):
    """Facts stated in probe-relevance-2026-11-05/FINDINGS.txt, read from the committed records."""

    LIVE = PROBE.parent / "live-20261106T002702Z"

    def records(self, path):
        return {json.loads(line)["id"].split("/")[1]: json.loads(line)
                for line in path.read_text(encoding="utf-8").splitlines()}

    def setUp(self):
        self.probe = self.records(self.LIVE / "live-records.jsonl")
        self.saved = self.records(SET.parent / "saved-records.jsonl")
        self.replay = self.records(SET.parent / "live-20261105T234403Z/live-records.jsonl")

    def ids(self, record):
        return [r["id"] for r in record["response"]["ranked"]]

    def test_committed_probe_checks(self):
        self.assertEqual(sets.check_live_dir(ROOT, PROBE, self.LIVE), [])

    def test_scores_returned_first_attempt(self):
        for r in self.probe.values():
            self.assertEqual([a["status"] for a in r["attempts"]], [200])
            self.assertTrue(all(isinstance(x.get("score"), float) for x in r["response"]["ranked"]))

    def test_ranks_7_8_have_smallest_gap(self):
        expected = {"q4": 0.005886, "q5": 0.048153, "q6": 0.065405}
        for q, gap in expected.items():
            scores = [x["score"] for x in self.probe[f"{q}-default-scored"]["response"]["ranked"]]
            gaps = [scores[i] - scores[i + 1] for i in range(9)]
            self.assertEqual(min(range(9), key=lambda i: gaps[i]), 6)
            self.assertAlmostEqual(gaps[6], gap, places=5)

    def test_order_matches_replay_and_differs_from_grok_by_one_swap(self):
        for q in ("q4", "q5", "q6"):
            probe = self.ids(self.probe[f"{q}-default-scored"])
            name = f"adj1-{q.upper()}"
            grok, replay = self.ids(self.saved[name]), self.ids(self.replay[name])
            self.assertEqual(probe, replay)
            swapped = grok[:6] + [grok[7], grok[6]] + grok[8:]
            self.assertEqual(probe, swapped)

    def test_explicit_sort_equals_default(self):
        a, b = self.probe["q4-default-scored"], self.probe["q4-explicit-scored"]
        self.assertEqual(a["response"]["ranked"], b["response"]["ranked"])

    def test_provider_echo_in_saved_records(self):
        adj = self.saved["adj1-Q1"]["response"]["provider_echo"]
        self.assertEqual((adj["order"], adj["order_default"]), ("best matches first", True))
        sec = self.saved["secE-F1"]["response"]["provider_echo"]["oql"]
        self.assertIn("(mental fatigue) in the title", sec)
        self.assertNotIn('"mental fatigue"', sec)
        self.assertIn('stemmed "ego depletion"', adj["oql"])


if __name__ == "__main__":
    unittest.main()
