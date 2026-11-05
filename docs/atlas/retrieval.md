# Locked queries recorded by code (`atlas.retrieval`) — X1

An audit's locked literature searches are queries it declares before looking at
results. This package writes the search record itself, from what it observes,
instead of relying on an executor's account of what it searched. It never calls a
model, and it never records a credential. It points; you judge.

Status: IMPLEMENTED and tested offline. The live replay has NOT been run (see
[Live replay](#live-replay)).

## Two modes

| Mode | Who retrieved | What the code establishes |
| --- | --- | --- |
| `saved` | the executor (for example Grok Bot) | That four things agree, or where they disagree: the declared query, the request the executor logged, the file the executor logged writing, and the committed response |
| `live` | `atlas.retrieval` itself | The request it sent (`request_sha256`), every attempt including failures, and digests it computed itself |

Live mode retries only on HTTP 429 and 5xx. A network or proxy error is recorded
and not retried, because a policy denial must not be retried. A run with no
successful attempt still produces a record, with status `FAILED`.

## Records

- **Spec** (`atlas-retrieval-spec/0.1`):
  - provider endpoint;
  - exact parameters;
  - `pages: first-only`; cursor paging is not supported;
  - provenance: `locked-before-run` or `reconstructed-after-run`;
  - the declaration: file, sha256, kind (`pre-run-lock` or `run-output`) and
    the terms that must appear in both the declaration and the request.
- **Record** (`atlas-retrieval-record/0.1`):
  - canonical request and its sha256;
  - `retrieval_performed_by`;
  - response summary: count, page, number of results, ranked ids, titles and
    years;
  - response digest and results digest;
  - abstract state: `ABSENT`, `STRIPPED` or `PRESENT`;
  - named checks, and observations from the executor log, labeled
    executor-written.
- The **response digest** follows the SEARCH_DIGESTS convention in Provenance #14:
  sha256 of canonical JSON with every `abstract_inverted_index` key removed.
  Stripping an abstract therefore never changes it. The **results digest** covers
  `results` only, because `meta` changes on every call.
- **Credentials.** `api_key` and `mailto` are never part of a spec or a canonical
  request.
  - Live mode sends no `mailto`.
  - A key, read from `OPENALEX_API_KEY`, goes only in the `Authorization`
    header. Records say that a key was used, never which key, and the code
    refuses to write a record that contains the key.
  - From an executor's log, only the names of credential parameters are kept.

## First set: Batch 2 (Baumeister et al. 1998)

The set is [`tests/atlas/retrieval/baumeister-batch2/`](../../tests/atlas/retrieval/baumeister-batch2/).
It covers the fourteen OpenAlex page-1 queries Grok Bot executed and saved in
the citation-network v2-candidate.3 run (#15):
- ADJUDICATION-1 Q1–Q7;
- Section E F1–F5;
- RECEPTION-1 and RECENT-1.

It also holds one sample check: the RECEPTION-1 inspection sample redrawn from
the declared rule. The report is `REPORT.txt`.

Results (TESTED, deterministic, offline):
- All 14 queries are **consistent**:
  - declared terms appear in both the declaration and the request;
  - declaration hashes match;
  - each committed file matches the sha256 the executor logged;
  - page 1 only; no abstracts.
- **One re-execution after a success.** For secE-F2 the log shows the statuses
  429, 429, 200, 429, 200. The committed file is the second success.
  - The lock says each query is executed once, with retries only on 429/5xx.
  - The first successful response was not kept, so whether the two responses
    differed is unknown.
- **Ranking not checked.** ADJUDICATION-1 declares OpenAlex relevance ranking,
  "the default for a search filter". The requests carry no `sort`, and
  `relevance_score` was not selected, so the ranking actually applied is not
  checked.
- **Quoted terms.** The Section E lock writes each term in quotes
  (`F1 "mental fatigue"`), and the requests send them unquoted. The lock does not
  say whether the quotes mark a phrase or only delimit the term. This is recorded,
  not resolved.
- **Where the corpus queries are declared.** RECEPTION-1 and RECENT-1 are declared
  in the run output (02c), not in a pre-run lock. Their declared response hashes
  match.
- **The sample reproduces.** `random.Random(20261105).sample(range(1, 51), 12)`
  gives the declared positions and ids.

What this does not show:
- that the executor really sent the logged request (the log is written by the
  executor);
- that OpenAlex ranked results as declared;
- that any result set is complete or relevant.

The specs were **reconstructed after the run** from the executor's log, so
"request matches log" holds by construction. The independent comparison is
between the declared terms and the request.

## Live replay

The replay sends every spec again, records each attempt, and compares the result
with the saved records (`drift.json`, `DRIFT.txt`). Each spec gets a status:
- UNCHANGED, REORDERED or CHANGED, listing what entered, left or moved; or
- NOT_COMPARED.

A change is an observation about the index over time, not about the audit.

NOT RUN. Claude's workspace cannot reach `api.openalex.org`: the egress proxy
denied CONNECT (403) on 2026-11-05. A policy denial is reported, not retried.

Two ways to run it:
- From any machine with network access:
  `python -m atlas.retrieval run-live tests/atlas/retrieval/baumeister-batch2/set.json --out <dir>`
- From GitHub, after merge: the manual workflow
  [`retrieval-live-replay.yml`](../../.github/workflows/retrieval-live-replay.yml).
  It never runs on push. It uploads the records as an artifact and commits
  nothing. The repository secret `OPENALEX_API_KEY` is optional. Without a key,
  OpenAlex's shared keyless budget applies, and 429s are recorded as failed
  attempts. Batch 2's own log shows 15 OpenAlex 429s, 12 of them on the
  queries in this set.

To review a committed replay offline:
`python -m atlas.retrieval drift <set.json> <dir>/live-records.jsonl`.

## Commands

```sh
python -m atlas.retrieval check tests/atlas/retrieval/*/set.json     # CI: outputs are a fresh build
python -m atlas.retrieval build tests/atlas/retrieval/baumeister-batch2/set.json [--write]
python -m atlas.retrieval run-live <set.json> --out <dir>             # network; optional OPENALEX_API_KEY
python -m atlas.retrieval drift <set.json> <live-records.jsonl>       # offline
```

Tests: `tests/atlas/test_retrieval.py`, 29 tests.
- Spec validation: credentials, paging, per-page, host, declaration.
- Canonical requests and the Provenance #14 digest convention.
- Tamper detection: response bytes, the declaration, a request that departs from
  the declaration, the sample seed, stale outputs.
- Live attempt recording with a fake opener. No test uses the network.
- Retry policy, the key never recorded, drift statuses.

Ten mutations of the checks were each caught.

## Limits and next steps

- The specs here are reconstructions. The intended order is the reverse: a spec
  written and hashed **before** the run, which is the AuditPlan in
  `claude/Execution_Interface_and_Hosting_Review_2026-11-05.txt`. The executor
  or this code then runs it.
- Batch 1 (Oster) has the same layout. Its set can be added once #16 is merged.
- One provider so far: OpenAlex. OpenCitations would give a second, independent
  citation graph.
- Records are not yet Atlas contract records. Linking them to `CorpusScope`
  and `SourceReadReceipt` is a later increment.
