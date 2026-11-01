# Recorded claim extraction (`atlas.extraction`) — M1 Increment B

One claim-extraction run on one real paper, recorded with its packet, checked
against the source, linked to earlier records, and given one declared evidence
check. It points; you judge.

This code never calls a model. A run is executed by a declared runner on a
fixed packet; the code records what came back.

## The run (`tests/atlas/extraction/s2-run1/`)

| | |
| --- | --- |
| Paper | S2, Ranehill et al. (2015), doi:10.1177/0956797614553946 |
| Source bytes | PDF sha256 `4ae91126…1369`, 374,723 bytes: byte-identical to the 2026-10-30 retrieval in the power-posing packet. Not redistributed |
| Extraction | `pdftotext -enc UTF-8` 24.02.0, output sha256 `afc448e6…b3ad` (same as recorded) |
| Instrument | `prompts/1-claim-extraction.txt`, blob `894579a7`, unchanged |
| Run prompt | `run-prompt.txt` (sha256 `182ffff4…`): instrument inputs, no retrieval, two added sections (SOURCE ANCHORS, READ RECORD). Names no paper, author, prior source or result |
| Runner | "Opus 5.5 Extra" on claude.ai, incognito, first attempt: all **operator-stated**, not verified |
| Exposure | The run reports prior exposure to the paper from training data. Independence not established |
| Preflight | The run could not hash the instrument: `INSTRUMENT VERSION UNVERIFIED`. The operator attests the attached file was the pinned one; that is recorded as an attestation |

## Two stages, because the source is not redistributed

**Local** (`python -m atlas.extraction local|local-verify`, needs the private full
output and the PDF): checks both hashes, re-runs pdftotext and checks the
extraction hash, matches every quoted anchor, and writes the public files.
`local-verify` recomputes them and requires every byte to match.

**Public** (`build|replay|show`, committed files only; CI replays it): parses the
redacted output, re-checks every published quote against a public excerpt and
every withheld quote's placeholder against its recorded hash, links to earlier
records, and runs the evidence check.

### Source-light publication

- The full output (39,090 bytes; 48 block quotes, about 37% of the article's
  extracted text) stays private. Its sha256 (`6b3b9d6c…`) is pinned.
- `output-redacted.md` is the output with each block quote replaced by its
  sha256 and length, except quotes lying inside an excerpt that is already
  public: four inside the packet's S2-E2/S2-E3, and A2.3, committed here as the
  evidence excerpt (`A2.3-excerpt.txt`, 361 bytes, the exact extraction span).
- Short inline quotations inside the run's own analysis text are kept, the
  longest being the article title (75 characters).
- Anyone with the same PDF can re-run `local-verify`.

## Anchor results

Of 60 SOURCE ANCHORS entries: 48 quotes, 6 cross-references, 5 absence findings,
1 reconstruction. Of the 48 quotes:

| State | n | Meaning |
| --- | --- | --- |
| `MATCH` | 8 | exact substring of the extraction |
| `NORMALIZED_MATCH_ONLY` | 36 | equal after NFC + whitespace collapse (line breaks) |
| `MISMATCH` | 4 | neither; recorded, not repaired |

All 44 located quotes are on the page the run stated. The four mismatches carry
a labelled heuristic diagnostic; on inspection they are text-layer effects:
- A1.2: the run restored a compound hyphen the text layer drops; the run flagged this itself.
- A1.4: the sentence is interrupted by a "Downloaded from…" page stamp in the extraction.
- A2.8 and A2.11: the extraction has soft hyphens (U+00AD) the run omitted.

No dehyphenation, stamp removal or fuzzy matching is applied.

## Links

- **To the reviewed import (run `:3`).** Four anchors (A2.2, A2.10 in S2-E2;
  A2.6, A2.7 in S2-E3) lie inside the passages both model reviews are bound to.
  Each `PassageLink` puts three layers side by side: the paper's statement (the
  anchor), the claim this run audits (its Field 6), and each reviewer's
  decomposition (review parts). The relation is offset containment in the same
  extraction; it says nothing about support. Review disagreement and
  `human_adjudication NOT_RECORDED` are carried as they are.
- **To the historical provisional map.** That map belongs to the citation-network
  run whose target is S1 (Carney et al. 2010). This run's target is S2.
  `CrossMapAlignment`: `DIFFERENT_TARGET_WORKS`, claim identity
  `NOT_THE_SAME_AUDIT_TARGET`. The old map is read from its pinned receipt and
  left unchanged.

## Evidence check `reported-statistics-consistency/1`

Declared target: the run's Field 6 section statement (the testosterone-change
result, t(196) = −1.405, p = .162). Evidence: A2.3, the Results sentence,
testosterone clause.

| Sub-check | Result |
| --- | --- |
| TRANSCRIPTION — every statistic in Field 6 equals the source's | CONSISTENT |
| P_FROM_T — two-tailed p from t and df: [0.16146, 0.16175] vs reported [.1615, .1625] | CONSISTENT |
| T_FROM_CI — t implied by mean and 95% CI: [−1.40498, −1.40439] vs reported [−1.4055, −1.4045]; CI centred on mean | CONSISTENT |

Values are compared as rounding intervals. The t distribution is computed with
the standard library (regularized incomplete beta); tests pin it against scipy
reference values to 1e-10. Not checked: Cohen's d (group sizes are not in the
main text), the data, the choice of test, and whether a non-significant result
shows the absence of an effect.

## Limits

- One run, one model, one paper. Nothing here measures extraction accuracy in
  general, and a consistent arithmetic check does not make the claim true.
- Runner identity and run conditions are the operator's statements.
- The local stage needs poppler 24.02.0 to reproduce the extraction hash.
- Field 4 (downstream uses) is provisional by design: the run had no retrieval.
