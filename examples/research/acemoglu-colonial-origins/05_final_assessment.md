# 05 — Handoffs and final assessment: AJR (2001)

Status: exploratory, single-agent, model-produced. **No finding below is established.** Each needs independent human or expert verification.

## Chain completeness
| Stage | File | Status |
|---|---|---|
| Pre-registration | 00a_preregistration_LOCKED.txt (sha256 b9d9085f…973b531) | LOCKED at 02:56 PST, before Stage 1 |
| 1 Claim extraction | 01_claim_extraction.md | COMPLETE. Repo parser: 0 issues. Anchors: 0 MISMATCH |
| 2 Internal validity | 02a_internal_validity.md | COMPLETE |
| 2 Construct validity | 02b_construct_validity.md | COMPLETE |
| 2 Citation network | 02c_citation_network_NOT_RUN.txt | **NOT RUN** (blocker) |
| 3 Counter-audit | 03_counter_audit.md | COMPLETE. IV supplied and consumed; citation network not supplied |
| Light replication | replication/ | COMPLETE |

## Handoffs
- 01 → 02a/02b: Field 6 is Table 4 col. 1 (PDF p. 19 / journal p. 1386), 0.94 (SE 0.16), n = 64.
  - Construct handoff: PRS index ITEMS-INFERRED; mortality ITEMS-RETRIEVED (narrower construct).
- 02a → 03: seven findings plus one acquittal.
  - IV-1 is ELIGIBLE (material, contested).
  - IV-6 is PENDING.
- 02b → 03: three findings plus one acquittal. All SURVIVE for Field 6; CV-1 narrows Field 2 (PROVISIONAL).

## Outcomes after counter-audit
- **Upheld (minor/none):**
  - IV-3: the posted data have Tanzania at 280, Table A2 has 145, and the printed 0.94 reproduces only with 280. Cause UNKNOWN; immaterial.
  - IV-5: 0.95 vs 0.94 wording.
  - CV-2.
  - IV-4 is a 2011-dataset row slip and lies outside Field 6.
- **Upheld but narrowed:**
  - IV-1: fragility conditional on Albouy coding.
  - IV-7: Field 2 only.
  - CV-1: abstract wording only.
  - CV-3: self-caveated.
- **Rejected as a threat:** IV-2 (clustering), defeated by the source's fn 18 and by recomputation.
- **Unresolved:** IV-6 (exclusion restriction). PROVISIONAL and pending.
- **Acquittals upheld:**
  - IV-A: exact reproduction; weak-IV-robust AR set [0.70, 1.43].
  - CV-A: the outcome measure.
- **Verdicts:**
  - Internal validity: C (borderline B) as prosecuted, recorded as **B–C CONTESTED** after the counter-audit.
  - Construct validity: VALID for Field 6, residual B.
  - Thesis impact: C (softened).
  - Confidence: Moderate.

## Competing explanations retained
1. AJR's reading: the mortality series is a valid, relevant instrument; data-construction choices (capping, outlier treatment, campaign coding) are defensible; the effect is robust.
2. Albouy's reading: once the rates are restricted to own-country data and campaign/laborer sources are flagged, identification with geographic controls is too weak to bound the effect.
3. Direct-channel alternatives to exclusion: disease environment, human capital, settler human capital. AJR test the named ones. Human-capital alternatives (e.g., Glaeser et al. 2004) were recalled, not retrieved (PROVISIONAL).

## Unblinding against the pre-registration
| Expectation (locked) | Observed |
|---|---|
| 1. Field 6 = Table 4 2SLS ~0.94 | CONFIRMED |
| 2. Construct check triggers (index → "institutions") | CONFIRMED. It triggered, but Field 6 is worded at the index, so it narrows Field 2, not Field 6 |
| 3. IV centred on exclusion and mortality construction; dispute UNRESOLVED | CONFIRMED (CONTESTED / UNRESOLVED). This agreement with prior expectation is itself a confirmation risk (J2) |
| 4. Table 4 col. 1 reproduces; robustness depends on coding; Albouy not fully reproducible without his package | CONFIRMED. Table 4 cols. 1–9 reproduced to the printed precision, with rounding-level exceptions (col. 8: 1.11 vs 1.10; first-stage col. 5: −1.21 vs −1.20 and col. 6: −1.14 vs −1.10, cause unknown; see 02a). Albouy's specs were approximated, not reproduced. **Unexpected:** the Tanzania 280/145 data-vs-appendix discrepancy, and the Indonesia row slip in the 2011 data |
| 5. No correction or retraction | CONFIRMED within bounded search (OpenAlex is_retracted = false). Not proof of absence |

## Mechanical vs scientific validation
- **Mechanical (passed):**
  - repo checker, unit tests and receipt replays are unchanged from baseline (checks_post.log);
  - the Stage-1 output parses under the repo's strict reader;
  - all 18 quotes match the PDF text layer (4 exact, 14 after normalization);
  - replication scripts rerun deterministically.
- **Scientific (NOT established):**
  - whether the exclusion restriction holds;
  - which mortality coding is historically correct;
  - whether the PRS index measures "institutions";
  - how the field took up Albouy's critique.
  These require domain experts, Albouy's package, PRS documentation, and a citation-network run.

## Decisive next tests
1. Blinded independent recoding of the 36 assigned mortality rates.
2. Rerun with Albouy's replication package.
3. Bounded-exclusion sensitivity (e.g., Conley-Hansen-Rossi plausibly-exogenous intervals).
4. A citation-network stage with a citation-context corpus.
