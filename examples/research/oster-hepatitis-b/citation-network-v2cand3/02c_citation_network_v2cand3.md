# Citation-Network Audit, v2-candidate.3 run — Oster (2005), "Hepatitis B and the Case of the Missing Women"

INSTRUMENT PREFLIGHT: yungmulaBABY1/Provenance @ a58d165d9a986edca220f8143fc0c0d9316c8a13 : candidates/research-analysis/2-citation-network.v2-candidate.txt | git blob fcbf4e80cfbaf1558784d052d3b8933b594310c7 | sha256 efc1a9fc336c30a67645ac9257701aa2ebe07dcc0be59f8e28523b0800d53064 | 2001 lines | 89337 bytes | markers: version line "2-citation-network v2-candidate.3", map "cn7-map-3" | IDENTITY CONFIRMED (gate checker blob b75a27e7…, sha256 ce6661a5…; v1 checker blob a3da0827…, sha256 f66650fe…)

INSTRUMENT VERSION: 2-citation-network v2-candidate.3

DIMENSION CLASS MAP: cn7-map-3

Run metadata. LIVE RUN of citation-network candidate revision 3 (not a validation run), Batch 1 of the four-paper brief. Executor: Grok Bot (audit run), branch audit/oster-hepatitis-b from Provenance-Atlas main 6c651d7593abfb5c4b6d2eb9f6846a5212fe001c. Execution date 2026-11-05 UTC (early morning PST). Clock times are UTC with PST (UTC-8) where useful. Mode: full sequence; upstream claim map ../01_claim_extraction.md (this run). Tools: OpenAlex works API with select= lists omitting abstract_inverted_index (corpora, graph, co-citation counts); Semantic Scholar citation contexts as EXCERPT access; authorized full texts (JPE article copy for the target; NBER WP w13971; Lin & Luoh author working paper; Europe PMC PMC11137505; Slate; Klasen comments on the Göttingen site). Recent window: from 2021-11-05. No abstract was read, coded from, or written to any file.

VALIDATION BOUNDARY. This instrument revision is a candidate. It has not been validated for open retrieval. This run used open retrieval over three registered corpora (49 + 6 + 46 works). Every percentage, band and label below is an unvalidated open-retrieval application, not a validated verdict.

EXPOSURE DISCLOSURE. Before this stage the executor had read the target (JPE 2005, full text) for Stages 1, 2a and 2b, and knew from prior reading (declared in 00a) that Lin & Luoh (2008, AER) and Oster, Chen, Yu & Lin (2010, Economics Letters) report null carrier effects and that Das Gupta (2005, 2006) disputed the HBV account. The 00a known-item list was written before the ADJUDICATION-1 search. The Section E lock is post-exposure (bibliography read in Stage 1) and is mechanical for that reason: sources are fixed by a ranked query, not chosen.

PRE-AUDIT CLAIM CONFIRMATION

- Claim under audit (map field 6): HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale's (1991) 60.26 million missing women in seven Asian/North-African units, mid-1980s (Table 11, Panel A).
- What was literally measured (map field 1): associations between HBsAg carrier status or prevalence and offspring or population sex ratios (six small family studies; Alaska/Taiwan series; 38-country cross-section; immigrants; Chinese counties), plus a calibrated re-run of Coale's accounting with HBV-predicted sex ratios (Tables 10–11).
- Weaker defensible claim (map field 3): conditional on a carrier offspring sex ratio of 1.54, the author's prevalence inputs and Coale's framework, about 47% (CI 13.5–71.5, sampling only) is an upper-bound total effect; aggregate associations are consistent with but not decisive for causality.
- Target layer: field 6 (layer L3 below) for the network verdict; layers L1–L4 and rivals R1–R4 are defined below.

The map is upstream-generated, not self-generated.

SECTION A0: CORPUS REGISTER AND SOURCE ELIGIBILITY

Corpus planning. Questions: (a) how Oster (2005) is received (RECEPTION-1, RECENT-1); (b) what the evidence base testing the layers and rivals contains (ADJUDICATION-1). Proposed inferences were tested in SECTION K0 before use; those that fail stay there as INSUFFICIENT or NOT-ASSESSED.

CLAIM LAYERS AND RIVALS

CLAIM LAYER: L1 — Individual carrier effect: offspring sex ratio of HBV carriers about 1.5 (1.54, CI 1.29–1.87).
CLAIM LAYER: L2 — Population transmission: HBV prevalence raises the population sex ratio at birth.
CLAIM LAYER: L3 — Accounting share (map field 6): HBV accounts for 47.24% of Coale's 60.26M missing women.
CLAIM LAYER: L4 — Interpretive: the imbalance is less attributable to discrimination; the remaining problem is concentrated in India and Pakistan.
RIVAL: R1 — Son preference and sex-selective behaviour (parity-specific).
RIVAL: R2 — Null or small individual carrier effect in large samples.
RIVAL: R3 — Ecological confounding of the HBV–sex-ratio association.
RIVAL: R4 — Benchmark misspecification (expected sex ratio varies with life expectancy or mortality).

CORPUS REGISTER

CORPUS ID: RECEPTION-1
CORPUS ROLE: RECEPTION
CORPUS QUESTION: How the most-cited works citing Oster (2005) relate to it and to each other.
CORPUS SELECTION RULE: OpenAlex works API, /works?filter=referenced_works:W3123222584&sort=cited_by_count:desc&per_page=50, page 1, executed 2026-11-05T10:25:08Z (2:25 AM PST); population 172; no date or type bounds; no screening; one row per work (W2125485011 and W1581958734 are one work, row N09); response raw/reception1_top50.json sha256 2529864d8e37346ee333a78ce835bf45ddfc78a8464ed656b8cde1dff54dc980.
CORPUS DISCOVERY: SEARCHED — ranked citation query (top 50 by cited_by_count); request, execution time and response hash recorded above
SELECTED ON TARGET CITATION: YES
CORPUS SIZE: 49
CITATION CONTEXT COVERAGE: RECEPTION-1 24/49
RECORD QUALITY: target record W3123222584 lists 318 referenced works (implausibly many) and has a RePEc preprint duplicate W3126094291; one work appears as two records (N09 W2125485011, N35 W1581958734; merged); two members are implausible citers (N19 income inequality and CO2; N44 prenatal smoking); OpenAlex reference lists are incomplete for some members.
CORPUS LOCK: 2026-11-05T10:25:08Z; response sha256 2529864d8e37346ee333a78ce835bf45ddfc78a8464ed656b8cde1dff54dc980

CORPUS ID: RECENT-1
CORPUS ROLE: RECEPTION
CORPUS QUESTION: How recent (2021-11-05 onward) citing works use Oster (2005).
CORPUS SELECTION RULE: OpenAlex works API, /works?filter=from_publication_date:2021-11-05,referenced_works:W3123222584&sort=cited_by_count:desc&per_page=25, executed 2026-11-05T10:25:12Z; population 6, so the top-25 rule returns a census; all 6 were to be inspected (lock/SAMPLES_draw.txt). Response raw/recent1_top25.json sha256 899ac2a524ef89b323e886bdc5fdb09908db38f01e03cbd2dc2975835126c46b.
CORPUS DISCOVERY: SEARCHED — ranked citation query; request, execution time and response hash recorded above
SELECTED ON TARGET CITATION: YES
CORPUS SIZE: 6
CITATION CONTEXT COVERAGE: RECENT-1 2/6
RECORD QUALITY: a population of 6 recent citers is implausibly small for a JPE paper with 172 OpenAlex citers (incomplete citation links); R01 (= N19) is an implausible citer; three of six are dissertations or low-visibility items.
CORPUS LOCK: 2026-11-05T10:25:12Z; response sha256 899ac2a524ef89b323e886bdc5fdb09908db38f01e03cbd2dc2975835126c46b

CORPUS ID: ADJUDICATION-1
CORPUS ROLE: ADJUDICATION
CORPUS QUESTION: What tests of claim layers L1–L4 and rivals R1–R4 exist, whether or not they cite the target, and what they find.
CORPUS SELECTION RULE: OpenAlex works API, five title_and_abstract.search queries Q1–Q5 (exact strings, date bounds 1980-01-01 to 2026-11-05 and types article|preprint|book-chapter in lock/ADJUDICATION-1_search_record.md), relevance ranking, top 10 per query, select= without abstract_inverted_index; one row per work; screening from title and record metadata only (abstracts not used), codes DIRECT (L1)/(R2)/(L2)/(R3)/(L3)/(L4)/(R1)/(R4), ADJACENT, BACKGROUND, UNRELATED, UNKNOWN.
CORPUS DISCOVERY: SEARCHED — lock/ADJUDICATION-1_search_record.md (raw/adj1_Q1..Q5.json, executed 2026-11-05T10:26:08Z)
SELECTED ON TARGET CITATION: NO
CORPUS SIZE: 46
CITATION CONTEXT COVERAGE: ADJUDICATION-1 2/46
RECORD QUALITY: target returned as two records (W3123222584, W3126094291; row T01); Drew et al. 1978 returned as the Science record and a 2000 reprint (row X01); the Kim baby-bonus work as two records (one row); several Q5 records have empty reference lists; titles only were used for screening, so relevance codes are METADATA-coded.
CORPUS LOCK: 2026-11-05T10:24:54Z (2:24:54 AM PST); search record sha256 aeead2c9ebc5cdbb6004693fb7109093654184fd3412ad2792e11c576baa97f8
KNOWN-ITEM RECALL: ADJUDICATION-1 3/8 (returned: K1 Das Gupta 2005 PDR [N08], K2 Lin & Luoh 2008 AER [N31], K8 Chahnazarian 1988 [A06]; not returned: K3 Oster, Chen, Yu & Lin 2010 Economics Letters, K4 Oster reply to Das Gupta, K5 Das Gupta 2006 PDR, K6 Klasen 2008, K7 Anderson & Ray 2010 REStud). K3, K5 and K7 are RECEPTION-1 members (N45, N46, N04) and enter adjudication only as POST HOC; K4 and K6 were not retrieved.

Overlap. N08, N25, N31 and N32 are in RECEPTION-1 and ADJUDICATION-1 and are recorded once with both corpus IDs; N19 is in RECEPTION-1 and RECENT-1 (also listed as R01). Reception rank does not weight the adjudication role. Duplicate records of one work are merged into one row with every identifier listed: N09 (+N35 record), T01 (+preprint record), X01 (+reprint record), and the Kim baby-bonus row. Rows X02–X12 are OUTSIDE every registered corpus (Section E locked sources and two named sources); they carry no corpus count.

SOURCE ELIGIBILITY LEDGER

| Source | Corpus membership | Question relevance | Relation to target | Evidence contribution | Source access | Citation context | Supported inference |
|---|---|---|---|---|---|---|---|
| N01 W2114978546 Missing Women and the Price of Tea in China: The… (2008) | RECEPTION-1 | ADJACENT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; sex-specific earnings and sex imbalance (QJE); citation present in OpenAlex refs, use not inspected |
| N02 W4234238734 The "Missing Girls" of China and the Unintended… (2010) | RECEPTION-1 | DIRECT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; one-child policy and missing girls; citation present in OpenAlex refs, use not inspected |
| N03 W2121199232 Child Gender and Parental Investments In India:… (2013) | RECEPTION-1 | BACKGROUND | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E1: lists Oster 2005 as "greater incidence of female-biased diseases" (mechanism misdescribed) |
| N04 W2026772829 Missing Women: Age and Disease (2010) | RECEPTION-1 | ADJACENT (L3) | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E2: "a recent debate on the effect of Hepatitis B on sex ratios" (cites Lin & Luoh, Oster et al.); K7; POST HOC adjudication member (known item K7, not returned by the ADJUDICATION-1 search) |
| N05 W2782446622 THE MEANING OF FAILED REPLICATIONS: A REVIEW AND… (2015) | RECEPTION-1 | ADJACENT | QUALIFIES | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E3: Oster 2005 used as an example of critiques and replication (Das Gupta 2006; Lin & Luoh 2008; Oster et al. 2010) |
| N06 W3123575441 Chapter 58 Extended Family and Kinship Networks:… (2007) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; handbook chapter on kinship networks; citation present in OpenAlex refs, use not inspected |
| N07 W2057390815 Estimating the Effect of the One-Child Policy on… (2011) | RECEPTION-1 | DIRECT (R1) | QUALIFIES | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E4: "raised the possibility" HBV accounts for "about 70%" of China's missing women; "Das Gupta (2005) questioned" |
| N08 W1982754848 Explaining Asia's “Missing Women”: A New Look at… (2005) | RECEPTION-1+ADJUDICATION-1 | DIRECT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; birth-order evidence on missing women (K1); full text not retrieved; citation present in OpenAlex refs, use not inspected |
| N09 W2125485011 + W1581958734 (N35 record) Financial Incentives and Fertility (2013) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; fertility incentives; one work under two records (N09 REStat 2013, N35 NBER WP 2007); citation present in OpenAlex refs, use not inspected |
| N10 W2123699796 The Competitive Saving Motive: Evidence from Ris… (2009) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; sex ratios and savings (uses sex ratios for another question); citation present in OpenAlex refs, use not inspected |
| N11 W3122231766 Are There Missing Girls in the United States? Ev… (2009) | RECEPTION-1 | ADJACENT (R1) | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E5, CTX-E6: HBV "can partly explain" high boy-birth shares; "around 75%" China vs "around 17%" India |
| N12 W2096320699 Does increased access increase equality? Gender… (2008) | RECEPTION-1 | ADJACENT | SUPPORTS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E7: author self-citation, HBV "responsible for around 20% of the (historical) gender imbalance in India" |
| N13 W2030091805 Evidence that mammalian sex ratios at birth are… (2007) | RECEPTION-1 | ADJACENT (L1) | SUPPORTS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E8: Chahnazarian et al. summarised the work "and the result confirmed by Oster (2005)" |
| N14 W1982250044 Estimating a Dynamic Model of Sex Selection in C… (2011) | RECEPTION-1 | DIRECT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; dynamic model of sex selection in China; citation present in OpenAlex refs, use not inspected |
| N15 W1593586622 Where Have All the Young Girls Gone? Identificat… (2010) | RECEPTION-1 | DIRECT (R1) | QUALIFIES | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E9: HBV level hypothesis cited "although see Oster forthcoming"; trends rule out level explanations |
| N16 W1969182143 Son targeting fertility behavior: Some consequen… (2010) | RECEPTION-1 | ADJACENT (R1) | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E10: rising SRB attributed to "biological factors, as Oster (…)" or to behaviour (passage truncated by S2) |
| N17 W3124330411 Chapter 52 Population Policies, Fertility, Women… (2007) | RECEPTION-1 | BACKGROUND | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E11: HBV "may offer a supplemental biological mechanism" for regional sex-ratio patterns |
| N18 W2176252721 Intrafamily Resource Allocations: A Dynamic Stru… (2012) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; birth-weight structural model; citation present in OpenAlex refs, use not inspected |
| N19 W4210337642 The income inequality-CO2 emissions nexus: Trans… (2022) | RECEPTION-1+RECENT-1 | UNRELATED | CITES-UNINSPECTED | NONE | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; income inequality and CO2; the OpenAlex citation link to the target is implausible (RECORD QUALITY); also RECENT-1 member R01 |
| N20 W2128916858 China's One‐Child Policy and ‘the Mystery of Mis… (2010) | RECEPTION-1 | DIRECT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; one-child policy, ethnic minorities and male-biased sex ratios; citation present in OpenAlex refs, use not inspected |
| N21 W2161434431 Causes and Consequences of Skewed Sex Ratios (2012) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Annual Review of Sociology review of skewed sex ratios; possible review hub; citation present in OpenAlex refs, use not inspected |
| N22 W2261388056 Improving Health in Developing Countries (2011) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; health handbook chapter; citation present in OpenAlex refs, use not inspected |
| N23 W2114131482 Does a legal ban on sex-selective abortions impr… (2013) | RECEPTION-1 | DIRECT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; legal ban on sex-selective abortion, India; citation present in OpenAlex refs, use not inspected |
| N24 W2100633408 Proximate sources of population sex imbalance in… (2009) | RECEPTION-1 | DIRECT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Oster-authored decomposition of India's sex imbalance; citation present in OpenAlex refs, use not inspected |
| N25 W2023373624 Missing Girls in India: Infanticide, Feticide an… (2008) | RECEPTION-1+ADJUDICATION-1 | DIRECT (R1) | CHALLENGES | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E12: the model "ignores the suggestion by Blumberg" that immunity moves the sex ratio the other way; also ADJUDICATION-1 (Q2) |
| N26 W1588168086 Sex Ratios, Entrepreneurship, and Economic Growt… (2011) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; sex ratios and entrepreneurship (a different work from N10); citation present in OpenAlex refs, use not inspected |
| N27 W1806205041 Why are adult women missing? Son preference and… (2018) | RECEPTION-1 | ADJACENT (R1) | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E13: "prevalence of Hepatitis B (Oster, 2005)" in a list of sex-ratio factors |
| N28 W2400620947 Work and Family: Latin American and Caribbean Wo… (2016) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; World Bank book on work and family; citation present in OpenAlex refs, use not inspected |
| N29 W2055080575 Sex ratios and the red dragon: using the Chinese… (2009) | RECEPTION-1 | BACKGROUND | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E14: results "not necessarily incompatible with the potential effect of the hepatitis B virus" |
| N30 W2083797948 Prenatal health investment decisions: Does the c… (2008) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; prenatal investment by child sex; citation present in OpenAlex refs, use not inspected |
| N31 W1994568240 Can Hepatitis B Mothers Account for the Number o… (2008) | RECEPTION-1+ADJUDICATION-1 | DIRECT (R2) | CHALLENGES | INDEPENDENT-DATA | FULL-TEXT (VERSION-SUBSTITUTE: author working-paper version 2008, homepage.ntu.edu.tw; AER version not retrieved) | INSPECTED | LL-E1 p. 1: effect "ranges only from 0.0010 to 0.0025"; LL-E2 p. 14: HBV has no effect on SRB; CTX-E15 restates "roughly half"; K2; also ADJUDICATION-1 (Q2) |
| N32 W1536465 Patrilocality and Missing Women (2014) | RECEPTION-1+ADJUDICATION-1 | ADJACENT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; patrilocality and missing women; also ADJUDICATION-1 (Q2); citation present in OpenAlex refs, use not inspected |
| N33 W2161438007 Sex Selection and Gender Balance (2011) | RECEPTION-1 | ADJACENT | MENTIONS | THEORY | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E16: "argument by Oster (2005) that hepatitis B infection raises the probability of having a boy" |
| N34 W2143614073 India's missing girls: biology, customs, and eco… (2007) | RECEPTION-1 | ADJACENT (L2) | MENTIONS | COMMENTARY | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E17: "Oster (2005) argues that hepatitis B may result in excessive male births" |
| N36 W1511329738 Son Preference in India: Implications for Gender… (2015) | RECEPTION-1 | ADJACENT | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E18: Drew et al. and Oster "contend that medical studies indicate" HBV mothers have fewer girls (2015; no refutation in passage) |
| N37 W2079414367 How do sex ratios in China influence marriage de… (2014) | RECEPTION-1 | BACKGROUND | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E19: footnote list of sex-ratio studies incl. Oster 2005, Lin & Luoh 2008, Oster et al. 2008 |
| N38 W2074516985 Why weren't (many) European women ‘missing’? (2011) | RECEPTION-1 | ADJACENT | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E20: whether there is "a biological dimension" (Das Gupta 2006; Oster 2005) |
| N39 W2115401314 Biological Basics and the Economics of the Famil… (2007) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; JEP essay on biology and family economics; citation present in OpenAlex refs, use not inspected |
| N40 W2066547533 Too Many Men? Sex Ratios and Women's Partnering… (2011) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | NOT-INSPECTED | S2 returned a truncated context that does not show the citation; use not inspected |
| N41 W2182501184 Gender Discrimination and Social Identity: Evide… (2018) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; gender discrimination, Pakistan; citation present in OpenAlex refs, use not inspected |
| N42 W2016329099 Female mouse fetal loss mediated by maternal aut… (2012) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; sex-specific fetal loss in mice; citation plausibly genuine (mechanism); citation present in OpenAlex refs, use not inspected |
| N43 W2048073431 Ultrasonography and Sex Ratios in China (2009) | RECEPTION-1 | DIRECT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; ultrasonography and sex ratios in China; citation present in OpenAlex refs, use not inspected |
| N44 W1964267580 The effect of the 1998 Master Settlement Agreeme… (2005) | RECEPTION-1 | UNRELATED | CITES-UNINSPECTED | NONE | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; prenatal smoking and the 1998 Master Settlement; the OpenAlex citation link to the target is implausible (RECORD QUALITY) |
| N45 W2042478072 Hepatitis B does not explain male-biased sex rat… (2010) | RECEPTION-1 | DIRECT (R2) | CHALLENGES | INDEPENDENT-DATA | FULL-TEXT (VERSION-SUBSTITUTE: NBER WP w13971, 2008; Economics Letters 2010 version not retrieved) | INSPECTED | OC-E1 p. 7: offspring of carrier vs non-carrier fathers 51.06% vs 51.56% male; OC-E2 p. 8: HBV carrier rates "cannot explain" China's male-biased sex ratios; K3; Oster co-author; POST HOC adjudication member (known item K3, not returned by the ADJUDICATION-1 search) |
| N46 W2119714514 Cultural versus Biological Factors in Explaining… (2006) | RECEPTION-1 | DIRECT (L3) | CHALLENGES | COMMENTARY | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E21: restates "75 percent of the 'missing women' in China" before contesting it (title: Response to Oster); K5; POST HOC adjudication member (known item K5, not returned by the ADJUDICATION-1 search) |
| N47 W1527265758 More Women Missing, Fewer Girls Dying: The Impac… (2008) | RECEPTION-1 | DIRECT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; abortion legalisation and sex ratios at birth, Taiwan; citation present in OpenAlex refs, use not inspected |
| N48 W2081799904 Son Preference and Household Income in Rural Chi… (2010) | RECEPTION-1 | ADJACENT (R1) | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E22: HBV "biological explanation" listed beside the socio-economic explanation |
| N49 W3124755079 Hidden consequences of a first-born boy for moth… (2014) | RECEPTION-1 | BACKGROUND | QUALIFIES | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E23: "her evidence, at least for China, has been widely criticized" |
| N50 W1976889960 Access to abortion, investments in neonatal heal… (2014) | RECEPTION-1 | BACKGROUND | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E24: Oster 2005 cited for Nepal being at risk of anti-girl bias |
| R02 W4403727727 Public pensions and family dynamics: Eldercare,… (2024) | RECENT-1 | ADJACENT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; pensions and son preference, rural China; citation present in OpenAlex refs, use not inspected |
| R03 W4397030871 Maternal hepatitis B status and Sex at birth: A… (2024) | RECENT-1 | DIRECT (R2) | CHALLENGES | INDEPENDENT-DATA | FULL-TEXT (PMC11137505, Europe PMC full-text XML; not committed) | INSPECTED | BA-E1 §1: restates "about 75 %" China and "about 20 %" South Asia; BA-E2 §4: no association between maternal HBsAg and offspring sex; POST HOC adjudication member (located via RECENT-1, not by the ADJUDICATION-1 search) |
| R04 W4409543403 The Estimation of the Number of Aborted Girls in… (2025) | RECENT-1 | ADJACENT (R1) | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed) | INSPECTED | CTX-E25: Oster (2005) "reported that women infected with … HBV are more likely to give birth to boys" (2025; no refutation in passage) |
| R05 W4385446270 Essays on culture, institutions and comparative… (2023) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; dissertation on culture and institutions; citation present in OpenAlex refs, use not inspected |
| R06 W4399729713 Dynamic general equilibrium models of the family… (2023) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; dissertation on family, fertility and health models; citation present in OpenAlex refs, use not inspected |
| A01 W2089286174 The Curiosities of Hepatitis B Virus: Prevention… (2006) | ADJUDICATION-1 | ADJACENT (L1) | UNKNOWN | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q1; Blumberg essay on HBV, sex ratio and demography; OpenAlex refs (7) omit the target but are incomplete |
| A02 W63810618 Hepatitis B Virus and Sex Ratio on Kar Kar Islan… (2000) | ADJUDICATION-1 | DIRECT (L1) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q1; reprint (2000) of Drew et al. 1982 Kar Kar island family study; predates target (cited by target as Drew et al. 1982) |
| A03 W195581690 Hepatitis B virus and sex ratio of offspring in… (1986) | ADJUDICATION-1 | DIRECT (L1) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q1; Greenland family study (1986); predates target; Section E locked source F2; cited by target |
| A04 W2391923276 Retrospective study on the association between m… (2010) | ADJUDICATION-1 | DIRECT (L1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q1; Chinese retrospective study of maternal HBV and offspring sex ratio (2010); result not read (no full text; abstracts not used) |
| A05 W2415116130 Hepatitis B virus, sex ratio and the H-Y antigen… (1980) | ADJUDICATION-1 | ADJACENT (L1) | NOT-CITING | COMMENTARY | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q1; HBV, sex ratio and H-Y antigen (1980); predates target |
| A06 W2129626017 Hepatitis B and the Sex Ratio at Birth: A Compar… (1988) | ADJUDICATION-1 | DIRECT (L1) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q1 and Q5; four-population comparison (1988); predates target; K8; Section E locked source F2; cited by target |
| A07 W1969795863 Sex ratio in offspring of mothers with hepatitis… (2000) | ADJUDICATION-1 | DIRECT (L1) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q1; offspring sex ratio of HBV mothers (2000); predates target; not in the target bibliography; result not read |
| A08 W2166552078 Support for a hypothesis on the offspring sex ra… (2007) | ADJUDICATION-1 | ADJACENT (L1) | UNKNOWN | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q1; James 2007 hypothesis note on HBV carriers' offspring sex ratios |
| A09 W2355691234 Hepatitis B Virus in Pregnant Women-the Influenc… (2007) | ADJUDICATION-1 | DIRECT (L1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q1; HBV in pregnant women and offspring sex ratio (2007, Chinese journal); result not read |
| A10 W2964809941 Missing Women, Gender Imbalance and Sex Ratio at… (2019) | ADJUDICATION-1 | ADJACENT (R1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q2; one-child policy and sex ratio at birth (SSRN 2019) |
| A11 W2978580588 Chapter 15. Missing Women (2009) | ADJUDICATION-1 | ADJACENT (L3) | UNKNOWN | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q2; Klasen chapter "Missing Women" (2009); possibly K6 (not counted as returned) |
| A12 W4403147335 + W3133548684 Baby Bonus, Fertility, and Missing Women (2024) | ADJUDICATION-1 | ADJACENT (R1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q2; baby bonus, fertility and missing women; one work under two records (SSRN preprint and JHR article) |
| A13 W2147178406 Son preference and the sex ratio at birth in Chi… (1997) | ADJUDICATION-1 | DIRECT (R1) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q3; provincial son preference and SRB in China (1997); predates target |
| A14 W2552766914 CHANGES IN SEX RATIO AT BIRTH IN CHINA: A DECOMP… (2016) | ADJUDICATION-1 | DIRECT (R1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; SRB decomposition by birth order, China |
| A15 W3162357794 Recent sex ratio at birth in China (2021) | ADJUDICATION-1 | ADJACENT (R1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; recent SRB in China |
| A16 W2355836375 Parity-Intensification Effect:Birth Planning Pol… (2009) | ADJUDICATION-1 | DIRECT (R1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; parity-intensification effect, China |
| A17 W3009429537 IS THERE SON PREFERENCE IN INDIA? - AN ANALYSIS… (2020) | ADJUDICATION-1 | DIRECT (R1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; son preference and SRB by birth order, India |
| A18 W2912981086 IMBALANCE IN CHINA'S SEX RATIO AT BIRTH: A REVIE… (2019) | ADJUDICATION-1 | ADJACENT (R1) | UNKNOWN | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; review of China's SRB imbalance; OpenAlex refs (47) omit the target but are incomplete |
| A19 W2020683083 Sex Ratio at Birth in India, Its Relation to Bir… (2011) | ADJUDICATION-1 | DIRECT (R1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; SRB in India by birth order and sex of previous children |
| A20 W2753884747 Why Are Indian Children So Short? The Role of Bi… (2017) | ADJUDICATION-1 | BACKGROUND | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q3; birth order, son preference and child height; OpenAlex refs (64) omit the target |
| A21 W2043906799 DAUGHTER DISCRIMINATION AND FUTURE SEX RATIO AT… (2012) | ADJUDICATION-1 | ADJACENT (R1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; daughter discrimination and future SRB, India |
| A22 W961876696 Study on the Relationship between Parity Structu… (2014) | ADJUDICATION-1 | DIRECT (R1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; parity structure and SRB imbalance, China |
| A23 W2021092087 BEHAVIOURAL AND BIOLOGICAL DETERMINANTS OF HUMAN… (2010) | ADJUDICATION-1 | ADJACENT (R4) | UNKNOWN | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; behavioural and biological determinants of SRB (James 2010) |
| A24 W2026289855 SKEWED SEX RATIO AT BIRTH IN INDIA (2009) | ADJUDICATION-1 | ADJACENT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; skewed SRB in India; OpenAlex refs contain the target; use not inspected |
| A25 W2116894238 Recent Increase in Sex Ratio at Birth in Viet Na… (2009) | ADJUDICATION-1 | ADJACENT (R1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; rising SRB in Viet Nam |
| A26 W2087034505 Sex ratio at birth: A model based approach (2012) | ADJUDICATION-1 | ADJACENT (R4) | UNKNOWN | METHOD | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; model-based SRB |
| A27 W2901780678 Trends in sex ratio at birth in Slovenia (2018) | ADJUDICATION-1 | BACKGROUND | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; SRB trends in Slovenia; no OpenAlex refs |
| A28 W2792316282 Correlation of sex ratio at birth with health an… (2018) | ADJUDICATION-1 | ADJACENT (R4) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; SRB and health or socio-economic indicators |
| A29 W2795258545 Infanticide and Sex Ratio at Birth in Contempora… (2018) | ADJUDICATION-1 | BACKGROUND | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; infanticide and SRB in Italy; OpenAlex refs (1) too sparse to code |
| A30 W2016338915 Sex Ratio at Birth and Mortality Rates Are Negat… (2011) | ADJUDICATION-1 | ADJACENT (R4) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; SRB negatively related to mortality |
| A31 W4407172282 Prenatal Care, Son Preference, and the Sex Ratio… (2025) | ADJUDICATION-1 | ADJACENT (R1) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; prenatal care, son preference and SRB (2025) |
| A32 W2393854264 An Analysis of Multifactor Effect on Sex Ratio a… (2009) | ADJUDICATION-1 | ADJACENT (R4) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; multifactor analysis of SRB (Chinese journal) |
| A33 W2875903878 Prophylactic hepatitis B immunization in chronic… (2018) | ADJUDICATION-1 | UNRELATED | UNKNOWN | NONE | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q5; HBV immunisation in kidney disease; no OpenAlex refs |
| A34 W2890595746 Post-Vaccine Immunity against Hepatitis B in Bur… (2018) | ADJUDICATION-1 | UNRELATED | NOT-CITING | NONE | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q5; post-vaccine HBV immunity, Burkina Faso; OpenAlex refs (8) omit the target |
| A35 W4405823174 Profile of the Immune Response to Hepatitis B Va… (2024) | ADJUDICATION-1 | UNRELATED | UNKNOWN | NONE | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q5; HBV vaccine response in dialysis; no OpenAlex refs |
| A36 W7117136974 Prevalence and Vaccination Status of Hepatitis B… (2025) | ADJUDICATION-1 | UNRELATED | NOT-CITING | NONE | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q5; HBV prevalence and vaccination among HIV patients, Chad; OpenAlex refs (9) omit the target |
| A37 W2185955083 The Relation of Infection With the Hepatitis B A… (2000) | ADJUDICATION-1 | BACKGROUND | NOT-CITING | NONE | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q5; HBV and primary hepatic carcinoma (2000 reprint of a Blumberg paper); predates target |
| A38 W4226002143 Completeness and Timeliness of Hepatitis B Vacci… (2022) | ADJUDICATION-1 | UNRELATED | NOT-CITING | NONE | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q5; HBV vaccination timeliness in children; OpenAlex refs (9) omit the target |
| A39 W7163756956 Evaluation of vaccination status and immune resp… (2026) | ADJUDICATION-1 | UNRELATED | UNKNOWN | NONE | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q5; HBV vaccination in haemodialysis; no OpenAlex refs |
| A40 W7114766517 Vaccine Response against Hepatitis B Virus in Pa… (2025) | ADJUDICATION-1 | UNRELATED | NOT-CITING | NONE | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q5; HBV vaccine response in kidney failure; OpenAlex refs (5) omit the target |
| T01 W3123222584 + W3126094291 (RePEc preprint record) Hepatitis B and the Case of the Missing Women (2005) — target | ADJUDICATION-1 | DIRECT (L1) | NOT-CITING | INDEPENDENT-DATA | FULL-TEXT (JPE 113(6) PDF, institutional access copy; not committed) | NOT-APPLICABLE | target source returned by Q2 and Q5; JP-E1 p. 1172, JP-E2 p. 1179, JP-E3 p. 1201, JP-E4 and JP-E5 p. 1203, JP-E6 p. 1189 used as source passages |
| X01 W2023743440 + W4235601100 (2000 reprint record) Hepatitis B Virus and Sex Ratio of Offspring (Drew, London, Lustbader 1978) | ADJUDICATION-1 | DIRECT (L1) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Science 1978 family study and its 2000 reprint (Q1); predates target; Section E locked source F2; cited by target |
| X02 Slate 2005, "Where did 100 million missing women go?" (Landsburg) | OUTSIDE | ADJACENT (L3) | SUPPORTS | COMMENTARY | FULL-TEXT (slate.com HTML, HTTP 200; not committed) | INSPECTED | SL-E1: if the results are "extremely compelling", her work "has established the fate of roughly 50 million" missing women (conditional) |
| X03 Klasen 2005, "Comments on Paper by Emily Oster" (Göttingen working note, 8 July 2005) | OUTSIDE | DIRECT (R4) | QUALIFIES | COMMENTARY | FULL-TEXT (uni-goettingen.de PDF, HTTP 200; not committed) | INSPECTED | KL-E1 p. 1: with a life-expectancy-adjusted SRB benchmark the total would "end up close to" Coale's 60 million |
| X04 W1992232430 Mothers and Sons: Preference Formation and Female Labor Force Dynamics (Fernández, Fogli & Olivetti 2004) | OUTSIDE | BACKGROUND | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F1; predates target; off-topic hit for "son preference"; retained, not replaced |
| X05 W2139821597 Why is son preference so persistent in East and South Asia? (Das Gupta et al. 2003) | OUTSIDE | ADJACENT (R1) | NOT-CITING | REVIEW | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F1; predates target; not cited by target |
| X06 W2074655452 Son preference and sex composition of children: evidence from India (Clark 2000) | OUTSIDE | ADJACENT (R1) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F1; predates target; not cited by target |
| X07 W1973842394 Maternal dominance, breeding success and birth sex ratios in red deer (Clutton-Brock et al. 1984) | OUTSIDE | BACKGROUND | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F3; predates target; animal sex-ratio biology; not cited by target |
| X08 W2249723975 Causes and implications of the recent increase in the reported sex ratio at birth in China (Zeng Yi et al. 1993) | OUTSIDE | DIRECT (R1) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F3; predates target; cited by target as Yi et al. 1993 (JP-E1) |
| X09 W2083763800 Evidence that mammalian sex ratios at birth are partially controlled by parental hormone levels (James 1996) | OUTSIDE | ADJACENT (L1) | NOT-CITING | THEORY | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F3; predates target; not cited by target (James 1987a, 1987b cited instead) |
| X10 W2081758747 Missing Women: Revisiting the Debate (Klasen & Wink 2003) | OUTSIDE | DIRECT (R4) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F4; predates target; not cited by target |
| X11 W3124113130 A Turning Point in Gender Bias in Mortality? (Klasen & Wink 2002) | OUTSIDE | DIRECT (R4) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F4; predates target; cited by target (JP-E4, n. 26) |
| X12 W2031660749 "Missing Women" Reconsidered (Klasen 1994) | OUTSIDE | DIRECT (R4) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F4; predates target; cited by target |

Coding notes. CTX-E ids resolve to Semantic Scholar citation contexts (request /graph/v1/paper/DOI:10.1086/498588/citations?fields=title,externalIds,year,contexts,intents&limit=1000, 2026-11-05T10:26:46Z, HTTP 200, response sha256 c570ae9f4fa617d1b873a455054a752b97ab0077f77d1ce11ed3e83576d1c3c4; response not committed). Relation for ADJUDICATION-1 non-reception members: OpenAlex reference list contains W3123222584 → CITES-UNINSPECTED; reference list empty or sparse → UNKNOWN; non-empty list without the target, or publication before the target → NOT-CITING (NOT-APPLICABLE). DIRECT members published after 2005 stay UNKNOWN when OpenAlex omits the target, because reference lists are incomplete. Relevance and contribution for METADATA rows are coded from the title only (abstracts were not used under the rights rules). JP-E ids resolve to pages of the target (JPE 113(6)): JP-E1 p. 1172 (sex-selective abortion literature), JP-E2 p. 1179 (six family studies), JP-E3 p. 1201 (share of missing women), JP-E4 p. 1203 n. 26 (Klasen & Wink), JP-E5 p. 1203 n. 27 (benchmark), JP-E6 p. 1189 (life-expectancy controls). LL-E, OC-E, BA-E, SL-E and KL-E ids resolve to the pages given in each row.

SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION

GRAPH CORPUS AND RECEIPTS

GRAPH CORPUS DEFINITION: RECEPTION-1 as registered in SECTION A0 (OpenAlex, filter=referenced_works:W3123222584, sort=cited_by_count:desc, top 50 records, executed 2026-11-05T10:25:08Z, no date or type bounds, no screening). Nodes are works: the two records of row N09 are one node, so n = 49. The target is outside the density corpus; citer -> target edges hold by construction and are not counted.
GRAPH CORPUS NODE LIST: N01=W2114978546; N02=W4234238734; N03=W2121199232; N04=W2026772829; N05=W2782446622; N06=W3123575441; N07=W2057390815; N08=W1982754848; N09=W2125485011+W1581958734; N10=W2123699796; N11=W3122231766; N12=W2096320699; N13=W2030091805; N14=W1982250044; N15=W1593586622; N16=W1969182143; N17=W3124330411; N18=W2176252721; N19=W4210337642; N20=W2128916858; N21=W2161434431; N22=W2261388056; N23=W2114131482; N24=W2100633408; N25=W2023373624; N26=W1588168086; N27=W1806205041; N28=W2400620947; N29=W2055080575; N30=W2083797948; N31=W1994568240; N32=W1536465; N33=W2161438007; N34=W2143614073; N36=W1511329738; N37=W2079414367; N38=W2074516985; N39=W2115401314; N40=W2066547533; N41=W2182501184; N42=W2016329099; N43=W2048073431; N44=W1964267580; N45=W2042478072; N46=W2119714514; N47=W1527265758; N48=W2081799904; N49=W3124755079; N50=W1976889960
INTERNAL EDGE LIST: N01 -> N31; N02 -> N08; N02 -> N31; N02 -> N45; N03 -> N01; N03 -> N04; N03 -> N12; N03 -> N15; N04 -> N08; N04 -> N11; N04 -> N24; N04 -> N31; N04 -> N45; N05 -> N31; N05 -> N45; N05 -> N46; N06 -> N08; N06 -> N39; N07 -> N01; N07 -> N02; N07 -> N08; N07 -> N31; N07 -> N45; N09 -> N02; N10 -> N08; N10 -> N14; N10 -> N20; N10 -> N31; N11 -> N30; N12 -> N24; N14 -> N01; N14 -> N02; N14 -> N08; N14 -> N11; N14 -> N31; N14 -> N47; N15 -> N02; N15 -> N03; N15 -> N08; N15 -> N11; N15 -> N24; N15 -> N30; N15 -> N33; N15 -> N34; N15 -> N45; N15 -> N47; N16 -> N34; N20 -> N01; N20 -> N08; N20 -> N10; N20 -> N31; N20 -> N45; N21 -> N04; N21 -> N08; N21 -> N11; N21 -> N33; N21 -> N45; N21 -> N46; N22 -> N01; N22 -> N02; N22 -> N08; N22 -> N31; N23 -> N01; N23 -> N02; N23 -> N08; N23 -> N29; N23 -> N31; N23 -> N43; N23 -> N47; N23 -> N50; N24 -> N01; N25 -> N08; N26 -> N08; N26 -> N10; N26 -> N14; N26 -> N20; N26 -> N31; N26 -> N43; N26 -> N45; N27 -> N01; N27 -> N03; N27 -> N04; N27 -> N08; N27 -> N11; N27 -> N15; N27 -> N24; N28 -> N08; N28 -> N11; N28 -> N24; N28 -> N31; N28 -> N45; N28 -> N46; N28 -> N47; N29 -> N01; N30 -> N11; N31 -> N01; N31 -> N08; N31 -> N45; N31 -> N46; N32 -> N01; N32 -> N02; N32 -> N08; N33 -> N01; N33 -> N04; N33 -> N11; N33 -> N31; N33 -> N34; N36 -> N08; N37 -> N01; N37 -> N08; N37 -> N29; N37 -> N31; N38 -> N08; N38 -> N11; N38 -> N46; N39 -> N06; N39 -> N08; N41 -> N01; N41 -> N03; N41 -> N15; N41 -> N31; N43 -> N31; N43 -> N47; N45 -> N08; N45 -> N31; N46 -> N08; N47 -> N01; N47 -> N04; N47 -> N14; N47 -> N31; N48 -> N20; N49 -> N39; N50 -> N15; N50 -> N47
DERIVATION MODE: COMPUTED-FROM-RETRIEVED
DENSITY CALCULATION: directed density = directed internal edges u -> v (u, v work nodes, u != v, v in OpenAlex referenced_works of u) / n(n-1), n = 49; computed by scripts/build_2c.py from raw/reception1_top50.json (record-level cross-check by scripts/graph.py).
DENSITY NUMERATOR: 134 directed internal edges among the 49 work nodes.
DENSITY DENOMINATOR: 2352 possible directed edges (49 × 48).
DENSITY INPUT COVERAGE: 50/50 record reference lists obtained from OpenAlex (3,641 indexed references across the 49 works). No Crossref cross-check.
DENSITY INFERENCE SCOPE: the density result applies only to RECEPTION-1. Because RECEPTION-1 is selected on target citation, it can establish density inside that target-citing corpus; it cannot establish or exclude field-wide, founding-cluster or premise-subnetwork closure. No seed-expanded or matched comparison graph was built.

Closure is not established and not excluded beyond the defined corpus.

Density results. Work-level directed density 134/2352 = 5.70%; record-level (50 records) 135/2450 = 5.51%. 40/49 works cite at least one other member. Reciprocal pairs: 7. In-degree leaders: N08 23, N31 18, N01 15, N45 10, N11 9, N02 7, N47 6, N04 5. The two most-cited nodes inside the corpus are critiques of the target (N08 Das Gupta 2005; N31 Lin & Luoh 2008). Oster-authored works (N12, N24, N45) receive 16/134 internal edges, 10 of them to N45, the author's own null test.

1. Top 50 most-cited works citing Oster (2005): RECEPTION-1 (Artifact 1 lists the top 15). Relevance composition: ADJACENT=16; BACKGROUND=17; DIRECT=14; UNRELATED=2.
2. Founding cluster: the target alone; there is no co-authoring team. Oster-authored works in RECEPTION-1: N12 (2008 JDE), N24 (2009 Demography), N45 (2010 Economics Letters, with Chen, Yu and Lin). The HBV–sex-ratio studies the target pools (Drew et al. 1978 onward) are prior medical work by other teams.
3. Founding papers' evidence type: the target is a secondary analysis of six small published family studies plus country and county associations (FULL-TEXT, JP-E2); N45 is a primary cohort test (FULL-TEXT, VERSION-SUBSTITUTE).
4. Hubs: N08 (in-degree 23) and N31 (18) are critiques; N01 Qian 2008 (15) is an R1 study. Oster-authored works receive 16/134 internal edges.
5. Hub substitution: within RECEPTION-1, 21/49 works co-cite Lin & Luoh 2008 or Oster et al. 2010 alongside the target; among the 35 works published 2009 or later, 18/35.
6. Small cluster citing itself: no closed cluster inside RECEPTION-1 (density 5.70%).
7. Gatekeeping roles: no editorial or referee data retrieved; UNASSESSED.
8. Self-citation in the founding cluster: N12 and N24 are the author's later son-preference work; N45 is the author's own test that withdraws L1 in substance.
9. Concentration by lab/journal/funder: not assessed beyond authorship (SECTION I).
10. Citation count vs independent confirmation: target cited_by_count 173 at retrieval; independent tests of L1 with new data (N31, N45, R03) are null (I13, I14).

SECTION B: EVIDENCE TYPE CODING

Every corpus member is coded in the SOURCE ELIGIBILITY LEDGER. Questions 11–16 describe the evidence base only on ADJUDICATION-1, the SEARCHED adjudication corpus; on RECEPTION-1 they describe the citing set.

ADJUDICATION-1 composition (evidence base, bounded by the locked search; METADATA-coded):
COMPOSITION: I15 | relevance | ADJACENT=18; BACKGROUND=4; DIRECT=17; UNRELATED=7 | TOTAL=46
COMPOSITION: I16 | contribution | COMMENTARY=1; INDEPENDENT-DATA=31; METHOD=1; NONE=8; REVIEW=4; THEORY=1 | TOTAL=46
RECEPTION-1 composition (citing set only):
COMPOSITION: I17 | relevance | ADJACENT=16; BACKGROUND=17; DIRECT=14; UNRELATED=2 | TOTAL=49

11. Primary empirical tests in ADJUDICATION-1: DIRECT (L1) 8 (A02, A03, A04, A06, A07, A09, T01, X01), DIRECT (R2) 1 (N31), DIRECT (R1) 8. Most DIRECT (L1) members are the pre-2005 family studies the target pools or later small studies whose results were not read (A04, A07, A09; I23).
12. Reviews/syntheses: REVIEW and COMMENTARY members are counted in I16; none was read in full.
13. Theory-only: THEORY members are counted in I16 (for example A08, James 2007 hypothesis note).
14. Unknown: relevance UNKNOWN as counted in I15; Relation UNKNOWN is common where OpenAlex reference lists are empty or omit the target.
15. Evidence-to-claim ratio: the L1 evidence the target rests on is six small family studies (355 boys and 248 girls among carriers' children, JP-E2); the later large tests (N31 Taiwan births, N45 Chinese cohort of about 67,000, R03 Ghana) use new and independent data (I14).
16. On RECEPTION-1 the same questions describe citers: ADJACENT=16; BACKGROUND=17; DIRECT=14; UNRELATED=2 (of 49).

SECTION C: CITATION POLARITY AND CLAIM USE

Citing passages inspected: CITATION CONTEXT COVERAGE: RECEPTION-1 24/49 (N03, N04, N05, N07, N11, N12, N13, N15, N16, N17, N25, N27, N29, N31, N33, N34, N36, N37, N38, N45, N46, N48, N49, N50); CITATION CONTEXT COVERAGE: RECENT-1 2/6; CITATION CONTEXT COVERAGE: ADJUDICATION-1 2/46. Most RECEPTION-1 passages are EXCERPT (Semantic Scholar contexts). The prespecified random sample of 12 lost 9 members (I05). Percentages use inspected passages only.

17. Supportive: SUPPORTS 2/24 (N12 self-citation; N13 "confirmed").
18. Critical: CHALLENGES 4/24; QUALIFIES 4/24.
19. Perfunctory/background: MENTIONS 14/24. RECENT-1: R03 CHALLENGES (tests and rejects L1), R04 MENTIONS.
20. Premise use: none of the inspected passages uses the HBV share as a premise for its own analysis.
21. Data/instrument reuse: none.
22. Polarity inflation: N13 upgrades the target's pooled re-tabulation to a confirmation (CTX-E8); N03 misdescribes the mechanism as female-biased disease (CTX-E1). Slate states the 50-million figure conditionally (SL-E1).

SECTION D: CLAIM MUTATION TRACKING

23–30. Original (JP-E3, p. 1201): about 47 percent of Coale's missing women, roughly 75 percent in China and under 20 percent in India, with a wide interval (13.5–71.5). Downstream restatements mostly preserve the magnitude: N07 "about 70%" (CTX-E4), N11 "around 75%" for China and "around 17%" for India (CTX-E5, CTX-E6), N31 roughly half (CTX-E15), N46 75 percent for China (CTX-E21), R03 about 75% and about 20% (BA-E1), Slate roughly 50 million, conditional on the results being compelling (SL-E1). Mutations found: a certainty upgrade in N13 ("confirmed", CTX-E8) and a mechanism misdescription in N03 (female-biased disease, CTX-E1). R03 frames the effect as maternal carrier status (BA-E1), whereas the target pools both parents. Severity: minor; no restatement inflates the magnitude. Post-refutation passages that state the HBV effect without the refutation (N36, N27, R04) are use drift, treated in SECTION H, not magnitude mutation.

| Original source | Original claim | Hub restatement | Downstream restatement | Mutation severity | Note |
|---|---|---|---|---|---|
| Oster 2005 p. 1201 (JP-E3) | about 47% of missing women; CI 13.5–71.5 | none found | N07 "about 70%" China; N31 roughly half | none | magnitude preserved |
| Oster 2005 p. 1179 (JP-E2) | pooled re-tabulation of six family studies | none found | N13: "the result confirmed by Oster (2005)" | minor | certainty upgrade |
| Oster 2005 p. 1179 (JP-E2) | carriers have more sons | none found | N03: "greater incidence of female-biased diseases" | minor | mechanism misdescribed |
| Oster 2005 p. 1179 (JP-E2) | carrier parent (either parent) | none found | R03: maternal carrier status (BA-E1) | minor | carrier narrowed to mother |

SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT

Steps 31–37. Layers L1–L4 and rivals R1–R4 are locked in lock/ADJUDICATION-1_search_record.md; fields F1–F4 and observations O1–O4 in lock/section_E_preregistration.md, hashed before the Section E queries ran. The lock is post-exposure (the target bibliography was read in Stage 1), so sources are fixed mechanically by a ranked query.

SOURCE-LOCK METHOD: LOCKED QUERY
SOURCE-LOCK DATABASE: OpenAlex works API (select omits abstract_inverted_index)
SOURCE-LOCK QUERY OR SOURCE LIST: filter=title.search:<terms>,to_publication_date:2005-06-30,type:article, sort=cited_by_count:desc, per-page=3; terms F1 "son preference", F2 "hepatitis B sex ratio", F3 "sex ratio at birth", F4 "missing women"
SOURCE-LOCK DATE CUTOFF: 2005-06-30 (publication on or before; JPE issue December 2005)
SOURCE-LOCK RANKING RULE: OpenAlex cited_by_count descending at query time
SOURCE-LOCK N: 12 (top 3 per field × 4 fields)
SOURCE-LOCK DEDUPLICATION RULE: by OpenAlex work ID; off-topic items retained and flagged, never replaced
SOURCE-LOCK TIMESTAMP OR HASH: 2026-11-05T10:29:05Z (2:29:05 AM PST); preregistration sha256 5e43e7a48d3a4271fd842e65b14fcc7e06b9ae94a3f705a618cca3a3120f9451; queries executed after the lock (F1 after about nine HTTP 429 retries, success 10:35:51Z)

Flip test (step 37): PASS. F1 and F3 are generated from rivals R1 and R4; F2 from both L1 and R2; F4 from L3 and R4 (both). Innocent explanations: F1 exemplars include an off-topic labour paper (X04); F3 exemplars include animal biology (X07).

Falsification-relevant literature preregistration table:

| Claim layer | Audited explanation | Strongest plausible rival explanation | Adjudicating observation | Candidate field | Generated from audited claim, rival, or both? | Measurement relevance | Adjudicative capacity | Independence | Publication-date cutoff | Historically available? | Flip-test result | Source-lock method | Lock timestamp / hash | Final engagement classification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L2/L3 | HBV raises the sex ratio at birth | R1 son preference and sex selection | O1 parity-specific sex ratios | F1 son preference | rival | sex-selection behaviour | could weaken L3 | independent | 2005-06-30 | yes | PASS | LOCKED QUERY | 5e43e7a4…9451 | direct substantive engagement (JP-E1 discusses sex-selective abortion) |
| L1 | carriers have more sons | R2 null carrier effect | O2 carrier vs non-carrier offspring sex | F2 HBV and offspring sex | both | individual-level effect | could defeat L1 | independent of the target | 2005-06-30 | yes | PASS | LOCKED QUERY | as above | direct substantive engagement (JP-E2 pools the F2 studies) |
| L3 | HBV-adjusted benchmark | R4 benchmark varies with mortality | O3 natural sex-ratio variation | F3 sex ratio at birth | rival | benchmark validity | could narrow L3 | independent | 2005-06-30 | yes | PASS | LOCKED QUERY | as above | citation with partial engagement (Zeng/Yi et al. cited, JP-E1; life-expectancy controls, JP-E6) |
| L3 | 47% of Coale's missing women | R4 and alternative counts | O4 deficit under other benchmarks | F4 missing-women accounting | both | the accounted quantity | could narrow L3 | independent | 2005-06-30 | yes | PASS | LOCKED QUERY | as above | direct substantive engagement (JP-E4, JP-E5) |

Adjacent-literature neglect table:

| Claim layer | Adjacent field | Nominated source and stable identifier | Verification state | Source class: CONSTRUCT-DEFINING / MECHANISM-SUPPORTING / DIRECTLY-ADJUDICATING | Actual result | Explanation favored | Explanation weakened | Precise revision required | Pre-inspection lock status or POST HOC | Cited by dominant cluster? | Engagement quality | Effect of omission |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L2/L3 | F1 son preference | X04 W1992232430 | LOCATED | MECHANISM-SUPPORTING | BACKGROUND (off-topic labour paper) (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited | none |
| L2/L3 | F1 son preference | X05 W2139821597 | LOCATED | MECHANISM-SUPPORTING | son preference persistence (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited; R1 literature engaged via other works (JP-E1) | minor context loss |
| L2/L3 | F1 son preference | X06 W2074655452 | LOCATED | MECHANISM-SUPPORTING | sex composition and son preference, India (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited; R1 engaged via other works | minor context loss |
| L1 | F2 HBV and offspring sex | X01 W2023743440 | LOCATED | DIRECTLY-ADJUDICATING | carrier families have more sons: carriers' offspring male-biased, as tabulated in the target (JP-E2; source text not read) | L1 | R2 (at small-sample level) | none for L1 from this source alone; superseded by larger tests (I13) | LOCKED (Section E query) | yes (target) | substantively engaged (JP-E2) | none |
| L1 | F2 HBV and offspring sex | A06 W2129626017 | LOCATED | DIRECTLY-ADJUDICATING | four-population comparison: carriers' offspring male-biased, as tabulated in the target (JP-E2; source text not read) | L1 | R2 (at small-sample level) | none for L1 from this source alone; superseded by larger tests (I13) | LOCKED (Section E query) | yes (target) | substantively engaged (JP-E2) | none |
| L1 | F2 HBV and offspring sex | A03 W195581690 | LOCATED | DIRECTLY-ADJUDICATING | Greenland family study: carriers' offspring male-biased, as tabulated in the target (JP-E2; source text not read) | L1 | R2 (at small-sample level) | none for L1 from this source alone; superseded by larger tests (I13) | LOCKED (Section E query) | yes (target) | substantively engaged (JP-E2) | none |
| L3 | F3 sex ratio at birth | X07 W1973842394 | LOCATED | CONSTRUCT-DEFINING | animal sex-ratio biology (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited | none |
| L3 | F3 sex ratio at birth | X08 W2249723975 | LOCATED | CONSTRUCT-DEFINING | rising reported sex ratio in China; underreporting and sex selection (title; results not read) | — | — | — | LOCKED (Section E query) | yes (target) | directly engaged (JP-E1) | none |
| L3 | F3 sex ratio at birth | X09 W2083763800 | LOCATED | CONSTRUCT-DEFINING | hormonal hypothesis of sex ratios (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited (other James papers cited) | minor context loss |
| L3 | F4 missing women | X10 W2081758747 | LOCATED | CONSTRUCT-DEFINING | missing women revisited (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited (2002 update cited instead) | minor context loss |
| L3 | F4 missing women | X11 W3124113130 | LOCATED | CONSTRUCT-DEFINING | updated missing-women estimates (title; results not read) | — | — | — | LOCKED (Section E query) | yes (target) | substantively engaged (JP-E4) | none |
| L3 | F4 missing women | X12 W2031660749 | LOCATED | CONSTRUCT-DEFINING | missing women reconsidered, benchmark (title; results not read) | — | — | — | LOCKED (Section E query) | yes (target) | engaged; benchmark argument answered in part (JP-E5, JP-E6) | none |
| L1 | R2 test | N31 W1994568240 Lin & Luoh 2008 | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | carrier mothers' effect 0.0010–0.0025 (LL-E1) | R2 | L1, L3 | L1: carrier effect near zero; L3 not supported | LOCKED (ADJUDICATION-1 search) | yes (N45 cites it) | substantively engaged by the author (OC-E2) | not omitted |
| L1 | R2 test | N45 W2042478072 Oster, Chen, Yu & Lin 2010 | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | 51.06% vs 51.56% male (OC-E1) | R2 | L1, L2, L3 | L3 withdrawn for China by the author (OC-E2) | POST HOC (known item K3, not returned by the locked search) | author's own work | the update itself | not omitted |
| L1 | R2 test | R03 W4397030871 Banyeh et al. 2024 | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | no association of maternal carrier status with infant sex (BA-E2) | R2 | L1 | as above | POST HOC (RECENT-1 member, not ADJUDICATION-1) | n/a (2024) | — | not omitted |

The source layer engages R1 (JP-E1), the F2 family studies (JP-E2) and the R4 benchmark debate (JP-E4, JP-E5, JP-E6). Of the 12 locked sources the target cites 6 (all three F2 sources, X08, X11, X12). The uncited items are off-topic exemplars or near-duplicates of cited work. ENGAGEMENT I19 carries the score; the R2 tests post-date the target and are scored under decisive tests and critique uptake.

SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING

40. Hubs inside RECEPTION-1: N08 Das Gupta 2005 (in-degree 23), N31 Lin & Luoh 2008 (18), N01 Qian 2008 (15), N45 Oster et al. 2010 (10). Review-type works: N21 Dyson 2012 (Annual Review of Sociology), N13 James 2007, handbook chapters N06, N17, N22.
41. Recent papers citing the hubs: Das Gupta 2005 2/6, Lin & Luoh 1/6, Oster et al. 2010 1/6 in RECENT-1.
42. Recent papers citing primary evidence directly: 6/6 cite the target by construction.
43. Hub substitution for inspection: not measurable from reference lists; no passage citing a review hub was inspected (I22 NOT-ASSESSED).
44–45. Hub accuracy: N13 (James 2007) upgrades certainty (CTX-E8); N21 Dyson not inspected.
46. Adjacent literatures in hubs: N08 and N46 are demography (R1); N31 and N45 are economics with medical data.
47. Hub as substitute for primary evidence: UNASSESSED.

| Hub paper | Recent papers citing hub | Recent papers citing primary evidence directly | Adjacent-field citation rate | Hub accuracy | Hub risk |
|---|---|---|---|---|---|
| Das Gupta 2005 (N08) | 2/6 RECENT-1 | 6/6 by construction | 23/49 RECEPTION-1 co-cite | critique; not inspected | low |
| Lin & Luoh 2008 (N31) | 1/6 RECENT-1 | 6/6 by construction | 18/49 RECEPTION-1 co-cite | accurate restatement (CTX-E15) and null test | low |
| James 2007 (N13) | 0/6 RECENT-1 | 6/6 by construction | — | certainty upgrade (CTX-E8) | low (small in-corpus in-degree) |
| Dyson 2012 (N21) | 0/6 RECENT-1 | 6/6 by construction | — | not inspected | UNASSESSED |

SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR

48. Proxy treated as construct: carrier prevalence stands in for an offspring sex-ratio effect; the inspected restatements keep the share framing (SECTION D); proxy mismatch was not traced further.
49. Export from low-stakes settings: the 1.54 carrier sex ratio comes from small, mostly non-Asian family studies (JP-E2) and is exported to Asian populations; this is a paper-level issue (Stages 2a/2b).
50. Ignored natural experiments: no; the target uses vaccination (Alaska, Taiwan) as quasi-experiments.
51. Model updating: yes; the author's cohort test concludes HBV cannot explain China's male-biased sex ratios (OC-E2).
52. Intervention expansion: no intervention claim; N/A.
53–55. Falsification criteria: the target states that vaccination should lower sex ratios; later tests use carrier status directly. 55 N/A.
56. Expansion over testing: no.

Ratchet scoring route. Intervention-evidence ratchet: N/A (no intervention claim). Model non-updating four-link gate: link 1 (model stated: HBV explains a large share) met, JP-E3; link 2 (verified later disconfirming evidence) met, N31 and N45 FULL-TEXT (I13); link 3 (reception opportunity) met, the author co-wrote N45; link 4 (non-updating) NOT met: the author updates (I18). Model non-updating SCORED 0.

SECTION H: IGNORED CRITIQUE AND NON-UPTAKE

1. Precondition: critique production strongly expected (JPE article; high-profile magnitude; popular coverage, X02).
2. Retrieval: Lin & Luoh (N31, FULL-TEXT version substitute); Oster et al. (N45, FULL-TEXT version substitute); Klasen comments (X03, FULL-TEXT); Das Gupta 2005 and 2006 (N08 METADATA; N46 EXCERPT only).
3. Reception opportunity: verified; the author co-wrote the cohort test N45.
4. Uptake in the uptake population: the author engages and accepts the null (ENGAGEMENT I18). Co-citation alone carries no score: Lin & Luoh or Oster et al. 2010 are co-cited by 18/35 RECEPTION-1 works published 2009 or later (I20, descriptive). Three inspected post-2010 passages state the HBV effect without the refutation in the passage (N36, N27, R04; I25), so downstream uptake is incomplete.

57. Serious critiques: Das Gupta 2005 and 2006 (R1, parity patterns); Lin & Luoh 2008 (R2); Oster et al. 2010 (R2); Klasen comments (R4 benchmark); Blumberg (immunity direction, raised via N25).
58. Cited by the dominant cluster: the author's own follow-up cites Lin & Luoh (N45).
59. Mode: engaged and accepted (the claim is withdrawn for China).
60. Network update: partial; critiques are hubs inside RECEPTION-1, yet some later citers restate the HBV effect (I25).
61. Recent papers: R03 tests and rejects L1 (BA-E2); R04 restates the 2005 claim (CTX-E25).
62–63. Practitioner warnings: not searched; UNASSESSED.

| Expected-production precondition | Critique / contrary evidence | Year | Source type | Main objection | Verification state | Reception opportunity | Cited by dominant cluster? | Uptake status | Dimension disposition | Effect on consensus |
|---|---|---|---|---|---|---|---|---|---|---|
| strong | Lin & Luoh, AER (N31, W1994568240) | 2008 | primary empirical | carrier effect near zero in Taiwan births (LL-E1, LL-E2) | FULL-TEXT-CONFIRMED | verified | yes (N45); 18/49 RECEPTION-1 | engaged and accepted by the author | SCORED 0 | refutation widely co-cited |
| strong | Oster, Chen, Yu & Lin (N45, W2042478072) | 2010 | primary empirical | 51.06% vs 51.56% male; HBV cannot explain China (OC-E1, OC-E2) | FULL-TEXT-CONFIRMED | verified | author's own | the update | SCORED 0 | claim withdrawn for China |
| strong | Das Gupta, PDR (N08, N46) | 2005, 2006 | primary empirical; reply | birth-order pattern implies sex selection | RECEPTION-CONFIRMED; LOCATED | verified | Oster reply (K4) not retrieved | UNASSESSED | not scored separately | most-cited node in RECEPTION-1 |
| moderate | Klasen, comments (X03) | 2005 | commentary | benchmark should vary with life expectancy (KL-E1) | FULL-TEXT-CONFIRMED | verified (comments on a draft) | life-expectancy controls in the target (JP-E6) | partly engaged | not scored separately | — |

SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING

64. Recurring authors: Oster on 3/49 RECEPTION-1 works (I03); Ebenstein (N02, N14, N32), Wei & Zhang (N10, N26) and Li (N07, N43) recur as independent R1 authors.
65–67. Venues, institutions, funding: not re-derived; UNASSESSED.
68. Dissent venues: AER (Lin & Luoh), PDR (Das Gupta), Economics Letters (Oster et al.), a medical journal (R03).
69–70. Gatekeeping and ideology: not assessable.

Closure type: no author, journal, funding or advocacy closure established; the reception is dominated by son-preference (R1) economics and demography.

SECTION J: FALSE-POSITIVE AND BASELINE CHECK

71. Small field: no (the economics and demography of sex ratios is large). 72. Baseline comparison: none built. 73. Adjacent expertise: the source pools medical studies and engages demography (JP-E1, JP-E4). 74. Only people studying the question: no. 75. Strong primary evidence: no; six small studies (JP-E2). 76. Repeated independent tests: yes; large tests with new data are null (I13, I14). 77. Limitations preserved: mostly, with minor certainty and mechanism drift (I10, I11). 78–80. Failed predictions acknowledged, critics engaged, updating: yes, by the author (I18).

Answers are mostly yes; this is not a cartel signature. The weak point is the paper's evidence base, not the network.

SECTION J2: THE CONCEDE TEST

| Finding | Declared target claim | Matches map field 6? | Same mechanism as another row? | Count separately? |
|---|---|---|---|---|
| 1 Decisive tests defeat L1 | field 6 via L1 | yes | no | yes |
| 2 Critique taken up; no closure | field 6 network support | yes | no | yes |
| 3 Certainty and mechanism drift | restatements of the target | no — MAP GAP: targets downstream restatements, not map field 6 | no | yes |
| 4 Post-refutation restatement | later use of the target | no — MAP GAP: targets downstream use, not map field 6 | no | yes |
| 5 Record quality | the OpenAlex record of the target | no — MAP GAP: targets the retrieval record, not map field 6 | no | yes |
| 6 Recent reception | field 6 network support | yes | no | yes |

| Finding | Concede test: SURVIVES / NARROWS / DEFEATS | Surviving claim if NARROWS |
|---|---|---|
| 1 | DEFEATS | — |
| 2 | SURVIVES | — |
| 3 | SURVIVES | — |
| 4 | SURVIVES | — |
| 5 | SURVIVES | — |
| 6 | SURVIVES | — |

| Finding | Scope-loss level | Original claim | Surviving claim | What epistemic or practical work is lost? |
|---|---|---|---|---|
| 1 | near-defeat | about 47% of missing women explained by HBV | none at field 6; the author's own test finds no carrier effect | the biological share of missing women |

Finding 1 DEFEATS field 6. Its failure location is the PAPER (six small pooled studies), not the citation network, which updated.

SECTION K0: EVIDENCE SUFFICIENCY LEDGER

Gate B was applied to every inference before any score or finding used it. Inferences that fail stay listed with what would make them sufficient.

INFERENCE LEDGER

| Inference | Class | Corpus | Claimed scope | Sampling rule | Members used | Disposition | Statement |
|---|---|---|---|---|---|---|---|
| I01 | GRAPH-STRUCTURE | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Directed internal density 134/2352 = 5.70% at work level (50/50 reference lists); no closed cluster inside RECEPTION-1. |
| I02 | GRAPH-STRUCTURE | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | In-degree leaders are critiques or rival studies (N08 23, N31 18, N01 15); Oster-authored works receive 16/134 internal edges, 10 to her null test N45. |
| I03 | DATABASE-RECORD | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | 3/49 works list Oster as author (N12, N24, N45); one work appears as two records (N09/N35); N19 and N44 are implausible citers. |
| I04 | GRAPH-STRUCTURE | RECENT-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | 1/6 recent citers cite an Oster-authored work beyond the target (R03 cites the 2010 null test); Lin & Luoh 1/6, Das Gupta 2005 2/6. |
| I05 | CITATION-USE | RECEPTION-1 | CORPUS | PRESPECIFIED-RANDOM | N07, N09, N10, N11, N20, N27, N28, N39, N40, N41, N42, N44 | INSUFFICIENT | How RECEPTION-1 uses the target cannot be estimated from the random sample: 3/12 sampled passages were inspectable (S2 contexts; no other authorized full text retrieved). Sufficient with all 12 passages. |
| I06 | CITATION-USE | RECEPTION-1 | WITHIN-SAMPLE | CONVENIENCE | N07, N11, N27 | SUPPORTED-WITHIN-SAMPLE | The three inspectable sampled passages: N07 QUALIFIES (notes the Das Gupta challenge), N11 and N27 MENTIONS (HBV listed as a partial factor). |
| I07 | CITATION-USE | RECEPTION-1 | WITHIN-SAMPLE | CONVENIENCE | N03, N04, N05, N07, N11, N12, N13, N15, N16, N17, N25, N27, N29, N31, N33, N34, N36, N37, N38, N45, N46, N48, N49, N50 | SUPPORTED-WITHIN-SAMPLE | Among 24 inspected passages: SUPPORTS 2, CHALLENGES 4, QUALIFIES 4, MENTIONS 14; no PREMISE or REUSES. |
| I08 | CITATION-USE | RECENT-1 | CORPUS | EXHAUSTIVE | ALL | INSUFFICIENT | How the recent census uses the target: 2/6 passages inspected (R01 implausible citer; R02, R05, R06 no context or text retrieved). Sufficient with all 6 passages. |
| I09 | CITATION-USE | RECENT-1 | WITHIN-SAMPLE | CONVENIENCE | R03, R04 | SUPPORTED-WITHIN-SAMPLE | R03 restates the target and tests it with new data (null, BA-E2); R04 restates the 2005 claim without the refutation (CTX-E25). |
| I10 | RESTATEMENT | — | NAMED | NOT-APPLICABLE | T01, N13 | SUPPORTED | N13 calls the target's pooled re-tabulation of earlier studies a confirmation (CTX-E8 vs JP-E2): certainty upgrade. |
| I11 | RESTATEMENT | — | NAMED | NOT-APPLICABLE | T01, N03 | SUPPORTED | N03 describes the target as finding more female-biased disease (CTX-E1); the target claims an offspring sex-ratio effect (JP-E2). |
| I12 | RESTATEMENT | — | NAMED | NOT-APPLICABLE | T01, N07, N11, N31, N46, R03, X02 | SUPPORTED | Restatements of the magnitude preserve it (JP-E3 vs CTX-E4, CTX-E5, CTX-E15, CTX-E21, BA-E1, SL-E1); none inflates it. |
| I13 | SOURCE-RESULT | — | NAMED | NOT-APPLICABLE | N31, N45, R03 | SUPPORTED | Three individual-level tests of L1 are null: Taiwan births (LL-E1), a Chinese cohort with 51.06% vs 51.56% male (OC-E1), Ghana mothers (BA-E2). |
| I14 | DATA-ORIGIN | — | NAMED | NOT-APPLICABLE | N31, N45, R03, T01 | SUPPORTED | The three null tests use data independent of the six family studies the target pools (JP-E2): Taiwan registry, Chinese cohort, Ghana hospital records. |
| I15 | COMPOSITION | ADJUDICATION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Relevance composition of the evidence base within the locked search (METADATA-coded). |
| I16 | COMPOSITION | ADJUDICATION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Contribution composition within the locked search (METADATA-coded). |
| I17 | COMPOSITION | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Relevance composition of the citing set; describes citers, not the evidence base. |
| I18 | ENGAGEMENT | — | NAMED | NOT-APPLICABLE | N45 | SUPPORTED | The target's author tests L1 on a large cohort and concludes HBV cannot explain China's male-biased sex ratios (OC-E1, OC-E2), citing Lin & Luoh. |
| I19 | ENGAGEMENT | — | NAMED | NOT-APPLICABLE | T01 | SUPPORTED | The target engages R1 (JP-E1), the F2 family studies (JP-E2) and the R4 benchmark debate (JP-E4, JP-E5, JP-E6). |
| I20 | CO-CITATION | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | 21/49 RECEPTION-1 works cite Lin & Luoh 2008 or Oster et al. 2010 (18/35 of those published 2009 or later); Das Gupta 2005 23/49. Co-citation, not use. |
| I21 | ENGAGEMENT | — | NAMED | NOT-APPLICABLE | — | NOT-ASSESSED | The author's uptake of the Das Gupta parity critique. Not assessed: the Oster reply (K4) was not retrieved; sufficient with its full text. |
| I22 | RESTATEMENT | — | NAMED | NOT-APPLICABLE | — | NOT-ASSESSED | Downstream reliance on review hubs (N21 Dyson, N13 James). Not assessed: no hub-citing passage was inspected; sufficient with inspected passages from a defined hub-citing set. |
| I23 | SOURCE-RESULT | — | NAMED | NOT-APPLICABLE | — | NOT-ASSESSED | Results of the other DIRECT (L1) members of ADJUDICATION-1 (A04, A07, A09). Not assessed: no authorized full text retrieved and abstracts not used; sufficient with their full texts. |
| I24 | DATABASE-RECORD | — | NAMED | NOT-APPLICABLE | T01 | SUPPORTED | The target OpenAlex record lists 318 referenced works and has a preprint duplicate (W3126094291); only 6 citers since 2021-11-05 against 172 in total. |
| I25 | CITATION-USE | — | NAMED | NOT-APPLICABLE | N36, N27, R04 | SUPPORTED | Three passages dated after the 2010 null test state the HBV effect without the refutation in the passage (CTX-E18, CTX-E13, CTX-E25). |

COMPOSITION: I15 | relevance | ADJACENT=18; BACKGROUND=4; DIRECT=17; UNRELATED=7 | TOTAL=46
COMPOSITION: I16 | contribution | COMMENTARY=1; INDEPENDENT-DATA=31; METHOD=1; NONE=8; REVIEW=4; THEORY=1 | TOTAL=46
COMPOSITION: I17 | relevance | ADJACENT=16; BACKGROUND=17; DIRECT=14; UNRELATED=2 | TOTAL=49

SAMPLE ATTRITION: I05 3/12

Sample record: ranks 7, 9, 10, 11, 20, 27, 28, 39, 40, 41, 42, 44 drawn with seed 20261105 (lock/SAMPLES_draw.txt); inspected N07, N11, N27; the N40 context did not show the citation; the other 8 had no context and no authorized full text retrieved.

Withheld inferences: I05 (INSUFFICIENT: sample attrition), I08 (INSUFFICIENT: 2/6 recent passages), I21, I22 and I23 (NOT-ASSESSED).

DIMENSION EVIDENCE BASIS

DIMENSION CLASS MAP: cn7-map-3

| Scorecard dimension | Scorecard disposition | Inference IDs | Basis note |
|---|---|---|---|
| Founding-cluster dominance | SCORED 0 | I02 (-), I03 (-) | critiques draw the most internal edges; Oster works 3/49 |
| Internal citation density | SCORED 0 | I01 (-) | 5.70% inside RECEPTION-1 only; closure not excluded beyond it |
| Recent-paper dependence | SCORED 0 | I04 (-), I09 (-), I08 (?) | 1/6 cite Oster work beyond the target (the null test); recent census 2/6 inspected |
| Review-hub laundering | UNASSESSED | — | I22 NOT-ASSESSED: no hub-citing passage inspected; sufficient with a defined hub-citing set |
| Proxy mismatch | UNASSESSED | — | not traced: carrier prevalence as a proxy for an offspring effect is a paper-level construct issue (Stage 2b); no restatement test run |
| Claim mutation | SCORED 1 | I10 (+), I11 (+), I12 (-) | minor certainty upgrade (N13) and mechanism misdescription (N03); magnitude preserved |
| Adjacent-field neglect | SCORED 0 | I19 (-) | source engages R1, F2 and R4 literatures |
| Lack of decisive tests | SCORED 0 | I13 (-), I14 (-), I23 (?) | three independent null tests of L1; other DIRECT (L1) results not read |
| Poor critique uptake | SCORED 0 | I18 (-), I21 (?) | the author tested and accepted the null; Das Gupta uptake not assessed |
| Intervention-evidence ratchet | N/A | — | no intervention claim at field 6 or in the traced network |
| Model non-updating | SCORED 0 | I18 (-) | four-link gate: links 1–3 met, link 4 not met; the author updated |

FINDING EVIDENCE BASIS

| Finding | Finding status | Inference IDs |
|---|---|---|
| Finding 1 | confirmed | I13, I14, I18 |
| Finding 2 | confirmed | I01, I02, I18, I20 |
| Finding 3 | confirmed | I10, I11, I12 |
| Finding 4 | provisional | I25, I09 |
| Finding 5 | confirmed | I24, I03 |
| Finding 6 | provisional | I04, I09, I08 |

SECTION K: CARTEL-RISK SCORING

Scores are in Artifact 8. All eight scored dimensions are INDEPENDENT: no two rest on the same passage. Founding-cluster dominance and internal density use the same RECEPTION-1 edge list but answer different questions (in-edge concentration and authorship records vs overall density).

- Verified risk score: 1/24
- Verified scored-dimension risk rate: 4.2
- Independent scored dimensions: 8
- Nested scored dimensions: 0
- Verified risk denominator: 24
- Evidentiary coverage: 8/10 applicable dimensions scored (80%)
- Execution completeness: 10/10 applicable dimensions completed (100%)
- Dimension inventory: 8 INDEPENDENT SCORED + 0 NESTED SCORED + 0 UNINFORMATIVE + 2 UNASSESSED + 1 N/A = 11 total dimensions; 10 applicable
- Unscored dimensions: Review-hub laundering — UNASSESSED (I22); Proxy mismatch — UNASSESSED (not traced); Intervention-evidence ratchet — N/A (no intervention claim)

Verified scored-dimension risk: 4.2%, calculated from 8 independent scored dimensions; 0 additional scored dimensions are NESTED; 8 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.

Formal-label gate: coverage 8/10 (80%) declared. Recent-paper dependence, adjacent-field neglect, lack of decisive tests and poor critique uptake carry open review items, so coverage is 4/10 (40%) if those items are withdrawn: the PROVISIONAL 70% gate (engineering threshold, not validated) is met only if the review items resolve. Label-essential check: the arithmetic position is the healthy/low-risk band, which needs affirmative no-concern evidence on closure-establishing dimensions; review-hub laundering is UNASSESSED and density is affirmative only inside a corpus selected on target citation. The band is withheld.

ARITHMETIC BAND POSITION: 0%–20% (healthy or low-risk network)
RISK BAND: WITHHELD — coverage meets the provisional 70% gate only if four review items resolve (40% without them), and the healthy band is label-essential on review-hub laundering (UNASSESSED) and on density beyond a target-selected corpus.
MECHANISM LABEL: an updating network around a defeated premise: the author and independent teams tested L1 with new data and found no effect; minor downstream certainty and mechanism drift; no closure signature inside RECEPTION-1

ARTIFACT 1: TOP 15 CITATION SPINE TABLE

| Rank | Paper | Year | Citation count | Evidence type | Role in network | Source of citation count |
|---:|---|---:|---:|---|---|---|
| 1 | N01 Nancy Qian: Missing Women and the Price of Tea in China: The Effect of Sex-Specifi (W2114978546) | 2008 | 876 | primary empirical study | ADJACENT (R1); CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 2 | N02 Avraham Y. Ebenstein: The "Missing Girls" of China and the Unintended Consequences of the On (W4234238734) | 2010 | 603 | primary empirical study | DIRECT (R1); CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 3 | N03 Silvia Barcellos, Leandro Carvalho, Adriana Lleras‐Muney: Child Gender and Parental Investments In India: Are Boys and Girls Tre (W2121199232) | 2013 | 327 | primary empirical study | BACKGROUND; MENTIONS | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 4 | N04 Siwan Anderson, Debraj Ray B: Missing Women: Age and Disease (W2026772829) | 2010 | 314 | primary empirical study | ADJACENT (L3); MENTIONS | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 5 | N05 Michael Andrew Clemens: THE MEANING OF FAILED REPLICATIONS: A REVIEW AND PROPOSAL (W2782446622) | 2015 | 245 | review article | ADJACENT; QUALIFIES | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 6 | N06 Donald Cox, Marcel Fafchamps A: Chapter 58 Extended Family and Kinship Networks: Economic Insights and (W3123575441) | 2007 | 236 | review article | BACKGROUND; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 7 | N07 Hongbin Li, Junjian Yi, Junsen Zhang: Estimating the Effect of the One-Child Policy on the Sex Ratio Imbalan (W2057390815) | 2011 | 225 | primary empirical study | DIRECT (R1); QUALIFIES | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 8 | N08 Mónica Das Gupta: Explaining Asia's “Missing Women”: A New Look at the Data (W1982754848) | 2005 | 214 | primary empirical study | DIRECT (R1); CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 9 | N09 Alma Cohen, Rajeev Dehejia, Dmitri Romanov: Financial Incentives and Fertility (W2125485011) | 2013 | 193 | primary empirical study | BACKGROUND; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 10 | N10 Shang‐Jin Wei, Xiaobo Zhang: The Competitive Saving Motive: Evidence from Rising Sex Ratios and Sav (W2123699796) | 2009 | 180 | primary empirical study | BACKGROUND; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 11 | N11 Jason I. Abrevaya: Are There Missing Girls in the United States? Evidence from Birth Data (W3122231766) | 2009 | 168 | primary empirical study | ADJACENT (R1); MENTIONS | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 12 | N12 Emily F. Oster: Does increased access increase equality? Gender and child health inves (W2096320699) | 2008 | 148 | primary empirical study | ADJACENT; SUPPORTS | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 13 | N13 William H. James: Evidence that mammalian sex ratios at birth are partially controlled b (W2030091805) | 2007 | 146 | review article | ADJACENT (L1); SUPPORTS | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 14 | N14 Avraham Y. Ebenstein: Estimating a Dynamic Model of Sex Selection in China (W1982250044) | 2011 | 141 | primary empirical study | DIRECT (R1); CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |
| 15 | N15 Sonia R. Bhalotra, Tom Cochrane: Where Have All the Young Girls Gone? Identification of Sex Selection i (W1593586622) | 2010 | 132 | primary empirical study | DIRECT (R1); QUALIFIES | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |

ARTIFACT 2: FOUNDING CLUSTER TABLE

| Paper | Year | Claim introduced | Evidence type | Verification state | Later role | Risk |
|---|---|---|---|---|---|---|
| Oster, Hepatitis B and the Case of the Missing Women (T01, W3123222584) | 2005 | HBV explains about 47% of missing women | secondary analysis | FULL-TEXT-CONFIRMED | canonical source; claim later withdrawn for China | high for field 6 (premise defeated), low for network closure |
| Drew et al., hepatitis B virus and sex ratio of offspring (X01) | 1978 | carrier families have more sons | primary empirical study | LOCATED | prior medical source pooled by the target | low |
| Oster, Chen, Yu & Lin (N45) | 2010 | no carrier effect in a Chinese cohort | primary empirical study | FULL-TEXT-CONFIRMED | the author's update | none |

ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE

"Cites founding cluster?" means an Oster-authored work beyond the target (all cite the target by construction). "Cites adjacent fields?" means Lin & Luoh 2008, Oster et al. 2010 or Das Gupta 2005/2006 in the OpenAlex reference list.

| Recent paper | Year | Verification state | Cites founding cluster? | Cites hub? | Cites adjacent fields? | New evidence or recycling? |
|---|---:|---|---|---|---|---|
| R01 The income inequality-CO2 emissions nexus: Transmission mechanisms (W4210337642) | 2022 | RECEPTION-CONFIRMED; LOCATED | target only | no | no | unrelated (implausible citer) |
| R02 Public pensions and family dynamics: Eldercare, child investment, and  (W4403727727) | 2024 | RECEPTION-CONFIRMED; LOCATED | target only | Das Gupta 2005 | Das Gupta 2005 | new evidence on another question (title) |
| R03 Maternal hepatitis B status and Sex at birth: A cross-sectional study  (W4397030871) | 2024 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED | yes (Oster et al. 2010 (N45)) | no | Oster et al. 2010 | new evidence: null test of L1 (BA-E2) |
| R04 The Estimation of the Number of Aborted Girls in South Korea (W4409543403) | 2025 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | target only | Das Gupta 2005 | Lin & Luoh 2008, Das Gupta 2005 | new estimate of missing girls; restates 2005 claim (CTX-E25) |
| R05 Essays on culture, institutions and comparative development (W4385446270) | 2023 | RECEPTION-CONFIRMED; LOCATED | target only | no | no | dissertation; not determined |
| R06 Dynamic general equilibrium models of the family, fertility, and healt (W4399729713) | 2023 | RECEPTION-CONFIRMED; LOCATED | target only | no | no | dissertation; not determined |

RECENT-1 summary: Oster work beyond target 1/6; Das Gupta 2005 2/6; Lin & Luoh 1/6; Oster et al. 2010 1/6.

ARTIFACT 4: CITATION POLARITY TABLE

| Citing paper | Cited paper | Verification state | Citation polarity | Claim use | Inflation risk |
|---|---|---|---|---|---|
| N03 W2121199232 Child Gender and Parental Investments In India:… (2013 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E1: lists Oster 2005 as "greater incidence of female-biased diseases" (mechanism misdescribed) | low |
| N04 W2026772829 Missing Women: Age and Disease (2010) | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E2: "a recent debate on the effect of Hepatitis B on sex ratios" (cites Lin & Luoh, Oster et al.); K7; POST HOC adju | none |
| N05 W2782446622 THE MEANING OF FAILED REPLICATIONS: A REVIEW AND… (201 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | qualifying | CTX-E3: Oster 2005 used as an example of critiques and replication (Das Gupta 2006; Lin & Luoh 2008; Oster et al. 2010) | none |
| N07 W2057390815 Estimating the Effect of the One-Child Policy on… (201 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | qualifying | CTX-E4: "raised the possibility" HBV accounts for "about 70%" of China's missing women; "Das Gupta (2005) questioned" | none |
| N11 W3122231766 Are There Missing Girls in the United States? Ev… (200 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E5, CTX-E6: HBV "can partly explain" high boy-birth shares; "around 75%" China vs "around 17%" India | none |
| N12 W2096320699 Does increased access increase equality? Gender… (2008 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | supportive | CTX-E7: author self-citation, HBV "responsible for around 20% of the (historical) gender imbalance in India" | none |
| N13 W2030091805 Evidence that mammalian sex ratios at birth are… (2007 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | supportive | CTX-E8: Chahnazarian et al. summarised the work "and the result confirmed by Oster (2005)" | moderate |
| N15 W1593586622 Where Have All the Young Girls Gone? Identificat… (201 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | qualifying | CTX-E9: HBV level hypothesis cited "although see Oster forthcoming"; trends rule out level explanations | none |
| N16 W1969182143 Son targeting fertility behavior: Some consequen… (201 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E10: rising SRB attributed to "biological factors, as Oster (…)" or to behaviour (passage truncated by S2) | none |
| N17 W3124330411 Chapter 52 Population Policies, Fertility, Women… (200 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E11: HBV "may offer a supplemental biological mechanism" for regional sex-ratio patterns | none |
| N25 W2023373624 Missing Girls in India: Infanticide, Feticide an… (200 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | critical | CTX-E12: the model "ignores the suggestion by Blumberg" that immunity moves the sex ratio the other way; also ADJUDICATI | none |
| N27 W1806205041 Why are adult women missing? Son preference and… (2018 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E13: "prevalence of Hepatitis B (Oster, 2005)" in a list of sex-ratio factors | low |
| N29 W2055080575 Sex ratios and the red dragon: using the Chinese… (200 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E14: results "not necessarily incompatible with the potential effect of the hepatitis B virus" | none |
| N31 W1994568240 Can Hepatitis B Mothers Account for the Number o… (200 | Oster 2005 | FULL-TEXT-CONFIRMED | critical | LL-E1 p. 1: effect "ranges only from 0.0010 to 0.0025"; LL-E2 p. 14: HBV has no effect on SRB; CTX-E15 restates "roughly | none |
| N33 W2161438007 Sex Selection and Gender Balance (2011) | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E16: "argument by Oster (2005) that hepatitis B infection raises the probability of having a boy" | none |
| N34 W2143614073 India's missing girls: biology, customs, and eco… (200 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E17: "Oster (2005) argues that hepatitis B may result in excessive male births" | none |
| N36 W1511329738 Son Preference in India: Implications for Gender… (201 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E18: Drew et al. and Oster "contend that medical studies indicate" HBV mothers have fewer girls (2015; no refutation | low |
| N37 W2079414367 How do sex ratios in China influence marriage de… (201 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E19: footnote list of sex-ratio studies incl. Oster 2005, Lin & Luoh 2008, Oster et al. 2008 | none |
| N38 W2074516985 Why weren't (many) European women ‘missing’? (2011) | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E20: whether there is "a biological dimension" (Das Gupta 2006; Oster 2005) | none |
| N45 W2042478072 Hepatitis B does not explain male-biased sex rat… (201 | Oster 2005 | FULL-TEXT-CONFIRMED | critical | OC-E1 p. 7: offspring of carrier vs non-carrier fathers 51.06% vs 51.56% male; OC-E2 p. 8: HBV carrier rates "cannot exp | none |
| N46 W2119714514 Cultural versus Biological Factors in Explaining… (200 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | critical | CTX-E21: restates "75 percent of the 'missing women' in China" before contesting it (title: Response to Oster); K5; POST | none |
| N48 W2081799904 Son Preference and Household Income in Rural Chi… (201 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E22: HBV "biological explanation" listed beside the socio-economic explanation | none |
| N49 W3124755079 Hidden consequences of a first-born boy for moth… (201 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | qualifying | CTX-E23: "her evidence, at least for China, has been widely criticized" | none |
| N50 W1976889960 Access to abortion, investments in neonatal heal… (201 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E24: Oster 2005 cited for Nepal being at risk of anti-girl bias | none |
| R03 W4397030871 Maternal hepatitis B status and Sex at birth: A… (2024 | Oster 2005 | FULL-TEXT-CONFIRMED | critical | BA-E1 §1: restates "about 75 %" China and "about 20 %" South Asia; BA-E2 §4: no association between maternal HBsAg and o | none |
| R04 W4409543403 The Estimation of the Number of Aborted Girls in… (202 | Oster 2005 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E25: Oster (2005) "reported that women infected with … HBV are more likely to give birth to boys" (2025; no refutati | low |
| X02 Slate 2005, "Where did 100 million missing women go?" (Landsburg) | Oster 2005 | FULL-TEXT-CONFIRMED | supportive | SL-E1: if the results are "extremely compelling", her work "has established the fate of roughly 50 million" missing wome | low |
| X03 Klasen 2005, "Comments on Paper by Emily Oster" (Göttingen working | Oster 2005 (draft) | FULL-TEXT-CONFIRMED | qualifying | KL-E1 p. 1: with a life-expectancy-adjusted SRB benchmark the total would "end up close to" Coale's 60 million | none |

Semantic Scholar contexts were used as EXCERPT access; CTX-E ids resolve to Semantic Scholar citation contexts (request /graph/v1/paper/DOI:10.1086/498588/citations?fields=title,externalIds,year,contexts,intents&limit=1000, 2026-11-05T10:26:46Z, HTTP 200, response sha256 c570ae9f4fa617d1b873a455054a752b97ab0077f77d1ce11ed3e83576d1c3c4; response not committed).

ARTIFACT 5: CLAIM MUTATION TABLE

| Original source | Original claim | Verification state | Hub restatement | Downstream restatement | Mutation severity |
|---|---|---|---|---|---|
| Oster 2005 p. 1201 (JP-E3) | about 47% of missing women; CI 13.5–71.5 | FULL-TEXT-CONFIRMED | none found | N07 "about 70%"; N31 roughly half; SL-E1 conditional 50 million | none |
| Oster 2005 p. 1179 (JP-E2) | pooled re-tabulation of six family studies | FULL-TEXT-CONFIRMED | none found | N13: "the result confirmed by Oster (2005)" | minor |
| Oster 2005 p. 1179 (JP-E2) | carriers have more sons | FULL-TEXT-CONFIRMED | none found | N03: "greater incidence of female-biased diseases" | minor |

ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE

Preregistration table as in SECTION E. POST HOC rows anchor no score.

| Claim layer | Adjacent field | Nominated source and stable identifier | Verification state | Source class: CONSTRUCT-DEFINING / MECHANISM-SUPPORTING / DIRECTLY-ADJUDICATING | Actual result | Explanation favored | Explanation weakened | Precise revision required | Pre-inspection lock status or POST HOC | Cited by dominant cluster? | Engagement quality | Effect of omission |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L2/L3 | F1 son preference | X04 W1992232430 | LOCATED | MECHANISM-SUPPORTING | BACKGROUND (off-topic labour paper) (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited | none |
| L2/L3 | F1 son preference | X05 W2139821597 | LOCATED | MECHANISM-SUPPORTING | son preference persistence (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited; R1 literature engaged via other works (JP-E1) | minor context loss |
| L2/L3 | F1 son preference | X06 W2074655452 | LOCATED | MECHANISM-SUPPORTING | sex composition and son preference, India (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited; R1 engaged via other works | minor context loss |
| L1 | F2 HBV and offspring sex | X01 W2023743440 | LOCATED | DIRECTLY-ADJUDICATING | carrier families have more sons: carriers' offspring male-biased, as tabulated in the target (JP-E2; source text not read) | L1 | R2 (at small-sample level) | none for L1 from this source alone; superseded by larger tests (I13) | LOCKED (Section E query) | yes (target) | substantively engaged (JP-E2) | none |
| L1 | F2 HBV and offspring sex | A06 W2129626017 | LOCATED | DIRECTLY-ADJUDICATING | four-population comparison: carriers' offspring male-biased, as tabulated in the target (JP-E2; source text not read) | L1 | R2 (at small-sample level) | none for L1 from this source alone; superseded by larger tests (I13) | LOCKED (Section E query) | yes (target) | substantively engaged (JP-E2) | none |
| L1 | F2 HBV and offspring sex | A03 W195581690 | LOCATED | DIRECTLY-ADJUDICATING | Greenland family study: carriers' offspring male-biased, as tabulated in the target (JP-E2; source text not read) | L1 | R2 (at small-sample level) | none for L1 from this source alone; superseded by larger tests (I13) | LOCKED (Section E query) | yes (target) | substantively engaged (JP-E2) | none |
| L3 | F3 sex ratio at birth | X07 W1973842394 | LOCATED | CONSTRUCT-DEFINING | animal sex-ratio biology (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited | none |
| L3 | F3 sex ratio at birth | X08 W2249723975 | LOCATED | CONSTRUCT-DEFINING | rising reported sex ratio in China; underreporting and sex selection (title; results not read) | — | — | — | LOCKED (Section E query) | yes (target) | directly engaged (JP-E1) | none |
| L3 | F3 sex ratio at birth | X09 W2083763800 | LOCATED | CONSTRUCT-DEFINING | hormonal hypothesis of sex ratios (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited (other James papers cited) | minor context loss |
| L3 | F4 missing women | X10 W2081758747 | LOCATED | CONSTRUCT-DEFINING | missing women revisited (title; results not read) | — | — | — | LOCKED (Section E query) | no | not cited (2002 update cited instead) | minor context loss |
| L3 | F4 missing women | X11 W3124113130 | LOCATED | CONSTRUCT-DEFINING | updated missing-women estimates (title; results not read) | — | — | — | LOCKED (Section E query) | yes (target) | substantively engaged (JP-E4) | none |
| L3 | F4 missing women | X12 W2031660749 | LOCATED | CONSTRUCT-DEFINING | missing women reconsidered, benchmark (title; results not read) | — | — | — | LOCKED (Section E query) | yes (target) | engaged; benchmark argument answered in part (JP-E5, JP-E6) | none |

ARTIFACT 7: CRITIQUE-UPTAKE TABLE

| Expected-production precondition | Critique / contrary evidence | Year | Source type | Main objection | Verification state | Reception opportunity | Cited by dominant cluster? | Uptake status | Dimension disposition | Effect on consensus |
|---|---|---|---|---|---|---|---|---|---|---|
| strong | Lin & Luoh, AER (N31, W1994568240) | 2008 | primary empirical | carrier effect near zero in Taiwan births (LL-E1, LL-E2) | FULL-TEXT-CONFIRMED | verified | yes (N45); 18/49 RECEPTION-1 | engaged and accepted by the author | SCORED 0 | refutation widely co-cited |
| strong | Oster, Chen, Yu & Lin (N45, W2042478072) | 2010 | primary empirical | 51.06% vs 51.56% male; HBV cannot explain China (OC-E1, OC-E2) | FULL-TEXT-CONFIRMED | verified | author's own | the update | SCORED 0 | claim withdrawn for China |
| strong | Das Gupta, PDR (N08, N46) | 2005, 2006 | primary empirical; reply | birth-order pattern implies sex selection | RECEPTION-CONFIRMED; LOCATED | verified | Oster reply (K4) not retrieved | UNASSESSED | not scored separately | most-cited node in RECEPTION-1 |
| moderate | Klasen, comments (X03) | 2005 | commentary | benchmark should vary with life expectancy (KL-E1) | FULL-TEXT-CONFIRMED | verified (comments on a draft) | life-expectancy controls in the target (JP-E6) | partly engaged | not scored separately | — |

ARTIFACT 8: CARTEL-RISK SCORECARD

| Dimension | Applicability | Dimension disposition | Score if SCORED | Evidence / claim state | Evidence supporting disposition and score | Evidence identifiers | Retrieval coverage | AGGREGATION STATUS | Independent evidence and inferential work, or nesting rationale | Reason excluded from denominator | Effect on formal-label gate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Founding-cluster dominance | applicable | SCORED 0 | 0 | RECEPTION-CONFIRMED | critiques lead in-degree; Oster works receive 16/134 edges; 3/49 Oster-authored | I02; I03 | 50/50 reference lists | INDEPENDENT | in-edge concentration and authorship | — | counts toward coverage |
| Internal citation density | applicable | SCORED 0 | 0 | RECEPTION-CONFIRMED | 134/2352 = 5.70% | I01 | 50/50 inputs | INDEPENDENT | overall density | — | affirmative inside RECEPTION-1 only |
| Recent-paper dependence | applicable | SCORED 0 | 0 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (2 passages) | 1/6 cite Oster work beyond target (the null test); R03 new data | I04; I09; I08 | 6/6 reference lists; 2/6 passages | INDEPENDENT | recent census distinct from RECEPTION-1 | — | counts toward coverage; under review |
| Review-hub laundering | applicable | UNASSESSED | — | — | downstream hub reliance not traced | I22 | 0 hub-citing passages | — | — | UNASSESSED | label-essential for the healthy band; band withheld |
| Proxy mismatch | applicable | UNASSESSED | — | — | not traced in the network | — | — | — | — | UNASSESSED | not label-essential |
| Claim mutation | applicable | SCORED 1 | 1 | FULL-TEXT-CONFIRMED (excerpts) | certainty upgrade (N13) and mechanism misdescription (N03); magnitude preserved | I10; I11; I12 | 24 RECEPTION-1 passages | INDEPENDENT | restatement passages | — | counts toward coverage |
| Adjacent-field neglect | applicable | SCORED 0 | 0 | FULL-TEXT-CONFIRMED | source engages R1, F2, R4 (JP-E1, JP-E2, JP-E4–E6) | I19 | source text | INDEPENDENT | source-layer engagement | — | counts toward coverage; under review |
| Lack of decisive tests | applicable | SCORED 0 | 0 | FULL-TEXT-CONFIRMED | three independent null tests of L1 (LL-E1, OC-E1, BA-E2) | I13; I14; I23 | ADJUDICATION-1 screened by title | INDEPENDENT | named test results on independent data | — | counts toward coverage; under review |
| Poor critique uptake | applicable | SCORED 0 | 0 | FULL-TEXT-CONFIRMED | the author tested and accepted the null (OC-E2) | I18; I21 | N45 full text | INDEPENDENT | engagement in the uptake population | — | counts toward coverage; under review |
| Intervention-evidence ratchet | not applicable | N/A | — | — | no intervention claim | — | — | — | — | N/A: no intervention claim | none |
| Model non-updating | applicable | SCORED 0 | 0 | FULL-TEXT-CONFIRMED | four-link gate: link 4 not met; the author updated | I18 | N45 full text | INDEPENDENT | updating test | — | counts toward coverage |

Verified risk score 1/24; rate 4.2%; independent 8; nested 0; denominator 24; coverage 8/10 (80%); completeness 10/10 (100%).

Verified scored-dimension risk: 4.2%, calculated from 8 independent scored dimensions; 0 additional scored dimensions are NESTED; 8 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.

ARTIFACT 9: NETWORK MAP

Receipts as in SECTION A (RECEPTION-1, 49 work nodes, 134 edges, density 134/2352, input coverage 50/50, COMPUTED-FROM-RETRIEVED). Closure beyond RECEPTION-1 is not established and not excluded.

Edge list (CSV, citing,cited):

```
source,target
N01,N31
N02,N08
N02,N31
N02,N45
N03,N01
N03,N04
N03,N12
N03,N15
N04,N08
N04,N11
N04,N24
N04,N31
N04,N45
N05,N31
N05,N45
N05,N46
N06,N08
N06,N39
N07,N01
N07,N02
N07,N08
N07,N31
N07,N45
N09,N02
N10,N08
N10,N14
N10,N20
N10,N31
N11,N30
N12,N24
N14,N01
N14,N02
N14,N08
N14,N11
N14,N31
N14,N47
N15,N02
N15,N03
N15,N08
N15,N11
N15,N24
N15,N30
N15,N33
N15,N34
N15,N45
N15,N47
N16,N34
N20,N01
N20,N08
N20,N10
N20,N31
N20,N45
N21,N04
N21,N08
N21,N11
N21,N33
N21,N45
N21,N46
N22,N01
N22,N02
N22,N08
N22,N31
N23,N01
N23,N02
N23,N08
N23,N29
N23,N31
N23,N43
N23,N47
N23,N50
N24,N01
N25,N08
N26,N08
N26,N10
N26,N14
N26,N20
N26,N31
N26,N43
N26,N45
N27,N01
N27,N03
N27,N04
N27,N08
N27,N11
N27,N15
N27,N24
N28,N08
N28,N11
N28,N24
N28,N31
N28,N45
N28,N46
N28,N47
N29,N01
N30,N11
N31,N01
N31,N08
N31,N45
N31,N46
N32,N01
N32,N02
N32,N08
N33,N01
N33,N04
N33,N11
N33,N31
N33,N34
N36,N08
N37,N01
N37,N08
N37,N29
N37,N31
N38,N08
N38,N11
N38,N46
N39,N06
N39,N08
N41,N01
N41,N03
N41,N15
N41,N31
N43,N31
N43,N47
N45,N08
N45,N31
N46,N08
N47,N01
N47,N04
N47,N14
N47,N31
N48,N20
N49,N39
N50,N15
N50,N47
```

COMPLETION LEDGER

| Required heading | Exact heading present? | Status: completed / N/A / omitted | Reason or output location |
|---|---|---|---|
| `PRE-AUDIT CLAIM CONFIRMATION` | yes | completed | this file |
| `SECTION A0: CORPUS REGISTER AND SOURCE ELIGIBILITY` | yes | completed | this file |
| `SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION` | yes | completed | this file |
| `SECTION B: EVIDENCE TYPE CODING` | yes | completed | this file |
| `SECTION C: CITATION POLARITY AND CLAIM USE` | yes | completed | this file |
| `SECTION D: CLAIM MUTATION TRACKING` | yes | completed | this file |
| `SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT` | yes | completed | this file |
| `SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING` | yes | completed | this file |
| `SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR` | yes | completed | this file |
| `SECTION H: IGNORED CRITIQUE AND NON-UPTAKE` | yes | completed | this file |
| `SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING` | yes | completed | this file |
| `SECTION J: FALSE-POSITIVE AND BASELINE CHECK` | yes | completed | this file |
| `SECTION J2: THE CONCEDE TEST` | yes | completed | this file |
| `SECTION K0: EVIDENCE SUFFICIENCY LEDGER` | yes | completed | this file |
| `SECTION K: CARTEL-RISK SCORING` | yes | completed | this file |
| `ARTIFACT 1: TOP 15 CITATION SPINE TABLE` | yes | completed | this file |
| `ARTIFACT 2: FOUNDING CLUSTER TABLE` | yes | completed | this file |
| `ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE` | yes | completed | this file |
| `ARTIFACT 4: CITATION POLARITY TABLE` | yes | completed | this file |
| `ARTIFACT 5: CLAIM MUTATION TABLE` | yes | completed | this file |
| `ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE` | yes | completed | this file |
| `ARTIFACT 7: CRITIQUE-UPTAKE TABLE` | yes | completed | this file |
| `ARTIFACT 8: CARTEL-RISK SCORECARD` | yes | completed | this file |
| `ARTIFACT 9: NETWORK MAP` | yes | completed | this file |
| `COMPLETION LEDGER` | yes | completed | this file |
| `ARTIFACT 10: FINAL VERDICT` | yes | completed | this file |
| `FINAL SECTION: STANDARDIZED FINDING TABLE` | yes | completed | this file |

Gate result: PASS.

ARTIFACT 10: FINAL VERDICT

- Main founding cluster: the target alone; Oster-authored works are 3/49 of RECEPTION-1 and include her own null test
- Main amplification hub: none found; the most-cited nodes inside RECEPTION-1 are critiques (Das Gupta 2005, Lin & Luoh 2008)
- Main proxy problem: not traced in the network (UNASSESSED); carrier prevalence standing in for an offspring effect is a paper-level issue
- Main adjacent fields neglected: none at the source layer (JP-E1, JP-E2, JP-E4–E6)
- Main claim mutation: minor certainty upgrade (N13) and mechanism misdescription (N03)
- Most important ignored critique: none ignored by the author; some later citers restate the HBV effect without the refutation (I25)
- Decisive test missing: none; three independent null tests of L1 exist (I13, I14). Results of other DIRECT (L1) studies were not read (I23)
- Verified risk score: 1/24
- Verified scored-dimension risk rate: 4.2
- Independent scored dimensions: 8
- Nested scored dimensions: 0
- Verified risk denominator: 24
- Evidentiary coverage: 8/10 (80%)
- Execution completeness: 10/10 (100%)
- Dimension inventory: 8 INDEPENDENT SCORED + 0 NESTED SCORED + 0 UNINFORMATIVE + 2 UNASSESSED + 1 N/A
- Unscored dimensions and reasons: Review-hub laundering UNASSESSED (I22); Proxy mismatch UNASSESSED (not traced); Intervention-evidence ratchet N/A
- N-of-M scope statement: Verified scored-dimension risk: 4.2%, calculated from 8 independent scored dimensions; 0 additional scored dimensions are NESTED; 8 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.
- Arithmetic band position: 0%–20% (healthy or low-risk network)
- Risk band: WITHHELD — coverage meets the provisional 70% gate only if four review items resolve (40% without them), and the healthy band is label-essential on review-hub laundering (UNASSESSED) and on density beyond a target-selected corpus.
- Mechanism label: an updating network around a defeated premise: the author and independent teams tested L1 with new data and found no effect; minor downstream certainty and mechanism drift; no closure signature inside RECEPTION-1
- Formal-label gate status: coverage 80% declared; 40% if open review items are withdrawn; MET ONLY IF REVIEW ITEMS RESOLVE (PROVISIONAL threshold); band withheld
- Load-bearing finding(s): Finding 1 (decisive tests defeat L1 and so field 6); its failure location is the PAPER
- Concede-test result: field 6 DEFEATED by Finding 1; Findings 2–6 SURVIVE
- Failure location: PAPER (Finding 1); CITATION (Findings 2, 3, 4, 6); MODEL-RETRIEVAL (Finding 5)
- Best formal label: insufficient evidence for a network label (low arithmetic; band withheld); no cartel signature; the network updated
- Confidence level: Low to moderate. CITATION CONTEXT COVERAGE: RECEPTION-1 24/49; CITATION CONTEXT COVERAGE: RECENT-1 2/6; CITATION CONTEXT COVERAGE: ADJUDICATION-1 2/46
- What evidence would change this assessment: full texts of the 9 unretrieved sampled RECEPTION-1 members; the Oster reply to Das Gupta; results of A04, A07, A09; inspected passages citing Dyson 2012; a seed-expanded comparison graph
- Density inference scope: RECEPTION-1 only (OpenAlex referenced_works:W3123222584, top 50 records, executed 2026-11-05T10:25:08Z); closure is not established and not excluded beyond the defined corpus

FINAL SECTION: STANDARDIZED FINDING TABLE

Finding 1

| Field | Entry |
|---|---|
| Finding | Three large individual-level tests on independent data, one co-written by the target's author, find no carrier effect, so L1 and with it field 6 fail. |
| Target claim | HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale's (1991) 60.26 million missing women in seven Asian/North-African units, mid-1980s (Table 11, Panel A). |
| What was measured | full texts of N31 (LL-E1, LL-E2), N45 (OC-E1, OC-E2), R03 (BA-E2) against JP-E2 and JP-E3 |
| What was claimed | independence and decisiveness of the tests of L1 |
| Failure mode | other: premise defeated by decisive tests |
| Severity | fatal-for-strong-claim |
| Concede test | DEFEATS |
| Scope loss if NARROWS | N/A — DEFEATS |
| Evidence | I13; I14; I18; LL-E1; OC-E1; OC-E2; BA-E2. |
| Evidence type | primary study |
| Verification state | FULL-TEXT-CONFIRMED; CROSS-SOURCE-CONFIRMED |
| Possible innocent explanation | The tests use Taiwan, China and Ghana samples; an effect confined to other populations or carrier types is not excluded. |
| What would weaken this | A large test with a carrier effect near 1.5, or evidence that the null tests mismeasure carrier status. |
| Failure location | PAPER — six small pooled studies |
| Status | confirmed |

Finding 2

| Field | Entry |
|---|---|
| Finding | Critiques are taken up: the author tested and accepted the null, the critiques are the most-cited nodes inside RECEPTION-1, and no closed cluster exists there. |
| Target claim | HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale's (1991) 60.26 million missing women in seven Asian/North-African units, mid-1980s (Table 11, Panel A). |
| What was measured | RECEPTION-1 edge list (50/50 reference lists); N45 full text |
| What was claimed | closure and critique non-uptake |
| Failure mode | none — acquittal on closure and uptake |
| Severity | none |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I01; I02; I18; I20; Section A receipts. |
| Evidence type | author inference |
| Verification state | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED |
| Possible innocent explanation | Not applicable to an acquittal; closure beyond the corpus is not excluded. |
| What would weaken this | A wider citing set where the HBV share is used as a premise without the refutation. |
| Failure location | CITATION — network structure and uptake |
| Status | confirmed |

Finding 3

| Field | Entry |
|---|---|
| Finding | Two downstream restatements drift: one calls the pooled re-tabulation a confirmation and one misdescribes the mechanism. |
| Target claim | MAP GAP: this finding targets downstream restatements of the target, not map field 6. |
| What was measured | S2 citation contexts CTX-E8 and CTX-E1 against JP-E2 |
| What was claimed | claim mutation |
| Failure mode | claim mutation |
| Severity | minor |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I10; I11; I12; CTX-E8; CTX-E1; JP-E2. |
| Evidence type | author inference |
| Verification state | FULL-TEXT-CONFIRMED |
| Possible innocent explanation | Excerpts are short; the surrounding text may qualify the wording. |
| What would weaken this | Full texts of N13 and N03 showing the qualification nearby. |
| Failure location | CITATION — downstream restatement |
| Status | confirmed |

Finding 4

| Field | Entry |
|---|---|
| Finding | Some passages written after the 2010 null test state the HBV effect without mentioning the refutation. |
| Target claim | MAP GAP: this finding targets downstream use of the target, not map field 6. |
| What was measured | S2 citation contexts CTX-E18 (2015), CTX-E13 (2018), CTX-E25 (2025) |
| What was claimed | critique uptake by later citers |
| Failure mode | critique non-uptake |
| Severity | minor |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I25; I09; CTX-E18; CTX-E13; CTX-E25. |
| Evidence type | author inference |
| Verification state | FULL-TEXT-CONFIRMED (excerpts); PROVISIONAL |
| Possible innocent explanation | The refutation may appear elsewhere in these works. |
| What would weaken this | Full texts showing each work cites and accepts the null tests. |
| Failure location | CITATION — later citers |
| Status | provisional |

Finding 5

| Field | Entry |
|---|---|
| Finding | The target's OpenAlex record is unreliable: 318 referenced works, a preprint duplicate, implausible citers and only 6 recent citers. |
| Target claim | MAP GAP: this finding targets the retrieval record of the target, not map field 6. |
| What was measured | raw/target_work.json, raw/target_dupes_search.json, raw/reception1_top50.json, raw/recent1_top25.json |
| What was claimed | database record quality |
| Failure mode | other: database record quality |
| Severity | moderate |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I24; I03; raw/target_work.json. |
| Evidence type | author inference |
| Verification state | RECEPTION-CONFIRMED |
| Possible innocent explanation | OpenAlex merges and links records automatically; errors are database-wide, not specific to this paper. |
| What would weaken this | A second database giving the same citer counts and reference list. |
| Failure location | MODEL-RETRIEVAL — database record |
| Status | confirmed |

Finding 6

| Field | Entry |
|---|---|
| Finding | Recent reception is small; one of six recent citers cites an Oster work beyond the target, and it is the null test. |
| Target claim | HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale's (1991) 60.26 million missing women in seven Asian/North-African units, mid-1980s (Table 11, Panel A). |
| What was measured | RECENT-1 reference lists (6/6); 2/6 passages |
| What was claimed | recent-paper dependence |
| Failure mode | none — provisional acquittal |
| Severity | none |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I04; I09; I08 (INSUFFICIENT). |
| Evidence type | author inference |
| Verification state | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (2 passages) |
| Possible innocent explanation | Not applicable to an acquittal. |
| What would weaken this | A fuller recent citing set from another database showing reliance on the 2005 share. |
| Failure location | CITATION — recent reception |
| Status | provisional |
