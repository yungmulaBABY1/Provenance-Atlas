# Executed by build_2c.py with its namespace. Emits v2cand3/02c_citation_network_v2cand3.md (Baumeister et al. 1998)
L=[]
a=L.append
def blank(): a('')
S2='CTX-E ids resolve to Semantic Scholar citation contexts (requests /graph/v1/paper/DOI:10.1037/0022-3514.74.5.1252/citations?fields=title,year,externalIds,contexts,intents&limit=1000 at offsets 0–5000, 2026-11-05T11:46:57Z–11:47:33Z, HTTP 200; response sha256 offset 0 fa01fc13afde2ebebd3b45e3adb9a7521fbfbb17e35340a854d277b49b31d192, 1000 506bd23a…b869, 2000 aee93a2e…757e, 3000 bbd0daa7…a7ff, 4000 3e809623…2e15, 5000 735212ae…9929; three earlier offset-0 attempts at 11:45:37–11:46:10Z were logged without an HTTP status (rate-limited retries); responses not committed)'
F6='In Experiment 1, participants who ate radishes while resisting chocolate persisted about 8.35 min on unsolvable puzzles vs 18.90 (chocolate) and 20.86 (no food); N ≈ 67; t(44) = 6.03 (d ≈ 1.8) radish vs chocolate.'
TITLE='Baumeister, Bratslavsky, Muraven & Tice (1998), "Ego depletion: Is the active self a limited resource?"'
a('# Citation-Network Audit, v2-candidate.3 run — '+TITLE); blank()
a('INSTRUMENT PREFLIGHT: yungmulaBABY1/Provenance @ a58d165d9a986edca220f8143fc0c0d9316c8a13 : candidates/research-analysis/2-citation-network.v2-candidate.txt | git blob fcbf4e80cfbaf1558784d052d3b8933b594310c7 | sha256 efc1a9fc336c30a67645ac9257701aa2ebe07dcc0be59f8e28523b0800d53064 | 2001 lines | 89337 bytes | markers: version line "2-citation-network v2-candidate.3", map "cn7-map-3" | IDENTITY CONFIRMED (gate checker blob b75a27e7…, sha256 ce6661a5…; v1 checker blob a3da0827…, sha256 f66650fe…)'); blank()
a('INSTRUMENT VERSION: 2-citation-network v2-candidate.3'); blank()
a('DIMENSION CLASS MAP: cn7-map-3'); blank()
a('Run metadata. LIVE RUN of citation-network candidate revision 3 (not a validation run), Batch 2 of the four-paper brief. Target: JPSP 74(5):1252–1265, doi:10.1037/0022-3514.74.5.1252, OpenAlex W2123817056. Executor: Grok Bot (audit run), branch audit/baumeister-ego-depletion from Provenance-Atlas main 6c651d7593abfb5c4b6d2eb9f6846a5212fe001c. Execution date 2026-11-05 UTC (early morning PST). Clock times are UTC with PST (UTC-8) where useful. Mode: full sequence; upstream claim map ../01_claim_extraction.md (this run). Tools: OpenAlex works API with select= lists omitting abstract_inverted_index (corpora, graph, reference lists); Semantic Scholar citation contexts as EXCERPT access; authorized full texts (Hagger et al. 2016 RRR, Maastricht University repository; Vohs et al. 2021, eScholarship, CC BY; Dang et al. 2021, PMC8186735 author manuscript; Carter et al. 2015, author faculty page; Baumeister & Vohs 2016 comment, psychologicalscience.org; Englert & Bertrams 2021, Frontiers). The target body is not available from an authorized source (publisher HTTP 403); the target is held at ABSTRACT level (PubMed 9599441). Recent window: from 2021-11-05. Abstracts other than the target\'s own (Stage 1 source) were not read, coded from, or written to any file.'); blank()
a(f'VALIDATION BOUNDARY. This instrument revision is a candidate. It has not been validated for open retrieval. This run used open retrieval over three registered corpora ({len(members("RECEPTION-1"))} + {len(members("RECENT-1"))} + {len(members("ADJUDICATION-1"))} works). Every percentage, band and label below is an unvalidated open-retrieval application, not a validated verdict.'); blank()
a('EXPOSURE DISCLOSURE. Before this stage the executor had read the target abstract and the Stage 1 secondary sources (author lecture slides, an APA public page, the 2016 RRR, a replicability blog analysis), and the full texts of Vohs et al. 2021, Dang et al. 2021, Carter et al. 2015, Baumeister & Vohs 2016 and Englert & Bertrams 2021 (all retrieved in Stage 1, 11:13–11:16Z). The executor knew from prior reading (declared in 00a) that preregistered multi-site tests report small or null depletion effects and that the founding authors disputed the 2016 RRR. The 00a known-item list was written before the ADJUDICATION-1 search. Stage files 01, 02a and 02b were regenerated at 11:53–11:57Z after a box-restore file loss, i.e. after this stage\'s corpora had been retrieved (run deviation, recorded in 00 and RUN_REPORT); the claim layers and rivals used here are the ones locked in lock/ADJUDICATION-1_search_record.md at 11:28:23Z. The Section E lock was written before the target reference list was inspected and is mechanical: sources are fixed by a ranked query, not chosen.'); blank()
a('PRE-AUDIT CLAIM CONFIRMATION'); blank()
a('- Claim under audit (map field 6): '+F6+' (PROVISIONAL in the map: secondhand numbers.)')
a('- What was literally measured (map field 1): between-condition behavioural differences after different first tasks: persistence on unsolvable figure-tracing after radish/chocolate/no food (Exp 1); persistence after a choice (Exp 2); anagram performance after emotion suppression (Exp 3); passive-option choice after letter crossing (Exp 4). The inner resource is not measured; it is inferred.')
a('- Weaker defensible claim (map field 3): in one lab, about 22 per cell, radish-eaters quit unsolvable puzzles sooner; three further small same-direction contrasts; consistent with but not specific to a shared resource.')
a('- Target layer: field 6 (layer L1 below) for the network verdict; layers L1–L4 and rivals R1–R4 are defined below.'); blank()
a('The map is upstream-generated, not self-generated.'); blank()
a('SECTION A0: CORPUS REGISTER AND SOURCE ELIGIBILITY'); blank()
a('Corpus planning. Questions: (a) how the target is received (RECEPTION-1, RECENT-1); (b) what the evidence base testing the layers and rivals contains (ADJUDICATION-1). Proposed inferences were tested in SECTION K0 before use; those that fail stay there as INSUFFICIENT or NOT-ASSESSED.'); blank()
a('CLAIM LAYERS AND RIVALS'); blank()
a('CLAIM LAYER: L1 — Original depletion effect (map field 6): resisting chocolate and eating radishes causes much faster quitting on unsolvable puzzles (d about 1.8–2.0), replicable in that paradigm.')
a('CLAIM LAYER: L2 — General sequential-task effect: an initial act of self-control reliably reduces subsequent self-control (nonzero, at least small-to-moderate).')
a('CLAIM LAYER: L3 — Mechanism: self-control draws on a limited common resource (later specified as glucose).')
a('CLAIM LAYER: L4 — Interpretive/applied: willpower works like a muscle; decision fatigue and everyday self-control failures follow from depletion.')
a('RIVAL: R1 — Null or inflated effect (small samples, selective publication).')
a('RIVAL: R2 — Motivation/attention shift (process model; opportunity cost); no resource consumed.')
a('RIVAL: R3 — Beliefs/expectancy (lay theories of willpower; demand).')
a('RIVAL: R4 — Task-specific confounds (affect, frustration, hunger, non-blind experimenter delivery).'); blank()
a('CORPUS REGISTER'); blank()
a('CORPUS ID: RECEPTION-1')
a('CORPUS ROLE: RECEPTION')
a('CORPUS QUESTION: How the most-cited works citing the target relate to it and to each other.')
a('CORPUS SELECTION RULE: OpenAlex works API, /works?filter=cites:W2123817056&sort=cited_by_count:desc&per-page=50, page 1, executed 2026-11-05T11:31:57Z (3:31:57 AM PST); population 5359; no date or type bounds; no screening; one row per work; response raw/reception1_top50.json sha256 dc54ce7c6ef2fb6440b0a4bf9ac0b54acd48cc57b823c8f6c0160cd602916a25.')
a('CORPUS DISCOVERY: SEARCHED — ranked citation query (top 50 by cited_by_count); request, execution time and response hash recorded above')
a('SELECTED ON TARGET CITATION: YES')
a(f'CORPUS SIZE: {len(members("RECEPTION-1"))}')
a(f'CITATION CONTEXT COVERAGE: RECEPTION-1 {cov["RECEPTION-1"][0]}/{cov["RECEPTION-1"][1]}')
a('RECORD QUALITY: the corpus is dominated by highly cited works from other fields (emotion regulation, conservation of resources, personality economics, ABCD imaging protocol) that cite the target in passing; no duplicate records found; OpenAlex reference lists were present for all 50. A stray file raw/reception_exec_time.txt reads 11:46:38Z; the retrieval log (11:31:57Z) and the response hash govern.')
a('CORPUS LOCK: 2026-11-05T11:31:57Z; response sha256 dc54ce7c6ef2fb6440b0a4bf9ac0b54acd48cc57b823c8f6c0160cd602916a25'); blank()
a('CORPUS ID: RECENT-1')
a('CORPUS ROLE: RECEPTION')
a('CORPUS QUESTION: How recent (2021-11-05 onward) citing works use the target.')
a('CORPUS SELECTION RULE: OpenAlex works API, /works?filter=cites:W2123817056,from_publication_date:2021-11-05&sort=cited_by_count:desc&per-page=25, executed 2026-11-05T11:32:05Z; population 1530; the top 25 form the corpus and all 25 were to be inspected (census of the corpus, lock/SAMPLES_draw.txt). Response raw/recent1_top25.json sha256 7101107597f4ebf092df16ef755aca5e216fe786ea4efa52c664a7e38cec6c60.')
a('CORPUS DISCOVERY: SEARCHED — ranked citation query; request, execution time and response hash recorded above')
a('SELECTED ON TARGET CITATION: YES')
a(f'CORPUS SIZE: {len(members("RECENT-1"))}')
a(f'CITATION CONTEXT COVERAGE: RECENT-1 {cov["RECENT-1"][0]}/{cov["RECENT-1"][1]}')
a('RECORD QUALITY: ranked by cited_by_count, so the corpus over-represents organisational behaviour and consumer-research reviews; R05 (Baumeister et al. 2024 status review) is also an ADJUDICATION-1 member; the remaining 1505 recent citers are outside the corpus.')
a('CORPUS LOCK: 2026-11-05T11:32:05Z; response sha256 7101107597f4ebf092df16ef755aca5e216fe786ea4efa52c664a7e38cec6c60'); blank()
a('CORPUS ID: ADJUDICATION-1')
a('CORPUS ROLE: ADJUDICATION')
a('CORPUS QUESTION: What tests of claim layers L1–L4 and rivals R1–R4 exist, whether or not they cite the target, and what they find.')
a('CORPUS SELECTION RULE: OpenAlex works API, seven title_and_abstract.search queries Q1–Q7 (exact strings, date bounds 1998-01-01 to 2026-11-05 and types article|preprint|book-chapter|review in lock/ADJUDICATION-1_search_record.md), relevance ranking, top 10 per query, select= without abstract_inverted_index; one row per work; screening from title and record metadata (and full texts already retrieved from authorized sources) only, abstracts not used; codes DIRECT (L1)/(L2)/(L3)/(L4)/(R1)/(R2)/(R3)/(R4), ADJACENT, BACKGROUND, UNRELATED, UNKNOWN.')
a('CORPUS DISCOVERY: SEARCHED — lock/ADJUDICATION-1_search_record.md (raw/adj1_Q1..Q7.json, executed 2026-11-05T11:28:49Z–11:31:39Z; Q6 and Q7 after HTTP 429 retries)')
a('SELECTED ON TARGET CITATION: NO')
a(f'CORPUS SIZE: {len(members("ADJUDICATION-1"))}')
a(f'CITATION CONTEXT COVERAGE: ADJUDICATION-1 {cov["ADJUDICATION-1"][0]}/{cov["ADJUDICATION-1"][1]}')
a('RECORD QUALITY: Vohs et al. 2021 returned as the published record and a preprint record (row A03); the Stroop multilab replication as a 2018 record and a 2024 record (row A05); Dang et al. 2021 carries publication year 2020 in OpenAlex; Dang 2017 meta-analysis is listed in 00a as "Dang 2018" (00a governs the label, OpenAlex the year); Q7 returned no decision-fatigue-specific work; three records share the title "The Strength Model of Self-Control" (N09, 2007, Baumeister, Vohs & Tice; A48, 2013, a Chinese-language review; A50, 2021, a chapter); they are distinct works by year, venue and authorship and are kept as separate rows; relevance codes are METADATA-coded from titles.')
a('CORPUS LOCK: 2026-11-05T11:28:23Z (3:28:23 AM PST); search record sha256 d1e398eacd9045935a0a110659281f7c44970e6d9d4e46ff44d1b5fef938d7f7')
a('KNOWN-ITEM RECALL: ADJUDICATION-1 8/12 (returned: K1 Hagger et al. 2010 [N16], K2 Carter & McCullough 2014 [A09], K4 Hagger et al. 2016 RRR [N45], K5 Vohs et al. 2021 [A03], K6 Dang et al. 2021 [A01], K7 Dang meta-analysis [A08], K9 Job, Dweck & Walton 2010 [A32], K10 Inzlicht & Schmeichel 2012 [N47]; not returned: K3 Carter et al. 2015, K8 Gailliot et al. 2007, K11 Baumeister & Vohs 2016, K12 Kurzban 2010). K3 and K11 enter only as POST HOC rows X16 and X17; K8 is RECEPTION-1 member N41 and enters adjudication only as POST HOC; K12 was not retrieved.'); blank()
a('Overlap. N09, N16, N33, N45 and N47 are in RECEPTION-1 and ADJUDICATION-1, and R05 is in RECENT-1 and ADJUDICATION-1; each is recorded once with both corpus IDs. Reception rank does not weight the adjudication role. Duplicate records of one work are merged into one row with every identifier listed (A03, A05). Rows T01 and X01–X20 are OUTSIDE every registered corpus (the target, Section E locked sources and named POST HOC sources); they carry no corpus count.'); blank()
a('SOURCE ELIGIBILITY LEDGER'); blank()
a('| Source | Corpus membership | Question relevance | Relation to target | Evidence contribution | Source access | Citation context | Supported inference |')
a('|---|---|---|---|---|---|---|---|')
for r in rows:
    a('| '+' | '.join(x.replace('|','/') for x in r[1:])+' |')
blank()
a(f'Coding notes. {S2}. Relation for ADJUDICATION-1 non-reception members: OpenAlex reference list contains W2123817056 → CITES-UNINSPECTED; reference list empty or sparse → UNKNOWN; non-empty list without the target → NOT-CITING (NOT-APPLICABLE). Relevance and contribution for METADATA rows are coded from the title only (abstracts were not used under the rights rules). TA-E1 resolves to the target abstract (PubMed 9599441). RRR-E, VO-E, DA-E, CA-E, BV-E and EN-E ids resolve to the pages or sections given in each row. SC-E1, LS-E1 and AP-E1 resolve to Stage 1 sources S2, D1/D1b and D2/D2b as located in ../01_claim_extraction.md.'); blank()
a('SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION'); blank()
a('GRAPH CORPUS AND RECEIPTS'); blank()
a(f'GRAPH CORPUS DEFINITION: RECEPTION-1 as registered in SECTION A0 (OpenAlex, filter=cites:W2123817056, sort=cited_by_count:desc, top 50 records, executed 2026-11-05T11:31:57Z, no date or type bounds, no screening). Nodes are works, n = {n}. The target is outside the density corpus; citer -> target edges hold by construction and are not counted.')
a(f'GRAPH CORPUS NODE LIST: {nodelist}')
a(f'INTERNAL EDGE LIST: {edgelist}')
a('DERIVATION MODE: COMPUTED-FROM-RETRIEVED')
a(f'DENSITY CALCULATION: directed density = directed internal edges u -> v (u, v work nodes, u != v, v in OpenAlex referenced_works of u) / n(n-1), n = {n}; computed by scripts/build_2c.py from raw/reception1_top50.json (cross-check raw/graph_edges.json).')
a(f'DENSITY NUMERATOR: {len(E)} directed internal edges among the {n} work nodes.')
a(f'DENSITY DENOMINATOR: {den} possible directed edges ({n} × {n-1}).')
a(f'DENSITY INPUT COVERAGE: 50/50 record reference lists obtained from OpenAlex ({refs_total:,} indexed references across the {n} works). No Crossref cross-check.')
a('DENSITY INFERENCE SCOPE: the density result applies only to RECEPTION-1. Because RECEPTION-1 is selected on target citation, it can establish density inside that target-citing corpus; it cannot establish or exclude field-wide, founding-cluster or premise-subnetwork closure. No seed-expanded or matched comparison graph was built.'); blank()
a('Closure is not established and not excluded beyond the defined corpus.'); blank()
a(f'Density results. Work-level directed density {len(E)}/{den} = {dens}. {citing}/{n} works cite at least one other member. Reciprocal pairs: {recip}. In-degree leaders: {lead}. Founding-cluster works (any of the four target authors on the byline: {", ".join(FC)}; {len(FC)}/{n}) receive {fc_in}/{len(E)} internal edges, {nonfc_to_fc} of them from works outside the founding cluster.'); blank()
a('1. Top 50 most-cited works citing the target: RECEPTION-1 (Artifact 1 lists the top 15). Relevance composition: '+COMP['I17'][0]+'.')
a(f'2. Founding cluster: the four target authors (Baumeister, Bratslavsky, Muraven, Tice) and works they co-author. In RECEPTION-1: {", ".join(FC)}. The founding authors also co-author ADJUDICATION-1 members A03 (Vohs et al. 2021, Muraven on the byline), A22, A45, A47 and R05.')
a('3. Founding papers\' evidence type: the target reports four small single-lab experiments (map field 1; ABSTRACT-level, TA-E1); founding-cluster follow-ups in RECEPTION-1 are primary studies (N19, N36, N41) and reviews (N06, N09, N26, N33).')
a(f'4. Hubs: N19 Muraven, Tice & Baumeister 1998 (in-degree {indeg["N19"]}) and N06 Muraven & Baumeister 2000 review ({indeg["N06"]}) lead; both are founding-cluster works. N41 Gailliot et al. 2007 ({indeg["N41"]}, founding cluster) and N01 Gross 1998 ({indeg["N01"]}, emotion regulation) follow.')
a(f'5. Hub substitution: within RECEPTION-1, {rec_N19}/{n} works cite N19 and {rec_N06}/{n} cite N06 alongside the target (co-citation, not use).')
a(f'6. Small cluster citing itself: founding-cluster works cite each other ({fc_out} internal edges among them); the corpus overall is sparse (density {dens}).')
a('7. Gatekeeping roles: no editorial or referee data retrieved; UNASSESSED.')
a('8. Self-citation in the founding cluster: present (founding-cluster members of RECEPTION-1 cite the target by construction); its rate relative to field norms was not measured.')
a('9. Concentration by lab/journal/funder: authorship only (SECTION I).')
a('10. Citation count vs independent confirmation: target cited_by_count 5374 at retrieval; DA-E1 reports "cited over 5,000 times". The preregistered multi-site tests of L2 with new data report d = 0.04 (RRR-E2), 0.06 (VO-E2) and 0.10 (DA-E2) (I13, I14); no direct test of L1 was found in ADJUDICATION-1 (I18).'); blank()
a('SECTION B: EVIDENCE TYPE CODING'); blank()
a('Every corpus member is coded in the SOURCE ELIGIBILITY LEDGER. Questions 11–16 describe the evidence base only on ADJUDICATION-1, the SEARCHED adjudication corpus; on RECEPTION-1 they describe the citing set.'); blank()
a('ADJUDICATION-1 composition (evidence base, bounded by the locked search; METADATA-coded):')
for iid,col in (('I15','relevance'),('I16','contribution')): a(f'COMPOSITION: {iid} | {col} | {COMP[iid][0]} | TOTAL={COMP[iid][1]}')
a('RECEPTION-1 composition (citing set only):')
a(f'COMPOSITION: I17 | relevance | {COMP["I17"][0]} | TOTAL={COMP["I17"][1]}'); blank()
dsum='; '.join(f'{k} {v}' for k,v in sorted(dirs.items()))
a(f'11. Primary empirical tests in ADJUDICATION-1: DIRECT codes {dsum}. DIRECT (L1): {len(dl1)} — no member tests the food-temptation → persistence paradigm itself (I18). The RRR chose another first task, citing "extensive experimenter involvement" in the original (RRR-E1, p. 548).')
a('12. Reviews/syntheses: REVIEW and COMMENTARY members are counted in I16; of the bias-corrected syntheses only Carter et al. 2015 (X16, POST HOC) was read in full.')
a('13. Theory-only: THEORY members are counted in I16 (for example A44, A51, A52).')
a('14. Unknown: relevance or relation UNKNOWN where OpenAlex reference lists are empty (A05, A07, A12, A17, A50).')
a('15. Evidence-to-claim ratio: field 6 rests on one single-lab experiment of about 67 participants; the large later tests of L2 (23-lab RRR, multi-site Vohs et al. 2021, 12-lab Dang et al. 2021) use new data under preregistered protocols (I14).')
a(f'16. On RECEPTION-1 the same questions describe citers: {COMP["I17"][0]} (of {COMP["I17"][1]}).'); blank()
a('SECTION C: CITATION POLARITY AND CLAIM USE'); blank()
ni=cov['RECEPTION-1'][0]; nr=cov['RECENT-1'][0]
a(f'Citing passages inspected: CITATION CONTEXT COVERAGE: RECEPTION-1 {cov["RECEPTION-1"][0]}/{cov["RECEPTION-1"][1]} ({", ".join(insp_rec)}); CITATION CONTEXT COVERAGE: RECENT-1 {cov["RECENT-1"][0]}/{cov["RECENT-1"][1]} ({", ".join(insp_rcn)}); CITATION CONTEXT COVERAGE: ADJUDICATION-1 {cov["ADJUDICATION-1"][0]}/{cov["ADJUDICATION-1"][1]}. Most passages are EXCERPT (Semantic Scholar contexts). The prespecified random sample of 12 lost {12-len(kept)} members (I05). Percentages use inspected passages only.'); blank()
sup=[r[0] for r in members('RECEPTION-1') if r[4]=='SUPPORTS']
a(f'17. Supportive: SUPPORTS {relc.get("SUPPORTS",0)}/{ni} in RECEPTION-1 ({", ".join(sup)}).')
a(f'18. Critical: CHALLENGES {relc.get("CHALLENGES",0)}/{ni} (N45 RRR); QUALIFIES {relc.get("QUALIFIES",0)}/{ni} (N27: true choice "was not depleting", CTX-E13).')
a(f'19. Perfunctory/background: MENTIONS {relc.get("MENTIONS",0)}/{ni}. RECENT-1: PREMISE {relr.get("PREMISE",0)}/{nr}, MENTIONS {relr.get("MENTIONS",0)}/{nr}, QUALIFIES {relr.get("QUALIFIES",0)}/{nr} (R16 excludes ego-depletion studies, CTX-E28).')
a(f'20. Premise use: RECEPTION-1 {", ".join(prem_n)} and RECENT-1 {", ".join(prem_r)} use the limited-resource model as a premise for their own argument (for example CTX-E4, CTX-E25, CTX-E27, CTX-E30).')
a('21. Data/instrument reuse: the target\'s e-crossing manipulation is reused as a depletion task (A27 CTX-E39, A32 CTX-E40, A06 EN-E1); R02 reuses choice time as a proxy (CTX-E23).')
a('22. Polarity inflation: several passages state a drained resource as what the target showed (CTX-E2, CTX-E5, CTX-E19, CTX-E22, CTX-E27), while the target abstract states the resource as an inference (TA-E1, "suggest"). A08 states that "over 300 independent studies have replicated this effect" (CTX-E34). Graded under proxy mismatch (I10, I11); the restatement comparison against the target text is INSUFFICIENT (I12).'); blank()
a('SECTION D: CLAIM MUTATION TRACKING'); blank()
a('23–30. Original: the target is held at ABSTRACT level only (TA-E1); its body, where field 6\'s numbers sit, was not read (publisher HTTP 403; no authorized copy). The RESTATEMENT class needs FULL-TEXT or EXCERPT access to both texts, so no mutation is graded. Candidate restatements recorded for review: hedge loss from "suggest" (TA-E1) to "Willpower is limited" (X19, founding-author slides) and "drained the subjects\' self-control" (X20); A08 "over 300 independent studies have replicated" (CTX-E34); R01 attributes "displaced behavior theory" to Baumeister (CTX-E22); N13 restates Experiment 1 faithfully (CTX-E6). Claim mutation is UNASSESSED (I12 INSUFFICIENT).'); blank()
a('| Original source | Original claim | Hub restatement | Downstream restatement | Mutation severity | Note |')
a('|---|---|---|---|---|---|')
a('| Target abstract (TA-E1) | results "suggest" a limited capacity for volition | N33: "appears to depend on a limited resource" (CTX-E15) | X19 slides "Willpower is limited"; X20 "drained the subjects\' self-control" | not graded | target body not read; RESTATEMENT minimum unmet |')
a('| Target Experiment 1 (field 6, PROVISIONAL) | radish eaters quit sooner, one lab | none found | N13 faithful (CTX-E6); A22 faithful (CTX-E38) | not graded | as above |')
a('| Target and follow-ups | depletion effect first reported | none found | A08 "over 300 independent studies have replicated this effect" (CTX-E34) | not graded | compare RRR-E2, VO-E2, CA-E2 |')
a('| Target | ego depletion / limited resource | none found | R01 "displaced behavior theory" attributed to Baumeister (CTX-E22) | not graded | possible misattribution |'); blank()
a('SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT'); blank()
a('Steps 31–37. Layers L1–L4 and rivals R1–R4 are locked in lock/ADJUDICATION-1_search_record.md; fields F1–F5 and observations O1–O5 in lock/section_E_preregistration.md, hashed before the Section E queries ran. The lock was written before the target reference list was inspected; the executor\'s prior knowledge is declared in 00a. Sources are fixed mechanically by a ranked query.'); blank()
a('SOURCE-LOCK METHOD: LOCKED QUERY')
a('SOURCE-LOCK DATABASE: OpenAlex works API (select omits abstract_inverted_index)')
a('SOURCE-LOCK QUERY OR SOURCE LIST: filter=title.search:<terms>,to_publication_date:1998-04-30,type:article, sort=cited_by_count:desc, per-page=3; terms F1 "mental fatigue", F2 "learned helplessness", F3 "mood persistence", F4 "experimenter expectancy", F5 "mental effort"')
a('SOURCE-LOCK DATE CUTOFF: 1998-04-30 (before the JPSP May 1998 issue)')
a('SOURCE-LOCK RANKING RULE: OpenAlex cited_by_count descending at query time')
a('SOURCE-LOCK N: 15 (top 3 per field × 5 fields)')
a('SOURCE-LOCK DEDUPLICATION RULE: by OpenAlex work ID; off-topic items retained and flagged, never replaced')
a('SOURCE-LOCK TIMESTAMP OR HASH: 2026-11-05T11:28:40Z (3:28:40 AM PST); preregistration sha256 791e03ac0bbe7ff3abe4e806ce0d17b57c1bc3e55d7816afe5d5c86ea6bed737; queries executed after the lock (F1–F5 11:45:13Z–11:46:48Z; F2 retrieved twice, the retained response sha256 a0bba566a2f0a91c2500… is the one on disk)'); blank()
a('Flip test (step 37): PASS. F1 is generated from rival R2; F3 and F4 from R4; F2 from both L1 and R4; F5 from L3 (the audited claim). Innocent explanations: F3 exemplars include an off-topic breast-feeding paper (X07); F5 exemplars include an off-topic motor-imagery paper (X15).'); blank()
a(f'Engagement check. The target body is not accessible, so engagement is checked against the target\'s OpenAlex reference list (58 IDs; 57 resolved, raw/target_reflist_titles.json, retrieved 12:05:02Z after the lock, METADATA). It contains {sec_cited}/15 locked sources. It does list adjacent works outside the lock: stress aftereffects (Glass & Singer 1969; Cohen 1980), persistence (Feather 1961; McFarlin 1985), mood (Mayer & Gaschke 1988), self-reported effort (Johnson & Saccuzzo 1995), thought suppression, reactance and dissonance works. It lists no learned-helplessness (F2) or experimenter-expectancy (F4) work.'); blank()
a('Falsification-relevant literature preregistration table:'); blank()
a('| Claim layer | Audited explanation | Strongest plausible rival explanation | Adjudicating observation | Candidate field | Generated from audited claim, rival, or both? | Measurement relevance | Adjudicative capacity | Independence | Publication-date cutoff | Historically available? | Flip-test result | Source-lock method | Lock timestamp / hash | Final engagement classification |')
a('|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|')
a('| L1/L3 | a limited resource is spent | R2 motivation/attention shift | O1 incentives remove post-effort decrements | F1 mental fatigue | rival | outcome-task performance after effort | could narrow L3 | independent | 1998-04-30 | yes | PASS | LOCKED QUERY | 791e03ac…d737 | no locked source cited; related stress-aftereffect works cited (reference list only; text UNASSESSED) |')
a('| L1 | depletion shortens persistence | R4 aversive/uncontrollable experience shortens persistence | O2 persistence on unsolvable tasks after uncontrollable failure | F2 learned helplessness | both | the same outcome (unsolvable-task persistence) | could defeat L1\'s specificity | independent | 1998-04-30 | yes | PASS | LOCKED QUERY | as above | not cited; no learned-helplessness work in the reference list; text engagement UNASSESSED |')
a('| L1 | resource, not affect | R4 affect | O3 induced mood changes persistence | F3 mood and persistence | rival | same outcome | could narrow L1 | independent | 1998-04-30 | yes | PASS | LOCKED QUERY | as above | no locked source cited; Mayer & Gaschke 1988 mood work cited (reference list only) |')
a('| L1 | manipulation drives behaviour | R4 non-blind experimenter delivery | O4 non-blind experimenters shift timed outcomes | F4 experimenter expectancy | rival | experimenter-delivered manipulation | could narrow L1 | independent | 1998-04-30 | yes | PASS | LOCKED QUERY | as above | not cited; no expectancy work in the reference list; text engagement UNASSESSED |')
a('| L3 | one limited general capacity | capacity is task-specific | O5 a general capacity depleted by effort | F5 mental effort | audited claim | construct definition | could narrow L3 | independent | 1998-04-30 | yes | PASS | LOCKED QUERY | as above | no locked source cited; self-reported effort work cited (reference list only) |'); blank()
cls={'F1':'MECHANISM-SUPPORTING','F2':'DIRECTLY-ADJUDICATING','F3':'MECHANISM-SUPPORTING','F4':'MECHANISM-SUPPORTING','F5':'CONSTRUCT-DEFINING'}
fld={'F1':('L1/L3','F1 mental fatigue'),'F2':('L1','F2 learned helplessness'),'F3':('L1','F3 mood and persistence'),'F4':('L1','F4 experimenter expectancy'),'F5':('L3','F5 mental effort')}
fof={f'X{i:02d}':f'F{(i-1)//3+1}' for i in range(1,16)}
NEGH='| Claim layer | Adjacent field | Nominated source and stable identifier | Verification state | Source class: CONSTRUCT-DEFINING / MECHANISM-SUPPORTING / DIRECTLY-ADJUDICATING | Actual result | Explanation favored | Explanation weakened | Precise revision required | Pre-inspection lock status or POST HOC | Cited by dominant cluster? | Engagement quality | Effect of omission |'
def negrows():
    a(NEGH); a('|---|---|---|---|---|---|---|---|---|---|---|---|---|')
    for i in range(1,16):
        sid=f'X{i:02d}'; r=bysid[sid]; f=fof[sid]; lay,fn=fld[f]; wid_=r[1].split()[1]
        t=' '.join(r[1].split()[2:])[:60].replace('|','/')
        off=r[3]=='UNRELATED'
        eff='none (off-topic exemplar)' if off else ('rival not addressed at reference-list level' if f in ('F2','F4') else 'minor context loss')
        nd='not determined: results not read (METADATA only)'
        a(f'| {lay} | {fn} | {sid} {wid_} {t} | LOCATED | {cls[f]} | {"off-topic (title)" if off else "title only; results not read"} | {nd} | {nd} | {nd} | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | {eff} |')
a('Adjacent-literature neglect table:'); blank()
negrows()
a('| L2 | R1 test | N45 W2499154041 Hagger et al. 2016 RRR | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | pooled d = 0.04 across 23 labs (RRR-E2) | R1 | L2 | L2 effect near zero for the RRR paradigm | LOCKED (ADJUDICATION-1 search) | founding authors replied (X17) | disputed by founding authors (BV-E1) | not omitted |')
a('| L2 | R1 test | A03 W3119325546 Vohs et al. 2021 | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | d = 0.06, 95% CI [−0.02, 0.14] (VO-E2) | R1 | L2 | depletion "not as reliable or robust as previously assumed" (VO-E3) | LOCKED (ADJUDICATION-1 search) | founding-cluster co-authored (Muraven) | the update itself | not omitted |')
a('| L2 | R1 test | X16 Carter et al. 2015 | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | PET and PEESE estimates indistinguishable from zero (CA-E2) | R1 | L2 | bias-corrected effect not distinguishable from zero | POST HOC (known item K3, not returned by the locked search) | not determined | — | not omitted |'); blank()
a('At the reference-list level the target engages stress-aftereffect, persistence and mood work but no learned-helplessness or experimenter-expectancy source, although F2 shares the outcome (persistence on unsolvable tasks) and F4 addresses the experimenter involvement the RRR cites (RRR-E1). Whether the text addresses these rivals is UNASSESSED (I22). GRAPH-STRUCTURE I21 carries the score; the multi-site R1 tests post-date the target and are scored under decisive tests and critique uptake.'); blank()
a('SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING'); blank()
a(f'40. Hubs inside RECEPTION-1: N19 Muraven, Tice & Baumeister 1998 (in-degree {indeg["N19"]}), N06 Muraven & Baumeister 2000 review ({indeg["N06"]}), N41 Gailliot et al. 2007 glucose study ({indeg["N41"]}), N01 Gross 1998 emotion-regulation review ({indeg["N01"]}), N16 Hagger et al. 2010 meta-analysis ({indeg["N16"]}). Review-type founding-cluster works: N06, N09, N26, N33.')
a(f'41. Recent papers citing the hubs (RECENT-1, 25): N09 {rc_hub["N09"]}/25, N06 {rc_hub["N06"]}/25, N16 {rc_hub["N16"]}/25, N19 {rc_hub["N19"]}/25.')
a('42. Recent papers citing primary evidence directly: 25/25 cite the target by construction.')
a('43. Hub substitution for inspection: not measurable from reference lists; no passage citing a hub in place of the target was inspected (I26 NOT-ASSESSED).')
a('44–45. Hub accuracy: N06 states the food-temptation test was run "to help rule out moods" (CTX-E3); N33 hedges ("appears to depend", CTX-E15); N16 says the target "provided initial support" (CTX-E8). These are founding-cluster or synthesis restatements; RESTATEMENT comparison against the target body is not possible (ABSTRACT only).')
a('46. Adjacent literatures in hubs: N01 is emotion regulation; N16 is a meta-analysis later reanalysed for publication bias (A09, X16).')
a('47. Hub as substitute for primary evidence: UNASSESSED (I26).'); blank()
a('| Hub paper | Recent papers citing hub | Recent papers citing primary evidence directly | Adjacent-field citation rate | Hub accuracy | Hub risk |')
a('|---|---|---|---|---|---|')
a(f'| Muraven, Tice & Baumeister 1998 (N19) | {rc_hub["N19"]}/25 RECENT-1 | 25/25 by construction | {rec_N19}/{n} RECEPTION-1 co-cite | not inspected | founding-cluster hub; UNASSESSED |')
a(f'| Muraven & Baumeister 2000 (N06) | {rc_hub["N06"]}/25 RECENT-1 | 25/25 by construction | {rec_N06}/{n} RECEPTION-1 co-cite | mood rule-out claim (CTX-E3); not graded | founding-cluster hub; UNASSESSED |')
a(f'| Baumeister, Vohs & Tice 2007 (N09) | {rc_hub["N09"]}/25 RECENT-1 | 25/25 by construction | — | not inspected | UNASSESSED |')
a(f'| Hagger et al. 2010 (N16) | {rc_hub["N16"]}/25 RECENT-1 | 25/25 by construction | — | "provided initial support" (CTX-E8); bias-corrected reanalyses disagree (CA-E2) | UNASSESSED |'); blank()
a('SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR'); blank()
a('48. Proxy treated as construct: persistence and performance differences stand in for a depleted inner resource; several later passages state the resource as what was shown (CTX-E19, CTX-E22, CTX-E27), where the target abstract says the results "suggest" it (TA-E1). Graded under proxy mismatch (I10, I11).')
a('49. Export from low-stakes settings: laboratory persistence in about 67 students is exported to workplace, consumer and health settings (R07, R13, R17, R18, N43; L4); applied claims are a paper-level and Stage 2b issue.')
a('50. Ignored natural experiments: not assessed.')
a('51. Model updating: mixed. A 2021 multi-site test co-authored by Muraven concludes depletion is "not as reliable or robust as previously assumed" (VO-E3); the founding authors\' 2016 comment says the RRR "did not test ego depletion" (BV-E1); the 2024 status review (R05) was not read.')
a('52. Intervention expansion: no intervention claim at field 6; N/A.')
a('53–55. Falsification criteria: not stated in the target abstract; 55 N/A.')
a('56. Expansion over testing: L4 applications grew while the L1 paradigm was not re-tested at scale (I18; Section E; recent premise use I09).'); blank()
a('Ratchet scoring route. Intervention-evidence ratchet: N/A (no intervention claim). Model non-updating four-link gate: link 1 (model stated: a limited resource, TA-E1) met; link 2 (verified later disconfirming evidence) met for L2, RRR-E2, VO-E2, DA-E2, CA-E2 (I13, I14); link 3 (reception opportunity) met, founding authors replied to the RRR (X17) and Muraven co-authored A03; link 4 (non-updating) NOT DETERMINABLE: the founding cluster both disputes (BV-E1, 2016) and co-signs a downgrade (VO-E3, 2021), and its latest position (R05, 2024) was not read (I24 NOT-ASSESSED). Model non-updating UNASSESSED.'); blank()
a('SECTION H: IGNORED CRITIQUE AND NON-UPTAKE'); blank()
a('1. Precondition: critique production strongly expected (highly cited JPSP paradigm paper; large effect from small cells; later replication debate).')
a('2. Retrieval: RRR (N45, FULL-TEXT); Vohs et al. 2021 (A03, FULL-TEXT); Dang et al. 2021 (A01, FULL-TEXT version substitute); Carter et al. 2015 (X16, FULL-TEXT, POST HOC); Baumeister & Vohs 2016 comment (X17, FULL-TEXT, POST HOC); Inzlicht & Schmeichel 2012 and Kurzban et al. 2013 (N47, N37, METADATA).')
a('3. Reception opportunity: verified; the founding authors replied to the RRR (X17) and Muraven co-authored A03.')
a(f'4. Uptake in the uptake population: founding authors dispute the RRR manipulation (BV-E1; ENGAGEMENT I19) and a founding author co-signs the 2021 downgrade (VO-E3; I20). Co-citation carries no score: {post_crit}/{len(post)} RECEPTION-1 works published 2017 or later cite a listed critique (I23, descriptive); in RECENT-1, {rc_crit}/25 cite a listed critique or null test and {rc_fc}/25 cite a founding-cluster work beyond the target. Six inspected recent passages use the limited-resource model as a premise ({", ".join(prem_r)}; I09); one recent review excludes ego-depletion studies (R16, CTX-E28).'); blank()
a('57. Serious critiques: RRR 2016 (N45); Carter & McCullough 2014 and Carter et al. 2015 (A09, X16); Vohs et al. 2021 (A03); Dang et al. 2021 (A01); process-model and opportunity-cost revisions (N47, N37; R2); lay theories of willpower (A32; R3).')
a('58. Cited by the dominant cluster: founding authors cite and dispute the RRR (X17); R05 (2024) not read.')
a('59. Mode: disputed (2016), then partially accepted (2021 co-authored multi-site test).')
a('60. Network update: partial; RRR and process-model works are inside RECEPTION-1, while recent citers still use the model as a premise (I09).')
a('61. Recent papers: R16 qualifies (excludes depletion studies); R07, R08, R13, R17, R18, R21 use the model as a premise.')
a('62–63. Practitioner warnings: not searched; UNASSESSED.'); blank()
CRH='| Expected-production precondition | Critique / contrary evidence | Year | Source type | Main objection | Verification state | Reception opportunity | Cited by dominant cluster? | Uptake status | Dimension disposition | Effect on consensus |'
def critrows():
    a(CRH); a('|---|---|---|---|---|---|---|---|---|---|---|')
    a('| strong | Hagger et al. RRR (N45, W2499154041) | 2016 | preregistered multi-lab test | pooled d = 0.04 across 23 labs (RRR-E2) | FULL-TEXT-CONFIRMED | verified | yes; founding authors replied (X17) | disputed: "did not test ego depletion" (BV-E1) | SCORED 1 (I19, under review) | effect contested |')
    a('| strong | Vohs et al. (A03, W3119325546) | 2021 | preregistered multi-site test | d = 0.06, 95% CI [−0.02, 0.14] (VO-E2) | FULL-TEXT-CONFIRMED | verified | co-authored by Muraven | accepted: "not as reliable or robust as previously assumed" (VO-E3) | counts against concern (I20) | downgrade from inside the cluster |')
    a('| strong | Dang et al. (A01, W3014898655) | 2021 | preregistered multi-lab test | d = 0.10, 95% CI [0.01, 0.19] (DA-E2) | FULL-TEXT-CONFIRMED (version substitute) | verified | not determined | UNASSESSED | not scored separately | small effect |')
    a('| strong | Carter et al. 2015 (X16) | 2015 | bias-corrected meta-analysis | PET and PEESE "indistinguishable from zero" (CA-E2) | FULL-TEXT-CONFIRMED; POST HOC | verified | not determined | UNASSESSED | not scored separately | effect size contested |')
    a('| moderate | Inzlicht & Schmeichel 2012; Kurzban et al. 2013 (N47, N37) | 2012–2013 | theory | motivation/opportunity-cost rival (R2) | RECEPTION-CONFIRMED; METADATA | verified | not determined | UNASSESSED | not scored separately | rival mechanism inside RECEPTION-1 |')
critrows(); blank()
a('SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING'); blank()
vtxt='; '.join(f'{k} {v}' for k,v in venue.most_common(6))
a(f'64. Recurring authors: the four target authors appear on {len(FC)}/{n} RECEPTION-1 works ({", ".join(FC)}; I03), on R05 in RECENT-1, and on A03, A22, A45, A47 and R05 in ADJUDICATION-1 (plus overlap members N09, N33).')
a(f'65. Venues in RECEPTION-1 (top six): {vtxt}.')
a('66–67. Institutions, funding: not derived; UNASSESSED.')
a('68. Dissent venues: Perspectives on Psychological Science (RRR), Journal of Experimental Psychology: General (Carter et al. 2015), Psychological Science (Vohs et al. 2021), Social Psychological and Personality Science (Dang et al. 2021).')
a('69–70. Gatekeeping and ideology: not assessable.'); blank()
a('Closure type: authorship concentration around the founding cluster inside RECEPTION-1 (10/50 works, 62/113 internal in-edges); no journal, funding or advocacy closure established.'); blank()
a('SECTION J: FALSE-POSITIVE AND BASELINE CHECK'); blank()
a('71. Small field: no (self-control research is large; the target has more than 5,000 citers). 72. Baseline comparison: none built. 73. Adjacent expertise: the target\'s reference list includes stress, persistence and mood works, but none from the learned-helplessness or experimenter-expectancy queries (Section E). 74. Only people studying the question: no; most of RECEPTION-1 is from other fields. 75. Strong primary evidence: no; four small single-lab experiments (map field 1). 76. Repeated independent tests: yes for L2, with new data and near-zero to small effects (I13, I14); none for L1 in the locked search (I18). 77. Limitations preserved: partly; several premise uses state the resource as established (I09, I10). 78–80. Failed predictions acknowledged, critics engaged, updating: mixed (I19, I20).'); blank()
a('Answers are mixed; this is not a cartel signature. The founding cluster is central to the reception, but critiques sit inside the corpus and part of the founding cluster has updated.'); blank()
a('SECTION J2: THE CONCEDE TEST'); blank()
a('| Finding | Declared target claim | Matches map field 6? | Same mechanism as another row? | Count separately? |')
a('|---|---|---|---|---|')
a('| 1 Field-6 paradigm untested at scale; general effect near zero to small | field 6 via L1 and L2 | yes | no | yes |')
a('| 2 Founding-cluster-centred reception | field 6 network support | yes | no | yes |')
a('| 3 Recent premise use | later use of the target | no — MAP GAP: targets downstream use, not map field 6 | no | yes |')
a('| 4 Resource stated as shown | restatements of the target | no — MAP GAP: targets downstream restatements, not map field 6 | no | yes |')
a('| 5 Mixed critique uptake | field 6 network support | yes | no | yes |')
a('| 6 Rival literatures absent from the reference list | the target\'s reference list | no — MAP GAP: targets the source\'s engagement, not map field 6 | no | yes |')
a('| 7 Retrieval and record limits | the retrieval record | no — MAP GAP: targets the retrieval record, not map field 6 | no | yes |'); blank()
a('| Finding | Concede test: SURVIVES / NARROWS / DEFEATS | Surviving claim if NARROWS |')
a('|---|---|---|')
a('| 1 | NARROWS | In one lab with about 22 per cell, radish eaters quit unsolvable puzzles sooner; the magnitude is not supported as a general effect, and the paradigm has no high-powered direct replication in the locked search |')
for i in range(2,8): a(f'| {i} | SURVIVES | — |')
blank()
a('| Finding | Scope-loss level | Original claim | Surviving claim | What epistemic or practical work is lost? |')
a('|---|---|---|---|---|')
a('| 1 | major | d about 1.8 food-temptation effect showing a limited self-control resource | a single-lab small-sample difference; the general effect is near zero to small in preregistered multi-site tests (RRR-E2, VO-E2, DA-E2) | the large effect size and its use as evidence for a general limited resource |'); blank()
a('Finding 1 NARROWS field 6. Its failure location is the PAPER (small single-lab cells; numbers PROVISIONAL from secondhand sources); the network carries the claim forward (Findings 2–5).'); blank()
a('SECTION K0: EVIDENCE SUFFICIENCY LEDGER'); blank()
a('Gate B was applied to every inference before any score or finding used it. Inferences that fail stay listed with what would make them sufficient.'); blank()
a('INFERENCE LEDGER'); blank()
a('| Inference | Class | Corpus | Claimed scope | Sampling rule | Members used | Disposition | Statement |')
a('|---|---|---|---|---|---|---|---|')
inspR=', '.join(insp_rec)
INF=[
('I01','GRAPH-STRUCTURE','RECEPTION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED',f'Directed internal density {len(E)}/{den} = {dens} at work level (50/50 reference lists); no dense closed cluster inside RECEPTION-1.'),
('I02','GRAPH-STRUCTURE','RECEPTION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED',f'Founding-cluster works ({len(FC)}/{n} nodes) receive {fc_in}/{len(E)} internal edges, {nonfc_to_fc} from outside the cluster; the two top in-degree nodes are founding-cluster works (N19 {indeg["N19"]}, N06 {indeg["N06"]}).'),
('I03','DATABASE-RECORD','RECEPTION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED',f'{len(FC)}/{n} works list Baumeister, Bratslavsky, Muraven or Tice as an author ({", ".join(FC)}).'),
('I04','GRAPH-STRUCTURE','RECENT-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED',f'{rc_fc}/25 recent citers cite a founding-cluster work beyond the target; {rc_crit}/25 cite a listed critique or null test; {len(rc_fc_nocrit)}/25 cite founding-cluster work and no listed critique ({", ".join(rc_fc_nocrit)}).'),
('I05','CITATION-USE','RECEPTION-1','CORPUS','PRESPECIFIED-RANDOM',', '.join(sample_ids),'INSUFFICIENT',f'How RECEPTION-1 uses the target cannot be estimated from the random sample: {len(kept)}/12 sampled passages were inspectable (S2 contexts; no other authorized full text retrieved). Sufficient with all 12 passages.'),
('I06','CITATION-USE','RECEPTION-1','WITHIN-SAMPLE','CONVENIENCE',', '.join(kept),'SUPPORTED-WITHIN-SAMPLE','The four inspectable sampled passages: N27 QUALIFIES (CTX-E13), N41 SUPPORTS (CTX-E17), N42 and N44 MENTIONS (CTX-E18, CTX-E20).'),
('I07','CITATION-USE','RECEPTION-1','WITHIN-SAMPLE','CONVENIENCE',inspR,'SUPPORTED-WITHIN-SAMPLE',f'Among {ni} inspected passages: SUPPORTS {relc.get("SUPPORTS",0)}, PREMISE {relc.get("PREMISE",0)}, CHALLENGES {relc.get("CHALLENGES",0)}, QUALIFIES {relc.get("QUALIFIES",0)}, MENTIONS {relc.get("MENTIONS",0)}.'),
('I08','CITATION-USE','RECENT-1','CORPUS','EXHAUSTIVE','ALL','INSUFFICIENT',f'How the recent corpus uses the target: {nr}/25 passages inspected. Sufficient with all 25 passages.'),
('I09','CITATION-USE','RECENT-1','WITHIN-SAMPLE','CONVENIENCE',', '.join(insp_rcn),'SUPPORTED-WITHIN-SAMPLE',f'{len(prem_r)}/{nr} inspected recent passages use the limited-resource model as a premise ({", ".join(prem_r)}); R16 excludes depletion studies (CTX-E28).'),
('I10','CITATION-USE','—','NAMED','NOT-APPLICABLE','N05, N12, N22, N25, N43, R01, R07, R13','SUPPORTED','Eight passages state resource drain as an established fact when citing the target (CTX-E2, CTX-E5, CTX-E10, CTX-E11, CTX-E19, CTX-E22, CTX-E25, CTX-E27).'),
('I11','SOURCE-RESULT','—','NAMED','NOT-APPLICABLE','T01','SUPPORTED','The target measured behavioural differences; it states the limited resource as an inference: results "suggest" a limited capacity (TA-E1).'),
('I12','RESTATEMENT','—','NAMED','NOT-APPLICABLE','T01, N13, N33, A08, R01','INSUFFICIENT','Whether downstream restatements mutate the target claim. The target body was not read (publisher 403; ABSTRACT only), so the RESTATEMENT minimum is unmet. Sufficient with the target full text from an authorized source.'),
('I13','SOURCE-RESULT','—','NAMED','NOT-APPLICABLE','N45, A03, A01','SUPPORTED','Three preregistered multi-site tests of L2 find near-zero to small effects: d = 0.04 (RRR-E2), d = 0.06 [−0.02, 0.14] (VO-E2), d = 0.10 [0.01, 0.19] (DA-E2).'),
('I14','DATA-ORIGIN','—','NAMED','NOT-APPLICABLE','N45, A03, A01, T01','SUPPORTED','The three tests use new data collected under preregistered protocols across 23, multiple and 12 labs, independent of the target\'s single-lab data.'),
('I15','COMPOSITION','ADJUDICATION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED','Relevance composition of the evidence base within the locked search (METADATA-coded).'),
('I16','COMPOSITION','ADJUDICATION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED','Contribution composition within the locked search (METADATA-coded).'),
('I17','COMPOSITION','RECEPTION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED','Relevance composition of the citing set; describes citers, not the evidence base.'),
('I18','ABSENCE','ADJUDICATION-1','WITHIN-SAMPLE','EXHAUSTIVE','SCREENED','SUPPORTED-WITHIN-SAMPLE',f'Within the screened members of the locked search (59/59 screened), none tests L1 (the food-temptation → persistence paradigm): {len(dl1)} are DIRECT (L1). Bounded by queries Q1–Q7, top 10 each; known-item recall 8/12, so no statement is made beyond the search. The RRR chose another task (RRR-E1).'),
('I19','ENGAGEMENT','—','NAMED','NOT-APPLICABLE','X17','SUPPORTED','The founding authors\' 2016 comment says the RRR "did not test ego depletion" (BV-E1): critique engaged and disputed. X17 is a named POST HOC source (K11); under review.'),
('I20','ENGAGEMENT','—','NAMED','NOT-APPLICABLE','A03','SUPPORTED','A 2021 multi-site test co-authored by Muraven concludes depletion is "not as reliable or robust as previously assumed" (VO-E3): partial update inside the founding cluster.'),
('I21','GRAPH-STRUCTURE','—','NAMED','NOT-APPLICABLE','T01, '+', '.join(f'X{i:02d}' for i in range(1,16)),'SUPPORTED',f'The target\'s OpenAlex reference list (57/58 resolved) contains {sec_cited}/15 Section E locked sources and no learned-helplessness (F2) or experimenter-expectancy (F4) work.'),
('I22','ENGAGEMENT','—','NAMED','NOT-APPLICABLE','T01','NOT-ASSESSED','Whether the target text addresses helplessness, expectancy or motivation rivals. Not assessed: target body not read; sufficient with the full text.'),
('I23','CO-CITATION','RECEPTION-1','CORPUS','EXHAUSTIVE','ALL','SUPPORTED',f'{post_crit}/{len(post)} RECEPTION-1 works published 2017 or later cite a listed critique. Co-citation, not use; descriptive only.'),
('I24','ENGAGEMENT','—','NAMED','NOT-APPLICABLE','R05','NOT-ASSESSED','The founding authors\' 2024 status review (R05). Not assessed: no authorized full text retrieved; sufficient with its full text.'),
('I25','DATABASE-RECORD','—','NAMED','NOT-APPLICABLE','T01, A01, A03, A05','SUPPORTED','Target record: cited_by_count 5374 against a citing population of 5359; 58 referenced works, 57 resolved. Dang et al. 2021 carries year 2020; two works appear as duplicate records (A03, A05).'),
('I26','RESTATEMENT','—','NAMED','NOT-APPLICABLE','—','NOT-ASSESSED','Downstream reliance on review hubs (N06, N09, N16) in place of the target. Not assessed: no hub-citing passage inspected; sufficient with inspected passages from a defined hub-citing set.'),
]
for r in INF: a('| '+' | '.join(r)+' |')
blank()
for iid,col in (('I15','relevance'),('I16','contribution'),('I17','relevance')): a(f'COMPOSITION: {iid} | {col} | {COMP[iid][0]} | TOTAL={COMP[iid][1]}')
blank()
a(f'SAMPLE ATTRITION: I05 {len(kept)}/12'); blank()
a(f'Sample record: ranks 7, 9, 10, 11, 20, 27, 28, 39, 40, 41, 42, 44 drawn with the preregistered seed (lock/SAMPLES_draw.txt, sha256 cddd163f3db599c0ab84b4589764ee2c8f247a09bc8887479803511833df5a2f); inspected {", ".join(kept)}; the N40 context did not show the citation; the other 7 had no usable context and no authorized full text retrieved.'); blank()
a('Withheld inferences: I05 (INSUFFICIENT: sample attrition), I08 (INSUFFICIENT: 12/25 recent passages), I12 (INSUFFICIENT: target body not read), I22, I24 and I26 (NOT-ASSESSED).'); blank()
a('DIMENSION EVIDENCE BASIS'); blank()
a('DIMENSION CLASS MAP: cn7-map-3'); blank()
a('| Scorecard dimension | Scorecard disposition | Inference IDs | Basis note |')
a('|---|---|---|---|')
DIM=[('Founding-cluster dominance','SCORED 2','I02 (+), I03 (+)',f'founding works {len(FC)}/{n} nodes take {fc_in}/{len(E)} internal edges; top two hubs are founding works'),
('Internal citation density','SCORED 0','I01 (-)',f'{dens} inside RECEPTION-1 only; closure not excluded beyond it'),
('Recent-paper dependence','SCORED 2','I04 (+), I09 (+), I08 (?)',f'{rc_fc}/25 recent citers cite founding work beyond the target; {len(prem_r)}/{nr} inspected passages premise use; census {nr}/25 inspected'),
('Review-hub laundering','UNASSESSED','—','I26 NOT-ASSESSED: no hub-citing passage inspected; RESTATEMENT minimum unmet'),
('Proxy mismatch','SCORED 1','I10 (+), I11 (+), I12 (?)','behavioural differences restated as a shown resource drain; restatement comparison INSUFFICIENT'),
('Claim mutation','UNASSESSED','—','I12 INSUFFICIENT: target held at ABSTRACT level'),
('Adjacent-field neglect','SCORED 1','I21 (+), I22 (?)','0/15 locked sources and no F2/F4 work in the reference list; text engagement not assessed'),
('Lack of decisive tests','SCORED 1','I18 (+), I13 (-), I14 (-)',f'L2 tested decisively with new data (near zero to small); L1 paradigm {len(dl1)}/59 in the locked search'),
('Poor critique uptake','SCORED 1','I19 (+), I20 (-), I24 (?)','founding authors disputed the RRR (2016) and one co-signed a downgrade (2021); 2024 review not read'),
('Intervention-evidence ratchet','N/A','—','no intervention claim at field 6 or in the traced network'),
('Model non-updating','UNASSESSED','—','four-link gate: link 4 not determinable (I19, I20 mixed; I24 NOT-ASSESSED)')]
for r in DIM: a('| '+' | '.join(r)+' |')
blank()
a('FINDING EVIDENCE BASIS'); blank()
a('| Finding | Finding status | Inference IDs |')
a('|---|---|---|')
for r in [('Finding 1','confirmed','I11, I13, I14, I18'),('Finding 2','confirmed','I01, I02, I03'),('Finding 3','provisional','I04, I09, I08'),('Finding 4','provisional','I10, I11, I12'),('Finding 5','provisional','I19, I20, I24'),('Finding 6','provisional','I21, I22'),('Finding 7','confirmed','I25')]: a('| '+' | '.join(r)+' |')
blank()
a('SECTION K: CARTEL-RISK SCORING'); blank()
a('Scores are in Artifact 8. All seven scored dimensions are INDEPENDENT: no two rest on the same passage or test. Founding-cluster dominance and internal density use the same RECEPTION-1 edge list but answer different questions (in-edge concentration and authorship vs overall density); recent-paper dependence uses the separate RECENT-1 corpus.'); blank()
a('- Verified risk score: 8/21')
a('- Verified scored-dimension risk rate: 38.1')
a('- Independent scored dimensions: 7')
a('- Nested scored dimensions: 0')
a('- Verified risk denominator: 21')
a('- Evidentiary coverage: 7/10 applicable dimensions scored (70%)')
a('- Execution completeness: 7/10 applicable dimensions completed (70%)')
a('- Dimension inventory: 7 INDEPENDENT SCORED + 0 NESTED SCORED + 0 UNINFORMATIVE + 3 UNASSESSED + 1 N/A = 11 total dimensions; 10 applicable')
a('- Unscored dimensions: Review-hub laundering — UNASSESSED (I26); Claim mutation — UNASSESSED (I12 INSUFFICIENT); Model non-updating — UNASSESSED (link 4 not determinable); Intervention-evidence ratchet — N/A (no intervention claim)'); blank()
VS='Verified scored-dimension risk: 38.1%, calculated from 7 independent scored dimensions; 0 additional scored dimensions are NESTED; 7 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.'
a(VS); blank()
a('Formal-label gate: coverage 7/10 (70%) declared, exactly at the PROVISIONAL 70% gate (engineering threshold, not validated). Recent-paper dependence, proxy mismatch, adjacent-field neglect, lack of decisive tests and poor critique uptake carry open review items, so coverage is 2/10 (20%) if those items are withdrawn: the gate is met only if the review items resolve. Label-essential check: the arithmetic position is the >20%–40% band, which is not a closure, laundering or healthy label; no closure or laundering label is proposed, because review-hub laundering, claim mutation and model non-updating are UNASSESSED. The rate is 1.9 points below the 40% boundary, so the band position is sensitive to any one score.'); blank()
a('ARITHMETIC BAND POSITION: >20%–40% (normal field clustering with some weaknesses)')
BAND='>20%–40% normal field clustering with some weaknesses — computed over 7 independent scored dimensions; breadth requirement PASSED. PROVISIONAL: coverage meets the 70% gate exactly and only if five review items resolve (20% without them); no closure or laundering label is supported because review-hub laundering, claim mutation and model non-updating are UNASSESSED.'
a('RISK BAND: '+BAND)
MECH='a founding-cluster-centred reception: the founding authors\' own works are the main internal hubs and recent citers keep using the limited-resource model as a premise, while independent preregistered multi-site tests of the general effect found near-zero to small effects and the founding cluster has only partly updated; the field-6 paradigm itself was not re-tested at scale'
a('MECHANISM LABEL: '+MECH); blank()
a('ARTIFACT 1: TOP 15 CITATION SPINE TABLE'); blank()
a('| Rank | Paper | Year | Citation count | Evidence type | Role in network | Source of citation count |')
a('|---:|---|---:|---:|---|---|---|')
for i,w in enumerate(R[:15],1):
    sid=f'N{i:02d}'; r=bysid[sid]
    au_=', '.join(x['author']['display_name'] for x in w['authorships'][:3])+(' et al.' if len(w['authorships'])>3 else '')
    et={'REVIEW':'review article','THEORY':'theory','METHOD':'method','INDEPENDENT-DATA':'primary empirical study','COMMENTARY':'commentary'}.get(r[5],r[5])
    a(f'| {i} | {sid} {au_}: {w["display_name"][:70]} ({w["id"][21:]}) | {w["publication_year"]} | {w["cited_by_count"]} | {et} | {r[3]}; {r[4]}{"; founding cluster" if sid in FC else ""} | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |')
blank()
a('ARTIFACT 2: FOUNDING CLUSTER TABLE'); blank()
a('| Paper | Year | Claim introduced | Evidence type | Verification state | Later role | Risk |')
a('|---|---|---|---|---|---|---|')
a('| Baumeister, Bratslavsky, Muraven & Tice, Ego depletion (T01, W2123817056) | 1998 | acts of volition draw on a limited resource; radish/chocolate persistence effect | four small single-lab experiments | ABSTRACT only (TA-E1) | canonical source; cited by 5,000+ | high for field 6 magnitude (Finding 1) |')
a(f'| Muraven, Tice & Baumeister, Self-control as a limited resource (N19) | 1998 | regulatory depletion across tasks | primary empirical study | RECEPTION-CONFIRMED; METADATA | top in-degree hub ({indeg["N19"]}) | founding-cluster hub |')
a(f'| Muraven & Baumeister, Self-regulation and depletion of limited resources (N06) | 2000 | strength model review | review article | RECEPTION-CONFIRMED; EXCERPT (CTX-E3) | second hub ({indeg["N06"]}); {rc_hub["N06"]}/25 recent citers | founding-cluster hub |')
a(f'| Gailliot et al., Self-control relies on glucose (N41) | 2007 | glucose as the resource (L3) | primary empirical study | RECEPTION-CONFIRMED; EXCERPT (CTX-E17) | third hub ({indeg["N41"]}) | L3 mechanism later contested (A16, A19 titles) |')
a('| Vohs et al., multisite preregistered paradigm (A03) | 2021 | depletion "not as reliable or robust as previously assumed" | preregistered multi-site test | FULL-TEXT-CONFIRMED | partial update with founding-author co-author (Muraven) | none |'); blank()
a('ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE'); blank()
a('"Cites founding cluster?" means a work by Baumeister, Bratslavsky, Muraven or Tice beyond the target (all cite the target by construction). "Cites hub?" means N06, N09, N16 or N19. "Cites adjacent fields?" means a listed critique, null test or rival-mechanism work in the OpenAlex reference list.'); blank()
a('| Recent paper | Year | Verification state | Cites founding cluster? | Cites hub? | Cites adjacent fields? | New evidence or recycling? |')
a('|---|---:|---|---|---|---|---|')
for sid,w,fcw,cr,rv,hb in recent_rows:
    r=bysid[sid]
    vs_='RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt)' if r[7]=='INSPECTED' else 'RECEPTION-CONFIRMED; LOCATED'
    if r[7]=='INSPECTED':
        nev=('recycling: premise use' if r[4]=='PREMISE' else r[4].lower())+f' ({CTX[sid]})'
    else: nev='not determined (no passage inspected)'
    adj=cr+rv
    a(f'| {sid} {w["display_name"][:70]} ({w["id"][21:]}) | {w["publication_year"]} | {vs_} | {"yes ("+", ".join(fcw)+")" if fcw else "target only"} | {", ".join(hb) if hb else "no"} | {"; ".join(adj) if adj else "no"} | {nev} |')
blank()
a(f'RECENT-1 summary: founding-cluster work beyond the target {rc_fc}/25; listed critique or null test {rc_crit}/25; rival-mechanism work {rc_riv}/25; founding work without any listed critique {len(rc_fc_nocrit)}/25; hubs N09 {rc_hub["N09"]}, N06 {rc_hub["N06"]}, N16 {rc_hub["N16"]}, N19 {rc_hub["N19"]}.'); blank()
a('ARTIFACT 4: CITATION POLARITY TABLE'); blank()
a('| Citing paper | Cited paper | Verification state | Citation polarity | Claim use | Inflation risk |')
a('|---|---|---|---|---|---|')
pol={'SUPPORTS':'supportive','CHALLENGES':'critical','QUALIFIES':'qualifying','MENTIONS':'neutral/background','PREMISE':'supportive (premise)'}
infl=('N05','N12','N22','N25','N43','R01','R07','R13','A08','X20')
for r in rows:
    if r[7]=='INSPECTED':
        st='FULL-TEXT-CONFIRMED' if r[6].startswith('FULL') else 'FULL-TEXT-CONFIRMED (excerpt)'
        risk='moderate' if r[0] in infl else ('none' if r[4] in ('CHALLENGES','QUALIFIES') else 'low')
        a(f'| {r[1][:70]} | Baumeister et al. 1998 | {st} | {pol.get(r[4],"neutral/background")} | {r[8][:120].replace("|","/")} | {risk} |')
blank()
a(f'Semantic Scholar contexts were used as EXCERPT access; {S2}.'); blank()
a('ARTIFACT 5: CLAIM MUTATION TABLE'); blank()
a('| Original source | Original claim | Verification state | Hub restatement | Downstream restatement | Mutation severity |')
a('|---|---|---|---|---|---|')
a('| Target abstract (TA-E1) | results "suggest" a limited capacity for volition | ABSTRACT only | N33 "appears to depend on a limited resource" (CTX-E15) | X19 "Willpower is limited"; X20 "drained the subjects\' self-control" | not graded (RESTATEMENT minimum unmet) |')
a('| Target Experiment 1 (field 6, PROVISIONAL) | radish eaters quit sooner, one lab | secondhand (Stage 1) | none found | N13 (CTX-E6), A22 (CTX-E38) faithful | not graded |')
a('| Target and follow-ups | depletion effect first reported | ABSTRACT only | none found | A08 "over 300 independent studies have replicated this effect" (CTX-E34) | not graded |')
a('| Target | ego depletion / limited resource | ABSTRACT only | none found | R01 "displaced behavior theory" attributed to Baumeister (CTX-E22) | not graded |'); blank()
a('ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE'); blank()
a('Preregistration table as in SECTION E. POST HOC rows anchor no score.'); blank()
negrows(); blank()
a('ARTIFACT 7: CRITIQUE-UPTAKE TABLE'); blank()
critrows(); blank()
a('ARTIFACT 8: CARTEL-RISK SCORECARD'); blank()
a('| Dimension | Applicability | Dimension disposition | Score if SCORED | Evidence / claim state | Evidence supporting disposition and score | Evidence identifiers | Retrieval coverage | AGGREGATION STATUS | Independent evidence and inferential work, or nesting rationale | Reason excluded from denominator | Effect on formal-label gate |')
a('|---|---|---|---|---|---|---|---|---|---|---|---|')
a(f'| Founding-cluster dominance | applicable | SCORED 2 | 2 | RECEPTION-CONFIRMED (verification state for score 2: computed from 50/50 OpenAlex reference lists and authorships) | {len(FC)}/{n} founding works take {fc_in}/{len(E)} internal edges; top two hubs founding | I02; I03 | 50/50 reference lists | INDEPENDENT | in-edge concentration and authorship | — | counts toward coverage |')
a(f'| Internal citation density | applicable | SCORED 0 | 0 | RECEPTION-CONFIRMED | {len(E)}/{den} = {dens} | I01 | 50/50 inputs | INDEPENDENT | overall density | — | affirmative inside RECEPTION-1 only |')
a(f'| Recent-paper dependence | applicable | SCORED 2 | 2 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpts) (verification state for score 2: 25/25 reference lists; {nr}/25 passages) | {rc_fc}/25 cite founding work beyond target; {len(prem_r)}/{nr} inspected premise use | I04; I09; I08 | 25/25 reference lists; {nr}/25 passages | INDEPENDENT | separate recent corpus | — | counts toward coverage; under review |')
a('| Review-hub laundering | applicable | UNASSESSED | — | — | hub reliance not traced | I26 | 0 hub-citing passages | — | — | UNASSESSED | not essential to the issued band; closure and laundering labels unavailable |')
a('| Proxy mismatch | applicable | SCORED 1 | 1 | FULL-TEXT-CONFIRMED (excerpts); ABSTRACT for target | resource drain stated as shown (8 passages) vs "suggest" in TA-E1 | I10; I11; I12 | 8 named passages | INDEPENDENT | restated construct vs measured behaviour | — | counts toward coverage; under review |')
a('| Claim mutation | applicable | UNASSESSED | — | — | target body not read | I12 | ABSTRACT only | — | — | UNASSESSED | closure and laundering labels unavailable |')
a(f'| Adjacent-field neglect | applicable | SCORED 1 | 1 | METADATA (reference list) | {sec_cited}/15 locked sources; no F2/F4 work cited | I21; I22 | 57/58 references resolved | INDEPENDENT | source-layer reference list | — | counts toward coverage; under review |')
a(f'| Lack of decisive tests | applicable | SCORED 1 | 1 | FULL-TEXT-CONFIRMED (tests); METADATA (screen) | L2 tested decisively (RRR-E2, VO-E2, DA-E2); L1 {len(dl1)}/59 in the locked search | I18; I13; I14 | ADJUDICATION-1 screened by title | INDEPENDENT | named test results and search absence | — | counts toward coverage; under review |')
a('| Poor critique uptake | applicable | SCORED 1 | 1 | FULL-TEXT-CONFIRMED | RRR disputed (BV-E1); 2021 downgrade co-signed (VO-E3) | I19; I20; I24 | X17, A03 full texts | INDEPENDENT | engagement in the uptake population | — | counts toward coverage; under review |')
a('| Intervention-evidence ratchet | not applicable | N/A | — | — | no intervention claim | — | — | — | — | N/A: no intervention claim | none |')
a('| Model non-updating | applicable | UNASSESSED | — | — | link 4 not determinable | I19; I20; I24 | R05 not read | — | — | UNASSESSED | closure label unavailable |'); blank()
a('Verified risk score 8/21; rate 38.1%; independent 7; nested 0; denominator 21; coverage 7/10 (70%); completeness 7/10 (70%).'); blank()
a(VS); blank()
a('ARTIFACT 9: NETWORK MAP'); blank()
a(f'Receipts as in SECTION A (RECEPTION-1, {n} work nodes, {len(E)} edges, density {len(E)}/{den}, input coverage 50/50, COMPUTED-FROM-RETRIEVED). Founding-cluster nodes: {", ".join(FC)}. Closure beyond RECEPTION-1 is not established and not excluded.'); blank()
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
for x in [f'Main founding cluster: the four target authors; {len(FC)}/{n} RECEPTION-1 works, receiving {fc_in}/{len(E)} internal edges',
 'Main amplification hub: N19 Muraven, Tice & Baumeister 1998 and N06 Muraven & Baumeister 2000 (founding-cluster works); N09 is the hub most cited by recent works',
 'Main proxy problem: behavioural persistence differences restated as a shown resource drain (I10, I11)',
 'Main adjacent fields neglected: learned helplessness (same outcome) and experimenter expectancy at the reference-list level (I21); text engagement not assessed (I22)',
 'Main claim mutation: not graded (target body not read); candidate certainty upgrades recorded (A08 "over 300 independent studies", X19, X20)',
 'Most important ignored critique: the 2016 RRR, disputed by the founding authors (BV-E1); later partly accepted (VO-E3)',
 f'Decisive test missing: a high-powered direct replication of the food-temptation → persistence paradigm ({len(dl1)}/59 in the locked search); the general effect has been tested (I13, I14)',
 'Verified risk score: 8/21','Verified scored-dimension risk rate: 38.1','Independent scored dimensions: 7','Nested scored dimensions: 0','Verified risk denominator: 21',
 'Evidentiary coverage: 7/10 (70%)','Execution completeness: 7/10 (70%)','Dimension inventory: 7 INDEPENDENT SCORED + 0 NESTED SCORED + 0 UNINFORMATIVE + 3 UNASSESSED + 1 N/A',
 'Unscored dimensions and reasons: Review-hub laundering UNASSESSED (I26); Claim mutation UNASSESSED (I12); Model non-updating UNASSESSED (link 4); Intervention-evidence ratchet N/A',
 'N-of-M scope statement: '+VS,'Arithmetic band position: >20%–40% (normal field clustering with some weaknesses)','Risk band: '+BAND,'Mechanism label: '+MECH,
 'Formal-label gate status: coverage 70% declared (exactly at the PROVISIONAL threshold); 20% if open review items are withdrawn; MET ONLY IF REVIEW ITEMS RESOLVE',
 'Load-bearing finding(s): Finding 1 (field-6 magnitude NARROWS); Finding 2 (founding-cluster-centred reception)',
 'Concede-test result: field 6 NARROWED by Finding 1 (scope loss major); Findings 2–7 SURVIVE',
 'Failure location: PAPER (Findings 1, 6); CITATION (Findings 2, 3, 4, 5); MODEL-RETRIEVAL (Finding 7)',
 'Best formal label: normal field clustering with some weaknesses (the >20%–40% band; field size is not small), provisional at the 70% gate; no cartel or laundering label supported',
 f'Confidence level: Low to moderate. CITATION CONTEXT COVERAGE: RECEPTION-1 {cov["RECEPTION-1"][0]}/{cov["RECEPTION-1"][1]}; CITATION CONTEXT COVERAGE: RECENT-1 {cov["RECENT-1"][0]}/{cov["RECENT-1"][1]}; CITATION CONTEXT COVERAGE: ADJUDICATION-1 {cov["ADJUDICATION-1"][0]}/{cov["ADJUDICATION-1"][1]}',
 'What evidence would change this assessment: the target full text from an authorized source; the 8 uninspectable sampled RECEPTION-1 passages; the 13 uninspected RECENT-1 passages; the 2024 status review (R05); inspected passages citing N06, N09 or N16; a direct high-powered replication of the food-temptation paradigm',
 'Density inference scope: RECEPTION-1 only (OpenAlex cites:W2123817056, top 50 records, executed 2026-11-05T11:31:57Z); closure is not established and not excluded beyond the defined corpus']:
    a('- '+x)
blank()
a('FINAL SECTION: STANDARDIZED FINDING TABLE'); blank()
FIND=[
dict(Finding='The field-6 paradigm has no high-powered direct replication in the locked search, and preregistered multi-site tests of the general effect find near-zero to small effects, so the large field-6 effect does not hold as a general result.',T=F6,M='full texts of N45 (RRR-E1, RRR-E2), A03 (VO-E2, VO-E3), A01 (DA-E2); ADJUDICATION-1 screen; TA-E1',C='size and generality of the depletion effect',FM='other: unreplicated paradigm with a small general effect',S='major',CT='NARROWS',SL='major — surviving claim: in one lab with about 22 per cell, radish eaters quit unsolvable puzzles sooner; the magnitude is not supported as a general effect',E='I11; I13; I14; I18; RRR-E2; VO-E2; DA-E2.',ET='primary study',VS='FULL-TEXT-CONFIRMED; CROSS-SOURCE-CONFIRMED; field-6 numbers PROVISIONAL',IE='The multi-site tests used other first tasks (e-crossing, writing) and the RRR cited the original task\'s experimenter involvement; the original paradigm may behave differently.',W='A preregistered high-powered replication of the food-temptation paradigm with an effect near the original.',FL='PAPER — small single-lab cells',St='confirmed'),
dict(Finding=f'The reception is founding-cluster-centred: {len(FC)}/{n} RECEPTION-1 works are by the target authors and receive {fc_in}/{len(E)} internal edges, though overall density is low.',T=F6,M='RECEPTION-1 edge list (50/50 reference lists) and authorships',C='founding-cluster dominance and closure',FM='founding-cluster dominance',S='moderate',CT='SURVIVES',SL='N/A — SURVIVES',E='I01; I02; I03; Section A receipts.',ET='author inference',VS='RECEPTION-CONFIRMED',IE='Founding authors are prolific in a large field; their reviews are natural hubs.',W='A matched comparison graph showing the same in-edge concentration for other influential papers.',FL='CITATION — network structure',St='confirmed'),
dict(Finding=f'Recent citers rely on founding-cluster work and use the limited-resource model as a premise: {rc_fc}/25 cite founding work beyond the target; {len(prem_r)}/{nr} inspected passages use it as a premise.',T='MAP GAP: this finding targets downstream use of the target, not map field 6.',M='RECENT-1 reference lists (25/25); 12/25 passages',C='recent-paper dependence',FM='other: recent premise recycling',S='moderate',CT='SURVIVES',SL='N/A — SURVIVES',E='I04; I09; I08 (INSUFFICIENT); CTX-E25; CTX-E27; CTX-E30.',ET='author inference',VS='RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpts); PROVISIONAL',IE='Ranking by citation count favours applied reviews; premise use may be framed with caveats elsewhere.',W='Full recent passages showing caveats, or a random recent sample with less premise use.',FL='CITATION — recent reception',St='provisional'),
dict(Finding='Several citing passages state resource drain as shown, where the target abstract states it as an inference.',T='MAP GAP: this finding targets downstream restatements of the target, not map field 6.',M='S2 contexts CTX-E2, E5, E10, E11, E19, E22, E25, E27 against TA-E1',C='proxy-to-construct mismatch',FM='proxy-to-construct mismatch',S='minor',CT='SURVIVES',SL='N/A — SURVIVES',E='I10; I11; I12 (INSUFFICIENT); TA-E1.',ET='author inference',VS='FULL-TEXT-CONFIRMED (excerpts); ABSTRACT for target; PROVISIONAL',IE='Excerpts are short; the target body may state the resource more strongly than the abstract.',W='The target full text stating the resource as demonstrated.',FL='CITATION — downstream restatement',St='provisional'),
dict(Finding='Critique uptake is mixed: the founding authors disputed the RRR in 2016, and a founding-author co-signed multi-site test conceded in 2021 that the effect is less reliable than assumed.',T=F6,M='full texts X17 (BV-E1), A03 (VO-E3)',C='critique uptake',FM='critique non-uptake (partial)',S='minor',CT='SURVIVES',SL='N/A — SURVIVES',E='I19; I20; I24 (NOT-ASSESSED); BV-E1; VO-E3.',ET='author inference',VS='FULL-TEXT-CONFIRMED; PROVISIONAL',IE='Disputing a manipulation check is a legitimate scientific response.',W='The 2024 status review (R05) fully accepting or rejecting the null results.',FL='CITATION — uptake by the founding cluster',St='provisional'),
dict(Finding=f'The target\'s reference list contains {sec_cited}/15 locked adjacent sources and no learned-helplessness or experimenter-expectancy work, though both bear on the field-6 outcome.',T='MAP GAP: this finding targets the source\'s engagement, not map field 6.',M='raw/target_reflist_titles.json (57/58 resolved) against the Section E lock',C='adjacent-field neglect',FM='adjacent-field neglect',S='minor',CT='SURVIVES',SL='N/A — SURVIVES',E='I21; I22 (NOT-ASSESSED); Section E table.',ET='author inference',VS='METADATA; PROVISIONAL',IE='The text may address these rivals without citing the locked works; the lock picks the most-cited titles, not the most relevant.',W='The target text discussing helplessness or expectancy explanations.',FL='PAPER — reference list',St='provisional'),
dict(Finding='Retrieval limits bound this audit: the target body is not authorized-accessible, the random sample lost 8/12 passages, and OpenAlex records carry duplicates and a wrong year.',T='MAP GAP: this finding targets the retrieval record, not map field 6.',M='retrieval log; lock/SAMPLES_draw.txt; raw/target_work.json; ADJUDICATION-1 records',C='retrieval and record quality',FM='other: retrieval and database record limits',S='moderate',CT='SURVIVES',SL='N/A — SURVIVES',E='I25; SAMPLE ATTRITION I05 4/12 and RECENT-1 coverage 12/25 (SECTION K0, recorded facts, not inferences).',ET='author inference',VS='RECEPTION-CONFIRMED',IE='Paywalls and database merges are general, not specific to this paper.',W='Authorized access to the target and to the sampled passages.',FL='MODEL-RETRIEVAL — access and database record',St='confirmed')]
for i,f in enumerate(FIND,1):
    a(f'Finding {i}'); blank()
    a('| Field | Entry |'); a('|---|---|')
    for k,lab_ in (('Finding','Finding'),('T','Target claim'),('M','What was measured'),('C','What was claimed'),('FM','Failure mode'),('S','Severity'),('CT','Concede test'),('SL','Scope loss if NARROWS'),('E','Evidence'),('ET','Evidence type'),('VS','Verification state'),('IE','Possible innocent explanation'),('W','What would weaken this'),('FL','Failure location'),('St','Status')):
        a(f'| {lab_} | {f[k]} |')
    if i<len(FIND): blank()
import os; os.makedirs('v2cand3',exist_ok=True)
OUTF='v2cand3/02c_citation_network_v2cand3.md'
open(OUTF,'w').write('\n'.join(L)+'\n')
print('wrote',OUTF,'lines',len(L))
