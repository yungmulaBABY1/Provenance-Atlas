# Claim links (`atlas.claims`) — M1 Increment A

Deterministic, offline linking of an imported audit's own claim statements to
its findings and to the reviews bound to them. It points; you judge.

It does not run an audit, extract claims from a paper, call a model, or decide
whether two differently worded statements are the same claim. Every such case
is recorded as `UNRESOLVED_REQUIRES_REVIEW`.

## Run it

```sh
python -m atlas.claims build tests/atlas/claims/power-posing-reviewed.json --out .atlas/claims
python -m atlas.claims show .atlas/claims/records.jsonl            # verified view
python -m atlas.claims show .atlas/claims/records.jsonl --unverified
python -m atlas.claims replay .atlas/claims/manifest.json .atlas/claims/records.jsonl --level content
```

`show` replays the bundle at content level from the inputs it pins (resolved
from `--root`, default the current directory) and renders only if every record
re-derives; otherwise it prints `NOT_VERIFIED` and renders nothing. A verified
view says which inputs it was derived from and that verification covers
recording, not correctness. `--unverified` renders stored labels as written,
under an `UNVERIFIED RENDERING OF STORED ASSERTIONS` banner that comes before
any label; use it for a bundle whose inputs you do not have.

## What it reads

- **One import bundle**, pinned by the SHA-256 of its `manifest.json` and
  `records.jsonl`. The bundle is re-validated and its native projections and
  review bindings re-derived (`atlas.integrity.verify_records`) before use. A
  changed byte without a new pin fails `INPUT_HASH_MISMATCH`; a re-pinned but
  tampered bundle fails `DEPENDENCY_INVALID`.
- **The claim-extraction contract** (`prompts/1-claim-extraction.txt`), pinned
  by hash. Its seven output-table rows (1, 2, 3, 4, 5A, 5B, 6) are checked in
  the bytes on every build; they define which fields a full map would have.
- **The audit output text**, taken from the bundle's `AuditRun` (hash-checked
  there), never re-read from the working tree.

## What it parses

Only what the citation-network instrument itself specifies
(`prompts/research-analysis/2-citation-network.txt`, vendored baseline): the
**degraded standalone fallback** (`CLAIM MAP: SELF-GENERATED — PROVISIONAL`,
fields 1, 3 and 6 only) and the four **PRE-AUDIT CLAIM CONFIRMATION** lines.
Hyphen, en dash and em dash separators, and same-line or indented
continuation text, are accepted. Anything else is reported in `parse_issues`
and left unparsed. A full upstream claim map pasted into an output is not
parsed by this version.

Each field number must carry its instrument label (1: *What was literally
measured*, 3: *Weaker defensible claim*, 6: *Claim under audit*; case and
spacing differences are accepted and recorded as `CASE_OR_SPACE_ONLY`). Every
entry is kept as a `ClaimStatement`, and each field gets a status:

| Status | Meaning | Linkable |
| --- | --- | --- |
| `USABLE` | One non-empty entry with its own label | yes |
| `LABEL_MISMATCH` | Label belongs to another field or none | no |
| `DUPLICATE_ENTRIES` | More than one entry for the number; all kept, in order, none preferred | no |
| `EMPTY` | No text | no |
| `OUTSIDE_FALLBACK` | A field number the fallback does not define (2, 4, 5A, 5B) | no |

Only `USABLE` statements may be compared or designated as the audited claim.
Any other Field 6 leaves the findings with no designated target
(`designated_target_state` names why; the conflicting entries are listed as
candidates, not linked), and a bare "Claim map field 6" reference becomes
`UNRESOLVED_REQUIRES_REVIEW`. A map with any defect is `PRESENT_WITH_DEFECTS`.
Confirmation lines follow the same rule. The validator enforces this: a
comparison or designation that touches a non-`USABLE` statement, or a
`SAME_TEXT*` identity without the comparison that backs it, is rejected.

## Records (`atlas-claimlink/0.1`)

| Type | Holds |
| --- | --- |
| `ClaimLinkRun` | Dependency identity and status, method, whether a source (paper) statement is available and why not, counts by claim identity |
| `ClaimMap` | The output's own map: state, native label, fields present, fields absent with reason, reconciliation state, parse issues |
| `ClaimStatement` | One statement as written: role, native label, field status, exact text and hash, code-point span in the output, who wrote it (the audit run). ID is run + role/occurrence + text hash: changed wording gets a new identity, and identical sentences in different runs or roles stay distinct records |
| `TextComparison` | Exact and `nfc-whitespace/2` comparison of two statements: `MATCH`, `NORMALIZED_MATCH_ONLY` or `MISMATCH`. Semantic equivalence is `UNASSESSED` unless the text is identical |
| `TargetAlignment` | Per finding: target kind, designated target and its state (or candidates when ambiguous), comparisons, claim identity, the output's own mentions of Field 6, bound and detached reviews |
| `ReviewScope` | Per review: binding, the finding field and span it reviews, its parts and dispositions, reviewer, and whether it reviews the target claim |
| `ClaimLinkManifest` | Code, parser, contract and dependency identities; environment; record list and hash |

Claim identity values:

| Value | Meaning |
| --- | --- |
| `SAME_TEXT` | Finding target text is byte-identical to Field 6 |
| `SAME_TEXT_AFTER_NORMALIZATION` | Identical after NFC and whitespace collapse only |
| `DECLARED_BY_REFERENCE` | Target cell says "Claim map field 6" with nothing added; the output's declaration, not verified |
| `DECLARED_NOT_ON_MAP` | Target cell begins `MAP GAP:` — the instrument's own flag |
| `UNRESOLVED_REQUIRES_REVIEW` | Anything else, including qualified references and paraphrase |
| `NO_TARGET_STATED` | No target claim field |

Three layers stay separate: what a paper says (`ClaimLinkRun.source_statement`;
not available in any current fixture), the claim the audit says it is auditing
(Field 6), and how a reviewer decomposed a statement (`ReviewScope.parts`).

## The development case: power-posing, run `:3`

What the records show (see `python -m atlas.claims show`):

- The map is the run's own standalone fallback: fields 1, 3, 6; fields 2, 4,
  5A, 5B absent by instrument design; no claim inventory; not reconciled.
- Both findings' target claims differ in wording from Field 6 (`MISMATCH`) and
  match the confirmation restatement after normalization only. Claim identity:
  `UNRESOLVED_REQUIRES_REVIEW`. Finding 1's own text says it was "classified
  DEFEATS for Field 6 wording"; that is kept as the output's assertion.
- Each of Fields 1, 3 and 6 is restated differently in the confirmation
  block (`MISMATCH`). Field 3's "may increase" is restated as "may affect".
  Whether those are the same claim is not decided here.
- The two model reviews bind to Finding 1's Evidence field, characters
  [0, 80) (the S2 clause), not to the target claim. Their disagreement
  (`SUPPORTS_WITH_QUALIFICATION` vs `SUPPORTS`) is preserved.
- The paper's own statement is unavailable: no Field 2, and the target work
  (S1) was `RETRIEVAL_FAILED` in the recorded retrieval.
- The dependency run is `QUARANTINED` (syntax `FAIL`) with producing-instrument
  compliance `UNDETERMINED`. Linking does not change that.

Real controls in the tests, from the other committed receipts: case 12 (sub-claim
targets, all unresolved), Shen known-bad (no map in output, off-spec
confirmation block reported, reference targets, one `MAP GAP`), and the
unreviewed power-posing run (no decomposition).

## Limits

- Statement IDs are scoped to a run and a role. They are not global claim
  identities and must not be used to merge identical sentences across runs;
  semantic claims, when introduced, need their own records.
- Text comparison is not meaning. A paraphrase and a scope change look the
  same here: both are `MISMATCH`.
- Content-addressed statement IDs give changed wording a new identity;
  records with stable IDs that depend on it change content, so merging two
  builds is an ID/content conflict, never a silent update. There is no claim
  ledger yet: bundles are files, not appended to the import ledger, because
  that would require new record types in `atlas/contract.py` and so new import
  receipts.
- The package sits in `atlas/claims/` because import receipts pin every
  `atlas/*.py` file (non-recursive). A test asserts that pin is unchanged.
- No executor, no new claim extraction, no report beyond `show`. Those are
  Increments B and C.
