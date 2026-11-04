# Atlas integration status: AJR 2001 audit

Repository: yungmulaBABY1/Provenance-Atlas @ ce028e1 (branch audit/acemoglu-colonial-origins).
Atlas code, schemas, validation rules, prompts and existing receipts were **not modified**. No receipt was written for this run.

| Atlas surface | Contract (read in code/docs) | Status for this run | Reason |
|---|---|---|---|
| `python -m atlas import <context> --out` (atlas/adapter.py) | Imports pinned **citation-network** native output only. The output must pass prompts/research-analysis/check-citation-network-output.py, PROMPT is 2-citation-network.txt, and the context keys are modelled on tests/atlas/power-sources.json | **BLOCKED** | No citation-network output exists (02c NOT RUN). Claim-map, internal-validity, construct-validity and counter-audit outputs have no import adapter |
| `python -m atlas.claims build` | Links one pinned *import bundle* | **BLOCKED** | It depends on an import bundle, and none exists |
| `python -m atlas.extraction local / build` (context schema atlas-extraction-context/0.1) | The context requires `links.import_bundle`, `links.provisional_map_bundle` and a sources packet with excerpts (build.py lines ~200–202, 262, 358) | **BLOCKED** | Both mandatory links exist only for the power-posing fixture. Pointing them at power-posing bundles for an AJR extraction would fabricate provenance |
| Evidence check `reported-statistics-consistency/1` (atlas/extraction/stats.py) | Scope is one two-sample t test (mean difference, 95% CI, t(df), p, d) | **NOT_CHECKABLE** (gap) | IV coefficient and SE are outside scope. Scratch probe: atlas_probe/stats_check_probe.json |
| Output parser `atlas.extraction.output.parse` (atlas-claim-extraction-output/1) | Strict reader for the Stage-1 output format | **USED AS LIBRARY (scratch)**: 0 parse issues; table fields 1, 2, 3, 4, 5A, 5B, 6; Field 6 USABLE; 5 summaries | Confirms format conformance only; no receipt |
| Anchor matcher `atlas.extraction.anchors.match` (nfc-whitespace/2) | Quote vs pdftotext layer; page from form feeds | **USED AS LIBRARY (scratch)**: 18 quotes, 4 MATCH, 14 NORMALIZED_MATCH_ONLY, 0 MISMATCH, 0 page inconsistencies | atlas_probe/anchor_probe_01.json (output sha256 f6e7df18…, text-layer sha256 d33c1a05…) |
| Replays (`atlas replay`, `atlas.claims replay`, `atlas.extraction replay`) | Recompute the existing receipts | **RUN, PASS**: existing receipts are unchanged | See checks log. These validate the *existing* fixtures, not this audit |

## Blockers (recorded, not worked around)
1. **B-ATLAS-1.** No adapter exists for Stage-1, Stage-2 IV/CV or Stage-3 native outputs. Only the citation-network output is importable.
2. **B-ATLAS-2.** The citation-network stage was not run (see 02c), so the only importable path has no input.
3. **B-ATLAS-3.** The extraction receipt pipeline is hard-wired to an import bundle and a provisional map bundle, which are unavailable for AJR.
4. **B-ATLAS-4.** The statistics check covers t-tests only. IV/2SLS estimates, first-stage F and AR sets have no declared check.
5. **B-ATLAS-5.** There is no contract for replication outputs: scripts, datasets and estimate tables. replication/results.json is a run-local format.

## Mechanical versus scientific
Every PASS above is mechanical. It shows that the repo's tests and replays still reproduce their fixtures, and that this run's Stage-1 text parses and its quotes match the PDF text layer. None of it verifies any scientific finding in this audit.
