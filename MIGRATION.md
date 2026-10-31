# M0 migration record

Migration of the Atlas adapter and its dependency closure from
`yungmulaBABY1/Provenance` into `yungmulaBABY1/Provenance-Atlas`. Migration
only: no instrument, schema, fixture, receipt, evidence mapping or native label
was changed. Prepared 31 October 2026.

## Source and destination

| | |
| --- | --- |
| Source repository | https://github.com/yungmulaBABY1/Provenance |
| Source commit | `cb795accd2563bfc787713f8523d7f3564030fc0` (main; merge of PR #12) |
| Source tree | `git rev-parse cb795acc^{tree}` |
| Destination repository | https://github.com/yungmulaBABY1/Provenance-Atlas |
| Destination base | `e81e6602499b69c8d1a7e2cb42dfb1f2f72e5218` (initial commit, one-line README) |
| History import commit | `267bda9f6619e698231651a9a6ce547ab2259705` |
| Pruned tree, validated | `4ff48fd6b5eff5d8ad8cba371f30c4b074c599f5` |

START_HERE Revision 1 named `c1bcb8bf` as the baseline. Main moved to
`cb795acc` before migration. Between them, Atlas paths changed only in
`tests/atlas/test_adapter.py` and `tests/atlas/test_evidence_reviews.py`
(SQLite connections now closed with `contextlib.closing`; assertions unchanged).
`atlas/` and `docs/atlas/` did not change.

## Method

**History.** The destination already had an initial commit, so Provenance main
was merged in with `--allow-unrelated-histories` instead of force-pushing.
The import commit's tree is byte-identical to `cb795acc`; the only conflict,
`README.md`, was resolved to Provenance's file and replaced later. Every
Provenance commit is reachable, including those recorded in receipts and the
baseline pin (`d7000315`, `072fa8a0`) and PR #9's merge (`b7527f4c`). No
old-to-new commit map is needed because no commit was rewritten.

**Merging this PR:** use *Create a merge commit*. *Squash and merge* would
drop the Provenance history from main; *Rebase and merge* would rewrite every
imported commit SHA. Either would break the property above.

**Keep set.** The dependency closure was measured, not inferred: `strace`
recorded every Git-tracked file opened during the three CI steps at
`cb795acc`. Of 228 tracked files, 115 were read: 66 inside `atlas/`,
`tests/atlas/`, `docs/atlas/` and `.github/`, and 49 outside them. Copies
with the three directories alone fail all 12 test modules and all six
replays (`INPUT_UNAVAILABLE`); adding the 49 files at identical paths passes
everything. The closure is sufficient for current CI; it is not proven
minimal.

Kept (198 files, all unchanged, all at original paths):

- `atlas/`, `tests/atlas/`, `docs/atlas/`, `.github/workflows/atlas-adapter.yml`
- the 49 traced files (in `compliance/`, `tests/cases/`, `prompts/`,
  `reference/`, `examples/research/shen/`, plus
  `tests/test-citation-network-checker.py`)
- all of `prompts/`, `reference/` and `FAILURES.md`: instruments, philosophy,
  methodology and failure record that START_HERE requires to travel;
  `prompts/1-claim-extraction.txt` is needed for M1
- the complete `examples/research/shen/` run: three of its files are CI
  inputs; the rest preserve the run they come from
- `.gitignore`

Paths are unchanged because receipts record input paths and test `setUp`
copies the live `prompts/research-analysis/2-citation-network.txt` from the
repository root. Validation itself uses the vendored copies in
`atlas/baseline/files/`.

Removed (30 files; still in this repository's history and in Provenance):
`webapp/provenance.html`, `.github/workflows/prompt-parity.yml`,
`tools/` (2), `deferred/` (1), `tests/runs/` (16), `tests/RESULTS.md`,
`tests/RESULTS.reconciled-candidate.md`, `tests/README.md`,
`examples/README.md`, `CHANGELOG.md`, `TODO.md`,
`current-state-inventory.md`, `TOOL-004-prompt-propagation-report.txt`,
`Revision_Log_v0.2.xlsx`.

Added: this file, a new `README.md`, and `START_HERE.txt` (Revision 1
verbatim, then Revision 2).

## Verification

Run on a fresh clone of the pruned tree (`4ff48fd`), no `.git` dependency at
runtime, in an isolated container. Later commits on this branch change only
`README.md`, `MIGRATION.md` and `START_HERE.txt`, none of which CI reads.

| Check | Result |
| --- | --- |
| Blob identity: every file in the pruned tree equals its blob at the same path in `cb795acc` | 198 / 198 |
| `git diff cb795acc -- atlas tests/atlas docs/atlas` | empty |
| Checker regression, Python 3.11.18 and 3.13.18 | `PASS` on both |
| `unittest` (tests/atlas), Python 3.11.18 and 3.13.18 | 143 tests `OK` on both |
| Content replay, six current receipts, both interpreters | 6 / 6 pass on both |
| Tracked files modified by the runs | none |
| CLI: import all six contexts into one shared ledger | exit codes 1,1,0,1,1,1 (case12, case13, power-control, power-sources, power-sources-reviewed, shen-known-bad); identical in Provenance `cb795acc`. Exit 1 is the designed quarantine of historical outputs that fail the current checker grammar |
| Shared-ledger export, destination vs Provenance `cb795acc`, same interpreter | byte-identical (103 records) |
| Export, restore, export | byte-identical |
| Fresh import vs committed receipt records | identical except one `environment.python` field per receipt (3.11.18 now, 3.11.17 when committed) |

Review detachment, conflict rejection and restore tampering are covered by
the unit suite (`test_moved_locator_stays_detached_after_export_and_restore`,
`test_conflict_rolls_back_entire_import`,
`test_restore_rejects_forged_binding` and others) and pass.

**Receipts:** none changed, none added, none regenerated. No
migration-induced difference was found, so no migration receipts were needed.

GitHub Actions on this branch is the independent check of the above; these
local results do not substitute for it.

## Known limits

- **Links to removed files (4):** `reference/philosophy.md`,
  `reference/methodology.md` (2) and `reference/architecture-note.md` link to
  `../current-state-inventory.md`. It was left behind because it is an
  August 2026 Provenance status snapshot that would misstate Atlas's state.
  It remains at
  https://github.com/yungmulaBABY1/Provenance/blob/cb795accd2563bfc787713f8523d7f3564030fc0/current-state-inventory.md.
  Carried files were not edited to repoint it.
- **Links already broken in Provenance (16):** `compliance/README.md` (14
  pilot-01..03 files) and `tests/cases/README.md` (`case_FAIL-MB-017` and
  `case_FAIL-MB-018` Ceuta case files). None of those targets exist at
  `cb795acc` either. Carried unchanged.
- `docs/atlas/contracts/` refers to paths in an earlier alternative package
  that is not present (START_HERE §5 item 7). Carried unchanged.
- Strict (byte-exact) replay was not used; it depends on the exact
  interpreter patch release. `historical-*` receipts are not replayable.
- No license file, as in Provenance.

## Not done here

Provenance status notice and pointer, archival of Provenance, release tags
and any license decision are separate deliberate actions after this
migration is reviewed and merged.
