# STAGE 2 — CONSTRUCT-VALIDITY AUDIT (CLAIM VS. MEASUREMENT)
## Target: AJR (2001), Table 4 col. 1

INSTRUMENT PREFLIGHT: prompts/research-analysis/2-construct-validity.txt @ commit ce028e1294873df0143ca1ae00d6abf74a910563 | blob 7f3db5ed66db3cb4c5ca84f9e71760d134ced9c8 (sha256 8f87676ae76ecf745748a58a7e68b285255c324da25a92a22f3d1a797f6feadb) | 1255 lines | 44222 bytes | markers PRESENT | IDENTITY CONFIRMED

Declared inputs: the claim map 01_claim_extraction.md (full-sequence mode, not degraded) and the source AJR 2001 (S1). Also used: Albouy 2012 (S5) and AJR 2012 (S8, S9) for instrument coding rules, and the downstream item R3 (2024 Prize press release).

The internal-validity output (02a) is NOT a declared input. It was written earlier in the same session by the same agent, so it was visible. Its findings are not imported here, and its verdict is not used as a premise. Process independence is NOT_ESTABLISHED. This is a disclosure; a contamination check is not possible.

Source retrieval-basis preflight:
- AJR 2001 full text: FULL-TEXT-CONFIRMED.
- PRS/ICRG expropriation-risk items and codebook: NOT RETRIEVED, so the index's operationalization is ITEMS-INFERRED.
- Mortality coding rules: ITEMS-RETRIEVED (Table A2 values; Albouy 2012 and AJR 2012 appendix give source-by-source coding).

APPLICABLE-CHECKS NOTE
- Target document type: an empirical cross-country IV study (primary study).
- Sections that apply: 1–3, 4 (level of analysis), 5 (confounds, construct side only), 6, 7, 9 (limited), 11–16.
- Sections that are N/A:
  - Construct properties WRONGNESS, HARM and PREVALENCE are N/A, because these are belief/attitude-construct properties and the constructs here are institutional and macroeconomic.
  - P2 grade-before-assert is N/A, because no belief is graded.
  - Section 8 (cross-reanalysis object) is applied only briefly: Albouy and AJR analyse the same object.

1. CLAIM MAP (received)
Field 6: "In the base sample of 64 former colonies, the 2SLS estimate of the effect of average protection against expropriation risk (1985–1995) on log GDP per capita (PPP) in 1995, instrumenting with log settler mortality, is 0.94 with a standard error of 0.16 (Table 4, column 1)."
- Dependence: the map hands off FORM as ESTABLISHED-CITED (the "cluster of institutions" in fn 3) and gives the expropriation index as ITEMS-INFERRED.
- Retrieval cap: the PRS items were not fetched, so construct findings about the index are capped at PROVISIONAL.
- ESTABLISHED-CITED split: fn 3 asserts that expropriation risk "is related to all these institutionalfeatures" and cites AJR (2000) for "similar results with other institutionsvariables". AJR 2000 Tables 4a–e were not retrieved. The cited support is therefore UNCHECKED, not classified as contested or uncontested.
- Not-firing condition: Field 6 as worded names the measured index, not "institutions". The construct-validity audit therefore cannot find a definition-operationalization mismatch INSIDE Field 6. The relabel to "institutions" sits in Field 2 (abstract and conclusion). It is reported below as context, not as a defeat of Field 6.

2. MEASUREMENT EXTRACTION
- Outcome: log GDP per capita (PPP) in 1995 (Table A2 header; FULL-TEXT-CONFIRMED). This is a standard measure with no construct gap relative to "income per capita".
- Regressor: the PRS "risk of expropriation" index, averaged over 1985–95, on a 0–10 scale. It is "specifically for foreign investment" (fn, PDF p. 11). The authors cite Knack and Keefer for the claim that foreign and domestic expropriation risks are highly correlated (Knack and Keefer not retrieved). Items are ITEMS-INFERRED.
- Instrument: 19th-century annualized mortality per 1,000 among European soldiers (some in barracks, some on campaign), Latin American bishops (benchmarked), and in a few cases African laborers. The rates are partly assigned from neighbouring or similar places. ITEMS-RETRIEVED.

3. CLAIM VS. MEASUREMENT TABLE

| Claimed construct | Measured | Scope result | Basis |
|---|---|---|---|
| "institutions" (Field 2) / "protection against expropriation risk" (Field 6) | PRS index of expropriation risk for foreign investors, 1985–95 | UNKNOWN for "institutions" (ITEMS-INFERRED); coextensive for the Field 6 wording | ITEMS-INFERRED |
| "potential settler mortality" (theory) | soldier/bishop/laborer mortality, earliest available, partly assigned | narrower | ITEMS-RETRIEVED |
| "income per capita" | log GDP pc PPP 1995 | coextensive | ESTABLISHED-REPORTED |

4. LEVEL-OF-ANALYSIS CHECK
The analysis is at country level, and the coefficient is a cross-country average conditional effect. The conclusion's policy reading moves from a long-run cross-sectional equilibrium relationship to intervention: it cites "substantial economic gains from improving institutions, for example as in the case of Japan during the Meiji Restoration or South Korea". The paper itself flags that institutions are a "black box" and that the results "do not point out what concrete steps would lead to an improvement". This is an intervention ratchet in the conclusion, partly self-caveated. It is outside Field 6.

5. CONFOUND AUDIT (construct side)
For the construct reading, an omitted confound would make the PRS index stand in for something else correlated with it, such as general state capacity or the perceived business climate. Expert ratings may carry a halo from income. With a valid instrument, rating error that is uncorrelated with the instrument does not bias the 2SLS coefficient. It does change what one unit of the index MEANS. Retrieval basis: author inference (theoretical).

6. ECOLOGICAL VALIDITY CHECK
The sample is former colonies only. The paper explicitly conditions on colonization (fn 2, "there is no selection bias here", read as a scope statement). It does not generalize to never-colonized countries. No failure is found for Field 6.

7. DECISIVE-TEST CHECK
The decisive construct test would show that the coefficient is similar across independent operationalizations of institutions with the same instrument. The paper reports constraint-on-executive and other measures: fn 19 gives 0.87, and fn 22 says "results … very similar". These alternatives are only partly read in the text. The tables for them (AJR 2000 Tables 4a–e) were not retrieved, so the decisive test is PARTIALLY reported, PROVISIONAL.

9. CITATION-USE AUDIT
Only one downstream item was retrieved (R3, the Prize press release). It credits the laureates' body of work, not AJR 2001 by name. This is NOT ASSESSED for this paper.

10. IGNORED-LITERATURE CHECK
Not assessed by retrieval. A human-capital alternative (settlers brought human capital, not institutions) is recalled from training memory (e.g., Glaeser et al. 2004). It is PROVISIONAL, was not retrieved, and is non-anchoring.

11. EVIDENCE-TYPE, VERIFICATION, FAILURE-LOCATION
The evidence is a primary study. Every finding below locates in the PAPER. None is PR/media or model.

12. INTERNAL CONSISTENCY CHECK
The baseline is stated as 0.95 on p. 26 versus 0.94 in Table 4 (claim-map anchor A5.1). This is wording only, severity none.

13. THE CONCEDE TEST

| Finding | Concede result | Scope loss / surviving claim |
|---|---|---|
| CV-1 The "institutions" label rests on a single PRS foreign-investor expropriation index whose items were not retrieved | SURVIVES for Field 6 (worded at the index); NARROWS the Field 2 abstract claim | Field 2 surviving claim: "large effects of protection against expropriation risk (a proxy the authors take to index a broader institutional cluster)". Scope loss: incidental for Field 6 |
| CV-2 The instrument construct (potential settler mortality) is measured by soldier/bishop/laborer mortality, partly assigned | SURVIVES for Field 6 | An instrument does not need construct fidelity to be valid, only relevance and exclusion. The narrower construct matters for the mechanism claim (deferred) and for how plausible the exclusion restriction is (an internal-validity matter, not imported) |
| CV-3 Intervention ratchet in the conclusion (cross-sectional coefficient → policy gains) | SURVIVES for Field 6 | Self-caveated by the "black box" passage |
| CV-A Acquittal: the outcome measure is coextensive with "income per capita" | — | — |

SCOPE-LOSS ASSESSMENT: no NARROWS applies to Field 6. CV-1 narrows Field 2 incidentally.

14. VERDICT
- Claim under audit: VALID (Field 6 as worded: an estimate on the named index)
- DEFEATS finding(s), if any: none
- Failure mechanism: none for Field 6. For the Field 2 relabel: insufficient information (PRS items not retrieved)
- Surviving residual: the Field 6 claim as stated
- Residual usefulness grade: B (partial evidence with clear limits: the regressor's items were not retrieved, and the construct reading as "institutions" is ITEMS-INFERRED)

Explanation: the claim map deliberately targeted the quantified Table 4 estimate, which is worded at the measured index. At that wording, the construct prosecutor finds no mismatch between claim and measurement. The construct-side vulnerability is the abstract's relabel of a foreign-investor expropriation index as "institutions". That vulnerability is real but PROVISIONAL, because the index items were not retrieved, and it belongs to a deferred claim. This is an acquittal for Field 6 at the construct layer, not an endorsement of the broader claim.

15. PAPER-SAFE WORDING
A. Neutral: In 64 former colonies, AJR estimate that a one-point higher 1985–95 PRS protection-against-expropriation score is associated, via settler-mortality IV, with about 0.94 higher log GDP per capita in 1995.
B. Critique: The paper relabels a single foreign-investor expropriation-risk rating as "institutions", and the support for that equivalence is cited rather than shown in the paper.
C. Adversarial: "Large effects of institutions" is an estimate on one investor-risk rating whose construct breadth the paper asserts rather than demonstrates.
D. Decisive test: Re-estimate with several independently constructed institution measures (item-level documented) under the same instrument, and report weak-IV-robust sets for each.

16. FAILURE-MODE CLASSIFICATION
- [x] Proxy problem: the expropriation index as proxy for an institutional cluster (PROVISIONAL; ITEMS-INFERRED).
- [x] Intervention ratchet: the policy gains in the conclusion, self-caveated.
- [x] Construct-establishment gap. Property: FORM. Status: ESTABLISHED-CITED (cited support unchecked).
- Not marked: fatal proxy failure, citation laundering, premise laundering, motive claim.

Verification flags: [x] Load-bearing evidence remains PROVISIONAL (for the Field 2 construct reading only). [x] Full source required (PRS codebook; AJR 2000 Tables 4a–e). [x] Reception check required (downstream items naming AJR 2001).

17. FINAL OUTPUT FORMAT
- Claim under audit status: VALID
- DEFEATS finding(s): none
- Surviving residual: Field 6 as stated
- Residual usefulness grade: B
- Strongest defensible claim: the Field 6 estimate on the named index
- Claim being overextended: "large effects of institutions" (Field 2), conditional on the proxy
- Definition-operationalization mismatch: UNKNOWN (ITEMS-INFERRED) for "institutions"; narrower for "potential settler mortality"
- Construct-establishment gap: FORM; ESTABLISHED-CITED; cited support unchecked
- Grade-before-assert outcome: N/A
- Main proxy problem: a foreign-investor expropriation rating standing for institutions
- Main level-of-analysis problem: cross-country coefficient → intervention gains (conclusion only)
- Main omitted confound: construct side only, rating halo (does not bias a valid IV, but changes meaning)
- Decisive test: as in 15D
- Citation-use verdict: not assessed
- Load-bearing finding(s): none for Field 6
- Concede-test result: SURVIVES (all)
- Failure location: PAPER (Field 2 wording)
- Overall verdict: VALID for Field 6; Field 2 construct reading PROVISIONAL
- Confidence level: Moderate
- What would change this assessment: PRS items showing that the index captures something narrow and investor-specific that diverges from other institution measures; or the AJR 2000 alternative-measure tables showing divergent estimates.

FINAL SECTION: STANDARDIZED FINDING TABLE

| Field | CV-1 | CV-2 | CV-3 |
|---|---|---|---|
| Finding | "Institutions" operationalized by one PRS foreign-investor expropriation index | Instrument measured as soldier/bishop/laborer mortality, partly assigned, standing in for potential settler mortality | Conclusion moves from cross-sectional coefficient to intervention gains |
| Target claim | Field 6 (context: Field 2) | Field 6 | Field 6 (context: conclusion) |
| What was measured | PRS index, 1985–95 average | 19th-c. mortality rates per Table A2 | Cross-country 2SLS |
| What was claimed | "large effects of institutions" | "settlermortalityis a plausible instrumentfor institutional development" | "substantial economic gains from improving institutions" |
| Failure mode | Proxy problem | Definition-operationalization mismatch | Intervention ratchet |
| Failure-mode subtype | N/A | narrower operationalization | N/A |
| Severity | minor | none (for Field 6) | minor |
| Concede test | SURVIVES (Field 6) | SURVIVES | SURVIVES |
| Scope loss if NARROWS | N/A (Field 2: incidental) | N/A | N/A |
| Construct property | form | N/A | N/A |
| Construct-property status | ESTABLISHED-CITED | N/A | N/A |
| ESTABLISHED-CITED prosecutor split | N/A (cited support not retrieved) | N/A | N/A |
| Operationalization retrieval basis | ITEMS-INFERRED | ITEMS-RETRIEVED | N/A |
| Operationalization scope result | UNKNOWN | narrower | N/A |
| P2 belief grade | N/A | N/A | N/A |
| P2 strength gate | N/A | N/A | N/A |
| Evidence | PDF p. 3 (A1.2), p. 11 fn (A1.3), p. 4 fn 3 | Table A2; PDF p. 15–16; Albouy 2012; AJR 2012 appendix | PDF p. 28 Conclusion |
| Evidence type | primary study | primary study + methodological critique | primary study |
| Verification state | FULL-TEXT-CONFIRMED (text); PROVISIONAL (items) | FULL-TEXT-CONFIRMED | FULL-TEXT-CONFIRMED |
| Possible innocent explanation | The authors report similar results with other measures (fn 19, 22; AJR 2000) | Instrument validity does not require construct fidelity | The paper itself says the results "do not point out what concrete steps" |
| What would weaken this | Retrieved alternative-measure tables showing similar estimates | — | — |
| Failure location | PAPER | PAPER | PAPER |
| Finding disposition | PROVISIONAL | CONFIRMED | CONFIRMED |
