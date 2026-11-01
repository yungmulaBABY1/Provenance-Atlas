# Provenance Atlas

*It points; you judge.*

Provenance Atlas is an open evidence-linked record for research and media
investigation: sources, claims, audit findings, reviews, disagreements and
corrections, kept separately and kept inspectable. It does not issue
automated verdicts or credibility scores.

Start with [`START_HERE.txt`](START_HERE.txt). It is the project map, the
current status and the next build brief.

## What exists now

Implemented, with mechanical test coverage:

- A deterministic adapter that imports existing Provenance citation-network
  audit outputs, keeps their native labels as written and runs the pinned
  checker against a vendored baseline.
- Work, source-version, passage and source-read records; per-check source
  eligibility; exact versus normalized text matching.
- An append-only SQLite ledger with JSONL export, restore and replay.
- Attributed evidence reviews bound to an exact finding span and passage
  descriptors.
- Claim links (`atlas.claims`): an imported audit's own claim statements
  linked to its findings and bound reviews by exact and normalized text
  comparison, with mismatches recorded rather than resolved
  ([docs/atlas/claims.md](docs/atlas/claims.md)).

Not implemented: running a new audit or claim extraction, any user interface,
human adjudication, public release controls. Import is not a model
audit, and passage matching is not evidentiary support. See
[`docs/atlas/README.md`](docs/atlas/README.md) for the full scope and limits.

## Run the checks

Python 3.11 or later. Standard library only; no network access. (The
power-posing packet's optional external re-verification script,
`tests/atlas/sources/power-posing/source_packet.py`, additionally needs
network access and Poppler. CI does not run it.)

```sh
python tests/test-citation-network-checker.py
python -m unittest discover -s tests/atlas -p 'test_*.py'
for dir in tests/atlas/receipts/*/; do
  case "$dir" in */historical-*/) continue ;; esac
  python -m atlas replay "${dir}manifest.json" "${dir}records.jsonl" --level content
done
for dir in tests/atlas/claims/receipts/*/; do
  python -m atlas.claims replay "${dir}manifest.json" "${dir}records.jsonl" --level content
done
```

Expected: checker regression `PASS`, 187 tests `OK`, six import content
replays and one claim-link content replay pass. `historical-*` receipts were produced by earlier code and are not
replayable. CI runs the same steps (`.github/workflows/atlas-adapter.yml`).

## Layout

| Path | Contents |
| --- | --- |
| `atlas/` | Adapter, ledger, replay, reviews; `baseline/` holds the vendored pinned instrument files |
| `tests/atlas/` | Tests, import contexts, source and review packets, committed receipts |
| `docs/atlas/` | Adapter documentation, changelog, contract notes |
| `prompts/`, `reference/`, `FAILURES.md` | Provenance instruments, philosophy, methodology and failure record, carried unchanged |
| `compliance/`, `tests/cases/`, `examples/research/shen/` | Fixtures and inputs the tests and receipts read, at their original paths |

Files outside `atlas/`, `tests/atlas/` and `docs/atlas/` are kept at their
Provenance paths because receipts record those input paths. Moving them is a
versioned change with new receipts, not housekeeping.

## Origin

This repository continues the Atlas work begun in
[yungmulaBABY1/Provenance](https://github.com/yungmulaBABY1/Provenance), which
is now a frozen reference implementation. Provenance's full history is merged
here unchanged, so every commit referenced by a receipt resolves in this
repository. [`MIGRATION.md`](MIGRATION.md) records exactly what was carried,
what was left behind and how the migration was verified.

## License

There is no license file yet, as in Provenance. Do not infer permissions from
the repository being public. Third-party excerpts in the source packets keep
their own terms.
