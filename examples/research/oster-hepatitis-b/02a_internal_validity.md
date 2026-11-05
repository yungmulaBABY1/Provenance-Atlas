# Stage 2a — Internal Validity & Replication Audit

INSTRUMENT PREFLIGHT: prompts/research-analysis/2-internal-validity.txt @ commit a58d165d9a986edca220f8143fc0c0d9316c8a13 | blob/hash ff54b2a6e88d25cfef37c4626aee256d2d2442e8 / sha256 55e8aa1635c33088f91178c275d2776cbb378a95abd0fd9196efec08fbdb5007 | 970 lines | 46009 bytes | markers PRESENT ("INTERNAL VALIDITY & REPLICATION AUDIT PROMPT") | IDENTITY CONFIRMED (operator-pinned commit + blob + sha256; retrieval at the immutable commit, HTTP 200; independently cross-checked by git rev-parse in a separate clone)

SIBLING-PROSECUTOR INPUT: NONE
INDEPENDENCE STATUS: INDEPENDENT

Effort: high (as briefed). The full pinned prompt was read before writing.

## Inputs

1. Foundational paper: Oster (2005) JPE 113(6):1163–1216, published version, read in full (institutional copy, not committed). Locators are JPE pages.
2. Central finding: taken from the Stage 1 map (supplied: 01_claim_extraction.md).
3. Downstream use: Stage 1 Field 4 (Slate 2005; citing literature).
4. Known replication attempts, retrieved this run from authorized copies:
   - Lin & Luoh 2008 working-paper version (authors' homepage, NTU; HTTP 200). VERSION-SUBSTITUTE for AER 98(5):2259–73.
   - Oster, Chen, Yu & Lin, NBER WP w13971, May 2008 (nber.org; HTTP 200). VERSION-SUBSTITUTE for Economics Letters 107(2), 2010.
   - Klasen 2005 comments (Göttingen institutional page, HTTP 200) and the Klasen VoxEU column (WebFetch 200): critiques, not replications.
5. Pre-registration: none. This is a 2005 observational economics paper; the paper reports none (reported in the paper itself, by absence: no registration is mentioned anywhere).
6. Construct-validity output: NONE.

## Claim-map confirmation

- Claim under audit (map field 6): HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale's (1991) 60.26 million missing women (Table 11, Panel A).
- What was literally measured (map field 1):
  - carrier status/prevalence ↔ offspring/population sex-ratio associations (six small family studies; Alaska/Taiwan series; 38-country cross-section; immigrants; Chinese counties);
  - plus a calibrated re-run of Coale's accounting with SR_HBV = 1.54.
- Weaker defensible claim (map field 3): conditional on SR_HBV 1.54, the author's prevalence inputs and Coale's framework, about 47% (CI 13.5–71.5) is an upper-bound total effect. The aggregate associations are consistent with, but not decisive for, causality.
- Target layer: source claim.

Load-bearing chain for Field 6:
- Table 11 (p.1202) takes predicted SRB from Table 10 (p.1200).
- Table 10 = 1.048·(1 − prevalence) + **1.54**·prevalence, with prevalence among pregnant women.
- 1.54 comes from the pooled six-study individual-level estimate (Table 9 Panel A, p.1199).
- The aggregate evidence (Tables 4–8, 12) corroborates direction and rough magnitude but does not enter the calculation.

## Section A — Data generation audit

| Data source | Collection method | Selection bias risk | Missingness pattern | Incentive structure risk | AI-analysis check run |
|---|---|---|---|---|---|
| Six family studies 1975–88 (Table 3, p.1180) | Retrospective/opportunistic serology plus reported offspring, collected by the Blumberg research group and others; observational | High: small convenience populations (Greenland, Kar Kar, Greek villages, Philippines, France); literature selected for reporting a sex-ratio association | Cannot assess: offspring reporting and inclusion rules vary by study; which parent is the carrier varies | Moderate: the originating group proposed the hypothesis | N/A |
| Country HBsAg prevalence (p.1188–89; Table 10) | Author aggregation of PubMed studies, countries with ≥2,500 tested | High: prevalence studies are convenience samples (blood donors, pregnant women, villages); study list off-paper (author's web page, not retrieved) | MNAR likely: countries with few studies drop out (38 retained) | Low | N/A |
| UN Demographic Yearbook SRB (Table 6) | Administrative registration | Moderate: registration completeness varies; the paper shows a complete-reporting subsample, N=30 | MNAR (under-registration of girls is itself the rival R1) | Low | N/A |
| IPUMS (Tables 2, 4, 7), Taiwan factbook (Table 5), Africa DHS (Table 8), Chinese counties (Table 12) | Census/survey/administrative | Moderate | Cannot assess | Low | N/A |
| Coale (1991) inputs (Table 11) | Published model-life-table accounting | Low for this step (taken as given) | — | Low | N/A |

Determination basis: reported in the paper itself (pages cited).

- All load-bearing data are observational. The calibration treats the pooled association (1.54) as a causal per-carrier effect.
- The paper itself grades this evidence as "clearly suggestive … it is not conclusive" (p.1181).

## Section B — Pre-registration and analysis plan

| Pre-registration status | Analysis match | Outcomes tested | Outcomes reported | Post-hoc subgroups | P-hacking risk |
|---|---|---|---|---|---|
| None (reported in paper by absence; era-typical) | Cannot assess | Many: at least 6 cross-country variants (Table 6), immigrant and DHS variants, Alaska ×2, Taiwan ×2, India/China counties | Reported specifications are all directionally consistent | Region, OECD and complete-reporting subsamples; Iran and Mexico discussed as outliers | Moderate |

There is no evidence of null specifications being suppressed. However, specifications that point the same way share the same prevalence inputs, so their agreement is not independent.

## Section C — Effect size and statistical power

| Reported effect size | Field typical range | Corrected meta-analysis estimate | Sample size | Estimated power | Winner's curse risk |
|---|---|---|---|---|---|
| Carrier offspring SR 1.54 (CI 1.29–1.87); P(male) ≈ .606 vs .512 for noncarriers (≈ +9.4 pp) | Known SRB determinants move P(male) by ≤ ~1 pp (field context; PROVISIONAL, not retrieved) | No meta-analysis. Large-sample estimates: maternal +0.10 to +0.25 pp (Lin & Luoh, Taiwan, ~3M births); no maternal or paternal effect (Oster et al. 2008, China, ~67,000 cohort members) | 603 carrier-parent children, 4,126 noncarrier (Table 3) | High power for a 9-pp effect (z ≈ 3.8 on the raw pooled share); very low power for effects of the size later found (~0.25 pp) | High |

Derivation mode: COMPUTED-FROM-RETRIEVED.
- P(male) = SR/(1+SR).
- z = (355/603 − .512)/√(.25/603) ≈ 3.8.
- Lin & Luoh Table 2: HBsAg(+) .51969 vs (−) .51736 on 1,440,949 births (mothers aged ≤25 at first appearance).
- An effect 30–90× larger than later large-sample estimates, drawn from a small, hypothesis-originating literature, matches the winner's-curse pattern.

## Section D — HARKing

| Hypothesis type | Pre-registered? | HARKing indicators | HARKing risk |
|---|---|---|---|
| Directional hypothesis stated up front (HBV raises SRB), derived from prior medical literature | No | None strong: the direction is fixed by the prior Blumberg literature; the calibration is presented as illustrative | Low |

## Section D2 — Forking paths

| Decision point | Choice made | Pre-specified? | Defensible alternatives | Result under alternatives | Fragility |
|---|---|---|---|---|---|
| Source of SR_HBV for the calibration | Individual-level pooled 1.54 (Table 9A) | No | Aggregate 1.40–1.60 (Table 9B); Taiwan implied ~1.25 (p.1186); large-sample external estimates ≈1.06 (Lin & Luoh) | Holds (1.40–1.60); weakens substantially (1.25); disappears (external large-sample) | Fragile |
| Which parent's prevalence | Prevalence among pregnant women (Table 10) | No | Paternal or either-parent prevalence (the pooled studies mix carrier parents) | Untested in paper | Untested |
| Noncarrier SRB | 1.048 from lowest-prevalence countries (Table 10) | No | 1.05–1.06 (Coale 1.059) | Untested; share sensitive | Untested |
| Prevalence data inclusion | ≥2,500 tested, PubMed aggregation | No | Other thresholds or WHO categories | Cross-country coefficient stable across reported variants (.0009–.0014) | Mixed |
| Total vs partial effect | Total effect (no behavioural response) | Stated (p.1165) | Partial effect via counterfactual counties | China partial 62% vs total 76% (p.1204) | Mixed |

Integration: the fragility on the first decision point coincides with no pre-registration and a high winner's-curse risk. These are consolidated as one inference: the calibration input may be specific to a small, selected literature rather than a stable effect (see IV-1 / IV-2).

## Section E — Selective reporting

| Outcomes registered | Outcomes reported | Missing outcomes | Subgroup selectivity | Publication bias indicators |
|---|---|---|---|---|
| None | All analyses directionally supportive | No sign of omitted specifications in the paper; the effect by birth order is not reported (relevant to R1) | Low–moderate | Positive result in a top journal; the input literature is from the hypothesis-originating group; later large-sample estimates are far smaller |

## Section F — Replication status

| Direct replications | Success rate | Pre-registered reps | Independent reps | Meta-analytic estimate | Effect shrinkage | Verification state |
|---|---|---|---|---|---|---|
| 2 large-sample individual-level tests located and read: Lin & Luoh 2008 (Taiwan, maternal, ~3M births) and Oster, Chen, Yu & Lin 2008/2010 (China, maternal + paternal, ~67,000 cohort) | 0/2 reproduce an effect near 1.5 (Lin & Luoh: maternal +0.10 to +0.25 pp, i.e. SR ≈1.06 vs 1.05; Oster et al.: no effect, e.g. paternal carriers 51.06% boys vs non-carriers 51.56%) | 0 | 1 independent (Lin & Luoh); 1 same-author (Oster et al.) | none | From +9.4 pp to ≈0–0.25 pp | FULL-TEXT-CONFIRMED and RECEPTION-CONFIRMED (both read in authorized working-paper versions; published versions not retrieved: VERSION-SUBSTITUTE) |

- Locators:
  - Lin & Luoh WP abstract, Table 2, Sec. 4.
  - Oster et al. w13971, abstract, pp.3–6, Sec. 4.
- Current best estimate:
  - maternal carrier effect on P(male) ≈ +0.1 to +0.25 pp (Taiwan);
  - no detectable maternal or paternal effect in the China cohort.
- This does not support the 1.54 input or the downstream 47% share.
- Lin & Luoh's own upper-bound calculation: HBV explains about 0.9–1.8% of China's missing women (WP introduction p.2).

## Section G — Data and code availability

| Data available | Code available | Reanalysis attempted | Reanalysis result | PubPeer flags | Corrections issued | Verification state |
|---|---|---|---|---|---|---|
| A publisher supplement "31452.dataset.zip" is listed on the JPE page (from a search snippet), but retrieval failed (HTTP 403). The prevalence study list is on the author's page (HTTP 403) | Unknown | This audit: NOT RUN (replication/NOT_RUN.txt). Third party: Oster et al. re-analysed the Greece/Philippines data and found a paternal, not maternal, association (w13971 p.3; reported in Chen et al. 2008, not retrieved) | See left | Not checked (PubPeer not queried this run) | No formal correction or retraction (Crossref, Stage 1). Author's successor paper: "we conclude that hepatitis B carrier rates cannot explain male-biased sex ratios or the 'missing women' in China" (w13971 Sec. 4) | Data existence: PROVISIONAL (snippet only). Corrections: Crossref-checked. Successor: FULL-TEXT-CONFIRMED |

## Section H — Summary table

| Dimension | Assessment | Severity | Notes |
|---|---|---|---|
| Data generation quality | Small, old, convenience family studies drive the input | Major | IV-1 |
| Selection bias | High (studies and prevalence sources) | Moderate | Section A |
| Missingness handling | Not addressed | Moderate | Registration completeness only partly handled (N=30 subsample) |
| Incentive structure risk | Moderate (hypothesis-originating literature) | Minor | |
| Pre-registration | None | Minor | Era-typical |
| Analysis plan compliance | Cannot assess | Cannot assess | |
| P-hacking risk | Moderate | Minor | |
| Effect size plausibility | 9.4-pp shift implausibly large relative to large-sample estimates | Major | IV-2 |
| Statistical power | Adequate for the reported size; inadequate for realistic sizes | Moderate | |
| Winner's curse risk | High | Major | IV-2 |
| HARKing risk | Low | None | |
| Forking-paths fragility | Fragile on SR_HBV source | Major | IV-4 |
| Selective reporting | Low–moderate | Minor | Birth-order split not reported |
| Replication success rate | 0/2 large-sample | Fatal (for the 47% claim) | IV-2, IV-3 |
| Effect size trajectory | Collapsed to ≈0 | Fatal (for the 47% claim) | |
| Data/code availability | Listed but not retrieved | Cannot assess | Replication NOT_RUN |
| Post-publication flags | Author's successor concludes no China effect | Major | IV-3 |

## Section H2 — Concede test

| Finding | Verification state | Technical outcome status | Conditional concede result | Verdict eligibility | Eligibility basis | Surviving claim if NARROWS |
|---|---|---|---|---|---|---|
| IV-1 The calibration's SR_HBV = 1.54 rests on six small heterogeneous studies (603 carrier-parent children) that the paper itself calls "not conclusive" (p.1181; Tables 3, 9) | FULL-TEXT-CONFIRMED | SOURCE-DIRECT | NARROWS | ELIGIBLE | Paper's own tables and text | 47% is a conditional illustration; the CI already spans 13.5–71.5 |
| IV-2 Large-sample individual data (Lin & Luoh, Taiwan, ~1.44M births in the restricted sample) find a maternal effect of +0.10 to +0.25 pp on P(male), vs about +9.4 pp implied by 1.54 | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | INDEPENDENT-REANALYSIS-CONFIRMED (independent data, method and result stated; WP Table 2, Sec. 4) | DEFEATS | ELIGIBLE | Independent study read in detail; the calibration uses maternal (pregnant-women) prevalence, so the test matches the input as used | — |
| IV-3 The author's own successor study (China cohort, ~67,000; maternal and paternal status) finds no carrier effect and concludes HBV "cannot explain male-biased sex ratios or the 'missing women' in China" | FULL-TEXT-CONFIRMED (NBER WP version) | ACKNOWLEDGED-CORRECTION (author response explicitly withdrawing the China conclusion; not a journal notice) | DEFEATS (China accounts for 23.24M of the 28.47M explained) | ELIGIBLE | Author statement, w13971 Sec. 4 | — |
| IV-4 The calibration result depends on choosing the individual-level 1.54 over the paper's own lower Taiwan estimate (~1.25, p.1186) | FULL-TEXT-CONFIRMED | SOURCE-DIRECT | NARROWS | ELIGIBLE | p.1186, Table 9 | The share would fall materially with 1.25; not recomputed (would require the paper's prevalence inputs per country; not reconstructed) |
| IV-5 Text states "roughly 47 percent, or 31 million, of Coale's missing women are explained" (p.1201), but Table 11 shows 31.79M *remaining* and 28.47M explained | FULL-TEXT-CONFIRMED | SOURCE-DIRECT | SURVIVES | ELIGIBLE | Table 11 arithmetic: (60.26−31.79)/60.26 = 47.24% | — |
| IV-6 Aggregate evidence is ecological, with prevalence from convenience studies and a vaccination timing that coincides with sex-selection technology (Taiwan, p.1186; acknowledged) | FULL-TEXT-CONFIRMED | SOURCE-DIRECT | NARROWS (L2 only; not an input to Field 6) | ELIGIBLE | Paper's own caveats | Associations consistent with, not decisive for, HBV causation |
| IV-7 Re-analysis of the original Greece/Philippines data reportedly finds a paternal, not maternal, association | FULL-TEXT-CONFIRMED (as reported in w13971 p.3) | UNVERIFIED (Chen, Oster, Yu & Lin 2008 not retrieved) | NARROWS (would undercut the use of maternal prevalence) | PENDING VERIFICATION | Retrieve Chen et al. 2008 and check the re-analysis tables | — |
| IV-8 Birth-order pattern: Chinese SRB is normal at first births and elevated at higher orders (R1) | FULL-TEXT-CONFIRMED (Lin & Luoh Table 1 and text citing Das Gupta) | UNRESOLVED (Das Gupta 2005 and Oster 2006 reply not retrieved for 2a) | NARROWS | PENDING VERIFICATION | Retrieve Das Gupta 2005/2006 and Oster 2006 | — |

| Finding | Scope-loss level | Original claim | Surviving claim | What practical or inferential work is lost? |
|---|---|---|---|---|
| IV-1 | Material | 47% of Coale's missing women | Conditional illustration with wide CI | Cannot be stated as an estimate |
| IV-4 | Material | 47% | Smaller under the paper's own Taiwan estimate | Magnitude |
| IV-6 | Incidental (for field 6) | — | — | Causal reading of L2 |

## Section I — Verdict

- Claim under audit: INVALID
- Eligible DEFEATS finding(s): IV-2 (INDEPENDENT-REANALYSIS-CONFIRMED); IV-3 (ACKNOWLEDGED-CORRECTION)
- Eligible MATERIAL NARROWING finding(s): IV-1, IV-4
- Findings pending verification:
  - IV-7 | NARROWS | re-analysis not retrieved | retrieve Chen, Oster, Yu & Lin 2008
  - IV-8 | NARROWS | Das Gupta/Oster exchange not retrieved | retrieve PDR 31(3), 32(2)
- Pending-evidence effect on assessability: NONE
- Surviving residual: none for the 47% share. A separate, narrower residual on L2 survives: population SRB is positively associated with HBV prevalence in cross-country and some within-country aggregate data (Tables 6–8, 12). That residual no longer performs the accounting work.
- Internal-validity grade: E

Answers:
1. Is the foundational finding (carrier SR ≈1.5) likely real? No, not at that magnitude, on the large-sample evidence read (IV-2, IV-3).
2. Even if a small effect is real, is it sufficient for the downstream claim? No. +0.25 pp implies ≈1–2% of China's missing women (Lin & Luoh, upper bound).
3. Best current estimate of the effect: maternal +0.10–0.25 pp on P(male) (Taiwan); no effect, maternal or paternal (China cohort).
4. What would upgrade the grade: none. The relevant large tests exist and are negative.
5. Decisive test not run: none outstanding for L1 in Taiwan/China. Paternal effects outside China remain only partly tested (IV-7).
6. AI-assisted analysis: N/A.
7. Fragile to analytical choices: yes, on the SR_HBV source.
8. Usable residual: "surviving residual: none" for field 6.

## Section J — Integration with construct validity

SIBLING-PROSECUTOR INPUT: NONE
INDEPENDENCE STATUS: INDEPENDENT

No construct-validity output was formally supplied to this run. The following reasons only from general construct concerns and does not adopt any specific sibling finding or verdict visible elsewhere in session context.

The foundational finding is not likely real at the magnitude used, based on the eligible internal-validity evidence. Even if the construct interpretation is accepted, the 47% share does not follow, because its key input fails large-sample replication. Any specific construct-validity compounding claim remains outside this independent run.

## Section K — Summary

- **Verdict.** The finding that HBV accounts for 47.24% of Coale's missing women is INVALID on internal-validity grounds (grade E).
- **Why.** Its load-bearing input, a carrier offspring sex ratio of 1.54 pooled from six small 1975–88 family studies, was not reproduced by the two large individual-level tests read in this run:
  - Lin & Luoh, about 1.4–3M Taiwanese births: maternal effect +0.10–0.25 pp on the probability of a male birth, against roughly +9.4 pp implied by 1.54;
  - Oster, Chen, Yu & Lin, a China cohort of about 67,000: no maternal or paternal effect. Its authors, including the target's author, conclude that HBV cannot explain China's missing women.
- **Current best estimate.** About 0–0.25 pp.
- **Data.** Data generation for the input is weak: convenience samples from a hypothesis-originating literature. Winner's-curse risk is high, and the calibration is fragile to the choice of SR_HBV source.
- **Concede test.** The load-bearing concede tests are eligible DEFEATS (IV-2, IV-3).
- **Surviving residual.** None for field 6. A narrower aggregate association (L2) survives but no longer carries the accounting.
- **Replication.** Replication of the paper's own calculations was not run (data blocked, HTTP 403). This does not affect the verdict, which rests on external evidence and the author's own correction.
- **Construct validity.** If a construct-validity failure (e.g., benchmark choice) were independently established, it would compound with this result only by further lowering an already-defeated share.
- **Decisive test.** Already run: large linked registries of parental HBV status and offspring sex.

## Standardized finding table

| Field | IV-1 | IV-2 | IV-3 | IV-4 | IV-5 | IV-6 | IV-7 | IV-8 |
|---|---|---|---|---|---|---|---|---|
| Finding | 1.54 rests on six small heterogeneous studies | Large Taiwan registry finds maternal effect ≈0.1–0.25 pp | Author's successor finds no China effect and withdraws China conclusion | Calibration ignores paper's own lower Taiwan estimate | "31 million … explained" mislabels the remaining count | Aggregate evidence ecological and confounded in timing | Original data re-analysis: paternal not maternal | China SRB elevated only at higher parities |
| Target claim | Field 6 | Field 6 | Field 6 | Field 6 | Field 6 | Field 6 (via L2) | Field 6 | Field 6 |
| What was measured | Table 3/9 pooled OLS | Probit/OLS on HBMI registry, 1988–99 | Cohort offspring sex by parental HBsAg | Table 5 vs Table 9 | Table 11 | Tables 4–8 | Re-analysis (reported) | SRB by birth order |
| What was claimed | SR_HBV 1.54 | SR_HBV ≈1.5 | HBV explains ~75% in China | 47% | 47% / 31M | HBV raises population SRB | maternal-prevalence calibration | biological SRB elevation |
| Failure mode | data generation / power | failed replication / effect shrinkage | post-publication correction | forking paths | reporting error | confounding | data generation | rival explanation |
| Severity | moderate | fatal-for-strong-claim | fatal-for-strong-claim | moderate | minor | moderate | moderate | moderate |
| Concede test | NARROWS | DEFEATS | DEFEATS | NARROWS | SURVIVES | NARROWS | NARROWS | NARROWS |
| Scope loss if NARROWS | material: conditional illustration | — | — | material: smaller share | — | incidental | material | material |
| Evidence | p.1180–81, p.1199 | Lin & Luoh WP Table 2, abstract | w13971 abstract, Sec. 4 | p.1186; Table 9 | p.1201; Table 11 | p.1186; Table 6 | w13971 p.3 | Lin & Luoh WP Table 1 |
| Evidence type | primary study | replication | replication (same author) | primary study | primary study | primary study | replication (reported) | primary study (secondary report) |
| Verification state | FULL-TEXT-CONFIRMED | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | FULL-TEXT-CONFIRMED | FULL-TEXT-CONFIRMED | FULL-TEXT-CONFIRMED | FULL-TEXT-CONFIRMED | PROVISIONAL (underlying not retrieved) | PROVISIONAL |
| Possible innocent explanation | Best evidence available in 2005; paper flags it as not conclusive | Taiwan maternal-only; genotype or paternal pathways differ | Village-official offspring reports may be noisy; China-specific | Taiwan series short and confounded; author judged 1.5 better supported | Typo or slip | Author tests multiple sources and controls | Small original data | Higher-order elevation could coexist with HBV |
| What would weaken this | Large studies confirming ≈1.5 | A larger, paternal-status study confirming a large effect | Evidence the cohort's offspring data are badly misreported | Evidence Taiwan estimate is biased downward | Errata showing different numbers | A clean natural experiment | Retrieved re-analysis showing a maternal effect | Data showing first-birth SRB elevation tracks HBV |
| Failure location | PAPER | PAPER | PAPER | PAPER | PAPER | PAPER | PAPER | PAPER |
| Status | confirmed | confirmed | confirmed | confirmed | confirmed | confirmed | provisional | provisional |
