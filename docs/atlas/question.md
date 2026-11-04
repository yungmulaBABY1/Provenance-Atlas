# Research questions (`atlas.question`)

A research question is one declared question over a declared list of sources. It
is the Research counterpart of a Media story family: the unit a question-level
page is built from. It records what Atlas already holds. It adds no judgment.

```sh
python -m atlas.question build tests/atlas/question/power-posing/context.json \
    --out tests/atlas/question/power-posing/receipt
python -m atlas.question replay tests/atlas/question/power-posing/receipt/manifest.json \
    tests/atlas/question/power-posing/receipt/records.jsonl --level content
python -m atlas.view build-all        # renders every page in docs/atlas/views/views.json
```

## What a question bundle holds (schema `atlas-question/0.1`)

| Record | Holds |
|---|---|
| `ResearchQuestion` | The question text and who worded it (`DRAFTED_BY_ASSISTANT` or `DECLARED_BY_OPERATOR`, plus confirmation); the corpus as a `DECLARED_LIST` with its selection rule; any declared claim links. |
| `QuestionMember` | One per source: Work, source versions and read outcomes, passages on record (with speaker and, where declared, subject), the checks that need this source and their eligibility, and the audit records that touch it. |
| `QuestionClaim` | A claim a model run already chose for checking, quoted as written, with the run that wrote it, that run's target paper, and any recorded identity between claims. |
| `QuestionCoverage` | Counts, each with the denominator (sources in the declared list) and the members counted. |
| `QuestionManifest` | Code hashes, the full input context, every pinned input, environment, and the record list and hash. |

Every input is pinned by SHA-256. The build checks that the import context is the
one the import run recorded, that the source packet is pinned by that import, and
it content-replays every extraction receipt it names. The extraction receipts must
link the same import and provisional-map bundles as the question does.

## Rules the validator enforces

1. **No judgment fields.** `score`, `verdict`, `rating`, `credibility`, `trust`,
   `consensus`, `support_count`, `weight`, `rank`, `stance` and `position` may not
   appear anywhere in a record (`JUDGMENT_FIELD_NOT_ALLOWED`). Positions on the
   question are a later, attributed record type.
2. **Counts recompute.** Coverage rows are recomputed from the member records on
   every validation; stored counts are never trusted (`INVALID_COUNT`).
3. **Access states follow the records.** A source with no retrieved copy and no
   passages is `METADATA_ONLY`. Passages without a retrieved copy are rejected.
4. **Words stay with their speaker.** A passage is listed under the source whose
   text it is. A passage in which one source describes another carries the
   described source as its subject. It appears under the described source as
   "described in another source" and never among its own passages
   (`MISATTRIBUTED_PASSAGE`). A subject must be backed by an import check that
   requires that passage (`SUBJECT_BASIS_INVALID`).
5. **Claim identity is declared, not inferred.** Links between claims may only use
   `DECLARED_BY_REFERENCE` or `UNRESOLVED_REQUIRES_REVIEW`, with a declarer and a
   basis. Text-identity labels need a recorded comparison, which this package does
   not make (`UNSUPPORTED_IDENTITY`).
6. **The wording is attributed.** Operator-declared wording is confirmed by
   definition; drafted wording stays `NOT_CONFIRMED` until the operator confirms it.

## The first question

`tests/atlas/question/power-posing/`: four sources (S1 Carney, Cuddy & Yap 2010;
S2 Ranehill et al. 2015; S3 Carney, Cuddy & Yap 2015; S4 Simmons & Simonsohn 2017),
the same four the power-sources import pins. The question wording was drafted by
Claude from S1's title and is not confirmed.

What the bundle records today: 2 of 4 sources have a retrieved copy and passages
on record (S2, S4). 1 of 4 (S3) is described in another source's words (S4-E2). 1
of 4 has a recorded claim extraction (S2). 1 of 4 was the target of an imported
audit (S1). 0 of 4 have a decision by a person on record. Two model-written claims
are on record, from runs with different target papers, recorded as not the same
claim.

## The page

`docs/atlas/views/power-posing/` (see [view.md](view.md)). It shows no source
text: the passages are bounded excerpts not reviewed for public release, so they
are listed by label, page and match result. The S2 audit record links down to the
S2 page; that page carries a breadcrumb back with the same denominator.

## Limits

- One question, built from records that already existed; no search, no new runs.
- No positions, no lineage or independence assessment, no cross-source claim
  identity. Those are the next attributed record types.
- The selection rule is "what Atlas already holds"; the passages on record were
  chosen for the imported audit, not for this question. The page says both.
