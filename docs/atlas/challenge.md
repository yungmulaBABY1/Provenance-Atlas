# Challenges (`atlas.challenge`) — M1 Increment C part 2

Attributed decisions on the items an imported audit leaves for human review. It
points; you judge. Here, "you" is literal: this code records decisions and makes none.

## Run it

```sh
python -m atlas.challenge show tests/atlas/challenge/ajr2001/receipt/records.jsonl
python -m atlas.challenge template tests/atlas/challenge/ajr2001/context.json 2   # blank artifact for item 2
python -m atlas.challenge build tests/atlas/challenge/ajr2001/context.json --out tests/atlas/challenge/ajr2001/receipt
python -m atlas.challenge replay tests/atlas/challenge/ajr2001/receipt/manifest.json \
    tests/atlas/challenge/ajr2001/receipt/records.jsonl --level content
```

## What it reads

- **One import receipt**, pinned and **content-replayed** in every build
  (`IMPORT_RECEIPT_NOT_VERIFIED`).
- **The review items:** the vendored checker (`atlas/baseline.json`) is re-run on the
  run's own output bytes. Its result must equal the recorded checker status
  (`CHECKER_RESULT_DIFFERS`). Each `REVIEW_ITEM_n` line becomes one item.
- **Challenge artifacts** (`atlas-challenge-artifact/0.1`), each pinned by hash. A
  challenger writes one per decision. `template` prints a blank one bound to the
  exact item.
- **The declared code author**, so that a decision can be refused if its challenger
  declares that identity.

## What it records

| Record | Contents |
|---|---|
| `ReviewItem` | The checker's line verbatim, with its hash, code and instruction, bound to the output and checker hashes. Always has a `challenge_state`: `NOT_CHALLENGED` or `CHALLENGED`. Lists its attached challenges, their outcomes as written, and any detached challenges. |
| `Challenge` | One decision on one item. The fields are listed below. |
| `ChallengeRun` | Dependency pins, the checker re-run, and counts recomputed from the records: items, items not challenged, items with a decision by a person, challenges, detached challenges, and outcomes. |

`Challenge` fields:
- **Binding:** `MATCH` or `TARGET_MISMATCH`, naming what differs (run, output, checker,
  item number, code, text).
- **Who decided:** challenger, kind (`PERSON` / `MODEL_AGENT`), and relation to the run
  (producer, Atlas code author: `YES`/`NO`/`UNKNOWN`, declared and not verified).
- **Recording:** who wrote the file, and when the decision was made.
- **Exposure:** what the challenger saw before deciding, and any prior position.
- **The decision:** outcome, optional parts, reasons (required), evidence that must
  resolve, and what would change it.
- **Effect:** always "appended".

Outcomes: `CONDITION_MET`, `CONDITION_MET_WITH_QUALIFICATION`, `CONDITION_NOT_MET`,
`CANNOT_DETERMINE`. They answer the item's own instruction. They are not finding-level
or paper-level judgments.

## Rules

- **Two parties cannot decide:** the run's producer (`PRODUCER_CANNOT_CHALLENGE_OWN_RUN`)
  and the declared author of this code (`CODE_AUTHOR_CANNOT_DECIDE`). Relations and
  identities are declared, so this guards against honest error, not deception.
- **Changed targets detach:** a challenge whose target no longer matches is kept and
  shown, detached. It never counts toward the item.
- **Disagreements stay visible:** several challenges on one item are all kept, with
  their own outcomes. Nothing merges them.
- **Nothing is replaced:** the import's run, checker status and findings stay as they
  are, and no field in them changes.
- **No scores:** no `score`, `verdict` or similar field is allowed anywhere, in
  artifacts or records.
- **Counts recompute:** every count is recomputed from the records on validation.

## The AJR 2001 case

The checker leaves three items on Grok's citation-network run:
`SOURCE_LOCK_TRUTH`, `DIRECT_ADJUDICATION_SUBSTANCE` and `NESTING_SUBSTANCE`. The
committed receipt records all three as **`NOT_CHALLENGED`**; no decision has been made.
The reviewer packet is
[challenge-packets/ajr2001-review-items.txt](challenge-packets/ajr2001-review-items.txt).
It gives each item verbatim, where to look, and the questions. It contains no
assessment by the code author.

## Limits

- Only checker review items can be challenged in 0.1. Finding-field challenges on
  extraction runs (the original S2 target of Increment C part 2) need a second target
  kind.
- Identity and independence are self-declared, and the time of a decision is as
  stated.
- No view page yet. `show` is text only.
