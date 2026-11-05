# Citation-Network Audit, v2-candidate diagnostic run — Acemoglu, Johnson & Robinson (2001)

INSTRUMENT PREFLIGHT: yungmulaBABY1/Provenance @ 07b72b585c934c5daff63953b22cf6424bfa8f6b : candidates/research-analysis/2-citation-network.v2-candidate.txt | sha256 3b4be80dcea68dc804bb6d72ca461a25f99a24f8bd8784e086289d9040f89896 | 1949 lines | 85977 bytes | identity CONFIRMED against the brief's pins (gate checker sha256 90de7375…, v1 checker sha256 f66650fe…, claim map sha256 f6e7df18…)

INSTRUMENT VERSION: 2-citation-network v2-candidate.2

DIMENSION CLASS MAP: cn7-map-2

Run metadata. DIAGNOSTIC LIVE RUN of citation-network candidate revision 2 (not a validation run). Executor: Grok Bot (audit run), branch audit/acemoglu-colonial-origins-v2cand created from b6d786947030902cf58cb114055d6cd48df6ad9c. Execution date 2026-11-04 PST (2026-11-05 UTC). Clock times are PST (UTC-8) with UTC in parentheses. Mode: full-sequence; upstream claim map examples/research/acemoglu-colonial-origins/01_claim_extraction.md (sha256 f6e7df18…, verified). Tools: OpenAlex works API (all corpora, graph, co-citation counts); publisher, repository, HAL, NBER and arXiv full texts; v1 full texts and evidence passages reused by sha256. Semantic Scholar was not called; no EXCERPT access was used. Recent window: 2021-11-04 to 2026-11-04.

VALIDATION BOUNDARY. This instrument revision is a candidate. It has not been validated for open retrieval. This run used open retrieval over three registered corpora (50 + 25 + 58 members). Every percentage, band and label below is an unvalidated open-retrieval application reported for diagnosis of the instrument, not as a validated verdict.

EXPOSURE DISCLOSURE (before SECTION A0). Before this run the executor had: produced the v1 citation-network output (02c_citation_network.md) and stages 01, 2a, 2b and 3 of this audit; read AJR (2001) and NBER WP 7771, Albouy (2012) and its revision appendix, the AJR (2012) Reply, the 2024 Nobel scientific and popular backgrounds, and the v1 full texts of Rodrik et al., Glaeser et al., Sachs, Easterly–Levine, the AJR handbook WP, Chernozhukov et al., Hanushek–Woessmann, Levine, Dell–Jones–Olken, Rajan–Zingales, Hidalgo et al. and Keller; and had seen the v1 RECENT top-25 titles before drawing the RECENT-1 sample. During identity checks (about 8:28 PM PST, 04:28 UTC) a grep for "FAIL-CN" was run on an older local clone's FAILURES.md (commit c1bcb8b); it showed only the FAIL-CN-001…006 headings and contains no FAIL-CN-007 entry. None of the brief's no-open files (tests/cases/citation-network-v2-gates/ and README, the candidate CHANGES file, the FAIL-CN-007 entry, the Provenance PR #14 description) was opened. Because of this exposure the Section E requirement to lock before bibliography inspection cannot be met by this auditor: the v1 locked query is reused and marked reused, and the new ADJUDICATION-1 search was locked before any of its results were screened.

PRE-AUDIT CLAIM CONFIRMATION

- Claim under audit (map field 6): In the base sample of 64 former colonies, the 2SLS estimate of the effect of the 1985–95 protection-against-expropriation index on 1995 log GDP per capita, instrumented by log settler mortality, is 0.94 (SE 0.16).
- What was literally measured (map field 1): 64 former colonies; 1995 log GDP per capita (PPP); PRS average protection-against-expropriation index 1985–95; log settler mortality; OLS and 2SLS (AJR 2001 Table 4).
- Weaker defensible claim (map field 3): in this sample with this instrument the coefficient is 0.94 (SE 0.16); causal and "institutions" readings are conditional on the exclusion restriction and on the index as a proxy; the implied 7-fold Nigeria–Chile gap is an upper bound in the authors' words.
- Target layer: field 6 for the network verdict; downstream layers are named as MAP GAP findings. Layer labels L1–L4 and rivals R1 (direct geography/disease) and R2 (settler human capital) are defined in the v1 output Section E, not in the claim map.

The map is upstream-generated, not self-generated.

SECTION A0: CORPUS REGISTER AND SOURCE ELIGIBILITY

Corpus planning. Questions: (a) how AJR 2001 is received (RECEPTION-1, RECENT-1); (b) what the evidence base testing field 6 and its rivals contains (ADJUDICATION-1). Proposed inferences were tested in SECTION K0 before use; those that fail stay there as INSUFFICIENT or NOT-ASSESSED.

CORPUS REGISTER

CORPUS ID: RECEPTION-1
CORPUS ROLE: RECEPTION
CORPUS QUESTION: How the most-cited works citing AJR 2001 relate to it and to each other.
CORPUS SELECTION RULE: OpenAlex works API, filter=cites:W3124166904, sort=cited_by_count:desc, per-page=50, page 1, queried 2026-11-04 8:29 PM PST (2026-11-05T04:29:45Z); no date or type bounds; no screening; dedupe by OpenAlex ID (none needed). Response raw/reception1_top50.json.
CORPUS DISCOVERY: NONE — top 50 citing works taken mechanically from the ranked query
SELECTED ON TARGET CITATION: YES
CORPUS SIZE: 50
CITATION CONTEXT COVERAGE: RECEPTION-1 14/50

CORPUS ID: RECENT-1
CORPUS ROLE: RECEPTION
CORPUS QUESTION: How recent (2021-11-04 onward) citing works use AJR 2001.
CORPUS SELECTION RULE: OpenAlex works API, filter=cites:W3124166904,from_publication_date:2021-11-04, sort=cited_by_count:desc, per-page=25; population count 3,026. Inspection sample: 6 members drawn with random.Random(20261104).sample(sorted IDs, 6), recorded in lock/RECENT-1_sample.txt at 8:33:36 PM PST (04:33:36Z) before any inspection. Response raw/recent1_top25.json.
CORPUS DISCOVERY: NONE — top 25 recent citing works taken mechanically
SELECTED ON TARGET CITATION: YES
CORPUS SIZE: 25
CITATION CONTEXT COVERAGE: RECENT-1 2/25

CORPUS ID: ADJUDICATION-1
CORPUS ROLE: ADJUDICATION
CORPUS QUESTION: What tests of field 6 (L1) and of the R1/R2 rivals to L3 exist, and what they find.
CORPUS SELECTION RULE: OpenAlex works API, six title_and_abstract.search queries Q1–Q6 (exact strings in lock/ADJUDICATION-1_search_record.md), publication 2001-01-01 to 2026-11-04, type article|preprint, relevance ranking, top 10 per query, dedupe by OpenAlex ID → 58 members; screening codes DIRECT (L1) / DIRECT (L3-R1) / DIRECT (L3-R2) / DIRECT (L3-noSM) / ADJACENT / BACKGROUND / UNRELATED / UNKNOWN from title and abstract.
CORPUS DISCOVERY: SEARCHED — lock/ADJUDICATION-1_search_record.md (raw/adj1_Q1..Q6.json)
SELECTED ON TARGET CITATION: NO
CORPUS SIZE: 58
CITATION CONTEXT COVERAGE: ADJUDICATION-1 1/58
CORPUS LOCK: 2026-11-04 8:30:42 PM PST (2026-11-05T04:30:42Z); search record sha256 05ae137a5db11167164e758a2228f8e176f470bc6575b1694ad0de6541f90916

Overlap. W2994756033 (Rodrik, Subramanian & Trebbi 2004; N02) is in RECEPTION-1 and ADJUDICATION-1 (search result ADJ29) and is recorded once with both corpus IDs; its reception rank does not weight its adjudication role. Duplicate database records of one work inside RECEPTION-1: Rodrik (N02, N32), Reversal of Fortune (N06, N18), AJR handbook (N09, N16), Levine finance survey (N05, N11); each record is a separate member, as the selection rule returned them.

Membership differences from v1 (queried 2026-11-04 3:42 AM PST, 11:42Z). RECEPTION-1: 12 new members (W3021593216, W3124948273, W2110434128, W3124568416, W2113844427, W3122300128, W3125412951, W2155346737, W2168966825, W1977433163, W4240669445, W3122357778); 12 v1 members absent (W2131499322, W3193006831, W2891433665, W2090766907, W3121532354, W3123773675, W2889827801, W2113596540, W3126058703, W1511665033, W2103130810, W2107205575). RECENT-1: added W4386028756, W4404201184, W4376140760; dropped W3211527536, W3124497653, W4200071543; population 2,695 → 3,026. The AJR 2001 OpenAlex record now lists 55 referenced works (v1: 13).

SOURCE ELIGIBILITY LEDGER

| Source | Corpus membership | Question relevance | Relation to target | Evidence contribution | Source access | Citation context | Supported inference |
|---|---|---|---|---|---|---|---|
| N01 W3124131699 The Colonial Origins of Comparative Development:… (2012) | RECEPTION-1 | DIRECT (L1) | SUPPORTS+REUSES | REANALYSIS | FULL-TEXT (AER 2012 Reply PDF; record conflated with AJR 2001) | INSPECTED | p. 3078: answers Albouy's two data objections and re-estimates on the same series |
| N02 W2994756033 Institutions Rule: The Primacy of Institutions O… (2002) | RECEPTION-1+ADJUDICATION-1 | DIRECT (L3-R1) | SUPPORTS+QUALIFIES+REUSES | REANALYSIS | FULL-TEXT (NBER WP 9305 version) | INSPECTED | RD-E1 p. 6 adopts the AJR instrument; RD-E4 p. 21 criticises the interpretive leap; also ADJ29 in ADJUDICATION-1 |
| N03 W3124948273 Law, Finance, and Economic Growth in China (2003) | RECEPTION-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; citation present in OpenAlex refs; relevance not coded |
| N04 W2890314743 Do Institutions Cause Growth? (2004) | RECEPTION-1 | DIRECT (L3-R2) | CHALLENGES+REUSES | REANALYSIS | FULL-TEXT (NBER WP 10568 version) | INSPECTED | GL-E1, GL-E2 p. 24: malaria and human-capital rival channels tested on AJR instruments |
| N05 W2113844427 Finance and Growth: Theory and Evidence (2004) | RECEPTION-1 | BACKGROUND | MENTIONS | REVIEW | FULL-TEXT (NBER WP 10766; this record is that WP) | INSPECTED | p. 90: AJR in a list on endowments and institutions |
| N06 W3125412951 Reversal of Fortune: Geography and Institutions… (2002) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: AJR-team Reversal of Fortune (QJE); citation present in OpenAlex refs, use not inspected |
| N07 W3122778615 The great reversals: the politics of financial d… (2003) | RECEPTION-1 | BACKGROUND | MENTIONS | INDEPENDENT-DATA | FULL-TEXT (NBER WP 8178 version) | INSPECTED | reference list (WP p. 46): no in-text passage located; cited in the bibliography only |
| N08 W3123436326 Double/debiased machine learning for treatment a… (2017) | RECEPTION-1 | ADJACENT | SUPPORTS+REUSES | METHOD | FULL-TEXT (arXiv 1608.00060 version) | INSPECTED | DML-E1 p. 45 reuses the 64 AJR observations; DML-E2 p. 46 compares with AJR Table 4 |
| N09 W2108614304 Institutions as the Fundamental Cause of Long-Ru… (2004) | RECEPTION-1 | ADJACENT | PREMISE+SUPPORTS | REVIEW | FULL-TEXT (NBER WP 10481; this record is that WP) | INSPECTED | HB-E1 p. 29 restates AJR 2001 magnitude; p. 28 premise for the synthesis |
| N10 W2556507681 The Theory of Economic Development (2016) | RECEPTION-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; citation present in OpenAlex refs; relevance not coded (book chapter; OpenAlex attribution of the AJR citation unverified) |
| N11 W1588189399 Chapter 12 Finance and Growth: Theory and Eviden… (2005) | RECEPTION-1 | BACKGROUND | MENTIONS | REVIEW | FULL-TEXT (NBER WP 10766 version of the chapter) | INSPECTED | p. 90 (WP version): same passage as N-Levine report; duplicate work |
| N12 W2064927380 The Product Space Conditions the Development of… (2007) | RECEPTION-1 | BACKGROUND | MENTIONS | INDEPENDENT-DATA | FULL-TEXT (arXiv 0708.2090 version) | INSPECTED | p. 2 and p. 6: numbered citation (12,13) in a background list on institutions |
| N13 W1484474409 Institutions and the Resource Curse (2006) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: institutions x resource curse; citation present in OpenAlex refs, use not inspected |
| N14 W3122300128 Financial accounting information and corporate g… (2001) | RECEPTION-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; citation present in OpenAlex refs; relevance not coded |
| N15 W4240669445 Unbundling Institutions (2005) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | SHARED-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: Acemoglu-Johnson; abstract: colonial-history variation (shared instrument family); citation present in OpenAlex refs, use not inspected |
| N16 W1580107285 Chapter 6 Institutions as a Fundamental Cause of… (2005) | RECEPTION-1 | ADJACENT | PREMISE+SUPPORTS | REVIEW | FULL-TEXT (NBER WP 10481 version; published chapter not retrieved) | INSPECTED | HB-E1 p. 29 (WP version); duplicate work of N-Handbook WP |
| N17 W1480274481 The Role of Cognitive Skills in Economic Develop… (2008) | RECEPTION-1 | ADJACENT | QUALIFIES | REVIEW | FULL-TEXT (NBER WP 12832 version) | INSPECTED | HW-E1 p. 44: AJR geography finding "remains a disputed subject" |
| N18 W3021593216 Reversal of Fortune: Geography and Institutions… (2001) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: AJR-team Reversal of Fortune (NBER record; duplicate work); citation present in OpenAlex refs, use not inspected |
| N19 W3125697804 International Technology Diffusion (2004) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | FULL-TEXT (NBER WP 8573, 2001 version) | VERSION-MISMATCH | retrieved 2001 WP does not contain the AJR citation; published 2004 version not retrieved |
| N20 W2148534039 Culture and Institutions: Economic Development i… (2010) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: culture and institutions, European regions; citation present in OpenAlex refs, use not inspected |
| N21 W3123261979 Natural Resources: Curse or Blessing? (2011) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: resource-curse survey; citation present in OpenAlex refs, use not inspected |
| N22 W2104834906 What Do We Learn from the Weather? The New Clima… (2014) | RECEPTION-1 | BACKGROUND | MENTIONS | REVIEW | FULL-TEXT (NBER WP 19578 version) | INSPECTED | p. 6: summarises the settler-mortality channel as background |
| N23 W2109890836 Temperature Shocks and Economic Growth: Evidence… (2012) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | FULL-TEXT (NBER WP 14132 version) | VERSION-MISMATCH | retrieved WP contains only an acknowledgment of Acemoglu, not the AJR 2001 citation |
| N24 W2145309110 The Slave Trade and the Origins of Mistrust in A… (2011) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: slave trade and mistrust; citation present in OpenAlex refs, use not inspected |
| N25 W3122513675 Tropics, germs, and crops: how endowments influe… (2003) | RECEPTION-1 | DIRECT (L3-R1) | SUPPORTS+REUSES | REANALYSIS | FULL-TEXT (NBER WP 9106 version) | INSPECTED | EL-E1 p. 2 no direct germ effect beyond institutions; EL-E2 p. 15 settler mortality data compiled by AJR |
| N26 W3122357778 The Rise of Europe: Atlantic Trade, Institutiona… (2005) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: AJR-team Rise of Europe; citation present in OpenAlex refs, use not inspected |
| N27 W1934649023 Governance Matters IV : Governance Indicators Fo… (2005) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: governance indicators dataset; citation present in OpenAlex refs, use not inspected |
| N28 W2155346737 The Real Exchange Rate and Economic Growth (2008) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: real exchange rate and growth; citation present in OpenAlex refs, use not inspected |
| N29 W2110434128 Corporate Governance, Economic Entrenchment and… (2004) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: corporate governance survey; citation present in OpenAlex refs, use not inspected |
| N30 W3125767605 Distance to Frontier, Selection, and Economic Gr… (2006) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | THEORY | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: Acemoglu-team growth model; citation present in OpenAlex refs, use not inspected |
| N31 W3023420463 Eight Questions about Corruption (2005) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: corruption survey; citation present in OpenAlex refs, use not inspected |
| N32 W1977433163 Institutions Rule: The Primacy of Institutions o… (2002) | RECEPTION-1 | DIRECT (L3-R1) | SUPPORTS+QUALIFIES+REUSES | REANALYSIS | FULL-TEXT (NBER WP 9305; this record is that WP) | INSPECTED | RD-E1 p. 6; p. 34 uses AJR 64-country sample; duplicate record of N02 |
| N33 W2789051288 The Origins of State Capacity: Property Rights,… (2009) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | THEORY | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: state capacity model; citation present in OpenAlex refs, use not inspected |
| N34 W4253884756 Civil War (2010) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: civil war survey; citation present in OpenAlex refs, use not inspected |
| N35 W3122513589 Cronyism and capital controls: evidence from Mal… (2002) | RECEPTION-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; citation present in OpenAlex refs; relevance not coded |
| N36 W2046507863 The economics of poverty traps and persistent po… (2006) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | THEORY | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: poverty traps; citation present in OpenAlex refs, use not inspected |
| N37 W3123293195 The Credibility Revolution in Empirical Economic… (2010) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | COMMENTARY | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: credibility revolution essay; citation present in OpenAlex refs, use not inspected |
| N38 W2150851272 1 Economic Geography and International Inequalit… (2010) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: economic geography rival (market access); citation present in OpenAlex refs, use not inspected |
| N39 W3121534672 Income and Democracy (2005) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: AJR-team income and democracy; citation present in OpenAlex refs, use not inspected |
| N40 W2591654989 Culture and Institutions (2015) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | REVIEW | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: culture and institutions review; citation present in OpenAlex refs, use not inspected |
| N41 W2123148076 What Is Quality of Government? A Theory of Impar… (2008) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | THEORY | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: quality of government; citation present in OpenAlex refs, use not inspected |
| N42 W3124753968 Institutional causes, macroeconomic symptoms: vo… (2003) | RECEPTION-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; citation present in OpenAlex refs; relevance not coded |
| N43 W2490362664 Fighting Poverty in the US and Europe (2004) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: redistribution US vs Europe; citation present in OpenAlex refs, use not inspected |
| N44 W2114854852 What Have We Learned About the Causes of Corrupt… (2007) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: causes of corruption review; citation present in OpenAlex refs, use not inspected |
| N45 W2891506482 Do better schools lead to more growth? Cognitive… (2012) | RECEPTION-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; citation present in OpenAlex refs; relevance not coded |
| N46 W3121354442 The Death Toll from Natural Disasters: The Role… (2005) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: disaster death toll; citation present in OpenAlex refs, use not inspected |
| N47 W3124568416 The Persistent Effects of Peru's Mining Mita (2010) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: within-country colonial institution (mita) RD design; citation present in OpenAlex refs, use not inspected |
| N48 W2168966825 Was Weber Wrong? A Human Capital Theory of Prote… (2007) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: Protestant human capital; citation present in OpenAlex refs, use not inspected |
| N49 W2152556759 Growth Dynamics: The Myth of Economic Recovery (2008) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: output loss after crises; citation present in OpenAlex refs, use not inspected |
| N50 W3125033761 Persistence of Power, Elites, and Institutions (2008) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | THEORY | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded: Acemoglu-Robinson persistence model; citation present in OpenAlex refs, use not inspected |
| R01 W4292849668 Digitalization and sustainable development: How… (2022) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | sampled; full text not retrieved (DOI HTTP 403); abstract-coded; uses AJR for another question; use not inspected |
| R02 W4212979054 On the role of domestic trade flows for estimati… (2022) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded; uses AJR for another question; use not inspected |
| R03 W3165371825 Does institutional quality foster economic compl… (2022) | RECENT-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; relevance not coded |
| R04 W4206178768 Institutional Quality and Education Quality in D… (2022) | RECENT-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; relevance not coded |
| R05 W4224261420 Women’s political empowerment and economic growt… (2022) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded; uses AJR for another question; use not inspected |
| R06 W4223529822 Land property rights and rural enterprise growth… (2022) | RECENT-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | sampled; full text not retrieved (DOI HTTP 403); metadata only; relevance not coded |
| R07 W4200480718 Do economic growth and institutional quality red… (2021) | RECENT-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; relevance not coded |
| R08 W4307547529 How Do Institutional Quality, Natural Resources,… (2022) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded; uses AJR for another question; use not inspected |
| R09 W4376140760 Institutions, trade, and development: identifyin… (2023) | RECENT-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded; uses AJR for another question; use not inspected |
| R10 W4319016949 Instrumental variables estimation: Assumptions,… (2023) | RECENT-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | sampled; full text not retrieved (repository HTTP 403, curl fallback 403); metadata only; relevance not coded |
| R11 W4285081985 Effects of income inequality and governance on e… (2022) | RECENT-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; relevance not coded |
| R12 W4386322040 RETRACTED: Country-level institutional quality a… (2023) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | RETRACTED article; abstract-coded; excluded from inference |
| R13 W4292663674 Informal institutions and international business… (2022) | RECENT-1 | BACKGROUND | MENTIONS | REVIEW | FULL-TEXT (Springer JIBS PDF) | INSPECTED | p. 8: AJR in a background list of institutional-theory works; p. 11; reference list p. 20 |
| R14 W4388274323 Cultural Origin and Minority Shareholder Expropr… (2023) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded; uses AJR for another question; use not inspected |
| R15 W4318937711 Climate risk, institutional quality, and total f… (2023) | RECENT-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; relevance not coded |
| R16 W4281705180 The effects of FDI on economic growth in Africa (2022) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded; uses AJR for another question; use not inspected |
| R17 W4404201184 E-invoicing, tax audits and VAT compliance (2024) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded; uses AJR for another question; use not inspected |
| R18 W4390870694 Aid effectiveness and donor motives (2024) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded; uses AJR for another question; use not inspected |
| R19 W4200592490 Can female entrepreneurs boost social mobility i… (2021) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded; uses AJR for another question; use not inspected |
| R20 W4386647200 The role of public environmental concern on corp… (2023) | RECENT-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; relevance not coded |
| R21 W4387877962 Regulatory issues inhibiting the financial inclu… (2023) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | sampled; full text not retrieved (repository HTTP 500 x3); abstract-coded; uses AJR for another question; use not inspected |
| R22 W4293403519 Effect of environmental regulation policy synerg… (2022) | RECENT-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; relevance not coded |
| R23 W4391180104 Technological innovation and its influence on en… (2024) | RECENT-1 | BACKGROUND | MENTIONS | INDEPENDENT-DATA | FULL-TEXT (HAL preprint version) | INSPECTED | p. 22, §4.3: cited as precedent for endogeneity; reference list p. 41 |
| R24 W3124943234 The standard errors of persistence (2024) | RECENT-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | metadata only; relevance not coded |
| R25 W4386028756 Institutional quality and economic growth in Sub… (2023) | RECENT-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | abstract-coded; uses AJR for another question; use not inspected |
| ADJ01 W7167818940 Colonial Origins, Revisited Line by Line: A Comp… (2026) | ADJUDICATION-1 | DIRECT (L1) | UNKNOWN | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q1; screened DIRECT (L1); unreviewed Zenodo deposit; AR sets [0.71, 1.43] at baseline, unbounded under Albouy revisions |
| ADJ02 W7110560615 The Colonial Origins of Comparative Development:… (2007) | ADJUDICATION-1 | DIRECT (L1) | UNKNOWN | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q1+Q2; screened DIRECT (L1); Auer comment: settler-mortality data dispute |
| ADJ03 W140439859 A Response to Albouy's "A Reexamination Based on… (2005) | ADJUDICATION-1 | DIRECT (L1) | CITES-UNINSPECTED | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q1; screened DIRECT (L1); AJR 2005 response to Albouy |
| ADJ04 W2047459800 Poverty and Civil War: Revisiting the Evidence (2010) | ADJUDICATION-1 | BACKGROUND | CITES-UNINSPECTED | NONE | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q1; screened BACKGROUND |
| ADJ05 W2612901723 Revisiting the effect of colonial institutions o… (2017) | ADJUDICATION-1 | DIRECT (L1) | CITES-UNINSPECTED | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q1; screened DIRECT (L1); Assenova-Regele revisit colonial-institutions effect |
| ADJ06 W1578613673 Unbundling Ex-Colonies:A Comment on Acemoglu, Jo… (2004) | ADJUDICATION-1 | DIRECT (L1) | UNKNOWN | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q1; screened DIRECT (L1); Olsson comment on AJR |
| ADJ07 W7214121527 Causal Evidence on Institutions and Economic Dev… (2026) | ADJUDICATION-1 | DIRECT (L1) | CITES-UNINSPECTED | REANALYSIS | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q1; screened DIRECT (L1); title only: replication of institutions-development evidence |
| ADJ08 W4285097130 Does colonisation explain the low level of growt… (2022) | ADJUDICATION-1 | BACKGROUND | CITES-UNINSPECTED | NONE | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q1; screened BACKGROUND |
| ADJ09 W2945529632 Geography matters: Reconsidering the effect of g… (2008) | ADJUDICATION-1 | DIRECT (L3-R1) | CITES-UNINSPECTED | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q1+Q2; screened DIRECT (L3-R1); Bleaney-Dimico: geography matters |
| ADJ10 W3153282027 Did colonisation matter for comparative economic… (2021) | ADJUDICATION-1 | BACKGROUND | CITES-UNINSPECTED | NONE | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q1; screened BACKGROUND |
| ADJ11 W1589075589 The Colonial Origins of Comparative Development:… (2007) | ADJUDICATION-1 | DIRECT (L1) | UNKNOWN | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q2; screened DIRECT (L1); Auer: second record of the same comment |
| ADJ12 W3142281781 The Role of Historical Malaria in Institutions a… (2022) | ADJUDICATION-1 | DIRECT (L3-noSM) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q2; screened DIRECT (L3-noSM); title only: historical malaria and institutions |
| ADJ13 W1536671217 Geography vs. Institutions at the Village Level (2008) | ADJUDICATION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q2; screened ADJACENT |
| ADJ14 W7137625625 The Role of Historical Malaria in Institutions a… (2021) | ADJUDICATION-1 | DIRECT (L3-noSM) | UNKNOWN | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q2; screened DIRECT (L3-noSM); historical malaria instrument (dissertation) |
| ADJ15 W2123048668 Geographical Influences on Long-Run Development (2010) | ADJUDICATION-1 | DIRECT (L3-R1) | CITES-UNINSPECTED | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q2; screened DIRECT (L3-R1); Bleaney-Dimico: geographical influences |
| ADJ16 W2086477250 The effects of policy, institutions and geograph… (2004) | ADJUDICATION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q2; screened ADJACENT |
| ADJ17 W3161497846 Alternative Variables for Geography and Institut… (2020) | ADJUDICATION-1 | DIRECT (L3-R1) | UNKNOWN | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q2; screened DIRECT (L3-R1); alternative geography and institution variables |
| ADJ18 W1978529482 Root Causes of African Underdevelopment (2009) | ADJUDICATION-1 | DIRECT (L3-R1) | CITES-UNINSPECTED | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q2; screened DIRECT (L3-R1); Bhattacharyya: malaria matters for African underdevelopment |
| ADJ19 W4381428985 Colonial origins and quality of education eviden… (2023) | ADJUDICATION-1 | ADJACENT | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q3; screened ADJACENT; OpenAlex refs (n=39) omit AJR 2001 |
| ADJ20 W4292553381 Colonial Origins of Comparative Development in G… (2022) | ADJUDICATION-1 | ADJACENT | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q3; screened ADJACENT; OpenAlex refs (n=26) omit AJR 2001 |
| ADJ21 W4213324825 Colonial origin, ethnicity and intergenerational… (2022) | ADJUDICATION-1 | BACKGROUND | CITES-UNINSPECTED | NONE | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; screened BACKGROUND |
| ADJ22 W2600922460 The effects of colonial origin on economic growt… (2016) | ADJUDICATION-1 | ADJACENT | UNKNOWN | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q3; screened ADJACENT |
| ADJ23 W1977418886 Human Capital and Systems of Innovation in Afric… (2004) | ADJUDICATION-1 | ADJACENT | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q3; screened ADJACENT; OpenAlex refs (n=41) omit AJR 2001 |
| ADJ24 W2802938645 Colonial Origins and Comparative Development: In… (2017) | ADJUDICATION-1 | DIRECT (L3-R1) | UNKNOWN | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q3; screened DIRECT (L3-R1); Chakraborty: institutions matter |
| ADJ25 W4391339197 Quality and Equity in Cameroon's Primary Educati… (2024) | ADJUDICATION-1 | BACKGROUND | UNKNOWN | NONE | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; screened BACKGROUND |
| ADJ26 W192439523 Caribbean History: From Pre-Colonial Origins to… (2013) | ADJUDICATION-1 | UNRELATED | UNKNOWN | NONE | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q3; screened UNRELATED |
| ADJ27 W4226031116 Colonial Origins and Fertility: Can the Market O… (2022) | ADJUDICATION-1 | BACKGROUND | CITES-UNINSPECTED | NONE | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; screened BACKGROUND |
| ADJ28 W7155374057 Colonial origins and child poverty inequalities… (2026) | ADJUDICATION-1 | BACKGROUND | UNKNOWN | NONE | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q3; screened BACKGROUND |
| ADJ30 W3124718896 Institutions Rule; The Primacy of Institutions o… (2002) | ADJUDICATION-1 | DIRECT (L3-R1) | UNKNOWN | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q4; screened DIRECT (L3-R1); IMF/NBER record of Institutions Rule |
| ADJ31 W3123032229 Institutions Rule (2002) | ADJUDICATION-1 | DIRECT (L3-R1) | CITES-UNINSPECTED | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q4; screened DIRECT (L3-R1); IMF WP record of Institutions Rule |
| ADJ32 W1988424882 Deep determinants of economic growth: institutio… (2004) | ADJUDICATION-1 | ADJACENT | CITES-UNINSPECTED | REVIEW | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q4; screened ADJACENT |
| ADJ33 W1529198445 Do Institutions Rule? The Role of Heterogeneity… (2009) | ADJUDICATION-1 | DIRECT (L3-R1) | UNKNOWN | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q4; screened DIRECT (L3-R1); Kourtellos et al.: heterogeneity in institutions vs geography |
| ADJ34 W4296052492 Institutions Rule in Export Diversity (2022) | ADJUDICATION-1 | BACKGROUND | CITES-UNINSPECTED | NONE | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q4; screened BACKGROUND |
| ADJ35 W144118490 The Primacy of Institutions (and what this does… (2013) | ADJUDICATION-1 | ADJACENT | CITES-UNINSPECTED | COMMENTARY | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q4; screened ADJACENT |
| ADJ36 W2566351377 The Primacy of Institutions Reconsidered (2012) | ADJUDICATION-1 | DIRECT (L3-R1) | UNKNOWN | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q4; screened DIRECT (L3-R1); Carstensen-Gundlach 2012 record |
| ADJ37 W2052626067 Economic development and the geography of instit… (2006) | ADJUDICATION-1 | UNKNOWN | CITES-UNINSPECTED | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | Q4; screened UNKNOWN |
| ADJ38 W2001123479 The Primacy of Institutions Reconsidered: Direct… (2006) | ADJUDICATION-1 | DIRECT (L3-R1) | CITES-UNINSPECTED | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q4; screened DIRECT (L3-R1); Carstensen-Gundlach: direct income effects of malaria |
| ADJ39 W4407425804 Distributional Instrumental Variable Method (2025) | ADJUDICATION-1 | DIRECT (L1) | UNKNOWN | METHOD | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q5; screened DIRECT (L1); distributional IV method; AJR application |
| ADJ40 W3022286213 Does graduate human capital production increase… (2020) | ADJUDICATION-1 | UNRELATED | NOT-CITING | NONE | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q5; screened UNRELATED; OpenAlex refs (n=94) omit AJR 2001 |
| ADJ41 W7162082492 Bayesian Model Averaging in Causal Instrumental… (2026) | ADJUDICATION-1 | DIRECT (L3-R1) | UNKNOWN | METHOD | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q5; screened DIRECT (L3-R1); BMA for IV; malaria-institutions application |
| ADJ42 W7161015320 The security of property rights and subjective w… (2026) | ADJUDICATION-1 | BACKGROUND | NOT-CITING | NONE | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q5; screened BACKGROUND; OpenAlex refs (n=1) omit AJR 2001 |
| ADJ43 W2069316799 Institutions and geography as sources of economi… (2005) | ADJUDICATION-1 | DIRECT (L3-R1) | CITES-UNINSPECTED | REANALYSIS | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q5; screened DIRECT (L3-R1); Presbitero: institutions and geography |
| ADJ44 W3127103038 Machine Learning Indices, Political Institutions… (2018) | ADJUDICATION-1 | UNKNOWN | UNKNOWN | UNKNOWN | METADATA (OpenAlex record) | NOT-INSPECTED | Q5; screened UNKNOWN |
| ADJ45 W4323897988 The Effects of Institutions on Economic Developm… (2022) | ADJUDICATION-1 | ADJACENT | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q5; screened ADJACENT; OpenAlex refs (n=48) omit AJR 2001 |
| ADJ46 W2231632438 On the determinants of life insurance developmen… (2015) | ADJUDICATION-1 | BACKGROUND | NOT-CITING | NONE | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q5; screened BACKGROUND; OpenAlex refs (n=32) omit AJR 2001 |
| ADJ47 W7168135264 Why Does Individualism Affect Economic Developme… (2026) | ADJUDICATION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q5; screened ADJACENT |
| ADJ48 W2001270353 Technology Trade in Economic Development (2007) | ADJUDICATION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q5; screened ADJACENT |
| ADJ49 W3119817639 Rule of law, democracy, openness, and income (2005) | ADJUDICATION-1 | DIRECT (L3-noSM) | CITES-UNINSPECTED | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q6; screened DIRECT (L3-noSM); Rigobon-Rodrik: identification through heteroskedasticity |
| ADJ50 W2925821398 Impact of Institutional Quality on Financial Dev… (2019) | ADJUDICATION-1 | BACKGROUND | NOT-CITING | NONE | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q6; screened BACKGROUND; OpenAlex refs (n=72) omit AJR 2001 |
| ADJ51 W1560261142 Income Growth and Institutional Quality: Evidenc… (2012) | ADJUDICATION-1 | ADJACENT | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q6; screened ADJACENT; OpenAlex refs (n=18) omit AJR 2001 |
| ADJ52 W1488479141 Property Rights Reform and Development: A Critiq… (2022) | ADJUDICATION-1 | ADJACENT | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q6; screened ADJACENT; OpenAlex refs (n=43) omit AJR 2001 |
| ADJ53 W2143392786 Institutions and Economic Growth: A Cross Countr… (2009) | ADJUDICATION-1 | ADJACENT | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q6; screened ADJACENT; OpenAlex refs (n=62) omit AJR 2001 |
| ADJ54 W1809608383 Institutions and Economic Growth: Empirical Evid… (2001) | ADJUDICATION-1 | ADJACENT | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q6; screened ADJACENT; OpenAlex refs (n=24) omit AJR 2001 |
| ADJ55 W7168616766 Institutional quality and pandemic resilience: c… (2026) | ADJUDICATION-1 | BACKGROUND | CITES-UNINSPECTED | NONE | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q6; screened BACKGROUND |
| ADJ56 W4365447584 Corruption Control, Financial Development, and G… (2023) | ADJUDICATION-1 | BACKGROUND | NOT-CITING | NONE | ABSTRACT (OpenAlex abstract) | NOT-APPLICABLE | Q6; screened BACKGROUND; OpenAlex refs (n=42) omit AJR 2001 |
| ADJ57 W7165369567 Remittances and National Peace: The Conditional… (2026) | ADJUDICATION-1 | BACKGROUND | CITES-UNINSPECTED | NONE | ABSTRACT (OpenAlex abstract) | NOT-INSPECTED | Q6; screened BACKGROUND |
| ADJ58 W4206624208 Does institutional quality affect air pollution? (2022) | ADJUDICATION-1 | BACKGROUND | CITES-UNINSPECTED | NONE | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q6; screened BACKGROUND |
| X01 W3124166904 AJR 2001 Colonial Origins (target) | OUTSIDE | DIRECT (L1) | NOT-CITING | INDEPENDENT-DATA | FULL-TEXT (AER 2001 PDF) | NOT-APPLICABLE | target source; AJR-E2 p. 20, AJR-E4 p. 24 used as source passages |
| X02 W1969918011 Albouy 2012 AER Comment | OUTSIDE | DIRECT (L1) | CHALLENGES | REANALYSIS | FULL-TEXT (JSTOR mirror PDF) | INSPECTED | p. 3060: mortality rates for many of the 64 countries argued non-comparable |
| X03 NBER w9490 Sachs 2003 Institutions don't rule | OUTSIDE | DIRECT (L3-R1) | CHALLENGES | REANALYSIS | FULL-TEXT (NBER WP 9490) | INSPECTED | SA-E1 p. 10: AJR-style null rejected using malaria risk |
| X04 Nobel 2024 scientific background | OUTSIDE | ADJACENT | QUALIFIES | REVIEW | FULL-TEXT (nobelprize.org PDF) | INSPECTED | NS-E1, NS-E2, NS-E3 p. 19: grain of salt; Albouy; human capital hard to distinguish |
| X05 Nobel 2024 popular background | OUTSIDE | ADJACENT | SUPPORTS | COMMENTARY | FULL-TEXT (nobelprize.org PDF) | INSPECTED | NP-E1 p. 4: "a clear chain of causality" |
| X06 W139828295 Malawi household malaria cost (1994) | OUTSIDE | ADJACENT | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (v1 reused) | NOT-APPLICABLE | v1 Section E locked source F1; predates target |
| X07 W2088758477 Gambia malaria risk factors (1995) | OUTSIDE | ADJACENT | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (v1 reused) | NOT-APPLICABLE | v1 Section E locked source F1; predates target |
| X08 W2618788771 Gallup, Sachs & Mellinger (1999) | OUTSIDE | ADJACENT | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (v1 reused) | NOT-APPLICABLE | v1 Section E locked source F2; predates target |
| X09 W1492460295 Development, geography, and economic theory | OUTSIDE | ADJACENT | UNKNOWN | THEORY | ABSTRACT (v1 reused) | NOT-INSPECTED | v1 Section E locked source F2; date not re-verified |
| X10 W3121822366 Becker, Murphy & Tamura (1990) | OUTSIDE | ADJACENT | NOT-CITING | THEORY | ABSTRACT (v1 reused) | NOT-APPLICABLE | v1 Section E locked source F3; predates target |
| X11 W2035652178 Glomm & Ravikumar (1992) | OUTSIDE | ADJACENT | NOT-CITING | THEORY | ABSTRACT (v1 reused) | NOT-APPLICABLE | v1 Section E locked source F3; predates target |
| X12 W2165144879 Staiger & Stock (1997) | OUTSIDE | ADJACENT | NOT-CITING | METHOD | ABSTRACT (v1 reused) | NOT-APPLICABLE | v1 Section E locked source F4; predates target |
| X13 W1980412904 Bound, Jaeger & Baker (1995) | OUTSIDE | ADJACENT | NOT-CITING | METHOD | ABSTRACT (v1 reused) | NOT-APPLICABLE | v1 Section E locked source F4; predates target |
| X14 W3121147769 North (1990) record, mis-typed | OUTSIDE | BACKGROUND | NOT-CITING | THEORY | ABSTRACT (v1 reused) | NOT-APPLICABLE | v1 Section E locked source F6; predates target |
| X15 W2010235856 Knack & Keefer (1995) | OUTSIDE | ADJACENT | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (v1 reused) | NOT-APPLICABLE | v1 Section E locked source F6; source of the PRS data; predates target |

Coding notes. Relation for ADJUDICATION-1: OpenAlex reference list contains W3124166904 → CITES-UNINSPECTED; reference list empty → UNKNOWN; non-empty list without AJR → NOT-CITING (NOT-APPLICABLE), except DIRECT members and abstracts naming AJR, which stay UNKNOWN because OpenAlex reference lists are incomplete. Relevance and contribution were coded from abstracts; rows marked "title-coded from METADATA" were coded from the title alone. A working-paper version was accepted as the inspected version when it contains the citation; otherwise the row is VERSION-MISMATCH.

SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION

GRAPH CORPUS AND RECEIPTS

GRAPH CORPUS DEFINITION: RECEPTION-1 as registered in SECTION A0 (OpenAlex, filter=cites:W3124166904, sort=cited_by_count:desc, top 50, queried 2026-11-05T04:29:45Z UTC = 8:29 PM PST Nov 4, no date or type bounds, no screening, dedupe by OpenAlex ID, inclusion = all 50 returned, exclusion = none). Target W3124166904 is outside the density corpus; the 50 citer -> target edges hold by construction and are not counted.
GRAPH CORPUS NODE LIST: N01=W3124131699; N02=W2994756033; N03=W3124948273; N04=W2890314743; N05=W2113844427; N06=W3125412951; N07=W3122778615; N08=W3123436326; N09=W2108614304; N10=W2556507681; N11=W1588189399; N12=W2064927380; N13=W1484474409; N14=W3122300128; N15=W4240669445; N16=W1580107285; N17=W1480274481; N18=W3021593216; N19=W3125697804; N20=W2148534039; N21=W3123261979; N22=W2104834906; N23=W2109890836; N24=W2145309110; N25=W3122513675; N26=W3122357778; N27=W1934649023; N28=W2155346737; N29=W2110434128; N30=W3125767605; N31=W3023420463; N32=W1977433163; N33=W2789051288; N34=W4253884756; N35=W3122513589; N36=W2046507863; N37=W3123293195; N38=W2150851272; N39=W3121534672; N40=W2591654989; N41=W2123148076; N42=W3124753968; N43=W2490362664; N44=W2114854852; N45=W2891506482; N46=W3121354442; N47=W3124568416; N48=W2168966825; N49=W2152556759; N50=W3125033761
INTERNAL EDGE LIST: N01 -> N06; N01 -> N07; N01 -> N35; N01 -> N19; N01 -> N42; N01 -> N25; N01 -> N38; N01 -> N13; N01 -> N30; N02 -> N01; N02 -> N06; N02 -> N42; N02 -> N18; N02 -> N25; N03 -> N01; N04 -> N01; N04 -> N06; N04 -> N02; N04 -> N32; N04 -> N18; N04 -> N25; N05 -> N29; N05 -> N01; N05 -> N25; N05 -> N03; N05 -> N30; N06 -> N18; N07 -> N01; N09 -> N01; N09 -> N06; N09 -> N18; N09 -> N05; N09 -> N42; N09 -> N26; N09 -> N30; N10 -> N01; N10 -> N27; N11 -> N29; N11 -> N01; N11 -> N05; N11 -> N25; N11 -> N03; N11 -> N30; N12 -> N01; N13 -> N01; N15 -> N06; N15 -> N07; N15 -> N42; N16 -> N01; N16 -> N06; N16 -> N18; N16 -> N05; N16 -> N42; N16 -> N26; N17 -> N01; N17 -> N06; N17 -> N45; N17 -> N18; N17 -> N09; N18 -> N01; N20 -> N01; N20 -> N04; N20 -> N50; N20 -> N42; N20 -> N25; N20 -> N26; N20 -> N02; N21 -> N01; N21 -> N33; N21 -> N04; N21 -> N42; N21 -> N25; N21 -> N02; N21 -> N13; N22 -> N01; N22 -> N23; N22 -> N02; N23 -> N01; N23 -> N06; N23 -> N02; N23 -> N22; N23 -> N18; N24 -> N01; N24 -> N06; N24 -> N18; N24 -> N20; N25 -> N01; N25 -> N06; N26 -> N01; N26 -> N06; N26 -> N50; N26 -> N18; N26 -> N39; N27 -> N02; N27 -> N32; N27 -> N04; N28 -> N01; N28 -> N02; N28 -> N32; N29 -> N01; N29 -> N06; N29 -> N35; N29 -> N07; N29 -> N18; N29 -> N09; N29 -> N25; N30 -> N01; N31 -> N04; N32 -> N01; N32 -> N42; N32 -> N18; N32 -> N25; N33 -> N01; N33 -> N15; N33 -> N07; N33 -> N21; N35 -> N01; N35 -> N07; N36 -> N01; N38 -> N01; N39 -> N01; N39 -> N06; N39 -> N50; N39 -> N18; N39 -> N09; N39 -> N26; N40 -> N01; N40 -> N04; N40 -> N39; N40 -> N48; N40 -> N09; N40 -> N25; N40 -> N20; N41 -> N01; N41 -> N06; N41 -> N32; N41 -> N18; N41 -> N25; N41 -> N02; N42 -> N01; N42 -> N06; N42 -> N18; N42 -> N25; N42 -> N26; N44 -> N01; N44 -> N02; N44 -> N04; N45 -> N01; N45 -> N04; N45 -> N16; N45 -> N17; N45 -> N09; N46 -> N01; N46 -> N06; N46 -> N02; N46 -> N32; N46 -> N18; N46 -> N25; N47 -> N04; N48 -> N01; N48 -> N06; N48 -> N04; N48 -> N17; N48 -> N09; N48 -> N20; N49 -> N01; N49 -> N42; N50 -> N01; N50 -> N06; N50 -> N16; N50 -> N18; N50 -> N39; N50 -> N09; N50 -> N26
DERIVATION MODE: COMPUTED-FROM-RETRIEVED
DENSITY CALCULATION: directed density = directed internal edges u -> v (u, v in N01..N50, u != v, v in OpenAlex referenced_works of u) / n(n-1), n = 50; computed by graph2.py from raw/reception1_top50.json.
DENSITY NUMERATOR: 174 directed internal edges among the 50 corpus nodes.
DENSITY DENOMINATOR: 2450 possible directed edges (50 × 49).
DENSITY INPUT COVERAGE: 50/50 reference lists obtained from OpenAlex (6,000 indexed references). No Crossref cross-check in this run.
DENSITY INFERENCE SCOPE: the density result applies only to RECEPTION-1. Because RECEPTION-1 is selected on target citation, it can establish density inside that target-citing corpus; it cannot establish or exclude field-wide, founding-cluster or premise-subnetwork closure. No seed-expanded or matched comparison graph was built.

Closure is not established and not excluded beyond the defined corpus.

Density results. Raw directed density 174/2450 = 7.10%. Excluding N01 (the conflated Reply/AJR 2001 record, in-degree 38) gives 127/2352 = 5.40%. 44/50 nodes cite at least one other corpus node. Reciprocal pairs: 13. Internal references are 174/6,000 = 2.90% of all indexed outbound references. In-degree leaders: N01 38, N06 18, N18 16, N25 13, N02 10, N42 9. Excluding N01: N06 17, N18 16, N25 12, N02 10, N04 9.

1. Top 50 most-cited works citing AJR 2001: RECEPTION-1 (Artifact 1 lists the top 15). Relevance composition: ADJACENT 14, BACKGROUND 25, DIRECT 5, UNKNOWN 6.
2. Founding cluster: AJR 2001 with AJR-team follow-ups (Reversal of Fortune, the handbook synthesis, the 2012 Reply). 12/50 RECEPTION-1 records have Acemoglu, Johnson or Robinson as an author (N01, N06, N09, N15, N16, N18, N26, N30, N35, N39, N42, N50).
3. Founding papers' evidence type: AJR 2001 primary cross-country IV (FULL-TEXT); Reversal of Fortune primary cross-country (ABSTRACT); handbook synthesis (FULL-TEXT, WP version); Reply re-analysis (FULL-TEXT).
4. Hubs: AJR-team records receive 109/174 internal edges (62.6%); excluding the conflated N01 they receive 67/127 (52.8%). Leading node after N01: N06.
5. Hub substitution: within RECENT-1, Rodrik 2004 is co-cited by 6/25 and an AJR-team work beyond the target by 7/25 (all cite AJR 2001 by construction).
6. Small cluster citing itself: no closed cluster inside RECEPTION-1 (density 7.10%).
7. Gatekeeping roles: no editorial or referee data retrieved; UNASSESSED.
8. Self-citation in the founding cluster: ordinary programme self-citation (team records cite each other and N01).
9. Concentration by lab/journal/funder: not assessed beyond authorship (SECTION I).
10. Citation count vs independent confirmation: AJR 2001 cited_by_count 9,952 at retrieval; see DATA-ORIGIN inference I21.

SECTION B: EVIDENCE TYPE CODING

Every corpus member is coded in the SOURCE ELIGIBILITY LEDGER. Questions 11–16 describe the evidence base only on ADJUDICATION-1, the SEARCHED adjudication corpus; on RECEPTION-1 they describe the citing set.

ADJUDICATION-1 composition (evidence base, bounded by the locked search):
COMPOSITION: I15 | relevance | ADJACENT=15; BACKGROUND=15; DIRECT=24; UNKNOWN=2; UNRELATED=2 | TOTAL=58
COMPOSITION: I16 | contribution | COMMENTARY=1; INDEPENDENT-DATA=16; METHOD=2; NONE=17; REANALYSIS=19; REVIEW=1; UNKNOWN=2 | TOTAL=58
RECEPTION-1 composition (citing set only):
COMPOSITION: I17 | relevance | ADJACENT=14; BACKGROUND=25; DIRECT=5; UNKNOWN=6 | TOTAL=50

11. Primary empirical tests in ADJUDICATION-1: 24 DIRECT members (L1 8, L3-R1 13, L3-noSM 3, L3-R2 0); contribution REANALYSIS 19, INDEPENDENT-DATA 16, METHOD 2.
12. Reviews/syntheses: REVIEW 1, COMMENTARY 1.
13. Theory-only: none among DIRECT members.
14. Unknown: relevance UNKNOWN 2, contribution UNKNOWN 2 (ADJ37, ADJ44 title-only).
15. Evidence-to-claim ratio: within the locked search, re-analyses of the AJR series dominate the DIRECT set; independent-data DIRECT members are the historical-malaria and identification-through-heteroskedasticity papers (ADJ12, ADJ14, ADJ49).
16. On RECEPTION-1 the same questions describe citers: DIRECT 5/50, ADJACENT 14/50, BACKGROUND 25/50, UNKNOWN 6/50.

SECTION C: CITATION POLARITY AND CLAIM USE

Citing passages inspected: RECEPTION-1 14/50 (N01, N02, N04, N05, N07, N08, N09, N11, N12, N16, N17, N22, N25, N32); RECENT-1 2/25; ADJUDICATION-1 1/58. The instrument's 15-passage target was not reached for RECENT-1 or ADJUDICATION-1. Percentages use inspected citations only.

17. Supportive: SUPPORTS in 7/14 inspected RECEPTION-1 passages (50%).
18. Critical: CHALLENGES 1/14; QUALIFIES 3/14.
19. Perfunctory/background: MENTIONS 5/14; RECENT-1 2/2 inspected passages are MENTIONS.
20. Premise use: PREMISE 2/14.
21. Data/instrument reuse: REUSES 6/14.
22. Polarity inflation: the self-authored handbook (HB-E1) restates magnitude without the qualifier (SECTION D); inspected independent users preserve proxy wording (DML-E1, HW-E1).

SECTION D: CLAIM MUTATION TRACKING

23–30. Original (AJR-E2, AJR 2001 PDF p. 20 = AER p. 1387): the 0.94 estimate implies an approximately 7-fold Nigeria–Chile difference, which the authors call an upper bound because of measurement error. Hub restatement (HB-E1, NBER WP 10481 p. 29): "most of the gap between rich and poor countries today is due to differences in economic institutions". Construct: the regressor "average protection against expropriation risk" is restated as "enforcement of property rights" and "economic institutions" (HB-E1). Independent users preserve it: DML-E1 "an index which measures protection against expropriation risk". Public layer: NP-E1 "a clear chain of causality" vs NS-E1 "taken with a grain of salt". Severity: moderate at the self-authored hub; preserved by independent users; inflation at the popular layer.

| Original source | Original claim | Hub restatement | Downstream restatement | Mutation severity | Note |
|---|---|---|---|---|---|
| AJR 2001 p. 1387 (AJR-E2) | 0.94 implies about a 7-fold gap; an upper bound | HB-E1: most of the gap due to economic institutions | NP-E1: "a clear chain of causality" | moderate | self-authored hub; NS-E1 preserves caution |
| AJR 2001 Table 4 regressor | PRS expropriation-risk index | HB-E1: "enforcement of property rights" | DML-E1 preserves the index wording | minor | broadening at the hub only |

SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT

Steps 31–37 reuse the v1 preregistration (reused; lock/section_E_preregistration.md on branch audit/acemoglu-colonial-origins, sha256 84847dd02aca0af819994008ae98d407fae5f75560c8d5de9b628346df965154). Layers L1–L4, rivals R1 and R2, observations O1–O4 and fields F1–F6 are as recorded there. This run adds ADJUDICATION-1, a SEARCHED corpus locked before screening, as the discovery route for DIRECTLY-ADJUDICATING sources.

SOURCE-LOCK METHOD: LOCKED QUERY
SOURCE-LOCK DATABASE: OpenAlex works API (reused v1 lock; raw responses on the v1 branch)
SOURCE-LOCK QUERY OR SOURCE LIST: filter=title.search:<terms>,to_publication_date:2000-12-31,type:article with terms F1 "malaria economic", F2 "geography economic development", F3 "human capital growth", F4 "weak instruments", F6 "institutions economic performance" (reused)
SOURCE-LOCK DATE CUTOFF: 2000-12-31 (publication on or before)
SOURCE-LOCK RANKING RULE: OpenAlex cited_by_count descending at query time
SOURCE-LOCK N: 10 (top 2 per field × 5 fields)
SOURCE-LOCK DEDUPLICATION RULE: by OpenAlex work ID; off-topic items retained and flagged, never replaced
SOURCE-LOCK TIMESTAMP OR HASH: 2026-11-04T11:42:25Z (3:42:25 AM PST, reused); preregistration sha256 84847dd02aca0af819994008ae98d407fae5f75560c8d5de9b628346df965154

Flip test (step 37): PASS (reused): F1, F2 from R1; F3 from R2; F4 from both. Innocent explanations as in v1: scope mismatch for F1 exemplars; disciplinary boundary and timing for F3; missing weak-IV methods route to lack of decisive tests.

Falsification-relevant literature preregistration table:

| Claim layer | Audited explanation | Strongest plausible rival explanation | Adjudicating observation | Candidate field | Generated from audited claim, rival, or both? | Measurement relevance | Adjudicative capacity | Independence | Publication-date cutoff | Historically available? | Flip-test result | Source-lock method | Lock timestamp / hash | Final engagement classification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1/L3 | colonial institutions (expropriation-risk proxy) drive income | R1 direct disease channel | O1 disease effects with institutions fixed | F1 malaria economics | rival | disease burden | could weaken L3 | independent | 2000-12-31 | yes | PASS | LOCKED QUERY (reused) | 84847dd0…5154 | direct substantive engagement (AJR-E4) |
| L1/L3 | as above | R1 direct geography channel | O2 geography conditional on institutions | F2 geography | rival | geographic correlates | could weaken L3 | independent | 2000-12-31 | yes | PASS | LOCKED QUERY (reused) | as above | direct substantive engagement (geography controls) |
| L3 | as above | R2 settler human capital | O3 decomposition | F3 human capital | rival | schooling effects | could weaken L3 | independent | 2000-12-31 | partly | PASS | LOCKED QUERY (reused) | as above | no located engagement (theory exemplars; timing) |
| L1/L2 | as above | weak or noisy instrument | O4 2SLS reliability | F4 weak-IV econometrics | both | inferential validity | could narrow L1/L2 | independent | 2000-12-31 | yes | PASS | LOCKED QUERY (reused) | as above | citation without substantive engagement |
| L1 | as above | not a rival | construct definition | F6 institutional measurement | audited claim | defines regressor | construct-defining | partly shared provider | 2000-12-31 | yes | PASS | LOCKED QUERY (reused) | as above | direct substantive engagement (Knack–Keefer) |

Adjacent-literature neglect table:

| Claim layer | Adjacent field | Nominated source and stable identifier | Verification state | Source class: CONSTRUCT-DEFINING / MECHANISM-SUPPORTING / DIRECTLY-ADJUDICATING | Actual result | Explanation favored | Explanation weakened | Precise revision required | Pre-inspection lock status or POST HOC | Cited by dominant cluster? | Engagement quality | Effect of omission |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L3 | F1 malaria | X06 W139828295 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | household malaria spending | — | — | — | LOCKED (reused) | no | not cited | minor context loss |
| L3 | F1 malaria | X07 W2088758477 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | socio-economic malaria risk factors | — | — | — | LOCKED (reused) | no | not cited | minor context loss |
| L1/L3 | F2 geography | X08 W2618788771 Gallup–Sachs–Mellinger | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | geography correlates with income | — | — | — | LOCKED (reused) | yes (AJR 2001) | directly tested against | minor context loss |
| L3 | F2 geography | X09 W1492460295 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | geography in development theory | — | — | — | LOCKED (reused) | no | not cited | minor context loss |
| L3 | F3 human capital | X10 W3121822366 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | human-capital growth theory | — | — | — | LOCKED (reused) | no | not cited | minor context loss |
| L3 | F3 human capital | X11 W2035652178 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | schooling-finance growth model | — | — | — | LOCKED (reused) | no | not cited | minor context loss |
| L1/L2 | F4 weak-IV | X12 W2165144879 Staiger–Stock | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | weak-instrument asymptotics | — | — | — | LOCKED (reused) | no | not cited | moderate weakness (routes to lack of decisive tests) |
| L1/L2 | F4 weak-IV | X13 W1980412904 Bound–Jaeger–Baker | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | weak IV biased toward OLS | — | — | — | LOCKED (reused) | yes (AJR-E3) | cited in passing | minor context loss |
| L1 | F6 measurement | X14 W3121147769 North 1990 record | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | definition of institutions | — | — | — | LOCKED (reused) | other North works cited | not cited | minor context loss |
| L1 | F6 measurement | X15 W2010235856 Knack–Keefer | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | ICRG/BERI indices predict growth | — | — | — | LOCKED (reused) | yes (AJR 2001) | substantively engaged | minor context loss |
| L3 | R1 test | ADJ38 W2001123479 Carstensen–Gundlach | ABSTRACT-CONFIRMED; CONTESTED | DIRECTLY-ADJUDICATING | abstract: malaria has a direct income effect alongside institutions | R1 | L3 strong form | L3: institutions a major channel; direct disease channel not excluded | LOCKED (ADJUDICATION-1 search) | UNASSESSED (later AJR-team reference lists not traced) | UNASSESSED because retrieval was insufficient | moderate weakness |
| L3 | R1 test | X03 Sachs 2003 NBER w9490 | FULL-TEXT-CONFIRMED; CONTESTED | DIRECTLY-ADJUDICATING | AJR-style null rejected with malaria risk (SA-E1) | R1 | L3 strong form | as above | POST HOC | UNASSESSED | UNASSESSED because retrieval was insufficient | moderate weakness |
| L3 | R2 test | N04 W2890314743 Glaeser et al. 2004 | FULL-TEXT-CONFIRMED; CONTESTED | DIRECTLY-ADJUDICATING | malaria risk significant alongside settler mortality; human-capital channel (GL-E1, GL-E2) | R1 and R2 | L3 strong form | L3: institutions or settler human capital, not separately identified | POST HOC (RECEPTION-1 member; not returned by the locked search) | acknowledged in NS-E3 | UNASSESSED because retrieval was insufficient | moderate weakness |

The source layer engages R1 directly (AJR-E4: malaria controls). Dominant-cluster engagement with the later R1/R2 tests was not traced in this run, so the dimension is scored on the source layer only (ENGAGEMENT I19); POST HOC rows anchor nothing.

SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING

40. Hubs: Rodrik et al. 2004 (N02/N32; independent) and the AJR handbook (N09/N16; self-authored). In-degree inside RECEPTION-1: N02 10, N32 5, N09 7, N16 2.
41. Recent papers citing the hub: Rodrik 6/25 in RECENT-1; handbook records 4/25.
42. Recent papers citing primary evidence directly: 25/25 by construction.
43. Hub substitution for inspection: not measurable from reference lists; no downstream passage citing the handbook was inspected (I23 NOT-ASSESSED).
44–45. Accuracy: Rodrik accurate and critical of interpretation (RD-E4); handbook drops the upper-bound qualifier (HB-E1 vs AJR-E2).
46. Adjacent literatures in hubs: both engage geography.
47. Hub as substitute for primary evidence: UNASSESSED.

| Hub paper | Recent papers citing hub | Recent papers citing primary evidence directly | Adjacent-field citation rate | Hub accuracy | Hub risk |
|---|---|---|---|---|---|
| Rodrik, Subramanian & Trebbi 2004 (N02) | 6/25 RECENT-1 | 25/25 by construction | Glaeser co-cited by 4/25 RECENT-1; 225/3,026 recent AJR citers | accurate; critical of interpretation | low |
| AJR handbook (N09, N16) | 4/25 RECENT-1 | 25/25 by construction | as above | qualifier dropped; construct broadened | moderate (downstream reliance not traced) |

SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR

48. Proxy treated as construct: at the self-authored hub (HB-E1), not by inspected independent users (DML-E1, HW-E1).
49. Export from low-stakes settings: not applicable; the counterfactual is bounded by the authors (AJR-E2).
50. Ignored natural experiments: no; within-country designs appear in RECEPTION-1.
51. Model updating: the Reply defends the model against Albouy (p. 3078); updating vs defence is CONTESTED.
52. Intervention expansion: no intervention claim; N/A.
53–55. Falsification criteria stated via the exclusion restriction and controls (AJR-E4); 55 N/A.
56. Expansion over testing: not assessed.

Ratchet scoring route. Intervention-evidence ratchet: N/A (no intervention claim). Model non-updating four-link gate: link 1 met; link 2 (verified later disconfirming evidence) not reached — Albouy and the R1/R2 tests are CONTESTED; links 3–4 not traced. The dimension is UNASSESSED.

SECTION H: IGNORED CRITIQUE AND NON-UPTAKE

1. Precondition: critique production strongly expected (AER lead article; cited_by_count 9,952; Nobel 2024).
2. Retrieval: Albouy 2012 (X02, FULL-TEXT); Glaeser et al. 2004 (GL-E1, GL-E2); Sachs 2003 (SA-E1).
3. Reception opportunity: verified for Albouy (Reply in the same AER issue, p. 3078).
4. Uptake in the uptake population: the Reply (N01) engages Albouy substantively (ENGAGEMENT I18). Glaeser uptake by the AJR team not traced (I22 NOT-ASSESSED). Co-citation alone carries no score: Albouy 72/3,026 and Glaeser 225/3,026 recent AJR citers (I20, descriptive).

57. Serious critiques: Albouy 2012; Glaeser et al. 2004; Sachs 2003; Rodrik et al. 2004 on interpretation.
58. Cited by the dominant cluster: Albouy yes (Reply); others not traced.
59. Mode: engaged and contested (Albouy).
60. Network update: partial at the scientific-summary layer (NS-E1).
61. Recent papers: 2/2 inspected passages use AJR as background.
62–63. Practitioner warnings: not searched; UNASSESSED.

| Expected-production precondition | Critique / contrary evidence | Year | Source type | Main objection | Verification state | Reception opportunity | Cited by dominant cluster? | Uptake status | Dimension disposition | Effect on consensus |
|---|---|---|---|---|---|---|---|---|---|---|
| strong | Albouy, AER Comment (X02, W1969918011) | 2012 | formal comment | settler-mortality data construction | FULL-TEXT-CONFIRMED; CONTESTED | verified | yes (Reply p. 3078); 72/3,026 recent AJR citers | substantively engaged by the cluster | SCORED 0 | answered; scientific summary cautious (NS-E2) |
| strong | Glaeser et al. (N04) | 2004 | primary empirical | human capital; disease environment | FULL-TEXT-CONFIRMED; CONTESTED | verified | UNASSESSED; 225/3,026 recent AJR citers | UNASSESSED | not scored separately | acknowledged in NS-E3 |

SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING

64. Recurring authors: AJR-team authorship on 12/50 RECEPTION-1 records (I03), including duplicate records of two team works.
65–67. Venues, institutions, funding: not re-derived; UNASSESSED.
68. Dissent venues: Albouy and the Reply in the AER; Glaeser et al. and Rodrik et al. in the Journal of Economic Growth.
69–70. Gatekeeping and ideology: not assessable.

Closure type: normal clustering around a canonical paper inside RECEPTION-1; no author, journal, funding or advocacy closure established.

SECTION J: FALSE-POSITIVE AND BASELINE CHECK

71. Small field: no. 72. Baseline comparison: none built. 73. Adjacent expertise: the source engages geography and malaria (AJR-E4). 74. Only people studying the question: no; DIRECT members come from many teams. 75. Strong primary evidence: yes for the estimate; conditional for causal and construct readings. 76. Repeated independent tests: tests exist (24/58 DIRECT) but most reuse the AJR series (I21). 77. Limitations preserved: lost at the self-authored hub and popular layer; preserved by inspected independent users. 78–80. Failed predictions acknowledged, critics engaged, updating via comment-and-reply: yes.

Answers are mostly yes; this is not a cartel signature.

SECTION J2: THE CONCEDE TEST

| Finding | Declared target claim | Matches map field 6? | Same mechanism as another row? | Count separately? |
|---|---|---|---|---|
| 1 Database record instability | the OpenAlex record and reception corpora of AJR 2001 | no — MAP GAP: this finding targets the retrieval record, not map field 6 | no | yes |
| 2 Shared data origin of re-estimates | L3: independent confirmation | no — MAP GAP: this finding targets L3, not map field 6 | no | yes |
| 3 Hub qualifier loss and construct broadening | L3 restatement of the field-6 magnitude | no — MAP GAP: this finding targets the hub restatement | yes — proxy mismatch and claim mutation share HB-E1 | no — counted once (proxy mismatch NESTED) |
| 4 Direct tests exist and conflict | L3 and field-6 robustness | partly | no | yes |
| 5 Albouy critique engaged by the cluster | field 6 | yes | no | yes |
| 6 No closure inside RECEPTION-1 | field 6 network support | yes | no | yes |
| 7 Recent citers use AJR as background | field 6 network support | yes | no | yes |

| Finding | Concede test: SURVIVES / NARROWS / DEFEATS | Surviving claim if NARROWS |
|---|---|---|
| 1 | SURVIVES | — |
| 2 | NARROWS (against L3; SURVIVES against field 6) | several teams obtain similar estimates with the AJR series |
| 3 | NARROWS (against the restatement; SURVIVES against field 6) | 0.94 implies up to about a 7-fold gap, an upper bound |
| 4 | NARROWS (against L3; field 6 SURVIVES as an estimate) | institutions a major channel; direct disease effects not excluded |
| 5 | SURVIVES | — |
| 6 | SURVIVES | — |
| 7 | SURVIVES | — |

| Finding | Scope-loss level | Original claim | Surviving claim | What epistemic or practical work is lost? |
|---|---|---|---|---|
| 2 | material | independent work confirms institutions explain income differences | similar estimates on one shared data origin | independence of confirmation |
| 3 | material (restatement); incidental (field 6) | most of the gap due to economic institutions | up to about 7-fold, an upper bound | magnitude used in counterfactuals |
| 4 | material (L3) | institutions, not geography or disease, are the fundamental cause | institutions a major channel; rivals CONTESTED | exclusivity of the institutional explanation |

No finding DEFEATS field 6.

SECTION K0: EVIDENCE SUFFICIENCY LEDGER

Gate B was applied to every inference before any score or finding used it. Inferences that fail stay listed with what would make them sufficient.

INFERENCE LEDGER

| Inference | Class | Corpus | Claimed scope | Sampling rule | Members used | Disposition | Statement |
|---|---|---|---|---|---|---|---|
| I01 | GRAPH-STRUCTURE | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Directed internal density 174/2450 = 7.10% (50/50 reference lists); no closed cluster inside RECEPTION-1. |
| I02 | GRAPH-STRUCTURE | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | AJR-team records (12/50) receive 109/174 internal edges; 38 go to the conflated N01; excluding N01, team records receive 67/127. |
| I03 | DATABASE-RECORD | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | 12/50 members list Acemoglu, Johnson or Robinson as author; 4 works appear as two records each. |
| I04 | GRAPH-STRUCTURE | RECENT-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | 7/25 members cite at least one AJR-team work beyond the target (R03, R07, R11, R14, R19, R24, R25); 18/25 cite none. |
| I05 | CITATION-USE | RECENT-1 | WITHIN-SAMPLE | CONVENIENCE | R13, R23 | SUPPORTED-WITHIN-SAMPLE | Both inspected passages cite AJR 2001 as background (theory list; endogeneity precedent), not the field-6 estimate; 2 of 6 randomly drawn members were retrievable, so the inspected subset is CONVENIENCE. |
| I06 | CITATION-USE | RECENT-1 | CORPUS | PRESPECIFIED-RANDOM | R01, R06, R10, R13, R21, R23 | INSUFFICIENT | How RECENT-1 uses AJR 2001 cannot be estimated: 4/6 sampled full texts were not retrieved (HTTP 403 for three, 500 for one). Sufficient if all 6 sampled passages were inspected. |
| I07 | CITATION-USE | RECEPTION-1 | WITHIN-SAMPLE | CONVENIENCE | N01, N02, N04, N05, N07, N08, N09, N11, N12, N16, N17, N22, N25, N32 | SUPPORTED-WITHIN-SAMPLE | Among 14 inspected passages: SUPPORTS 7, PREMISE 2, QUALIFIES 3, CHALLENGES 1, MENTIONS 5; reuse of AJR data or instrument in 6. |
| I08 | RESTATEMENT | — | NAMED | NOT-APPLICABLE | X01, N09 | SUPPORTED | HB-E1 restates the AJR-E2 magnitude implication without the authors' upper-bound qualifier. |
| I09 | RESTATEMENT | — | NAMED | NOT-APPLICABLE | X01, N09 | SUPPORTED | HB-E1 restates the expropriation-risk regressor as enforcement of property rights and economic institutions. |
| I10 | CITATION-USE | — | NAMED | NOT-APPLICABLE | N08, N17 | SUPPORTED | Independent users preserve the proxy: DML-E1 names the expropriation-risk index; HW-E1 calls the geography finding disputed. |
| I11 | SOURCE-RESULT | — | NAMED | NOT-APPLICABLE | ADJ01, ADJ05, ADJ09, ADJ18, ADJ38, N04, X02, X03 | SUPPORTED | Named direct tests of field 6 (ADJ01, ADJ05, X02) and of the R1/R2 rivals (ADJ09, ADJ18, ADJ38, X03, Glaeser) exist with stated results. |
| I12 | SOURCE-RESULT | — | NAMED | NOT-APPLICABLE | ADJ09, ADJ18, ADJ38, X03, N04, N02, N25 | SUPPORTED | Results conflict: geography or malaria keeps direct effects in ADJ09, ADJ18, ADJ38, Sachs and Glaeser; institutions dominate in Rodrik and Easterly–Levine. |
| I13 | ABSENCE | ADJUDICATION-1 | WITHIN-SAMPLE | EXHAUSTIVE | SCREENED | SUPPORTED-WITHIN-SAMPLE | No DIRECT (L3-R2) human-capital decomposition test among 56/58 screened members; Glaeser 2004, outside the search bound, is one. Not used to score. |
| I14 | ABSENCE | ADJUDICATION-1 | LITERATURE | EXHAUSTIVE | ALL | INSUFFICIENT | No cross-country re-estimate of field 6 with an instrument independent of the AJR series exists. Insufficient: ADJ37 and ADJ44 unscreened; sufficient once screened and none qualifies. |
| I15 | COMPOSITION | ADJUDICATION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Relevance composition of the evidence base within the locked search. |
| I16 | COMPOSITION | ADJUDICATION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Contribution composition within the locked search. |
| I17 | COMPOSITION | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Relevance composition of the citing set; describes citers, not the evidence base. |
| I18 | ENGAGEMENT | — | NAMED | NOT-APPLICABLE | N01 | SUPPORTED | The Reply substantively answers Albouy's two data objections (p. 3078) and re-estimates on revised data. |
| I19 | ENGAGEMENT | — | NAMED | NOT-APPLICABLE | X01 | SUPPORTED | AJR 2001 engages the R1 malaria/geography rival directly with controls (AJR-E4). |
| I20 | CO-CITATION | POPULATION | POPULATION | NOT-APPLICABLE | UNSCREENED | SUPPORTED | Among recent AJR citers, Albouy 2012 is co-cited by 72/3026 and Glaeser 2004 by 225/3026 (OpenAlex counts); co-citation, not use. |
| I21 | DATA-ORIGIN | — | NAMED | NOT-APPLICABLE | N02, N25, N08, N01 | SUPPORTED | Rodrik, Easterly–Levine, Chernozhukov et al. and the Reply all use the AJR settler-mortality series (RD-E1, EL-E2, DML-E1). |
| I22 | ENGAGEMENT | — | NAMED | NOT-APPLICABLE | — | NOT-ASSESSED | AJR-team uptake of the Glaeser human-capital critique. Not assessed: the AJR-team response noted in NS-E3 was not retrieved; sufficient with its full text. |
| I23 | RESTATEMENT | — | NAMED | NOT-APPLICABLE | — | NOT-ASSESSED | Downstream works restate AJR via the handbook. Not assessed: no handbook-citing passage was inspected; sufficient with inspected passages from a defined hub-citing set. |
| I24 | DATABASE-RECORD | — | NAMED | NOT-APPLICABLE | X01 | SUPPORTED | The AJR 2001 OpenAlex record changed between runs about 17 hours apart: referenced works 13 → 55; RECEPTION-1 differs from v1 in 12/50 members; RECENT population 2695 → 3026. |

COMPOSITION: I15 | relevance | ADJACENT=15; BACKGROUND=15; DIRECT=24; UNKNOWN=2; UNRELATED=2 | TOTAL=58
COMPOSITION: I16 | contribution | COMMENTARY=1; INDEPENDENT-DATA=16; METHOD=2; NONE=17; REANALYSIS=19; REVIEW=1; UNKNOWN=2 | TOTAL=58
COMPOSITION: I17 | relevance | ADJACENT=14; BACKGROUND=25; DIRECT=5; UNKNOWN=6 | TOTAL=50

Withheld inferences: I06 (INSUFFICIENT: sample attrition), I14 (INSUFFICIENT: 2 unscreened members), I22 and I23 (NOT-ASSESSED). I13 passes within the search bound but is not used to score, because a known R2 test lies outside the bound.

DIMENSION EVIDENCE BASIS

DIMENSION CLASS MAP: cn7-map-2

| Scorecard dimension | Scorecard disposition | Inference IDs | Basis note |
|---|---|---|---|
| Founding-cluster dominance | SCORED 1 | I02 (+), I03 (+) | team records draw most internal edges, inflated by the conflated N01; authorship 12/50 |
| Internal citation density | SCORED 0 | I01 (-) | low density inside RECEPTION-1 only; closure not excluded beyond it |
| Recent-paper dependence | SCORED 1 | I04 (+), I05 (-) | 7/25 cite team works beyond the target; inspected uses are background (2 passages) |
| Review-hub laundering | UNASSESSED | — | I23 NOT-ASSESSED: downstream reliance on the handbook not traced |
| Proxy mismatch | SCORED 1 | I09 (+), I10 (-) | broadening at the self-authored hub; independent users preserve the proxy; NESTED under claim mutation |
| Claim mutation | SCORED 1 | I08 (+) | qualifier loss at the self-authored hub |
| Adjacent-field neglect | SCORED 0 | I19 (-) | source layer engages R1; cluster engagement with later R1/R2 tests not traced |
| Lack of decisive tests | SCORED 0 | I11 (-) | named direct tests exist; their results conflict (I12); bounded absence I13 not used |
| Poor critique uptake | SCORED 0 | I18 (-) | Albouy answered by the Reply; Glaeser uptake not traced (I22) |
| Intervention-evidence ratchet | N/A | — | no intervention claim at field 6 or in the traced network |
| Model non-updating | UNASSESSED | — | four-link gate: link 2 not verified (disconfirming evidence CONTESTED); links 3–4 not traced |

FINDING EVIDENCE BASIS

| Finding | Finding status | Inference IDs |
|---|---|---|
| Finding 1 | confirmed | I24, I03 |
| Finding 2 | confirmed | I21 |
| Finding 3 | confirmed | I08, I09 |
| Finding 4 | contested | I11, I12, I15 |
| Finding 5 | confirmed | I18, I20 |
| Finding 6 | confirmed | I01, I02 |
| Finding 7 | provisional | I04, I05, I06 |

SECTION K: CARTEL-RISK SCORING

Scores are in Artifact 8. Proxy mismatch rests on the same HB-E1 passage that owns claim mutation, so it is NESTED under Claim mutation. Founding-cluster dominance and internal density use the same RECEPTION-1 edge list but answer different questions (in-edge concentration plus authorship records vs overall density) and are kept INDEPENDENT.

- Verified risk score: 3/21
- Verified scored-dimension risk rate: 14.3
- Independent scored dimensions: 7
- Nested scored dimensions: 1
- Verified risk denominator: 21
- Evidentiary coverage: 8/10 applicable dimensions scored (80%)
- Execution completeness: 10/10 applicable dimensions completed (100%)
- Dimension inventory: 7 INDEPENDENT SCORED + 1 NESTED SCORED + 0 UNINFORMATIVE + 2 UNASSESSED + 1 N/A = 11 total dimensions; 10 applicable
- Unscored dimensions: Review-hub laundering — UNASSESSED (I23 not assessed); Model non-updating — UNASSESSED (four-link gate not traced); Intervention-evidence ratchet — N/A (no intervention claim)

Verified scored-dimension risk: 14.3%, calculated from 7 independent scored dimensions; 1 additional scored dimensions are NESTED; 8 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.

Formal-label gate: coverage 8/10 (80%) declared; 7/10 (70%) if the recent-paper dependence review item is withdrawn; both meet the PROVISIONAL 70% threshold (engineering threshold, not validated). Label-essential check: the arithmetic position is the healthy/low-risk band, which needs affirmative no-concern evidence on the dimensions that could establish closure. Claim transmission carries a SCORED 1 concern, review-hub laundering is UNASSESSED, and density is affirmative only inside a corpus selected on target citation. The band is withheld.

ARITHMETIC BAND POSITION: 0%–20% (healthy or low-risk network)
RISK BAND: WITHHELD — label-essential: the healthy/low-risk band needs affirmative no-concern evidence on closure-establishing dimensions; claim mutation is SCORED 1, review-hub laundering UNASSESSED, density bounded to a target-selected corpus.
MECHANISM LABEL: self-authored hub qualifier loss (HB-E1) on a shared data origin; no closure signature inside RECEPTION-1

ARTIFACT 1: TOP 15 CITATION SPINE TABLE

| Rank | Paper | Year | Citation count | Evidence type | Role in network | Source of citation count |
|---:|---|---:|---:|---|---|---|
| 1 | N01 Daron Acemoğlu, Simon Johnson, James A. Robinson: The Colonial Origins of Comparative Development: An Empirical Investig (W3124131699) | 2012 | 6187 | secondary analysis | DIRECT (L1); SUPPORTS+REUSES | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 2 | N02 Dani Rodrik, Arvind Subramanian, Francesco Trebbi: Institutions Rule: The Primacy of Institutions Over Geography and Inte (W2994756033) | 2002 | 5577 | secondary analysis | DIRECT (L3-R1); SUPPORTS+QUALIFIES+REUSES | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 3 | N03 F ALLEN, Jun “QJ” Qian, Meijun Qian: Law, Finance, and Economic Growth in China (W3124948273) | 2003 | 4472 | unclear / needs source audit | UNKNOWN; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 4 | N04 Edward L. Glaeser, Rafael La Porta, Florencio López‐de‐Silanes: Do Institutions Cause Growth? (W2890314743) | 2004 | 3881 | secondary analysis | DIRECT (L3-R2); CHALLENGES+REUSES | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 5 | N05 Ross Eric Levine: Finance and Growth: Theory and Evidence (W2113844427) | 2004 | 3743 | review article | BACKGROUND; MENTIONS | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 6 | N06 Daron Acemoğlu, Simon Johnson, James A. Robinson: Reversal of Fortune: Geography and Institutions in the Making of the M (W3125412951) | 2002 | 3324 | primary empirical study | ADJACENT; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 7 | N07 Raghuram G. Rajan, Luigi Zingales: The great reversals: the politics of financial development in the twen (W3122778615) | 2003 | 3241 | primary empirical study | BACKGROUND; MENTIONS | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 8 | N08 Victor Chernozhukov, Denis Chetverikov, Mert Demirer: Double/debiased machine learning for treatment and structural paramete (W3123436326) | 2017 | 3176 | methodological paper | ADJACENT; SUPPORTS+REUSES | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 9 | N09 Daron Acemoğlu, Simon Johnson, James A. Robinson: Institutions as the Fundamental Cause of Long-Run Growth (W2108614304) | 2004 | 3127 | review article | ADJACENT; PREMISE+SUPPORTS | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 10 | N10 Simone Raudino: The Theory of Economic Development (W2556507681) | 2016 | 3015 | unclear / needs source audit | UNKNOWN; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 11 | N11 Ross Eric Levine: Chapter 12 Finance and Growth: Theory and Evidence (W1588189399) | 2005 | 2979 | review article | BACKGROUND; MENTIONS | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 12 | N12 César A. Hidalgo, Bailey Klinger, Albert-Ĺaszló Barabási: The Product Space Conditions the Development of Nations (W2064927380) | 2007 | 2937 | primary empirical study | BACKGROUND; MENTIONS | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 13 | N13 Halvor Mehlum A, Karl Ove Moene, Ragnar Torvik: Institutions and the Resource Curse (W1484474409) | 2006 | 2874 | primary empirical study | ADJACENT; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 14 | N14 Robert M. Bushman, Abbie J. Smith: Financial accounting information and corporate governance (W3122300128) | 2001 | 2723 | unclear / needs source audit | UNKNOWN; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |
| 15 | N15 Daron Acemoğlu, Simon Johnson: Unbundling Institutions (W4240669445) | 2005 | 2553 | primary empirical study (shared data) | ADJACENT; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |

N01's count is inflated by conflation of the Reply record with AJR 2001 (Finding 1).

ARTIFACT 2: FOUNDING CLUSTER TABLE

| Paper | Year | Claim introduced | Evidence type | Verification state | Later role | Risk |
|---|---|---|---|---|---|---|
| AJR, Colonial Origins (W3124166904, X01) | 2001 | settler mortality instrument; 0.94 effect | primary empirical test | FULL-TEXT-CONFIRMED | canonical source | low for field 6 |
| AJR, Reversal of Fortune (N06, N18) | 2002 | reversal of pre-colonial prosperity | primary empirical study | ABSTRACT-CONFIRMED | cited beyond target in RECENT-1 | low |
| AJR, Institutions as a Fundamental Cause (N09, N16) | 2004/2005 | synthesis | review article | FULL-TEXT-CONFIRMED (WP version) | self-authored hub | moderate (HB-E1) |
| AJR, Reply to Albouy (N01) | 2012 | defence of data choices | secondary analysis | FULL-TEXT-CONFIRMED | answers Albouy; record conflated | low |

ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE

"Cites founding cluster?" means beyond AJR 2001 (all cite it by construction). "Cites adjacent fields?" means Glaeser 2004 or Albouy 2012 in the OpenAlex reference list.

| Recent paper | Year | Verification state | Cites founding cluster? | Cites hub? | Cites adjacent fields? | New evidence or recycling? |
|---|---:|---|---|---|---|---|
| R01 Digitalization and sustainable development: How could digital economy  (W4292849668) | 2022 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | AJR 2001 only | no | no | new evidence on another question (abstract) |
| R02 On the role of domestic trade flows for estimating the gravity model o (W4212979054) | 2022 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | AJR 2001 only | no | no | new evidence on another question (abstract) |
| R03 Does institutional quality foster economic complexity? The fundamental (W3165371825) | 2022 | RECEPTION-CONFIRMED; LOCATED | yes (W3124131699) | Rodrik 2004 | Glaeser 2004, Albouy 2012 | not determined (metadata only) |
| R04 Institutional Quality and Education Quality in Developing Countries: E (W4206178768) | 2022 | RECEPTION-CONFIRMED; LOCATED | AJR 2001 only | no | Glaeser 2004 | not determined (metadata only) |
| R05 Women’s political empowerment and economic growth (W4224261420) | 2022 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | AJR 2001 only | Rodrik 2004 | no | new evidence on another question (abstract) |
| R06 Land property rights and rural enterprise growth: Evidence from land t (W4223529822) | 2022 | RECEPTION-CONFIRMED; LOCATED | AJR 2001 only | no | no | not determined (metadata only) |
| R07 Do economic growth and institutional quality reduce poverty and inequa (W4200480718) | 2021 | RECEPTION-CONFIRMED; LOCATED | yes (W1580107285) | Rodrik 2004 | Glaeser 2004 | not determined (metadata only) |
| R08 How Do Institutional Quality, Natural Resources, Renewable Energy, and (W4307547529) | 2022 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | AJR 2001 only | no | no | new evidence on another question (abstract) |
| R09 Institutions, trade, and development: identifying the impact of countr (W4376140760) | 2023 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | AJR 2001 only | no | no | new evidence on another question (abstract) |
| R10 Instrumental variables estimation: Assumptions, pitfalls, and guidelin (W4319016949) | 2023 | RECEPTION-CONFIRMED; LOCATED | AJR 2001 only | no | no | not determined (metadata only) |
| R11 Effects of income inequality and governance on energy poverty alleviat (W4285081985) | 2022 | RECEPTION-CONFIRMED; LOCATED | yes (W2108614304) | no | no | not determined (metadata only) |
| R12 RETRACTED: Country-level institutional quality and financial system ef (W4386322040) | 2023 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | AJR 2001 only | no | no | new evidence on another question (abstract) |
| R13 Informal institutions and international business: Toward an integrativ (W4292663674) | 2022 | FULL-TEXT-CONFIRMED (passage inspected) | AJR 2001 only | no | no | background use (inspected) |
| R14 Cultural Origin and Minority Shareholder Expropriation: Historical Evi (W4388274323) | 2023 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | yes (W1580107285, W3125412951) | no | no | new evidence on another question (abstract) |
| R15 Climate risk, institutional quality, and total factor productivity (W4318937711) | 2023 | RECEPTION-CONFIRMED; LOCATED | AJR 2001 only | no | no | not determined (metadata only) |
| R16 The effects of FDI on economic growth in Africa (W4281705180) | 2022 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | AJR 2001 only | Rodrik 2004 | no | new evidence on another question (abstract) |
| R17 E-invoicing, tax audits and VAT compliance (W4404201184) | 2024 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | AJR 2001 only | no | no | new evidence on another question (abstract) |
| R18 Aid effectiveness and donor motives (W4390870694) | 2024 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | AJR 2001 only | no | no | new evidence on another question (abstract) |
| R19 Can female entrepreneurs boost social mobility in developing countries (W4200592490) | 2021 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | yes (W3125412951) | no | Glaeser 2004 | new evidence on another question (abstract) |
| R20 The role of public environmental concern on corporate social responsib (W4386647200) | 2023 | RECEPTION-CONFIRMED; LOCATED | AJR 2001 only | Rodrik 2004 | no | not determined (metadata only) |
| R21 Regulatory issues inhibiting the financial inclusion: a case study amo (W4387877962) | 2023 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | AJR 2001 only | no | no | new evidence on another question (abstract) |
| R22 Effect of environmental regulation policy synergy on carbon emissions  (W4293403519) | 2022 | RECEPTION-CONFIRMED; LOCATED | AJR 2001 only | no | no | not determined (metadata only) |
| R23 Technological innovation and its influence on energy risk management:  (W4391180104) | 2024 | FULL-TEXT-CONFIRMED (passage inspected) | AJR 2001 only | no | no | background use (inspected) |
| R24 The standard errors of persistence (W3124943234) | 2024 | RECEPTION-CONFIRMED; LOCATED | yes (W3125412951) | no | no | not determined (metadata only) |
| R25 Institutional quality and economic growth in Sub-Saharan Africa: a pan (W4386028756) | 2023 | RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED | yes (W1580107285, W3125412951) | Rodrik 2004 | no | new evidence on another question (abstract) |

RECENT-1 summary: founding cluster beyond target 7/25; Rodrik 6/25; Glaeser 4/25; Albouy 1/25.

ARTIFACT 4: CITATION POLARITY TABLE

| Citing paper | Cited paper | Verification state | Citation polarity | Claim use | Inflation risk |
|---|---|---|---|---|---|
| N01 AJR Reply 2012 | AJR 2001 | FULL-TEXT-CONFIRMED | supportive | defence and re-estimation (p. 3078) | low |
| N02/N32 Rodrik et al. | AJR 2001 | FULL-TEXT-CONFIRMED | supportive | instrument adopted (RD-E1); interpretation criticised (RD-E4) | low |
| N04 Glaeser et al. | AJR 2001 | FULL-TEXT-CONFIRMED | critical | rival tests (GL-E1, GL-E2) | none |
| N09/N16 AJR handbook | AJR 2001 | FULL-TEXT-CONFIRMED | used as premise | magnitude without qualifier (HB-E1) | moderate |
| N08 Chernozhukov et al. | AJR 2001 | FULL-TEXT-CONFIRMED | supportive | reuses the 64 observations (DML-E1) | low |
| N25 Easterly–Levine | AJR 2001 | FULL-TEXT-CONFIRMED | supportive | uses AJR settler-mortality data (EL-E2) | low |
| N17 Hanushek–Woessmann | AJR 2001 | FULL-TEXT-CONFIRMED | neutral/background | "remains a disputed subject" (HW-E1) | none |
| N05/N11 Levine | AJR 2001 | FULL-TEXT-CONFIRMED | neutral/background | background list | none |
| N22 Dell–Jones–Olken | AJR 2001 | FULL-TEXT-CONFIRMED | neutral/background | background | none |
| N12 Hidalgo et al. | AJR 2001 | FULL-TEXT-CONFIRMED | neutral/background | numbered background list p. 2 | none |
| N07 Rajan–Zingales | AJR 2001 | FULL-TEXT-CONFIRMED | perfunctory | reference list only | none |
| R13 recent | AJR 2001 | FULL-TEXT-CONFIRMED | neutral/background | background theory list | none |
| R23 recent | AJR 2001 | FULL-TEXT-CONFIRMED | neutral/background | endogeneity precedent | none |
| X05 Nobel popular 2024 | AJR 2001 | FULL-TEXT-CONFIRMED | inflated | "a clear chain of causality" (NP-E1) | moderate |
| X04 Nobel scientific 2024 | AJR 2001 | FULL-TEXT-CONFIRMED | supportive | "grain of salt" (NS-E1) | none |

No Semantic Scholar contexts were used.

ARTIFACT 5: CLAIM MUTATION TABLE

| Original source | Original claim | Verification state | Hub restatement | Downstream restatement | Mutation severity |
|---|---|---|---|---|---|
| AJR 2001 p. 1387 (AJR-E2) | 0.94 implies about a 7-fold gap; an upper bound | FULL-TEXT-CONFIRMED | HB-E1: most of the gap due to economic institutions | NP-E1: "a clear chain of causality" | moderate |
| AJR 2001 Table 4 regressor | PRS expropriation-risk index | FULL-TEXT-CONFIRMED | HB-E1: "enforcement of property rights" | DML-E1 preserves the index wording | minor |
| AJR 2001 Table 7 (AJR-E4) | malaria controls do not change results | FULL-TEXT-CONFIRMED | EL-E1: no direct germ effect beyond institutions | HW-E1: "remains a disputed subject" | none |

ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE

Preregistration table: as in SECTION E (reused v1 lock). POST HOC rows anchor no score.

| Claim layer | Adjacent field | Nominated source and stable identifier | Verification state | Source class: CONSTRUCT-DEFINING / MECHANISM-SUPPORTING / DIRECTLY-ADJUDICATING | Actual result | Explanation favored | Explanation weakened | Precise revision required | Pre-inspection lock status or POST HOC | Cited by dominant cluster? | Engagement quality | Effect of omission |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L3 | F1 malaria | X06 W139828295 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | household malaria spending | — | — | — | LOCKED (reused) | no | not cited | minor context loss |
| L3 | F1 malaria | X07 W2088758477 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | socio-economic malaria risk factors | — | — | — | LOCKED (reused) | no | not cited | minor context loss |
| L1/L3 | F2 geography | X08 W2618788771 Gallup–Sachs–Mellinger | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | geography correlates with income | — | — | — | LOCKED (reused) | yes (AJR 2001) | directly tested against | minor context loss |
| L3 | F2 geography | X09 W1492460295 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | geography in development theory | — | — | — | LOCKED (reused) | no | not cited | minor context loss |
| L3 | F3 human capital | X10 W3121822366 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | human-capital growth theory | — | — | — | LOCKED (reused) | no | not cited | minor context loss |
| L3 | F3 human capital | X11 W2035652178 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | schooling-finance growth model | — | — | — | LOCKED (reused) | no | not cited | minor context loss |
| L1/L2 | F4 weak-IV | X12 W2165144879 Staiger–Stock | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | weak-instrument asymptotics | — | — | — | LOCKED (reused) | no | not cited | moderate weakness (routes to lack of decisive tests) |
| L1/L2 | F4 weak-IV | X13 W1980412904 Bound–Jaeger–Baker | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | weak IV biased toward OLS | — | — | — | LOCKED (reused) | yes (AJR-E3) | cited in passing | minor context loss |
| L1 | F6 measurement | X14 W3121147769 North 1990 record | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | definition of institutions | — | — | — | LOCKED (reused) | other North works cited | not cited | minor context loss |
| L1 | F6 measurement | X15 W2010235856 Knack–Keefer | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | ICRG/BERI indices predict growth | — | — | — | LOCKED (reused) | yes (AJR 2001) | substantively engaged | minor context loss |
| L3 | R1 test | ADJ38 W2001123479 Carstensen–Gundlach | ABSTRACT-CONFIRMED; CONTESTED | DIRECTLY-ADJUDICATING | abstract: malaria has a direct income effect alongside institutions | R1 | L3 strong form | L3: institutions a major channel; direct disease channel not excluded | LOCKED (ADJUDICATION-1 search) | UNASSESSED (later AJR-team reference lists not traced) | UNASSESSED because retrieval was insufficient | moderate weakness |
| L3 | R1 test | X03 Sachs 2003 NBER w9490 | FULL-TEXT-CONFIRMED; CONTESTED | DIRECTLY-ADJUDICATING | AJR-style null rejected with malaria risk (SA-E1) | R1 | L3 strong form | as above | POST HOC | UNASSESSED | UNASSESSED because retrieval was insufficient | moderate weakness |
| L3 | R2 test | N04 W2890314743 Glaeser et al. 2004 | FULL-TEXT-CONFIRMED; CONTESTED | DIRECTLY-ADJUDICATING | malaria risk significant alongside settler mortality; human-capital channel (GL-E1, GL-E2) | R1 and R2 | L3 strong form | L3: institutions or settler human capital, not separately identified | POST HOC (RECEPTION-1 member; not returned by the locked search) | acknowledged in NS-E3 | UNASSESSED because retrieval was insufficient | moderate weakness |

ARTIFACT 7: CRITIQUE-UPTAKE TABLE

| Expected-production precondition | Critique / contrary evidence | Year | Source type | Main objection | Verification state | Reception opportunity | Cited by dominant cluster? | Uptake status | Dimension disposition | Effect on consensus |
|---|---|---|---|---|---|---|---|---|---|---|
| strong | Albouy, AER Comment (X02, W1969918011) | 2012 | formal comment | settler-mortality data construction | FULL-TEXT-CONFIRMED; CONTESTED | verified | yes (Reply p. 3078); 72/3,026 recent AJR citers | substantively engaged by the cluster | SCORED 0 | answered; scientific summary cautious (NS-E2) |
| strong | Glaeser et al. (N04) | 2004 | primary empirical | human capital; disease environment | FULL-TEXT-CONFIRMED; CONTESTED | verified | UNASSESSED; 225/3,026 recent AJR citers | UNASSESSED | not scored separately | acknowledged in NS-E3 |

ARTIFACT 8: CARTEL-RISK SCORECARD

| Dimension | Applicability | Dimension disposition | Score if SCORED | Evidence / claim state | Evidence supporting disposition and score | Evidence identifiers | Retrieval coverage | AGGREGATION STATUS | Independent evidence and inferential work, or nesting rationale | Reason excluded from denominator | Effect on formal-label gate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Founding-cluster dominance | applicable | SCORED 1 | 1 | RECEPTION-CONFIRMED | team records receive 109/174 internal edges (67/127 excluding N01); 12/50 team-authored | I02; I03 | 50/50 reference lists | INDEPENDENT | in-edge concentration and authorship records | — | counts toward coverage |
| Internal citation density | applicable | SCORED 0 | 0 | RECEPTION-CONFIRMED | 174/2450 = 7.10% | I01 | 50/50 inputs | INDEPENDENT | overall density | — | affirmative inside RECEPTION-1 only |
| Recent-paper dependence | applicable | SCORED 1 | 1 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (2 passages) | 7/25 cite team works beyond target; 2/2 inspected uses background | I04; I05 | 25/25 reference lists; 2/25 passages | INDEPENDENT | recent corpus distinct from RECEPTION-1 | — | counts toward coverage; under review |
| Review-hub laundering | applicable | UNASSESSED | — | — | downstream hub reliance not traced | I23 | 0 hub-citing passages | — | — | UNASSESSED | label-essential for the healthy band; band withheld |
| Proxy mismatch | applicable | SCORED 1 | 1 | CROSS-SOURCE-CONFIRMED | HB-E1 broadens the construct; DML-E1, HW-E1 preserve it | I09; I10 | hub and 2 independent texts | NESTED under Claim mutation | shares the HB-E1 passage with claim mutation | excluded from aggregate as NESTED | counts toward coverage |
| Claim mutation | applicable | SCORED 1 | 1 | CROSS-SOURCE-CONFIRMED | upper-bound qualifier lost (HB-E1 vs AJR-E2) | I08 | source and hub texts | INDEPENDENT | owns the HB-E1 evidence | — | counts toward coverage |
| Adjacent-field neglect | applicable | SCORED 0 | 0 | FULL-TEXT-CONFIRMED | source engages R1 (AJR-E4) | I19 | source text | INDEPENDENT | source-layer engagement | — | counts toward coverage |
| Lack of decisive tests | applicable | SCORED 0 | 0 | ABSTRACT-CONFIRMED; FULL-TEXT-CONFIRMED; CONTESTED | named direct tests exist; results conflict | I11; I12 | ADJUDICATION-1 56/58 screened | INDEPENDENT | named test results | — | counts toward coverage |
| Poor critique uptake | applicable | SCORED 0 | 0 | FULL-TEXT-CONFIRMED; CONTESTED | Reply answers Albouy | I18 | Reply full text | INDEPENDENT | engagement in the uptake population | — | counts toward coverage |
| Intervention-evidence ratchet | not applicable | N/A | — | — | no intervention claim | — | — | — | — | N/A: no intervention claim | none |
| Model non-updating | applicable | UNASSESSED | — | CONTESTED | four-link gate not traced | — | — | — | — | UNASSESSED | not label-essential |

Verified risk score 3/21; rate 14.3%; independent 7; nested 1; denominator 21; coverage 8/10 (80%); completeness 10/10 (100%).

Verified scored-dimension risk: 14.3%, calculated from 7 independent scored dimensions; 1 additional scored dimensions are NESTED; 8 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.

ARTIFACT 9: NETWORK MAP

Receipts as in SECTION A (RECEPTION-1, 50 nodes, 174 edges, density 174/2450, input coverage 50/50, COMPUTED-FROM-RETRIEVED). Closure beyond RECEPTION-1 is not established and not excluded.

Edge list (CSV, citing,cited):

```
source,target
N01,N06
N01,N07
N01,N35
N01,N19
N01,N42
N01,N25
N01,N38
N01,N13
N01,N30
N02,N01
N02,N06
N02,N42
N02,N18
N02,N25
N03,N01
N04,N01
N04,N06
N04,N02
N04,N32
N04,N18
N04,N25
N05,N29
N05,N01
N05,N25
N05,N03
N05,N30
N06,N18
N07,N01
N09,N01
N09,N06
N09,N18
N09,N05
N09,N42
N09,N26
N09,N30
N10,N01
N10,N27
N11,N29
N11,N01
N11,N05
N11,N25
N11,N03
N11,N30
N12,N01
N13,N01
N15,N06
N15,N07
N15,N42
N16,N01
N16,N06
N16,N18
N16,N05
N16,N42
N16,N26
N17,N01
N17,N06
N17,N45
N17,N18
N17,N09
N18,N01
N20,N01
N20,N04
N20,N50
N20,N42
N20,N25
N20,N26
N20,N02
N21,N01
N21,N33
N21,N04
N21,N42
N21,N25
N21,N02
N21,N13
N22,N01
N22,N23
N22,N02
N23,N01
N23,N06
N23,N02
N23,N22
N23,N18
N24,N01
N24,N06
N24,N18
N24,N20
N25,N01
N25,N06
N26,N01
N26,N06
N26,N50
N26,N18
N26,N39
N27,N02
N27,N32
N27,N04
N28,N01
N28,N02
N28,N32
N29,N01
N29,N06
N29,N35
N29,N07
N29,N18
N29,N09
N29,N25
N30,N01
N31,N04
N32,N01
N32,N42
N32,N18
N32,N25
N33,N01
N33,N15
N33,N07
N33,N21
N35,N01
N35,N07
N36,N01
N38,N01
N39,N01
N39,N06
N39,N50
N39,N18
N39,N09
N39,N26
N40,N01
N40,N04
N40,N39
N40,N48
N40,N09
N40,N25
N40,N20
N41,N01
N41,N06
N41,N32
N41,N18
N41,N25
N41,N02
N42,N01
N42,N06
N42,N18
N42,N25
N42,N26
N44,N01
N44,N02
N44,N04
N45,N01
N45,N04
N45,N16
N45,N17
N45,N09
N46,N01
N46,N06
N46,N02
N46,N32
N46,N18
N46,N25
N47,N04
N48,N01
N48,N06
N48,N04
N48,N17
N48,N09
N48,N20
N49,N01
N49,N42
N50,N01
N50,N06
N50,N16
N50,N18
N50,N39
N50,N09
N50,N26
```

COMPLETION LEDGER

| Required heading | Exact heading present? | Status: completed / N/A / omitted | Reason or output location |
|---|---|---|---|
| `PRE-AUDIT CLAIM CONFIRMATION` | yes | completed | four lines |
| `SECTION A0: CORPUS REGISTER AND SOURCE ELIGIBILITY` | yes | completed | register and ledger |
| `SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION` | yes | completed | receipts, Q1–10 |
| `SECTION B: EVIDENCE TYPE CODING` | yes | completed | Q11–16 |
| `SECTION C: CITATION POLARITY AND CLAIM USE` | yes | completed | Q17–22 |
| `SECTION D: CLAIM MUTATION TRACKING` | yes | completed | Q23–30 |
| `SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT` | yes | completed | lock, tables |
| `SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING` | yes | completed | Q40–47 |
| `SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR` | yes | completed | Q48–56 |
| `SECTION H: IGNORED CRITIQUE AND NON-UPTAKE` | yes | completed | Q57–63 |
| `SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING` | yes | completed | Q64–70 |
| `SECTION J: FALSE-POSITIVE AND BASELINE CHECK` | yes | completed | Q71–80 |
| `SECTION J2: THE CONCEDE TEST` | yes | completed | three tables |
| `SECTION K0: EVIDENCE SUFFICIENCY LEDGER` | yes | completed | ledgers, basis tables |
| `SECTION K: CARTEL-RISK SCORING` | yes | completed | arithmetic, gate |
| `ARTIFACT 1: TOP 15 CITATION SPINE TABLE` | yes | completed | 15 rows |
| `ARTIFACT 2: FOUNDING CLUSTER TABLE` | yes | completed | 4 rows |
| `ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE` | yes | completed | 25 rows |
| `ARTIFACT 4: CITATION POLARITY TABLE` | yes | completed | 15 rows |
| `ARTIFACT 5: CLAIM MUTATION TABLE` | yes | completed | 3 rows |
| `ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE` | yes | completed | 13 rows |
| `ARTIFACT 7: CRITIQUE-UPTAKE TABLE` | yes | completed | 2 rows |
| `ARTIFACT 8: CARTEL-RISK SCORECARD` | yes | completed | 11 dimensions |
| `ARTIFACT 9: NETWORK MAP` | yes | completed | edge CSV |
| `COMPLETION LEDGER` | yes | completed | this table |
| `ARTIFACT 10: FINAL VERDICT` | yes | completed | after ledger |
| `FINAL SECTION: STANDARDIZED FINDING TABLE` | yes | completed | seven findings |

Gate result: PASS.

ARTIFACT 10: FINAL VERDICT

- Main founding cluster: AJR 2001 with Reversal of Fortune, the handbook synthesis and the 2012 Reply; 12/50 RECEPTION-1 records AJR-team authored
- Main amplification hub: Rodrik et al. 2004 (independent, accurate) and the AJR handbook (self-authored, drops the qualifier)
- Main proxy problem: expropriation-risk index restated as property-rights enforcement and economic institutions at the self-authored hub (HB-E1)
- Main adjacent fields neglected: none at the source layer; cluster engagement with later R1/R2 tests not traced
- Main claim mutation: upper-bound qualifier (AJR-E2) lost in HB-E1; popular "clear chain of causality" (NP-E1)
- Most important ignored critique: none established; Albouy answered by the Reply; Glaeser uptake not traced
- Decisive test missing: an instrument-independent cross-country magnitude test (I14 INSUFFICIENT); a human-capital decomposition inside the locked search (I13, bounded)
- Verified risk score: 3/21
- Verified scored-dimension risk rate: 14.3
- Independent scored dimensions: 7
- Nested scored dimensions: 1
- Verified risk denominator: 21
- Evidentiary coverage: 8/10 (80%)
- Execution completeness: 10/10 (100%)
- Dimension inventory: 7 INDEPENDENT SCORED + 1 NESTED SCORED + 0 UNINFORMATIVE + 2 UNASSESSED + 1 N/A
- Unscored dimensions and reasons: Review-hub laundering UNASSESSED (I23); Model non-updating UNASSESSED; Intervention-evidence ratchet N/A
- N-of-M scope statement: Verified scored-dimension risk: 14.3%, calculated from 7 independent scored dimensions; 1 additional scored dimensions are NESTED; 8 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.
- Arithmetic band position: 0%–20% (healthy or low-risk network)
- Risk band: WITHHELD — label-essential: the healthy/low-risk band needs affirmative no-concern evidence on closure-establishing dimensions; claim mutation is SCORED 1, review-hub laundering UNASSESSED, density bounded to a target-selected corpus.
- Mechanism label: self-authored hub qualifier loss (HB-E1) on a shared data origin; no closure signature inside RECEPTION-1
- Formal-label gate status: coverage MET (80%; 70% if the review item is withdrawn; PROVISIONAL threshold); band withheld on label-essential grounds
- Load-bearing finding(s): none against field 6; Findings 2, 3 and 4 for the L3 restatements
- Concede-test result: field 6 SURVIVES every finding; L3 NARROWS (Findings 2, 3, 4)
- Failure location: CITATION (Findings 2, 3, 6, 7); MIXED evidence base (Finding 4); MODEL-RETRIEVAL (Finding 1); none at PAPER for field 6
- Best formal label: insufficient evidence (low arithmetic, but the healthy label's label-essential evidence is missing)
- Confidence level: Low. CITATION CONTEXT COVERAGE: RECEPTION-1 14/50; CITATION CONTEXT COVERAGE: RECENT-1 2/25; CITATION CONTEXT COVERAGE: ADJUDICATION-1 1/58
- What evidence would change this assessment: inspected passages from handbook citers; the 4 unretrieved RECENT-1 sample texts; screening ADJ37 and ADJ44; AJR-team responses to Glaeser; a seed-expanded comparison graph
- Density inference scope: RECEPTION-1 only (OpenAlex cites:W3124166904, top 50, queried 2026-11-05T04:29:45Z UTC); closure is not established and not excluded beyond the defined corpus

FINAL SECTION: STANDARDIZED FINDING TABLE

Finding 1

| Field | Entry |
|---|---|
| Finding | The OpenAlex record and reception corpora of AJR 2001 are unstable: the same query about 17 hours apart returned 12/50 different top citers and a reference list grown from 13 to 55 works. |
| Target claim | MAP GAP: this finding targets the retrieval record of AJR 2001, not map field 6. |
| What was measured | raw/ajr2001_work.json (55 referenced works) vs v1 (13); RECEPTION-1 vs v1 membership; RECENT population 2,695 → 3,026; N01 conflation persists. |
| What was claimed | Database reception corpora are reproducible snapshots of AJR 2001's reception. |
| Failure mode | other: database record drift and identity conflation |
| Severity | moderate for single-database network metrics; none for field 6 |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I24; I03; raw/ajr2001_work.json; raw/reception1_top50.json. |
| Evidence type | author inference |
| Verification state | RECEPTION-CONFIRMED |
| Possible innocent explanation | OpenAlex updates continuously; ties in cited_by_count reorder near the cut-off. |
| What would weaken this | A versioned dump showing the differences are cut-off reordering only. |
| Failure location | MODEL-RETRIEVAL — database record |
| Status | confirmed |

Finding 2

| Field | Entry |
|---|---|
| Finding | Downstream cross-country re-estimates reuse the AJR settler-mortality series, so their agreement is robustness on one data origin. |
| Target claim | MAP GAP: this finding targets L3, not map field 6. |
| What was measured | RD-E1, EL-E2, DML-E1 and the Reply all use the AJR series. |
| What was claimed | Independent studies converge on institutions. |
| Failure mode | source dependence |
| Severity | moderate |
| Concede test | NARROWS |
| Scope loss if NARROWS | material — surviving claim: several teams obtain similar estimates with the AJR series. |
| Evidence | I21; RD-E1; EL-E2; DML-E1. |
| Evidence type | author inference |
| Verification state | FULL-TEXT-CONFIRMED |
| Possible innocent explanation | The instrument is the paper's contribution; reuse is expected in robustness work. |
| What would weaken this | Cross-country tests with an independently built instrument reproducing the magnitude. |
| Failure location | CITATION — aggregation of non-independent tests |
| Status | confirmed |

Finding 3

| Field | Entry |
|---|---|
| Finding | The self-authored handbook restates the magnitude without the authors' upper-bound qualifier and broadens the regressor to property-rights enforcement and economic institutions. |
| Target claim | MAP GAP: this finding targets the hub restatement of the field-6 magnitude, not map field 6. |
| What was measured | AJR-E2 (p. 1387) vs HB-E1 (WP 10481 p. 29). |
| What was claimed | Most of the rich–poor gap is due to economic institutions. |
| Failure mode | claim mutation |
| Severity | moderate |
| Concede test | NARROWS |
| Scope loss if NARROWS | material — surviving claim: up to about a 7-fold gap, an upper bound. |
| Evidence | I08; I09; AJR-E2; HB-E1. |
| Evidence type | author inference |
| Verification state | CROSS-SOURCE-CONFIRMED |
| Possible innocent explanation | Syntheses paraphrase; the published chapter may differ from the WP. |
| What would weaken this | The published Handbook text restoring the qualifier. |
| Failure location | CITATION — self-authored hub |
| Status | confirmed |

Finding 4

| Field | Entry |
|---|---|
| Finding | Direct tests of field 6 and of the disease/geography rival exist, and their results conflict. |
| Target claim | L3 (MAP GAP) and the robustness of the estimate in map field 6. |
| What was measured | ADJUDICATION-1: 24/58 DIRECT; ADJ09, ADJ18, ADJ38 and Sachs report direct geography or malaria effects; Rodrik and Easterly–Levine report institutions dominate; ADJ01 (unreviewed deposit) reports weak-IV-robust sets unbounded under Albouy revisions. |
| What was claimed | Institutions, not geography or disease, are the fundamental cause. |
| Failure mode | other: contested evidence base |
| Severity | moderate |
| Concede test | NARROWS |
| Scope loss if NARROWS | material — surviving claim: institutions a major channel; direct disease effects not excluded. |
| Evidence | I11; I12; I15; abstracts in raw/adj1_Q*.json. |
| Evidence type | primary study |
| Verification state | ABSTRACT-CONFIRMED; FULL-TEXT-CONFIRMED; CONTESTED |
| Possible innocent explanation | The tests use different samples and controls; conflict may reflect specification choice. |
| What would weaken this | A pre-registered multi-specification comparison resolving the conflict. |
| Failure location | MIXED — evidence base |
| Status | contested |

Finding 5

| Field | Entry |
|---|---|
| Finding | Albouy's data critique is substantively answered by the founding cluster. |
| Target claim | In the base sample of 64 former colonies, the 2SLS estimate of the effect of the 1985–95 protection-against-expropriation index on 1995 log GDP per capita, instrumented by log settler mortality, is 0.94 (SE 0.16). |
| What was measured | Reply p. 3078 answers both objections; population co-citation 72/3,026 (descriptive). |
| What was claimed | (Prosecutorial hypothesis) the cluster ignores the critique. |
| Failure mode | none — acquittal on critique uptake |
| Severity | none |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I18; I20. |
| Evidence type | primary study |
| Verification state | FULL-TEXT-CONFIRMED; CONTESTED |
| Possible innocent explanation | Not applicable to an acquittal. |
| What would weaken this | Evidence that the Reply's answers were later withdrawn or refuted. |
| Failure location | CITATION — uptake |
| Status | confirmed |

Finding 6

| Field | Entry |
|---|---|
| Finding | Inside RECEPTION-1 internal density is low; AJR-team records draw many internal edges, mostly via the conflated N01. |
| Target claim | In the base sample of 64 former colonies, the 2SLS estimate of the effect of the 1985–95 protection-against-expropriation index on 1995 log GDP per capita, instrumented by log settler mortality, is 0.94 (SE 0.16). |
| What was measured | Density 174/2450 = 7.10%; team in-edges 109/174, 67/127 excluding N01. |
| What was claimed | (Prosecutorial hypothesis) the estimate's authority rests on a closed cluster. |
| Failure mode | none — acquittal on closure inside the corpus |
| Severity | none |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I01; I02; Section A receipts. |
| Evidence type | author inference |
| Verification state | RECEPTION-CONFIRMED |
| Possible innocent explanation | Not applicable to an acquittal; closure beyond the corpus is not excluded. |
| What would weaken this | A seed-expanded or matched graph with higher closure. |
| Failure location | CITATION — network structure |
| Status | confirmed |

Finding 7

| Field | Entry |
|---|---|
| Finding | Recent citers mostly cite AJR 2001 without other AJR-team works, and the inspected uses are background. |
| Target claim | In the base sample of 64 former colonies, the 2SLS estimate of the effect of the 1985–95 protection-against-expropriation index on 1995 log GDP per capita, instrumented by log settler mortality, is 0.94 (SE 0.16). |
| What was measured | 7/25 cite team works beyond target; 2/2 inspected passages background; 4/6 sampled texts not retrieved. |
| What was claimed | (Prosecutorial hypothesis) recent work recycles the founding cluster. |
| Failure mode | none — provisional acquittal |
| Severity | none |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I04; I05; I06 (INSUFFICIENT). |
| Evidence type | author inference |
| Verification state | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (2 passages) |
| Possible innocent explanation | Not applicable to an acquittal. |
| What would weaken this | The 4 unretrieved sampled passages showing premise use of the estimate. |
| Failure location | CITATION — recent reception |
| Status | provisional |
