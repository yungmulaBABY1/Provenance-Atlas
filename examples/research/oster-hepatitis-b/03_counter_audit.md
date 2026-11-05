# Stage 3 — Oppositional Citation & Neglected Evidence Counter-Audit

INSTRUMENT PREFLIGHT: prompts/research-analysis/3-counter-audit.txt @ commit a58d165d9a986edca220f8143fc0c0d9316c8a13 | blob/hash 74357f08562a47fa8fdbbde4325657ad3c9cd871 / sha256 291f2339992eeaca83c60281263975d3b5643d64ec6e5d118fa39c44b6c9ede9 | 915 lines | 42287 bytes | markers PRESENT ("OPPOSITIONAL CITATION & NEGLECTED EVIDENCE COUNTER-AUDIT PROMPT (v3)") | IDENTITY CONFIRMED (operator-pinned commit + blob + sha256; retrieval form IMMUTABLE REMOTE at the pinned commit, HTTP 200; independently cross-checked by `git rev-parse` in a separate clone)

Effort: maximum (as briefed). The full pinned prompt (915 lines) was read before writing.
Run date 2026-11-05 (UTC); operator TZ America/Los_Angeles.

## Inputs

0. Claim map: SUPPLIED — `01_claim_extraction.md` (field 6 below; layers L1–L4, rivals R1–R4).
1. Foundational paper: Oster (2005) JPE 113(6):1163–1216, published version, read in full.
   - Source: Belfer Center institutional copy (not committed).
   - The author's 23 Aug 2005 working paper was also read for version comparison.
   - Locators are JPE pages.
2. Citation-network output: SUPPLIED — `citation-network-v2cand3/02c_citation_network_v2cand3.md`.
   - Instrument: v2-candidate.
   - RISK BAND: WITHHELD.
   - Findings: 1–6.
3. Construct-validity output: SUPPLIED — `02b_construct_validity.md` (CV-1…CV-8).
4. Internal-validity output: SUPPLIED — `02a_internal_validity.md` (IV-1…IV-8). It is consumed in E0 and G2 on the same terms as the other prosecutors [FAIL-CA-003].
5. Thesis paragraph / draft: NOT SUPPLIED. The FIDELITY CHECK does not run.
6. Central claim being audited (map field 6): "HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale's (1991) 60.26 million missing women in seven Asian/North-African units, mid-1980s (Table 11, Panel A)."
7. Current audit verdict (the thesis being counter-audited):
   - 2a INVALID, grade E (DEFEATS: IV-2, IV-3).
   - 2b INVALID, residual none (DEFEATS: CV-1, with CV-2 nested).
   - 2c: Finding 1 DEFEATS field 6, failure location PAPER. Network acquitted on closure and uptake (Finding 2). RISK BAND WITHHELD.
8. Known hub / founding cluster:
   - The six 1975–88 carrier-family studies (Blumberg group and others), pooled in Table 3/9. In the network: X01 Drew et al. 1978 (reprint record), A03 1986, A06 Chahnazarian et al. 1988.
   - Most-cited RECEPTION-1 nodes: N08 Das Gupta 2005 (in-degree 23), N31 Lin & Luoh 2008 (18), N01 Qian 2008 (15), N45 Oster et al. 2010 (10).
9. Adjacent fields already suspected (from 2b §10 and 2c): parity-specific sex-ratio demography; the SRB–life-expectancy benchmark literature; large-registry HBV epidemiology.

Evidence-base note:
- Load-bearing sources read in full this run (working-paper versions where the published version is paywalled; VERSION-SUBSTITUTE):
  - Lin & Luoh 2008 WP;
  - Oster, Chen, Yu & Lin NBER w13971 (2008);
  - Klasen 2005 comments;
  - Banyeh et al. 2024 (PMC).
- The Klasen VoxEU column ("Hepatitis B and missing women: the rise and decline of a finding") was re-read this stage via WebFetch (HTTP 200; scripted curl 403 at Stage 1). It is used for reception facts only.
- Items known only from reference lists or reception texts are labelled LOCATED or PROVISIONAL. Nothing load-bearing comes from model memory.

How-found labels used below (DATA-HONESTY RULE):
- cites foundational paper directly — verified via OpenAlex RECEPTION-1 (2c) or the full text read;
- cited by foundational paper — verified in the JPE reference list;
- found through keyword search — 2c ADJUDICATION-1, or the Stage 1/2 web searches;
- unresolved source lead — named only inside another source (VoxEU, Banyeh references, w13971).

Where a citation link was not checked: "Unverified citation relationship."

## A. Oppositional citing papers (ranked, most threatening first)

| Paper | Year | Cites foundational/hub? | Main criticism | Evidence quality | Relationship to claim | Verification state | Field uptake | Strength |
|---|---:|---|---|---:|---|---|---|---|
| A1. Lin, M.-J. & Luoh, M.-C., "Can Hepatitis B Mothers Account for the Number of Missing Women? Evidence from Three Million Newborns in Taiwan", AER 98(5) (N31) — replication / failed replication; cites foundational paper directly (RECEPTION-1 edge; WP text) | 2008 | yes (target) | In ~3M linked Taiwanese births (1.44M in the restricted sample), maternal HBsAg raises P(male) by only +0.10 to +0.25 pp, vs ≈+9.4 pp implied by 1.54. The authors' upper bound is that HBV explains ≈0.9–1.8% of China's missing women | 4 | directly contradicts (L1 maternal → field 6) | FULL-TEXT-CONFIRMED (WP version; AER version not retrieved, VERSION-SUBSTITUTE); RECEPTION-CONFIRMED (in-degree 18/49 in RECEPTION-1; accepted by the target's author in N45 — "this work is quite conclusive for the case of mothers", w13971 abstract; no rebuttal located in the 24 RECEPTION-1 contexts or in VoxEU) | substantively engaged; incorporated into model revision (N45) | potentially decisive |
| A2. Oster, E., Chen, G., Yu, X. & Lin, W., "Hepatitis B does not explain male-biased sex ratios in China", Economics Letters 107(2) (N45) — replication / failed replication (same author); cites foundational paper directly | 2010 (NBER w13971, 2008) | yes (target) | China cohort of ~67,000, with both maternal and paternal HBsAg: no effect (e.g., paternal carriers 51.06% boys vs 51.56%). The authors conclude HBV "cannot explain" China's sex ratios | 4 | directly contradicts (L1 → L3 for China, which is 23.24M of the 28.47M explained) | FULL-TEXT-CONFIRMED (NBER WP version; journal version not retrieved); RECEPTION-CONFIRMED (in-degree 10; cited by R03; VoxEU calls it "a complete retraction"; no rebuttal located) | incorporated into model revision (author's own) | potentially decisive |
| A3. Das Gupta, M., "Explaining Asia's 'Missing Women': A New Look at the Data", PDR 31(3) (N08); response N46 (PDR 32, 2006) — methodological critique + primary data; cites foundational paper directly (published before the JPE issue, against the WP) | 2005 | yes (WP version of target) | Parity- and sex-composition-specific SRB patterns (R1) fit son preference, not a biological carrier effect | 3 | weakens (L4; complicates L3) | LOCATED (full text not retrieved; content from 2a/2b secondary reports and RECEPTION-1 metadata); RECEPTION-CONFIRMED in part: most-cited node (23/49); the target's author replied (Oster 2006, PDR — LOCATED via VoxEU reference list, not read); Das Gupta answered (N46). Standing: CONTESTED at 2006, then overtaken by A1/A2 | substantively engaged (exchange) | strong (capped: reply unread) |
| A4. Klasen, S., "Comments on Paper by Emily Oster: Hepatitis B and the Case of Missing Women" (institutional page) — methodological critique; cites foundational paper directly (the Feb/Mar 2005 draft) | 2005 | yes (draft of target) | Questions the six small studies, genotype transferability and the benchmark (SRB rises with life expectancy, R4). Argues the adjustment roughly cancels | 2 | weakens (R4 narrows L3) | FULL-TEXT-CONFIRMED (comments read); RECEPTION-CONFIRMED in part: the published target answers the benchmark point at p.1203 n.26–27 (see E0); amended as Klasen 2008 (LOCATED via VoxEU). Standing: CONTESTED on R4 | cited and reframed (n.27 defends the 1.059 level) | moderate |
| A5. Banyeh, M. et al., "Maternal hepatitis B status and sex at birth: a cross-sectional study in a Ghanaian population", Heliyon (R03) — primary empirical study; cites foundational paper directly (reference 9) | 2024 | yes (target) | No association between maternal HBsAg and sex at birth (χ² 0.531, P = 0.472) | 1 | weakens (L1; consistent with R2) | FULL-TEXT-CONFIRMED (PMC); RECEPTION: not checked beyond OpenAlex (1 citer); capped "contested / needs verification" | not applicable (recent) | weak |
| A6. Anderson, S. & Ray, D., "Missing Women: Age and Disease", RES (N04, POST HOC known item) — primary empirical study; cites foundational paper per OpenAlex | 2010 | yes (OpenAlex edge; Unverified citation relationship in text) | Locates excess female deaths across ages, not only at birth (complicates the at-birth reading of L4) | 2 | complicates (L4) | LOCATED (metadata only); reception not checked; capped | unclear / needs verification | weak (capped) |

**Self-application note on A5 (symmetry).**
- 2c Finding 1 describes "three large individual-level tests" (N31, N45, R03).
- In R03, HBsAg+ mothers number 40 of 380, with 20 sons and 20 daughters (Table 3, PMC text).
- This sample is far too small to test a ≈0.25-pp effect, and borderline for a 9-pp effect (power not computed). R03 is therefore weak support, not a third decisive test, and it was a POST HOC addition in 2c.
- Finding 1 still stands on A1 and A2. Its wording overstates R03; see G2 (rows 2c-1) and J2.

**Temptation noted (symmetric scoring).** A1 and A2 get 4 because:
- they use linked individual parental status;
- their samples are 2–3 orders of magnitude larger than the six studies;
- they are drawn from the target populations.

A comparably sized support study would also get 4. None was found. Section E1 lists the strongest support at 2, because of its small samples.

## B. Non-citing opposition

| Paper / source | Year | Does not cite hub? | Main argument | Why it matters | Evidence quality | Relationship to claim | Reception (if load-bearing) |
|---|---:|---|---|---|---:|---|---|
| B1. Chahnazarian, A., "Determinants of the sex ratio at birth", PhD dissertation, Princeton — practitioner/academic dissertation; unresolved source lead (quoted in VoxEU) | 1986 | predates target; cites the carrier studies (Unverified citation relationship) | Quoted (VoxEU): carrier-parent birth-order pattern "fails to provide an explanation of the unusually high sex ratios at birth observed at higher parities in China" | Mechanism test against R1 from inside the hub's own research group | 2 | weakens (L1→L3 China) | not load-bearing; PROVISIONAL (quotation only; dissertation not retrieved) |
| B2. ADJUDICATION-1 DIRECT (L1) studies with unread results: A04 (2010 Chinese retrospective study of maternal HBV and infant sex), A07 (2000, offspring of HBsAg mothers), A09 (2007, pregnant women) — primary empirical studies; found through keyword search (2c ADJUDICATION-1) | 2000–2010 | Unverified citation relationship | Direction of results unknown: titles only | These are candidate independent L1 tests outside the economics network | 1 (unscored in substance) | unclear / needs verification | not load-bearing; LOCATED |
| B3. Lin, M.-J., Chen, P.-J. & Luoh, M.-C., "HBeAg(+) and sex ratio of offspring: evidence from Taiwan's three million newborns", Am J Hum Biol 24(4):541–544 — primary empirical study; unresolved source lead (Banyeh reference 8) | 2012 | Unverified citation relationship | Tests HBeAg (replicating-virus status), the pathway the target itself flags (p.1180–81 mechanism; genotype appendix) | Would close the "wrong marker" escape route for A1 | 2 (unread) | unclear / needs verification | not load-bearing; LOCATED |
| B4. Abrevaya (2008), AEJ Applied "Are there missing girls in the United States?"; Ebenstein (2007) mimeo — unresolved source leads (VoxEU) | 2007–08 | Unverified citation relationship | Per VoxEU, they scrutinised other parts of the evidence (e.g., sex ratios among Asian-origin births in the US) | Bear on L2 (immigrant-mother evidence, Table 7) | 1 | complicates (L2) | not load-bearing; LOCATED |

Why outside the network:
- B2 are medical and Chinese-language epidemiology, not indexed into the economics citation stream.
- B1 is an unpublished dissertation.
- B3 is in a biology journal.

None is load-bearing here. The field should have engaged B1, a known Blumberg-group output; the target cites Chahnazarian et al. 1988 but not the dissertation.

## C. Neglected references the hub should have cited

| Neglected source | Year | Relevance | Cited by foundation? | Cited by hub? | Effect of omission | Evidence quality |
|---|---:|---|---|---|---|---:|
| C1. Chahnazarian 1986 dissertation (B1) | 1986 | Birth-order pattern among carrier families, against R1 (PROVISIONAL quotation) | no (Chahnazarian, Blumberg & London 1988 cited instead) | Unverified citation relationship | moderate weakness | 2 |
| C2. Parity-specific SRB demography for China (e.g., Zeng Yi et al. 1993; Das Gupta's sources) | 1990s | Distinguishes R1 from L1: HBV predicts elevation at all parities | partly (Yi et al. 1993 cited for sex-selective abortion, p.1172; parity split not analysed) | n/a | moderate weakness | 2 |
| C3. Klasen & Wink 2003, "Missing Women: Revisiting the Debate" (X10; OUTSIDE corpus) | 2003 | Benchmark update (R4) | no; target cites Klasen & Wink 2002 (p.1203 n.26) | n/a | minor context loss (the 2002 version is used) | 2 |
| C4. James (1996) on parental hormone levels and sex ratio (X09; OUTSIDE corpus) | 1996 | Mechanism for small, natural SRB variation | no (James 1987a/b cited instead; 1996 absent from the JPE reference list) | n/a | minor context loss | 1 |

## D. Ignored adjacent fields (4–6)

| Adjacent field | Key sources | Why relevant | Better method / measure | Decisive test suggested | Engagement by target field | Effect of neglect |
|---|---|---|---|---|---|---|
| D1. Large-registry HBV epidemiology / maternal-child health | Lin & Luoh 2008; Lin, Chen & Luoh 2012 (LOCATED); Oster et al. 2010; Taiwan HBMI registry | L1 is a medical claim | linked parental serostatus × offspring sex in registries | maternal and paternal HBsAg/HBeAg × offspring sex, N ≥ 10⁵, target populations | adopted after 2005 (A1, A2); not before | fatal for strong claim (once run) |
| D2. Parity-specific sex-ratio demography | Das Gupta 2005; Chahnazarian 1986 (PROVISIONAL); Zeng Yi et al. 1993 | R1 makes a distinct parity prediction | SRB by birth order × sex of prior children | first-birth SRB vs prevalence | engaged after publication (PDR exchange) | moderate |
| D3. Mortality-benchmark demography (natural SRB vs life expectancy) | Klasen 1994; Klasen & Wink 2002/2003 | R4 sets the counterfactual | life-table-consistent expected SRB | recompute Coale with an SRB that depends on life expectancy | partly (n.26–27) | moderate (moot once L1 fails) |
| D4. Natural sex-ratio biology | James 1996/2007 (N13, X09) | Plausible size of biological SRB shifts | hormone/parental-condition studies | — | partly: the target cites James 1987a/b reviews (p.1196), not the hormone hypothesis | minor |
| D5. Vaccination natural experiments | target's own Alaska/Taiwan series; Lin & Luoh cohorts | Cohort exposure to HBV falls sharply after vaccination | event studies with parity controls | SRB of births to vaccinated cohorts of mothers, by parity | attempted early (target §IV.C; "still quite early", p.1186) | minor |

## E. Strongest evidence supporting the original claim

### E0. Source self-defense check (run first)

Sections of the target searched:
- abstract;
- introduction and caveats (p.1163–1166);
- §III (China, p.1172–1175);
- §IV.A–B (mechanism, individual studies, p.1176–1181);
- §IV.C (Alaska/Taiwan, p.1182–1187);
- §IV.D (cross-country, p.1188–1197; Tables 6–8);
- §IV.E (calibration and robustness, p.1197–1200);
- §V (Tables 10–12, p.1200–1205; n.25–27);
- conclusion (p.1205–1207);
- Appendix A (genotype/transmission).

Method: full read, plus targeted text search for "not conclusive", "unrealistic", "parity/birth order", "father/paternal", "genotype", "life expectancy", "1.25", "confidence interval" and "Klasen".

| Prosecutor finding | Source passage that anticipates it (quote + location) | Type | Does it answer the finding? | Effect on the finding |
|---|---|---|---|---|
| 2a IV-1: SR_HBV 1.54 rests on six small heterogeneous studies | "while the existing scientific evidence is clearly suggestive of a hepatitis–sex ratio connection, it is not conclusive" (p.1181); data quality "particularly problematic in Greenland and Kar Kar Island" (p.1180); dropping Greece 1 moves 1.54 to 1.52 (p.1198) | acknowledged limitation + sensitivity test | partly | RECHARACTERIZED — new charge: "disclosed and inadequately defended". The paper names the weakness and runs one leave-one-out test, yet still uses 1.54 as the calibration's point estimate and puts no qualifier in the abstract. |
| 2a IV-2: Lin & Luoh large-sample maternal effect ≈0.1–0.25 pp | NONE FOUND (post-dates the source). Nearest: "further confirmation seems necessary" (p.1181) | NONE FOUND | not at all | UNAFFECTED — searched all listed sections; the source cannot pre-empt 2008 data. |
| 2a IV-3: author's successor study finds no China effect | NONE FOUND (post-dates) | NONE FOUND | not at all | UNAFFECTED — searched all listed sections. |
| 2a IV-4: calibration ignores the paper's own lower Taiwan estimate (~1.25) | "the implied sex ratio at birth among HBV carriers is around 1.25 boys for each girl" with individual and cross-country data implying "around 1.5" (p.1186); cross-country implied 1.40–1.60 (p.1199, Table 9B); "still quite early to draw conclusions" (p.1186); CI 1.29–1.87 carried into a share CI of "roughly 13.5–70 percent" (p.1201) | stated assumption + sensitivity (CI) | partly | NARROWED — restated: the paper considered the Taiwan estimate and set it aside because two other estimates converge near 1.5. Its reported share CI (13.5–71.5%) comes from an SR range (1.29–1.87) that excludes 1.25, so the share at 1.25 would lie at or below the bottom of the reported CI. This is inferred from monotonicity and was not recomputed. The charge is "lower own estimate set aside without a share computed at it", not "ignored". |
| 2a IV-5: "31 million … explained" vs Table 11's 31.79M remaining | NONE FOUND; Table 11 itself shows 31.79M as the HBV-adjusted count (p.1202) | NONE FOUND | not at all | UNAFFECTED — searched §V text and Table 11 notes; the slip stands (minor). |
| 2a IV-6: aggregate evidence ecological; vaccination timing coincides with sex selection | n.5: ultrasound "was not widely available in China prior to the 1980s" yet the 1982 cohort ratio is "close to 1.09" (p.1174); controls for GDP, infant mortality, life expectancy and fertility (p.1189); post-1990 China/Korea excluded (Table 6 note) | acknowledged limitation + sensitivity tests | partly | RECHARACTERIZED — new charge: "tested inadequately". Controls and exclusions exist, but there is no within-country parity analysis. Scope unchanged: L2 only. |
| 2a IV-7: original data re-analysis points to a paternal association (provisional) | The paper notes the studies differ in which parent was the carrier; "carrier women are less likely to conceive daughters" is listed as one hypothesis (p.1181); the calibration uses prevalence among pregnant women (Table 10) | NONE FOUND (no maternal-vs-paternal justification) | not at all | UNAFFECTED — searched §IV.B, §IV.E and Table 10 notes. Still PROVISIONAL (Chen et al. 2008 not retrieved). |
| 2a IV-8: Chinese SRB elevated only at higher parities (R1) (provisional) | p.1172: sex-selective abortion "there can be no doubt that there has been some use"; n.5 1982 cohort argument (p.1174); maternal age/birth order dummies in the immigrant regressions (p.1195, Table 7 col. 2) | acknowledged limitation + partial sensitivity test | partly | RECHARACTERIZED — new charge: "rival acknowledged and tested only via maternal-age controls; the parity-specific SRB pattern is not analysed". Still PROVISIONAL (Das Gupta/Oster PDR exchange not read). |
| 2b CV-1: FORM contested; the causal maternal 1.54 fails in large target-population data | "it is not conclusive" (p.1181); "The paper will not endeavor to prove the biological …" (p.1181) | acknowledged limitation | not at all (disclosure does not answer external refutation) | UNAFFECTED for the claim's validity — searched all sections. Hindsight note (G2): the culpability framing ("fatal construct failure") is downgraded. The paper disclosed the premise as unproven; the large tests post-date it. |
| 2b CV-2: level-of-analysis (small studies → national accounting) | as CV-1 | — | — | NESTED in CV-1 (same mechanism; not separately counted). |
| 2b CV-3: total-effect assumption | "what is estimated in this paper is the total effect of hepatitis, not the partial effect" … "This is unrealistic." (p.1165); partial-effect counterfactual, China 62% (p.1203–04) | stated assumption + sensitivity test | fully | DEFEATED — the source states the assumption, calls it unrealistic and quantifies the alternative. The residual problem (the abstract omits the caveat) is carried by 1-5A / CV-7, not here. Cut from later rankings. |
| 2b CV-4: rich-country benchmark despite the SRB–life-expectancy gradient | n.27: the true counterfactual "is 1.059, well above the estimate of around 1.050" (p.1203); n.26: against Klasen & Wink's 93M, HBV "explains about 55 percent" (p.1203); noncarrier base 1.048 (Table 10) | stated assumption + sensitivity test | partly | NARROWED — restated: the paper defends the benchmark's level (1.059 already above Western 1.050) and checks one alternative benchmark (Klasen & Wink: 55%). It does not apply a life-expectancy-dependent SRB to the expected sex ratio. The open charge is about the gradient only, and is unquantified. |
| 2b CV-5: ecological confounding of L2 | as IV-6 (p.1174 n.5; p.1189; Table 6 col. 4 region FE) | acknowledged limitation + sensitivity tests | partly | RECHARACTERIZED — "tested inadequately" (as IV-6; nested with IV-6 in G2). |
| 2b CV-6: prevalence inputs from convenience studies; list off-paper | selection rule ≥2,500 tested; list "available on the author's Web page" (p.1188–89) | stated assumption | partly | RECHARACTERIZED — "disclosed; underlying list not retrievable (HTTP 403)". |
| 2b CV-7: abstract frames the Coale share against "as many as 100 million" | Body: "roughly 47 percent … of Coale's missing women" (p.1201); Panel B vs Sen (Table 11) | scope | partly (the body scopes it; the abstract does not) | UNAFFECTED — the finding is precisely that the abstract lacks the body's scoping; searched the abstract, §I and §V. |
| 2b CV-8: Slate major inflation (PR-media; §9 only) | none possible (downstream) | NONE FOUND | not at all | UNAFFECTED — not a paper-layer finding. |
| 2c Finding 1: decisive tests defeat L1 and so field 6 | "further confirmation seems necessary" (p.1181) | acknowledged limitation | not at all | UNAFFECTED (post-dates); see G2 for the R03 overstatement. |
| 2c Finding 2: critique taken up; no closure (acquittal) | — (not adverse to the source) | NONE FOUND | n/a | UNAFFECTED |
| 2c Finding 3: certainty and mechanism drift in restatements | "it is not conclusive" (p.1181) | acknowledged limitation | — (the source text supports the finding: a downstream "confirmed" contradicts the source's own grading) | UNAFFECTED |
| 2c Finding 4: post-refutation restatement (provisional) | none (post-dates) | NONE FOUND | not at all | UNAFFECTED |
| 2c Finding 5: OpenAlex record quality | none (database layer) | NONE FOUND | not at all | UNAFFECTED |
| 2c Finding 6: small recent reception (provisional acquittal) | none | NONE FOUND | n/a | UNAFFECTED |

E0 RESIDUAL: 22 prosecutor rows. DEFEATED 1 (CV-3); NARROWED 2 (IV-4, CV-4); RECHARACTERIZED 5 (IV-1, IV-6, IV-8, CV-5, CV-6); UNAFFECTED 13 (IV-2, IV-3, IV-5, IV-7, CV-1, CV-7, CV-8, 2c F1–F6); NESTED 1 (CV-2 in CV-1).

Most UNAFFECTED rows are post-publication evidence (IV-2, IV-3, 2c F1, F4) or downstream-layer findings (CV-8, 2c F3–F6). In those cases the source's silence is structural, not a sign that the search was skipped.

Rule-b check:
- The load-bearing DEFEATS (IV-2, IV-3, CV-1) concern an element the source tested only by leave-one-out (Greece 1, p.1198) and by aggregate cross-checks (Table 9B).
- That test is inadequate against the finding: it re-samples the same small literature, and the aggregate estimates share the ecological confounds (IV-6).
- Severity therefore stays.

### E1. External supporting evidence

| Supporting source | Year | What it supports | Answers construct problem? | Runs decisive test? | Strong or narrow claim? | Verification state | Impact on audit |
|---|---:|---|---|---|---|---|---|
| S1. The six carrier-family studies pooled by the target (Drew et al. 1978 [X01 record]; Livadas et al. 1979; Chahnazarian, Blumberg & London 1988 [A06]; others) — primary empirical studies; cited by foundational paper (Table 3) | 1975–88 | L1: carrier families had more sons (355/248 vs 2,083/2,043) | no (small, non-representative, mixed carrier parent) | no | narrow (studied communities) | LOCATED (originals not retrieved); content FULL-TEXT-CONFIRMED only as tabulated by the target (Table 3). Reception: contradicted at scale by A1/A2; re-analysis reported to show a paternal, not maternal, association (w13971 p.3; PROVISIONAL). Standing: weakened | no effect. Evidence quality 2 (small samples). Same bar as A5: a 40-carrier null gets 1; these together give 603 carrier-parent children, so 2 |
| S2. The target's own aggregate evidence (38-country cross-section .0009–.0014; IPUMS immigrant mothers N = 210,556; Alaska; Taiwan; Chinese counties) — primary empirical study | 2005 | L2: positive association between HBV prevalence and SRB | no (ecological) | no | narrow (association) | FULL-TEXT-CONFIRMED. Reception: per VoxEU, other parts of the evidence were "scrutinised" by Abrevaya (2008) and Ebenstein (2007) (LOCATED only). Standing: contested | narrows the critique: the L2 residual survives as an association (2a, 2b both keep it) |
| S3. Lin & Luoh 2008 (A1) read as support — a small positive maternal effect | 2008 | L1 in a weak form: +0.10–0.25 pp, statistically detectable | no | yes (maternal) | supports a weaker version (≈1–2% of China's missing women, authors' upper bound) | FULL-TEXT-CONFIRMED (WP); RECEPTION-CONFIRMED | no effect on the field-6 verdict; it is the same evidence that defeats field 6 |
| S4. James (2007) review (N13) — review; cites foundational paper directly | 2007 | Describes the HBV link as confirmed (CTX-E8, S2 excerpt) | no | no | strong (restates) | FULL-TEXT-CONFIRMED for the excerpt only (2c CTX-E8). Reception: superseded by A1/A2; 2c Finding 3 records this as certainty drift | no effect (a restatement, not evidence) |

Honest summary:
- No large or representative study supporting a carrier effect near 1.5 was found in this run (2c ADJUDICATION-1 and the reception corpus).
- The strongest support (S1, S2) backs only a narrower claim: an association in small carrier families, and a cross-country association. Neither backs the 47% share.

## F. Citation-network uptake of opposition

| Opposition / neglected source | Cited by hub? | Later uptake? | Engagement quality | Survived reception check? | Suppression vs. correctly-discounted | Network implication |
|---|---|---|---|---|---|---|
| A1 Lin & Luoh 2008 | yes: N45 cites and accepts it | high (in-degree 18/49 in RECEPTION-1; co-cited with the target in 21/49 citers) | incorporated into model revision | yes (no rebuttal located; accepted by the target's author) | neither: high uptake | field updated |
| A2 Oster et al. 2010 | n/a (it is the author's own revision) | moderate (in-degree 10; cited by R03) | incorporated into model revision | yes | neither: high uptake | field updated |
| A3 Das Gupta 2005 (+ N46 2006) | target author replied (Oster 2006, LOCATED) | highest in corpus (in-degree 23) | substantively engaged | CONTESTED (reply not read) | neither: high uptake | healthy uptake |
| A4 Klasen 2005 / 2008 | partly answered in the published target (n.26–27) | Klasen 2008 LOCATED; VoxEU column | cited and reframed | CONTESTED on R4 | not assessed (uptake not counted) | partial uptake |
| A5 Banyeh 2024 | n/a | 1 citer | n/a | not checked | n/a (too recent) | unclear / needs verification |
| B1/C1 Chahnazarian 1986 | no (target cites the 1988 article) | resurfaced in VoxEU (2008) | not cited | not checked (PROVISIONAL) | low uptake: (a) suppression and (b) correct discounting both possible; neither verified, because the dissertation was not retrieved, so no suppression claim is made | unclear / needs verification |

Verified conditions:
- (i) Reception survival is verified for A1 and A2 only.
- (ii) Low uptake is observed for C1 only, and C1's reception is unchecked.

No "critique marginalized" claim is made. Later passages that restate the effect after 2010 (2c Finding 4, provisional) show the critique did not reach every citer. That is partial non-uptake at the citer level, not marginalization by the field.

## G. Summary table — opposition strength

| Category | Number Found | Strongest Example | Evidence Quality | Verification state | Impact on Central Claim |
|---|---:|---|---:|---|---|
| Oppositional citing papers | 6 | Lin & Luoh 2008 (A1) | 4 | FULL-TEXT-CONFIRMED (WP); RECEPTION-CONFIRMED | strengthens audit |
| Non-citing opposition papers | 4 entries (≥7 works, none load-bearing) | Chahnazarian 1986 (B1) | 2 | PROVISIONAL | needs verification |
| Neglected references | 4 | Chahnazarian 1986 (C1) | 2 | PROVISIONAL | narrows claim |
| Ignored adjacent fields | 5 | Large-registry HBV epidemiology (D1) | 4 (via A1/A2) | RECEPTION-CONFIRMED (A1/A2) | strengthens audit |
| Strongest support for original claim | 4 | Target's aggregate evidence (S2) | 2 | FULL-TEXT-CONFIRMED; contested | narrows claim (L2 residual only) |

The three most threatening findings in order of severity are:
1. Lin & Luoh 2008: the maternal effect in about 3M Taiwanese births is +0.10–0.25 pp, against the ≈9.4 pp implied by 1.54. FULL-TEXT-CONFIRMED (WP) and RECEPTION-CONFIRMED.
2. Oster, Chen, Yu & Lin 2008/2010: no maternal or paternal effect in a China cohort of about 67,000; the author withdraws the China conclusion (China is about 82% of the explained count). FULL-TEXT-CONFIRMED (WP) and RECEPTION-CONFIRMED.
3. The paper's own grading of its load-bearing input as "not conclusive" (p.1181), together with its lower Taiwan estimate (1.25, p.1186). FULL-TEXT-CONFIRMED in the source.

Capped out of the top three:
- Das Gupta 2005 (CONTESTED; reply unread);
- Chahnazarian 1986 (PROVISIONAL);
- Banyeh 2024 (reception unchecked; small sample).

## G2. Did the prosecution attack the strongest version?

| Prosecutor | Finding | Declared target claim | Claim-map version attacked | Matches field 6? | Failure location | Severity after re-aiming |
|---|---|---|---|---|---|---|
| 2a | IV-1 small-study input | Field 6 | field 6 (input to field 2/3) | yes | PAPER | moderate; recharacterized as disclosed-and-inadequately-defended (E0) |
| 2a | IV-2 Lin & Luoh | Field 6 | field 6 | yes | PAPER (input) | fatal-for-strong-claim (survives) |
| 2a | IV-3 author's successor | Field 6 | field 6 | yes | PAPER (input) | fatal-for-strong-claim for China's 23.24M of 28.47M; nested with IV-2 as one lever, see guard |
| 2a | IV-4 own Taiwan 1.25 set aside | Field 6 | field 6 | yes | PAPER | moderate, narrowed (E0) |
| 2a | IV-5 "31 million … explained" | Field 6 | field 2 body text (number slip) | partly (the 47.24% itself is correct) | PAPER | minor |
| 2a | IV-6 ecological L2 | Field 6 (via L2) | L2, not an input to field 6 | no (L2 only) | PAPER | moderate for L2; incidental for field 6 |
| 2a | IV-7 paternal not maternal | Field 6 | field 6 (multiplier choice) | yes | PAPER | moderate; PROVISIONAL (capped) |
| 2a | IV-8 parity pattern (R1) | Field 6 | L4 / R1 more than field 6 | partly | PAPER | moderate; PROVISIONAL (capped) |
| 2b | CV-1 FORM contested | Field 6 | field 6 | yes | PAPER (input) | fatal for claim validity; culpability framing downgraded as hindsight (see Q5) |
| 2b | CV-2 level-of-analysis | (nested in CV-1) | field 6 | yes | PAPER | nested, one lever |
| 2b | CV-3 total effect | Field 6 | field 6 | yes | — | DEFEATED in E0 (removed) |
| 2b | CV-4 benchmark | Field 6 | field 6 | yes | PAPER | moderate, narrowed to the gradient point; moot once L1 fails |
| 2b | CV-5 ecological | Field 6 | L2 | no (L2 only) | PAPER | incidental for field 6 (nested with IV-6) |
| 2b | CV-6 prevalence inputs | Field 6 | field 6 (input) | yes | PAPER | minor |
| 2b | CV-7 abstract scope | Field 6 | field 2 (abstract) | no — attacks the abstract framing, which field 6 already scopes out | PAPER (abstract) | minor |
| 2b | CV-8 Slate inflation | none (Section 9) | field 4 (downstream) | no | PR / MEDIA | minor at paper layer; major at media layer |
| 2c | F1 decisive tests defeat L1 | Field 6 | field 6 | yes | PAPER | fatal-for-strong-claim; survives on N31 + N45. Its wording "three large individual-level tests" overstates R03 (n = 380, 40 carriers): restate as two large tests plus one small consistent study |
| 2c | F2 acquittal on closure/uptake | Field 6 network support | network | yes (as acquittal) | CITATION (no failure) | none |
| 2c | F3 certainty/mechanism drift | MAP GAP (restatements) | field 4 | no — MAP GAP | CITATION | minor |
| 2c | F4 post-refutation restatement | MAP GAP | field 4 | no — MAP GAP | CITATION | minor; PROVISIONAL |
| 2c | F5 record quality | MAP GAP | none (database) | no — MAP GAP | MODEL / RETRIEVAL | moderate at retrieval layer; none at paper layer |
| 2c | F6 recent reception | Field 6 network support | network | yes (as provisional acquittal) | CITATION (no failure) | none |

DOUBLE-COUNT GUARD [FAIL-MB-003]. Consolidated as ONE lever (one mechanism: the 1.54 input fails at scale in the target populations):
- IV-2, IV-3, CV-1, CV-2 and 2c F1.
- These rows have one contribution to severity and one place in the top-three ranking. A1 and A2 are cited separately in the top three because they are distinct evidence (maternal Taiwan; maternal and paternal China), but they bear on the same lever.

Other nests:
- IV-6 with CV-5 (ecological L2), as one lever.
- IV-1 with IV-4: both concern the evidential basis of 1.54 in the source, a second, weaker lever.
- Independent levers retained: CV-4 (benchmark); IV-5 (number slip); CV-7 (abstract scope); IV-7 and IV-8 (provisional).

1. Versions attacked:
   - 2a and 2b mostly attacked field 6 itself, which is also the weaker defensible claim (field 3), since field 6 already carries the CI and Coale scope.
   - CV-7 and IV-5 attack field 2 (abstract/body text).
   - CV-8 attacks field 4.
   - 2c F3–F5 attack versions off the map (MAP GAP: downstream restatements, the database record).
2. Was that the version to evaluate? Yes for the load-bearing lever. CV-7, IV-5, CV-8 and 2c F3–F5 are sound but do not support the field-6 conclusion, and are not counted toward it.
3. Where does each failure live?
   - PAPER: the load-bearing lever, IV-1/IV-4, CV-4, CV-6, IV-5 and CV-7.
   - CITATION: 2c F3 and F4 (minor).
   - PR / MEDIA: CV-8 (Slate).
   - MODEL / RETRIEVAL: 2c F5.
   - Overall: MIXED, with the field-6 failure at the PAPER layer.
4. "The source is defensible on this point; the failure is at the citation layer." This applies to 2c F3 and F4, where the source's own text ("not conclusive", p.1181) is more cautious than its restatements. "The source is defensible on this point; the failure is at the PR layer." This applies to CV-8.
5. Severity after re-aiming:
   - The load-bearing lever keeps its fatal-for-strong-claim severity against field 6.
   - Hindsight downgrade: CV-1's framing as a construct-validity failure of the 2005 paper, and the 2b §16 checkbox "Missing decisive test (at the time)", use 2008/2010 evidence. As a judgment of field 6's truth this is valid. As a judgment of the 2005 paper's method it is hindsight-driven, because the paper disclosed the premise as "not conclusive" (p.1181) and the decisive registry tests did not yet exist in the literature.
   - The paper-layer charge is therefore "load-bearing reliance on a disclosed, weak premise" (moderate), not "fatal construct failure".
   - CV-3 is removed (E0 DEFEATED). CV-7, IV-5 and CV-8 are minor at the paper layer.

MAP DISAGREEMENT: none. The claim map located within-source inflation at the PAPER (5A) and downstream inflation at PR / MEDIA (5B); the prosecution's findings agree. The map did not anticipate the MODEL / RETRIEVAL finding (2c F5), which is recorded as a MAP GAP, not a disagreement.

| Question | Answer | Supporting prosecutor findings |
|---|---|---|
| Versions attacked | field 6 (= field 3 scope) for the load-bearing lever; field 2 (abstract/body); field 4 (Slate); MAP GAP (restatements, database record) | IV-1–IV-4, IV-7, CV-1, CV-4, CV-6, 2c F1; IV-5, CV-7; CV-8; 2c F3–F5 |
| Version audit targeted (map field 6) | 47.24% (CI 13.5–71.5%) of Coale's 60.26M, Table 11A | — |
| Finding-level match rate | 13/22 yes (IV-1, IV-2, IV-3, IV-4, IV-7, CV-1, CV-2, CV-3, CV-4, CV-6, 2c F1, F2, F6); 2/22 partly (IV-5, IV-8); 4/22 no (IV-6, CV-5 aimed at L2; CV-7 at field 2; CV-8 at field 4); 3/22 MAP GAP (2c F3–F5) | as listed |
| Failure location(s) | MIXED: PAPER for field 6; CITATION minor; PR / MEDIA (Slate); MODEL / RETRIEVAL (record) | lever; F3/F4; CV-8; F5 |
| Severity survives re-aiming? | yes for the load-bearing lever (claim validity); paper-culpability downgraded to moderate (hindsight); CV-3 cut | IV-2, IV-3, CV-1, 2c F1 |
| Nested findings consolidated | {IV-2, IV-3, CV-1, CV-2, 2c F1}; {IV-6, CV-5}; {IV-1, IV-4} | — |

## H. Revised thesis impact

Category: **F — Mixed**:
- The thesis is strengthened on the load-bearing lever. Large-sample tests that passed the reception gate (A1, A2) defeat field 6, and the author accepted them.
- The thesis is narrowed elsewhere:
  - CV-3 is cut (E0);
  - CV-4 and IV-4 are narrowed;
  - the paper-layer charge is downgraded from "fatal construct failure" to "load-bearing reliance on a disclosed, weak premise" (hindsight);
  - 2c Finding 1's "three large tests" is restated (R03 is small).

Not B: the strengthening on the central lever is real.
Not D or E: no evidence reverses the audit's central claim.

1. Which claims should be removed?
   - CV-3 as a finding against the paper (the source states and quantifies it).
   - Any description of R03 (Banyeh 2024) as a "large" or decisive test.
2. Which claims should be narrowed?
   - CV-4 → "life-expectancy gradient not applied; level defended in n.27; one alternative benchmark (Klasen & Wink) gives 55%".
   - IV-4 → "own lower estimate set aside; the share at 1.25 would sit at or below the reported CI floor (not recomputed)".
   - IV-1 → disclosed and inadequately defended.
   - CV-1 paper-culpability → reliance on a disclosed weak premise (claim-validity verdict unchanged).
3. Which claims should be strengthened? The field-6 INVALID verdict: two independent, reception-checked large tests, plus the author's explicit acceptance (N45; VoxEU calls it "a complete retraction").
4. Which claims require better sourcing?
   - IV-7 (Chen, Oster, Yu & Lin 2008 re-analysis);
   - IV-8 / A3 (Das Gupta 2005; Oster 2006 reply);
   - B1 / C1 (Chahnazarian 1986);
   - B2 / B3 (A04, A07, A09; Lin, Chen & Luoh 2012);
   - the published versions of A1 and A2 (only WPs read);
   - the JPE dataset (replication not assessable).
5. Which claims survived unchanged?
   - IV-2, IV-3, CV-1 as to claim validity, and 2c F1's DEFEATS result;
   - IV-5 (number slip);
   - CV-7 (abstract scope);
   - CV-8 (Slate inflation);
   - 2c F2 (no closure) and F5 (record quality).
6. Which evidence most improves the thesis? Lin & Luoh 2008 (A1), which is RECEPTION-CONFIRMED.
7. Which evidence most threatens the thesis? Within the reception-checked set, the target's own aggregate associations (S2), contested. They keep an L2 residual alive but cannot restore the 1.54 input. Nothing reception-checked threatens the field-6 verdict.

## I. Revised thesis paragraph

What Oster (2005) measured:
- associations between HBsAg carrier status and offspring sex in six small 1975–88 family studies (pooled SR 1.54, CI 1.29–1.87);
- associations between HBV prevalence and population sex ratios at birth (cross-country, immigrant, Alaska, Taiwan, Chinese counties).

What it claimed: substituting the pooled ratio into Coale's (1991) accounting makes HBV account for 47.24% (CI 13.5–71.5%) of Coale's 60.26M missing women.

The proxy gap is the step from a pooled association in unrepresentative communities to a causal per-mother multiplier for national populations. The paper disclosed this step as "not conclusive", but still used it as the calibration's point estimate.

Opposing evidence:
- Two large individual-level tests in the target region, both of which passed reception checks, reject that multiplier:
  - Lin & Luoh (2008; about 3M Taiwanese births): +0.10–0.25 pp, maternal;
  - Oster, Chen, Yu & Lin (2008/2010; about 67,000 people in China): no maternal or paternal effect, and the author withdraws the China conclusion.
- On these tests the share is near zero, about 1–2% for China on Lin & Luoh's upper bound.

What survives:
- a narrower ecological association between HBV prevalence and the sex ratio at birth (contested);
- the paper's own scoped caveats (total effect, Coale benchmark).

The decisive test is parental HBsAg/HBeAg by offspring sex, by birth order, in large registries of high-prevalence populations. It has been run for Taiwan (maternal) and China (both parents). It has not been run for South Asia or for paternal status outside China.

The citation network took up the critiques: they are its most-cited nodes, and the author updated. A few later citers restate the effect without the refutation (provisional). That is incomplete uptake, not suppression.

Where the failure sits:
- The field-6 failure is at the PAPER layer, as reliance on a weak premise the paper disclosed. Judged in 2005 terms it was not concealment.
- The "missing women solved" framing originates at the PR/media layer (Slate 2005).

## J. Final adversarial verdict

- Strongest opposition to the foundational claim:
  - Lin & Luoh 2008 (AER; WP read). RECEPTION-CONFIRMED: in-degree 18 in RECEPTION-1, accepted by the target's author in w13971, no rebuttal located.
  - Assessed by full-text read of the WP plus 2c reception edges and S2 contexts.
- Strongest support for the foundational claim:
  - The target's own aggregate associations (cross-country .0009–.0014 per prevalence point). Contested; supports L2 only.
  - Assessed by full-text read and VoxEU reception facts (Abrevaya and Ebenstein LOCATED only).
- Strongest neglected adjacent-field evidence: large-registry HBV epidemiology (D1), which the field later adopted (A1, A2).
- Strongest paper the hub should have cited: Chahnazarian 1986 dissertation (PROVISIONAL; quoted in VoxEU only).
- Most important non-citing opposition: none load-bearing. The best lead is Chahnazarian 1986 (PROVISIONAL); the B2/B3 epidemiology is LOCATED, results unread.
- Did the field engage the opposition? Yes. It was engaged substantively and incorporated into the model's revision by the author (N45). The critiques are the most-cited RECEPTION-1 nodes.
- Marginalization / suppression: none claimed. The only low-uptake source (C1) was not reception-checked.
- Did the opposition change the thesis? Yes, partially (category F). The central verdict is strengthened; four findings are narrowed, cut or downgraded.
- Source self-defense (E0):
  - DEFEATED: CV-3 (p.1165 "This is unrealistic."; partial effect p.1203–04).
  - NARROWED: IV-4 (p.1186; Table 9B; CI p.1201) and CV-4 (p.1203 n.26–27).
  - RECHARACTERIZED: IV-1 (p.1180–81, p.1198); IV-6 and CV-5 (p.1174 n.5, p.1189, Table 6); IV-8 (p.1172, p.1195); CV-6 (p.1188–89).
  - UNAFFECTED: IV-2, IV-3, IV-5, IV-7, CV-1, CV-7, CV-8, 2c F1–F6.
  - NESTED: CV-2.
- Version the prosecution attacked:
  - load-bearing findings: the strongest-claim figure as scoped in field 6, which coincides with the defensible version (field 3);
  - minor findings: the abstract (field 2) and the downstream claim (field 4).
- Failure location: MIXED. PAPER for field 6; PR/MEDIA for the Slate inflation; CITATION minor; MODEL/RETRIEVAL for the database record.
- Does the severity survive re-aiming to the audited claim?
  - Yes for claim validity (fatal-for-strong-claim).
  - The paper-culpability charge is downgraded to moderate (hindsight).
- Finding-target alignment (G2): 13/22 yes, 2 partly, 4 aimed elsewhere, 3 MAP GAP.
- Internal-validity coverage: SUPPLIED AND CONSUMED (02a: IV-1–IV-8 run through E0 and G2).
- Double-count resolution:
  - {IV-2, IV-3, CV-1, CV-2, 2c F1} form one lever;
  - {IV-6, CV-5} form one lever;
  - {IV-1, IV-4} form one lever;
  - CV-4, IV-5, CV-7, IV-7 and IV-8 are retained as independent.
- Revised thesis impact category: F (Mixed).
- Claims to remove: CV-3 as a paper finding; "three large tests" (R03 is small).
- Claims to narrow: IV-1, IV-4, CV-4, and the CV-1 culpability framing.
- Claims strengthened: field 6 INVALID (A1 + A2 reception-confirmed; author acceptance).
- Three most threatening findings ranked by severity:
  1. A1 Lin & Luoh (RECEPTION-CONFIRMED);
  2. A2 Oster et al. (RECEPTION-CONFIRMED);
  3. the source's own "not conclusive" grading plus its lower Taiwan estimate (FULL-TEXT-CONFIRMED in source).
- Main remaining source-risk:
  - A1 and A2 were read only as working papers (VERSION-SUBSTITUTE).
  - The JPE dataset was not retrieved.
  - The Das Gupta–Oster exchange was not read.
- Confidence level: High for field 6 INVALID; Moderate for the narrowed paper-layer characterizations.
- What evidence would change this assessment: a large, representative study in a high-prevalence population finding carrier offspring sex ratios near 1.5 (maternal or paternal), or evidence that the Taiwan/China tests misclassify carrier status or offspring sex.

## FIDELITY CHECK

N/A: Input 5 (thesis paragraph / draft) was NOT SUPPLIED.

## J2. Self-tilt disclosure

- Direction of lean: slightly toward the critique.
  - The central verdict was pre-registered (00a) and the run confirmed it.
  - E0 cut only one finding, and the hindsight downgrade changes characterization, not the verdict.
- Least reception-checked findings of this stage:
  - the Chahnazarian 1986 quotation (VoxEU only);
  - B2/B3 (titles only);
  - A6 (metadata);
  - Banyeh's reception.
  - None is load-bearing.
- Sources this stage introduced and promoted:
  - the VoxEU column, used for reception facts. It is a critic's account, and its line on Lin & Luoh ("no link") overstates their small positive maternal estimate. It was not used for effect sizes.
  - Banyeh 2024, which was demoted rather than promoted.
  - Gating: the opposition sources were gated at least as hard as the support sources (S1 got 2; A5 got 1).
- Order: the source was searched before the literature, across all sections listed in E0. E0 was not all-UNAFFECTED (1 DEFEATED, 2 NARROWED, 5 RECHARACTERIZED).
- Did I let the prosecution's target stand unexamined because I expected the conclusion? Risk acknowledged. Re-aiming weakened the paper-culpability charge (hindsight) and 2c F1's "three large tests". Reluctance to weaken the central verdict was checked: no reception-checked evidence supports reversing it.
- A counter-audit of this counter-audit would likely flag first that A1 and A2 were read as working papers, not as the published AER and Economics Letters versions, and that Lin & Luoh's later HBeAg paper (B3) was not read.
- The single assumption most likely to be wrong: that the Taiwan and China nulls transfer to South Asia, the Middle East and Egypt. They are about 18% of the explained count in Table 11A, and no large test there was found. This is immaterial to field 6's INVALID verdict, but material to any "zero everywhere" restatement.

## K. Final one-paragraph summary

The strongest counter-evidence to Oster (2005) comes from two large individual-level tests, and both survived reception checks:
- Lin & Luoh 2008 (Taiwan, about 3M births): maternal carrier effect +0.10–0.25 pp.
- Oster, Chen, Yu & Lin 2008/2010 (China, about 67,000 people): no maternal or paternal effect; the author withdraws the China conclusion.

Together they defeat the 1.54 input, and with it the claim that HBV accounts for 47.24% of Coale's 60.26M missing women. This strengthens the original audit's central verdict (INVALID).

The counter-audit also narrows the audit:
- The paper stated and quantified the total-effect assumption (finding cut).
- It defended its benchmark level (narrowed to the life-expectancy gradient).
- It flagged its key input as "not conclusive", so the paper-layer charge is reliance on a disclosed weak premise, not a hidden construct failure.
- Banyeh 2024 is a small study, not a third large test.

The field engaged the opposition. The critiques are the most-cited nodes and the author updated. A few later citers restate the effect without the refutation, which is incomplete uptake, not suppression.

The most defensible revised position: field 6 is invalid. An ecological association between HBV prevalence and the sex ratio at birth survives as contested L2 evidence. The paper's inflation lives in the abstract (scope and caveats), and the "mystery solved" framing at the media layer.
