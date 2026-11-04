# Citation-Network Audit (Stage 2c) — Acemoglu, Johnson & Robinson (2001)

INSTRUMENT PREFLIGHT: prompts/research-analysis/2-citation-network.txt @ commit ce028e1294873df0143ca1ae00d6abf74a910563 | blob/hash 7ac79f0da337c4d52e39e1490088d06c82a9d42b | 1665 lines | 68231 bytes | markers PRESENT | IDENTITY CONFIRMED

Run metadata. Executor: Grok Bot (audit run), branch audit/acemoglu-colonial-origins. Execution date 2026-11-04 (all clock times below are PST, UTC-8, unless a value is explicitly marked UTC). Mode: full-sequence mode; the upstream Claim Extraction / Inflation Map is examples/research/acemoglu-colonial-origins/01_claim_extraction.md, so the degraded standalone warning does not apply. Available citation tools actually used: OpenAlex works API (primary graph database), Crossref REST API (reference-count cross-check), Semantic Scholar Graph API (attempted; rate-limited, see limitations), publisher/NBER/arXiv/Nobel full texts. Time window for recent behavior: 2021-11-04 to 2026-11-04 (five years before execution).

VALIDATION BOUNDARY (instrument lines 418–427, restated). This instrument has been exercised on supplied packets of up to 26 sources and 70 edges. It is NOT validated for open retrieval. This run used open retrieval over a 50-node citing corpus with 136 internal edges plus a 25-node recent corpus and population-level co-citation counts. Every percentage, band and label below is therefore an unvalidated open-retrieval application of the instrument, and must be read as such.

Exposure disclosure. Before this stage the executor had read AJR (2001) in full, Albouy (2012), the AJR (2012) Reply, and produced the internal-validity, construct-validity and counter-audit stages of this audit. The Section E adjacent-field list was preregistered and hashed at 2026-11-04 03:42:25 PST (2026-11-04T11:42:25Z) before any citing-work record was inspected (lock/section_E_preregistration.md, sha256 84847dd02aca0af819994008ae98d407fae5f75560c8d5de9b628346df965154).

PRE-AUDIT CLAIM CONFIRMATION

- Claim under audit (map field 6): In the base sample of 64 former colonies, the 2SLS estimate of the effect of the 1985–95 protection-against-expropriation index on 1995 log GDP per capita, instrumented by log settler mortality, is 0.94 (SE 0.16).
- What was literally measured in the foundational source(s) (map field 1): 64 former colonies; 1995 log GDP per capita (PPP); Political Risk Services average protection-against-expropriation index 1985–95; log settler mortality compiled from Curtin and other historical sources; OLS and 2SLS regressions (AJR 2001 Table 4).
- Weaker defensible claim (map field 3): in this sample with this instrument, the coefficient on the expropriation index is 0.94 (SE 0.16); the causal reading and the "institutions" reading are conditional on the exclusion restriction and on the index as a proxy, and the implied 7-fold Nigeria–Chile gap is, in the authors' own words, an upper bound.
- Target layer: source claim (map field 6) for the network verdict; downstream citation, PR-media and model-retrieval layers are audited as MAP GAP findings where they concern restatements (L3/L4) rather than the field-6 estimate itself.

The map is upstream-generated, not self-generated, so no PROVISIONAL-map warning applies. Because field 6 is a bare, replicated estimate (reproduced exactly in Stage 2a: 0.94, SE 0.16), a citation network cannot by itself defeat it; most network findings below are therefore either SURVIVES against field 6 or MAP GAP findings aimed at the downstream claim layers L3 ("institutions explain income differences") and L4 (public wording).

SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION

GRAPH CORPUS AND RECEIPTS

GRAPH CORPUS DEFINITION: OpenAlex works API (api.openalex.org), query `filter=cites:W3124166904&sort=cited_by_count:desc&per-page=50&page=1`, executed 2026-11-04 (UTC timestamps in raw/retrieval_log.jsonl), no date bound, all document types, no screening (the top 50 citing works by OpenAlex cited_by_count are taken mechanically), deduplication by OpenAlex work ID (no duplicates occurred), inclusion = every one of the 50 returned works, exclusion = none. Target node N00 = W3124166904 (AJR 2001, DOI 10.1257/aer.91.5.1369) is outside the density corpus; the 50 citer -> N00 edges hold by construction and are not counted. Saved response: raw/top50_citers.json (sha256 recorded in sources/retrieval-manifest.json).
GRAPH CORPUS NODE LIST: N01=W3124131699; N02=W2994756033; N03=W2890314743; N04=W3122778615; N05=W2108614304; N06=W3123436326; N07=W2556507681; N08=W2064927380; N09=W1588189399; N10=W1484474409; N11=W1580107285; N12=W1480274481; N13=W3125697804; N14=W2104834906; N15=W3123261979; N16=W2109890836; N17=W2148534039; N18=W2145309110; N19=W1934649023; N20=W3023420463; N21=W3122513675; N22=W2789051288; N23=W4253884756; N24=W2150851272; N25=W3121534672; N26=W3123293195; N27=W3122513589; N28=W2046507863; N29=W2591654989; N30=W3125767605; N31=W3124753968; N32=W2490362664; N33=W2114854852; N34=W2123148076; N35=W3121354442; N36=W2152556759; N37=W2891506482; N38=W3193006831; N39=W2103130810; N40=W2090766907; N41=W3125033761; N42=W1511665033; N43=W2107205575; N44=W2113596540; N45=W2131499322; N46=W2889827801; N47=W2891433665; N48=W3123773675; N49=W3121532354; N50=W3126058703
INTERNAL EDGE LIST: N01 -> N10; N01 -> N42; N01 -> N24; N01 -> N27; N01 -> N21; N01 -> N04; N01 -> N31; N01 -> N13; N01 -> N30; N02 -> N21; N02 -> N01; N02 -> N31; N03 -> N47; N03 -> N02; N03 -> N21; N03 -> N01; N04 -> N01; N05 -> N01; N05 -> N31; N05 -> N30; N07 -> N19; N07 -> N01; N08 -> N01; N09 -> N21; N09 -> N01; N09 -> N30; N10 -> N01; N11 -> N01; N11 -> N31; N12 -> N05; N12 -> N37; N12 -> N01; N13 -> N42; N14 -> N43; N14 -> N16; N14 -> N02; N14 -> N01; N15 -> N10; N15 -> N45; N15 -> N22; N15 -> N03; N15 -> N02; N15 -> N01; N15 -> N31; N16 -> N14; N16 -> N02; N16 -> N01; N17 -> N03; N17 -> N02; N17 -> N21; N17 -> N01; N17 -> N31; N18 -> N42; N18 -> N40; N18 -> N17; N18 -> N49; N18 -> N01; N19 -> N03; N19 -> N02; N20 -> N03; N20 -> N47; N21 -> N01; N22 -> N04; N22 -> N15; N22 -> N01; N24 -> N01; N25 -> N05; N25 -> N01; N25 -> N41; N25 -> N38; N26 -> N49; N26 -> N50; N27 -> N04; N27 -> N01; N28 -> N01; N29 -> N05; N29 -> N17; N29 -> N03; N29 -> N25; N29 -> N21; N29 -> N01; N30 -> N01; N31 -> N21; N31 -> N01; N33 -> N03; N33 -> N02; N33 -> N01; N34 -> N02; N34 -> N21; N34 -> N01; N35 -> N02; N35 -> N21; N35 -> N01; N36 -> N01; N36 -> N31; N36 -> N38; N37 -> N12; N37 -> N11; N37 -> N05; N37 -> N03; N37 -> N01; N37 -> N38; N39 -> N26; N39 -> N01; N39 -> N50; N40 -> N18; N40 -> N17; N40 -> N03; N40 -> N02; N40 -> N01; N41 -> N05; N41 -> N25; N41 -> N01; N42 -> N01; N43 -> N21; N43 -> N01; N44 -> N05; N44 -> N17; N44 -> N03; N44 -> N02; N44 -> N21; N44 -> N01; N45 -> N21; N45 -> N15; N45 -> N31; N46 -> N10; N46 -> N49; N46 -> N01; N47 -> N02; N47 -> N21; N47 -> N04; N47 -> N01; N48 -> N19; N48 -> N01; N49 -> N01; N50 -> N01
DERIVATION MODE: COMPUTED-FROM-RETRIEVED
DENSITY CALCULATION: directed density = number of directed internal edges u -> v (u, v in N01..N50, u != v, v in OpenAlex referenced_works of u) divided by n(n-1) with n = 50; computed by scripts/graph.py from the saved referenced_works lists.
DENSITY NUMERATOR: 136 directed internal edges among the 50 corpus nodes.
DENSITY DENOMINATOR: 2450 possible directed edges (50 × 49).
DENSITY INPUT COVERAGE: 50/50 reference lists obtained from OpenAlex (5,334 indexed references in total); 49/50 nodes cross-checked against Crossref reference counts (N24 has no DOI). Median OpenAlex/Crossref reference-count ratio 1.46 (min 0.56); OpenAlex reference lists for the corpus are not systematically truncated. The target's own OpenAlex reference list is truncated (13 references indexed for AJR 2001), which does not enter the density numerator.
DENSITY INFERENCE SCOPE: the density result applies only to the top-50 AJR-citing corpus defined above. Because this corpus was selected for citing the target, it can establish density inside that target-citing corpus; it cannot establish or exclude field-wide, founding-cluster, or premise-subnetwork closure. No seed-expanded graph or matched comparison corpus was built.

Closure is not established and not excluded beyond the defined corpus.

Density results. Raw directed density 136/2450 = 5.55%. Excluding N01 (the 2012 Reply, whose OpenAlex record is conflated with the 2001 article: 34 of its 40 in-edges come from works published before 2012, which is time-infeasible for the Reply itself) gives 87/2352 = 3.70%. 46/50 nodes cite at least one other corpus node (35/49 excluding N01); 26/50 cite three or more (12/49 excluding N01). Reciprocal pairs: 14 raw, 6 excluding N01 (N12–N37, N14–N16, N15–N45, N15–N22, N18–N40, N25–N41). Internal references are 136/5,334 = 2.55% of all indexed outbound references of the corpus (1.68% excluding N01). 45 internal edges are time-infeasible on the published dates (34 to N01, 11 others), consistent with working-paper circulation and with OpenAlex version conflation; they are retained in the numerator (conservative toward higher density) and flagged.

1. Top 50 most-cited papers on the central claim. The instrument asks for the most-cited papers "on the central claim". Field 6 is a single estimate; the operational corpus is the top 50 works citing AJR 2001 by citation count (Artifact 1 lists the top 15 with count, year, authors, type and count source; Section B codes all 50). Only 3 of the 50 are primary empirical tests of the institutions-vs-alternatives question (N02 Rodrik et al. 2004, N03 Glaeser et al. 2004, N21 Easterly–Levine 2003) and one is a re-analysis by the original authors (N01). The remaining 46 are highly cited works that use AJR as background, premise, instrument, or worked example.

2. Founding cluster. AJR 2001 itself plus the same team's follow-ups: Reversal of Fortune (AJR 2002, QJE), the 2004 NBER / 2005 Handbook synthesis (N05/N11), and the 2012 Reply (N01). Eight of the top 50 citing works (16%) have at least one of Acemoglu, Johnson or Robinson as author (N01, N05, N11, N25, N27, N30, N31, N41).

3. Founding papers' own evidence type. AJR 2001 is a primary cross-country IV study (FULL-TEXT-CONFIRMED). Reversal of Fortune is a primary cross-country study using pre-colonial urbanization and population density (not retrieved in full this stage; LOCATED). The handbook chapter is a review/synthesis (FULL-TEXT-CONFIRMED in its NBER WP 10481 version). The Reply is a re-analysis of the same settler-mortality data (FULL-TEXT-CONFIRMED).

4. Hub papers. Two hubs: (a) Rodrik, Subramanian & Trebbi 2004 "Institutions Rule" (N02), independent authors, in-degree 12 within the corpus excluding N01, co-cited by 377/2,695 = 14.0% of recent (2021-11-04 onward) AJR citers; (b) the AJR self-authored synthesis (N05 + N11), in-degree 6 within the corpus, co-cited by 276/2,695 = 10.2% of recent AJR citers. The principal critique Glaeser et al. 2004 (N03) is itself a hub (in-degree 9).

5. Do later papers cite the hubs instead of the primary evidence? Partly. Among all recent works citing Rodrik 2004 (1,184), 807 do not cite AJR 2001; among all recent works citing the AJR handbook (1,676), 1,400 do not cite AJR 2001. So the hubs circulate widely without the primary article, but within the AJR-citing population the primary article is cited by construction and the hubs are co-cited by a minority (10–14%).

6. Small cluster repeatedly citing itself? No closed cluster is visible inside the defined corpus: raw density 5.55%, 3.70% excluding the conflated Reply node; the in-degree leaders excluding N01 are N21 Easterly–Levine (12), N02 Rodrik (12), N03 Glaeser (9), N31 AJR volatility (7), N05 AJR handbook (6). Critics and independent teams are as central as the founding team.

7. Founding authors as reviewers/editors/gatekeepers. Not assessable from the retrieved records; no editorial or referee data were retrieved. The founding authors did write the main synthesis hub (N05/N11) and the 2012 Reply in the same AER issue as Albouy's Comment.

8. Self-citation in the founding cluster. Within the corpus, AJR-authored nodes cite each other (e.g., N05 -> N01, N05 -> N31, N05 -> N30, N11 -> N31, N25 -> N41 reciprocal), and the handbook restates the 2001 result (Section D). This is ordinary programme self-citation; it matters here only because the self-authored hub drops a qualifier (Finding 3).

9. Disproportionately cited by one lab/institution/journal/funder. AJR-authored works are 8/50 of the top citers; MIT/Harvard/NBER affiliations are common in the top 50, which is the normal centre of the field (see Section I). No single funder could be assessed.

10. Is the network small enough that citation count overstates independent confirmation? The network is not small (OpenAlex cited_by_count 8,594 for AJR 2001; Crossref 7,813; Semantic Scholar 12,600; union of the 2001 and 2012 OpenAlex records 11,316). But independent confirmation is much narrower than the count: every cross-country "confirmation" in the top 50 that re-estimates the institutions effect (N01, N02, N21, N06, N31) uses the AJR settler-mortality series as instrument or data (Finding 2). Citation count therefore overstates the number of independent information origins for L3.

SECTION B: EVIDENCE TYPE CODING

All 50 corpus nodes are coded below with the Section B vocabulary. "Primary empirical study (not of the central claim)" is used for primary empirical work on a different question that cites AJR as background or premise; the instrument's list has no off-claim code, so this wording is a plain description, not a new code. Coding was done from abstracts (39/50 retrieved through OpenAlex) and, where noted, full texts.

| Node | OpenAlex ID | Year | Authors (first 3) | Title | Evidence type | Relation to central claim | Verification state of coding |
|---|---|---:|---|---|---|---|---|
| N01 | W3124131699 | 2012 | Daron Acemoğlu, Simon Johnson, James A. Robinson | The Colonial Origins of Comparative Development: An Empirical Investigation: Reply | secondary analysis | central claim; authors' reply re-analysing AJR data | FULL-TEXT-CONFIRMED (version noted in Section C) |
| N02 | W2994756033 | 2004 | Dani Rodrik, Arvind Subramanian, Francesco Trebbi | Institutions Rule: The Primacy of Institutions Over Geography and Integration in Economic Development | primary empirical test of the central claim | reuses AJR settler-mortality instrument | FULL-TEXT-CONFIRMED (version noted in Section C) |
| N03 | W2890314743 | 2004 | Edward L. Glaeser, Rafael La Porta, Florencio López‐de‐Silanes | Do Institutions Cause Growth? | primary empirical test of the central claim | critical; reuses AJR instrument, adds human-capital tests | FULL-TEXT-CONFIRMED (version noted in Section C) |
| N04 | W3122778615 | 2003 | Raghuram G. Rajan, Luigi Zingales | The great reversals: the politics of financial development in the twentieth century | primary empirical study (not of the central claim) | financial development; background citation | FULL-TEXT-CONFIRMED (version noted in Section C) |
| N05 | W2108614304 | 2004 | Daron Acemoğlu, Simon Johnson, James A. Robinson | Institutions as the Fundamental Cause of Long-Run Growth | review article | self-authored synthesis hub (NBER WP) | FULL-TEXT-CONFIRMED (version noted in Section C) |
| N06 | W3123436326 | 2017 | Victor Chernozhukov, Denis Chetverikov, Mert Demirer | Double/debiased machine learning for treatment and structural parameters | theoretical / conceptual paper | econometric method; re-analyses AJR 64-country data as an example | FULL-TEXT-CONFIRMED (version noted in Section C) |
| N07 | W2556507681 | 2016 | Simone Raudino | The Theory of Economic Development | unclear / needs source audit | OpenAlex record likely misattributed (book chapter) | LOCATED |
| N08 | W2064927380 | 2007 | César A. Hidalgo, Bailey Klinger, Albert-Ĺaszló Barabási | The Product Space Conditions the Development of Nations | primary empirical study (not of the central claim) | product space; background citation | FULL-TEXT-CONFIRMED (version noted in Section C) |
| N09 | W1588189399 | 2005 | Ross Eric Levine | Chapter 12 Finance and Growth: Theory and Evidence | review article | finance and growth; background citation | FULL-TEXT-CONFIRMED (version noted in Section C) |
| N10 | W1484474409 | 2006 | Halvor Mehlum A, Karl Ove Moene, Ragnar Torvik | Institutions and the Resource Curse | primary empirical study (not of the central claim) | institutions x resource curse; adjacent | ABSTRACT-CONFIRMED |
| N11 | W1580107285 | 2005 | Daron Acemoğlu, Simon Johnson, James A. Robinson | Chapter 6 Institutions as a Fundamental Cause of Long-Run Growth | review article | self-authored synthesis hub (Handbook chapter) | LOCATED |
| N12 | W1480274481 | 2008 | Eric Alan Hanushek, Ludger Woessmann | The Role of Cognitive Skills in Economic Development | review article | human capital and growth; rival R2 field | FULL-TEXT-CONFIRMED (version noted in Section C) |
| N13 | W3125697804 | 2004 | Wolfgang Keller | International Technology Diffusion | review article | technology diffusion; background | ABSTRACT-CONFIRMED (working-paper full text retrieved does not cite AJR; version mismatch) |
| N14 | W2104834906 | 2014 | Melissa Dell, Benjamin F. Jones, Benjamin Olken | What Do We Learn from the Weather? The New Climate-Economy Literature | review article | climate-economy; geography-adjacent | FULL-TEXT-CONFIRMED (version noted in Section C) |
| N15 | W3123261979 | 2011 | Frederick van der Ploeg | Natural Resources: Curse or Blessing? | review article | resource curse; adjacent | ABSTRACT-CONFIRMED |
| N16 | W2109890836 | 2012 | Melissa Dell, Benjamin F. Jones, Benjamin Olken | Temperature Shocks and Economic Growth: Evidence from the Last Half Century | primary empirical study (not of the central claim) | temperature shocks; geography-adjacent | ABSTRACT-CONFIRMED (working-paper full text retrieved does not cite AJR; version mismatch) |
| N17 | W2148534039 | 2010 | Guido Tabellini | Culture and Institutions: Economic Development in the Regions of Europe | primary empirical study (not of the central claim) | culture and institutions in European regions | ABSTRACT-CONFIRMED |
| N18 | W2145309110 | 2011 | Nathan Nunn, Léonard Wantchekon | The Slave Trade and the Origins of Mistrust in Africa | primary empirical study (not of the central claim) | historical persistence (slave trade, trust) | ABSTRACT-CONFIRMED |
| N19 | W1934649023 | 2005 | Daniel Kaufmann, Aart Kraay, Massimo Mastruzzi | Governance Matters IV : Governance Indicators For 1996-2004 | secondary analysis | governance indicator construction; construct-adjacent | ABSTRACT-CONFIRMED |
| N20 | W3023420463 | 2005 | Jakob Svensson | Eight Questions about Corruption | review article | corruption; background | ABSTRACT-CONFIRMED |
| N21 | W3122513675 | 2003 | William Russell Easterly, Ross Eric Levine | Tropics, germs, and crops: how endowments influence economic development | primary empirical test of the central claim | reuses AJR settler-mortality series | FULL-TEXT-CONFIRMED (version noted in Section C) |
| N22 | W2789051288 | 2009 | Timothy J. Besley, Torsten Persson | The Origins of State Capacity: Property Rights, Taxation, and Politics | theoretical / conceptual paper | state capacity | ABSTRACT-CONFIRMED |
| N23 | W4253884756 | 2010 | Christopher Blattman, Edward A. Miguel | Civil War | review article | civil war; background | ABSTRACT-CONFIRMED |
| N24 | W2150851272 | 2010 | Globalisation Programme, Stephen J. Redding, Anthony J. Venables | 1 Economic Geography and International Inequality | primary empirical study (not of the central claim) | economic geography; rival-adjacent | ABSTRACT-CONFIRMED |
| N25 | W3121534672 | 2005 | Daron Acemoğlu, Simon Johnson, James A. Robinson | Income and Democracy | primary empirical study (not of the central claim) | income and democracy (AJR team) | ABSTRACT-CONFIRMED |
| N26 | W3123293195 | 2010 | Joshua D. Angrist, Jörn‐Steffen Pischke | The Credibility Revolution in Empirical Economics: How Better Research Design is Taking the Con out of Econome | commentary / editorial | econometric-methods essay | ABSTRACT-CONFIRMED |
| N27 | W3122513589 | 2002 | Simon Johnson, Todd Mitton | Cronyism and capital controls: evidence from Malaysia | primary empirical study (not of the central claim) | cronyism, Malaysia (Johnson co-author) | LOCATED |
| N28 | W2046507863 | 2006 | Michael Ross Carter, Christopher B. Barrett | The economics of poverty traps and persistent poverty: An asset-based approach | theoretical / conceptual paper | poverty traps | ABSTRACT-CONFIRMED |
| N29 | W2591654989 | 2015 | Alberto Alesina, Paola Giuliano | Culture and Institutions | review article | culture and institutions | ABSTRACT-CONFIRMED |
| N30 | W3125767605 | 2006 | Daron Acemoğlu, Philippe Aghion, Fabrizio Zilibotti | Distance to Frontier, Selection, and Economic Growth | theoretical / conceptual paper | growth theory (Acemoglu co-author) | ABSTRACT-CONFIRMED |
| N31 | W3124753968 | 2003 | Daron Acemoğlu, Simon Johnson, James A. Robinson | Institutional causes, macroeconomic symptoms: volatility, crises and growth | primary empirical study (not of the central claim) | volatility; reuses AJR instrument (AJR team) | LOCATED |
| N32 | W2490362664 | 2004 | Alberto Alesina, Edward L. Glaeser | Fighting Poverty in the US and Europe | secondary analysis | book; redistribution US vs Europe | ABSTRACT-CONFIRMED |
| N33 | W2114854852 | 2007 | Daniel S. Treisman | What Have We Learned About the Causes of Corruption from Ten Years of Cross-National Empirical Research? | review article | corruption | ABSTRACT-CONFIRMED |
| N34 | W2123148076 | 2008 | Bo Rothstein, Jan Teorell | What Is Quality of Government? A Theory of Impartial Government Institutions | theoretical / conceptual paper | quality of government; construct-defining | ABSTRACT-CONFIRMED |
| N35 | W3121354442 | 2005 | Matthew E. Kahn | The Death Toll from Natural Disasters: The Role of Income, Geography, and Institutions | primary empirical study (not of the central claim) | natural-disaster deaths | ABSTRACT-CONFIRMED |
| N36 | W2152556759 | 2008 | Valerie Cerra, Sweta Saxena | Growth Dynamics: The Myth of Economic Recovery | primary empirical study (not of the central claim) | output after crises | ABSTRACT-CONFIRMED |
| N37 | W2891506482 | 2012 | Eric Alan Hanushek, Ludger Woessmann | Do better schools lead to more growth? Cognitive skills, economic outcomes, and causation | primary empirical study (not of the central claim) | cognitive skills and growth; rival R2 field | LOCATED |
| N38 | W3193006831 | 2005 | Ricardo Hausmann, Lant H. Pritchett, Dani Rodrik | Growth Accelerations | primary empirical study (not of the central claim) | growth accelerations | LOCATED |
| N39 | W2103130810 | 2010 | Angus Deaton | Instruments, Randomization, and Learning about Development | commentary / editorial | critique of IV and RCT practice in development | ABSTRACT-CONFIRMED |
| N40 | W2090766907 | 2010 | Yann Algan, Pierre Cahuc | Inherited Trust and Growth | primary empirical study (not of the central claim) | inherited trust and growth | ABSTRACT-CONFIRMED |
| N41 | W3125033761 | 2008 | Daron Acemoğlu, James A. Robinson | Persistence of Power, Elites, and Institutions | theoretical / conceptual paper | persistence of power (Acemoglu-Robinson) | ABSTRACT-CONFIRMED |
| N42 | W1511665033 | 2005 | Abhijit Banerjee, Lakshmi Iyer | History, Institutions, and Economic Performance: The Legacy of Colonial Land Tenure Systems in India | primary empirical study (not of the central claim) | within-India colonial land institutions; independent data origin for L3 | ABSTRACT-CONFIRMED |
| N43 | W2107205575 | 2009 | Richard S.J. Tol | The Economic Effects of Climate Change | review article | climate-change damages | ABSTRACT-CONFIRMED |
| N44 | W2113596540 | 2013 | Andrés Rodríguez‐Pose | Do Institutions Matter for Regional Development? | review article | regional development and institutions | ABSTRACT-CONFIRMED |
| N45 | W2131499322 | 2012 | Xavier Sala-i-Martín, Arvind Subramanian | Addressing the Natural Resource Curse: An Illustration from Nigeria | primary empirical study (not of the central claim) | resource curse, Nigeria | ABSTRACT-CONFIRMED |
| N46 | W2889827801 | 2009 | Nathan Nunn, Diego Puga | Ruggedness: The Blessing of Bad Geography in Africa | primary empirical study (not of the central claim) | ruggedness; geography x history | ABSTRACT-CONFIRMED |
| N47 | W2891433665 | 2003 | Simeon Djankov, Edward L. Glaeser, Rafael La Porta | The New Comparative Economics | theoretical / conceptual paper | comparative-economics framework | LOCATED |
| N48 | W3123773675 | 2007 | Andrei A. Levchenko | Institutional Quality and International Trade | primary empirical study (not of the central claim) | institutions and trade | ABSTRACT-CONFIRMED |
| N49 | W3121532354 | 2008 | Nathan Nunn | The Long-Term Effects of Africa's Slave Trades * | primary empirical study (not of the central claim) | slave trades; historical persistence | ABSTRACT-CONFIRMED |
| N50 | W3126058703 | 2008 | Raghuram G. Rajan, Arvind Subramanian | Aid and Growth: What Does the Cross-Country Evidence Really Show? | primary empirical study (not of the central claim) | aid and growth | ABSTRACT-CONFIRMED |

Tally: primary empirical test of the central claim 3 (N02, N03, N21); secondary analysis 3 (N01, N19, N32); review article 13; theoretical / conceptual paper 7; commentary / editorial 2 (N26, N39); unclear / needs source audit 1 (N07); primary empirical study not of the central claim 21. No systematic review / meta-analysis, policy / guideline document, qualitative study, survey study or public-facing synthesis appears in the top 50 (the Nobel popular background, a public-facing synthesis, is analysed outside the corpus in Section D).

11. Primary empirical tests of the central claim: 3/50 (6%) — N02, N03, N21 — plus the authors' own re-analysis N01. All four rely on the AJR settler-mortality series.
12. Proxy studies: none of the top 50 is a proxy study for field 6 in the instrument's sense; however the field-6 regressor is itself a proxy (PRS expropriation-risk index for "institutions"), and downstream users mostly substitute other governance indices (e.g., Kaufmann–Kraay–Mastruzzi N19) without discussing comparability (see Section C).
13. Reviews or commentaries: 13 review articles and 2 commentaries (30%).
14. Reviews citing other reviews rather than primary evidence: the AJR handbook (N05/N11) cites the Reply-conflated node and N31/N30 and restates AJR 2001 directly; Levine's finance review (N09) cites N21 and N30. There is no review-only chain that bypasses AJR 2001 inside this corpus (every node cites AJR by construction).
15. Papers cited as if they answer the central claim while measuring something narrower: the expropriation-risk coefficient is cited as the effect of "economic institutions" or "property rights" (handbook HB-E1) — this is the CV-1 construct issue at the citation layer (Finding 3).
16. Is the network built on direct evidence, proxies, theory, reviews, or repeated citation? On one direct-but-proxied primary estimate (AJR 2001) whose data are reused, plus a large mass of downstream users who cite it as background premise. Direct independent re-tests of the institutions-vs-geography claim with independent data origins are rare in the corpus; within-country designs with independent data (N42 Banerjee–Iyer) bear on L3 but not on the field-6 magnitude.

SECTION C: CITATION POLARITY AND CLAIM USE

Polarity was coded only where the citing passage was retrieved; otherwise "unclear without full text". Full texts retrieved: N01, N02 (NBER WP 9305), N03 (NBER WP 10568), N04 (NBER w8178), N05 (NBER WP 10481), N06 (arXiv 1608.00060), N08 (arXiv 0708.2090), N09 (NBER w10766), N12 (NBER w12832), N13 (NBER w8573, 2001 WP), N14 (NBER w19578), N16 (NBER w14132), N21 (NBER WP 9106). Retrieval failed for N10 (sv.uio.no HTTP 404) and N15 (ora.ox.ac.uk HTTP 500 ×3).

17. Supportive: N01 (self, defence), N02 (supportive of the identification strategy, "AER (American Economic Review)-test", RD-E1), N05/N11 (self, premise-building), N06 (methodological reuse; "qualitatively similar", DML-E2), N21 (EL-E1: no direct effect of tropics, germs, crops other than through institutions).
18. Neutral/background: N08 (product-space background list), N09 (finance survey background), N12 (background, preserves dispute: "this remains a disputed subject (cf., e.g., McArthur and Sachs (2001))", HW-E1), N14 (accurate background on the settler-mortality channel).
19. Critical: N03 (Glaeser et al., GL-E1 and GL-E2: malaria risk significant alongside settler mortality; human-capital channel), and N02 on interpretation (RD-E3, RD-E4: the institutions/policies distinction is "not made adequately clear in AJR"; "AJR do not carry out a direct test of the impact of colonial policies and institutions").
20. Perfunctory: N04 Rajan–Zingales (the retrieved WP cites only Acemoglu and Johnson 2000 in text; AJR 2001 appears only in the reference list). Version mismatch: N13 and N16 (the retrieved working-paper versions do not cite AJR at all; the OpenAlex edge comes from the published version).
21. Used as premise without examining limitations: the handbook restatement (HB-E1) and the Nobel popular background (NP-E1). Downstream recent users (Artifact 3) mostly cite AJR as a premise for using institutional-quality indices; their citing passages were not retrieved, so this is ABSTRACT-CONFIRMED at most.
22. Cited for claims it did not establish: the handbook's "most of the gap between rich and poor countries today is due to differences in economic institutions" and "almost the entire difference in incomes per-capita between them could be explained by the differences in the security of property rights" (HB-E1, citing p. 1387) state as established what AJR p. 1387 labels an upper bound (AJR-E2). The Nobel popular text's "clear chain of causality" (NP-E1) exceeds the scientific background's "grain of salt" (NS-E1).

The full top-15 polarity table is Artifact 4.

SECTION D: CLAIM MUTATION TRACKING

23. Original measured claim: the 2SLS coefficient 0.94 (SE 0.16) on the PRS expropriation index in 64 colonies (field 6), with the authors' magnitude illustration "as much as a 7-fold increase in Nigeria's income" (AJR-E1) and the explicit caveat "the presence of measurementerrorcomplicatesthis interpretation … Therefore,the 7-fold differenceis an upperbound" (AJR-E2, PDF p. 20 = AER p. 1387).
24. Original limitations: measurement error in the index (upper-bound caveat), the exclusion restriction (tested with geography, malaria, religion, legal origin controls; AJR-E4 shows the malaria control lowers the coefficient to 0.69, SE 0.25), small sample (64), the too-many-instruments problem (AJR-E3), and the proxy nature of the index (fn 3 / CV-1).
25. Restatement by hubs: Rodrik 2004 adopts the instrument as validated by the "AER-test" (RD-E1) while criticising interpretation (RD-E3, RD-E4). The AJR handbook restates the result as "most of the gap … is due to differences in economic institutions" and, citing p. 1387, "almost the entire difference … could be explained by the differences in the security of property rights" (HB-E1).
26. Restatement by recent papers: recent top-cited citers use AJR as background for regressions on governance indicators (Artifact 3); citing passages were not retrieved, so recent restatement wording is UNASSESSED beyond abstracts.
27. Did the claim become broader, stronger, more causal, more general, or more policy-relevant? Yes, at two loci: the self-authored hub (broader construct "economic institutions"/"security of property rights", stronger magnitude without the upper-bound qualifier) and the popular Nobel text (more causal: "clear chain of causality"). The Nobel scientific background preserves limits ("grain of salt", NS-E1; Albouy criticism acknowledged, NS-E2; "very hard to distinguish … human capital", NS-E3).
28. Were limitations lost? The upper-bound qualifier is lost in HB-E1 on the very page it cites; DML (DML-E1) preserves the proxy wording ("a proxy for the strength of institutions"); Hanushek–Woessmann preserves the dispute (HW-E1).
29. Did proxy findings become direct claims? Yes in HB-E1 ("security of property rights" and "economic institutions" for an expropriation-risk rating).
30. Did correlation become causation? Not at the source layer (AJR is an IV design making a conditional causal claim). The popular Nobel wording turns a conditional IV inference into "a clear chain of causality".

| Original source | Original measured claim | Hub-paper restatement | Downstream restatement | Mutation severity | Notes |
|---|---|---|---|---|---|
| AJR 2001, AER p. 1387 (AJR-E2) | 0.94 implies about a 7-fold Nigeria–Chile difference; "the 7-fold differenceis an upperbound" | AJR 2004/2005 handbook (HB-E1): "almost the entire difference … could be explained by the differences in the security of property rights" | Nobel popular 2024 (NP-E1): "a clear chain of causality" | moderate (hub); minor (public) | Hub is self-authored; Nobel scientific background (NS-E1) preserves "grain of salt" |
| AJR 2001 Table 4 (field 6) | coefficient on PRS expropriation index | Handbook: "economic institutions" (HB-E1) | DML 2018: "a proxy for the strength of institutions" (DML-E1) | minor | Construct broadening at the self-hub; independent methods users preserve proxy status |
| AJR 2001 Table 7 (AJR-E4) | malaria control lowers estimate to 0.69 (SE 0.25), still significant | Easterly–Levine (EL-E1): no direct effect of germs other than through institutions | Hanushek–Woessmann (HW-E1): "remains a disputed subject" | none | Disagreement preserved downstream; Glaeser (GL-E1) and Sachs (SA-E1) contest |

SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT

Steps 31–37 were executed and locked before any citing-work record was inspected (lock/section_E_preregistration.md, hashed; locked at 2026-11-04 03:42:25 PST). Claim layers: L1 field-6 estimate; L2 field-3 weaker claim; L3 downstream "institutions explain income differences"; L4 public wording. Rivals: R1 direct geography/disease channel (strongest live rival, used for the flip test); R2 human capital carried by settlers. Adjudicating observations: O1 disease-burden effects with institutions held fixed; O2 geography effects conditional on independently measured institutions; O3 decomposition of settler effects into human-capital vs institutional channels; O4 reliability of 2SLS with weak or noisy instruments. Candidate fields: F1 malaria/tropical-disease economics (from R1), F2 geography and development (R1), F3 human capital and growth (R2), F4 weak-instrument econometrics (both), F5 historical troop-mortality epidemiology (both; excluded because it is the instrument's own data source, not independent), F6 measurement of institutional quality (audited claim; construct-defining).

SOURCE-LOCK METHOD: LOCKED QUERY
SOURCE-LOCK DATABASE: OpenAlex works API (api.openalex.org), executed once; raw JSON responses saved and hashed
SOURCE-LOCK QUERY OR SOURCE LIST: filter=title.search:<terms>,to_publication_date:2000-12-31,type:article with terms F1 "malaria economic", F2 "geography economic development", F3 "human capital growth", F4 "weak instruments", F6 "institutions economic performance"
SOURCE-LOCK DATE CUTOFF: 2000-12-31 (publication on or before)
SOURCE-LOCK RANKING RULE: OpenAlex cited_by_count descending at query time
SOURCE-LOCK N: 10 (top 2 per field × 5 fields)
SOURCE-LOCK DEDUPLICATION RULE: by OpenAlex work ID; exact duplicates counted once; off-topic or mis-typed items retained and flagged, never replaced
SOURCE-LOCK TIMESTAMP OR HASH: 2026-11-04T11:42:25Z (03:42:25 PST); preregistration sha256 84847dd02aca0af819994008ae98d407fae5f75560c8d5de9b628346df965154; locked result list sha256 521b3a52716a5dc75e8684bf7464cb3d90aea124815282d19ff82ee25f855a3c

Flip test (step 37): PASS — F1 and F2 were generated from R1 itself and F3 from R2; F4 from both; the field set does not depend on which explanation is favored. A competent auditor favoring R1 would produce materially the same field list; the per-field exemplars are fixed by the query, not by the auditor.

Innocent explanations tested (step 39). F1 exemplars returned by the locked query (household malaria-expenditure studies in Malawi and The Gambia) measure household cost and risk factors, not country-level income effects; their non-citation is explained by scope mismatch, and AJR engages the same field through Gallup & Sachs (1998) malaria data and Table 7 (AJR-E4) — redundancy, not neglect. F2 exemplar Gallup–Sachs–Mellinger is cited by AJR in its NBER WP 6849 version and its variables are used as controls (directly tested against). F3 exemplars (Becker–Murphy–Tamura 1990; Glomm–Ravikumar 1992) are growth theory without cross-country tests that could discriminate R2 from institutions; non-citation is a reasonable disciplinary boundary, and the R2 test only became available with Glaeser et al. (2004), after the source. F4: Bound–Jaeger–Baker 1995 is cited (AJR-E3, as the too-many-instruments reference); Staiger–Stock 1997 is not; a missing methods paper routes to lack of decisive tests, not to neglect. F6: Knack–Keefer 1995 is the source of the PRS data and is substantively used; the OpenAlex record W3121147769 is North (1990) "Institutions, Institutional Change and Economic Performance", mis-typed as a Southern Economic Journal article (a review record); AJR cites other North works (1981; North & Thomas 1973; North et al.), so non-citation of the 1990 book is redundancy.

Falsification-relevant literature preregistration table:

| Claim layer | Audited explanation | Strongest plausible rival explanation | Adjudicating observation | Candidate field | Generated from audited claim, rival, or both? | Measurement relevance | Adjudicative capacity | Independence | Publication-date cutoff | Historically available? | Flip-test result | Source-lock method | Lock timestamp / hash | Final engagement classification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1/L3 | colonial institutions (proxied by expropriation risk) drive income | R1 direct disease channel | O1 disease-burden income effects with institutions fixed | F1 malaria economics | rival | measures disease burden | could weaken L3 | independent of AJR data | 2000-12-31 | yes | PASS | LOCKED QUERY | 2026-11-04T11:42:25Z; 84847dd0…5154 | direct substantive engagement (via Gallup–Sachs malaria variable, Table 7); locked exemplars not cited (scope mismatch) |
| L1/L3 | as above | R1 direct geography channel | O2 geography conditional on institutions | F2 geography and development | rival | measures geographic correlates | could weaken L3 | independent | 2000-12-31 | yes | PASS | LOCKED QUERY | as above | direct substantive engagement (Gallup–Sachs–Mellinger cited and its controls tested) |
| L3 | as above | R2 settler human capital | O3 human-capital vs institutions decomposition | F3 human capital and growth | rival | measures schooling effects | could weaken L3 | independent | 2000-12-31 | partly (theory only; decomposition test appears 2004) | PASS | LOCKED QUERY | as above | no located engagement after adequate search (locked theory exemplars); innocent: disciplinary boundary and timing |
| L1/L2 | as above | inference artefact from weak/noisy instrument | O4 reliability of 2SLS | F4 weak-IV econometrics | both | determines inferential validity | could narrow L1/L2 | independent | 2000-12-31 | yes | PASS | LOCKED QUERY | as above | citation without substantive engagement (Bound et al. cited for too-many-instruments; Staiger–Stock not cited) |
| L1 | as above | not a rival test | construct definition of the regressor | F6 institutional-quality measurement | audited claim | defines regressor | construct-defining only | partly shared provider (PRS/ICRG) | 2000-12-31 | yes | PASS | LOCKED QUERY | as above | direct substantive engagement (Knack–Keefer data source) |
| L1 | as above | not independent | instrument construct | F5 troop-mortality epidemiology | both | defines instrument | none independent (it is the data source) | NOT independent | 2000-12-31 | yes | PASS | LOCKED QUERY (field excluded) | as above | excluded from nomination; UNINFORMATIVE as an adjacent check |

Adjacent-literature neglect table (Section E form):

| Claim layer | Adjacent field | Nominated source and stable identifier | Verification state | Source class: CONSTRUCT-DEFINING / MECHANISM-SUPPORTING / DIRECTLY-ADJUDICATING | Actual result | Explanation favored | Explanation weakened | Precise revision required | Pre-inspection lock status or POST HOC | Cited by dominant cluster? | Engagement quality | Effect of omission |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L3 | F1 malaria economics | Economic impact of malaria in Malawian households (1994), OpenAlex W139828295 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | very-low-income households spend little on malaria prevention | — | — | — | LOCKED | no (AJR 2001 no; top-50 0/50) | not cited | minor context loss |
| L3 | F1 malaria economics | Gambia peri-urban malaria risk factors 1995, DOI 10.1016/0035-9203(95)90471-9, OpenAlex W2088758477 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | socio-economic risk factors for malaria | — | — | — | LOCKED | no (0/50) | not cited | minor context loss |
| L1/L3 | F2 geography and development | Gallup, Sachs & Mellinger 1999, DOI 10.1177/016001799761012334, OpenAlex W2618788771 | ABSTRACT-CONFIRMED (its citation in the AJR 2001 reference list as NBER WP 6849 is FULL-TEXT-CONFIRMED) | MECHANISM-SUPPORTING | geography correlates strongly with income | — | — | — | LOCKED | yes (AJR 2001; top-50 6/50; recent 76/2,695) | directly tested against | minor context loss |
| L3 | F2 geography and development | Development, Geography, and Economic Theory, DOI 10.2307/144349, OpenAlex W1492460295 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | theoretical treatment of geography in development | — | — | — | LOCKED | no (0/50) | not cited | minor context loss |
| L3 | F3 human capital and growth | Becker, Murphy & Tamura 1990, DOI 10.1086/261723, OpenAlex W3121822366 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | growth theory with human-capital accumulation | — | — | — | LOCKED | no (0/50) | not cited | minor context loss |
| L3 | F3 human capital and growth | Glomm & Ravikumar 1992, DOI 10.1086/261841, OpenAlex W2035652178 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | public vs private schooling growth model | — | — | — | LOCKED | no (0/50) | not cited | minor context loss |
| L1/L2 | F4 weak-IV econometrics | Staiger & Stock 1997, DOI 10.2307/2171753, OpenAlex W2165144879 | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | weak-instrument asymptotics; first-stage strength diagnostics | — | — | — | LOCKED | no (AJR 2001 no; top-50 2/50; recent 37/2,695) | not cited | moderate weakness (routes to lack of decisive tests) |
| L1/L2 | F4 weak-IV econometrics | Bound, Jaeger & Baker 1995, DOI 10.1080/01621459.1995.10476536, OpenAlex W1980412904 | ABSTRACT-CONFIRMED (its citation in AJR fn 29 is FULL-TEXT-CONFIRMED) | CONSTRUCT-DEFINING | weak instruments bias IV toward OLS | — | — | — | LOCKED | yes (AJR-E3; top-50 1/50; recent 3/2,695) | cited in passing | minor context loss |
| L1 | F6 institutional measurement | North 1990 book (OpenAlex W3121147769, mis-typed as journal article) | ABSTRACT-CONFIRMED (record mis-typed) | CONSTRUCT-DEFINING | conceptual definition of institutions | — | — | — | LOCKED (mis-typed item retained, flagged) | no for this record; other North works cited (top-50 13/50) | not cited | minor context loss |
| L1 | F6 institutional measurement | Knack & Keefer 1995, OpenAlex W2010235856 | ABSTRACT-CONFIRMED (AJR use of its PRS data is FULL-TEXT-CONFIRMED) | CONSTRUCT-DEFINING | ICRG/BERI institutional indices predict growth | — | — | — | LOCKED | yes (AJR 2001; top-50 11/50; recent 165/2,695) | substantively engaged | minor context loss |
| L3 | rival-explanation test (R1) | Sachs 2003, NBER WP 9490 | FULL-TEXT-CONFIRMED; CONTESTED | DIRECTLY-ADJUDICATING | "the null hypothesis may be readily rejected using an alternative geographical variable: malaria risk" (SA-E1) | R1 (direct disease effect) | L3 strong form (institutions as sole fundamental channel) | L3 must read "institutions are a major channel; a direct disease channel is not excluded" | POST HOC | no in AJR 2001 (timing); union AJR citers 494/11,316 = 4.4%; recent 67/2,695 = 2.5% | cited in passing (AJR-team engagement not retrieved; rarely co-cited by downstream citers) | moderate weakness |
| L3 | rival-explanation test (R2) | Glaeser et al. 2004, NBER WP 10568 | FULL-TEXT-CONFIRMED; CONTESTED | DIRECTLY-ADJUDICATING | malaria risk significant alongside settler mortality; instruments may work through human capital (GL-E1, GL-E2) | R1 and R2 | L3 strong form; exclusion restriction behind field 6's causal reading | L3 must read "institutions or settler human capital (not separately identified)"; field 6 unchanged as an estimate | POST HOC | union 1,539/11,316 = 13.6%; 2005+ 1,524/10,897 = 14.0%; recent 202/2,695 = 7.5%; top-50 in-degree 9 | substantively engaged (Nobel background NS-E3 records an Acemoglu, Gallego and Robinson response; that response was not retrieved) | moderate weakness |

The two POST HOC rows were added after citation inspection, are labelled POST HOC, do not erase the locked-list result, and may support at most SCORED 1 on adjacent-field neglect.

SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING

40. Main hubs: Rodrik, Subramanian & Trebbi 2004 (independent amplification hub) and the AJR 2004/2005 handbook chapter (self-authored synthesis hub).
41. Percentage of recent papers citing the hub: Rodrik 377/2,695 = 14.0%; handbook 276/2,695 = 10.2% (population of OpenAlex works citing W3124166904 published 2021-11-04 or later). In the recent top-25 sample: Rodrik 5/25, handbook 3/25.
42. Percentage citing the original primary studies directly: 100% of the recent population by construction (it is defined as citers of AJR 2001); Reversal of Fortune is co-cited by 336/2,695 = 12.5%.
43. Percentage citing the hub instead of inspecting underlying evidence: among recent works citing the hub at all, 807/1,184 (68%) of Rodrik citers and 1,400/1,676 (84%) of handbook citers do not cite AJR 2001. Whether they inspected the evidence cannot be determined from reference lists; this is RECEPTION-CONFIRMED as a citation pattern only.
44. Does the hub accurately represent methods and limits? Rodrik: represents the identification and openly criticises the interpretive leap (RD-E3, RD-E4) — accurate. Handbook: drops the upper-bound qualifier from the page it cites (HB-E1 vs AJR-E2) — inaccurate on magnitude.
45. Does the hub overstate? The handbook overstates magnitude ("almost the entire difference") and broadens the construct ("economic institutions", "security of property rights"). Rodrik relies on publication prestige ("AER-test") to treat the instrument as validated (RD-E1).
46. Does the hub cite adjacent literatures? Rodrik and the handbook both engage geography (Sachs, Gallup) and Rodrik engages trade; the handbook engages human capital only partly.
47. Does the hub become the substitute for direct empirical evidence? For the handbook, partly: 1,400 recent works cite the synthesis without the primary article. Its restatement is the version most likely to be repeated.

| Hub paper | Recent papers citing hub | Recent papers citing primary evidence directly | Adjacent-field citation rate | Hub accuracy | Hub risk |
|---|---|---|---|---|---|
| Rodrik, Subramanian & Trebbi 2004 (W2994756033) | 377/2,695 AJR citers (14.0%); 1,184 recent works overall | 2,695/2,695 by construction; 377/1,184 of hub citers (32%) | Sachs 2003 2.5%, Glaeser 2004 7.5% of recent AJR citers | accurate; critical of interpretation | low |
| AJR 2004 WP / 2005 Handbook (W1580107285, W2108614304) | 276/2,695 (10.2%); 1,676 recent works overall | 276/1,676 of hub citers (16%) | as above | magnitude qualifier dropped; construct broadened | moderate |

SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR

48. Proxy treated as construct: partly. At the source, AJR label the PRS index a measure of institutions with an explicit caveat about measurement error; at the self-authored hub the index becomes "economic institutions" and "security of property rights" (HB-E1). Independent methods users preserve the proxy wording (DML-E1). This is the CV-1 issue propagating through one hub, not field-wide.
49. Export from low-stakes settings: not applicable in the instrument's sense; the inference is from historical cross-country variation to long-run income, which is the same domain. The export risk is from a 64-country cross-section to country-specific policy counterfactuals (Nigeria→Chile), which AJR themselves bound (AJR-E2).
50. Ignored natural experiments: no. Within-country natural-experiment designs with independent data origins exist and are highly cited inside the corpus (N42 Banerjee–Iyer 2005, in-degree 3 excluding N01; N18/N49 Nunn on slave trades). They bear on L3 (institutions matter) but cannot test the field-6 magnitude.
51. Model updating when predictions fail: the authors replied to Albouy (N01) with revised data choices and kept the conclusion; the Nobel scientific background records the dispute and the robustness checks (NS-E2). The model was defended, not abandoned; whether that is warranted is CONTESTED (Stage 2a IV-1).
52. Intervention expansion after failure: no intervention claim is made at the network level; N/A.
53. Falsification criteria: AJR state the identifying assumption and test it with overidentification and controls (AJR-E4, AJR-E3); Sachs explicitly frames the test as a null hypothesis to reject (SA-E1).
54. Evidence that would change the conclusion: stated implicitly through the exclusion restriction; the human-capital rival remains "very hard to distinguish" (NS-E3).
55. Metric improvement without construct improvement: N/A (no intervention).
56. Does the network reward expansion over testing? Mixed. The expanded synthesis (handbook, 1,676 recent citers overall) is cited more than the main rival-explanation tests among recent AJR citers (Glaeser 7.5%, Sachs 2.5%), but the main critique Glaeser 2004 is itself a top-50 hub and Rodrik's test is the most central node after the conflated Reply.

Ratchet scoring route. Intervention-evidence ratchet: N/A, because no intervention claim exists at the field-6 or network level (CV-3's intervention language is in the source's conclusion and was self-caveated; it does not form a downstream intervention literature traced here). Model non-updating: four-link gate — (1) model: colonial institutions, proxied by expropriation risk and identified by settler mortality, explain income differences (stated); (2) later external evidence contradicting or bounding that model: Albouy 2012 and Glaeser 2004 bound it, but both are CONTESTED and not verified as contradictions; (3) reception opportunity: verified (AJR Reply 2012 in the same AER issue; Nobel background 2024); (4) persistence without update: the model persists with a defence. Link 2 is not met with verified disconfirming evidence, so the dimension is UNINFORMATIVE rather than scored.

SECTION H: IGNORED CRITIQUE AND NON-UPTAKE

1. Precondition assessment: critique production was strongly expected — AER lead article, more than 8,000 OpenAlex citations, policy salience, a replication-active field, and a 2024 Nobel citation.
2. Critique retrieval: Albouy (2012, AER Comment, OpenAlex W1969918011, FULL-TEXT-CONFIRMED in Stage 2a); Glaeser et al. (2004, GL-E1, GL-E2); Sachs (2003, SA-E1); McArthur & Sachs (2001, cited by AJR itself, AJR-E3); Rodrik et al. (2004) on interpretation (RD-E3, RD-E4).
3. Reception opportunity: verified — the AJR Reply (N01) appeared in the same AER issue as Albouy; the 2004 critiques preceded the handbook chapter (2005) and the Nobel background (2024).
4. Uptake test: the dominant cluster engages the critiques — the Reply answers Albouy; the Nobel scientific background cites Albouy and the human-capital argument (NS-E2, NS-E3). The broad citing mass mostly does not: Albouy is co-cited by 220/7,375 = 3.0% of 2013+ citers of AJR 2001 or the Reply (union of OpenAlex records) and 50/2,695 = 1.9% of recent AJR citers. Baseline: Rodríguez & Rodrik (2000), the canonical critique of Frankel & Romer (1999), is co-cited by 1,181/5,570 = 21.2% of 2001+ Frankel–Romer citers.

57. Serious critiques: Albouy 2012 (data construction), Glaeser et al. 2004 (human capital, disease environment), Sachs 2003 (malaria), Rodrik et al. 2004 (interpretation), Deaton 2010 (N39, general IV critique).
58. Cited by the dominant cluster: yes (Reply; handbook cites Glaeser-era debate in part; Nobel background).
59. Mode: engaged and contested (Albouy answered; human-capital rival acknowledged as hard to distinguish).
60. Did the network update? The scientific summary (NS-E1 "grain of salt") shows partial updating of certainty; the point estimate continues to be cited unchanged.
61. Recent papers: most recent top citers use institutions indices as regressors and cite AJR as premise; 1.9% co-cite Albouy. They largely continue citing the premise unchanged.
62. Practitioner warnings: not searched (no forum or trade-publication retrieval); UNASSESSED for this question.
63. Effect of practitioner warnings: UNASSESSED.

| Expected-production precondition | Critique / contrary evidence | Year | Source type | Main objection | Verification state | Reception opportunity | Cited by dominant cluster? | Uptake status | Dimension disposition | Effect |
|---|---|---|---|---|---|---|---|---|---|---|
| strong (AER lead article, policy salience) | Albouy, AER Comment (W1969918011) | 2012 | formal comment | settler-mortality data construction; robustness | FULL-TEXT-CONFIRMED; CONTESTED | verified (same AER issue as Reply) | yes (Reply; Nobel NS-E2) | partially incorporated (cluster) / cited but not engaged or ignored (broad mass: 3.0% of 2013+ citers vs 21.2% baseline) | SCORED 1 | low uptake in the citing mass; consensus wording softened only in the scientific summary |
| strong | Glaeser, La Porta, Lopez-de-Silanes & Shleifer (W2890314743) | 2004 | primary empirical | human-capital channel; modern disease environment | FULL-TEXT-CONFIRMED; CONTESTED | verified (2004 onward) | yes (Nobel NS-E3) | partially incorporated | SCORED 1 | rival acknowledged as hard to distinguish |
| strong | Sachs, NBER WP 9490 | 2003 | primary empirical | direct malaria effect | FULL-TEXT-CONFIRMED; CONTESTED | verified | UNASSESSED for the cluster | cited but not engaged (4.4% of union citers) | SCORED 1 | little visible effect on the citing mass |
| strong | Rodrik, Subramanian & Trebbi (W2994756033) | 2004 | primary empirical | institutions vs policies not separated | FULL-TEXT-CONFIRMED | verified | yes (hub) | partially incorporated | SCORED 1 | interpretation narrowed in the literature that cites both |

SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING

64. Recurring authors: Acemoglu appears on 41 and Robinson on 38 of 8,578 OpenAlex citing works (0.48% and 0.44%; group-by on authorships at retrieval time); in the top 50, AJR team members author 8 works.
65. Recurring venues and institutions: the citing mass is spread across SSRN (1,076), CUP eBooks (374), Springer eBooks (229), World Development (129); institutions NBER (215), Harvard (199), World Bank (172), LSE (159), CEPR (155), IMF (154). The top 50 concentrate in the AER (8), JEL (7) and Journal of Economic Growth (4), the normal general-interest venues.
66. Funding sources: not retrievable from OpenAlex for this corpus; UNASSESSED.
67. Overlap with policy networks: World Bank and IMF authors are common citers, consistent with policy use of governance indicators; no closure evidence.
68. Dissent venues: dissent is published in the same top venues — Albouy and the Reply in the AER; Glaeser et al. and Rodrik et al. in the same Journal of Economic Growth volume; Sachs as an NBER working paper.
69. Gatekeeping: no explicit gatekeeping evidence; no functional closure inside the defined corpus (Section A).
70. Ideological alignment: not assessable from retrieved records.

Closure type: normal small-field clustering, with the caveat that the field is not small; the observed clustering is the ordinary centrality of a canonical paper and its follow-ups within growth/development economics. No author-network, journal, funding or advocacy closure is established.

SECTION J: FALSE-POSITIVE AND BASELINE CHECK

71. Small field? No; the citing population is above 8,500 works across economics, political science, management and environmental studies, so dense internal citation is not expected and was not found (5.55% / 3.70%).
72. Comparison with an adjacent subfield: critique-uptake baseline only (Frankel–Romer / Rodríguez–Rodrik, 21.2%); no matched density comparison corpus was built, which is why closure is neither established nor excluded beyond the defined corpus.
73. Engagement with adjacent expertise: the source paper engages geography and malaria directly (AJR-E4) and the institutional-measurement literature (Knack–Keefer); it does not engage weak-IV diagnostics beyond Bound et al.
74. Citing each other because they are the only people studying the question? No; the citing mass is broad and mostly off-question.
75. Strong primary evidence in the founding cluster? Yes for the field-6 estimate (exact reproduction in Stage 2a); conditional for the causal and construct readings.
76. Repeated independent direct tests? Repeated tests exist (Rodrik, Easterly–Levine, Glaeser, Sachs, DML) but share the AJR settler-mortality series; independence of data origin is limited (Finding 2). Within-country designs supply independent origins for L3 only.
77. Limitations preserved downstream? Mixed: lost in the self-authored hub (HB-E1) and in the popular Nobel text (NP-E1); preserved in the scientific background (NS-E1, NS-E2, NS-E3), Hanushek–Woessmann (HW-E1), and DML (DML-E1).
78. Failed predictions acknowledged? Disputes are acknowledged (Reply; Nobel background).
79. Critics cited and engaged? By the dominant cluster, yes; by the broad citing mass, rarely.
80. Mechanism for updating? Yes: comment-and-reply in the AER, subsequent tests in the same venues.

Answers are mostly yes; this is not a cartel. Per the instrument, call it a small but active literature in structure — here, more accurately, a large, active literature around a canonical estimate.

SECTION J2: THE CONCEDE TEST

| Finding | Declared target claim | Matches map field 6? | Same mechanism as another row? | Count separately? |
|---|---|---|---|---|
| 1 Database identity conflation and target reference truncation | citation metrics and graph for AJR 2001 (model-retrieval layer) | no — MAP GAP: this finding targets the retrieval record of AJR 2001, not map field 6 | no | yes |
| 2 Non-independent convergence on one data origin | L3: independent work confirms that institutions explain income differences | no — MAP GAP: this finding targets L3, not map field 6 | shares evidence with Finding 6 only through the same downstream papers; distinct mechanism (data-origin dependence vs rival-test uptake) | yes |
| 3 Self-authored hub drops the upper-bound qualifier and broadens the construct | L3 restatement of the field-6 magnitude implication (p. 1387) | no — MAP GAP: this finding targets the hub restatement of the field-6 estimate's magnitude implication | yes — review-hub laundering and claim mutation rest on the same HB-E1 passage | no — counted once (claim mutation owns it; review-hub laundering NESTED) |
| 4 Public certainty inflation ("clear chain of causality") | L4 public wording (map field 4) | no — MAP GAP: this finding targets map field 4 wording, not map field 6 | partly with Finding 3 (same direction) but different source and layer | yes (minor) |
| 5 Albouy critique low uptake in the citing mass | field 6 (the critique targets the instrument behind the estimate) | yes | no | yes |
| 6 Rival-explanation tests rarely co-cited downstream; source layer engaged | L3 | no — MAP GAP: this finding targets L3, not map field 6 | no | yes |
| 7 No closure inside the defined corpus (acquittal) | field 6 network support | yes | no | yes |

Concede test (field 6 wording: "In the base sample of 64 former colonies, the 2SLS estimate … is 0.94 (SE 0.16)"):

| Finding | Concede test: SURVIVES / NARROWS / DEFEATS | Surviving claim if NARROWS |
|---|---|---|
| 1 | SURVIVES | — |
| 2 | NARROWS (against declared L3 target; SURVIVES against field 6) | several teams obtain similar estimates with the AJR instrument; this is specification robustness on one data origin, not independent confirmation |
| 3 | NARROWS (against declared L3 restatement; SURVIVES against field 6) | the 0.94 estimate implies up to about a 7-fold Nigeria–Chile gap, which the authors call an upper bound because of measurement error |
| 4 | NARROWS (against L4; SURVIVES against field 6) | evidence "strongly suggests" colonial institutions are a key mechanism, with the estimate "taken with a grain of salt" |
| 5 | SURVIVES | — |
| 6 | NARROWS (against L3; SURVIVES against field 6) | institutions are a major channel; direct disease and settler human-capital channels are not excluded |
| 7 | SURVIVES | — |

NARROWS details. Finding 2: material narrowing — the asserted independence and breadth of confirmation shrink; the estimate is untouched. Finding 3: material narrowing for the magnitude restatement — the qualifier lost is load-bearing for "almost the entire difference"; incidental for field 6. Finding 4: incidental narrowing — the public text overstates certainty; the scientific background preserves limits. Finding 6: material narrowing for L3 — the rival channels remain live and CONTESTED.

No finding DEFEATS field 6. No network finding is load-bearing against field 6; the load-bearing findings for the downstream layers are 2 and 3.

SECTION K: CARTEL-RISK SCORING

The scorecard with dispositions, ordinal scores and aggregation status is Artifact 8. Nesting: review-hub laundering reuses the HB-E1 passage that owns claim mutation, so it is NESTED under Claim mutation. All other scored dimensions rest on distinct evidence (founding-cluster dominance on authorship and co-citation shares; density on the graph receipts; recent-paper dependence on the recent corpus; proxy mismatch on construct wording across DML, HW and the handbook; adjacent-field neglect on the locked list plus POST HOC rows; lack of decisive tests on the absence of instrument-independent magnitude tests; critique uptake on the Albouy co-citation counts).

- Verified risk score: 7/24
- Verified scored-dimension risk rate: 29.2
- Independent scored dimensions: 8
- Nested scored dimensions: 1
- Verified risk denominator: 24
- Evidentiary coverage: 9/10 applicable dimensions scored (90%)
- Execution completeness: 10/10 applicable dimensions completed (100%)
- Dimension inventory: 8 INDEPENDENT SCORED + 1 NESTED SCORED + 1 UNINFORMATIVE + 0 UNASSESSED + 1 N/A = 11 total dimensions; 10 applicable
- Unscored dimensions: Model non-updating — UNINFORMATIVE (four-link gate link 2 not met: disconfirming evidence is CONTESTED, not verified); Intervention-evidence ratchet — N/A (no intervention claim)
- Risk band: issued (see below)
- Mechanism label: issued (see below)

Verified scored-dimension risk: 29.2%, calculated from 8 independent scored dimensions; 1 additional scored dimensions are NESTED; 9 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.

Formal-label gate: coverage 90% ≥ the PROVISIONAL 70% threshold (an engineering threshold, not validated); no label-essential dimension UNASSESSED. Breadth: the 7 points are spread as score 1 across 7 distinct independent dimensions, so the score is not driven by a few severe dimensions. Functional-closure labels are not available: density is low and closure is not established.

ARITHMETIC BAND POSITION: >20%–40% (normal field clustering with some weaknesses).
RISK BAND: >20%–40% normal field clustering with some weaknesses — computed over 8 independent scored dimensions; breadth requirement PASSED. Caveat: open-retrieval application outside the instrument's validated packet regime (lines 418–427).
MECHANISM LABEL: shared-data pseudo-convergence (downstream "confirmations" reuse the AJR settler-mortality series) plus self-authored hub qualifier loss (HB-E1).

ARTIFACT 1: TOP 15 CITATION SPINE TABLE

| Rank | Paper | Year | Citation count | Evidence type | Role in network | Source of citation count |
|---:|---|---:|---:|---|---|---|
| 1 | Daron Acemoğlu, Simon Johnson, James A. Robinson: The Colonial Origins of Comparative Development: An Empirical Investigation: Reply (W3124131699) | 2012 | 6266 | secondary analysis | authors' reply; OpenAlex identity conflated with AJR 2001 | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 2 | Dani Rodrik, Arvind Subramanian, Francesco Trebbi: Institutions Rule: The Primacy of Institutions Over Geography and Integration in Economic  (W2994756033) | 2004 | 5484 | primary empirical test of the central claim | independent amplification hub ("Institutions Rule") | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 3 | Edward L. Glaeser, Rafael La Porta, Florencio López‐de‐Silanes: Do Institutions Cause Growth? (W2890314743) | 2004 | 3990 | primary empirical test of the central claim | principal critique (human capital) | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 4 | Raghuram G. Rajan, Luigi Zingales: The great reversals: the politics of financial development in the twentieth century (W3122778615) | 2003 | 3350 | primary empirical study (not of the central claim) | financial development; background citation | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 5 | Daron Acemoğlu, Simon Johnson, James A. Robinson: Institutions as the Fundamental Cause of Long-Run Growth (W2108614304) | 2004 | 3181 | review article | self-authored synthesis hub | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 6 | Victor Chernozhukov, Denis Chetverikov, Mert Demirer: Double/debiased machine learning for treatment and structural parameters (W3123436326) | 2017 | 3112 | theoretical / conceptual paper | methods paper using AJR data as worked example | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 7 | Simone Raudino: The Theory of Economic Development (W2556507681) | 2016 | 3019 | unclear / needs source audit | likely database misattribution | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 8 | César A. Hidalgo, Bailey Klinger, Albert-Ĺaszló Barabási: The Product Space Conditions the Development of Nations (W2064927380) | 2007 | 2957 | primary empirical study (not of the central claim) | product space; background citation | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 9 | Ross Eric Levine: Chapter 12 Finance and Growth: Theory and Evidence (W1588189399) | 2005 | 2893 | review article | background in finance survey | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 10 | Halvor Mehlum A, Karl Ove Moene, Ragnar Torvik: Institutions and the Resource Curse (W1484474409) | 2006 | 2874 | primary empirical study (not of the central claim) | institutions x resource curse; adjacent | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 11 | Daron Acemoğlu, Simon Johnson, James A. Robinson: Chapter 6 Institutions as a Fundamental Cause of Long-Run Growth (W1580107285) | 2005 | 2498 | review article | self-authored synthesis hub (published) | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 12 | Eric Alan Hanushek, Ludger Woessmann: The Role of Cognitive Skills in Economic Development (W1480274481) | 2008 | 2485 | review article | rival-field review that preserves dispute | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 13 | Wolfgang Keller: International Technology Diffusion (W3125697804) | 2004 | 2398 | review article | technology diffusion; background | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 14 | Melissa Dell, Benjamin F. Jones, Benjamin Olken: What Do We Learn from the Weather? The New Climate-Economy Literature (W2104834906) | 2014 | 2310 | review article | adjacent-field review; background | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |
| 15 | Frederick van der Ploeg: Natural Resources: Curse or Blessing? (W3123261979) | 2011 | 2309 | review article | resource curse; adjacent | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |

Citation counts are OpenAlex cited_by_count at retrieval. Cross-database counts for AJR 2001: OpenAlex 8,594; Crossref is-referenced-by 7,813; Semantic Scholar 12,600; union of the OpenAlex 2001 and 2012-Reply records 11,316. N01's 6,266 is inflated by conflation with the 2001 article (Finding 1).

ARTIFACT 2: FOUNDING CLUSTER TABLE

| Paper | Year | Claim introduced | Evidence type | Verification state | Later role | Risk |
|---|---|---|---|---|---|---|
| AJR, The Colonial Origins of Comparative Development (W3124166904) | 2001 | settler mortality as instrument; 0.94 effect of expropriation protection on log income | primary empirical test of the central claim | FULL-TEXT-CONFIRMED; CROSS-SOURCE-CONFIRMED (estimate reproduced in Stage 2a) | canonical source; instrument reused by most re-tests | low for field 6; moderate for L3 restatements |
| AJR, Reversal of Fortune (W3125412951 and related records) | 2002 | pre-colonial prosperity reversal | primary empirical study (not of the central claim) | LOCATED | co-cited by 12.5% of recent AJR citers; 19/50 of top-50 | low |
| AJR, Institutions as the Fundamental Cause of Long-Run Growth (N05 WP 10481; N11 Handbook) | 2004/2005 | synthesis: institutions as fundamental cause | review article | FULL-TEXT-CONFIRMED (WP version; published chapter not retrieved) | self-authored hub; 1,676 recent citers overall | moderate (qualifier loss, HB-E1) |
| AJR, Reply to Albouy (W3124131699) | 2012 | defence of data choices | secondary analysis | FULL-TEXT-CONFIRMED | answers the main data critique; OpenAlex record conflated with 2001 article | low |

ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE

Recent corpus: OpenAlex `filter=cites:W3124166904,from_publication_date:2021-11-04&sort=cited_by_count:desc&per-page=25` (population 2,695). "Cites founding cluster?" means beyond AJR 2001 itself, which all rows cite by construction. "Cites adjacent fields?" means co-citation of the POST HOC rival tests (Glaeser 2004, Sachs 2003), Albouy 2012, or a locked Section E source.

| Recent paper | Year | Verification state | Cites founding cluster? | Cites hub? | Cites adjacent fields? | New evidence or recycling? |
|---|---:|---|---|---|---|---|
| R01 Digitalization and sustainable development: How could digital economy development improve  (W4292849668) | 2022 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | AJR 2001 only (by construction) | no | no | new evidence on another question (China green innovation); AJR use not retrieved |
| R02 On the role of domestic trade flows for estimating the gravity model of trade (W4212979054) | 2022 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | AJR 2001 only (by construction) | no | no | new methods evidence (gravity model); AJR use not retrieved |
| R03 Land property rights and rural enterprise growth: Evidence from land titling reform in Chi (W4223529822) | 2022 | RECEPTION-CONFIRMED (reference list); LOCATED | AJR 2001 only (by construction) | no | no | new quasi-experimental evidence (China land titling); property-rights adjacent |
| R04 Women’s political empowerment and economic growth (W4224261420) | 2022 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | AJR 2001 only (by construction) | Rodrik 2004 | no | new cross-country evidence (women political empowerment) |
| R05 Does institutional quality foster economic complexity? The fundamental drivers of producti (W3165371825) | 2022 | RECEPTION-CONFIRMED (reference list); LOCATED | AJR 2001 only (by construction) | Rodrik 2004 | Glaeser 2004; Sachs 2003; Albouy 2012 | new cross-country evidence (economic complexity); co-cites critics |
| R06 How Do Institutional Quality, Natural Resources, Renewable Energy, and Financial Developme (W4307547529) | 2022 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | AJR 2001 only (by construction) | no | no | new panel evidence (ecological footprint) |
| R07 Instrumental variables estimation: Assumptions, pitfalls, and guidelines (W4319016949) | 2023 | RECEPTION-CONFIRMED (reference list); LOCATED | AJR 2001 only (by construction) | no | no | methods guide; AJR likely an IV example (context not retrieved) |
| R08 Do economic growth and institutional quality reduce poverty and inequality in West Africa? (W4200480718) | 2021 | RECEPTION-CONFIRMED (reference list); LOCATED | yes (handbook) | Rodrik 2004, AJR handbook | Glaeser 2004; Sachs 2003; locked source W3121147769 | new regional panel (West Africa poverty) |
| R09 Institutional Quality and Education Quality in Developing Countries: Effects and Transmiss (W4206178768) | 2022 | RECEPTION-CONFIRMED (reference list); LOCATED | AJR 2001 only (by construction) | no | Glaeser 2004 | new cross-country evidence (education quality) |
| R10 Converging to Convergence (W3211527536) | 2022 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | AJR 2001 only (by construction) | no | Glaeser 2004 | growth-empirics review (NBER Macro Annual) |
| R11 Effects of income inequality and governance on energy poverty alleviation: Implications fo (W4285081985) | 2022 | RECEPTION-CONFIRMED (reference list); LOCATED | yes (handbook) | AJR handbook | no | new panel (energy poverty) |
| R12 RETRACTED: Country-level institutional quality and financial system efficiency: An interna (W4386322040) | 2023 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | AJR 2001 only (by construction) | no | no | RETRACTED paper; excluded from inference |
| R13 Informal institutions and international business: Toward an integrative research agenda (W4292663674) | 2022 | RECEPTION-CONFIRMED (reference list); LOCATED | AJR 2001 only (by construction) | no | no | conceptual review (informal institutions) |
| R14 The Impact of Institutions on Innovation (W3124497653) | 2022 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | yes (Reversal) | no | Glaeser 2004 | new evidence (institutions and innovation) |
| R15 Climate risk, institutional quality, and total factor productivity (W4318937711) | 2023 | RECEPTION-CONFIRMED (reference list); LOCATED | AJR 2001 only (by construction) | no | locked source W2618788771 | new panel (climate risk, TFP) |
| R16 Cultural Origin and Minority Shareholder Expropriation: Historical Evidence (W4388274323) | 2023 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | yes (Reversal, handbook) | AJR handbook | no | new historical evidence (cultural origin, shareholder expropriation) |
| R17 The effects of FDI on economic growth in Africa (W4281705180) | 2022 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | AJR 2001 only (by construction) | Rodrik 2004 | locked source W2010235856 | new panel (FDI, Africa) |
| R18 Regulatory issues inhibiting the financial inclusion: a case study among Islamic banks and (W4387877962) | 2023 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | AJR 2001 only (by construction) | no | no | qualitative case study (Indonesia) |
| R19 The role of public environmental concern on corporate social responsibility: Evidence from (W4386647200) | 2023 | RECEPTION-CONFIRMED (reference list); LOCATED | AJR 2001 only (by construction) | Rodrik 2004 | no | new firm-level evidence (China CSR) |
| R20 The standard errors of persistence (W3124943234) | 2024 | RECEPTION-CONFIRMED (reference list); LOCATED | yes (Reversal) | no | no | methods critique of persistence regressions (spatial noise) |
| R21 Effect of environmental regulation policy synergy on carbon emissions in China under consi (W4293403519) | 2022 | RECEPTION-CONFIRMED (reference list); LOCATED | AJR 2001 only (by construction) | no | no | new panel (China carbon policy) |
| R22 Can female entrepreneurs boost social mobility in developing countries? An institutional a (W4200592490) | 2021 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | yes (Reversal) | no | Glaeser 2004 | new evidence (female entrepreneurs, institutions) |
| R23 Technological innovation and its influence on energy risk management: Unpacking China’s en (W4391180104) | 2024 | RECEPTION-CONFIRMED (reference list); LOCATED | AJR 2001 only (by construction) | no | no | new evidence (China energy risk) |
| R24 Aid effectiveness and donor motives (W4390870694) | 2024 | RECEPTION-CONFIRMED (reference list); ABSTRACT-CONFIRMED | AJR 2001 only (by construction) | no | no | new aid-effectiveness evidence |
| R25 Institutional quality and human capital development in Africa (W4200071543) | 2021 | RECEPTION-CONFIRMED (reference list); LOCATED | AJR 2001 only (by construction) | no | locked source W2010235856 | new panel (Africa human capital) |

Recent-25 summary: Rodrik hub 5/25; handbook 3/25; Reversal 4/25; Glaeser 6/25; Sachs 2/25; Albouy 1/25; locked adjacent sources 4/25. Population-level recent co-citation (n = 2,695): Rodrik 14.0%, Reversal 12.5%, Hall–Jones 10.5%, handbook 10.2%, Glaeser 7.5%, Knack–Keefer 6.1%, Easterly–Levine 3.4%, Gallup–Sachs–Mellinger 2.8%, Sachs 2003 2.5%, Albouy 1.9%, Staiger–Stock 1.4%, Bound et al. 0.1%. R12 is retracted and excluded from inference.

ARTIFACT 4: CITATION POLARITY TABLE

| Citing paper | Cited paper | Verification state | Citation polarity | Claim use | Inflation risk |
|---|---|---|---|---|---|
| N01 AJR Reply 2012 | AJR 2001 | FULL-TEXT-CONFIRMED | supportive | defence of data and estimate (self) | low |
| N02 Rodrik et al. 2004 | AJR 2001 | FULL-TEXT-CONFIRMED | supportive | instrument adopted ("AER-test", RD-E1); interpretation criticised (RD-E3, RD-E4) | low (prestige-as-validation noted) |
| N03 Glaeser et al. 2004 | AJR 2001 | FULL-TEXT-CONFIRMED | critical | rival tests (GL-E1, GL-E2) | none |
| N04 Rajan & Zingales 2003 | AJR 2001 | FULL-TEXT-CONFIRMED (WP w8178) | perfunctory | reference list only | none |
| N05 AJR 2004 WP | AJR 2001 | FULL-TEXT-CONFIRMED | used as premise | "almost the entire difference" without the upper bound (HB-E1) | moderate |
| N06 Chernozhukov et al. 2018 | AJR 2001 | FULL-TEXT-CONFIRMED | supportive | methodological reuse of the 64 observations; compares to Table 4 col 7 (DML-E1, DML-E2) | low; non-independent data |
| N07 Raudino 2016 | AJR 2001 | LOCATED | unclear without full text | OpenAlex attribution likely wrong | unclear |
| N08 Hidalgo et al. 2007 | AJR 2001 | FULL-TEXT-CONFIRMED (arXiv) | neutral/background | "requisite institutions" background list | none |
| N09 Levine 2005 | AJR 2001 | FULL-TEXT-CONFIRMED (WP w10766) | neutral/background | background list | none |
| N10 Mehlum, Moene & Torvik 2006 | AJR 2001 | ABSTRACT-CONFIRMED | unclear without full text | retrieval failed (HTTP 404) | unclear |
| N11 AJR 2005 Handbook | AJR 2001 | ABSTRACT-CONFIRMED (published chapter not retrieved; WP version is N05) | used as premise | same as N05 assumed, not verified | moderate (inferred from N05) |
| N12 Hanushek & Woessmann 2008 | AJR 2001 | FULL-TEXT-CONFIRMED (WP w12832) | neutral/background | "remains a disputed subject" (HW-E1) | none |
| N13 Keller 2004 | AJR 2001 | ABSTRACT-CONFIRMED | unclear without full text | retrieved 2001 WP does not cite AJR (version mismatch) | unclear |
| N14 Dell, Jones & Olken 2014 | AJR 2001 | FULL-TEXT-CONFIRMED (WP w19578) | neutral/background | accurate summary of the settler-mortality channel | none |
| N15 van der Ploeg 2011 | AJR 2001 | ABSTRACT-CONFIRMED | unclear without full text | retrieval failed (HTTP 500 ×3) | unclear |
| Nobel popular background 2024 (outside corpus) | AJR 2001 | FULL-TEXT-CONFIRMED | inflated | "a clear chain of causality" (NP-E1) | moderate (public layer) |
| Nobel scientific background 2024 (outside corpus) | AJR 2001 | FULL-TEXT-CONFIRMED | supportive | "grain of salt"; Albouy acknowledged (NS-E1, NS-E2) | none |

Semantic Scholar citation contexts (planned as a second polarity source) were not obtained: 24 API calls, 21 HTTP 429, 2 HTTP 200, 1 HTTP 404; the background job was stopped at about 12 minutes. Polarity above rests only on retrieved full texts.

ARTIFACT 5: CLAIM MUTATION TABLE

| Original source | Original claim | Verification state | Hub restatement | Downstream restatement | Mutation severity |
|---|---|---|---|---|---|
| AJR 2001 p. 1387 (AJR-E2) | 0.94 implies about a 7-fold Nigeria–Chile gap; "the 7-fold differenceis an upperbound" | FULL-TEXT-CONFIRMED | "almost the entire difference … could be explained by the differences in the security of property rights" (HB-E1) | Nobel popular: "a clear chain of causality" (NP-E1) | moderate |
| AJR 2001 Table 4 regressor | PRS protection-against-expropriation index | FULL-TEXT-CONFIRMED | "economic institutions" (HB-E1) | DML: "a proxy for the strength of institutions" (DML-E1) — preserved | minor |
| AJR 2001 Table 7 (AJR-E4) | malaria control: 0.69 (SE 0.25), still significant | FULL-TEXT-CONFIRMED | EL: no direct germ effect other than through institutions (EL-E1) | HW: "remains a disputed subject" (HW-E1) | none |

Cross-source check: HB-E1 cites "p. 1387" explicitly; AJR-E2 is located on PDF page 20 = AER p. 1387 (verified with layout extraction). The comparison is CROSS-SOURCE-CONFIRMED.

ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE

| Claim layer | Adjacent field | Nominated source and stable identifier | Verification state | Source class: CONSTRUCT-DEFINING / MECHANISM-SUPPORTING / DIRECTLY-ADJUDICATING | Actual result | Explanation favored | Explanation weakened | Precise revision required | Pre-inspection lock status or POST HOC | Cited? | Engagement quality | Omission severity |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L3 | F1 malaria economics | W139828295 (Malawi household malaria cost, 1994) | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | household-level spending | — | — | — | LOCKED | no | not cited | minor context loss |
| L3 | F1 malaria economics | W2088758477 (Gambia risk factors, 1995) | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | socio-economic risk factors | — | — | — | LOCKED | no | not cited | minor context loss |
| L1/L3 | F2 geography | W2618788771 Gallup, Sachs & Mellinger | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | geography correlates with income | — | — | — | LOCKED | yes | directly tested against | minor context loss |
| L3 | F2 geography | W1492460295 | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | theory of geography in development | — | — | — | LOCKED | no | not cited | minor context loss |
| L3 | F3 human capital | W3121822366 Becker, Murphy & Tamura | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | human-capital growth theory | — | — | — | LOCKED | no | not cited | minor context loss |
| L3 | F3 human capital | W2035652178 Glomm & Ravikumar | ABSTRACT-CONFIRMED | MECHANISM-SUPPORTING | schooling-finance growth theory | — | — | — | LOCKED | no | not cited | minor context loss |
| L1/L2 | F4 weak-IV | W2165144879 Staiger & Stock | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | weak-instrument asymptotics | — | — | — | LOCKED | no | not cited | moderate weakness |
| L1/L2 | F4 weak-IV | W1980412904 Bound, Jaeger & Baker | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | weak IV biased toward OLS | — | — | — | LOCKED | yes | cited in passing | minor context loss |
| L1 | F6 institutional measurement | W3121147769 North 1990 (mis-typed record) | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | conceptual definition of institutions | — | — | — | LOCKED | no (other North works cited) | not cited | minor context loss |
| L1 | F6 institutional measurement | W2010235856 Knack & Keefer | ABSTRACT-CONFIRMED | CONSTRUCT-DEFINING | ICRG/BERI indices predict growth | — | — | — | LOCKED | yes | substantively engaged | minor context loss |
| L3 | R1 test | Sachs 2003 NBER WP 9490 | FULL-TEXT-CONFIRMED; CONTESTED | DIRECTLY-ADJUDICATING | null "readily rejected using … malaria risk" (SA-E1) | R1 | L3 strong form | L3: "institutions are a major channel; a direct disease channel is not excluded" | POST HOC | 4.4% of union citers | cited in passing | moderate weakness |
| L3 | R1/R2 test | Glaeser et al. 2004 NBER WP 10568 | FULL-TEXT-CONFIRMED; CONTESTED | DIRECTLY-ADJUDICATING | malaria risk significant alongside settler mortality; human-capital channel (GL-E1, GL-E2) | R1 and R2 | L3 strong form | L3: "institutions or settler human capital, not separately identified" | POST HOC | 13.6% of union citers | substantively engaged | moderate weakness |

Adjacent-field neglect disposition: at the source layer, engagement is affirmative (geography and malaria directly tested; institutional-measurement source used; weak-IV only in passing). The two DIRECTLY-ADJUDICATING rows are POST HOC and can support at most SCORED 1; their low co-citation by downstream citers gives SCORED 1.

ARTIFACT 7: CRITIQUE-UPTAKE TABLE

| Expected-production precondition | Critique / contrary evidence | Year | Source type | Main objection | Verification state | Reception opportunity | Cited? | Uptake status | Dimension disposition | Effect on consensus |
|---|---|---|---|---|---|---|---|---|---|---|
| strong | Albouy (W1969918011) | 2012 | formal comment | data construction of settler mortality | FULL-TEXT-CONFIRMED; CONTESTED | verified | yes by cluster; 3.0% of 2013+ citers | partially incorporated | SCORED 1 | scientific summary softened ("grain of salt"); citing mass unchanged |
| strong | Glaeser et al. (W2890314743) | 2004 | primary empirical | human capital; disease environment | FULL-TEXT-CONFIRMED; CONTESTED | verified | yes; 14.0% of 2005+ citers | partially incorporated | SCORED 1 | rival acknowledged (NS-E3) |
| strong | Sachs 2003 | 2003 | primary empirical | direct malaria effect | FULL-TEXT-CONFIRMED; CONTESTED | verified | 4.4% of union citers | cited but not engaged | SCORED 1 | little visible effect |
| strong | Rodrik et al. (W2994756033) | 2004 | primary empirical | institutions vs policy distinction | FULL-TEXT-CONFIRMED | verified | yes (hub) | partially incorporated | SCORED 1 | interpretation narrowed among co-citers |

Baseline: Rodríguez & Rodrik (2000) co-cited by 21.2% of 2001+ Frankel–Romer citers (1,181/5,570).

ARTIFACT 8: CARTEL-RISK SCORECARD

| Dimension | Applicability | Dimension disposition | Score if SCORED | Evidence / claim state | Evidence supporting disposition and score | Evidence identifiers | Retrieval coverage | AGGREGATION STATUS | Independent evidence and inferential work, or nesting rationale | Reason excluded from denominator | Effect on formal-label gate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Founding-cluster dominance | applicable | SCORED 1 | 1 | RECEPTION-CONFIRMED | 8/50 top citers AJR-authored; Reversal in 19/50 and recent 12.5%; handbook recent 10.2%; critics equally central | raw/top50_citers.json; recent_cocite_counts.json | 50/50 reference lists | INDEPENDENT | authorship and co-citation shares, distinct from other rows | — | counts toward coverage |
| Internal citation density | applicable | SCORED 0 | 0 | RECEPTION-CONFIRMED | 136/2450 = 5.55% raw; 87/2352 = 3.70% excluding conflated N01; reference lists not truncated (Crossref check) | graph.json; refcount_compare.json | 50/50 inputs | INDEPENDENT | graph receipts in Section A | — | affirmative low density inside corpus only |
| Recent-paper dependence | applicable | SCORED 1 | 1 | ABSTRACT-CONFIRMED; RECEPTION-CONFIRMED | recent citers mostly use AJR as background premise for governance-index regressions; new evidence on other questions | recent5y_top25.json; recent25_abstracts.json | 25 sampled of 2,695 | INDEPENDENT | recent corpus is distinct evidence | — | counts toward coverage |
| Review-hub laundering | applicable | SCORED 1 | 1 | CROSS-SOURCE-CONFIRMED | self-authored hub drops upper bound; 1,400 recent works cite it without AJR 2001 | HB-E1; AJR-E2; recent_all_HB.json | WP version only | NESTED under Claim mutation | same HB-E1 passage owns the mutation | excluded from aggregate as NESTED | counts toward coverage |
| Proxy mismatch | applicable | SCORED 1 | 1 | FULL-TEXT-CONFIRMED | PRS expropriation index cited as "economic institutions"; DML and HW preserve proxy wording | HB-E1; DML-E1; HW-E1 | 13 full texts | INDEPENDENT | construct-wording comparison across three independent sources | — | counts toward coverage |
| Claim mutation | applicable | SCORED 1 | 1 | CROSS-SOURCE-CONFIRMED | upper-bound qualifier lost (HB-E1 vs AJR-E2); popular "clear chain of causality" (NP-E1) vs scientific "grain of salt" (NS-E1) | HB-E1; AJR-E2; NP-E1; NS-E1 | hub and Nobel texts retrieved | INDEPENDENT | owns the HB-E1 evidence | — | counts toward coverage |
| Adjacent-field neglect | applicable | SCORED 1 | 1 | FULL-TEXT-CONFIRMED; CONTESTED | source layer affirmative; POST HOC directly-adjudicating rival tests co-cited by 4.4% and 13.6% of citers; capped at 1 by POST HOC rule | locked_sources.json; SA-E1; GL-E1 | 10/10 locked sources; 2 POST HOC | INDEPENDENT | locked list and co-citation counts | — | counts toward coverage |
| Lack of decisive tests | applicable | SCORED 1 | 1 | FULL-TEXT-CONFIRMED | no instrument-independent test of the cross-country magnitude; institutions vs human capital "very hard to distinguish" | NS-E3; RD-E4; EL-E2; DML-E1 | 13 full texts | INDEPENDENT | concerns test design, distinct from uptake | — | counts toward coverage |
| Poor critique uptake | applicable | SCORED 1 | 1 | RECEPTION-CONFIRMED; CONTESTED | Albouy 3.0% of 2013+ citers vs 21.2% baseline; formally engaged by the cluster | union_citers_2013plus_albouy.json; baseline_fr_2001plus_rr.json; NS-E2 | population counts | INDEPENDENT | co-citation counts and reception opportunity | — | counts toward coverage |
| Intervention-evidence ratchet | not applicable | N/A | — | — | no intervention claim | — | — | — | — | N/A: no intervention claim | none |
| Model non-updating | applicable | UNINFORMATIVE | — | CONTESTED | four-link gate link 2 not met (disconfirming evidence CONTESTED, not verified) | Albouy; N01; NS-E2 | traced | — | — | UNINFORMATIVE | does not block label (not label-essential for issued band) |

Verified risk score 7/24; rate 29.2%; independent 8; nested 1; denominator 24 (repeated from Section K).

ARTIFACT 9: NETWORK MAP

GRAPH CORPUS DEFINITION (repeated): top 50 OpenAlex works citing W3124166904 by cited_by_count, no date or type bound, no screening; target N00 excluded from the density count. Node identifiers: N01=W3124131699; N02=W2994756033; N03=W2890314743; N04=W3122778615; N05=W2108614304; N06=W3123436326; N07=W2556507681; N08=W2064927380; N09=W1588189399; N10=W1484474409; N11=W1580107285; N12=W1480274481; N13=W3125697804; N14=W2104834906; N15=W3123261979; N16=W2109890836; N17=W2148534039; N18=W2145309110; N19=W1934649023; N20=W3023420463; N21=W3122513675; N22=W2789051288; N23=W4253884756; N24=W2150851272; N25=W3121534672; N26=W3123293195; N27=W3122513589; N28=W2046507863; N29=W2591654989; N30=W3125767605; N31=W3124753968; N32=W2490362664; N33=W2114854852; N34=W2123148076; N35=W3121354442; N36=W2152556759; N37=W2891506482; N38=W3193006831; N39=W2103130810; N40=W2090766907; N41=W3125033761; N42=W1511665033; N43=W2107205575; N44=W2113596540; N45=W2131499322; N46=W2889827801; N47=W2891433665; N48=W3123773675; N49=W3121532354; N50=W3126058703

Edge list (CSV, Gephi-ready; 136 directed internal edges, citing,cited):

```
source,target
N01,N10
N01,N42
N01,N24
N01,N27
N01,N21
N01,N04
N01,N31
N01,N13
N01,N30
N02,N21
N02,N01
N02,N31
N03,N47
N03,N02
N03,N21
N03,N01
N04,N01
N05,N01
N05,N31
N05,N30
N07,N19
N07,N01
N08,N01
N09,N21
N09,N01
N09,N30
N10,N01
N11,N01
N11,N31
N12,N05
N12,N37
N12,N01
N13,N42
N14,N43
N14,N16
N14,N02
N14,N01
N15,N10
N15,N45
N15,N22
N15,N03
N15,N02
N15,N01
N15,N31
N16,N14
N16,N02
N16,N01
N17,N03
N17,N02
N17,N21
N17,N01
N17,N31
N18,N42
N18,N40
N18,N17
N18,N49
N18,N01
N19,N03
N19,N02
N20,N03
N20,N47
N21,N01
N22,N04
N22,N15
N22,N01
N24,N01
N25,N05
N25,N01
N25,N41
N25,N38
N26,N49
N26,N50
N27,N04
N27,N01
N28,N01
N29,N05
N29,N17
N29,N03
N29,N25
N29,N21
N29,N01
N30,N01
N31,N21
N31,N01
N33,N03
N33,N02
N33,N01
N34,N02
N34,N21
N34,N01
N35,N02
N35,N21
N35,N01
N36,N01
N36,N31
N36,N38
N37,N12
N37,N11
N37,N05
N37,N03
N37,N01
N37,N38
N39,N26
N39,N01
N39,N50
N40,N18
N40,N17
N40,N03
N40,N02
N40,N01
N41,N05
N41,N25
N41,N01
N42,N01
N43,N21
N43,N01
N44,N05
N44,N17
N44,N03
N44,N02
N44,N21
N44,N01
N45,N21
N45,N15
N45,N31
N46,N10
N46,N49
N46,N01
N47,N02
N47,N21
N47,N04
N47,N01
N48,N19
N48,N01
N49,N01
N50,N01
```

Plus 50 edges Nxx -> N00 by construction (not shown). Hubs by in-degree excluding N01: N21 12, N02 12, N03 9, N31 7, N05 6, N17 4, N49 3, N04 3, N42 3. Reciprocal pairs excluding N01: N12–N37, N14–N16, N15–N45, N15–N22, N18–N40, N25–N41.

COMPLETION LEDGER

| Required heading | Exact heading present? | Status: completed / N/A / omitted | Reason or output location |
|---|---|---|---|
| `PRE-AUDIT CLAIM CONFIRMATION` | yes | completed | Four confirmation lines |
| `SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION` | yes | completed | Graph receipts, density, Q1–10 |
| `SECTION B: EVIDENCE TYPE CODING` | yes | completed | 50-node coding, Q11–16 |
| `SECTION C: CITATION POLARITY AND CLAIM USE` | yes | completed | Q17–22; Artifact 4 |
| `SECTION D: CLAIM MUTATION TRACKING` | yes | completed | Q23–30 and mutation table |
| `SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT` | yes | completed | Locked query, preregistration and neglect tables |
| `SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING` | yes | completed | Q40–47 and hub table |
| `SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR` | yes | completed | Q48–56; four-link gate |
| `SECTION H: IGNORED CRITIQUE AND NON-UPTAKE` | yes | completed | Sequence, Q57–63, uptake table |
| `SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING` | yes | completed | Q64–70; closure type |
| `SECTION J: FALSE-POSITIVE AND BASELINE CHECK` | yes | completed | Q71–80 |
| `SECTION J2: THE CONCEDE TEST` | yes | completed | Target gate and concede tables |
| `SECTION K: CARTEL-RISK SCORING` | yes | completed | Arithmetic, gate, band |
| `ARTIFACT 1: TOP 15 CITATION SPINE TABLE` | yes | completed | 15 rows |
| `ARTIFACT 2: FOUNDING CLUSTER TABLE` | yes | completed | 4 rows |
| `ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE` | yes | completed | 25 rows |
| `ARTIFACT 4: CITATION POLARITY TABLE` | yes | completed | 17 rows |
| `ARTIFACT 5: CLAIM MUTATION TABLE` | yes | completed | 3 rows |
| `ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE` | yes | completed | 12 rows |
| `ARTIFACT 7: CRITIQUE-UPTAKE TABLE` | yes | completed | 4 rows |
| `ARTIFACT 8: CARTEL-RISK SCORECARD` | yes | completed | 11 dimensions |
| `ARTIFACT 9: NETWORK MAP` | yes | completed | 136-edge CSV |
| `COMPLETION LEDGER` | yes | completed | This table |
| `ARTIFACT 10: FINAL VERDICT` | yes | completed | Issued after ledger because no required block was omitted |
| `FINAL SECTION: STANDARDIZED FINDING TABLE` | yes | completed | Seven findings follow |

Gate result: PASS. No applicable analytical section or Artifact 1–9 was omitted, so Artifact 10 may issue.

ARTIFACT 10: FINAL VERDICT

- Main founding cluster: AJR 2001 with Reversal of Fortune (2002), the AJR 2004/2005 synthesis and the 2012 Reply; 8/50 top citers are AJR-authored.
- Main amplification hub: Rodrik, Subramanian & Trebbi 2004 (independent; accurate and critical of interpretation) and the AJR handbook (self-authored; drops the upper-bound qualifier).
- Main proxy problem: the PRS protection-against-expropriation index restated as "economic institutions" and "security of property rights" at the self-authored hub (HB-E1); independent users preserve the proxy wording.
- Main adjacent fields neglected: none at the source layer; downstream, the direct-disease (Sachs 2003) and human-capital (Glaeser 2004) rival tests are co-cited by small minorities (POST HOC rows).
- Main claim mutation: "the 7-fold differenceis an upperbound" (AJR-E2) becomes "almost the entire difference … could be explained" (HB-E1), citing the same page; publicly, "a clear chain of causality" (NP-E1).
- Most important ignored critique: Albouy (2012) in the broad citing mass (3.0% of 2013+ citers vs a 21.2% baseline), though engaged by the dominant cluster.
- Decisive test missing: an instrument-independent test of the cross-country magnitude, and a design separating colonial institutions from settler human capital.
- Verified risk score: 7/24
- Verified scored-dimension risk rate: 29.2
- Independent scored dimensions: 8
- Nested scored dimensions: 1
- Verified risk denominator: 24
- Evidentiary coverage: 9/10 (90%)
- Execution completeness: 10/10 (100%)
- Dimension inventory: 8 INDEPENDENT SCORED + 1 NESTED SCORED + 1 UNINFORMATIVE + 0 UNASSESSED + 1 N/A
- Unscored dimensions and reasons: Model non-updating UNINFORMATIVE (link 2 not met); Intervention-evidence ratchet N/A (no intervention claim)
- N-of-M scope statement: Verified scored-dimension risk: 29.2%, calculated from 8 independent scored dimensions; 1 additional scored dimensions are NESTED; 9 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.
- ARITHMETIC BAND POSITION: >20%–40% (normal field clustering with some weaknesses)
- RISK BAND: >20%–40% normal field clustering with some weaknesses — computed over 8 independent scored dimensions; breadth requirement PASSED (open-retrieval, outside the validated packet regime)
- MECHANISM LABEL: shared-data pseudo-convergence plus self-authored hub qualifier loss
- Formal-label gate status: PASSED (coverage 90% against the PROVISIONAL 70% threshold; no label-essential dimension UNASSESSED); closure labels unavailable
- Load-bearing finding(s): none against field 6; Findings 2 and 3 are load-bearing for the downstream L3 restatements
- Concede-test result: field 6 SURVIVES every finding; L3 NARROWS (Findings 2, 3, 6); L4 NARROWS incidentally (Finding 4)
- Failure location: CITATION (Findings 2, 3, 5, 6, 7), PR-MEDIA (Finding 4), MODEL-RETRIEVAL (Finding 1); none at PAPER for field 6
- Best formal label: normal small-field clustering (the field is not small; the label is the instrument's nearest option for ordinary canonical-paper centrality without closure)
- Confidence level: moderate that no closure exists inside the defined corpus; low on the magnitude of downstream inflation (citing passages retrieved for 13 of 50 top citers and 0 of 25 recent citers)
- What evidence would change this assessment: a seed-expanded or matched comparison graph showing higher closure; citing-passage retrieval for the recent corpus showing systematic upper-bound loss; verified (uncontested) disconfirmation of the settler-mortality data that later same-model papers ignore; or independent-data cross-country tests that reproduce the magnitude.
- DENSITY INFERENCE SCOPE (repeated): the density score applies only to the top-50 AJR-citing corpus (OpenAlex, cites:W3124166904, top 50 by cited_by_count). Closure is not established and not excluded beyond the defined corpus.

FINAL SECTION: STANDARDIZED FINDING TABLE

Finding 1

| Field | Entry |
|---|---|
| Finding | OpenAlex conflates AJR 2001 with the 2012 Reply and truncates the target's own reference list, so single-database citation metrics for AJR 2001 are unreliable. |
| Target claim | MAP GAP: this finding targets the retrieval record of AJR 2001 (citation counts and graph position), not map field 6. |
| What was measured | 34 of 40 in-corpus edges to the Reply record W3124131699 come from works published before 2012; AJR 2001 has 13 indexed references in OpenAlex; counts differ across OpenAlex 8,594, Crossref 7,813, Semantic Scholar 12,600, OpenAlex union 11,316. |
| What was claimed | Database citation counts and graphs represent the reception of AJR 2001. |
| Failure mode | model-retrieval identity conflation / reference truncation |
| Severity | moderate for any single-database network metric; none for field 6 |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | raw/top50_citers.json referenced_works and publication dates; raw/ajr2001_work.json; crossref_ajr2001.json; s2_ajr2001.json; refcount_compare.json (median OpenAlex/Crossref ratio 1.46 for corpus nodes). |
| Evidence type | secondary analysis |
| Verification state | RECEPTION-CONFIRMED |
| Possible innocent explanation | Working-paper versions of the Reply-era debate and DOI merges can legitimately produce early edges; databases differ in coverage by design. |
| What would weaken this | A database audit showing that the pre-2012 edges point to a genuine early version of the Reply rather than to AJR 2001. |
| Failure location | MODEL-RETRIEVAL — database record identity |
| Status | confirmed |

Finding 2

| Field | Entry |
|---|---|
| Finding | Downstream cross-country "confirmations" reuse the AJR settler-mortality series, so their agreement is specification robustness on one information origin rather than independent confirmation. |
| Target claim | MAP GAP: this finding targets L3, "independent work confirms that colonial institutions explain income differences", not map field 6. |
| What was measured | Rodrik et al. adopt the AJR instrument ("AER-test", RD-E1); Easterly–Levine state "AJR (2001) compiles data" for SETTLER MORTALITY (EL-E2); Chernozhukov et al. "use the same set of 64 country-level observations as AJR" (DML-E1); the Reply re-analyses the same series. |
| What was claimed | Multiple independent studies converge on the primacy of institutions. |
| Failure mode | source dependence / pseudo-convergence on shared data |
| Severity | moderate |
| Concede test | NARROWS |
| Scope loss if NARROWS | material — the breadth and independence of confirmation shrink to one data origin; the estimate itself is untouched. Surviving claim: several teams obtain similar estimates with the AJR instrument and data. |
| Evidence | RD-E1, EL-E2, DML-E1, DML-E2 (exact passages in citation-network/sources). |
| Evidence type | secondary analysis |
| Verification state | FULL-TEXT-CONFIRMED; CROSS-SOURCE-CONFIRMED |
| Possible innocent explanation | The instrument is the paper's contribution; reuse is expected, and these papers test alternative specifications and controls rather than claim independent data. Within-country designs (e.g., Banerjee–Iyer 2005) supply independent origins for L3. |
| What would weaken this | Cross-country tests with an independently constructed instrument reproducing the magnitude, or evidence that the downstream papers present themselves only as robustness checks. |
| Failure location | CITATION — downstream aggregation of non-independent tests |
| Status | confirmed |

Finding 3

| Field | Entry |
|---|---|
| Finding | The self-authored synthesis hub restates the p. 1387 magnitude implication without the authors' own upper-bound qualifier and broadens the construct from an expropriation-risk index to "economic institutions" and "security of property rights". |
| Target claim | MAP GAP: this finding targets the hub restatement of the field-6 estimate's magnitude implication, not map field 6 itself. |
| What was measured | AJR 2001 p. 1387: "the 7-fold differenceis an upperbound" (AJR-E2). AJR 2004 WP p. 29: "More precisely, we showed (p. 1387) … almost the entire difference in incomes per-capita between them could be explained by the differences in the security of property rights" (HB-E1). |
| What was claimed | Most of the rich–poor gap is due to economic institutions; almost the entire Nigeria–Chile difference is explained. |
| Failure mode | review-hub amplification / qualifier loss / construct broadening |
| Severity | moderate |
| Concede test | NARROWS |
| Scope loss if NARROWS | material — for the magnitude restatement, the surviving claim is that 0.94 implies up to about a 7-fold gap, an upper bound because of measurement error; incidental for field 6. |
| Evidence | AJR-E2 (AJR 2001 PDF p. 20 = AER p. 1387) and HB-E1 (NBER WP 10481 PDF p. 29). |
| Evidence type | review / synthesis restatement compared with primary source |
| Verification state | CROSS-SOURCE-CONFIRMED; FULL-TEXT-CONFIRMED |
| Possible innocent explanation | A synthesis paraphrases; the authors discuss measurement error elsewhere; the published Handbook chapter (not retrieved) may differ from the WP. |
| What would weaken this | The published 2005 Handbook text restoring the upper-bound qualifier, or a passage in the same chapter that does so. |
| Failure location | CITATION — self-authored hub restatement |
| Status | confirmed |

Finding 4

| Field | Entry |
|---|---|
| Finding | The 2024 Nobel popular background states "a clear chain of causality", while the scientific background says the IV estimate "should thus be taken with a grain of salt". |
| Target claim | MAP GAP: this finding targets map field 4 public wording (L4), not map field 6. |
| What was measured | NP-E1 (popular background p. 4) versus NS-E1, NS-E2 and NS-E3 (scientific background p. 19). |
| What was claimed | AJR uncovered a clear causal chain from institutions to long-run growth. |
| Failure mode | PR/media certainty inflation |
| Severity | minor |
| Concede test | NARROWS |
| Scope loss if NARROWS | incidental — the scientific wording survives: the evidence "strongly suggests" institutions are a key mechanism, with the IV estimate taken with a grain of salt. |
| Evidence | NP-E1; NS-E1; NS-E2; NS-E3. |
| Evidence type | public-facing synthesis |
| Verification state | CROSS-SOURCE-CONFIRMED |
| Possible innocent explanation | Popular texts compress; the same institution published the caveated scientific version at the same time. |
| What would weaken this | Evidence that the popular text elsewhere restores the caveat. |
| Failure location | PR-MEDIA — prize communication |
| Status | confirmed |

Finding 5

| Field | Entry |
|---|---|
| Finding | Albouy's (2012) data critique is engaged by the dominant cluster but rarely co-cited by the broad citing mass. |
| Target claim | In the base sample of 64 former colonies, the 2SLS estimate of the effect of the 1985–95 protection-against-expropriation index on 1995 log GDP per capita, instrumented by log settler mortality, is 0.94 (SE 0.16). |
| What was measured | 220/7,375 (3.0%) of 2013+ citers of AJR 2001 or the Reply co-cite Albouy; 50/2,695 (1.9%) of recent citers; baseline Rodríguez–Rodrik co-citation among Frankel–Romer citers 1,181/5,570 (21.2%). The Reply answers Albouy; the Nobel scientific background cites him (NS-E2). |
| What was claimed | The estimate is cited as settled background. |
| Failure mode | poor critique uptake in the citing mass |
| Severity | minor |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | union_citers_2013plus.json; union_citers_2013plus_albouy.json; recent_cocite_AL.json; baseline_fr_2001plus.json; baseline_fr_2001plus_rr.json; NS-E2. |
| Evidence type | secondary analysis |
| Verification state | RECEPTION-CONFIRMED; CONTESTED |
| Possible innocent explanation | Most citers use AJR for background, not for the estimate's robustness; the critique is CONTESTED and answered; the baseline pair is not matched on field or use. |
| What would weaken this | A matched baseline with similarly low uptake, or citing-passage evidence that recent users rely on capped or recoded variants. |
| Failure location | CITATION — downstream reception |
| Status | confirmed |

Finding 6

| Field | Entry |
|---|---|
| Finding | The source paper engages the geography and malaria rivals directly, but the later directly adjudicating rival tests (Sachs 2003; Glaeser et al. 2004) are co-cited by small minorities of downstream citers. |
| Target claim | MAP GAP: this finding targets L3, "institutions explain income differences", not map field 6. |
| What was measured | AJR Table 7 malaria control gives 0.69 (SE 0.25) (AJR-E4); Sachs: the null "may be readily rejected using … malaria risk" (SA-E1); Glaeser: malaria risk significant alongside settler mortality, human-capital channel (GL-E1, GL-E2); co-citation 4.4% (Sachs) and 13.6% (Glaeser) of union citers; recent 2.5% and 7.5%. |
| What was claimed | Institutions, not geography or human capital, are the fundamental cause of income differences. |
| Failure mode | adjacent rival-test non-uptake (downstream) |
| Severity | moderate |
| Concede test | NARROWS |
| Scope loss if NARROWS | material — surviving L3 claim: institutions are a major channel; direct disease and settler human-capital channels are not excluded. |
| Evidence | AJR-E4; SA-E1; GL-E1; GL-E2; NS-E3; union_citers_sachs.json; union_citers_glaeser.json; recent_cocite_SA.json; recent_cocite_GL.json. |
| Evidence type | primary empirical (rival tests) with reception counts |
| Verification state | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED; CONTESTED |
| Possible innocent explanation | The rival tests are themselves CONTESTED; many citers address unrelated questions; the rows are POST HOC and cannot anchor a higher score. |
| What would weaken this | Decisive evidence rebutting the malaria and human-capital channels, or citing-passage evidence that downstream users acknowledge the rivals without citing them. |
| Failure location | CITATION — downstream reception of rival tests |
| Status | contested |

Finding 7

| Field | Entry |
|---|---|
| Finding | Acquittal on closure: inside the defined top-50 citing corpus, internal density is low and critics are as central as the founding team. |
| Target claim | In the base sample of 64 former colonies, the 2SLS estimate of the effect of the 1985–95 protection-against-expropriation index on 1995 log GDP per capita, instrumented by log settler mortality, is 0.94 (SE 0.16). |
| What was measured | Directed density 136/2450 = 5.55% (87/2352 = 3.70% excluding N01); in-degree leaders N21 12, N02 12, N03 9; reference lists not truncated (Crossref check). |
| What was claimed | (Prosecutorial hypothesis) The estimate's authority rests on a closed self-referential cluster. |
| Failure mode | none — acquittal |
| Severity | none |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | graph.json; graph_derived.json; refcount_compare.json; Section A receipts. |
| Evidence type | secondary analysis |
| Verification state | RECEPTION-CONFIRMED |
| Possible innocent explanation | Not applicable to an acquittal; the limitation is that closure is not established and not excluded beyond the defined corpus. |
| What would weaken this | A seed-expanded or matched comparison graph showing materially higher closure. |
| Failure location | CITATION — network structure |
| Status | confirmed |
