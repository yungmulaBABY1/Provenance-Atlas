# Atlas adapter changelog

## Unreleased — Oster set, kept bodies, relevance probe (`atlas.retrieval`)

- **Second set** `tests/atlas/retrieval/oster-batch1/`: Batch 1's eleven
  OpenAlex page-1 queries (#16).
  - 9 consistent.
  - RECEPTION-1 and RECENT-1 inconsistent: declared `referenced_works:`/`per_page`,
    executed `cites:`/`per-page`. Possibly equivalent; not tested.
  - Lock and first attempt in the same second (secE-F1).
  - Malformed executor-log line 25, reported.
  - The sample and the census reproduce.
- **Kept bodies.** Live replays now keep response bodies, without abstracts, under
  `responses/`. Drift counts the fields that changed in works present both times.
- **Ranking and error text.** Records carry `ranking`, which says whether the
  sort key is in the response. Ranked rows carry `score` when the provider
  returns `relevance_score`. HTTP errors record the provider's error text.
- **Specs without saved responses** (for future runs): declarations are checked
  at build, and drift is `NOT_COMPARED`. First use: the
  `probe-relevance-2026-11-05` set, with `PLAN.txt` written before any request.
  Not run.
- **Replay checks.** `check` now pins every file in a committed replay and
  verifies kept bodies against their records.
- **Log reading.** The executor-log reader reports malformed lines instead of
  failing. Declaration-vs-attempt order is now `before`, `same-second` or
  `after`; it was a boolean. Batch 2's outputs were rebuilt accordingly.
- **Reconstruction.** `reconstruct_specs.py` for both sets and
  `atlas.retrieval.reconstruct`. Batch 2's specs are byte-identical to the
  committed ones, so the committed replay still checks.
- 13 new tests.

## Unreleased — first live replay committed (`atlas.retrieval`)

- `tests/atlas/retrieval/baumeister-batch2/live-20261105T234403Z/`: the
  artifact of GitHub Actions run 42131614466, committed unchanged, with
  `PROVENANCE.json`. The artifact zip's sha256 equals GitHub's digest.
- Result against Grok's saved responses:
  - all 14 queries returned the same works and counts;
  - 11 unchanged;
  - 3 swapped ranks 7 and 8 (Q4, Q5, Q6; cause unknown);
  - no 429s.
- `check` now also verifies committed replays:
  - provenance hashes;
  - records are of the current specs;
  - allowed credential field;
  - drift recomputed offline.
- 7 new tests.

## Unreleased — locked queries 0.1.0 (`atlas.retrieval`, X1)

- New package `atlas/retrieval/` (schemas `atlas-retrieval-spec/0.1`,
  `atlas-retrieval-record/0.1`, `atlas-retrieval-set/0.1`, `atlas-retrieval-drift/0.1`).
  It records an audit's locked literature searches by code. See
  [retrieval.md](retrieval.md).
  - Saved mode checks the declaration, the executor's logged request, the
    executor's logged file hash and the committed response against each other.
  - Live mode records every attempt and retries only on 429 and 5xx.
  - The response digest follows the Provenance #14 SEARCH_DIGESTS convention.
  - Credentials are never recorded.
- First set: the fourteen OpenAlex page-1 queries of Batch 2 (Baumeister 1998),
  with specs reconstructed after the run.
  - All 14 are consistent.
  - One query (secE-F2) was re-executed after a success.
  - The RECEPTION-1 sample reproduces.
- CI step `Locked-query records are current` (offline). Manual workflow
  `retrieval-live-replay.yml`, which needs network and never runs on push.
- 29 new tests. The live replay has not been run: Claude's workspace is denied
  egress to api.openalex.org.

## Unreleased — audit page (`atlas.view`, kind `audit`)

- New page `docs/atlas/views/ajr2001/`: a paper page for Grok's AJR 2001
  citation-network audit. It is rendered from the verified map-link and challenge
  bundles, which must pin the same import. It covers the glance rows, the audit on
  record, the claim under audit and its wordings, the seven findings with the run's
  labels and their map alignment, the three review items with all six challenges
  (item 1's disagreement shown), the sources and what is not established.
- No source text is shown. Model-written text quoting 8 or more consecutive words
  of a source passage is withheld with a notice. On AJR this applies to finding 4,
  which quotes NS-E1.
- Label table `atlas-plain-labels/0.3` (additions only). Refs name bundle runs by
  kind; one ref on the power-posing page now reads "import" where it read "run".
- 10 new tests.

## Unreleased — challenges 0.1.0 (`atlas.challenge`, M1 Increment C part 2)

- New package `atlas/challenge/` (schema `atlas-challenge/0.1`, artifacts
  `atlas-challenge-artifact/0.1`). It records attributed decisions on the review items
  a checker leaves open. See [challenge.md](challenge.md).
  - It content-replays the import receipt.
  - It re-runs the vendored checker on the run's output bytes.
  - Every item has a stated challenge state.
  - Challenges bind to the exact item and only append.
- The run's producer and the declared code author cannot record a decision.
- A changed target detaches a challenge but keeps it, and disagreeing challenges are
  all kept.
- AJR 2001: three items (`SOURCE_LOCK_TRUTH`, `DIRECT_ADJUDICATION_SUBSTANCE`,
  `NESTING_SUBSTANCE`). A reviewer packet is in `challenge-packets/`. Two model
  reviewers answered it, ChatGPT/Codex and ChatGPT (GPT-6), and both answers are
  transcribed verbatim:
  - item 1: `CANNOT_DETERMINE` / `CONDITION_MET_WITH_QUALIFICATION` (they disagree);
  - item 2: `CONDITION_MET_WITH_QUALIFICATION` from both;
  - item 3: `CONDITION_NOT_MET` from both.
  0 of 3 items have a decision by a person.
- Evidence may be `EXTERNAL` (kept as cited, not resolved), and file evidence may carry a note. An artifact may name a
  pinned `transcribed_from` source, whose text fields are then checked verbatim.
- 26 new tests. CI adds challenge replay.

## Unreleased — map links 0.1.0 (`atlas.maplink`, M1 Increment E)

- New package `atlas/maplink/` (schema `atlas-maplink/0.1`). It links an imported
  audit's findings to a separately produced Stage-1 claim map, for outputs that carry
  no map of their own (`atlas.claims`: `CLAIM MAP ABSENT`).
  - It content-replays the claim-link receipt it depends on.
  - It parses the pinned map with `atlas-claim-extraction-output/1`.
  - It records the map's provenance as declared: `run_prompt: NOT_RECORDED`,
    `run_receipt: NONE`.
  - See [maplink.md](maplink.md).
- First receipt: Grok's AJR 2001 citation-network run (PR #7).
  - The output names its map at line 5.
  - Reconciliation of fields 1, 3 and 6 is `UNRESOLVED_REQUIRES_REVIEW` for all three:
    the citation stage reworded the map.
  - Findings: 4 `DECLARED_NOT_FIELD_6` and 3 `UNRESOLVED_REQUIRES_REVIEW`.
- MAP GAP declarations are classified by the instrument's two forms, matched as
  written. A field mentioned inside a gap is never resolved as the target.
- `atlas.claims` and `atlas.extraction` are unchanged, so every existing receipt still
  replays.
- 28 new tests. CI adds map-link replay.

## Unreleased — research questions 0.1.0 (`atlas.question`, M1 Increment D)

- New package `atlas/question/` (schema `atlas-question/0.1`): one declared question
  over a declared list of sources, built from pinned receipts only. Records the
  question and who worded it, the corpus and its selection rule, and per source:
  access, passages with speaker and subject, checks and eligibility, audit records
  and reviews. See [question.md](question.md).
- First question: power posing over S1-S4, wording drafted by Claude from S1's title
  and marked not confirmed. Coverage today: 2/4 retrieved, 2/4 passages on record,
  1/4 described in another source's words, 1/4 extracted, 1/4 target of an imported
  audit, 0/4 with a decision by a person.
- No judgment: score/verdict/stance/position fields are rejected, counts recompute
  from the members, a passage stays with its speaker, and claim identity across
  sources is declared and attributed only.
- `atlas.view`: question page (`docs/atlas/views/power-posing/`, no source text) and
  a breadcrumb on the S2 page with the same denominator. Pages are now declared in
  `docs/atlas/views/views.json` and rendered with `build-all`/`check-all`.
  Labels table bumped to `atlas-plain-labels/0.2` (additions only).
- Fixes to the 0.1.0 view (PR #5): wrapped list items in report.txt repeated their
  bullet on every line; one table could widen the page by 2px at 390px.
- 22 new tests (252 total, one skipped without private inputs). CI adds question
  replay and checks every declared page.

## Unreleased — evidence view 0.1.0 (`atlas.view`, M1 Increment C part 1 / M2)

- New package `atlas/view/`: verifies an extraction bundle by content replay, builds
  one view model (`view.json`, schema `atlas-view/0.1`) in which every item names
  the records it comes from, and renders it twice: a reader-first page
  (`index.html`) and a plain-text report (`report.txt`). See [view.md](view.md).
- First real screen: `docs/atlas/views/s2-run1/`, the S2 testosterone claim.
- No paraphrase of content. Plain language only through the declared label table
  `atlas-plain-labels/0.1`, always beside the native label; an unlisted label is
  an error. No score or verdict.
- 13 new tests. CI checks the committed view is a fresh render.
- Not in this increment: the attributed challenge record (Increment C part 2).

## Unreleased — recorded extraction 0.1.0 (`atlas.extraction`, M1 Increment B)

- New package `atlas/extraction/` (schema `atlas-extraction/0.1`) and the first
  recorded run: a claim-extraction map of S2 (Ranehill et al. 2015) by a
  declared external runner, with its packet pinned. See [extraction.md](extraction.md).
- Two stages. Local (private full output + PDF): source hashes, extraction hash,
  48 quotes matched (8 exact, 36 normalized only, 4 mismatched; 44/44 on their
  stated page). Public (CI): redacted output, published quotes re-checked
  against public excerpts, links, evidence check.
- Source-light: the full output stays private; 43 block quotes are withheld by
  hash; one new bounded excerpt (A2.3, 361 bytes) is committed as evidence.
- Links: four anchors lie inside the passages the two model reviews are bound
  to; the historical provisional map targets S1, so it is recorded as a
  different target, not merged.
- Evidence check `reported-statistics-consistency/1` on the run's Field 6:
  transcription, p from t, t from CI — all consistent.
- 30 new tests (217 total; one needs the private inputs and is skipped in CI).
  CI adds a content-replay step for extraction receipts. No existing module,
  receipt, fixture or instrument changed.

## Unreleased — claim links 0.2.0 (`atlas.claims`, M1 Increment A)

Revised in review before merge; supersedes 0.1.0 (schema `atlas-claimlink/0.1`,
parser 1) at bb017ec, which was never merged.

- **Ambiguous map fields no longer become link targets.** Parser 2 validates
  each field number against its instrument label and keeps every entry. A
  mislabelled (`LABEL_MISMATCH`) or repeated (`DUPLICATE_ENTRIES`) Field 6 no
  longer supplies a designated target; at bb017ec, "Field 6 - Weaker defensible
  claim: A" was accepted silently and the first of two contradictory Field 6
  entries was kept, so either could yield `SAME_TEXT`. Conflicting text is
  preserved as statements and listed as candidates. The validator rejects
  comparisons or designations that touch a non-`USABLE` statement and
  `SAME_TEXT*` identities without a backing comparison. Schema `atlas-claimlink/0.2`.
- **`show` verifies before rendering.** It replays the bundle at content level
  and renders nothing if replay fails (`NOT_VERIFIED`). `--unverified` renders
  stored assertions under a banner placed before any label. At bb017ec, `show`
  displayed edited labels such as `VERIFIED` and review `MATCH` unchanged.
- 12 new tests (44 in `test_claims.py`, 187 total). Reintroducing either
  defect, or rendering without verification, fails the targeted tests.
- Receipt `tests/atlas/claims/receipts/power-posing-reviewed/` regenerated
  (code and schema changed). Its findings are unchanged.

- New package `atlas/claims/` with its own record schema `atlas-claimlink/0.1`,
  context schema, CLI (`python -m atlas.claims build|replay|show`) and receipt
  (`tests/atlas/claims/receipts/power-posing-reviewed/`). See
  [claims.md](claims.md).
- Links the power-posing run `:3` output's own standalone claim map and
  pre-audit confirmation lines to its findings' target claims and to the two
  bound reviews, by exact and normalized text comparison only.
- The import adapter is unchanged: no `atlas/*.py` file changed, so the six
  current import receipts and their code pins are unchanged. CI adds a
  content-replay step for claim-link receipts.
- 32 new tests (`tests/atlas/test_claims.py`): committed case, real controls
  from three other receipts, output mutations (identical, wrapped, polarity
  and scope changes, review detachment), dependency and contract pins,
  tampering, parser grammar.

## Unreleased — adapter 0.3.0: review binding contract `atlas-evidence-review/2`

- Reviews now bind each passage by a full descriptor: source version, component,
  start and end offsets, offset unit, interval and quotation hash. Under `/1` a
  passage moved by one character kept the same quotation hash, so it became
  `MISMATCH` while both reviews stayed `MATCH`. That gap is closed.
- `/1` is retired: import and restore reject it with `UNSUPPORTED_REVIEW_SCHEMA`.
  The `/1` artifacts are kept in `tests/atlas/reviews/power-posing/v1/`.
- The F1-S2 reviews are re-issued as `/2`. Only the binding changed; each has a
  `reissue` block naming its `/1` predecessor by hash, and neither review was
  repeated. They are imported as run `:3` (`tests/atlas/power-sources-reviewed.json`).
- Receipts:
  - the six receipts current at 4718225 moved unchanged to
    `tests/atlas/receipts/historical-4718225/`;
  - the `/1`-bound run `:2` receipt there is rejected on restore, and the
    others still restore;
  - current receipts regenerated (only manifests differ for unreviewed runs).
- New tests: a moved locator unbinds in both directions; every descriptor field
  is bound; the review stays detached after export and restore; restore rejects
  a moved locator with a kept binding; `/1` artifacts and receipts are rejected.
  Reverting to quotation-only binding fails 10 of them.

## Adapter 0.2.0 (PR #9 at 4718225, not merged): first substantively reviewed evidence relationship

- New review kind `atlas-evidence-review/1` (`atlas/reviews.py`), imported as a
  `ReviewDecision`. It is bound to an exact proposition span, finding projection,
  mapping, passages, source version and input bytes; any change gives
  `TARGET_MISMATCH` with the components named. Restore and append re-derive the
  binding and check the artifact. Record schema unchanged (`atlas-adapter/0.2`).
- Reviews of Finding 1's S2 clause (`tests/atlas/reviews/power-posing/`):
  - review A (primary session): `SUPPORTS_WITH_QUALIFICATION`;
  - review B (separate subagent context): `SUPPORTS`.

  Both are kept. Neither is independent, and neither is human adjudication.
- `tests/atlas/power-sources-reviewed.json` imports them as run `:2`.
- `source_packet.py verify` also re-checks review locators against a fresh
  extraction.
- Receipts:
  - the five receipts current at 7c55e2c moved unchanged to
    `tests/atlas/receipts/historical-7c55e2c/` (restorable, not replayable
    under 0.2.0 code);
  - current receipts regenerated (only manifests differ);
  - new receipt `power-sources-reviewed`.

## Unreleased — power-posing real-source packet

No adapter code changes; record schema, parser and normalizer unchanged.

- `tests/atlas/sources/power-posing/`: bounded excerpts from the two retrievable
  packet sources (S2 publisher PDF, S4 accepted manuscript), with retrieval and
  extraction provenance in `SOURCES.json`. S1 and S3 (HTTP 403) are recorded as
  `RETRIEVAL_FAILED`. `source_packet.py` rebuilds or re-verifies the packet
  against the live sources; it is not run in CI.
- `tests/atlas/power-sources.json`: import of the archived pilot output with
  explicit finding-to-check mappings based on each finding's Evidence field.
- `tests/atlas/test_power_sources.py`: provenance, the three separate facts, and
  controls for missing methods, failed extraction, changed bytes, incorrect
  quotations, unavailable sources; CLI import/export/restore/replay.
- `tests/atlas/receipts/power-sources/`: committed receipt, content-replayed by CI.

## Unreleased — P0 review repairs (branch `atlas/p0-adapter`)

Implements the requirements in the P0 review record (sections 5 and 6) on top
of 072fa8a. Record schema `atlas-adapter/0.2`; import contexts stay
`atlas-adapter/0.1`; parser `atlas-citation-network-native` version 3;
normalizer `nfc-whitespace/2`.

### Integrity (R1, F1, F6)
- Every AuditRun and every record belonging to it must be covered by exactly one
  RunManifest; Work and SourceVersion may be shared. Uncovered records are
  rejected with `INVALID_MANIFEST_COVERAGE`.
- RunManifest records the parser identity (name, version, SHA-256 of
  `atlas/native.py`).
- Restore and append re-derive native findings, scorecard, parse issues,
  imported source lock, null assertion and output anchors from
  `raw_output_text`; any difference is `NATIVE_PROJECTION_MISMATCH`.
- Unsupported parser versions are reported as `NATIVE_PROJECTION_UNVERIFIED`.

### Anchors (R2)
- Passages store `exact_match` and `normalized_match` separately. `MATCH` only
  when exact; `NORMALIZED_MATCH_ONLY` otherwise when normalized forms agree; it
  is a named limitation, never full eligibility.
- NFKC removed; normalizer is `nfc-whitespace/2`; record schema bumped to 0.2.

### Contract-relative labels (F2)
- Parser issue code `INSTRUMENT_VIOLATION` renamed `CURRENT_CONTRACT_MISMATCH`.
- New `AuditRun.producing_instrument_compliance`: `UNDETERMINED` unless the
  historical instrument is `VERIFIED` as the baseline prompt blob; then
  `CONFORMS` or `VIOLATION`.

### Validation baseline (F3)
- The ten pinned files are vendored under `atlas/baseline/files/` and checked
  on SHA-256, git blob and byte count (`BASELINE_HASH_MISMATCH`).
- Working-tree drift is recorded as `VALIDATION_BASELINE_DIFFERS_FROM_WORKING_TREE`
  in the manifest environment; import still succeeds.

### Replay (F4)
- `replay --level strict` (default, byte-identical) and `--level content`
  (everything except the environment block; environment delta printed).
- `REPLAY_MISMATCH` names the differing component(s).
- CI content-replays every committed receipt.

### Reviews (F5)
- AuditRun refs list only target-matched reviews; others are under
  `mismatched_review_ids`.

### Null results
- `clean_display` and `SCOPED_NULL_ASSERTION_ONLY` removed. AuditRun records
  `imported_null_assertion` and `adapter_source_eligibility` as separate facts.

### Ported from package B
- Case 12/13 paired packet fixtures (`tests/atlas/case12-healthy.json`,
  `tests/atlas/case13-closed.json`).
- Exact character spans (`char_start`, `char_end`) on finding output anchors,
  re-derived on restore.
- `docs/atlas/contracts/prompt-contracts.md` and `native-contract-excerpts.md`
  (documentation only).

### Fixed
- Issues for unknown scorecard dimension names were emitted in hash-seed order,
  so imports of affected outputs were not deterministic across processes
  (inherited from 072fa8a). They are now sorted; parser version 3.

### Receipts
- Current receipts for power-control, shen-known-bad, case12-healthy and
  case13-closed under `tests/atlas/receipts/`, built on CPython 3.11.17.
- The 072fa8a receipts are kept under `tests/atlas/receipts/historical-072fa8a/`;
  they cannot be replayed or restored by this version.

### Known baseline debt
- `tools/embed_prompts.py --check` returns STALE at the base commit; not changed.

## 0.1.0 — 072fa8a

Initial deterministic citation-network adapter (authored by Codex in a separate
session): native parser, pinned checker execution, source read receipts and
eligibility, append-only SQLite ledger, canonical JSONL export, byte-exact replay.
