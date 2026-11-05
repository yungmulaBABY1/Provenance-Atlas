# Stage 2b — Construct-Validity Audit: Claim vs. Measurement

INSTRUMENT PREFLIGHT: prompts/research-analysis/2-construct-validity.txt @ commit a58d165d9a986edca220f8143fc0c0d9316c8a13 | blob/hash 7f3db5ed66db3cb4c5ca84f9e71760d134ced9c8 / sha256 8f87676ae76ecf745748a58a7e68b285255c324da25a92a22f3d1a797f6feadb | 1255 lines | 44222 bytes | markers PRESENT ("CONSTRUCT-VALIDITY AUDIT PROMPT:", "CLAIM VS. MEASUREMENT") | IDENTITY CONFIRMED (operator-pinned commit + blob + sha256; immutable-commit retrieval HTTP 200; independently cross-checked by git rev-parse)

Effort: high (as briefed). The full pinned prompt was read before writing. Sibling prosecutor outputs (02a) were not used as inputs. This is an independent Stage-2 run that uses only the Stage 1 map and the sources listed below.

SOURCE RETRIEVAL BASIS: full text fetched. The target is the published JPE version (Belfer Center institutional copy, read in full; author WP 23 Aug 2005 for version comparison). Additional sources retrieved and read in full or in the relevant sections:
- Klasen (2005) comments, Göttingen institutional page;
- Lin & Luoh (2008) WP, authors' homepage;
- Oster, Chen, Yu & Lin, NBER w13971 (2008);
- Dubner & Levitt, Slate (2005);
- Klasen, VoxEU column.
Nothing load-bearing is recalled from training data. Items marked PROVISIONAL are flagged individually.

| Specific figure | Value stated | Verification state | Source |
|---|---|---|---|
| Share of Coale's missing women explained | 47.24% (CI 13.5–71.5) | FULL-TEXT-CONFIRMED | Table 11A, p.1202 |
| Coale total / HBV-adjusted remaining | 60.26M / 31.79M | FULL-TEXT-CONFIRMED | Table 11A |
| China share | 76.40% | FULL-TEXT-CONFIRMED | Table 11A |
| Carrier offspring SR | 1.54 (1.29–1.87) | FULL-TEXT-CONFIRMED | Table 9, p.1199 |
| Carrier/noncarrier children in pooled studies | 355/248; 2,083/2,043 | FULL-TEXT-CONFIRMED | Table 3, p.1180 |
| Noncarrier SRB used | 1.048 | FULL-TEXT-CONFIRMED | Table 10, p.1200 |
| China / India prevalence among pregnant women | 11.24% / 4.33% | FULL-TEXT-CONFIRMED | Table 10 |
| Life-expectancy coefficient on share male | .0003–.0010 | FULL-TEXT-CONFIRMED | Table 6, p.1191 |
| China partial-effect share | 62% (18M) | FULL-TEXT-CONFIRMED | p.1204 |
| Taiwan maternal HBsAg effect on P(male) | +0.0010 to +0.0025 | FULL-TEXT-CONFIRMED (WP version) | Lin & Luoh WP abstract, Table 2 |
| China cohort size; paternal carriers' share of boys | ~67,000; 51.06% vs 51.56% | FULL-TEXT-CONFIRMED (NBER WP version) | w13971 abstract, p.4 |

Applicable-checks note:
- Target document type: peer-reviewed empirical journal article with a calibration exercise.
- Sections that apply: 1, 1A, 2–16.
- Sections that are N/A: none. Section 9 (citation use) is limited to the retrieved items in Stage 1 Field 4.

## 1. Claim map (received)

- Claim under audit (map field 6): HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale's (1991) 60.26 million missing women (Table 11, Panel A).
- What was literally measured (map field 1): carrier status/prevalence ↔ offspring/population sex-ratio associations, plus a calibrated re-run of Coale's accounting with SR_HBV 1.54.
- Weaker defensible claim (map field 3): conditional on 1.54, the prevalence inputs and Coale's framework, about 47% is an upper-bound total effect; the aggregate associations are not decisive for causality.
- Target layer: source claim.

No MAP DISAGREEMENT.

## 1A. Construct establishment

Triggered: the paper escalates to a causal claim. HBV causes elevated SRB, which accounts for a share of missing women, so the bias is "less attributable to differences in tastes and preferences" (p.1165).

Assessed from full text plus introduction and citations checked. The cited 1975–88 studies were not themselves retrieved; their content is checked as reported in Table 3.

| Property | Claim-map status | Does the normative / causal claim depend on it? | ESTABLISHED-CITED prosecutor split | Evidence and exact inferential load | Finding disposition |
|---|---|---|---|---|---|
| PREVALENCE | ESTABLISHED-REPORTED | Yes (multiplier in Table 10) | N/A | Author aggregation; study list off-paper | no finding (see CV-6 for selection concerns) |
| FORM | ESTABLISHED-CITED + ESTABLISHED-REPORTED | Yes, entirely: the share is proportional to (SR_HBV − SR_N)·prevalence | **contested-in-respect-required** | The cited studies support "carrier families in six small populations had more sons". The paper places a stronger load on them: a causal maternal effect of 1.54 that transfers to the national populations of China, India and others. The paper itself says "not conclusive" (p.1181). Large-sample tests retrieved this run find ≈0 (Lin & Luoh; Oster et al.) | CONFIRMED (CV-1) |
| DOMAIN | ESTABLISHED-REPORTED | Yes | N/A | Seven units, 1980s | no finding |
| WRONGNESS | not applicable | No | N/A | No belief graded | — |
| HARM | not applicable | No | N/A | — | — |

Not-firing condition: does not apply to FORM.

## 2. Measurement extraction

- Sample sizes:
  - six studies, 4,729 children (603 with a carrier parent);
  - 38 countries;
  - IPUMS immigrants 210,556;
  - Alaska 5,041; Taiwan 96 cohort-years;
  - 60 Chinese counties (about 100 tested each).
- Population:
  - family studies in Greenland, Kar Kar, Greece, Philippines, France;
  - national populations for the cross-section;
  - the calibration is applied to China, India, Pakistan, Bangladesh, Nepal, Western Asia and Egypt.
- Recruitment: convenience serology studies.
- Instrument: HBsAg serology; offspring sex as reported; UN Demographic Yearbook SRB; Coale's model life tables.
- Time scale: studies 1975–88; SRB 1960s–1990s; populations mid-1980s.
- Outcome: share male at birth; derived count of missing women.
- Controls: study fixed effects (individual level); GDP, TFR, life expectancy, infant mortality and region FE (cross-country).
- Exclusions: China and Korea post-1990 SRB (Table 6 note); countries with <2,500 tested.
- Not measured:
  - parental HBV status of births in the target populations;
  - HBV genotype;
  - birth order × HBV;
  - partial (behaviour-held-constant) effect, except one China county exercise.

The "share of missing women explained" is not measured. It is a derived counterfactual quantity. Its relation to HBV causation is entirely through the proxy SR_HBV = 1.54 imported from other populations.

Definition–operationalization check:
- Definition: missing women = women absent relative to the expected population sex ratio (eq. 1, p.1168).
- Operationalization: Coale's (1991) benchmark and life tables, with the expected SRB replaced by the HBV-predicted SRB (Table 11 note).
- Retrieval basis: ITEMS-RETRIEVED.
- Scope result: narrower than the abstract's framing ("as many as 100 million" / "about 45 percent of the 'missing women'"). The claim under audit already names Coale, so field 6 itself is coextensive with Table 11A.
- No pathologization question arises.

## 3. Claim vs. measurement table

| Measured variable | Claimed construct | Are they the same? | Gap | Severity | Notes |
|---|---|---|---|---|---|
| Pooled offspring sex ratio in six small carrier-family studies | Causal per-mother HBV effect on SRB in national populations | No | Proxy gap and level-of-analysis: small heterogeneous samples (carrier parent varies) → national maternal-prevalence multiplier | fatal-for-strong-claim | CV-1, CV-2 |
| Coale counterfactual with HBV-predicted SRB | Share of missing women "accounted for" by HBV | Partly | Total effect; benchmark from rich-country SRB | moderate | CV-3, CV-4 |
| Cross-country HBV–SRB association | HBV causes SRB elevation | No | Ecological; regional confounding with son preference | moderate | CV-5 |
| Abstract "about 45 percent of the 'missing women'" | Share of Coale's 60.26M | Narrower | Definition-operationalization mismatch (abstract framing only) | minor | CV-7 |

## 4. Level-of-analysis check

- Evidence level: small community/family serology studies; ecological country aggregates.
- Claim level: population-level accounting for national sex ratios (seven units).
- Bridging assumptions:
  - (a) the association is causal;
  - (b) it operates through mothers (prevalence among pregnant women is used);
  - (c) it is homogeneous across HBV genotypes and populations;
  - (d) it is additive with no behavioural response.
- Tested: (a) only via ecological and time-series designs, the paper's own "suggestive"; (b) not tested; (c) not tested; (d) assumed and acknowledged as "unrealistic" (p.1165).
- Would a domain expert accept the bridge? The retrieved large-sample tests in the target region reject (a)+(b): Lin & Luoh, maternal, Taiwan; Oster et al., maternal and paternal, China.

## 5. Confound audit

| Confound | Domain obvious? | Controlled? | Acknowledged? | Impact if omitted |
|---|---|---|---|---|
| Son preference / parity-specific sex selection (R1) | Yes | No birth-order analysis | Partly (sex-selection technology caveat, p.1165, p.1186) | High |
| Region/culture correlated with both HBV and son preference (R3) | Yes | Region FE (Table 6 col. 4: .0011 retained) | Yes | Moderate |
| Development/mortality affecting baseline SRB (R4) | Yes | Controls in Table 6; not in the calibration benchmark | Partly | Moderate |
| Registration completeness (girls under-registered) | Yes | Complete-reporting subsample N=30 | Yes | Moderate |
| Vaccination timing coinciding with prenatal sex selection (Taiwan) | Yes | No | Yes (p.1186) | Moderate (L2 only) |
| Which parent is the carrier; HBV genotype | Yes | No | Partly | High (now evidenced: re-analysis reported in w13971 p.3 points to paternal) |

## 6. Ecological validity check

- The six studies are of populations unlike the target ones (Greenland, Kar Kar, Greek villages), and the virus genotypes differ (Klasen 2005 raises this; the paper cites the genotype literature).
- The time scale matches (1980s populations).
- Verdict: **Not ecologically valid for the claim being made.** Ecologically valid only for a narrower claim about the studied communities.

## 7. Decisive-test check

- What the test measures: offspring sex by parental (maternal and paternal) HBsAg status in large, representative registries of the target populations, by birth order.
- Supports the claim if: P(male) is about 9 pp higher for carriers.
- Falsifies the claim if: no meaningful difference.
- Has it been run? Not by the source. It has since been run by Lin & Luoh (Taiwan, maternal, ≈3M births: +0.1–0.25 pp) and by Oster et al. (China cohort, maternal and paternal: no effect).
- The field acknowledges these results: the source's author co-wrote the second test and concludes "hepatitis B carrier rates cannot explain male-biased sex ratios or the 'missing women' in China" (w13971 Sec. 4).

"The decisive test would be: compare offspring sex ratios by maternal and paternal HBsAg status in a large representative birth registry of a high-prevalence target population, stratified by birth order."

## 8. Cross-reanalysis object check

- **Lin & Luoh vs the source.**
  - Object: maternal carrier status in Taiwan, 1988–99.
  - The source's calibration multiplies by prevalence among pregnant women, so it is the same object as the calibration input. This is a genuine contradiction.
  - Lin & Luoh do not test paternal status.
- **Oster et al. vs Lin & Luoh.**
  - Different objects: China cohort, maternal and paternal.
  - Convergent, not conflicting; together they cover both parents in the two largest Chinese-population tests.
- **Re-analysis of Greece/Philippines (paternal association, reported in w13971 p.3) vs Oster et al. China (no paternal effect).**
  - These are different populations (and possibly genotypes).
  - They are not necessarily contradictory, but the paternal pathway is tested only for China.
  - The dispute is resolved for the claim as operationalized (China plus maternal multiplier). It is not resolved for a general "HBV affects SRB somewhere" claim.
- **Klasen 2005 vs the source.**
  - Different object: benchmark and evidence quality, not a new test.

## 9. Citation-use audit

| Downstream item | Classification | Note |
|---|---|---|
| Slate, Dubner & Levitt 2005 (D1) | Major inflation | "established the fate of roughly 50 million of Amartya Sen's missing women": hedge removal plus baseline substitution (pre-publication version) |
| Lin & Luoh WP (D2) | Accurate citation | "as much as half … up to 75 percent of those in China" |
| Klasen 2005 (D3) | Accurate citation | |
| Klasen VoxEU (D4) | Accurate (critic paraphrase; mixes denominators) | |

## 10. Ignored-literature check

| Ignored literature / evidence | Why it matters | Was it cited? | Effect of omission |
|---|---|---|---|
| Birth-order-specific SRB in China (demography; e.g., Zeng Yi et al. 1993 is cited; parity analysis not used) | R1 predicts parity-specific elevation that HBV does not | Partly (Yi et al. 1993, Hull 1990 cited for sex selection) | Moderate weakness |
| Chahnazarian (1986) dissertation: carrier-parent birth-order pattern fails to explain Chinese high-parity SRB (as quoted in Klasen VoxEU) | Directly contrary on mechanism | Not cited (Chahnazarian, Blumberg & London 1988 cited) | Moderate weakness (PROVISIONAL: dissertation not retrieved) |
| SRB–life-expectancy relationship (Klasen 1994; Klasen & Wink 2002) applied to the benchmark | R4 | Cited, not applied to the benchmark | Moderate weakness |

## 11. Evidence-type / verification / failure-location table

| Claim or evidence item | Evidence type | Measurement role | Verification state | Failure location | Directly measured / inferred / speculative | Source audit required? |
|---|---|---|---|---|---|---|
| SR_HBV 1.54 | Primary empirical evidence (pooled secondary data) | Proxy evidence | FULL-TEXT-CONFIRMED (pooling); cited studies LOCATED via references only | PAPER | Directly measured (in six studies) | Yes (original studies) |
| 47.24% share | Author inference (calibration) | Citation-dependent premise | FULL-TEXT-CONFIRMED | PAPER | Inferred | No |
| Cross-country association | Primary empirical evidence | Proxy evidence | FULL-TEXT-CONFIRMED | PAPER | Directly measured | Yes (prevalence list) |
| Lin & Luoh null | Primary empirical evidence | Direct measure | FULL-TEXT-CONFIRMED (WP) | — | Directly measured | Published version |
| Oster et al. null | Primary empirical evidence | Direct measure | FULL-TEXT-CONFIRMED (WP) | — | Directly measured | Published version |
| Slate restatement | Public reporting / journalism | Other measurement role (restatement) | FULL-TEXT-CONFIRMED | PR-MEDIA | — | No |

## 12. Internal consistency check

"Resolved" is used only for the claim as operationalized (China plus maternal multiplier). The general biological question is described as unresolved for paternal and non-Chinese populations. No contradictory language was found.

## 13. Concede test

| Finding | Concede test | Surviving claim if NARROWS |
|---|---|---|
| CV-1 FORM contested-in-respect-required: the 1.54 causal maternal effect does not hold in large target-population data | DEFEATS | — |
| CV-2 Level-of-analysis: small-study proxy imported into national maternal-prevalence accounting | DEFEATS (same mechanism as CV-1; consolidated, not counted twice) | — |
| CV-3 Total-effect assumption (no behavioural response), acknowledged; partial effect 62% for China | NARROWS | Share is an upper bound under no compensating behaviour |
| CV-4 Benchmark: rich-country SRB used where the paper's own Table 6 shows SRB rises with life expectancy | NARROWS | Share is overstated by an unquantified amount; Klasen's stronger claim (adjustment roughly cancels) UNVERIFIED |
| CV-5 Ecological confounding of L2 | NARROWS (L2) | Associations, not causal effects |
| CV-6 Prevalence inputs from convenience studies; list off-paper | SURVIVES | — |
| CV-7 Abstract frames the Coale share against "as many as 100 million" | SURVIVES | — |

| Finding | Scope-loss level | Original claim | Surviving claim | What practical or inferential work is lost? |
|---|---|---|---|---|
| CV-3 | Incidental | 47% | ≤47% total effect | Interpretation as "not discrimination" |
| CV-4 | Material | 47% | Smaller, unquantified | Magnitude |
| CV-5 | Material (for L2) | HBV raises SRB | Positive ecological association | Causal reading |

## 14. Verdict

- Claim under audit: INVALID
- DEFEATS finding(s): CV-1 (with CV-2 as the same mechanism)
- Failure mechanism: fatal construct-validity failure (the proxy SR_HBV 1.54 does not measure the causal maternal effect in the target populations)
- Surviving residual: none for the share. Separately, a positive cross-country association between HBV prevalence and share male at birth survives as an ecological observation.
- Residual usefulness grade: none

Explanation:
- The 47% figure is the product of a borrowed proxy (1.54) and prevalence.
- The proxy was meant to stand for the causal effect of HBV in Chinese, South Asian and Middle-Eastern mothers.
- The two large direct tests in Chinese populations find effects one to two orders of magnitude smaller, or none.
- Once FORM is contested in the required respect, the share has no remaining evidential basis.
- The benchmark and total-effect issues would narrow even a valid share, but they are moot.

## 15. Paper-safe wording

A. Oster (2005) calibrated that, if HBV carriers have offspring sex ratios near 1.5, HBV would account for about 47% of Coale's 60 million missing women, mostly in China.

B. The calibration imports a pooled effect from six small family studies as a causal maternal multiplier for national populations, a bridge that later large-sample tests in Taiwan and China did not support.

C. The 47% figure measures the arithmetic consequence of an assumed 1.54 sex ratio, not HBV's contribution to missing women; direct tests in the target populations put that contribution near zero.

D. The question is settled for China by linked parental-HBsAg and offspring-sex data in large representative cohorts; such data find no meaningful carrier effect.

## 16. Failure-mode classification

- [x] Untested premise: the causal, maternal, transferable 1.54 is assumed.
- [x] Proxy problem: the six-study pooled ratio stands in for the target-population effect.
- [x] Fatal proxy failure: direct tests reject the proxy's value in the target populations.
- [x] Level-of-analysis error: small-community data → national accounting.
- [x] Ecological-validity failure: unrepresentative populations and genotypes.
- [x] Omitted confound: parity-specific son preference not analysed.
- [ ] Citation laundering
- [ ] Premise laundering
- [x] Ignored adjacent literature (minor): birth-order demography and Chahnazarian (1986), the latter PROVISIONAL.
- [x] Missing decisive test (at the time): no large parental-status registry test (since run by others).
- [ ] Intervention ratchet
- [ ] Institutional measurement gap
- [x] Definition-operationalization mismatch (abstract framing; scope narrower).
- [ ] Operationalization pathologizes an accurate version
- [x] Construct-establishment gap: FORM, ESTABLISHED-CITED, contested-in-respect-required.
- [ ] Motive claim unsupported

Verification flags:
- [ ] Load-bearing evidence remains PROVISIONAL (no: load-bearing items are FULL-TEXT-CONFIRMED, though in WP versions)
- [x] Full source required (the cited 1975–88 studies and the published versions of the two replications)
- [ ] Reception check required (done in part; Stage 2c)

## 17. Final summary

- Claim under audit status: INVALID
- DEFEATS finding(s): CV-1 (CV-2 consolidated)
- Surviving residual: none
- Residual usefulness grade: none
- Strongest defensible claim: across countries, HBV prevalence is positively associated with share male at birth (ecological, Table 6).
- Claim being overextended: HBV accounts for 47% of Coale's missing women.
- Definition-operationalization mismatch: scope result narrower (abstract vs Coale); no subtype.
- Construct-establishment gap: FORM; claim-map ESTABLISHED-CITED; load-bearing; contested-in-respect-required.
- Grade-before-assert outcome: not applicable (no belief graded); the map's row was P2 WEAK, so no wrongness finding.
- Main proxy problem: SR_HBV 1.54 from six small studies used as a causal maternal multiplier.
- Main level-of-analysis problem: community studies → national accounting.
- Main omitted confound: parity-specific son preference.
- Decisive test: large parental-HBsAg × offspring-sex registry by birth order (run since; negative).
- Citation-use verdict: citing literature accurate in retrieved items; media layer (Slate) major inflation.
- Load-bearing finding(s): CV-1.
- Concede-test result: DEFEATS.
- Failure location: PAPER (with PR-MEDIA inflation separately).
- Overall verdict: INVALID for the claim under audit; residual none.
- Confidence level: High.
- What would change this assessment: a large representative study in a high-prevalence target population finding carrier offspring sex ratios near 1.5 (maternal or paternal), or evidence that the Taiwan and China data are badly misclassified.

## Standardized finding table

CV-8 (Slate major inflation, PR-MEDIA) is recorded in Section 9 only. It concerns the downstream layer, not field 6, so it has no row here.

| Field | CV-1 | CV-3 | CV-4 | CV-5 | CV-6 | CV-7 |
|---|---|---|---|---|---|---|
| Finding | FORM (causal 1.54) contested in the respect required; direct tests ≈0 | Total-effect assumption | Rich-country benchmark despite SRB–life-expectancy gradient | Ecological confounding of L2 | Prevalence inputs from convenience studies | Abstract scope framing |
| Target claim | Field 6 | Field 6 | Field 6 | Field 6 | Field 6 | Field 6 |
| What was measured | Six-study pooled SR | Coale counterfactual | Coale 1.059 / noncarrier 1.048 | Cross-country regressions | PubMed aggregation | Table 11A |
| What was claimed | Causal maternal 1.54 in target populations | Share "accounted for" | Share | HBV causes SRB | Prevalence | 45% of "missing women" |
| Failure mode | Construct-establishment gap | Untested premise | Omitted confound | Omitted confound | Proxy problem | Definition-operationalization mismatch |
| Failure-mode subtype | N/A | N/A | N/A | N/A | N/A | N/A |
| Severity | fatal-for-strong-claim | minor | moderate | moderate | minor | minor |
| Concede test | DEFEATS | NARROWS | NARROWS | NARROWS | SURVIVES | SURVIVES |
| Scope loss if NARROWS | — | incidental: ≤47% upper bound | material: smaller unquantified share | material: association only | — | — |
| Construct property | form | N/A | N/A | N/A | prevalence | N/A |
| Construct-property status | ESTABLISHED-CITED | N/A | N/A | N/A | ESTABLISHED-REPORTED | N/A |
| ESTABLISHED-CITED prosecutor split | contested-in-respect-required | N/A | N/A | N/A | N/A | N/A |
| Operationalization retrieval basis | ITEMS-RETRIEVED | ITEMS-RETRIEVED | ITEMS-RETRIEVED | N/A | N/A | ITEMS-RETRIEVED |
| Operationalization scope result | N/A | N/A | N/A | N/A | N/A | narrower |
| P2 belief grade | N/A | N/A | N/A | N/A | N/A | N/A |
| P2 strength gate | N/A | N/A | N/A | N/A | N/A | N/A |
| Evidence | p.1181; Tables 3, 9, 10; Lin & Luoh WP Table 2; w13971 Sec. 3–4 | p.1165; p.1203–04 | Table 6; Table 10; Klasen 2005 comments, General Comment 3 (p.1–2) | Table 6; p.1186 | p.1188–89; Table 6 note | abstract; Table 11 |
| Evidence type | replication | primary study | methodological critique | primary study | primary study | primary study |
| Verification state | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | FULL-TEXT-CONFIRMED | FULL-TEXT-CONFIRMED | FULL-TEXT-CONFIRMED | FULL-TEXT-CONFIRMED | FULL-TEXT-CONFIRMED |
| Possible innocent explanation | Best available evidence in 2005; flagged "not conclusive" | Author states it and gives a partial estimate | Noncarrier 1.048 already below 1.059 | Region FE and controls included | Standard practice absent registries | Abstract shorthand |
| What would weaken this | Large target-population test finding ≈1.5 | Evidence of no behavioural response | Evidence benchmark gradient is negligible for these units | Within-country causal designs confirming effect | Representative prevalence data giving same inputs | — |
| Failure location | PAPER | PAPER | PAPER | PAPER | PAPER | PAPER |
| Finding disposition | CONFIRMED | CONFIRMED | CONTESTED | CONFIRMED | CONFIRMED | CONFIRMED |
