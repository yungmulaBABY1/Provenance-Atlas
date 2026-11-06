# Locked queries recorded by code (`atlas.retrieval`) — X1

An audit's locked literature searches are queries it declares before looking at
results. This package writes the search record itself, from what it observes,
instead of relying on an executor's account of what it searched. It never calls a
model, and it never records a credential. It points; you judge.

Status: IMPLEMENTED and tested offline. One live replay has been RUN and committed
(see [Live replay](#live-replay)).

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
  - `ranking`: what decides the order, and whether the response carries that
    key (`checkable`);
  - named checks, and observations from the executor log, labeled
    executor-written;
  - in live records, the kept body (`body_file`, without abstracts) and, for
    errors, the provider's error text (first 300 characters).
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
- **Ranking reported, not recomputed.** ADJUDICATION-1 declares OpenAlex
  relevance ranking, "the default for a search filter". The requests carry no
  `sort`, and `relevance_score` was not selected, so the order cannot be
  recomputed. The provider's own echo in each saved response (`meta.x_query`,
  now recorded as `provider_echo`) reports "best matches first" (default). That
  is the declared ranking, as the provider reports it.
- **Quoted terms.** The Section E lock writes each term in quotes
  (`F1 "mental fatigue"`), and the requests send them unquoted.
  - The provider's echo reads them as plain words, "(mental fatigue) in the
    title", whereas the quoted phrases of ADJUDICATION-1 appear as phrases.
  - So the executed Section E queries were word matches.
  - Whether the lock meant phrases is still not stated.
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

## Second set: Batch 1 (Oster 2005)

The set is [`tests/atlas/retrieval/oster-batch1/`](../../tests/atlas/retrieval/oster-batch1/).
It covers eleven OpenAlex page-1 queries from the run merged in #16:
- ADJUDICATION-1 Q1–Q5;
- Section E F1–F4;
- RECEPTION-1 and RECENT-1.

It also holds the RECEPTION-1 sample redraw and the RECENT-1 census.

Results (TESTED, deterministic, offline):
- **9 of 11 consistent.**
- **2 inconsistent: RECEPTION-1 and RECENT-1.** The run output declares
  `filter=referenced_works:W3123222584` and `per_page`. The executed requests used
  `filter=cites:W3123222584` and `per-page`.
  - OpenAlex documents `cites:W` as the works that have W in their
    `referenced_works`, so the two may select the same works. That equivalence
    is not tested here.
  - The declared response hashes match the committed files.
  - The mismatch is in how the query was written down, and it is recorded, not
    resolved.
- **Same-second lock (secE-F1).** The Section E lock time and the first attempt
  fall in the same second (10:29:05Z, both executor-written). Their order cannot
  be established at one-second resolution. That attempt was the first of eleven
  429s before a success.
- **Malformed log line.** Line 25 of the executor's log is not valid JSON
  (`"status":000`, a PDF fetch). It is reported and not repaired. It does not
  concern these queries.
- **The sample and the census reproduce.**
- Unlike Batch 2's, these logged requests carry no `mailto`.

## Reconstructing specs

Each reconstructed set has a `reconstruct_specs.py`. It rebuilds the specs and
`set.json` from the executor's log (`atlas.retrieval.reconstruct`), together
with the declared terms, which were copied by hand into the script. A test
reruns both scripts and requires byte-identical output.

## Specs for a future run

A set item may have no saved response. Such a spec is meant to be locked before
any run, and only a live replay records it:
- `build` checks its declaration (hash and terms);
- `run-live` records it;
- its drift is `NOT_COMPARED` ("no saved record").

The first example is
[`tests/atlas/retrieval/probe-relevance-2026-11-05/`](../../tests/atlas/retrieval/probe-relevance-2026-11-05/).
Its `PLAN.txt` was written before any request and asks three questions:
- Does OpenAlex return `relevance_score` when it is selected?
- Are ranks 7 and 8 near-tied in Batch 2's Q4–Q6?
- Does an explicit `sort=relevance_score:desc` match the default order?

It was RUN on 2026-11-06 00:27 UTC: GitHub Actions run 42136887560, no key.
The run is committed in `live-20261106T002702Z/`, and the answers are in
[`FINDINGS.txt`](../../tests/atlas/retrieval/probe-relevance-2026-11-05/FINDINGS.txt):
- **Scores returned.** OpenAlex returns `relevance_score` when it is selected.
- **The swaps are near-ties.** In Q4, Q5 and Q6, ranks 7 and 8 have the
  smallest adjacent score gap in the top 10: 0.006, 0.048 and 0.065, against
  top-10 ranges of 13.6–19.1.
  - The swaps fell exactly at the near-ties.
  - Why the order changed between 11:28Z and 23:44Z remains open: a small
    rescoring or the provider's tie-breaking. Grok's saved responses carry no
    scores.
- **Explicit sort changes nothing.** An explicit `sort=relevance_score:desc`
  gives the default order.

Recommendation, not yet applied to any instrument: a relevance-ranked top-N
should select `relevance_score`, request a few more than N, and record the
score margin at the cutoff.

## Live replay

The replay sends every spec again, records each attempt, and compares the result
with the saved records (`drift.json`, `DRIFT.txt`). Each spec gets a status:
- UNCHANGED, REORDERED or CHANGED, listing what entered, left or moved; or
- NOT_COMPARED.

A change is an observation about the index over time, not about the audit.

How to run it:
- From GitHub: the manual workflow
  [`retrieval-live-replay.yml`](../../.github/workflows/retrieval-live-replay.yml).
  - It never runs on push. It uploads the records as an artifact and commits
    nothing.
  - The repository secret `OPENALEX_API_KEY` is optional. Without a key,
    OpenAlex's keyless budget applies, and 429s are recorded as failed attempts.
- From any machine with network access:
  `python -m atlas.retrieval run-live tests/atlas/retrieval/baumeister-batch2/set.json --out <dir>`

Claude's workspace cannot run it: its egress proxy denied CONNECT to
`api.openalex.org` (403) on 2026-11-05.

### Replay of 2026-11-05 (RUN, committed)

The files are in
[`tests/atlas/retrieval/baumeister-batch2/live-20261105T234403Z/`](../../tests/atlas/retrieval/baumeister-batch2/live-20261105T234403Z/).
- **Where it ran:** GitHub Actions run 42131614466, at commit `e595610`, with no
  API key.
- **How it got here:** the owner downloaded the artifact and attached it to a
  Claude session.
  - Its sha256 equals GitHub's artifact digest
    (`e967daa2…`).
  - The three files are committed unchanged. `PROVENANCE.json` pins them.
  - CI checks that the files match those hashes and that every record is of a
    current spec. It also checks that the drift recomputes byte for byte.

Result, compared with Grok Bot's saved responses about 12 hours earlier:
- All 14 queries succeeded on the first attempt, with no 429s. Grok's run had 12
  on these queries, from another network, keyless, with a `mailto`.
- **Membership is identical everywhere.** Every query returned the same works
  and the same total count.
- **11 UNCHANGED.**
- **3 REORDERED:** ADJUDICATION-1 Q4, Q5 and Q6. In each, the works at ranks 7
  and 8 trade places. The cause is UNKNOWN. Candidates:
  - OpenAlex rescoring between the runs;
  - a difference between the executor's request and the code's (only `mailto`
    differs);
  - near-tied relevance scores.

  The responses do not include `relevance_score`, so these cannot be separated.
  The audit's screened sets are unaffected, because membership is unchanged.
- **Results digests differ** for 9 of 14 queries, including some UNCHANGED ones.
  Some field inside the records changed (citation counts are the likely field;
  not verified). Live records keep summaries, not full bodies, so the changed
  field is not recorded.
- **Four more dispatches** ran within a minute of this one. Their job logs print
  the same DRIFT.txt apart from timestamps. Their artifacts are not committed.

To review a committed replay offline:
`python -m atlas.retrieval drift <set.json> <dir>/live-records.jsonl`.

## Commands

```sh
python -m atlas.retrieval check tests/atlas/retrieval/*/set.json     # CI: outputs are a fresh build
python -m atlas.retrieval build tests/atlas/retrieval/baumeister-batch2/set.json [--write]
python -m atlas.retrieval run-live <set.json> --out <dir>             # network; optional OPENALEX_API_KEY
python -m atlas.retrieval drift <set.json> <live-records.jsonl>       # offline
```

Tests: `tests/atlas/test_retrieval.py`, 55 tests.
- Spec validation: credentials, paging, per-page, host, declaration.
- Canonical requests and the Provenance #14 digest convention.
- Tamper detection: response bytes, the declaration, a request that departs from
  the declaration, the sample seed, stale outputs.
- Live attempt recording with a fake opener. No test uses the network.
- Retry policy, the key never recorded, drift statuses.
- The committed replay: file hashes, a spec changed since the replay, an edited
  record, the credential field, missing provenance.
- Kept bodies: no abstracts, field-change counts, an edited body, an unpinned
  file.
- The Oster findings, the census, the malformed log line, same-second ordering.
- Ranking basis, scores in ranked rows, provider error text.
- Specs without saved responses.
- Both reconstruction scripts reproduce their committed files.
- The probe findings, read from the committed records.

Twenty mutations of the checks were each caught: ten for the first version and
ten for these additions.

## Limits and next steps

- The specs here are reconstructions. The intended order is the reverse: a spec
  written and hashed **before** the run, which is the AuditPlan in
  `claude/Execution_Interface_and_Hosting_Review_2026-11-05.txt`. The executor
  or this code then runs it.
- One provider so far: OpenAlex. OpenCitations would give a second, independent
  citation graph.
- Response bodies are kept, without abstracts, under `responses/`, and drift
  counts the fields that changed. The 2026-11-05 replay predates this and has
  no bodies.
- Ranking can be checked only when the sort key is selected (`ranking` in
  every record). OpenAlex accepts `relevance_score` in `select` (probe,
  2026-11-06).
- Records are not yet Atlas contract records. Linking them to `CorpusScope`
  and `SourceReadReceipt` is a later increment.
