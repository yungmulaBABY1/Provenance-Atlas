# Stage 1 — Claim Extraction / Inflation Map

Target: Oster, Emily. 2005. "Hepatitis B and the Case of the Missing Women." *Journal of Political Economy* 113(6): 1163–1216. DOI 10.1086/498588.
Run: Batch 1, audit/oster-hepatitis-b. Executor: Grok Bot (audit run). Run date 2026-11-05 (UTC); operator TZ America/Los_Angeles.

INSTRUMENT PREFLIGHT: prompts/1-claim-extraction.txt @ commit a58d165d9a986edca220f8143fc0c0d9316c8a13 | blob/hash 894579a79e67508bdc4026b77c0a104681f903ad / sha256 656b11c301931726a5435b231774f40797a10fd0cab950224616fc18951c035f | 1038 lines | 44072 bytes | markers PRESENT ("CLAIM EXTRACTION / INFLATION MAP") | IDENTITY CONFIRMED against operator-pinned immutable commit + blob + sha256 (retrieval form: IMMUTABLE REMOTE, raw.githubusercontent at the pinned commit, HTTP 200; independently cross-checked by `git rev-parse a58d165:prompts/1-claim-extraction.txt` in a separate clone).

## Inputs

- Target document: published JPE version (54-page PDF, pp. 1163–1216), retrieved from the Belfer Center (Harvard Kennedy School) institutional publication page. Pages carry a University of Chicago Press download stamp. The author's own working-paper version (dated 23 Aug 2005, emilyoster.net) was also retrieved for version comparison. Neither file is committed. Locators below use JPE page numbers.
- Document type: peer-reviewed journal article (economics), empirical and calibration.
- Downstream uses: none supplied. Field 4 was searched actively (see below).
- The claim that prompted this audit: the operator brief names the paper (Batch 1). No downstream claim was supplied.

## Publication status

PUBLICATION STATUS: no correction, corrigendum, retraction or expression of concern found. Crossref record for 10.1086/498588: `relation` is empty, `update-to`/`updated-by` are absent, and `filter=updates:10.1086/498588` returns 0 results (HTTP 200, raw/crossref_updates.json). The publisher landing page could not be checked (HTTP 403 to scripted access). Check basis: Crossref only. Critiques and the author's later work are NOT listed here; they belong to Stage 2c and Stage 3.

## Field 1 — Literally measured

The paper uses several data sources. Each estimates something narrower than "missing women":

1. **Individual carrier–offspring sex ratio** (Sec. IV.B, Table 3, p.1180; calibration Sec. IV.E, Table 9, p.1199). Six small published family studies from 1975–1988 (Greenland, Kar Kar, Greece ×2, Philippines, France). Combined: children of HBsAg-carrier parents 355 boys / 248 girls; noncarrier parents 2,083 / 2,043. A pooled child-level OLS with study fixed effects gives offspring sex ratio for carriers SR_HBV = 1.54, 95% CI (1.29, 1.87) (p.1199). The studies differ in which parent was a carrier, and the paper reports that mechanism and data quality are unknown (p.1181).
2. **Within-population time series around vaccination** (Sec. IV.C):
   - Alaska Natives vs non-Natives, IPUMS 1970–1990: Native×1980 coefficient .034, N=5,041 (Table 4, p.1184).
   - Taiwan cohort sex ratios against HBV prevalence among women of childbearing age, 96 cohort-years: coefficient .00056 (t 2.76) (Table 5, p.1186).
3. **Cross-country association** (Sec. IV.D):
   - Country HBV carrier prevalence aggregated by the author from PubMed "HBsAg [country]" studies; ≥2,500 tested gives 38 countries (p.1188–89; study list on the author's web page).
   - Regressed on the UN Demographic Yearbook sex ratio at birth: coefficient .0009 (t 4.63), R² .37 (Table 6, p.1191). Variants with controls, OECD subsample, regional FE, and a complete-reporting sample (N=30) give .0010–.0014.
   - Further variants: IPUMS US immigrant children by mother's birth country (Table 7, N=210,556, .0013); Africa DHS (Table 8).
   - Within-country: India states and 60 Chinese counties (Table 12, p.1204).
4. **Accounting step** (Sec. IV.E–V.A, Tables 10–11, pp.1200–1202):
   - Predicted country sex ratio at birth = noncarrier SR 1.048 × (1 − prevalence among pregnant women) + 1.54 × prevalence.
   - These replace Coale's (1991) constant 1.059 in Coale's own missing-women formula (eq. 1–2), using Coale's model life tables and mid-1980s populations.
   - Output: HBV-adjusted missing women per country, and the share of Coale's (or Sen's) count "explained".

What is literally measured: associations between HBsAg carrier status or prevalence and offspring or population sex ratios, in small family studies and in aggregate data. The "share of missing women explained" is not measured. It is a calibrated counterfactual: Coale's accounting rerun with an HBV-predicted sex ratio at birth.

### Definition–operationalization check
- Named central construct: "missing women", i.e. women absent relative to an expected population sex ratio. In the abstract this is framed by Sen's "as many as 100 million" (p.1163).
- Operationalization (ITEMS-RETRIEVED: eq. 1–2 p.1168–69; Table 11 columns and note p.1202): Coale's (1991) calculation for seven countries/regions (China, India, Pakistan, Bangladesh, Nepal, Western Asia, Egypt) with mid-1980s populations. Coale's total = 60.26M. Panel B repeats the comparison against Sen's 0.977 benchmark, total 107.47M.
- Scope result: **narrower**. The headline share ("about 45 percent", abstract) is a share of Coale's 60.26M for seven units in the 1980s. It is not a share of "as many as 100 million" (Sen), and it does not cover later cohorts. Out-of-scope items: Sen-benchmark counts (Panel B, 70.42%); post-1990 cohorts and the period of prenatal sex selection (acknowledged p.1165); partial vs total effect (p.1165, p.1203). MAP CONTENT, not a verdict.

### Construct-establishment check (triggered: causal escalation — sex-ratio bias "may be less attributable to differences in tastes and preferences", p.1165)
- PREVALENCE (HBV carrier prevalence by country): ESTABLISHED-REPORTED. Author-compiled PubMed aggregation, Table 10 p.1200; study list off-paper on the author's web page, not retrieved.
- FORM (carrier → offspring sex ratio ≈1.5): ESTABLISHED-CITED (Blumberg-group studies, Table 3) plus ESTABLISHED-REPORTED (pooled re-estimate, p.1199). The source's own grading is "clearly suggestive … it is not conclusive" (p.1181).
- DOMAIN (which populations and periods the counterfactual covers): ESTABLISHED-REPORTED (Table 11: seven units, mid-1980s).
- WRONGNESS: row not applicable as a belief-accuracy property. The paper does not grade a belief; it re-estimates a count.
- HARM: row not applicable. No harm claim about a construct.

## Field 2 — Source's strongest claim (hedges preserved)

- Abstract (p.1163): "I argue that hepatitis B can account for about 45 percent of the 'missing women': around 75 percent in China". It continues: "between 20 and 50 percent in Egypt and western Asia, and under 20 percent in India, Bangladesh, Pakistan, and Nepal."
- Body (p.1201): "After I adjust for HBV, roughly 47 percent, or 31 million, of Coale's missing women are explained." The confidence interval is given as "roughly 13.5–70 percent" (p.1201).
- Conclusion (p.1205): HBV "decreases the number of missing women by around one-half."
- Interpretive step (p.1165): "sex ratio bias may be less attributable to differences in tastes and preferences than many have suggested."
- Hedges and caveats that the source states:
  - total, not partial, effect: "there would be no compensating behavioral response. This is unrealistic." (p.1165; repeated p.1203);
  - prenatal sex-selection technology after about 1990 (p.1165);
  - the individual-level evidence "is not conclusive" (p.1181).
- Where hedging differs: the abstract keeps "I argue … can account" but omits the confidence interval (13.5–71.5%), the total-vs-partial caveat, and the Coale-only denominator.

## Field 3 — Weaker defensible claim (author reconstruction from Field 1)

Take three inputs as given:
- (i) the carrier offspring sex ratio of 1.54, estimated from six small, heterogeneous family studies;
- (ii) the author's PubMed-aggregated prevalence for pregnant women;
- (iii) Coale's 1980s accounting framework and benchmark.

Under those inputs, an HBV-elevated sex ratio at birth would account for roughly 47% (95% CI about 13.5–71.5%, reflecting sampling uncertainty in (i) only) of Coale's 60.26M missing women in seven Asian/North African units. This is an upper-bound total effect assuming no compensating behaviour. The share is about 76% for China and under 20% for India.

Supporting this, the population sex ratio at birth is positively associated with HBV prevalence across countries, with immigrant mothers, in Alaska, in Taiwan cohorts and in Chinese counties. These associations are consistent with, but not decisive for, a causal carrier effect.

## Field 4 — Downstream claim (searched)

Searches run this stage: web search for media/press restatements and for critiques and data. Retrieved pages are logged in the worklog with HTTP status. Labels follow the four provenance states.

| ID | Layer | Provenance | Quoted restatement (<25 words) | Locator |
|---|---|---|---|---|
| D1 | PR / media | RETRIEVED | "her detective work has established the fate of roughly 50 million of Amartya Sen's missing women" | Dubner & Levitt, "The Search for 100 Million Missing Women," Slate, 24 May 2005, paragraph beginning "If you believe Oster's numbers"; https://slate.com/business/2005/05/where-did-100-million-missing-women-go.html (HTTP 200) |
| D1b | PR / media | RETRIEVED | "Except the women weren't really missing at all, for they had never been born." | same article, preceding sentence |
| D2 | citing literature (working paper of a later journal article) | RETRIEVED | "estimated that as much as half of the 'missing women', and up to 75 percent of those in China could be explained by HBV" | Lin & Luoh, "HBV and Missing Women" (2008 working-paper version of AER 98(5)), introduction p.2; author homepage, homepage.ntu.edu.tw/~mjlin (HTTP 200) |
| D3 | citing literature (critical comment) | RETRIEVED | "About half of the 60 million missing women that Coale had calculated in 1991 can be explained this way." | Klasen, "Comments on Paper by Emily Oster," 8 July 2005, p.1 "Main Message"; uni-goettingen.de (HTTP 200) |
| D4 | citing literature / commentary | RETRIEVED | "Around 45% to 70% of the alleged 100 million victims of anti-female discrimination were missing due to this biological relationship." | Klasen, "Hepatitis B and missing women: the rise and decline of a finding," VoxEU column, para 1; cepr.org (WebFetch 200; curl 403) |

- RETRIEVED (secondary only): R. Barro, Business Week, 28 Feb 2005, "biology explains a good deal of the missing-women puzzle". It was seen only as a quotation inside D4 (para 4). The primary text was not accessed, and it concerns the February 2005 draft. Not anchor-eligible.
- RECALLED: later popular-book restatements (Freakonomics-related) of the hepatitis-B explanation are believed to exist. They were not retrieved this run and do not anchor anything.
- Scope note: no exhaustive enumeration of press coverage, encyclopedia entries or model summaries was attempted.

Attribution and scope arithmetic:
- **D1 / D1b (Slate)**
  - Cites the paper as "soon-to-be-published", i.e. a pre-publication version. The March 2005 draft was not retrieved (version substitute: JPE published).
  - Against the audited version: Panel A explains 60.26 − 31.79 = 28.47M of Coale's count; Panel B explains 75.68M of Sen's 107.47M. "roughly 50 million of Amartya Sen's missing women" matches neither, and it reframes the share onto Sen's benchmark.
  - D1b drops the total-vs-partial caveat. On the paper's own partial-effect counterfactual (p.1203–04), not all of the women "had never been born" in the counterfactual sense.
  - Classification: downstream restatement with baseline substitution (Coale → Sen) and hedge removal. The successor version could not be compared.
- **D2**: consistent with the source ("as much as half"; "up to 75 percent in China"). No inflation apparent.
- **D3**: consistent with Panel A.
- **D4**: quotes the 45–70% range, which maps to the Coale/Sen panels. Attaching it to "the alleged 100 million" mixes denominators; this is a critic's paraphrase. No inflation attributed to the paper.

## Field 5A — Within-source inflation point + failure location

Candidate within-source transitions (MAP CONTENT, not verdicts):

1. **Body numerics.** "roughly 47 percent, or 31 million, of Coale's missing women are explained" (p.1201). In Table 11 (p.1202), 31.79M is the HBV-adjusted *remaining* count, so the number explained is 28.47M. The sentence's "31 million" therefore does not match the table's explained quantity. The text CI "roughly 13.5–70" vs the table's (13.5, 71.5) is rounding.
2. **Abstract scope.** "about 45 percent of the 'missing women'" appears beside the "as many as 100 million" framing. The quantity is a share of Coale's 60.26M. The abstract omits the CI and the total-vs-partial caveat that the body states (p.1165, p.1203).
3. **Abstract range vs table.** "between 20 and 50 percent in Egypt and western Asia" vs Table 11: Egypt 53.67%, Western Asia 29.54%. In the body (p.1201), Bangladesh is "intermediate", while the abstract lists it "under 20 percent" (table 19.64).
4. **Provenance of the evidence.** The abstract presents carrier offspring sex ratios "around 1.50" as "new evidence". The 1.54 estimate re-pools six existing small studies (Table 3/9). The paper's new evidence is aggregate (cross-country, Alaska, Taiwan), and those aggregate estimates are not the input used in the calibration (Table 9, p.1199).

Failure location: PAPER. Abstract vs body, and one body sentence vs its own table. Basis: FULL-TEXT-CONFIRMED (published version read in full).

## Field 5B — Downstream inflation point + failure location

PR / MEDIA. Anchored on D1 and D1b (RETRIEVED, ANCHOR-ELIGIBLE).
- The move: a share of Coale's 1980s count (total effect, upper bound) becomes "established the fate of roughly 50 million of Amartya Sen's missing women", plus "had never been born".
- This is a baseline (scope) substitution plus hedge removal ("I argue … can account" → "established").
- Verification: D1 RETRIEVED; target FULL-TEXT-CONFIRMED.
- Caveat: D1 describes a pre-publication version that was not retrieved, so part of the numeric gap may reflect version differences.

Citing-literature layer: no inflation found in the retrieved items (D2, D3).

### Anchoring table

| Item | Provenance state | Quotation present? | Locator present? | Attribution cross-source-confirmed, if applicable? | Anchor eligibility |
|---|---|---|---|---|---|
| D1 Slate 2005 | RETRIEVED | yes | yes | N/A (not classified MISATTRIBUTED) | ELIGIBLE |
| D1b Slate 2005 | RETRIEVED | yes | yes | N/A | ELIGIBLE |
| D2 Lin & Luoh WP | RETRIEVED | yes | yes | N/A | ELIGIBLE (no inflation found) |
| D3 Klasen 2005 | RETRIEVED | yes | yes | N/A | ELIGIBLE (no inflation found) |
| D4 Klasen VoxEU | RETRIEVED | yes | yes | N/A | ELIGIBLE (critic paraphrase; no inflation attributed) |
| Barro 2005 | RETRIEVED only as secondary quotation | yes (secondary) | partial | N/A | NOT ELIGIBLE — primary not accessed; concerns Feb-2005 draft |
| Popular-book restatements | RECALLED | no | no | N/A | NOT ELIGIBLE — recalled only |

## Claim inventory

| Claim | Quantified? | Why it might be inflated | Selected for Field 6? |
|---|---|---|---|
| C1 HBV accounts for 47.24% (CI 13.5–71.5) of Coale's 60.26M missing women (Table 11A) | yes | rests on 1.54 from six small studies; total-effect assumption; denominator is Coale's, not Sen's | **YES** |
| C2 HBV accounts for about 75% (76.40%) of China's missing women | yes | same chain; China prevalence input; vaccination coincides with sex-selection technology | deferred |
| C3 Carrier parents have offspring sex ratio ≈1.5 (1.54, CI 1.29–1.87) | yes | small, old, heterogeneous studies; mother vs father carrier; mechanism unknown | deferred (input to C1) |
| C4 1-pp HBV prevalence raises SRB by ≈.0009–.0014 across countries | yes | ecological; reporting quality; omitted country factors | deferred |
| C5 HBV explains 70.42% vs Sen's benchmark | yes | benchmark choice | deferred |
| C6 Partial effect: 62% for China (18M) | yes | counterfactual county choice | deferred |
| C7 Missing women "may be more heavily focused on India and Pakistan"; bias "less attributable to … tastes and preferences" | no | interpretive escalation from C1 | deferred |

Field 6 selection reason:
- C1 is the most precisely quantified form of the abstract's headline (Rule 2). Every other quantified claim is either an input to it (C3, C4) or a sub-component of it (C2, C5, C6).
- Auditing C1 tests whether the paper overreached, i.e. the source's own claim (#2), not the downstream Slate restatement.

## CLAIM LAYERS AND RIVALS (codes reused verbatim by Stage 2c)

Claim layers:

- **L1 — Individual carrier effect.** Births to HBsAg-carrier parents (especially mothers) have a sex ratio of about 1.5 boys per girl (pooled 1.54, CI 1.29–1.87), vs about 1.05 for noncarriers.
- **L2 — Population transmission.** Across and within populations, higher HBV carrier prevalence raises the population sex ratio at birth by the amount implied by L1 (cross-country .0009–.0014 per prevalence point; Alaska and Taiwan vaccination time series; Chinese counties; immigrant mothers).
- **L3 — Accounting share (Field 6).** Replacing Coale's 1.059 with HBV-predicted SRBs makes HBV account for 47.24% (CI 13.5–71.5) of Coale's 60.26M missing women. By unit: about 76% in China, under 20% in India, Pakistan and Nepal.
- **L4 — Interpretive.** Asia's male-biased sex ratios (especially China's) are therefore less attributable to discrimination or son preference than claimed, and the missing-women problem is concentrated in India and Pakistan.

Strongest rivals:

- **R1 — Son preference / sex-selective behaviour.** Elevated sex ratios at birth arise from parity- and sex-composition-specific behaviour: prenatal sex selection, stopping rules, under-registration or infanticide of girls. This predicts normal first-birth SRB and excess males at higher parities after daughters, independent of HBV.
- **R2 — Null or small individual carrier effect.** In large representative samples, maternal or parental HBV status raises the probability of a male birth negligibly. The 1.5 figure reflects small-sample noise, selection or confounding in the 1975–88 studies.
- **R3 — Ecological confounding.** The cross-country, cross-county and time-series HBV–SRB associations reflect other correlated factors (region or culture, development or mortality, reporting quality, timing of sex-selection technology alongside vaccination) rather than a causal HBV effect.
- **R4 — Benchmark misspecification.** The no-HBV counterfactual SRB for low-life-expectancy populations is below 1.059 (SRB rises with life expectancy). HBV adjustment would then leave the missing-women count close to Coale's original.

## Required output table

| Field | Content | Verification state |
|---|---|---|
| 1. Literally measured | Associations between HBsAg carrier status or prevalence and offspring or population sex ratios (six small family studies; Alaska/Taiwan series; 38-country cross-section; immigrants; Chinese counties), plus a calibrated re-run of Coale's (1991) accounting with HBV-predicted SRB (Tables 10–11) | FULL-TEXT-CONFIRMED |
| 2. Source's strongest claim | "I argue that hepatitis B can account for about 45 percent of the 'missing women': around 75 percent in China" (abstract); body "roughly 47 percent" of Coale's (p.1201); caveats on total vs partial effect (p.1165) and "not conclusive" (p.1181) preserved | FULL-TEXT-CONFIRMED |
| 3. Weaker defensible claim | Conditional on 1.54, on the author's prevalence inputs and on Coale's framework: about 47% (CI 13.5–71.5, sampling only) of Coale's 60.26M is an upper-bound total effect; aggregate associations are consistent with but not decisive for causality | author reconstruction from Field 1 |
| 4. Downstream claim | D1 Slate: "established the fate of roughly 50 million of Amartya Sen's missing women"; D2–D4 citing/critical restatements faithful or critic paraphrase | RETRIEVED (D1–D4); target FULL-TEXT-CONFIRMED |
| 5A. Within-source inflation point + failure location | Abstract: Coale-share stated against a 100M frame, without CI or partial-effect caveat; body "31 million … explained" vs Table 11 remaining 31.79M (explained 28.47M); abstract Egypt/Bangladesh ranges vs table; "new evidence" vs re-pooled old studies → PAPER | FULL-TEXT-CONFIRMED |
| 5B. Downstream inflation point + failure location | Slate: baseline substitution (Coale → Sen) + hedge removal ("established", "had never been born") → PR / MEDIA; version caveat | RETRIEVED (D1); FULL-TEXT-CONFIRMED (target) |
| 6. Claim under audit | HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale's (1991) 60.26 million missing women in seven Asian/North-African units, mid-1980s (Table 11, Panel A). | FULL-TEXT-CONFIRMED |

## Required construct-side handoff sub-schema

| Check | Object | Retrieval status / basis | Result | Verification state | Evidence |
|---|---|---|---|---|---|
| Construct establishment | PREVALENCE | ESTABLISHED-REPORTED | HBV carrier prevalence among pregnant women by country, author-aggregated from PubMed studies (China 11.24%, India 4.33%) | FULL-TEXT-CONFIRMED (in-paper); study list off-paper, not retrieved | Table 10 p.1200; p.1188–89 |
| Construct establishment | FORM | ESTABLISHED-CITED + ESTABLISHED-REPORTED | carrier offspring SR 1.54 (1.29–1.87), source grades evidence "not conclusive" | FULL-TEXT-CONFIRMED (cited studies not retrieved) | Table 3 p.1180; p.1181; p.1199 |
| Construct establishment | DOMAIN | ESTABLISHED-REPORTED | seven units, mid-1980s populations, Coale life tables | FULL-TEXT-CONFIRMED | Table 11 note p.1202 |
| Construct establishment | WRONGNESS | not applicable (no belief graded) | — | — | — |
| Construct establishment | HARM | not applicable (no harm claim) | — | — | — |
| Definition-operationalization | "missing women" ↔ Coale eq. 1 with HBV SRB | ITEMS-RETRIEVED | narrower (Coale 60.26M, seven units, 1980s; not Sen's ~100M; total effect) | FULL-TEXT-CONFIRMED | eq. 1–2 p.1168–69; Table 11 |
| Grade-before-assert | "Coale/Sen counts reflect excess female mortality" (the view the paper partly revises) | source's own analysis + six cited studies | GRADE-CONTESTED | FULL-TEXT-CONFIRMED | P2 strength gate: WEAK — the paper's own grading of its key input is "not conclusive" (p.1181) |

- CLAIM UNDER AUDIT: HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale's (1991) 60.26 million missing women (Table 11, Panel A).
- WITHIN-SOURCE FAILURE LOCATION: paper — FULL-TEXT-CONFIRMED (abstract vs body scope and caveats; one body sentence vs Table 11).
- DOWNSTREAM FAILURE LOCATION: PR-media — RETRIEVED, ANCHOR-ELIGIBLE (Slate 2005); target FULL-TEXT-CONFIRMED; pre-publication version not retrieved.
- GAP TYPE: both.
- MAP CONFIDENCE: moderate. It would be raised by retrieving the March 2005 draft cited by Slate, the author's web-page prevalence study list, and the JPE supplementary dataset (HTTP 403 this run).

Unselected claims C2–C7 are DEFERRED, not dismissed.
