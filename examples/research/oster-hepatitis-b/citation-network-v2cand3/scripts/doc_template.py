# Executed by build_2c.py with its namespace. Emits out/02c_citation_network_v2cand3.md
L=[]
a=L.append
def blank(): a('')
S2='CTX-E ids resolve to Semantic Scholar citation contexts (request /graph/v1/paper/DOI:10.1086/498588/citations?fields=title,externalIds,year,contexts,intents&limit=1000, 2026-11-05T10:26:46Z, HTTP 200, response sha256 c570ae9f4fa617d1b873a455054a752b97ab0077f77d1ce11ed3e83576d1c3c4; response not committed)'
a('# Citation-Network Audit, v2-candidate.3 run — Oster (2005), "Hepatitis B and the Case of the Missing Women"'); blank()
a('INSTRUMENT PREFLIGHT: yungmulaBABY1/Provenance @ a58d165d9a986edca220f8143fc0c0d9316c8a13 : candidates/research-analysis/2-citation-network.v2-candidate.txt | git blob fcbf4e80cfbaf1558784d052d3b8933b594310c7 | sha256 efc1a9fc336c30a67645ac9257701aa2ebe07dcc0be59f8e28523b0800d53064 | 2001 lines | 89337 bytes | markers: version line "2-citation-network v2-candidate.3", map "cn7-map-3" | IDENTITY CONFIRMED (gate checker blob b75a27e7…, sha256 ce6661a5…; v1 checker blob a3da0827…, sha256 f66650fe…)'); blank()
a('INSTRUMENT VERSION: 2-citation-network v2-candidate.3'); blank()
a('DIMENSION CLASS MAP: cn7-map-3'); blank()
a('Run metadata. LIVE RUN of citation-network candidate revision 3 (not a validation run), Batch 1 of the four-paper brief. Executor: Grok Bot (audit run), branch audit/oster-hepatitis-b from Provenance-Atlas main 6c651d7593abfb5c4b6d2eb9f6846a5212fe001c. Execution date 2026-11-05 UTC (early morning PST). Clock times are UTC with PST (UTC-8) where useful. Mode: full sequence; upstream claim map ../01_claim_extraction.md (this run). Tools: OpenAlex works API with select= lists omitting abstract_inverted_index (corpora, graph, co-citation counts); Semantic Scholar citation contexts as EXCERPT access; authorized full texts (JPE article copy for the target; NBER WP w13971; Lin & Luoh author working paper; Europe PMC PMC11137505; Slate; Klasen comments on the Göttingen site). Recent window: from 2021-11-05. No abstract was read, coded from, or written to any file.'); blank()
a('VALIDATION BOUNDARY. This instrument revision is a candidate. It has not been validated for open retrieval. This run used open retrieval over three registered corpora (49 + 6 + 46 works). Every percentage, band and label below is an unvalidated open-retrieval application, not a validated verdict.'); blank()
a('EXPOSURE DISCLOSURE. Before this stage the executor had read the target (JPE 2005, full text) for Stages 1, 2a and 2b, and knew from prior reading (declared in 00a) that Lin & Luoh (2008, AER) and Oster, Chen, Yu & Lin (2010, Economics Letters) report null carrier effects and that Das Gupta (2005, 2006) disputed the HBV account. The 00a known-item list was written before the ADJUDICATION-1 search. The Section E lock is post-exposure (bibliography read in Stage 1) and is mechanical for that reason: sources are fixed by a ranked query, not chosen.'); blank()
a('PRE-AUDIT CLAIM CONFIRMATION'); blank()
a('- Claim under audit (map field 6): HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale\'s (1991) 60.26 million missing women in seven Asian/North-African units, mid-1980s (Table 11, Panel A).')
a('- What was literally measured (map field 1): associations between HBsAg carrier status or prevalence and offspring or population sex ratios (six small family studies; Alaska/Taiwan series; 38-country cross-section; immigrants; Chinese counties), plus a calibrated re-run of Coale\'s accounting with HBV-predicted sex ratios (Tables 10–11).')
a('- Weaker defensible claim (map field 3): conditional on a carrier offspring sex ratio of 1.54, the author\'s prevalence inputs and Coale\'s framework, about 47% (CI 13.5–71.5, sampling only) is an upper-bound total effect; aggregate associations are consistent with but not decisive for causality.')
a('- Target layer: field 6 (layer L3 below) for the network verdict; layers L1–L4 and rivals R1–R4 are defined below.'); blank()
a('The map is upstream-generated, not self-generated.'); blank()
a('SECTION A0: CORPUS REGISTER AND SOURCE ELIGIBILITY'); blank()
a('Corpus planning. Questions: (a) how Oster (2005) is received (RECEPTION-1, RECENT-1); (b) what the evidence base testing the layers and rivals contains (ADJUDICATION-1). Proposed inferences were tested in SECTION K0 before use; those that fail stay there as INSUFFICIENT or NOT-ASSESSED.'); blank()
a('CLAIM LAYERS AND RIVALS'); blank()
a('CLAIM LAYER: L1 — Individual carrier effect: offspring sex ratio of HBV carriers about 1.5 (1.54, CI 1.29–1.87).')
a('CLAIM LAYER: L2 — Population transmission: HBV prevalence raises the population sex ratio at birth.')
a('CLAIM LAYER: L3 — Accounting share (map field 6): HBV accounts for 47.24% of Coale\'s 60.26M missing women.')
a('CLAIM LAYER: L4 — Interpretive: the imbalance is less attributable to discrimination; the remaining problem is concentrated in India and Pakistan.')
a('RIVAL: R1 — Son preference and sex-selective behaviour (parity-specific).')
a('RIVAL: R2 — Null or small individual carrier effect in large samples.')
a('RIVAL: R3 — Ecological confounding of the HBV–sex-ratio association.')
a('RIVAL: R4 — Benchmark misspecification (expected sex ratio varies with life expectancy or mortality).'); blank()
a('CORPUS REGISTER'); blank()
a('CORPUS ID: RECEPTION-1')
a('CORPUS ROLE: RECEPTION')
a('CORPUS QUESTION: How the most-cited works citing Oster (2005) relate to it and to each other.')
a('CORPUS SELECTION RULE: OpenAlex works API, /works?filter=referenced_works:W3123222584&sort=cited_by_count:desc&per_page=50, page 1, executed 2026-11-05T10:25:08Z (2:25 AM PST); population 172; no date or type bounds; no screening; one row per work (W2125485011 and W1581958734 are one work, row N09); response raw/reception1_top50.json sha256 2529864d8e37346ee333a78ce835bf45ddfc78a8464ed656b8cde1dff54dc980.')
a('CORPUS DISCOVERY: SEARCHED — ranked citation query (top 50 by cited_by_count); request, execution time and response hash recorded above')
a('SELECTED ON TARGET CITATION: YES')
a(f'CORPUS SIZE: {len(members("RECEPTION-1"))}')
a(f'CITATION CONTEXT COVERAGE: RECEPTION-1 {cov["RECEPTION-1"][0]}/{cov["RECEPTION-1"][1]}')
a('RECORD QUALITY: target record W3123222584 lists 318 referenced works (implausibly many) and has a RePEc preprint duplicate W3126094291; one work appears as two records (N09 W2125485011, N35 W1581958734; merged); two members are implausible citers (N19 income inequality and CO2; N44 prenatal smoking); OpenAlex reference lists are incomplete for some members.')
a('CORPUS LOCK: 2026-11-05T10:25:08Z; response sha256 2529864d8e37346ee333a78ce835bf45ddfc78a8464ed656b8cde1dff54dc980'); blank()
a('CORPUS ID: RECENT-1')
a('CORPUS ROLE: RECEPTION')
a('CORPUS QUESTION: How recent (2021-11-05 onward) citing works use Oster (2005).')
a('CORPUS SELECTION RULE: OpenAlex works API, /works?filter=from_publication_date:2021-11-05,referenced_works:W3123222584&sort=cited_by_count:desc&per_page=25, executed 2026-11-05T10:25:12Z; population 6, so the top-25 rule returns a census; all 6 were to be inspected (lock/SAMPLES_draw.txt). Response raw/recent1_top25.json sha256 899ac2a524ef89b323e886bdc5fdb09908db38f01e03cbd2dc2975835126c46b.')
a('CORPUS DISCOVERY: SEARCHED — ranked citation query; request, execution time and response hash recorded above')
a('SELECTED ON TARGET CITATION: YES')
a(f'CORPUS SIZE: {len(members("RECENT-1"))}')
a(f'CITATION CONTEXT COVERAGE: RECENT-1 {cov["RECENT-1"][0]}/{cov["RECENT-1"][1]}')
a('RECORD QUALITY: a population of 6 recent citers is implausibly small for a JPE paper with 172 OpenAlex citers (incomplete citation links); R01 (= N19) is an implausible citer; three of six are dissertations or low-visibility items.')
a('CORPUS LOCK: 2026-11-05T10:25:12Z; response sha256 899ac2a524ef89b323e886bdc5fdb09908db38f01e03cbd2dc2975835126c46b'); blank()
a('CORPUS ID: ADJUDICATION-1')
a('CORPUS ROLE: ADJUDICATION')
a('CORPUS QUESTION: What tests of claim layers L1–L4 and rivals R1–R4 exist, whether or not they cite the target, and what they find.')
a('CORPUS SELECTION RULE: OpenAlex works API, five title_and_abstract.search queries Q1–Q5 (exact strings, date bounds 1980-01-01 to 2026-11-05 and types article|preprint|book-chapter in lock/ADJUDICATION-1_search_record.md), relevance ranking, top 10 per query, select= without abstract_inverted_index; one row per work; screening from title and record metadata only (abstracts not used), codes DIRECT (L1)/(R2)/(L2)/(R3)/(L3)/(L4)/(R1)/(R4), ADJACENT, BACKGROUND, UNRELATED, UNKNOWN.')
a('CORPUS DISCOVERY: SEARCHED — lock/ADJUDICATION-1_search_record.md (raw/adj1_Q1..Q5.json, executed 2026-11-05T10:26:08Z)')
a('SELECTED ON TARGET CITATION: NO')
a(f'CORPUS SIZE: {len(members("ADJUDICATION-1"))}')
a(f'CITATION CONTEXT COVERAGE: ADJUDICATION-1 {cov["ADJUDICATION-1"][0]}/{cov["ADJUDICATION-1"][1]}')
a('RECORD QUALITY: target returned as two records (W3123222584, W3126094291; row T01); Drew et al. 1978 returned as the Science record and a 2000 reprint (row X01); the Kim baby-bonus work as two records (one row); several Q5 records have empty reference lists; titles only were used for screening, so relevance codes are METADATA-coded.')
a('CORPUS LOCK: 2026-11-05T10:24:54Z (2:24:54 AM PST); search record sha256 aeead2c9ebc5cdbb6004693fb7109093654184fd3412ad2792e11c576baa97f8')
a('KNOWN-ITEM RECALL: ADJUDICATION-1 3/8 (returned: K1 Das Gupta 2005 PDR [N08], K2 Lin & Luoh 2008 AER [N31], K8 Chahnazarian 1988 [A06]; not returned: K3 Oster, Chen, Yu & Lin 2010 Economics Letters, K4 Oster reply to Das Gupta, K5 Das Gupta 2006 PDR, K6 Klasen 2008, K7 Anderson & Ray 2010 REStud). K3, K5 and K7 are RECEPTION-1 members (N45, N46, N04) and enter adjudication only as POST HOC; K4 and K6 were not retrieved.'); blank()
a('Overlap. N08, N25, N31 and N32 are in RECEPTION-1 and ADJUDICATION-1 and are recorded once with both corpus IDs; N19 is in RECEPTION-1 and RECENT-1 (also listed as R01). Reception rank does not weight the adjudication role. Duplicate records of one work are merged into one row with every identifier listed: N09 (+N35 record), T01 (+preprint record), X01 (+reprint record), and the Kim baby-bonus row. Rows X02–X12 are OUTSIDE every registered corpus (Section E locked sources and two named sources); they carry no corpus count.'); blank()
a('SOURCE ELIGIBILITY LEDGER'); blank()
a('| Source | Corpus membership | Question relevance | Relation to target | Evidence contribution | Source access | Citation context | Supported inference |')
a('|---|---|---|---|---|---|---|---|')
for r in rows:
    a('| '+' | '.join(x.replace('|','/') for x in r[1:])+' |')
blank()
a(f'Coding notes. {S2}. Relation for ADJUDICATION-1 non-reception members: OpenAlex reference list contains W3123222584 → CITES-UNINSPECTED; reference list empty or sparse → UNKNOWN; non-empty list without the target, or publication before the target → NOT-CITING (NOT-APPLICABLE). DIRECT members published after 2005 stay UNKNOWN when OpenAlex omits the target, because reference lists are incomplete. Relevance and contribution for METADATA rows are coded from the title only (abstracts were not used under the rights rules). JP-E ids resolve to pages of the target (JPE 113(6)): JP-E1 p. 1172 (sex-selective abortion literature), JP-E2 p. 1179 (six family studies), JP-E3 p. 1201 (share of missing women), JP-E4 p. 1203 n. 26 (Klasen & Wink), JP-E5 p. 1203 n. 27 (benchmark), JP-E6 p. 1189 (life-expectancy controls). LL-E, OC-E, BA-E, SL-E and KL-E ids resolve to the pages given in each row.'); blank()
a('SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION'); blank()
a('GRAPH CORPUS AND RECEIPTS'); blank()
a(f'GRAPH CORPUS DEFINITION: RECEPTION-1 as registered in SECTION A0 (OpenAlex, filter=referenced_works:W3123222584, sort=cited_by_count:desc, top 50 records, executed 2026-11-05T10:25:08Z, no date or type bounds, no screening). Nodes are works: the two records of row N09 are one node, so n = {n}. The target is outside the density corpus; citer -> target edges hold by construction and are not counted.')
a(f'GRAPH CORPUS NODE LIST: {nodelist}')
a(f'INTERNAL EDGE LIST: {edgelist}')
a('DERIVATION MODE: COMPUTED-FROM-RETRIEVED')
a(f'DENSITY CALCULATION: directed density = directed internal edges u -> v (u, v work nodes, u != v, v in OpenAlex referenced_works of u) / n(n-1), n = {n}; computed by scripts/build_2c.py from raw/reception1_top50.json (record-level cross-check by scripts/graph.py).')
a(f'DENSITY NUMERATOR: {len(E)} directed internal edges among the {n} work nodes.')
a(f'DENSITY DENOMINATOR: {den} possible directed edges ({n} × {n-1}).')
a(f'DENSITY INPUT COVERAGE: 50/50 record reference lists obtained from OpenAlex ({refs_total:,} indexed references across the {n} works). No Crossref cross-check.')
a('DENSITY INFERENCE SCOPE: the density result applies only to RECEPTION-1. Because RECEPTION-1 is selected on target citation, it can establish density inside that target-citing corpus; it cannot establish or exclude field-wide, founding-cluster or premise-subnetwork closure. No seed-expanded or matched comparison graph was built.'); blank()
a('Closure is not established and not excluded beyond the defined corpus.'); blank()
a(f'Density results. Work-level directed density {len(E)}/{den} = {D["dens"]}; record-level (50 records) {D["nrec"]}/2450 = {D["drec"]}. {citing}/{n} works cite at least one other member. Reciprocal pairs: {recip}. In-degree leaders: {lead}. The two most-cited nodes inside the corpus are critiques of the target (N08 Das Gupta 2005; N31 Lin & Luoh 2008). Oster-authored works (N12, N24, N45) receive {ost_in}/{len(E)} internal edges, {indeg["N45"]} of them to N45, the author\'s own null test.'); blank()
a('1. Top 50 most-cited works citing Oster (2005): RECEPTION-1 (Artifact 1 lists the top 15). Relevance composition: '+COMP['I17'][0]+'.')
a('2. Founding cluster: the target alone; there is no co-authoring team. Oster-authored works in RECEPTION-1: N12 (2008 JDE), N24 (2009 Demography), N45 (2010 Economics Letters, with Chen, Yu and Lin). The HBV–sex-ratio studies the target pools (Drew et al. 1978 onward) are prior medical work by other teams.')
a('3. Founding papers\' evidence type: the target is a secondary analysis of six small published family studies plus country and county associations (FULL-TEXT, JP-E2); N45 is a primary cohort test (FULL-TEXT, VERSION-SUBSTITUTE).')
a(f'4. Hubs: N08 (in-degree {indeg["N08"]}) and N31 ({indeg["N31"]}) are critiques; N01 Qian 2008 ({indeg["N01"]}) is an R1 study. Oster-authored works receive {ost_in}/{len(E)} internal edges.')
a(f'5. Hub substitution: within RECEPTION-1, {either(ws)}/{n} works co-cite Lin & Luoh 2008 or Oster et al. 2010 alongside the target; among the {len(post)} works published 2009 or later, {either(post)}/{len(post)}.')
a(f'6. Small cluster citing itself: no closed cluster inside RECEPTION-1 (density {D["dens"]}).')
a('7. Gatekeeping roles: no editorial or referee data retrieved; UNASSESSED.')
a('8. Self-citation in the founding cluster: N12 and N24 are the author\'s later son-preference work; N45 is the author\'s own test that withdraws L1 in substance.')
a('9. Concentration by lab/journal/funder: not assessed beyond authorship (SECTION I).')
a('10. Citation count vs independent confirmation: target cited_by_count 173 at retrieval; independent tests of L1 with new data (N31, N45, R03) are null (I13, I14).'); blank()
a('SECTION B: EVIDENCE TYPE CODING'); blank()
a('Every corpus member is coded in the SOURCE ELIGIBILITY LEDGER. Questions 11–16 describe the evidence base only on ADJUDICATION-1, the SEARCHED adjudication corpus; on RECEPTION-1 they describe the citing set.'); blank()
a('ADJUDICATION-1 composition (evidence base, bounded by the locked search; METADATA-coded):')
for iid,col in (('I15','relevance'),('I16','contribution')): a(f'COMPOSITION: {iid} | {col} | {COMP[iid][0]} | TOTAL={COMP[iid][1]}')
a('RECEPTION-1 composition (citing set only):')
a(f'COMPOSITION: I17 | relevance | {COMP["I17"][0]} | TOTAL={COMP["I17"][1]}'); blank()
dl1=[r[0] for r in members('ADJUDICATION-1') if r[3].startswith('DIRECT (L1)')]
dr1=[r[0] for r in members('ADJUDICATION-1') if r[3].startswith('DIRECT (R1)')]
dr2=[r[0] for r in members('ADJUDICATION-1') if r[3].startswith('DIRECT (R2)')]
a(f'11. Primary empirical tests in ADJUDICATION-1: DIRECT (L1) {len(dl1)} ({", ".join(dl1)}), DIRECT (R2) {len(dr2)} ({", ".join(dr2)}), DIRECT (R1) {len(dr1)}. Most DIRECT (L1) members are the pre-2005 family studies the target pools or later small studies whose results were not read (A04, A07, A09; I23).')
a('12. Reviews/syntheses: REVIEW and COMMENTARY members are counted in I16; none was read in full.')
a('13. Theory-only: THEORY members are counted in I16 (for example A08, James 2007 hypothesis note).')
a('14. Unknown: relevance UNKNOWN as counted in I15; Relation UNKNOWN is common where OpenAlex reference lists are empty or omit the target.')
a('15. Evidence-to-claim ratio: the L1 evidence the target rests on is six small family studies (355 boys and 248 girls among carriers\' children, JP-E2); the later large tests (N31 Taiwan births, N45 Chinese cohort of about 67,000, R03 Ghana) use new and independent data (I14).')
a(f'16. On RECEPTION-1 the same questions describe citers: {COMP["I17"][0]} (of {COMP["I17"][1]}).'); blank()
a('SECTION C: CITATION POLARITY AND CLAIM USE'); blank()
ni=cov['RECEPTION-1'][0]
a(f'Citing passages inspected: CITATION CONTEXT COVERAGE: RECEPTION-1 {cov["RECEPTION-1"][0]}/{cov["RECEPTION-1"][1]} ({", ".join(insp_rec)}); CITATION CONTEXT COVERAGE: RECENT-1 {cov["RECENT-1"][0]}/{cov["RECENT-1"][1]}; CITATION CONTEXT COVERAGE: ADJUDICATION-1 {cov["ADJUDICATION-1"][0]}/{cov["ADJUDICATION-1"][1]}. Most RECEPTION-1 passages are EXCERPT (Semantic Scholar contexts). The prespecified random sample of 12 lost 9 members (I05). Percentages use inspected passages only.'); blank()
a(f'17. Supportive: SUPPORTS {relc.get("SUPPORTS",0)}/{ni} (N12 self-citation; N13 "confirmed").')
a(f'18. Critical: CHALLENGES {relc.get("CHALLENGES",0)}/{ni}; QUALIFIES {relc.get("QUALIFIES",0)}/{ni}.')
a(f'19. Perfunctory/background: MENTIONS {relc.get("MENTIONS",0)}/{ni}. RECENT-1: R03 CHALLENGES (tests and rejects L1), R04 MENTIONS.')
a('20. Premise use: none of the inspected passages uses the HBV share as a premise for its own analysis.')
a('21. Data/instrument reuse: none.')
a('22. Polarity inflation: N13 upgrades the target\'s pooled re-tabulation to a confirmation (CTX-E8); N03 misdescribes the mechanism as female-biased disease (CTX-E1). Slate states the 50-million figure conditionally (SL-E1).'); blank()
a('SECTION D: CLAIM MUTATION TRACKING'); blank()
a('23–30. Original (JP-E3, p. 1201): about 47 percent of Coale\'s missing women, roughly 75 percent in China and under 20 percent in India, with a wide interval (13.5–71.5). Downstream restatements mostly preserve the magnitude: N07 "about 70%" (CTX-E4), N11 "around 75%" for China and "around 17%" for India (CTX-E5, CTX-E6), N31 roughly half (CTX-E15), N46 75 percent for China (CTX-E21), R03 about 75% and about 20% (BA-E1), Slate roughly 50 million, conditional on the results being compelling (SL-E1). Mutations found: a certainty upgrade in N13 ("confirmed", CTX-E8) and a mechanism misdescription in N03 (female-biased disease, CTX-E1). R03 frames the effect as maternal carrier status (BA-E1), whereas the target pools both parents. Severity: minor; no restatement inflates the magnitude. Post-refutation passages that state the HBV effect without the refutation (N36, N27, R04) are use drift, treated in SECTION H, not magnitude mutation.'); blank()
a('| Original source | Original claim | Hub restatement | Downstream restatement | Mutation severity | Note |')
a('|---|---|---|---|---|---|')
a('| Oster 2005 p. 1201 (JP-E3) | about 47% of missing women; CI 13.5–71.5 | none found | N07 "about 70%" China; N31 roughly half | none | magnitude preserved |')
a('| Oster 2005 p. 1179 (JP-E2) | pooled re-tabulation of six family studies | none found | N13: "the result confirmed by Oster (2005)" | minor | certainty upgrade |')
a('| Oster 2005 p. 1179 (JP-E2) | carriers have more sons | none found | N03: "greater incidence of female-biased diseases" | minor | mechanism misdescribed |')
a('| Oster 2005 p. 1179 (JP-E2) | carrier parent (either parent) | none found | R03: maternal carrier status (BA-E1) | minor | carrier narrowed to mother |'); blank()
a('SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT'); blank()
a('Steps 31–37. Layers L1–L4 and rivals R1–R4 are locked in lock/ADJUDICATION-1_search_record.md; fields F1–F4 and observations O1–O4 in lock/section_E_preregistration.md, hashed before the Section E queries ran. The lock is post-exposure (the target bibliography was read in Stage 1), so sources are fixed mechanically by a ranked query.'); blank()
a('SOURCE-LOCK METHOD: LOCKED QUERY')
a('SOURCE-LOCK DATABASE: OpenAlex works API (select omits abstract_inverted_index)')
a('SOURCE-LOCK QUERY OR SOURCE LIST: filter=title.search:<terms>,to_publication_date:2005-06-30,type:article, sort=cited_by_count:desc, per-page=3; terms F1 "son preference", F2 "hepatitis B sex ratio", F3 "sex ratio at birth", F4 "missing women"')
a('SOURCE-LOCK DATE CUTOFF: 2005-06-30 (publication on or before; JPE issue December 2005)')
a('SOURCE-LOCK RANKING RULE: OpenAlex cited_by_count descending at query time')
a('SOURCE-LOCK N: 12 (top 3 per field × 4 fields)')
a('SOURCE-LOCK DEDUPLICATION RULE: by OpenAlex work ID; off-topic items retained and flagged, never replaced')
a('SOURCE-LOCK TIMESTAMP OR HASH: 2026-11-05T10:29:05Z (2:29:05 AM PST); preregistration sha256 5e43e7a48d3a4271fd842e65b14fcc7e06b9ae94a3f705a618cca3a3120f9451; queries executed after the lock (F1 after about nine HTTP 429 retries, success 10:35:51Z)'); blank()
a('Flip test (step 37): PASS. F1 and F3 are generated from rivals R1 and R4; F2 from both L1 and R2; F4 from L3 and R4 (both). Innocent explanations: F1 exemplars include an off-topic labour paper (X04); F3 exemplars include animal biology (X07).'); blank()
a('Falsification-relevant literature preregistration table:'); blank()
a('| Claim layer | Audited explanation | Strongest plausible rival explanation | Adjudicating observation | Candidate field | Generated from audited claim, rival, or both? | Measurement relevance | Adjudicative capacity | Independence | Publication-date cutoff | Historically available? | Flip-test result | Source-lock method | Lock timestamp / hash | Final engagement classification |')
a('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
a('| L2/L3 | HBV raises the sex ratio at birth | R1 son preference and sex selection | O1 parity-specific sex ratios | F1 son preference | rival | sex-selection behaviour | could weaken L3 | independent | 2005-06-30 | yes | PASS | LOCKED QUERY | 5e43e7a4…9451 | direct substantive engagement (JP-E1 discusses sex-selective abortion) |')
a('| L1 | carriers have more sons | R2 null carrier effect | O2 carrier vs non-carrier offspring sex | F2 HBV and offspring sex | both | individual-level effect | could defeat L1 | independent of the target | 2005-06-30 | yes | PASS | LOCKED QUERY | as above | direct substantive engagement (JP-E2 pools the F2 studies) |')
a('| L3 | HBV-adjusted benchmark | R4 benchmark varies with mortality | O3 natural sex-ratio variation | F3 sex ratio at birth | rival | benchmark validity | could narrow L3 | independent | 2005-06-30 | yes | PASS | LOCKED QUERY | as above | citation with partial engagement (Zeng/Yi et al. cited, JP-E1; life-expectancy controls, JP-E6) |')
a('| L3 | 47% of Coale\'s missing women | R4 and alternative counts | O4 deficit under other benchmarks | F4 missing-women accounting | both | the accounted quantity | could narrow L3 | independent | 2005-06-30 | yes | PASS | LOCKED QUERY | as above | direct substantive engagement (JP-E4, JP-E5) |'); blank()
bysid={r[0]:r for r in rows}
neg=[('L2/L3','F1 son preference','X04','BACKGROUND (off-topic labour paper)','no','not cited','none'),
     ('L2/L3','F1 son preference','X05','son preference persistence','no','not cited; R1 literature engaged via other works (JP-E1)','minor context loss'),
     ('L2/L3','F1 son preference','X06','sex composition and son preference, India','no','not cited; R1 engaged via other works','minor context loss'),
     ('L1','F2 HBV and offspring sex','X01','carrier families have more sons','yes (target)','substantively engaged (JP-E2)','none'),
     ('L1','F2 HBV and offspring sex','A06','four-population comparison','yes (target)','substantively engaged (JP-E2)','none'),
     ('L1','F2 HBV and offspring sex','A03','Greenland family study','yes (target)','substantively engaged (JP-E2)','none'),
     ('L3','F3 sex ratio at birth','X07','animal sex-ratio biology','no','not cited','none'),
     ('L3','F3 sex ratio at birth','X08','rising reported sex ratio in China; underreporting and sex selection','yes (target)','directly engaged (JP-E1)','none'),
     ('L3','F3 sex ratio at birth','X09','hormonal hypothesis of sex ratios','no','not cited (other James papers cited)','minor context loss'),
     ('L3','F4 missing women','X10','missing women revisited','no','not cited (2002 update cited instead)','minor context loss'),
     ('L3','F4 missing women','X11','updated missing-women estimates','yes (target)','substantively engaged (JP-E4)','none'),
     ('L3','F4 missing women','X12','missing women reconsidered, benchmark','yes (target)','engaged; benchmark argument answered in part (JP-E5, JP-E6)','none')]
cls={'F1 son preference':'MECHANISM-SUPPORTING','F2 HBV and offspring sex':'DIRECTLY-ADJUDICATING','F3 sex ratio at birth':'CONSTRUCT-DEFINING','F4 missing women':'CONSTRUCT-DEFINING'}
NEGH='| Claim layer | Adjacent field | Nominated source and stable identifier | Verification state | Source class: CONSTRUCT-DEFINING / MECHANISM-SUPPORTING / DIRECTLY-ADJUDICATING | Actual result | Explanation favored | Explanation weakened | Precise revision required | Pre-inspection lock status or POST HOC | Cited by dominant cluster? | Engagement quality | Effect of omission |'
def negrows():
    a(NEGH); a('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    for lay,f,sid,res,cited,eng,eff in neg:
        wid_=bysid[sid][1].split()[1]
        if cls[f]=='DIRECTLY-ADJUDICATING':
            a(f'| {lay} | {f} | {sid} {wid_} | LOCATED | {cls[f]} | {res}: carriers\' offspring male-biased, as tabulated in the target (JP-E2; source text not read) | L1 | R2 (at small-sample level) | none for L1 from this source alone; superseded by larger tests (I13) | LOCKED (Section E query) | {cited} | {eng} | {eff} |')
        else:
            a(f'| {lay} | {f} | {sid} {wid_} | LOCATED | {cls[f]} | {res} (title; results not read) | — | — | — | LOCKED (Section E query) | {cited} | {eng} | {eff} |')
a('Adjacent-literature neglect table:'); blank()
negrows()
a('| L1 | R2 test | N31 W1994568240 Lin & Luoh 2008 | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | carrier mothers\' effect 0.0010–0.0025 (LL-E1) | R2 | L1, L3 | L1: carrier effect near zero; L3 not supported | LOCKED (ADJUDICATION-1 search) | yes (N45 cites it) | substantively engaged by the author (OC-E2) | not omitted |')
a('| L1 | R2 test | N45 W2042478072 Oster, Chen, Yu & Lin 2010 | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | 51.06% vs 51.56% male (OC-E1) | R2 | L1, L2, L3 | L3 withdrawn for China by the author (OC-E2) | POST HOC (known item K3, not returned by the locked search) | author\'s own work | the update itself | not omitted |')
a('| L1 | R2 test | R03 W4397030871 Banyeh et al. 2024 | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | no association of maternal carrier status with infant sex (BA-E2) | R2 | L1 | as above | POST HOC (RECENT-1 member, not ADJUDICATION-1) | n/a (2024) | — | not omitted |'); blank()
a('The source layer engages R1 (JP-E1), the F2 family studies (JP-E2) and the R4 benchmark debate (JP-E4, JP-E5, JP-E6). Of the 12 locked sources the target cites 6 (all three F2 sources, X08, X11, X12). The uncited items are off-topic exemplars or near-duplicates of cited work. ENGAGEMENT I19 carries the score; the R2 tests post-date the target and are scored under decisive tests and critique uptake.'); blank()
a('SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING'); blank()
a(f'40. Hubs inside RECEPTION-1: N08 Das Gupta 2005 (in-degree {indeg["N08"]}), N31 Lin & Luoh 2008 ({indeg["N31"]}), N01 Qian 2008 ({indeg["N01"]}), N45 Oster et al. 2010 ({indeg["N45"]}). Review-type works: N21 Dyson 2012 (Annual Review of Sociology), N13 James 2007, handbook chapters N06, N17, N22.')
a(f'41. Recent papers citing the hubs: Das Gupta 2005 {rc_DG5}/6, Lin & Luoh {rc_LL}/6, Oster et al. 2010 {rc_O10}/6 in RECENT-1.')
a('42. Recent papers citing primary evidence directly: 6/6 cite the target by construction.')
a('43. Hub substitution for inspection: not measurable from reference lists; no passage citing a review hub was inspected (I22 NOT-ASSESSED).')
a('44–45. Hub accuracy: N13 (James 2007) upgrades certainty (CTX-E8); N21 Dyson not inspected.')
a('46. Adjacent literatures in hubs: N08 and N46 are demography (R1); N31 and N45 are economics with medical data.')
a('47. Hub as substitute for primary evidence: UNASSESSED.'); blank()
a('| Hub paper | Recent papers citing hub | Recent papers citing primary evidence directly | Adjacent-field citation rate | Hub accuracy | Hub risk |')
a('|---|---|---|---|---|---|')
a(f'| Das Gupta 2005 (N08) | {rc_DG5}/6 RECENT-1 | 6/6 by construction | {cc(ws,DG5)}/{n} RECEPTION-1 co-cite | critique; not inspected | low |')
a(f'| Lin & Luoh 2008 (N31) | {rc_LL}/6 RECENT-1 | 6/6 by construction | {cc(ws,LL)}/{n} RECEPTION-1 co-cite | accurate restatement (CTX-E15) and null test | low |')
a('| James 2007 (N13) | 0/6 RECENT-1 | 6/6 by construction | — | certainty upgrade (CTX-E8) | low (small in-corpus in-degree) |')
a('| Dyson 2012 (N21) | 0/6 RECENT-1 | 6/6 by construction | — | not inspected | UNASSESSED |'); blank()
a('SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR'); blank()
a('48. Proxy treated as construct: carrier prevalence stands in for an offspring sex-ratio effect; the inspected restatements keep the share framing (SECTION D); proxy mismatch was not traced further.')
a('49. Export from low-stakes settings: the 1.54 carrier sex ratio comes from small, mostly non-Asian family studies (JP-E2) and is exported to Asian populations; this is a paper-level issue (Stages 2a/2b).')
a('50. Ignored natural experiments: no; the target uses vaccination (Alaska, Taiwan) as quasi-experiments.')
a('51. Model updating: yes; the author\'s cohort test concludes HBV cannot explain China\'s male-biased sex ratios (OC-E2).')
a('52. Intervention expansion: no intervention claim; N/A.')
a('53–55. Falsification criteria: the target states that vaccination should lower sex ratios; later tests use carrier status directly. 55 N/A.')
a('56. Expansion over testing: no.'); blank()
a('Ratchet scoring route. Intervention-evidence ratchet: N/A (no intervention claim). Model non-updating four-link gate: link 1 (model stated: HBV explains a large share) met, JP-E3; link 2 (verified later disconfirming evidence) met, N31 and N45 FULL-TEXT (I13); link 3 (reception opportunity) met, the author co-wrote N45; link 4 (non-updating) NOT met: the author updates (I18). Model non-updating SCORED 0.'); blank()
a('SECTION H: IGNORED CRITIQUE AND NON-UPTAKE'); blank()
a('1. Precondition: critique production strongly expected (JPE article; high-profile magnitude; popular coverage, X02).')
a('2. Retrieval: Lin & Luoh (N31, FULL-TEXT version substitute); Oster et al. (N45, FULL-TEXT version substitute); Klasen comments (X03, FULL-TEXT); Das Gupta 2005 and 2006 (N08 METADATA; N46 EXCERPT only).')
a('3. Reception opportunity: verified; the author co-wrote the cohort test N45.')
a(f'4. Uptake in the uptake population: the author engages and accepts the null (ENGAGEMENT I18). Co-citation alone carries no score: Lin & Luoh or Oster et al. 2010 are co-cited by {either(post)}/{len(post)} RECEPTION-1 works published 2009 or later (I20, descriptive). Three inspected post-2010 passages state the HBV effect without the refutation in the passage (N36, N27, R04; I25), so downstream uptake is incomplete.'); blank()
a('57. Serious critiques: Das Gupta 2005 and 2006 (R1, parity patterns); Lin & Luoh 2008 (R2); Oster et al. 2010 (R2); Klasen comments (R4 benchmark); Blumberg (immunity direction, raised via N25).')
a('58. Cited by the dominant cluster: the author\'s own follow-up cites Lin & Luoh (N45).')
a('59. Mode: engaged and accepted (the claim is withdrawn for China).')
a('60. Network update: partial; critiques are hubs inside RECEPTION-1, yet some later citers restate the HBV effect (I25).')
a('61. Recent papers: R03 tests and rejects L1 (BA-E2); R04 restates the 2005 claim (CTX-E25).')
a('62–63. Practitioner warnings: not searched; UNASSESSED.'); blank()
CRH='| Expected-production precondition | Critique / contrary evidence | Year | Source type | Main objection | Verification state | Reception opportunity | Cited by dominant cluster? | Uptake status | Dimension disposition | Effect on consensus |'
def critrows():
    a(CRH); a('|---|---|---|---|---|---|---|---|---|---|---|')
    a(f'| strong | Lin & Luoh, AER (N31, W1994568240) | 2008 | primary empirical | carrier effect near zero in Taiwan births (LL-E1, LL-E2) | FULL-TEXT-CONFIRMED | verified | yes (N45); {cc(ws,LL)}/{n} RECEPTION-1 | engaged and accepted by the author | SCORED 0 | refutation widely co-cited |')
    a('| strong | Oster, Chen, Yu & Lin (N45, W2042478072) | 2010 | primary empirical | 51.06% vs 51.56% male; HBV cannot explain China (OC-E1, OC-E2) | FULL-TEXT-CONFIRMED | verified | author\'s own | the update | SCORED 0 | claim withdrawn for China |')
    a('| strong | Das Gupta, PDR (N08, N46) | 2005, 2006 | primary empirical; reply | birth-order pattern implies sex selection | RECEPTION-CONFIRMED; LOCATED | verified | Oster reply (K4) not retrieved | UNASSESSED | not scored separately | most-cited node in RECEPTION-1 |')
    a('| moderate | Klasen, comments (X03) | 2005 | commentary | benchmark should vary with life expectancy (KL-E1) | FULL-TEXT-CONFIRMED | verified (comments on a draft) | life-expectancy controls in the target (JP-E6) | partly engaged | not scored separately | — |')
critrows(); blank()
a('SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING'); blank()
a('64. Recurring authors: Oster on 3/49 RECEPTION-1 works (I03); Ebenstein (N02, N14, N32), Wei & Zhang (N10, N26) and Li (N07, N43) recur as independent R1 authors.')
a('65–67. Venues, institutions, funding: not re-derived; UNASSESSED.')
a('68. Dissent venues: AER (Lin & Luoh), PDR (Das Gupta), Economics Letters (Oster et al.), a medical journal (R03).')
a('69–70. Gatekeeping and ideology: not assessable.'); blank()
a('Closure type: no author, journal, funding or advocacy closure established; the reception is dominated by son-preference (R1) economics and demography.'); blank()
a('SECTION J: FALSE-POSITIVE AND BASELINE CHECK'); blank()
a('71. Small field: no (the economics and demography of sex ratios is large). 72. Baseline comparison: none built. 73. Adjacent expertise: the source pools medical studies and engages demography (JP-E1, JP-E4). 74. Only people studying the question: no. 75. Strong primary evidence: no; six small studies (JP-E2). 76. Repeated independent tests: yes; large tests with new data are null (I13, I14). 77. Limitations preserved: mostly, with minor certainty and mechanism drift (I10, I11). 78–80. Failed predictions acknowledged, critics engaged, updating: yes, by the author (I18).'); blank()
a('Answers are mostly yes; this is not a cartel signature. The weak point is the paper\'s evidence base, not the network.'); blank()
a('SECTION J2: THE CONCEDE TEST'); blank()
a('| Finding | Declared target claim | Matches map field 6? | Same mechanism as another row? | Count separately? |')
a('|---|---|---|---|---|')
a('| 1 Decisive tests defeat L1 | field 6 via L1 | yes | no | yes |')
a('| 2 Critique taken up; no closure | field 6 network support | yes | no | yes |')
a('| 3 Certainty and mechanism drift | restatements of the target | no — MAP GAP: targets downstream restatements, not map field 6 | no | yes |')
a('| 4 Post-refutation restatement | later use of the target | no — MAP GAP: targets downstream use, not map field 6 | no | yes |')
a('| 5 Record quality | the OpenAlex record of the target | no — MAP GAP: targets the retrieval record, not map field 6 | no | yes |')
a('| 6 Recent reception | field 6 network support | yes | no | yes |'); blank()
a('| Finding | Concede test: SURVIVES / NARROWS / DEFEATS | Surviving claim if NARROWS |')
a('|---|---|---|')
a('| 1 | DEFEATS | — |')
for i in range(2,7): a(f'| {i} | SURVIVES | — |')
blank()
a('| Finding | Scope-loss level | Original claim | Surviving claim | What epistemic or practical work is lost? |')
a('|---|---|---|---|---|')
a('| 1 | near-defeat | about 47% of missing women explained by HBV | none at field 6; the author\'s own test finds no carrier effect | the biological share of missing women |'); blank()
a('Finding 1 DEFEATS field 6. Its failure location is the PAPER (six small pooled studies), not the citation network, which updated.'); blank()
a('SECTION K0: EVIDENCE SUFFICIENCY LEDGER'); blank()
a('Gate B was applied to every inference before any score or finding used it. Inferences that fail stay listed with what would make them sufficient.'); blank()
a('INFERENCE LEDGER'); blank()
a('| Inference | Class | Corpus | Claimed scope | Sampling rule | Members used | Disposition | Statement |')
a('|---|---|---|---|---|---|---|---|')
inspR=', '.join(insp_rec)
INF=[
('I01','GRAPH-STRUCTURE','RECEPTION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED',f'Directed internal density {len(E)}/{den} = {D["dens"]} at work level (50/50 reference lists); no closed cluster inside RECEPTION-1.'),
('I02','GRAPH-STRUCTURE','RECEPTION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED',f'In-degree leaders are critiques or rival studies (N08 {indeg["N08"]}, N31 {indeg["N31"]}, N01 {indeg["N01"]}); Oster-authored works receive {ost_in}/{len(E)} internal edges, {indeg["N45"]} to her null test N45.'),
('I03','DATABASE-RECORD','RECEPTION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED','3/49 works list Oster as author (N12, N24, N45); one work appears as two records (N09/N35); N19 and N44 are implausible citers.'),
('I04','GRAPH-STRUCTURE','RECENT-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED',f'{rc_beyond}/6 recent citers cite an Oster-authored work beyond the target (R03 cites the 2010 null test); Lin & Luoh {rc_LL}/6, Das Gupta 2005 {rc_DG5}/6.'),
('I05','CITATION-USE','RECEPTION-1','CORPUS','PRESPECIFIED-RANDOM',', '.join(sample_ids),'INSUFFICIENT',f'How RECEPTION-1 uses the target cannot be estimated from the random sample: {len(kept)}/12 sampled passages were inspectable (S2 contexts; no other authorized full text retrieved). Sufficient with all 12 passages.'),
('I06','CITATION-USE','RECEPTION-1','WITHIN-SAMPLE','CONVENIENCE',', '.join(kept),'SUPPORTED-WITHIN-SAMPLE','The three inspectable sampled passages: N07 QUALIFIES (notes the Das Gupta challenge), N11 and N27 MENTIONS (HBV listed as a partial factor).'),
('I07','CITATION-USE','RECEPTION-1','WITHIN-SAMPLE','CONVENIENCE',inspR,'SUPPORTED-WITHIN-SAMPLE',f'Among {ni} inspected passages: SUPPORTS {relc.get("SUPPORTS",0)}, CHALLENGES {relc.get("CHALLENGES",0)}, QUALIFIES {relc.get("QUALIFIES",0)}, MENTIONS {relc.get("MENTIONS",0)}; no PREMISE or REUSES.'),
('I08','CITATION-USE','RECENT-1','CORPUS','EXHAUSTIVE','ALL','INSUFFICIENT','How the recent census uses the target: 2/6 passages inspected (R01 implausible citer; R02, R05, R06 no context or text retrieved). Sufficient with all 6 passages.'),
('I09','CITATION-USE','RECENT-1','WITHIN-SAMPLE','CONVENIENCE','R03, R04','SUPPORTED-WITHIN-SAMPLE','R03 restates the target and tests it with new data (null, BA-E2); R04 restates the 2005 claim without the refutation (CTX-E25).'),
('I10','RESTATEMENT','—','NAMED','NOT-APPLICABLE','T01, N13','SUPPORTED','N13 calls the target\'s pooled re-tabulation of earlier studies a confirmation (CTX-E8 vs JP-E2): certainty upgrade.'),
('I11','RESTATEMENT','—','NAMED','NOT-APPLICABLE','T01, N03','SUPPORTED','N03 describes the target as finding more female-biased disease (CTX-E1); the target claims an offspring sex-ratio effect (JP-E2).'),
('I12','RESTATEMENT','—','NAMED','NOT-APPLICABLE','T01, N07, N11, N31, N46, R03, X02','SUPPORTED','Restatements of the magnitude preserve it (JP-E3 vs CTX-E4, CTX-E5, CTX-E15, CTX-E21, BA-E1, SL-E1); none inflates it.'),
('I13','SOURCE-RESULT','—','NAMED','NOT-APPLICABLE','N31, N45, R03','SUPPORTED','Three individual-level tests of L1 are null: Taiwan births (LL-E1), a Chinese cohort with 51.06% vs 51.56% male (OC-E1), Ghana mothers (BA-E2).'),
('I14','DATA-ORIGIN','—','NAMED','NOT-APPLICABLE','N31, N45, R03, T01','SUPPORTED','The three null tests use data independent of the six family studies the target pools (JP-E2): Taiwan registry, Chinese cohort, Ghana hospital records.'),
('I15','COMPOSITION','ADJUDICATION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED','Relevance composition of the evidence base within the locked search (METADATA-coded).'),
('I16','COMPOSITION','ADJUDICATION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED','Contribution composition within the locked search (METADATA-coded).'),
('I17','COMPOSITION','RECEPTION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED','Relevance composition of the citing set; describes citers, not the evidence base.'),
('I18','ENGAGEMENT','—','NAMED','NOT-APPLICABLE','N45','SUPPORTED','The target\'s author tests L1 on a large cohort and concludes HBV cannot explain China\'s male-biased sex ratios (OC-E1, OC-E2), citing Lin & Luoh.'),
('I19','ENGAGEMENT','—','NAMED','NOT-APPLICABLE','T01','SUPPORTED','The target engages R1 (JP-E1), the F2 family studies (JP-E2) and the R4 benchmark debate (JP-E4, JP-E5, JP-E6).'),
('I20','CO-CITATION','RECEPTION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED',f'{either(ws)}/{n} RECEPTION-1 works cite Lin & Luoh 2008 or Oster et al. 2010 ({either(post)}/{len(post)} of those published 2009 or later); Das Gupta 2005 {cc(ws,DG5)}/{n}. Co-citation, not use.'),
('I21','ENGAGEMENT','—','NAMED','NOT-APPLICABLE','—','NOT-ASSESSED','The author\'s uptake of the Das Gupta parity critique. Not assessed: the Oster reply (K4) was not retrieved; sufficient with its full text.'),
('I22','RESTATEMENT','—','NAMED','NOT-APPLICABLE','—','NOT-ASSESSED','Downstream reliance on review hubs (N21 Dyson, N13 James). Not assessed: no hub-citing passage was inspected; sufficient with inspected passages from a defined hub-citing set.'),
('I23','SOURCE-RESULT','—','NAMED','NOT-APPLICABLE','—','NOT-ASSESSED','Results of the other DIRECT (L1) members of ADJUDICATION-1 (A04, A07, A09). Not assessed: no authorized full text retrieved and abstracts not used; sufficient with their full texts.'),
('I24','DATABASE-RECORD','—','NAMED','NOT-APPLICABLE','T01','SUPPORTED','The target OpenAlex record lists 318 referenced works and has a preprint duplicate (W3126094291); only 6 citers since 2021-11-05 against 172 in total.'),
('I25','CITATION-USE','—','NAMED','NOT-APPLICABLE','N36, N27, R04','SUPPORTED','Three passages dated after the 2010 null test state the HBV effect without the refutation in the passage (CTX-E18, CTX-E13, CTX-E25).'),
]
for r in INF: a('| '+' | '.join(r)+' |')
blank()
for iid,col in (('I15','relevance'),('I16','contribution'),('I17','relevance')): a(f'COMPOSITION: {iid} | {col} | {COMP[iid][0]} | TOTAL={COMP[iid][1]}')
blank()
a(f'SAMPLE ATTRITION: I05 {len(kept)}/12'); blank()
a('Sample record: ranks 7, 9, 10, 11, 20, 27, 28, 39, 40, 41, 42, 44 drawn with seed 20261105 (lock/SAMPLES_draw.txt); inspected N07, N11, N27; the N40 context did not show the citation; the other 8 had no context and no authorized full text retrieved.'); blank()
a('Withheld inferences: I05 (INSUFFICIENT: sample attrition), I08 (INSUFFICIENT: 2/6 recent passages), I21, I22 and I23 (NOT-ASSESSED).'); blank()
a('DIMENSION EVIDENCE BASIS'); blank()
a('DIMENSION CLASS MAP: cn7-map-3'); blank()
a('| Scorecard dimension | Scorecard disposition | Inference IDs | Basis note |')
a('|---|---|---|---|')
DIM=[('Founding-cluster dominance','SCORED 0','I02 (-), I03 (-)','critiques draw the most internal edges; Oster works 3/49'),
('Internal citation density','SCORED 0','I01 (-)',f'{D["dens"]} inside RECEPTION-1 only; closure not excluded beyond it'),
('Recent-paper dependence','SCORED 0','I04 (-), I09 (-), I08 (?)','1/6 cite Oster work beyond the target (the null test); recent census 2/6 inspected'),
('Review-hub laundering','UNASSESSED','—','I22 NOT-ASSESSED: no hub-citing passage inspected; sufficient with a defined hub-citing set'),
('Proxy mismatch','UNASSESSED','—','not traced: carrier prevalence as a proxy for an offspring effect is a paper-level construct issue (Stage 2b); no restatement test run'),
('Claim mutation','SCORED 1','I10 (+), I11 (+), I12 (-)','minor certainty upgrade (N13) and mechanism misdescription (N03); magnitude preserved'),
('Adjacent-field neglect','SCORED 0','I19 (-)','source engages R1, F2 and R4 literatures'),
('Lack of decisive tests','SCORED 0','I13 (-), I14 (-), I23 (?)','three independent null tests of L1; other DIRECT (L1) results not read'),
('Poor critique uptake','SCORED 0','I18 (-), I21 (?)','the author tested and accepted the null; Das Gupta uptake not assessed'),
('Intervention-evidence ratchet','N/A','—','no intervention claim at field 6 or in the traced network'),
('Model non-updating','SCORED 0','I18 (-)','four-link gate: links 1–3 met, link 4 not met; the author updated')]
for r in DIM: a('| '+' | '.join(r)+' |')
blank()
a('FINDING EVIDENCE BASIS'); blank()
a('| Finding | Finding status | Inference IDs |')
a('|---|---|---|')
for r in [('Finding 1','confirmed','I13, I14, I18'),('Finding 2','confirmed','I01, I02, I18, I20'),('Finding 3','confirmed','I10, I11, I12'),('Finding 4','provisional','I25, I09'),('Finding 5','confirmed','I24, I03'),('Finding 6','provisional','I04, I09, I08')]: a('| '+' | '.join(r)+' |')
blank()
a('SECTION K: CARTEL-RISK SCORING'); blank()
a('Scores are in Artifact 8. All eight scored dimensions are INDEPENDENT: no two rest on the same passage. Founding-cluster dominance and internal density use the same RECEPTION-1 edge list but answer different questions (in-edge concentration and authorship records vs overall density).'); blank()
a('- Verified risk score: 1/24')
a('- Verified scored-dimension risk rate: 4.2')
a('- Independent scored dimensions: 8')
a('- Nested scored dimensions: 0')
a('- Verified risk denominator: 24')
a('- Evidentiary coverage: 8/10 applicable dimensions scored (80%)')
a('- Execution completeness: 10/10 applicable dimensions completed (100%)')
a('- Dimension inventory: 8 INDEPENDENT SCORED + 0 NESTED SCORED + 0 UNINFORMATIVE + 2 UNASSESSED + 1 N/A = 11 total dimensions; 10 applicable')
a('- Unscored dimensions: Review-hub laundering — UNASSESSED (I22); Proxy mismatch — UNASSESSED (not traced); Intervention-evidence ratchet — N/A (no intervention claim)'); blank()
VS='Verified scored-dimension risk: 4.2%, calculated from 8 independent scored dimensions; 0 additional scored dimensions are NESTED; 8 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.'
a(VS); blank()
a('Formal-label gate: coverage 8/10 (80%) declared. Recent-paper dependence, adjacent-field neglect, lack of decisive tests and poor critique uptake carry open review items, so coverage is 4/10 (40%) if those items are withdrawn: the PROVISIONAL 70% gate (engineering threshold, not validated) is met only if the review items resolve. Label-essential check: the arithmetic position is the healthy/low-risk band, which needs affirmative no-concern evidence on closure-establishing dimensions; review-hub laundering is UNASSESSED and density is affirmative only inside a corpus selected on target citation. The band is withheld.'); blank()
a('ARITHMETIC BAND POSITION: 0%–20% (healthy or low-risk network)')
BAND='WITHHELD — coverage meets the provisional 70% gate only if four review items resolve (40% without them), and the healthy band is label-essential on review-hub laundering (UNASSESSED) and on density beyond a target-selected corpus.'
a('RISK BAND: '+BAND)
MECH='an updating network around a defeated premise: the author and independent teams tested L1 with new data and found no effect; minor downstream certainty and mechanism drift; no closure signature inside RECEPTION-1'
a('MECHANISM LABEL: '+MECH); blank()
a('ARTIFACT 1: TOP 15 CITATION SPINE TABLE'); blank()
a('| Rank | Paper | Year | Citation count | Evidence type | Role in network | Source of citation count |')
a('|---:|---|---:|---:|---|---|---|')
ET={'N05':'review article','N06':'review article','N13':'review article'}
for i,w in enumerate(R[:15],1):
    sid=f'N{i:02d}'; r=bysid[sid]
    au=', '.join(x['author']['display_name'] for x in w['authorships'][:3])+(' et al.' if len(w['authorships'])>3 else '')
    a(f'| {i} | {sid} {au}: {w["display_name"][:70]} ({w["id"][21:]}) | {w["publication_year"]} | {w["cited_by_count"]} | {ET.get(sid,"primary empirical study")} | {r[3]}; {r[4]} | OpenAlex cited_by_count, query 2026-11-05T10:25Z (raw/reception1_top50.json) |')
blank()
a('ARTIFACT 2: FOUNDING CLUSTER TABLE'); blank()
a('| Paper | Year | Claim introduced | Evidence type | Verification state | Later role | Risk |')
a('|---|---|---|---|---|---|---|')
a('| Oster, Hepatitis B and the Case of the Missing Women (T01, W3123222584) | 2005 | HBV explains about 47% of missing women | secondary analysis | FULL-TEXT-CONFIRMED | canonical source; claim later withdrawn for China | high for field 6 (premise defeated), low for network closure |')
a('| Drew et al., hepatitis B virus and sex ratio of offspring (X01) | 1978 | carrier families have more sons | primary empirical study | LOCATED | prior medical source pooled by the target | low |')
a('| Oster, Chen, Yu & Lin (N45) | 2010 | no carrier effect in a Chinese cohort | primary empirical study | FULL-TEXT-CONFIRMED | the author\'s update | none |'); blank()
a('ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE'); blank()
a('"Cites founding cluster?" means an Oster-authored work beyond the target (all cite the target by construction). "Cites adjacent fields?" means Lin & Luoh 2008, Oster et al. 2010 or Das Gupta 2005/2006 in the OpenAlex reference list.'); blank()
a('| Recent paper | Year | Verification state | Cites founding cluster? | Cites hub? | Cites adjacent fields? | New evidence or recycling? |')
a('|---|---:|---|---|---|---|---|')
nev={'R01':'unrelated (implausible citer)','R02':'new evidence on another question (title)','R03':'new evidence: null test of L1 (BA-E2)','R04':'new estimate of missing girls; restates 2005 claim (CTX-E25)','R05':'dissertation; not determined','R06':'dissertation; not determined'}
vs={'R03':'RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED','R04':'RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt)'}
for sid,w,b,adj in recent_rows:
    a(f'| {sid} {w["display_name"][:70]} ({w["id"][21:]}) | {w["publication_year"]} | {vs.get(sid,"RECEPTION-CONFIRMED; LOCATED")} | {"yes ("+", ".join(b)+")" if b else "target only"} | {"Das Gupta 2005" if DG5 in refs(w) else "no"} | {", ".join(adj) if adj else "no"} | {nev[sid]} |')
blank()
a(f'RECENT-1 summary: Oster work beyond target {rc_beyond}/6; Das Gupta 2005 {rc_DG5}/6; Lin & Luoh {rc_LL}/6; Oster et al. 2010 {rc_O10}/6.'); blank()
a('ARTIFACT 4: CITATION POLARITY TABLE'); blank()
a('| Citing paper | Cited paper | Verification state | Citation polarity | Claim use | Inflation risk |')
a('|---|---|---|---|---|---|')
pol={'SUPPORTS':'supportive','CHALLENGES':'critical','QUALIFIES':'qualifying','MENTIONS':'neutral/background'}
for r in rows:
    if r[7]=='INSPECTED':
        st='FULL-TEXT-CONFIRMED' if r[6].startswith('FULL') else 'FULL-TEXT-CONFIRMED (excerpt)'
        risk='moderate' if r[0] in ('N13',) else ('low' if r[0] in ('N03','N36','N27','R04','X02') else 'none')
        cited='Oster 2005 (draft)' if r[0]=='X03' else 'Oster 2005'
        a(f'| {r[1][:70]} | {cited} | {st} | {pol.get(r[4],"neutral/background")} | {r[8][:120].replace("|","/")} | {risk} |')
blank()
a(f'Semantic Scholar contexts were used as EXCERPT access; {S2}.'); blank()
a('ARTIFACT 5: CLAIM MUTATION TABLE'); blank()
a('| Original source | Original claim | Verification state | Hub restatement | Downstream restatement | Mutation severity |')
a('|---|---|---|---|---|---|')
a('| Oster 2005 p. 1201 (JP-E3) | about 47% of missing women; CI 13.5–71.5 | FULL-TEXT-CONFIRMED | none found | N07 "about 70%"; N31 roughly half; SL-E1 conditional 50 million | none |')
a('| Oster 2005 p. 1179 (JP-E2) | pooled re-tabulation of six family studies | FULL-TEXT-CONFIRMED | none found | N13: "the result confirmed by Oster (2005)" | minor |')
a('| Oster 2005 p. 1179 (JP-E2) | carriers have more sons | FULL-TEXT-CONFIRMED | none found | N03: "greater incidence of female-biased diseases" | minor |'); blank()
a('ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE'); blank()
a('Preregistration table as in SECTION E. POST HOC rows anchor no score.'); blank()
negrows(); blank()
a('ARTIFACT 7: CRITIQUE-UPTAKE TABLE'); blank()
critrows(); blank()
a('ARTIFACT 8: CARTEL-RISK SCORECARD'); blank()
a('| Dimension | Applicability | Dimension disposition | Score if SCORED | Evidence / claim state | Evidence supporting disposition and score | Evidence identifiers | Retrieval coverage | AGGREGATION STATUS | Independent evidence and inferential work, or nesting rationale | Reason excluded from denominator | Effect on formal-label gate |')
a('|---|---|---|---|---|---|---|---|---|---|---|---|')
a(f'| Founding-cluster dominance | applicable | SCORED 0 | 0 | RECEPTION-CONFIRMED | critiques lead in-degree; Oster works receive {ost_in}/{len(E)} edges; 3/49 Oster-authored | I02; I03 | 50/50 reference lists | INDEPENDENT | in-edge concentration and authorship | — | counts toward coverage |')
a(f'| Internal citation density | applicable | SCORED 0 | 0 | RECEPTION-CONFIRMED | {len(E)}/{den} = {D["dens"]} | I01 | 50/50 inputs | INDEPENDENT | overall density | — | affirmative inside RECEPTION-1 only |')
a(f'| Recent-paper dependence | applicable | SCORED 0 | 0 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (2 passages) | {rc_beyond}/6 cite Oster work beyond target (the null test); R03 new data | I04; I09; I08 | 6/6 reference lists; 2/6 passages | INDEPENDENT | recent census distinct from RECEPTION-1 | — | counts toward coverage; under review |')
a('| Review-hub laundering | applicable | UNASSESSED | — | — | downstream hub reliance not traced | I22 | 0 hub-citing passages | — | — | UNASSESSED | label-essential for the healthy band; band withheld |')
a('| Proxy mismatch | applicable | UNASSESSED | — | — | not traced in the network | — | — | — | — | UNASSESSED | not label-essential |')
a('| Claim mutation | applicable | SCORED 1 | 1 | FULL-TEXT-CONFIRMED (excerpts) | certainty upgrade (N13) and mechanism misdescription (N03); magnitude preserved | I10; I11; I12 | 24 RECEPTION-1 passages | INDEPENDENT | restatement passages | — | counts toward coverage |')
a('| Adjacent-field neglect | applicable | SCORED 0 | 0 | FULL-TEXT-CONFIRMED | source engages R1, F2, R4 (JP-E1, JP-E2, JP-E4–E6) | I19 | source text | INDEPENDENT | source-layer engagement | — | counts toward coverage; under review |')
a('| Lack of decisive tests | applicable | SCORED 0 | 0 | FULL-TEXT-CONFIRMED | three independent null tests of L1 (LL-E1, OC-E1, BA-E2) | I13; I14; I23 | ADJUDICATION-1 screened by title | INDEPENDENT | named test results on independent data | — | counts toward coverage; under review |')
a('| Poor critique uptake | applicable | SCORED 0 | 0 | FULL-TEXT-CONFIRMED | the author tested and accepted the null (OC-E2) | I18; I21 | N45 full text | INDEPENDENT | engagement in the uptake population | — | counts toward coverage; under review |')
a('| Intervention-evidence ratchet | not applicable | N/A | — | — | no intervention claim | — | — | — | — | N/A: no intervention claim | none |')
a('| Model non-updating | applicable | SCORED 0 | 0 | FULL-TEXT-CONFIRMED | four-link gate: link 4 not met; the author updated | I18 | N45 full text | INDEPENDENT | updating test | — | counts toward coverage |'); blank()
a('Verified risk score 1/24; rate 4.2%; independent 8; nested 0; denominator 24; coverage 8/10 (80%); completeness 10/10 (100%).'); blank()
a(VS); blank()
a('ARTIFACT 9: NETWORK MAP'); blank()
a(f'Receipts as in SECTION A (RECEPTION-1, {n} work nodes, {len(E)} edges, density {len(E)}/{den}, input coverage 50/50, COMPUTED-FROM-RETRIEVED). Closure beyond RECEPTION-1 is not established and not excluded.'); blank()
a('Edge list (CSV, citing,cited):'); blank()
a('```'); a('source,target')
for u,v in E: a(f'{u},{v}')
a('```'); blank()
a('COMPLETION LEDGER'); blank()
a('| Required heading | Exact heading present? | Status: completed / N/A / omitted | Reason or output location |')
a('|---|---|---|---|')
CL=['PRE-AUDIT CLAIM CONFIRMATION','SECTION A0: CORPUS REGISTER AND SOURCE ELIGIBILITY','SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION','SECTION B: EVIDENCE TYPE CODING','SECTION C: CITATION POLARITY AND CLAIM USE','SECTION D: CLAIM MUTATION TRACKING','SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT','SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING','SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR','SECTION H: IGNORED CRITIQUE AND NON-UPTAKE','SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING','SECTION J: FALSE-POSITIVE AND BASELINE CHECK','SECTION J2: THE CONCEDE TEST','SECTION K0: EVIDENCE SUFFICIENCY LEDGER','SECTION K: CARTEL-RISK SCORING','ARTIFACT 1: TOP 15 CITATION SPINE TABLE','ARTIFACT 2: FOUNDING CLUSTER TABLE','ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE','ARTIFACT 4: CITATION POLARITY TABLE','ARTIFACT 5: CLAIM MUTATION TABLE','ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE','ARTIFACT 7: CRITIQUE-UPTAKE TABLE','ARTIFACT 8: CARTEL-RISK SCORECARD','ARTIFACT 9: NETWORK MAP','COMPLETION LEDGER','ARTIFACT 10: FINAL VERDICT','FINAL SECTION: STANDARDIZED FINDING TABLE']
for h in CL: a(f'| `{h}` | yes | completed | this file |')
blank(); a('Gate result: PASS.'); blank()
a('ARTIFACT 10: FINAL VERDICT'); blank()
for x in ['Main founding cluster: the target alone; Oster-authored works are 3/49 of RECEPTION-1 and include her own null test',
 'Main amplification hub: none found; the most-cited nodes inside RECEPTION-1 are critiques (Das Gupta 2005, Lin & Luoh 2008)',
 'Main proxy problem: not traced in the network (UNASSESSED); carrier prevalence standing in for an offspring effect is a paper-level issue',
 'Main adjacent fields neglected: none at the source layer (JP-E1, JP-E2, JP-E4–E6)',
 'Main claim mutation: minor certainty upgrade (N13) and mechanism misdescription (N03)',
 'Most important ignored critique: none ignored by the author; some later citers restate the HBV effect without the refutation (I25)',
 'Decisive test missing: none; three independent null tests of L1 exist (I13, I14). Results of other DIRECT (L1) studies were not read (I23)',
 'Verified risk score: 1/24','Verified scored-dimension risk rate: 4.2','Independent scored dimensions: 8','Nested scored dimensions: 0','Verified risk denominator: 24',
 'Evidentiary coverage: 8/10 (80%)','Execution completeness: 10/10 (100%)','Dimension inventory: 8 INDEPENDENT SCORED + 0 NESTED SCORED + 0 UNINFORMATIVE + 2 UNASSESSED + 1 N/A',
 'Unscored dimensions and reasons: Review-hub laundering UNASSESSED (I22); Proxy mismatch UNASSESSED (not traced); Intervention-evidence ratchet N/A',
 'N-of-M scope statement: '+VS,'Arithmetic band position: 0%–20% (healthy or low-risk network)','Risk band: '+BAND,'Mechanism label: '+MECH,
 'Formal-label gate status: coverage 80% declared; 40% if open review items are withdrawn; MET ONLY IF REVIEW ITEMS RESOLVE (PROVISIONAL threshold); band withheld',
 'Load-bearing finding(s): Finding 1 (decisive tests defeat L1 and so field 6); its failure location is the PAPER',
 'Concede-test result: field 6 DEFEATED by Finding 1; Findings 2–6 SURVIVE',
 'Failure location: PAPER (Finding 1); CITATION (Findings 2, 3, 4, 6); MODEL-RETRIEVAL (Finding 5)',
 'Best formal label: insufficient evidence for a network label (low arithmetic; band withheld); no cartel signature; the network updated',
 f'Confidence level: Low to moderate. CITATION CONTEXT COVERAGE: RECEPTION-1 {cov["RECEPTION-1"][0]}/{cov["RECEPTION-1"][1]}; CITATION CONTEXT COVERAGE: RECENT-1 {cov["RECENT-1"][0]}/{cov["RECENT-1"][1]}; CITATION CONTEXT COVERAGE: ADJUDICATION-1 {cov["ADJUDICATION-1"][0]}/{cov["ADJUDICATION-1"][1]}',
 'What evidence would change this assessment: full texts of the 9 unretrieved sampled RECEPTION-1 members; the Oster reply to Das Gupta; results of A04, A07, A09; inspected passages citing Dyson 2012; a seed-expanded comparison graph',
 'Density inference scope: RECEPTION-1 only (OpenAlex referenced_works:W3123222584, top 50 records, executed 2026-11-05T10:25:08Z); closure is not established and not excluded beyond the defined corpus']:
    a('- '+x)
blank()
a('FINAL SECTION: STANDARDIZED FINDING TABLE'); blank()
F6='HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale\'s (1991) 60.26 million missing women in seven Asian/North-African units, mid-1980s (Table 11, Panel A).'
FIND=[
dict(Finding='Three large individual-level tests on independent data, one co-written by the target\'s author, find no carrier effect, so L1 and with it field 6 fail.',T=F6,M='full texts of N31 (LL-E1, LL-E2), N45 (OC-E1, OC-E2), R03 (BA-E2) against JP-E2 and JP-E3',C='independence and decisiveness of the tests of L1',FM='other: premise defeated by decisive tests',S='fatal-for-strong-claim',CT='DEFEATS',SL='N/A — DEFEATS',E='I13; I14; I18; LL-E1; OC-E1; OC-E2; BA-E2.',ET='primary study',VS='FULL-TEXT-CONFIRMED; CROSS-SOURCE-CONFIRMED',IE='The tests use Taiwan, China and Ghana samples; an effect confined to other populations or carrier types is not excluded.',W='A large test with a carrier effect near 1.5, or evidence that the null tests mismeasure carrier status.',FL='PAPER — six small pooled studies',St='confirmed'),
dict(Finding='Critiques are taken up: the author tested and accepted the null, the critiques are the most-cited nodes inside RECEPTION-1, and no closed cluster exists there.',T=F6,M='RECEPTION-1 edge list (50/50 reference lists); N45 full text',C='closure and critique non-uptake',FM='none — acquittal on closure and uptake',S='none',CT='SURVIVES',SL='N/A — SURVIVES',E='I01; I02; I18; I20; Section A receipts.',ET='author inference',VS='RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED',IE='Not applicable to an acquittal; closure beyond the corpus is not excluded.',W='A wider citing set where the HBV share is used as a premise without the refutation.',FL='CITATION — network structure and uptake',St='confirmed'),
dict(Finding='Two downstream restatements drift: one calls the pooled re-tabulation a confirmation and one misdescribes the mechanism.',T='MAP GAP: this finding targets downstream restatements of the target, not map field 6.',M='S2 citation contexts CTX-E8 and CTX-E1 against JP-E2',C='claim mutation',FM='claim mutation',S='minor',CT='SURVIVES',SL='N/A — SURVIVES',E='I10; I11; I12; CTX-E8; CTX-E1; JP-E2.',ET='author inference',VS='FULL-TEXT-CONFIRMED',IE='Excerpts are short; the surrounding text may qualify the wording.',W='Full texts of N13 and N03 showing the qualification nearby.',FL='CITATION — downstream restatement',St='confirmed'),
dict(Finding='Some passages written after the 2010 null test state the HBV effect without mentioning the refutation.',T='MAP GAP: this finding targets downstream use of the target, not map field 6.',M='S2 citation contexts CTX-E18 (2015), CTX-E13 (2018), CTX-E25 (2025)',C='critique uptake by later citers',FM='critique non-uptake',S='minor',CT='SURVIVES',SL='N/A — SURVIVES',E='I25; I09; CTX-E18; CTX-E13; CTX-E25.',ET='author inference',VS='FULL-TEXT-CONFIRMED (excerpts); PROVISIONAL',IE='The refutation may appear elsewhere in these works.',W='Full texts showing each work cites and accepts the null tests.',FL='CITATION — later citers',St='provisional'),
dict(Finding='The target\'s OpenAlex record is unreliable: 318 referenced works, a preprint duplicate, implausible citers and only 6 recent citers.',T='MAP GAP: this finding targets the retrieval record of the target, not map field 6.',M='raw/target_work.json, raw/target_dupes_search.json, raw/reception1_top50.json, raw/recent1_top25.json',C='database record quality',FM='other: database record quality',S='moderate',CT='SURVIVES',SL='N/A — SURVIVES',E='I24; I03; raw/target_work.json.',ET='author inference',VS='RECEPTION-CONFIRMED',IE='OpenAlex merges and links records automatically; errors are database-wide, not specific to this paper.',W='A second database giving the same citer counts and reference list.',FL='MODEL-RETRIEVAL — database record',St='confirmed'),
dict(Finding='Recent reception is small; one of six recent citers cites an Oster work beyond the target, and it is the null test.',T=F6,M='RECENT-1 reference lists (6/6); 2/6 passages',C='recent-paper dependence',FM='none — provisional acquittal',S='none',CT='SURVIVES',SL='N/A — SURVIVES',E='I04; I09; I08 (INSUFFICIENT).',ET='author inference',VS='RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (2 passages)',IE='Not applicable to an acquittal.',W='A fuller recent citing set from another database showing reliance on the 2005 share.',FL='CITATION — recent reception',St='provisional')]
for i,f in enumerate(FIND,1):
    a(f'Finding {i}'); blank()
    a('| Field | Entry |'); a('|---|---|')
    for k,lab_ in (('Finding','Finding'),('T','Target claim'),('M','What was measured'),('C','What was claimed'),('FM','Failure mode'),('S','Severity'),('CT','Concede test'),('SL','Scope loss if NARROWS'),('E','Evidence'),('ET','Evidence type'),('VS','Verification state'),('IE','Possible innocent explanation'),('W','What would weaken this'),('FL','Failure location'),('St','Status')):
        a(f'| {lab_} | {f[k]} |')
    if i<len(FIND): blank()
import os; os.makedirs('out/citation-network-v2cand3',exist_ok=True)
OUTF='out/citation-network-v2cand3/02c_citation_network_v2cand3.md'
open(OUTF,'w').write('\n'.join(L)+'\n')
print('wrote',OUTF,'lines',len(L))
