# STAGE 2 — INTERNAL VALIDITY & REPLICATION AUDIT
## Target: AJR (2001), Table 4 col. 1, 2SLS = 0.94 (SE 0.16)

    SIBLING-PROSECUTOR INPUT: NONE
    INDEPENDENCE STATUS: INDEPENDENT

The declared-input label above follows the prompt's FAIL-IV-002 rule: no construct-validity output was formally supplied. This run was written BEFORE the construct-validity stage (02b) and does not use it. Process independence is still NOT_ESTABLISHED. The same agent, in the same session, ran the claim map, both prosecutors and the counter-audit, and the agent has disclosed prior exposure (00a_preregistration_LOCKED.txt). "INDEPENDENT" here describes the declared-input boundary only. It does not mean an independent researcher.

INSTRUMENT PREFLIGHT: prompts/research-analysis/2-internal-validity.txt @ commit ce028e1294873df0143ca1ae00d6abf74a910563 | blob ff54b2a6e88d25cfef37c4626aee256d2d2442e8 (sha256 55e8aa1635c33088f91178c275d2776cbb378a95abd0fd9196efec08fbdb5007) | 970 lines | 46009 bytes | markers PRESENT | IDENTITY CONFIRMED

### INPUTS (formally declared)
1. The claim map: 01_claim_extraction.md (Field 6 = Table 4 col. 1).
2. The source: AJR 2001, published version (SOURCES_MANIFEST S1).
3. Data and code: the AJR posted replication files colonial_origins.zip (maketable1–8 .do/.dta; S3) and the posted rebuttal dataset "dataset used for final AER rebuttal Sept 11 2011.dta" (S4).
4. Known reanalysis and reply: Albouy (2012) Comment (S5, JSTOR copy via a third-party mirror), Albouy's site revision and data appendix (S6, S7), the AJR (2012) Reply and its appendix (S8, S9).
5. Pre-registration status: none exists. The source is a 2001 observational cross-country study, and no registry existed for it. This is recorded as unknown/not applicable, not as non-compliance.
6. Optional construct-validity output: NONE.

### Replication receipts (Derivation mode: COMPUTED-FROM-RETRIEVED)
- Script: replication/replicate.py, run with Python 3 in /workspace/venv-audit. It uses linearmodels IV2SLS (debiased), statsmodels OLS, and Anderson–Rubin 95% sets by analytic inversion. The output is replication/results.json and replication/replicate.log.
- Discrepancy script: replication/discrepancy_check.py, outputting discrepancy_check.json and .log.
- Table A2 check: replication/tableA2_vs_posted.py, outputting tableA2_vs_posted.json and .log.
- Scope limit: the Albouy-style checks (Part B) are MY approximations built from AJR's posted rebuttal dataset. That dataset carries Albouy's indicator variables (source0, campaign, slave) and AJR's recodings (campaignsj, campaignsj2). Clusters are defined by shared mortality value (36 clusters). Albouy's own replication package was NOT retrieved, so Part B does not reproduce Albouy's published tables. It tests whether the qualitative pattern he reports appears in the posted data.

---

SECTION A: DATA GENERATION AUDIT

- The outcome (log GDP pc 1995) and the regressor (PRS expropriation risk) are standard third-party series. Reported in the paper itself.
- Instrument construction is the load-bearing data-generation question. The paper states that it uses the "earliest available number for each country" (p. 16, PDF p. 16) and that combining sources "will introduce measurement error" while arguing that this "does not lead to inconsistent estimates" (fn 17). The argument holds for classical error uncorrelated with the structural error. It does not hold for error that is correlated with income or institutions. The paper does not address that correlated case (reported in the paper itself; reasoning: author inference).
- Albouy (2012) documents that 28 of 64 countries have rates from within their own borders and 36 are conjectured or benchmarked. Some campaign-soldier rates are used disproportionately in high-expropriation-risk countries (found in methodological critique; FULL-TEXT-CONFIRMED, layout text p. 2 / journal p. 3060).
- AJR (2012) contest the coding of the campaign variable ("inconsistent and seriously at odds with the historical record in at least ten cases") and propose capping at 250/1,000 (found in replication literature, reply; FULL-TEXT-CONFIRMED).
- Posted-data discrepancy, found by this audit (COMPUTED-FROM-RETRIEVED, FULL-TEXT-CONFIRMED against Table A2):
  - Tanzania's mortality in the posted maketable4.dta is 280 (logem4 = ln 280). Appendix Table A2 of the published article prints 145, and AJR's 2011 rebuttal dataset also uses ln 145.
  - The published 0.94 reproduces only with 280 (0.9443). With 145 it is 0.9234 (SE 0.1523).
  - All 63 other rows of Table A2 agree with the posted data to the printed precision. Gabon's log GDP of 8.9079 prints as 8.90, which is a rounding difference only.
- Second discrepancy (COMPUTED-FROM-RETRIEVED):
  - The 2011 rebuttal dataset has Indonesia's log GDP = 7.33. Table A2 and maketable4 have 8.07. Table A2's value for India is 7.33, which makes an adjacent-row transcription slip plausible but unverified.
  - The effect on the rebuttal-data baseline is 0.9295 → 0.9235.
  - Whether the AJR (2012) or Albouy (2012) published estimates use this row value: UNKNOWN (not checked against their tables).

SECTION B: PRE-REGISTRATION AND ANALYSIS PLAN

No pre-registration exists (not applicable for the era and design: unknown/not reported). Analysis-plan compliance cannot be assessed. No inference of compliance or non-compliance is drawn.

SECTION C: EFFECT SIZE AND STATISTICAL POWER

- Reproduced: T4c1 IV = 0.94 (0.16). First stage −0.61 (0.13), F = 22.95 (homoskedastic). HC1: SE 0.18, F = 16.3. AR 95% set [0.70, 1.43] (homoskedastic) and [0.69, 1.61] (HC1). The base result rejects zero under weak-IV-robust inference.
- Magnitude: the IV exceeds OLS (0.52). The paper attributes the gap to measurement error / attenuation in the institutions measure (reported in the paper itself). A competing explanation is that the IV picks up a direct effect of the instrument (exclusion failure), which would also inflate IV relative to OLS. The data cannot separate the two. Author inference.
- Power: with N = 64 and F ≈ 16–23, the base specification is not weak by conventional (Staiger–Stock F > 10) rules. Stricter modern t-ratio thresholds exist (recalled; PROVISIONAL, not retrieved). The AR sets make that question moot for col. 1.
- The paper's own col. 8 (continent dummies + latitude) has first-stage F = 3.46 in reproduction, and its AR set is unbounded (two rays). The paper presents col. 8 (1.10, SE 0.46) as part of the robustness picture. Under weak-IV-robust inference col. 8 is uninformative rather than confirmatory (COMPUTED-FROM-RETRIEVED).

SECTION D: HARKING

Not assessable from retrieved material. The theory (settlement → institutions) is laid out before the results, and the 2000 NBER working paper (S2, w7771) precedes publication. No evidence of hypothesis revision after the results was found or sought in depth. Cannot assess.

SECTION D2: FORKING PATHS / ANALYTICAL-CHOICE MULTIVERSE

Each choice below was proposed in print by one side. All runs are on posted data; "orig" means the AJR 2001 mortality series. F is the first-stage F (robust or cluster as noted). AR is the 95% Anderson–Rubin set.

| Spec | Sample | Mortality | Control | IV (SE) | F | AR95 | Defended by |
|---|---|---|---|---|---|---|---|
| T4c1 | 64 | orig | none | 0.94 (0.16) | 22.95 | [0.70, 1.43] | AJR 2001 |
| B1 | 64, cluster | orig | none | 0.93 (0.20) | 12.45 | [0.65, 1.84] | Albouy (clustering) |
| B1 | 64, cluster | orig | latitude | 0.96 (0.27) | 7.30 | [0.62, 2.91] | Albouy (clustering) |
| B2 | 28 own-country | orig | none | 0.87 (0.22) | 9.24 | [0.57, 2.07] | Albouy |
| B2 | 28 own-country | orig | latitude | 0.82 (0.34) | 3.62 | unbounded | Albouy |
| B3 | 64 + campaign/laborer, cluster | orig | none | 1.09 (0.38) | 5.91 | [0.62, 5.26] | Albouy |
| B3 | 64 + campaign/laborer, cluster | orig | latitude | 1.15 (0.51) | 3.67 | unbounded | Albouy |
| B4 | 28 + campaign/laborer | orig | none | 1.02 (0.52) | 2.57 | unbounded | Albouy |
| B4 | 28 + campaign/laborer | orig | latitude | 0.90 (0.93) | 0.67 | whole line | Albouy |
| B0 | 64 | capped 250 | none | 0.82 (0.12) | 32.29 | [0.63, 1.14] | AJR 2012 |
| B2 | 28 | capped 250 | latitude | 0.73 (0.23) | 6.50 | [0.21, 2.02] | AJR 2012 |
| B3 | 64 + camp/lab, cluster | capped 250 | latitude | 0.85 (0.26) | 9.43 | [0.37, 1.88] | AJR 2012 |
| B4 | 28 + camp/lab | capped 250 | none | 0.95 (0.32) | 5.13 | [0.34, 5.31] | AJR 2012 |
| B4 | 28 + camp/lab | capped 250 | latitude | 0.73 (0.53) | 1.84 | whole line | (neither; smallest cell) |
| C1 | 27 own-country, drop Gambia | orig | none | 0.74 (0.11) | 24.16 | [0.53, 1.06] | AJR 2012 |
| C2 | 27, drop Gambia + camp/lab | orig | none | 0.77 (0.22) | 9.72 | [0.27, 1.51] | AJR 2012 |
| C3 | 64 + AJR recoding campaignsj2 | orig | none | 0.93 (0.21) | 11.49 | [0.64, 1.95] | AJR 2012 |
| C4 | 28 + campaignsj2 | orig | none | 0.97 (0.32) | 5.31 | [0.57, 6.42] | AJR 2012 |
| C6 | 64, naval benchmark | alt | none | 0.97 (0.19) | 15.66 | [0.71, 1.69] | AJR 2001/2012 |
| C7 | 64, Caribbean benchmark | alt | none | 0.96 (0.18) | 15.47 | [0.71, 1.67] | AJR 2012 |

Reading (author inference, mechanical):
- Point estimates stay positive and within 0.73–1.15 in every cell above, so sign and magnitude class are stable.
- What is fragile is identification strength. In cells that combine Albouy's sample restriction or campaign/laborer indicators WITH a latitude control on the original mortality series, the first stage is weak (F < 4) and AR sets are unbounded. Capping at 250, dropping Gambia, or using AJR's recoding restores bounded AR sets in all cells except the smallest one with latitude (B4-capped-latitude).
- This pattern matches both sides' printed characterizations: Albouy's "point estimates are … confidence intervals are often infinite", and AJR's "except in the very smallest of his samples".
- Robustness depends on which data-construction choice is accepted. Both choices have printed historical justifications that this audit cannot adjudicate.

SECTION E: SELECTIVE REPORTING

- The paper reports many robustness tables (4–8) and discloses weaker within-Africa results (fn 21) and the overid caveat. No evidence of selective reporting was found.
- Not reported in 2001: weak-IV-robust inference for the small-F columns (col. 8, F = 3.46). Weak-IV diagnostics were not standard practice in 2001 (author inference, PROVISIONAL), so this is a period limitation rather than evidence of selection.
- Footnote 16 discloses that Ethiopia was kept because excluding it "would have helped our hypothesis". This is a disclosed choice that cuts against the authors' interest.

SECTION F: REPLICATION STATUS

- Computational reproduction of Table 4 cols 1–9 from the posted data: REPRODUCED to the printed precision. The single exception is col. 8: 1.11 vs printed 1.10 (rounding of 1.105; immaterial). First-stage col. 5 gives −1.21 vs printed −1.20, and col. 6 gives −1.14 vs −1.10. These are small first-stage differences, cause unknown (data vintage?). Derivation mode: COMPUTED-FROM-RETRIEVED. This is a reproduction, NOT an independent replication: same data, same estimator.
- Reanalysis: Albouy (2012) exists. RECEPTION-CONFIRMED (OpenAlex W1969918011, a citing relation to W3124166904) and FULL-TEXT-CONFIRMED (read).
- Reply: AJR (2012). RECEPTION-CONFIRMED (W3124131699) and FULL-TEXT-CONFIRMED.
- AJR's 2005 "A Response to Albouy" (unpublished WP): RECEPTION-CONFIRMED (OpenAlex title match). Not retrieved.
- A 2017 paper titled "Graphs as a Tool for the Close Reading of Econometrics (Settler Mortality is not a Valid Instrument for Institutions)": RECEPTION-CONFIRMED (title only). Not retrieved, so its tenor is from the title only. PROVISIONAL.
- Other well-known critiques (e.g., Glaeser et al. 2004 on human capital) are recalled from memory, not retrieved: PROVISIONAL, and none may anchor a verdict.
- Scope fence: this audit does NOT adjudicate who is right in the Albouy/AJR exchange. It checks that each side's qualitative result appears in the posted data.

SECTION G: DATA AND CODE AVAILABILITY

- Data and Stata code for Tables 1–8 are posted (MIT data archive → Dropbox), as is the 2011 rebuttal dataset. FULL-TEXT-CONFIRMED (retrieved, opened, hashed).
- Mortality construction (AJR 2000 Appendix B, Table A5) is "available from the authors" and was not retrieved. The reply's appendix documents the sources country by country.
- Post-publication flags: OpenAlex is_retracted = false for all three works. No correction or erratum was found in a limited search (not exhaustive).
- OpenAlex metadata anomaly: the 2012 Reply shows cited_by_count = 6,266, implausibly close to the original's 8,594. This is likely a work-merge artifact, and those counts should not be read as citation evidence (RECEPTION metadata, flagged).

SECTION H: SUMMARY TABLE — INTERNAL VALIDITY

|Dimension               |Assessment|Severity|Notes|
|------------------------|----------|--------|-----|
|Data generation quality |Instrument partly assigned/benchmarked across countries (36/64 per Albouy); coding contested | Moderate | FULL-TEXT-CONFIRMED that assignment exists; adjudication CONTESTED |
|Selection bias          |Sample = ex-colonies with data; fn 2 argues conditional-on-colonization framing | Minor | author inference |
|Missingness handling    |Base sample defined by data availability | Minor | |
|Incentive structure risk|Not assessed | Cannot assess | |
|Pre-registration        |None (N/A for era) | Cannot assess | |
|Analysis plan compliance|N/A | Cannot assess | |
|P-hacking risk          |Low for col. 1 (AR set far from 0) | Minor | COMPUTED |
|Effect size plausibility|IV > OLS; attenuation vs exclusion-failure explanations both available | Moderate | author inference |
|Statistical power       |Base adequate; controls/continent specs weak (col. 8 F=3.46) | Minor (for Field 6) | COMPUTED |
|Winner's curse risk     |Not applicable in the usual sense | None | |
|HARKing risk            |Cannot assess | Cannot assess | |
|Forking-paths fragility |Identification strength fragile to contested data-construction choices; sign/magnitude stable | Moderate | COMPUTED + CONTESTED |
|Selective reporting     |None found | None | |
|Replication success rate|Computational reproduction succeeds; no independent new-data replication retrieved | Minor | |
|Effect size trajectory  |0.94 → 0.82 (capped) / 0.73–0.97 (AJR 2012 variants) | Minor | COMPUTED |
|Data/code availability  |Posted | None | |
|Post-publication flags  |Published Comment + Reply; no retraction | Moderate | RECEPTION-CONFIRMED |

SECTION H2: THE CONCEDE TEST

| Finding | Verification state | Technical outcome status | Conditional concede result | Verdict eligibility | Eligibility basis | Surviving claim if NARROWS |
|---|---|---|---|---|---|---|
| IV-1 Instrument-construction fragility: under Albouy's restrictions plus latitude, the first stage is weak and AR sets unbounded | FULL-TEXT-CONFIRMED (Albouy, reply) + COMPUTED-FROM-RETRIEVED | Mechanical pattern REPRODUCED on posted data; which coding is correct CONTESTED | NARROWS | ELIGIBLE (as a fragility finding); PENDING for "Albouy coding is correct" | Pattern reproduced from AJR's own posted rebuttal data; adjudication needs historical-source review | In the base sample with the AJR mortality series (or capped/recoded variants), the 2SLS coefficient is roughly 0.75–1.0 and bounded away from zero; in the 28-country own-data subsample with geographic controls and campaign indicators, the data are not informative about the coefficient |
| IV-2 Clustering by shared mortality value | COMPUTED-FROM-RETRIEVED | REPRODUCED (my cluster definition) | SURVIVES | ELIGIBLE | B1: SE 0.16→0.20, AR bounded | — |
| IV-3 Posted maketable4 TZA = 280 vs Table A2 145 | FULL-TEXT-CONFIRMED + COMPUTED | REPRODUCED | SURVIVES | ELIGIBLE | 0.94 → 0.92 | — |
| IV-4 Rebuttal-data IDN log GDP 7.33 vs 8.07 | COMPUTED-FROM-RETRIEVED | REPRODUCED; downstream use in 2012 tables UNKNOWN | SURVIVES | ELIGIBLE (for the data fact) | 0.93 → 0.92 | — |
| IV-5 Baseline stated as 0.95 on p. 26 vs 0.94 | FULL-TEXT-CONFIRMED | N/A | SURVIVES | ELIGIBLE | Wording | — |
| IV-6 Exclusion restriction (direct disease/human-capital channel) | PROVISIONAL (alternative-channel evidence not retrieved; only AJR's own controls read) | UNVERIFIED | DEFEATS (causal interpretation) | PENDING VERIFICATION | Needs retrieved evidence of a direct mortality→income channel that survives AJR's controls; overid tests have the self-acknowledged power caveat | — |
| IV-7 Col. 8 (continent + latitude) weak-IV: F=3.46, AR unbounded | COMPUTED-FROM-RETRIEVED | REPRODUCED | SURVIVES (Field 6 is col. 1) | ELIGIBLE | Bears on the robustness claim, not col. 1 | — |
| IV-A Acquittal: col. 1 survives weak-IV-robust inference | COMPUTED-FROM-RETRIEVED | REPRODUCED | n/a (acquittal) | ELIGIBLE | AR [0.70, 1.43] / HC1 [0.69, 1.61] | — |

| Finding | Scope-loss level | Original claim | Surviving claim | What practical or inferential work is lost? |
|---|---|---|---|---|
| IV-1 | MATERIAL (contested) | 0.94 (0.16), presented as robust | Positive coefficient of ~0.75–1.0 in the full sample under AJR or capped coding; uninformative in the smallest own-data subsamples with controls | The claim that the estimate is robust to any defensible data construction fails. Precision is lost in restricted samples; sign and magnitude class are not lost |

Note on the scope-loss label: a reasonable adjudicator could call IV-1 INCIDENTAL, because point estimates never leave the 0.73–1.15 band. It is labelled MATERIAL because the inferential work at stake in the 2012 exchange is whether the data identify the coefficient at all in the subsample that Albouy considers reliable. In that subsample the data do not identify it once latitude is controlled (B2 and B4 with latitude).

SECTION I: INTERNAL VALIDITY VERDICT

- Claim under audit: USEFUL-FOR-NARROWER
- Eligible DEFEATS finding(s), if any: none
- Eligible MATERIAL NARROWING finding(s), if any: IV-1 (contested adjudication; mechanical pattern reproduced)
- Findings pending verification:
  - IV-6 exclusion restriction | DEFEATS (causal reading) | alternative-channel evidence not retrieved; untestable with a single instrument | retrieve and assess the direct-effect literature and run sensitivity bounds (e.g., plausibly-exogenous / Conley-type)
  - IV-1 adjudication of Albouy vs AJR coding | — | a historical-source question | an independent historian's review of the 36 assigned rates and the campaign coding
- Pending-evidence effect on assessability: LIMITED
- Surviving residual: "In the 64-country base sample with the AJR 2001 mortality series, the 2SLS coefficient of 1995 log GDP per capita on the 1985–95 PRS expropriation-protection index is 0.94 (0.16), reproducible from posted data and bounded away from zero under weak-IV-robust inference. Its precision, though not its sign, depends on contested choices about how historical mortality rates are assigned and coded. Its causal interpretation rests on an exclusion restriction this audit could not verify."
- Internal-validity grade: C (Weak — "affected by moderate design or data-generation concerns"). The grade is borderline B/C. B would be the reading for someone who accepts AJR's capping/recoding as the correct data construction.

Answers:
1. Likely real? The positive reduced-form and first-stage associations are reproducible. Whether the IV estimate is a causal effect of institutions cannot be determined from internal-validity evidence alone (IV-6 pending).
2. Is the magnitude sufficient for the downstream claim? The paper itself calls the 7-fold implication an upper bound. Magnitudes of 0.73–1.15 across contested specs all imply large effects, if the exclusion restriction holds.
3. Best current estimate: about 0.8–0.95 in the full sample (capped 0.82, AJR-recoded 0.93, original 0.94). In restricted samples with controls it is not identified.
4. What would upgrade the grade: resolution of the mortality-coding dispute by independent historical review; new-data replication (e.g., sub-national or alternative instruments).
5. Decisive test not run here: re-coding the 36 assigned rates blind to income/institutions by an independent party, then re-estimating with AR inference, plus a sensitivity analysis bounding direct effects of the instrument.
6. AI-assisted analysis: the adversarial check found the TZA posted-data/appendix discrepancy and the IDN rebuttal-data value, which neither the 2001 paper nor the retrieved 2012 texts mention (as far as was read). Both are immaterial.
7. Fragile to defensible choices? Yes for identification strength in small subsamples with controls; no for sign.
8. Usable residual: yes, as stated above.

SECTION J: INTEGRATION WITH CONSTRUCT VALIDITY AUDIT

    SIBLING-PROSECUTOR INPUT: NONE
    INDEPENDENCE STATUS: INDEPENDENT

No construct-validity output was formally supplied to this run. The following reasons only from general construct concerns and does not adopt any specific sibling finding or verdict visible elsewhere in session context.

Even if the outcome measure's construct validity is accepted, IV-1 would still narrow the claim to a full-sample estimate whose precision depends on contested mortality coding. If an independently established construct-validity failure were later added (e.g., about what the expropriation index captures), it would compound with this result by changing what the coefficient is a coefficient OF, not whether it is precisely estimated.

The foundational finding cannot yet be determined to be likely real as a causal effect, based on the eligible internal-validity evidence. It is likely real as a reproducible conditional association and IV estimate. Even if the construct interpretation is accepted, its precision is contingent on contested mortality-data choices. Any specific construct-validity compounding claim remains outside this independent run.

SECTION K: ONE-PARAGRAPH SUMMARY

The headline estimate (Table 4 col. 1: 0.94, SE 0.16) reproduces exactly from the authors' posted data and survives weak-instrument-robust inference (AR 95% set about [0.70, 1.43]). That makes it a real, reproducible statistical result in the base sample. Whether it is a causal effect of "institutions" is a separate matter that rests on an exclusion restriction this audit could not test (pending). The best current point estimate in the full sample is about 0.8–0.95 depending on mortality coding. No independent new-data replication was retrieved: the post-publication record is a reanalysis (Albouy 2012) and a reply (AJR 2012). Data generation is the weak point. Over half the instrument values are assigned or benchmarked across countries, and their coding is disputed. In the posted data the sign is robust across every specification either side proposed, but identification collapses (F < 4, unbounded AR sets) when Albouy's own-data subsample or campaign indicators are combined with a latitude control. AJR's capping or Gambia exclusion restores it except in the smallest cell. Claim status is USEFUL-FOR-NARROWER, grade C (borderline B), with the load-bearing concede result NARROWS (material, contested). Two minor data discrepancies found here (TZA 280 vs 145 in the posted 2001 file; IDN log GDP in the 2011 file) do not change any conclusion. The decisive test is an independent, blinded recoding of the assigned mortality rates combined with weak-IV-robust inference and a bounded-exclusion sensitivity analysis.

FINAL SECTION: STANDARDIZED FINDING TABLE

| Field | IV-1 | IV-2 | IV-3 | IV-4 | IV-5 | IV-6 | IV-7 |
|---|---|---|---|---|---|---|---|
| Finding | Identification strength is fragile to contested mortality-data construction choices | Clustering by shared mortality rate widens SEs modestly; result survives | Posted 2001 data codes TZA mortality 280, Table A2 prints 145; published 0.94 matches 280 | 2011 rebuttal data has IDN log GDP 7.33 (Table A2: 8.07) | Baseline stated as 0.95 on p. 26 vs 0.94 in Table 4 | Exclusion restriction unverified; a direct mortality→income channel would defeat the causal reading | Paper's col. 8 robustness spec is weakly identified (F=3.46; AR unbounded) |
| Target claim | Field 6 | Field 6 | Field 6 | Field 6 (rebuttal baseline) | Field 6 | Field 6 | Field 6 (robustness context) |
| What was measured | 2SLS/AR across 20 specs on posted data | Cluster-robust 2SLS | Table A2 vs maketable4 row comparison; re-estimation | Row comparison; re-estimation | Text | — | 2SLS + AR |
| What was claimed | Robust large effect | "clustering has little effect" (fn 18) | 0.94 (0.16) | Rebuttal baseline | Baseline | Exclusion restriction "plausible" | Robustness to continent dummies |
| Failure mode | Forking-paths fragility / data-generation | Inference (SE) | Data transcription | Data transcription | Internal inconsistency | Untested identifying assumption | Weak instrument |
| Severity | moderate | none | minor | minor | none | moderate (non-anchoring; pending) | minor |
| Concede test | NARROWS | SURVIVES | SURVIVES | SURVIVES | SURVIVES | DEFEATS (conditional; pending) | SURVIVES |
| Scope loss if NARROWS | material (contested); surviving claim as in Section I | — | — | — | — | — | — |
| Evidence | replicate.log Part B/C; Albouy 2012 pp. 3060–72; AJR 2012 pp. 3078–80 | replicate.log B1 | tableA2_vs_posted.log; discrepancy_check.log | discrepancy_check.log | AJR p. 26 (PDF) vs p. 18 | AJR p. 4, p. 26 | replicate.log T4c8 |
| Evidence type | methodological critique + replication (computational) | replication (computational) | primary study + data | data | primary study | theoretical / author inference | replication (computational) |
| Verification state | FULL-TEXT-CONFIRMED; COMPUTED-FROM-RETRIEVED; CONTESTED | COMPUTED-FROM-RETRIEVED | FULL-TEXT-CONFIRMED | COMPUTED-FROM-RETRIEVED | FULL-TEXT-CONFIRMED | PROVISIONAL | COMPUTED-FROM-RETRIEVED |
| Possible innocent explanation | Albouy's restrictions discard most of the sample and his campaign coding is disputed; AJR's capping has a historical rationale (Tulloch) | My cluster definition (shared value) may differ from Albouy's | Table A2 may reflect a later correction not propagated to the posted file, or vice versa | Spreadsheet row slip in a dataset built for a reply | Rounding/typo | AJR's controls for malaria, climate, etc. leave the estimate at 0.69–0.91 | 2001 practice did not use weak-IV-robust inference |
| What would weaken this | An independent historian's recoding that agrees with AJR; Albouy's package showing my approximation misses his result | Albouy's exact clusters producing a much larger SE | An AJR erratum showing 280 is correct | Evidence it was corrected before the 2012 tables | — | Retrieved evidence that mortality has no direct income channel conditional on controls | — |
| Failure location | PAPER (data construction) / MIXED (dispute) | PAPER | PAPER (data/appendix) | PAPER (2012 rebuttal data) | PAPER | PAPER (assumption) | PAPER |
| Status | contested | confirmed | confirmed | confirmed (data fact); provisional (downstream use) | confirmed | provisional | confirmed |
