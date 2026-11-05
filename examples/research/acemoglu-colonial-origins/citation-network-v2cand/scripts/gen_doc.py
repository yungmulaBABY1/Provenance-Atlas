import json,re,subprocess
from collections import Counter
L=json.load(open('out/ledger.json')); rows=L['rows']; sid=L['sid']
G=json.load(open('graph_v2cand.json'))
r1=json.load(open('raw/reception1_top50.json'))['results']; rc=json.load(open('raw/recent1_top25.json'))['results']
W=lambda u:u.split('/')[-1]
S=lambda w:sid[w]
edges=[tuple(e) for e in G['edges']]; team=G['team']
E=len(edges)
ex=[(a,b) for a,b in edges if 'N01' not in (a,b)]
team_x=[t for t in team if t!='N01']
toteam_x=sum(1 for a,b in ex if b in team_x)
indeg=Counter(b for a,b in edges); indeg_x=Counter(b for a,b in ex)
es=set(edges); recip=sorted({tuple(sorted(e)) for e in edges if (e[1],e[0]) in es})
cite_any=len({a for a,b in edges})
rec=G['recent']; fc_recent=[S(r[0]) for r in rec if r[2]]
rodrik_recent=sum(1 for r in rec if r[3]); gl_recent=sum(1 for r in rec if r[4]); al_recent=sum(1 for r in rec if r[5])
hb_recent=sum(1 for r in rec if set(r[2])&{'W1580107285','W2108614304'})
def corp(c): return [r for r in rows if c in r['mem'].split('+')]
def cnt(c,k): return Counter((r[k].split()[0] if k in('rel','acc') else r[k]) for r in corp(c))
INS={c:sum(r['ctx']=='INSPECTED' for r in corp(c)) for c in ['RECEPTION-1','RECENT-1','ADJUDICATION-1']}
HB=S('W2108614304'); HBC=S('W1580107285'); RD=S('W2994756033'); RDW=S('W1977433163'); GL=S('W2890314743'); EL=S('W3122513675'); DML=S('W3123436326'); HW=S('W1480274481'); REPLY=S('W3124131699')
LEVR=S('W2113844427'); LEVC=S('W1588189399'); DJO=S('W2104834906'); HID=S('W2064927380'); RZ=S('W3122778615')
SAMPLE=['W4223529822','W4292663674','W4292849668','W4319016949','W4387877962','W4391180104']; SAMP=sorted(S(w) for w in SAMPLE)
r1ins=[r['sid'] for r in corp('RECEPTION-1') if r['ctx']=='INSPECTED']
def comp(iid,c,col,key):
    cc=cnt(c,key); return f"COMPOSITION: {iid} | {col} | "+"; ".join(f"{k}={v}" for k,v in sorted(cc.items()))+f" | TOTAL={sum(cc.values())}"
uc=Counter()
for r in corp('RECEPTION-1'):
    if r['ctx']=='INSPECTED':
        for u in r['relat'].split('+'): uc[u]+=1
d=E/2450*100; dx=len(ex)/(49*48)*100; tshare=sum(1 for a,b in edges if b in team)
k=INS['RECEPTION-1']
X,Y=3,21; rate=X/Y*100
o=[]; P=o.append
full=subprocess.run(['git','-C','/workspace/Provenance-Atlas','rev-parse','b6d7869:prompts/research-analysis/2-citation-network.v2-candidate.txt'],capture_output=True,text=True).stdout.strip() or 'UNRESOLVED'
P("# Citation-Network Audit, v2-candidate diagnostic run — Acemoglu, Johnson & Robinson (2001)\n")
P("INSTRUMENT PREFLIGHT: yungmulaBABY1/Provenance @ 07b72b585c934c5daff63953b22cf6424bfa8f6b : candidates/research-analysis/2-citation-network.v2-candidate.txt | sha256 3b4be80dcea68dc804bb6d72ca461a25f99a24f8bd8784e086289d9040f89896 | 1949 lines | 85977 bytes | identity CONFIRMED against the brief's pins (gate checker sha256 90de7375…, v1 checker sha256 f66650fe…, claim map sha256 f6e7df18…)\n")
P("INSTRUMENT VERSION: 2-citation-network v2-candidate.2\n")
P("DIMENSION CLASS MAP: cn7-map-2\n")
P("Run metadata. DIAGNOSTIC LIVE RUN of citation-network candidate revision 2 (not a validation run). Executor: Grok Bot (audit run), branch audit/acemoglu-colonial-origins-v2cand created from b6d786947030902cf58cb114055d6cd48df6ad9c. Execution date 2026-11-04 PST (2026-11-05 UTC). Clock times are PST (UTC-8) with UTC in parentheses. Mode: full-sequence; upstream claim map examples/research/acemoglu-colonial-origins/01_claim_extraction.md (sha256 f6e7df18…, verified). Tools: OpenAlex works API (all corpora, graph, co-citation counts); publisher, repository, HAL, NBER and arXiv full texts; v1 full texts and evidence passages reused by sha256. Semantic Scholar was not called; no EXCERPT access was used. Recent window: 2021-11-04 to 2026-11-04.\n")
P("VALIDATION BOUNDARY. This instrument revision is a candidate. It has not been validated for open retrieval. This run used open retrieval over three registered corpora (50 + 25 + 58 members). Every percentage, band and label below is an unvalidated open-retrieval application reported for diagnosis of the instrument, not as a validated verdict.\n")
P("EXPOSURE DISCLOSURE (before SECTION A0). Before this run the executor had: produced the v1 citation-network output (02c_citation_network.md) and stages 01, 2a, 2b and 3 of this audit; read AJR (2001) and NBER WP 7771, Albouy (2012) and its revision appendix, the AJR (2012) Reply, the 2024 Nobel scientific and popular backgrounds, and the v1 full texts of Rodrik et al., Glaeser et al., Sachs, Easterly–Levine, the AJR handbook WP, Chernozhukov et al., Hanushek–Woessmann, Levine, Dell–Jones–Olken, Rajan–Zingales, Hidalgo et al. and Keller; and had seen the v1 RECENT top-25 titles before drawing the RECENT-1 sample. During identity checks (about 8:28 PM PST, 04:28 UTC) a grep for \"FAIL-CN\" was run on an older local clone's FAILURES.md (commit c1bcb8b); it showed only the FAIL-CN-001…006 headings and contains no FAIL-CN-007 entry. None of the brief's no-open files (tests/cases/citation-network-v2-gates/ and README, the candidate CHANGES file, the FAIL-CN-007 entry, the Provenance PR #14 description) was opened. Because of this exposure the Section E requirement to lock before bibliography inspection cannot be met by this auditor: the v1 locked query is reused and marked reused, and the new ADJUDICATION-1 search was locked before any of its results were screened.\n")
P("PRE-AUDIT CLAIM CONFIRMATION\n")
P("- Claim under audit (map field 6): In the base sample of 64 former colonies, the 2SLS estimate of the effect of the 1985–95 protection-against-expropriation index on 1995 log GDP per capita, instrumented by log settler mortality, is 0.94 (SE 0.16).")
P("- What was literally measured (map field 1): 64 former colonies; 1995 log GDP per capita (PPP); PRS average protection-against-expropriation index 1985–95; log settler mortality; OLS and 2SLS (AJR 2001 Table 4).")
P("- Weaker defensible claim (map field 3): in this sample with this instrument the coefficient is 0.94 (SE 0.16); causal and \"institutions\" readings are conditional on the exclusion restriction and on the index as a proxy; the implied 7-fold Nigeria–Chile gap is an upper bound in the authors' words.")
P("- Target layer: field 6 for the network verdict; downstream layers are named as MAP GAP findings. Layer labels L1–L4 and rivals R1 (direct geography/disease) and R2 (settler human capital) are defined in the v1 output Section E, not in the claim map.\n")
P("The map is upstream-generated, not self-generated.\n")
P("SECTION A0: CORPUS REGISTER AND SOURCE ELIGIBILITY\n")
P("Corpus planning. Questions: (a) how AJR 2001 is received (RECEPTION-1, RECENT-1); (b) what the evidence base testing field 6 and its rivals contains (ADJUDICATION-1). Proposed inferences were tested in SECTION K0 before use; those that fail stay there as INSUFFICIENT or NOT-ASSESSED.\n")
P("CORPUS REGISTER\n")
reg=[('RECEPTION-1','RECEPTION','How the most-cited works citing AJR 2001 relate to it and to each other.',"OpenAlex works API, filter=cites:W3124166904, sort=cited_by_count:desc, per-page=50, page 1, queried 2026-11-04 8:29 PM PST (2026-11-05T04:29:45Z); no date or type bounds; no screening; dedupe by OpenAlex ID (none needed). Response raw/reception1_top50.json.",'NONE — top 50 citing works taken mechanically from the ranked query','YES','50',None),
('RECENT-1','RECEPTION','How recent (2021-11-04 onward) citing works use AJR 2001.',"OpenAlex works API, filter=cites:W3124166904,from_publication_date:2021-11-04, sort=cited_by_count:desc, per-page=25; population count 3,026. Inspection sample: 6 members drawn with random.Random(20261104).sample(sorted IDs, 6), recorded in lock/RECENT-1_sample.txt at 8:33:36 PM PST (04:33:36Z) before any inspection. Response raw/recent1_top25.json.",'NONE — top 25 recent citing works taken mechanically','YES','25',None),
('ADJUDICATION-1','ADJUDICATION','What tests of field 6 (L1) and of the R1/R2 rivals to L3 exist, and what they find.',"OpenAlex works API, six title_and_abstract.search queries Q1–Q6 (exact strings in lock/ADJUDICATION-1_search_record.md), publication 2001-01-01 to 2026-11-04, type article|preprint, relevance ranking, top 10 per query, dedupe by OpenAlex ID → 58 members; screening codes DIRECT (L1) / DIRECT (L3-R1) / DIRECT (L3-R2) / DIRECT (L3-noSM) / ADJACENT / BACKGROUND / UNRELATED / UNKNOWN from title and abstract.",'SEARCHED — lock/ADJUDICATION-1_search_record.md (raw/adj1_Q1..Q6.json)','NO','58','2026-11-04 8:30:42 PM PST (2026-11-05T04:30:42Z); search record sha256 05ae137a5db11167164e758a2228f8e176f470bc6575b1694ad0de6541f90916')]
for cid,role,q,rule,disc,sel,size,lock in reg:
    P(f"CORPUS ID: {cid}"); P(f"CORPUS ROLE: {role}"); P(f"CORPUS QUESTION: {q}"); P(f"CORPUS SELECTION RULE: {rule}")
    P(f"CORPUS DISCOVERY: {disc}"); P(f"SELECTED ON TARGET CITATION: {sel}"); P(f"CORPUS SIZE: {size}")
    P(f"CITATION CONTEXT COVERAGE: {cid} {INS[cid]}/{size}")
    if lock: P(f"CORPUS LOCK: {lock}")
    P("")
P(f"Overlap. W2994756033 (Rodrik, Subramanian & Trebbi 2004; {RD}) is in RECEPTION-1 and ADJUDICATION-1 (search result ADJ29) and is recorded once with both corpus IDs; its reception rank does not weight its adjudication role. Duplicate database records of one work inside RECEPTION-1: Rodrik ({RD}, {RDW}), Reversal of Fortune ({S('W3125412951')}, {S('W3021593216')}), AJR handbook ({HB}, {HBC}), Levine finance survey ({LEVR}, {LEVC}); each record is a separate member, as the selection rule returned them.\n")
P("Membership differences from v1 (queried 2026-11-04 3:42 AM PST, 11:42Z). RECEPTION-1: 12 new members (W3021593216, W3124948273, W2110434128, W3124568416, W2113844427, W3122300128, W3125412951, W2155346737, W2168966825, W1977433163, W4240669445, W3122357778); 12 v1 members absent (W2131499322, W3193006831, W2891433665, W2090766907, W3121532354, W3123773675, W2889827801, W2113596540, W3126058703, W1511665033, W2103130810, W2107205575). RECENT-1: added W4386028756, W4404201184, W4376140760; dropped W3211527536, W3124497653, W4200071543; population 2,695 → 3,026. The AJR 2001 OpenAlex record now lists 55 referenced works (v1: 13).\n")
P("SOURCE ELIGIBILITY LEDGER\n")
P("| Source | Corpus membership | Question relevance | Relation to target | Evidence contribution | Source access | Citation context | Supported inference |")
P("|---|---|---|---|---|---|---|---|")
for r in rows:
    P(f"| {r['label']} | {r['mem']} | {r['rel']} | {r['relat']} | {r['con']} | {r['acc']} | {r['ctx']} | {r['sup']} |")
P("")
P("Coding notes. Relation for ADJUDICATION-1: OpenAlex reference list contains W3124166904 → CITES-UNINSPECTED; reference list empty → UNKNOWN; non-empty list without AJR → NOT-CITING (NOT-APPLICABLE), except DIRECT members and abstracts naming AJR, which stay UNKNOWN because OpenAlex reference lists are incomplete. Relevance and contribution were coded from abstracts; rows marked \"title-coded from METADATA\" were coded from the title alone. A working-paper version was accepted as the inspected version when it contains the citation; otherwise the row is VERSION-MISMATCH.\n")
P("SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION\n")
P("GRAPH CORPUS AND RECEIPTS\n")
nodes="; ".join(f"{a}={b}" for a,b in sorted(G['node_list'].items()))
P("GRAPH CORPUS DEFINITION: RECEPTION-1 as registered in SECTION A0 (OpenAlex, filter=cites:W3124166904, sort=cited_by_count:desc, top 50, queried 2026-11-05T04:29:45Z UTC = 8:29 PM PST Nov 4, no date or type bounds, no screening, dedupe by OpenAlex ID, inclusion = all 50 returned, exclusion = none). Target W3124166904 is outside the density corpus; the 50 citer -> target edges hold by construction and are not counted.")
P("GRAPH CORPUS NODE LIST: "+nodes)
P("INTERNAL EDGE LIST: "+"; ".join(f"{a} -> {b}" for a,b in edges))
P("DERIVATION MODE: COMPUTED-FROM-RETRIEVED")
P("DENSITY CALCULATION: directed density = directed internal edges u -> v (u, v in N01..N50, u != v, v in OpenAlex referenced_works of u) / n(n-1), n = 50; computed by graph2.py from raw/reception1_top50.json.")
P(f"DENSITY NUMERATOR: {E} directed internal edges among the 50 corpus nodes.")
P("DENSITY DENOMINATOR: 2450 possible directed edges (50 × 49).")
P(f"DENSITY INPUT COVERAGE: 50/50 reference lists obtained from OpenAlex ({G['total_refs']:,} indexed references). No Crossref cross-check in this run.")
P("DENSITY INFERENCE SCOPE: the density result applies only to RECEPTION-1. Because RECEPTION-1 is selected on target citation, it can establish density inside that target-citing corpus; it cannot establish or exclude field-wide, founding-cluster or premise-subnetwork closure. No seed-expanded or matched comparison graph was built.\n")
P("Closure is not established and not excluded beyond the defined corpus.\n")
P(f"Density results. Raw directed density {E}/2450 = {d:.2f}%. Excluding N01 (the conflated Reply/AJR 2001 record, in-degree {indeg['N01']}) gives {len(ex)}/2352 = {dx:.2f}%. {cite_any}/50 nodes cite at least one other corpus node. Reciprocal pairs: {len(recip)}. Internal references are {E}/{G['total_refs']:,} = {E/G['total_refs']*100:.2f}% of all indexed outbound references. In-degree leaders: "+", ".join(f"{a} {b}" for a,b in indeg.most_common(6))+". Excluding N01: "+", ".join(f"{a} {b}" for a,b in indeg_x.most_common(5))+".\n")
P("1. Top 50 most-cited works citing AJR 2001: RECEPTION-1 (Artifact 1 lists the top 15). Relevance composition: "+", ".join(f"{a} {b}" for a,b in sorted(cnt('RECEPTION-1','rel').items()))+".")
P(f"2. Founding cluster: AJR 2001 with AJR-team follow-ups (Reversal of Fortune, the handbook synthesis, the 2012 Reply). {len(team)}/50 RECEPTION-1 records have Acemoglu, Johnson or Robinson as an author ({', '.join(team)}).")
P("3. Founding papers' evidence type: AJR 2001 primary cross-country IV (FULL-TEXT); Reversal of Fortune primary cross-country (ABSTRACT); handbook synthesis (FULL-TEXT, WP version); Reply re-analysis (FULL-TEXT).")
P(f"4. Hubs: AJR-team records receive {tshare}/{E} internal edges ({tshare/E*100:.1f}%); excluding the conflated N01 they receive {toteam_x}/{len(ex)} ({toteam_x/len(ex)*100:.1f}%). Leading node after N01: {indeg_x.most_common(1)[0][0]}.")
P(f"5. Hub substitution: within RECENT-1, Rodrik 2004 is co-cited by {rodrik_recent}/25 and an AJR-team work beyond the target by {len(fc_recent)}/25 (all cite AJR 2001 by construction).")
P(f"6. Small cluster citing itself: no closed cluster inside RECEPTION-1 (density {d:.2f}%).")
P("7. Gatekeeping roles: no editorial or referee data retrieved; UNASSESSED.")
P("8. Self-citation in the founding cluster: ordinary programme self-citation (team records cite each other and N01).")
P("9. Concentration by lab/journal/funder: not assessed beyond authorship (SECTION I).")
P("10. Citation count vs independent confirmation: AJR 2001 cited_by_count 9,952 at retrieval; see DATA-ORIGIN inference I21.\n")
P("SECTION B: EVIDENCE TYPE CODING\n")
P("Every corpus member is coded in the SOURCE ELIGIBILITY LEDGER. Questions 11–16 describe the evidence base only on ADJUDICATION-1, the SEARCHED adjudication corpus; on RECEPTION-1 they describe the citing set.\n")
P("ADJUDICATION-1 composition (evidence base, bounded by the locked search):")
P(comp('I15','ADJUDICATION-1','relevance','rel')); P(comp('I16','ADJUDICATION-1','contribution','con'))
P("RECEPTION-1 composition (citing set only):")
P(comp('I17','RECEPTION-1','relevance','rel'))
a=cnt('ADJUDICATION-1','rel'); ac=cnt('ADJUDICATION-1','con'); ar=Counter(r['rel'] for r in corp('ADJUDICATION-1'))
P(f"\n11. Primary empirical tests in ADJUDICATION-1: {a['DIRECT']} DIRECT members (L1 {ar['DIRECT (L1)']}, L3-R1 {ar['DIRECT (L3-R1)']}, L3-noSM {ar['DIRECT (L3-noSM)']}, L3-R2 {ar['DIRECT (L3-R2)']}); contribution REANALYSIS {ac['REANALYSIS']}, INDEPENDENT-DATA {ac['INDEPENDENT-DATA']}, METHOD {ac['METHOD']}.")
P(f"12. Reviews/syntheses: REVIEW {ac['REVIEW']}, COMMENTARY {ac['COMMENTARY']}.")
P("13. Theory-only: none among DIRECT members.")
P(f"14. Unknown: relevance UNKNOWN {a['UNKNOWN']}, contribution UNKNOWN {ac['UNKNOWN']} (ADJ37, ADJ44 title-only).")
P("15. Evidence-to-claim ratio: within the locked search, re-analyses of the AJR series dominate the DIRECT set; independent-data DIRECT members are the historical-malaria and identification-through-heteroskedasticity papers (ADJ12, ADJ14, ADJ49).")
rc1=cnt('RECEPTION-1','rel')
P(f"16. On RECEPTION-1 the same questions describe citers: DIRECT {rc1['DIRECT']}/50, ADJACENT {rc1['ADJACENT']}/50, BACKGROUND {rc1['BACKGROUND']}/50, UNKNOWN {rc1['UNKNOWN']}/50.\n")
P("SECTION C: CITATION POLARITY AND CLAIM USE\n")
P(f"Citing passages inspected: RECEPTION-1 {k}/50 ({', '.join(r1ins)}); RECENT-1 {INS['RECENT-1']}/25; ADJUDICATION-1 {INS['ADJUDICATION-1']}/58. The instrument's 15-passage target was not reached for RECENT-1 or ADJUDICATION-1. Percentages use inspected citations only.\n")
P(f"17. Supportive: SUPPORTS in {uc['SUPPORTS']}/{k} inspected RECEPTION-1 passages ({uc['SUPPORTS']/k*100:.0f}%).")
P(f"18. Critical: CHALLENGES {uc['CHALLENGES']}/{k}; QUALIFIES {uc['QUALIFIES']}/{k}.")
P(f"19. Perfunctory/background: MENTIONS {uc['MENTIONS']}/{k}; RECENT-1 2/2 inspected passages are MENTIONS.")
P(f"20. Premise use: PREMISE {uc['PREMISE']}/{k}.")
P(f"21. Data/instrument reuse: REUSES {uc['REUSES']}/{k}.")
P("22. Polarity inflation: the self-authored handbook (HB-E1) restates magnitude without the qualifier (SECTION D); inspected independent users preserve proxy wording (DML-E1, HW-E1).\n")
P("SECTION D: CLAIM MUTATION TRACKING\n")
P("23–30. Original (AJR-E2, AJR 2001 PDF p. 20 = AER p. 1387): the 0.94 estimate implies an approximately 7-fold Nigeria–Chile difference, which the authors call an upper bound because of measurement error. Hub restatement (HB-E1, NBER WP 10481 p. 29): \"most of the gap between rich and poor countries today is due to differences in economic institutions\". Construct: the regressor \"average protection against expropriation risk\" is restated as \"enforcement of property rights\" and \"economic institutions\" (HB-E1). Independent users preserve it: DML-E1 \"an index which measures protection against expropriation risk\". Public layer: NP-E1 \"a clear chain of causality\" vs NS-E1 \"taken with a grain of salt\". Severity: moderate at the self-authored hub; preserved by independent users; inflation at the popular layer.\n")
P("| Original source | Original claim | Hub restatement | Downstream restatement | Mutation severity | Note |")
P("|---|---|---|---|---|---|")
P("| AJR 2001 p. 1387 (AJR-E2) | 0.94 implies about a 7-fold gap; an upper bound | HB-E1: most of the gap due to economic institutions | NP-E1: \"a clear chain of causality\" | moderate | self-authored hub; NS-E1 preserves caution |")
P("| AJR 2001 Table 4 regressor | PRS expropriation-risk index | HB-E1: \"enforcement of property rights\" | DML-E1 preserves the index wording | minor | broadening at the hub only |\n")
P("SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT\n")
P("Steps 31–37 reuse the v1 preregistration (reused; lock/section_E_preregistration.md on branch audit/acemoglu-colonial-origins, sha256 84847dd02aca0af819994008ae98d407fae5f75560c8d5de9b628346df965154). Layers L1–L4, rivals R1 and R2, observations O1–O4 and fields F1–F6 are as recorded there. This run adds ADJUDICATION-1, a SEARCHED corpus locked before screening, as the discovery route for DIRECTLY-ADJUDICATING sources.\n")
P("SOURCE-LOCK METHOD: LOCKED QUERY")
P("SOURCE-LOCK DATABASE: OpenAlex works API (reused v1 lock; raw responses on the v1 branch)")
P("SOURCE-LOCK QUERY OR SOURCE LIST: filter=title.search:<terms>,to_publication_date:2000-12-31,type:article with terms F1 \"malaria economic\", F2 \"geography economic development\", F3 \"human capital growth\", F4 \"weak instruments\", F6 \"institutions economic performance\" (reused)")
P("SOURCE-LOCK DATE CUTOFF: 2000-12-31 (publication on or before)")
P("SOURCE-LOCK RANKING RULE: OpenAlex cited_by_count descending at query time")
P("SOURCE-LOCK N: 10 (top 2 per field × 5 fields)")
P("SOURCE-LOCK DEDUPLICATION RULE: by OpenAlex work ID; off-topic items retained and flagged, never replaced")
P("SOURCE-LOCK TIMESTAMP OR HASH: 2026-11-04T11:42:25Z (3:42:25 AM PST, reused); preregistration sha256 84847dd02aca0af819994008ae98d407fae5f75560c8d5de9b628346df965154\n")
P("Flip test (step 37): PASS (reused): F1, F2 from R1; F3 from R2; F4 from both. Innocent explanations as in v1: scope mismatch for F1 exemplars; disciplinary boundary and timing for F3; missing weak-IV methods route to lack of decisive tests.\n")
P("Falsification-relevant literature preregistration table:\n")
P("| Claim layer | Audited explanation | Strongest plausible rival explanation | Adjudicating observation | Candidate field | Generated from audited claim, rival, or both? | Measurement relevance | Adjudicative capacity | Independence | Publication-date cutoff | Historically available? | Flip-test result | Source-lock method | Lock timestamp / hash | Final engagement classification |")
P("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
for row in [("L1/L3","colonial institutions (expropriation-risk proxy) drive income","R1 direct disease channel","O1 disease effects with institutions fixed","F1 malaria economics","rival","disease burden","could weaken L3","independent","2000-12-31","yes","PASS","LOCKED QUERY (reused)","84847dd0…5154","direct substantive engagement (AJR-E4)"),
 ("L1/L3","as above","R1 direct geography channel","O2 geography conditional on institutions","F2 geography","rival","geographic correlates","could weaken L3","independent","2000-12-31","yes","PASS","LOCKED QUERY (reused)","as above","direct substantive engagement (geography controls)"),
 ("L3","as above","R2 settler human capital","O3 decomposition","F3 human capital","rival","schooling effects","could weaken L3","independent","2000-12-31","partly","PASS","LOCKED QUERY (reused)","as above","no located engagement (theory exemplars; timing)"),
 ("L1/L2","as above","weak or noisy instrument","O4 2SLS reliability","F4 weak-IV econometrics","both","inferential validity","could narrow L1/L2","independent","2000-12-31","yes","PASS","LOCKED QUERY (reused)","as above","citation without substantive engagement"),
 ("L1","as above","not a rival","construct definition","F6 institutional measurement","audited claim","defines regressor","construct-defining","partly shared provider","2000-12-31","yes","PASS","LOCKED QUERY (reused)","as above","direct substantive engagement (Knack–Keefer)")]:
    P("| "+" | ".join(row)+" |")
P("\nAdjacent-literature neglect table:\n")
NEH="| Claim layer | Adjacent field | Nominated source and stable identifier | Verification state | Source class: CONSTRUCT-DEFINING / MECHANISM-SUPPORTING / DIRECTLY-ADJUDICATING | Actual result | Explanation favored | Explanation weakened | Precise revision required | Pre-inspection lock status or POST HOC | Cited by dominant cluster? | Engagement quality | Effect of omission |"
NE=[("L3","F1 malaria","X06 W139828295","ABSTRACT-CONFIRMED","MECHANISM-SUPPORTING","household malaria spending","—","—","—","LOCKED (reused)","no","not cited","minor context loss"),
("L3","F1 malaria","X07 W2088758477","ABSTRACT-CONFIRMED","MECHANISM-SUPPORTING","socio-economic malaria risk factors","—","—","—","LOCKED (reused)","no","not cited","minor context loss"),
("L1/L3","F2 geography","X08 W2618788771 Gallup–Sachs–Mellinger","ABSTRACT-CONFIRMED","MECHANISM-SUPPORTING","geography correlates with income","—","—","—","LOCKED (reused)","yes (AJR 2001)","directly tested against","minor context loss"),
("L3","F2 geography","X09 W1492460295","ABSTRACT-CONFIRMED","MECHANISM-SUPPORTING","geography in development theory","—","—","—","LOCKED (reused)","no","not cited","minor context loss"),
("L3","F3 human capital","X10 W3121822366","ABSTRACT-CONFIRMED","MECHANISM-SUPPORTING","human-capital growth theory","—","—","—","LOCKED (reused)","no","not cited","minor context loss"),
("L3","F3 human capital","X11 W2035652178","ABSTRACT-CONFIRMED","MECHANISM-SUPPORTING","schooling-finance growth model","—","—","—","LOCKED (reused)","no","not cited","minor context loss"),
("L1/L2","F4 weak-IV","X12 W2165144879 Staiger–Stock","ABSTRACT-CONFIRMED","CONSTRUCT-DEFINING","weak-instrument asymptotics","—","—","—","LOCKED (reused)","no","not cited","moderate weakness (routes to lack of decisive tests)"),
("L1/L2","F4 weak-IV","X13 W1980412904 Bound–Jaeger–Baker","ABSTRACT-CONFIRMED","CONSTRUCT-DEFINING","weak IV biased toward OLS","—","—","—","LOCKED (reused)","yes (AJR-E3)","cited in passing","minor context loss"),
("L1","F6 measurement","X14 W3121147769 North 1990 record","ABSTRACT-CONFIRMED","CONSTRUCT-DEFINING","definition of institutions","—","—","—","LOCKED (reused)","other North works cited","not cited","minor context loss"),
("L1","F6 measurement","X15 W2010235856 Knack–Keefer","ABSTRACT-CONFIRMED","CONSTRUCT-DEFINING","ICRG/BERI indices predict growth","—","—","—","LOCKED (reused)","yes (AJR 2001)","substantively engaged","minor context loss"),
("L3","R1 test","ADJ38 W2001123479 Carstensen–Gundlach","ABSTRACT-CONFIRMED; CONTESTED","DIRECTLY-ADJUDICATING","abstract: malaria has a direct income effect alongside institutions","R1","L3 strong form","L3: institutions a major channel; direct disease channel not excluded","LOCKED (ADJUDICATION-1 search)","UNASSESSED (later AJR-team reference lists not traced)","UNASSESSED because retrieval was insufficient","moderate weakness"),
("L3","R1 test","X03 Sachs 2003 NBER w9490","FULL-TEXT-CONFIRMED; CONTESTED","DIRECTLY-ADJUDICATING","AJR-style null rejected with malaria risk (SA-E1)","R1","L3 strong form","as above","POST HOC","UNASSESSED","UNASSESSED because retrieval was insufficient","moderate weakness"),
("L3","R2 test",f"{GL} W2890314743 Glaeser et al. 2004","FULL-TEXT-CONFIRMED; CONTESTED","DIRECTLY-ADJUDICATING","malaria risk significant alongside settler mortality; human-capital channel (GL-E1, GL-E2)","R1 and R2","L3 strong form","L3: institutions or settler human capital, not separately identified","POST HOC (RECEPTION-1 member; not returned by the locked search)","acknowledged in NS-E3","UNASSESSED because retrieval was insufficient","moderate weakness")]
P(NEH); P("|"+"---|"*13)
for row in NE: P("| "+" | ".join(row)+" |")
P("\nThe source layer engages R1 directly (AJR-E4: malaria controls). Dominant-cluster engagement with the later R1/R2 tests was not traced in this run, so the dimension is scored on the source layer only (ENGAGEMENT I19); POST HOC rows anchor nothing.\n")
P("SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING\n")
P(f"40. Hubs: Rodrik et al. 2004 ({RD}/{RDW}; independent) and the AJR handbook ({HB}/{HBC}; self-authored). In-degree inside RECEPTION-1: {RD} {indeg[RD]}, {RDW} {indeg[RDW]}, {HB} {indeg[HB]}, {HBC} {indeg[HBC]}.")
P(f"41. Recent papers citing the hub: Rodrik {rodrik_recent}/25 in RECENT-1; handbook records {hb_recent}/25.")
P("42. Recent papers citing primary evidence directly: 25/25 by construction.")
P("43. Hub substitution for inspection: not measurable from reference lists; no downstream passage citing the handbook was inspected (I23 NOT-ASSESSED).")
P("44–45. Accuracy: Rodrik accurate and critical of interpretation (RD-E4); handbook drops the upper-bound qualifier (HB-E1 vs AJR-E2).")
P("46. Adjacent literatures in hubs: both engage geography.")
P("47. Hub as substitute for primary evidence: UNASSESSED.\n")
P("| Hub paper | Recent papers citing hub | Recent papers citing primary evidence directly | Adjacent-field citation rate | Hub accuracy | Hub risk |")
P("|---|---|---|---|---|---|")
P(f"| Rodrik, Subramanian & Trebbi 2004 ({RD}) | {rodrik_recent}/25 RECENT-1 | 25/25 by construction | Glaeser co-cited by {gl_recent}/25 RECENT-1; 225/3,026 recent AJR citers | accurate; critical of interpretation | low |")
P(f"| AJR handbook ({HB}, {HBC}) | {hb_recent}/25 RECENT-1 | 25/25 by construction | as above | qualifier dropped; construct broadened | moderate (downstream reliance not traced) |\n")
P("SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR\n")
P("48. Proxy treated as construct: at the self-authored hub (HB-E1), not by inspected independent users (DML-E1, HW-E1).")
P("49. Export from low-stakes settings: not applicable; the counterfactual is bounded by the authors (AJR-E2).")
P("50. Ignored natural experiments: no; within-country designs appear in RECEPTION-1.")
P("51. Model updating: the Reply defends the model against Albouy (p. 3078); updating vs defence is CONTESTED.")
P("52. Intervention expansion: no intervention claim; N/A.")
P("53–55. Falsification criteria stated via the exclusion restriction and controls (AJR-E4); 55 N/A.")
P("56. Expansion over testing: not assessed.\n")
P("Ratchet scoring route. Intervention-evidence ratchet: N/A (no intervention claim). Model non-updating four-link gate: link 1 met; link 2 (verified later disconfirming evidence) not reached — Albouy and the R1/R2 tests are CONTESTED; links 3–4 not traced. The dimension is UNASSESSED.\n")
P("SECTION H: IGNORED CRITIQUE AND NON-UPTAKE\n")
P("1. Precondition: critique production strongly expected (AER lead article; cited_by_count 9,952; Nobel 2024).")
P("2. Retrieval: Albouy 2012 (X02, FULL-TEXT); Glaeser et al. 2004 (GL-E1, GL-E2); Sachs 2003 (SA-E1).")
P("3. Reception opportunity: verified for Albouy (Reply in the same AER issue, p. 3078).")
P(f"4. Uptake in the uptake population: the Reply ({REPLY}) engages Albouy substantively (ENGAGEMENT I18). Glaeser uptake by the AJR team not traced (I22 NOT-ASSESSED). Co-citation alone carries no score: Albouy 72/3,026 and Glaeser 225/3,026 recent AJR citers (I20, descriptive).\n")
P("57. Serious critiques: Albouy 2012; Glaeser et al. 2004; Sachs 2003; Rodrik et al. 2004 on interpretation.")
P("58. Cited by the dominant cluster: Albouy yes (Reply); others not traced.")
P("59. Mode: engaged and contested (Albouy).")
P("60. Network update: partial at the scientific-summary layer (NS-E1).")
P("61. Recent papers: 2/2 inspected passages use AJR as background.")
P("62–63. Practitioner warnings: not searched; UNASSESSED.\n")
CRH="| Expected-production precondition | Critique / contrary evidence | Year | Source type | Main objection | Verification state | Reception opportunity | Cited by dominant cluster? | Uptake status | Dimension disposition | Effect on consensus |"
CR1="| strong | Albouy, AER Comment (X02, W1969918011) | 2012 | formal comment | settler-mortality data construction | FULL-TEXT-CONFIRMED; CONTESTED | verified | yes (Reply p. 3078); 72/3,026 recent AJR citers | substantively engaged by the cluster | SCORED 0 | answered; scientific summary cautious (NS-E2) |"
CR2=f"| strong | Glaeser et al. ({GL}) | 2004 | primary empirical | human capital; disease environment | FULL-TEXT-CONFIRMED; CONTESTED | verified | UNASSESSED; 225/3,026 recent AJR citers | UNASSESSED | not scored separately | acknowledged in NS-E3 |"
P(CRH); P("|"+"---|"*11); P(CR1); P(CR2); P("")
P("SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING\n")
P(f"64. Recurring authors: AJR-team authorship on {len(team)}/50 RECEPTION-1 records (I03), including duplicate records of two team works.")
P("65–67. Venues, institutions, funding: not re-derived; UNASSESSED.")
P("68. Dissent venues: Albouy and the Reply in the AER; Glaeser et al. and Rodrik et al. in the Journal of Economic Growth.")
P("69–70. Gatekeeping and ideology: not assessable.\n")
P("Closure type: normal clustering around a canonical paper inside RECEPTION-1; no author, journal, funding or advocacy closure established.\n")
P("SECTION J: FALSE-POSITIVE AND BASELINE CHECK\n")
P("71. Small field: no. 72. Baseline comparison: none built. 73. Adjacent expertise: the source engages geography and malaria (AJR-E4). 74. Only people studying the question: no; DIRECT members come from many teams. 75. Strong primary evidence: yes for the estimate; conditional for causal and construct readings. 76. Repeated independent tests: tests exist (24/58 DIRECT) but most reuse the AJR series (I21). 77. Limitations preserved: lost at the self-authored hub and popular layer; preserved by inspected independent users. 78–80. Failed predictions acknowledged, critics engaged, updating via comment-and-reply: yes.\n")
P("Answers are mostly yes; this is not a cartel signature.\n")
P("SECTION J2: THE CONCEDE TEST\n")
P("| Finding | Declared target claim | Matches map field 6? | Same mechanism as another row? | Count separately? |")
P("|---|---|---|---|---|")
for r in [("1 Database record instability","the OpenAlex record and reception corpora of AJR 2001","no — MAP GAP: this finding targets the retrieval record, not map field 6","no","yes"),
("2 Shared data origin of re-estimates","L3: independent confirmation","no — MAP GAP: this finding targets L3, not map field 6","no","yes"),
("3 Hub qualifier loss and construct broadening","L3 restatement of the field-6 magnitude","no — MAP GAP: this finding targets the hub restatement","yes — proxy mismatch and claim mutation share HB-E1","no — counted once (proxy mismatch NESTED)"),
("4 Direct tests exist and conflict","L3 and field-6 robustness","partly","no","yes"),
("5 Albouy critique engaged by the cluster","field 6","yes","no","yes"),
("6 No closure inside RECEPTION-1","field 6 network support","yes","no","yes"),
("7 Recent citers use AJR as background","field 6 network support","yes","no","yes")]: P("| "+" | ".join(r)+" |")
P("\n| Finding | Concede test: SURVIVES / NARROWS / DEFEATS | Surviving claim if NARROWS |")
P("|---|---|---|")
for r in [("1","SURVIVES","—"),("2","NARROWS (against L3; SURVIVES against field 6)","several teams obtain similar estimates with the AJR series"),("3","NARROWS (against the restatement; SURVIVES against field 6)","0.94 implies up to about a 7-fold gap, an upper bound"),("4","NARROWS (against L3; field 6 SURVIVES as an estimate)","institutions a major channel; direct disease effects not excluded"),("5","SURVIVES","—"),("6","SURVIVES","—"),("7","SURVIVES","—")]: P("| "+" | ".join(r)+" |")
P("\n| Finding | Scope-loss level | Original claim | Surviving claim | What epistemic or practical work is lost? |")
P("|---|---|---|---|---|")
P("| 2 | material | independent work confirms institutions explain income differences | similar estimates on one shared data origin | independence of confirmation |")
P("| 3 | material (restatement); incidental (field 6) | most of the gap due to economic institutions | up to about 7-fold, an upper bound | magnitude used in counterfactuals |")
P("| 4 | material (L3) | institutions, not geography or disease, are the fundamental cause | institutions a major channel; rivals CONTESTED | exclusivity of the institutional explanation |\n")
P("No finding DEFEATS field 6.\n")
P("SECTION K0: EVIDENCE SUFFICIENCY LEDGER\n")
P("Gate B was applied to every inference before any score or finding used it. Inferences that fail stay listed with what would make them sufficient.\n")
INF=[
("I01","GRAPH-STRUCTURE","RECEPTION-1","CORPUS","EXHAUSTIVE","ALL","SUPPORTED",f"Directed internal density {E}/2450 = {d:.2f}% (50/50 reference lists); no closed cluster inside RECEPTION-1."),
("I02","GRAPH-STRUCTURE","RECEPTION-1","CORPUS","EXHAUSTIVE","ALL","SUPPORTED",f"AJR-team records ({len(team)}/50) receive {tshare}/{E} internal edges; {indeg['N01']} go to the conflated N01; excluding N01, team records receive {toteam_x}/{len(ex)}."),
("I03","DATABASE-RECORD","RECEPTION-1","CORPUS","EXHAUSTIVE","ALL","SUPPORTED",f"{len(team)}/50 members list Acemoglu, Johnson or Robinson as author; 4 works appear as two records each."),
("I04","GRAPH-STRUCTURE","RECENT-1","CORPUS","EXHAUSTIVE","ALL","SUPPORTED",f"{len(fc_recent)}/25 members cite at least one AJR-team work beyond the target ({', '.join(fc_recent)}); {25-len(fc_recent)}/25 cite none."),
("I05","CITATION-USE","RECENT-1","WITHIN-SAMPLE","CONVENIENCE",f"{S('W4292663674')}, {S('W4391180104')}","SUPPORTED-WITHIN-SAMPLE","Both inspected passages cite AJR 2001 as background (theory list; endogeneity precedent), not the field-6 estimate; 2 of 6 randomly drawn members were retrievable, so the inspected subset is CONVENIENCE."),
("I06","CITATION-USE","RECENT-1","CORPUS","PRESPECIFIED-RANDOM",", ".join(SAMP),"INSUFFICIENT","How RECENT-1 uses AJR 2001 cannot be estimated: 4/6 sampled full texts were not retrieved (HTTP 403 for three, 500 for one). Sufficient if all 6 sampled passages were inspected."),
("I07","CITATION-USE","RECEPTION-1","WITHIN-SAMPLE","CONVENIENCE",", ".join(r1ins),"SUPPORTED-WITHIN-SAMPLE",f"Among {k} inspected passages: SUPPORTS {uc['SUPPORTS']}, PREMISE {uc['PREMISE']}, QUALIFIES {uc['QUALIFIES']}, CHALLENGES {uc['CHALLENGES']}, MENTIONS {uc['MENTIONS']}; reuse of AJR data or instrument in {uc['REUSES']}."),
("I08","RESTATEMENT","—","NAMED","NOT-APPLICABLE",f"X01, {HB}","SUPPORTED","HB-E1 restates the AJR-E2 magnitude implication without the authors' upper-bound qualifier."),
("I09","RESTATEMENT","—","NAMED","NOT-APPLICABLE",f"X01, {HB}","SUPPORTED","HB-E1 restates the expropriation-risk regressor as enforcement of property rights and economic institutions."),
("I10","CITATION-USE","—","NAMED","NOT-APPLICABLE",f"{DML}, {HW}","SUPPORTED","Independent users preserve the proxy: DML-E1 names the expropriation-risk index; HW-E1 calls the geography finding disputed."),
("I11","SOURCE-RESULT","—","NAMED","NOT-APPLICABLE",f"ADJ01, ADJ05, ADJ09, ADJ18, ADJ38, {GL}, X02, X03","SUPPORTED","Named direct tests of field 6 (ADJ01, ADJ05, X02) and of the R1/R2 rivals (ADJ09, ADJ18, ADJ38, X03, Glaeser) exist with stated results."),
("I12","SOURCE-RESULT","—","NAMED","NOT-APPLICABLE",f"ADJ09, ADJ18, ADJ38, X03, {GL}, {RD}, {EL}","SUPPORTED","Results conflict: geography or malaria keeps direct effects in ADJ09, ADJ18, ADJ38, Sachs and Glaeser; institutions dominate in Rodrik and Easterly–Levine."),
("I13","ABSENCE","ADJUDICATION-1","WITHIN-SAMPLE","EXHAUSTIVE","SCREENED","SUPPORTED-WITHIN-SAMPLE","No DIRECT (L3-R2) human-capital decomposition test among 56/58 screened members; Glaeser 2004, outside the search bound, is one. Not used to score."),
("I14","ABSENCE","ADJUDICATION-1","LITERATURE","EXHAUSTIVE","ALL","INSUFFICIENT","No cross-country re-estimate of field 6 with an instrument independent of the AJR series exists. Insufficient: ADJ37 and ADJ44 unscreened; sufficient once screened and none qualifies."),
("I15","COMPOSITION","ADJUDICATION-1","CORPUS","EXHAUSTIVE","ALL","SUPPORTED","Relevance composition of the evidence base within the locked search."),
("I16","COMPOSITION","ADJUDICATION-1","CORPUS","EXHAUSTIVE","ALL","SUPPORTED","Contribution composition within the locked search."),
("I17","COMPOSITION","RECEPTION-1","CORPUS","EXHAUSTIVE","ALL","SUPPORTED","Relevance composition of the citing set; describes citers, not the evidence base."),
("I18","ENGAGEMENT","—","NAMED","NOT-APPLICABLE",REPLY,"SUPPORTED","The Reply substantively answers Albouy's two data objections (p. 3078) and re-estimates on revised data."),
("I19","ENGAGEMENT","—","NAMED","NOT-APPLICABLE","X01","SUPPORTED","AJR 2001 engages the R1 malaria/geography rival directly with controls (AJR-E4)."),
("I20","CO-CITATION","POPULATION","POPULATION","NOT-APPLICABLE","UNSCREENED","SUPPORTED","Among recent AJR citers, Albouy 2012 is co-cited by 72/3026 and Glaeser 2004 by 225/3026 (OpenAlex counts); co-citation, not use."),
("I21","DATA-ORIGIN","—","NAMED","NOT-APPLICABLE",f"{RD}, {EL}, {DML}, {REPLY}","SUPPORTED","Rodrik, Easterly–Levine, Chernozhukov et al. and the Reply all use the AJR settler-mortality series (RD-E1, EL-E2, DML-E1)."),
("I22","ENGAGEMENT","—","NAMED","NOT-APPLICABLE","—","NOT-ASSESSED","AJR-team uptake of the Glaeser human-capital critique. Not assessed: the AJR-team response noted in NS-E3 was not retrieved; sufficient with its full text."),
("I23","RESTATEMENT","—","NAMED","NOT-APPLICABLE","—","NOT-ASSESSED","Downstream works restate AJR via the handbook. Not assessed: no handbook-citing passage was inspected; sufficient with inspected passages from a defined hub-citing set."),
("I24","DATABASE-RECORD","—","NAMED","NOT-APPLICABLE","X01","SUPPORTED","The AJR 2001 OpenAlex record changed between runs about 17 hours apart: referenced works 13 → 55; RECEPTION-1 differs from v1 in 12/50 members; RECENT population 2695 → 3026."),
]
P("INFERENCE LEDGER\n")
P("| Inference | Class | Corpus | Claimed scope | Sampling rule | Members used | Disposition | Statement |")
P("|---|---|---|---|---|---|---|---|")
for r in INF: P("| "+" | ".join(r)+" |")
P("")
P(comp('I15','ADJUDICATION-1','relevance','rel')); P(comp('I16','ADJUDICATION-1','contribution','con')); P(comp('I17','RECEPTION-1','relevance','rel'))
P("\nWithheld inferences: I06 (INSUFFICIENT: sample attrition), I14 (INSUFFICIENT: 2 unscreened members), I22 and I23 (NOT-ASSESSED). I13 passes within the search bound but is not used to score, because a known R2 test lies outside the bound.\n")
P("DIMENSION EVIDENCE BASIS\n")
P("DIMENSION CLASS MAP: cn7-map-2\n")
P("| Scorecard dimension | Scorecard disposition | Inference IDs | Basis note |")
P("|---|---|---|---|")
DIM=[("Founding-cluster dominance","SCORED 1","I02 (+), I03 (+)","team records draw most internal edges, inflated by the conflated N01; authorship 12/50"),
("Internal citation density","SCORED 0","I01 (-)","low density inside RECEPTION-1 only; closure not excluded beyond it"),
("Recent-paper dependence","SCORED 1","I04 (+), I05 (-)",f"{len(fc_recent)}/25 cite team works beyond the target; inspected uses are background (2 passages)"),
("Review-hub laundering","UNASSESSED","—","I23 NOT-ASSESSED: downstream reliance on the handbook not traced"),
("Proxy mismatch","SCORED 1","I09 (+), I10 (-)","broadening at the self-authored hub; independent users preserve the proxy; NESTED under claim mutation"),
("Claim mutation","SCORED 1","I08 (+)","qualifier loss at the self-authored hub"),
("Adjacent-field neglect","SCORED 0","I19 (-)","source layer engages R1; cluster engagement with later R1/R2 tests not traced"),
("Lack of decisive tests","SCORED 0","I11 (-)","named direct tests exist; their results conflict (I12); bounded absence I13 not used"),
("Poor critique uptake","SCORED 0","I18 (-)","Albouy answered by the Reply; Glaeser uptake not traced (I22)"),
("Intervention-evidence ratchet","N/A","—","no intervention claim at field 6 or in the traced network"),
("Model non-updating","UNASSESSED","—","four-link gate: link 2 not verified (disconfirming evidence CONTESTED); links 3–4 not traced")]
for r in DIM: P("| "+" | ".join(r)+" |")
P("\nFINDING EVIDENCE BASIS\n")
P("| Finding | Finding status | Inference IDs |")
P("|---|---|---|")
for r in [("Finding 1","confirmed","I24, I03"),("Finding 2","confirmed","I21"),("Finding 3","confirmed","I08, I09"),("Finding 4","contested","I11, I12, I15"),("Finding 5","confirmed","I18, I20"),("Finding 6","confirmed","I01, I02"),("Finding 7","provisional","I04, I05, I06")]: P("| "+" | ".join(r)+" |")
P("")
NOFM=f"Verified scored-dimension risk: {rate:.1f}%, calculated from 7 independent scored dimensions; 1 additional scored dimensions are NESTED; 8 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth."
BAND="WITHHELD — label-essential: the healthy/low-risk band needs affirmative no-concern evidence on closure-establishing dimensions; claim mutation is SCORED 1, review-hub laundering UNASSESSED, density bounded to a target-selected corpus."
MECH="self-authored hub qualifier loss (HB-E1) on a shared data origin; no closure signature inside RECEPTION-1"
P("SECTION K: CARTEL-RISK SCORING\n")
P("Scores are in Artifact 8. Proxy mismatch rests on the same HB-E1 passage that owns claim mutation, so it is NESTED under Claim mutation. Founding-cluster dominance and internal density use the same RECEPTION-1 edge list but answer different questions (in-edge concentration plus authorship records vs overall density) and are kept INDEPENDENT.\n")
P(f"- Verified risk score: {X}/{Y}")
P(f"- Verified scored-dimension risk rate: {rate:.1f}")
P("- Independent scored dimensions: 7")
P("- Nested scored dimensions: 1")
P(f"- Verified risk denominator: {Y}")
P("- Evidentiary coverage: 8/10 applicable dimensions scored (80%)")
P("- Execution completeness: 10/10 applicable dimensions completed (100%)")
P("- Dimension inventory: 7 INDEPENDENT SCORED + 1 NESTED SCORED + 0 UNINFORMATIVE + 2 UNASSESSED + 1 N/A = 11 total dimensions; 10 applicable")
P("- Unscored dimensions: Review-hub laundering — UNASSESSED (I23 not assessed); Model non-updating — UNASSESSED (four-link gate not traced); Intervention-evidence ratchet — N/A (no intervention claim)\n")
P(NOFM+"\n")
P("Formal-label gate: coverage 8/10 (80%) declared; 7/10 (70%) if the recent-paper dependence review item is withdrawn; both meet the PROVISIONAL 70% threshold (engineering threshold, not validated). Label-essential check: the arithmetic position is the healthy/low-risk band, which needs affirmative no-concern evidence on the dimensions that could establish closure. Claim transmission carries a SCORED 1 concern, review-hub laundering is UNASSESSED, and density is affirmative only inside a corpus selected on target citation. The band is withheld.\n")
P("ARITHMETIC BAND POSITION: 0%–20% (healthy or low-risk network)")
P("RISK BAND: "+BAND)
P("MECHANISM LABEL: "+MECH+"\n")
P("ARTIFACT 1: TOP 15 CITATION SPINE TABLE\n")
P("| Rank | Paper | Year | Citation count | Evidence type | Role in network | Source of citation count |")
P("|---:|---|---:|---:|---|---|---|")
rowmap={r['w']:r for r in rows}
ET={'REANALYSIS':'secondary analysis','REVIEW':'review article','INDEPENDENT-DATA':'primary empirical study','THEORY':'theoretical / conceptual paper','METHOD':'methodological paper','UNKNOWN':'unclear / needs source audit','SHARED-DATA':'primary empirical study (shared data)','COMMENTARY':'commentary'}
for i,x in enumerate(r1[:15],1):
    w=W(x['id']); r=rowmap[w]; au=', '.join(a_['author']['display_name'] for a_ in x['authorships'][:3])
    P(f"| {i} | {r['sid']} {au}: {x['display_name'][:70].replace('|','/')} ({w}) | {x['publication_year']} | {x['cited_by_count']} | {ET.get(r['con'],r['con'])} | {r['rel']}; {r['relat']} | OpenAlex cited_by_count, query 2026-11-05T04:29Z UTC (raw/reception1_top50.json) |")
P("\nN01's count is inflated by conflation of the Reply record with AJR 2001 (Finding 1).\n")
P("ARTIFACT 2: FOUNDING CLUSTER TABLE\n")
P("| Paper | Year | Claim introduced | Evidence type | Verification state | Later role | Risk |")
P("|---|---|---|---|---|---|---|")
P("| AJR, Colonial Origins (W3124166904, X01) | 2001 | settler mortality instrument; 0.94 effect | primary empirical test | FULL-TEXT-CONFIRMED | canonical source | low for field 6 |")
P(f"| AJR, Reversal of Fortune ({S('W3125412951')}, {S('W3021593216')}) | 2002 | reversal of pre-colonial prosperity | primary empirical study | ABSTRACT-CONFIRMED | cited beyond target in RECENT-1 | low |")
P(f"| AJR, Institutions as a Fundamental Cause ({HB}, {HBC}) | 2004/2005 | synthesis | review article | FULL-TEXT-CONFIRMED (WP version) | self-authored hub | moderate (HB-E1) |")
P(f"| AJR, Reply to Albouy ({REPLY}) | 2012 | defence of data choices | secondary analysis | FULL-TEXT-CONFIRMED | answers Albouy; record conflated | low |\n")
P("ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE\n")
P("\"Cites founding cluster?\" means beyond AJR 2001 (all cite it by construction). \"Cites adjacent fields?\" means Glaeser 2004 or Albouy 2012 in the OpenAlex reference list.\n")
P("| Recent paper | Year | Verification state | Cites founding cluster? | Cites hub? | Cites adjacent fields? | New evidence or recycling? |")
P("|---|---:|---|---|---|---|---|")
recd={r[0]:r for r in rec}
for x in rc:
    w=W(x['id']); r=rowmap[w]; t=recd[w]
    vs='FULL-TEXT-CONFIRMED (passage inspected)' if r['ctx']=='INSPECTED' else ('RECEPTION-CONFIRMED; ABSTRACT-CONFIRMED' if r['acc'].startswith('ABSTRACT') else 'RECEPTION-CONFIRMED; LOCATED')
    fc=('yes ('+', '.join(t[2])+')') if t[2] else 'AJR 2001 only'
    adj=', '.join([s_ for s_,f_ in (('Glaeser 2004',t[4]),('Albouy 2012',t[5])) if f_]) or 'no'
    new='background use (inspected)' if r['ctx']=='INSPECTED' else ('new evidence on another question (abstract)' if r['acc'].startswith('ABSTRACT') else 'not determined (metadata only)')
    P(f"| {r['sid']} {x['display_name'][:70].replace('|','/')} ({w}) | {x['publication_year']} | {vs} | {fc} | {'Rodrik 2004' if t[3] else 'no'} | {adj} | {new} |")
P(f"\nRECENT-1 summary: founding cluster beyond target {len(fc_recent)}/25; Rodrik {rodrik_recent}/25; Glaeser {gl_recent}/25; Albouy {al_recent}/25.\n")
P("ARTIFACT 4: CITATION POLARITY TABLE\n")
P("| Citing paper | Cited paper | Verification state | Citation polarity | Claim use | Inflation risk |")
P("|---|---|---|---|---|---|")
for c,p,u,ri in [(f"{REPLY} AJR Reply 2012","supportive","defence and re-estimation (p. 3078)","low"),(f"{RD}/{RDW} Rodrik et al.","supportive","instrument adopted (RD-E1); interpretation criticised (RD-E4)","low"),(f"{GL} Glaeser et al.","critical","rival tests (GL-E1, GL-E2)","none"),(f"{HB}/{HBC} AJR handbook","used as premise","magnitude without qualifier (HB-E1)","moderate"),(f"{DML} Chernozhukov et al.","supportive","reuses the 64 observations (DML-E1)","low"),(f"{EL} Easterly–Levine","supportive","uses AJR settler-mortality data (EL-E2)","low"),(f"{HW} Hanushek–Woessmann","neutral/background","\"remains a disputed subject\" (HW-E1)","none"),(f"{LEVR}/{LEVC} Levine","neutral/background","background list","none"),(f"{DJO} Dell–Jones–Olken","neutral/background","background","none"),(f"{HID} Hidalgo et al.","neutral/background","numbered background list p. 2","none"),(f"{RZ} Rajan–Zingales","perfunctory","reference list only","none"),(f"{S('W4292663674')} recent","neutral/background","background theory list","none"),(f"{S('W4391180104')} recent","neutral/background","endogeneity precedent","none"),("X05 Nobel popular 2024","inflated","\"a clear chain of causality\" (NP-E1)","moderate"),("X04 Nobel scientific 2024","supportive","\"grain of salt\" (NS-E1)","none")]:
    P(f"| {c} | AJR 2001 | FULL-TEXT-CONFIRMED | {p} | {u} | {ri} |")
P("\nNo Semantic Scholar contexts were used.\n")
P("ARTIFACT 5: CLAIM MUTATION TABLE\n")
P("| Original source | Original claim | Verification state | Hub restatement | Downstream restatement | Mutation severity |")
P("|---|---|---|---|---|---|")
P("| AJR 2001 p. 1387 (AJR-E2) | 0.94 implies about a 7-fold gap; an upper bound | FULL-TEXT-CONFIRMED | HB-E1: most of the gap due to economic institutions | NP-E1: \"a clear chain of causality\" | moderate |")
P("| AJR 2001 Table 4 regressor | PRS expropriation-risk index | FULL-TEXT-CONFIRMED | HB-E1: \"enforcement of property rights\" | DML-E1 preserves the index wording | minor |")
P("| AJR 2001 Table 7 (AJR-E4) | malaria controls do not change results | FULL-TEXT-CONFIRMED | EL-E1: no direct germ effect beyond institutions | HW-E1: \"remains a disputed subject\" | none |\n")
P("ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE\n")
P("Preregistration table: as in SECTION E (reused v1 lock). POST HOC rows anchor no score.\n")
P(NEH); P("|"+"---|"*13)
for row in NE: P("| "+" | ".join(row)+" |")
P("")
P("ARTIFACT 7: CRITIQUE-UPTAKE TABLE\n")
P(CRH); P("|"+"---|"*11); P(CR1); P(CR2); P("")
P("ARTIFACT 8: CARTEL-RISK SCORECARD\n")
P("| Dimension | Applicability | Dimension disposition | Score if SCORED | Evidence / claim state | Evidence supporting disposition and score | Evidence identifiers | Retrieval coverage | AGGREGATION STATUS | Independent evidence and inferential work, or nesting rationale | Reason excluded from denominator | Effect on formal-label gate |")
P("|---|---|---|---|---|---|---|---|---|---|---|---|")
for r in [("Founding-cluster dominance","applicable","SCORED 1","1","RECEPTION-CONFIRMED",f"team records receive {tshare}/{E} internal edges ({toteam_x}/{len(ex)} excluding N01); 12/50 team-authored","I02; I03","50/50 reference lists","INDEPENDENT","in-edge concentration and authorship records","—","counts toward coverage"),
("Internal citation density","applicable","SCORED 0","0","RECEPTION-CONFIRMED",f"{E}/2450 = {d:.2f}%","I01","50/50 inputs","INDEPENDENT","overall density","—","affirmative inside RECEPTION-1 only"),
("Recent-paper dependence","applicable","SCORED 1","1","RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (2 passages)",f"{len(fc_recent)}/25 cite team works beyond target; 2/2 inspected uses background","I04; I05","25/25 reference lists; 2/25 passages","INDEPENDENT","recent corpus distinct from RECEPTION-1","—","counts toward coverage; under review"),
("Review-hub laundering","applicable","UNASSESSED","—","—","downstream hub reliance not traced","I23","0 hub-citing passages","—","—","UNASSESSED","label-essential for the healthy band; band withheld"),
("Proxy mismatch","applicable","SCORED 1","1","CROSS-SOURCE-CONFIRMED","HB-E1 broadens the construct; DML-E1, HW-E1 preserve it","I09; I10","hub and 2 independent texts","NESTED under Claim mutation","shares the HB-E1 passage with claim mutation","excluded from aggregate as NESTED","counts toward coverage"),
("Claim mutation","applicable","SCORED 1","1","CROSS-SOURCE-CONFIRMED","upper-bound qualifier lost (HB-E1 vs AJR-E2)","I08","source and hub texts","INDEPENDENT","owns the HB-E1 evidence","—","counts toward coverage"),
("Adjacent-field neglect","applicable","SCORED 0","0","FULL-TEXT-CONFIRMED","source engages R1 (AJR-E4)","I19","source text","INDEPENDENT","source-layer engagement","—","counts toward coverage"),
("Lack of decisive tests","applicable","SCORED 0","0","ABSTRACT-CONFIRMED; FULL-TEXT-CONFIRMED; CONTESTED","named direct tests exist; results conflict","I11; I12","ADJUDICATION-1 56/58 screened","INDEPENDENT","named test results","—","counts toward coverage"),
("Poor critique uptake","applicable","SCORED 0","0","FULL-TEXT-CONFIRMED; CONTESTED","Reply answers Albouy","I18","Reply full text","INDEPENDENT","engagement in the uptake population","—","counts toward coverage"),
("Intervention-evidence ratchet","not applicable","N/A","—","—","no intervention claim","—","—","—","—","N/A: no intervention claim","none"),
("Model non-updating","applicable","UNASSESSED","—","CONTESTED","four-link gate not traced","—","—","—","—","UNASSESSED","not label-essential")]: P("| "+" | ".join(r)+" |")
P(f"\nVerified risk score {X}/{Y}; rate {rate:.1f}%; independent 7; nested 1; denominator {Y}; coverage 8/10 (80%); completeness 10/10 (100%).\n")
P(NOFM+"\n")
P("ARTIFACT 9: NETWORK MAP\n")
P(f"Receipts as in SECTION A (RECEPTION-1, 50 nodes, {E} edges, density {E}/2450, input coverage 50/50, COMPUTED-FROM-RETRIEVED). Closure beyond RECEPTION-1 is not established and not excluded.\n")
P("Edge list (CSV, citing,cited):\n")
P("```"); P("source,target")
for a_,b_ in edges: P(f"{a_},{b_}")
P("```\n")
P("COMPLETION LEDGER\n")
P("| Required heading | Exact heading present? | Status: completed / N/A / omitted | Reason or output location |")
P("|---|---|---|---|")
for h,loc in [("PRE-AUDIT CLAIM CONFIRMATION","four lines"),("SECTION A0: CORPUS REGISTER AND SOURCE ELIGIBILITY","register and ledger"),("SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION","receipts, Q1–10"),("SECTION B: EVIDENCE TYPE CODING","Q11–16"),("SECTION C: CITATION POLARITY AND CLAIM USE","Q17–22"),("SECTION D: CLAIM MUTATION TRACKING","Q23–30"),("SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT","lock, tables"),("SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING","Q40–47"),("SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR","Q48–56"),("SECTION H: IGNORED CRITIQUE AND NON-UPTAKE","Q57–63"),("SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING","Q64–70"),("SECTION J: FALSE-POSITIVE AND BASELINE CHECK","Q71–80"),("SECTION J2: THE CONCEDE TEST","three tables"),("SECTION K0: EVIDENCE SUFFICIENCY LEDGER","ledgers, basis tables"),("SECTION K: CARTEL-RISK SCORING","arithmetic, gate"),("ARTIFACT 1: TOP 15 CITATION SPINE TABLE","15 rows"),("ARTIFACT 2: FOUNDING CLUSTER TABLE","4 rows"),("ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE","25 rows"),("ARTIFACT 4: CITATION POLARITY TABLE","15 rows"),("ARTIFACT 5: CLAIM MUTATION TABLE","3 rows"),("ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE","13 rows"),("ARTIFACT 7: CRITIQUE-UPTAKE TABLE","2 rows"),("ARTIFACT 8: CARTEL-RISK SCORECARD","11 dimensions"),("ARTIFACT 9: NETWORK MAP","edge CSV"),("COMPLETION LEDGER","this table"),("ARTIFACT 10: FINAL VERDICT","after ledger"),("FINAL SECTION: STANDARDIZED FINDING TABLE","seven findings")]:
    P(f"| `{h}` | yes | completed | {loc} |")
P("\nGate result: PASS.\n")
P("ARTIFACT 10: FINAL VERDICT\n")
for k2,v in [("Main founding cluster",f"AJR 2001 with Reversal of Fortune, the handbook synthesis and the 2012 Reply; {len(team)}/50 RECEPTION-1 records AJR-team authored"),
("Main amplification hub","Rodrik et al. 2004 (independent, accurate) and the AJR handbook (self-authored, drops the qualifier)"),
("Main proxy problem","expropriation-risk index restated as property-rights enforcement and economic institutions at the self-authored hub (HB-E1)"),
("Main adjacent fields neglected","none at the source layer; cluster engagement with later R1/R2 tests not traced"),
("Main claim mutation","upper-bound qualifier (AJR-E2) lost in HB-E1; popular \"clear chain of causality\" (NP-E1)"),
("Most important ignored critique","none established; Albouy answered by the Reply; Glaeser uptake not traced"),
("Decisive test missing","an instrument-independent cross-country magnitude test (I14 INSUFFICIENT); a human-capital decomposition inside the locked search (I13, bounded)"),
("Verified risk score",f"{X}/{Y}"),("Verified scored-dimension risk rate",f"{rate:.1f}"),("Independent scored dimensions","7"),("Nested scored dimensions","1"),("Verified risk denominator",str(Y)),("Evidentiary coverage","8/10 (80%)"),("Execution completeness","10/10 (100%)"),("Dimension inventory","7 INDEPENDENT SCORED + 1 NESTED SCORED + 0 UNINFORMATIVE + 2 UNASSESSED + 1 N/A"),
("Unscored dimensions and reasons","Review-hub laundering UNASSESSED (I23); Model non-updating UNASSESSED; Intervention-evidence ratchet N/A"),
("N-of-M scope statement",NOFM),("Arithmetic band position","0%–20% (healthy or low-risk network)"),("Risk band",BAND),("Mechanism label",MECH),
("Formal-label gate status","coverage MET (80%; 70% if the review item is withdrawn; PROVISIONAL threshold); band withheld on label-essential grounds"),
("Load-bearing finding(s)","none against field 6; Findings 2, 3 and 4 for the L3 restatements"),
("Concede-test result","field 6 SURVIVES every finding; L3 NARROWS (Findings 2, 3, 4)"),
("Failure location","CITATION (Findings 2, 3, 6, 7); MIXED evidence base (Finding 4); MODEL-RETRIEVAL (Finding 1); none at PAPER for field 6"),
("Best formal label","insufficient evidence (low arithmetic, but the healthy label's label-essential evidence is missing)"),
("Confidence level",f"Low. CITATION CONTEXT COVERAGE: RECEPTION-1 {INS['RECEPTION-1']}/50; CITATION CONTEXT COVERAGE: RECENT-1 {INS['RECENT-1']}/25; CITATION CONTEXT COVERAGE: ADJUDICATION-1 {INS['ADJUDICATION-1']}/58"),
("What evidence would change this assessment","inspected passages from handbook citers; the 4 unretrieved RECENT-1 sample texts; screening ADJ37 and ADJ44; AJR-team responses to Glaeser; a seed-expanded comparison graph"),
("Density inference scope","RECEPTION-1 only (OpenAlex cites:W3124166904, top 50, queried 2026-11-05T04:29:45Z UTC); closure is not established and not excluded beyond the defined corpus")]:
    P(f"- {k2}: {v}")
P("")
P("FINAL SECTION: STANDARDIZED FINDING TABLE\n")
F6="In the base sample of 64 former colonies, the 2SLS estimate of the effect of the 1985–95 protection-against-expropriation index on 1995 log GDP per capita, instrumented by log settler mortality, is 0.94 (SE 0.16)."
FIND=[
dict(f="The OpenAlex record and reception corpora of AJR 2001 are unstable: the same query about 17 hours apart returned 12/50 different top citers and a reference list grown from 13 to 55 works.",t="MAP GAP: this finding targets the retrieval record of AJR 2001, not map field 6.",m="raw/ajr2001_work.json (55 referenced works) vs v1 (13); RECEPTION-1 vs v1 membership; RECENT population 2,695 → 3,026; N01 conflation persists.",c="Database reception corpora are reproducible snapshots of AJR 2001's reception.",fm="other: database record drift and identity conflation",sev="moderate for single-database network metrics; none for field 6",ct="SURVIVES",sl="N/A — SURVIVES",ev="I24; I03; raw/ajr2001_work.json; raw/reception1_top50.json.",et="author inference",vs="RECEPTION-CONFIRMED",ie="OpenAlex updates continuously; ties in cited_by_count reorder near the cut-off.",ww="A versioned dump showing the differences are cut-off reordering only.",fl="MODEL-RETRIEVAL — database record",st="confirmed"),
dict(f="Downstream cross-country re-estimates reuse the AJR settler-mortality series, so their agreement is robustness on one data origin.",t="MAP GAP: this finding targets L3, not map field 6.",m="RD-E1, EL-E2, DML-E1 and the Reply all use the AJR series.",c="Independent studies converge on institutions.",fm="source dependence",sev="moderate",ct="NARROWS",sl="material — surviving claim: several teams obtain similar estimates with the AJR series.",ev="I21; RD-E1; EL-E2; DML-E1.",et="author inference",vs="FULL-TEXT-CONFIRMED",ie="The instrument is the paper's contribution; reuse is expected in robustness work.",ww="Cross-country tests with an independently built instrument reproducing the magnitude.",fl="CITATION — aggregation of non-independent tests",st="confirmed"),
dict(f="The self-authored handbook restates the magnitude without the authors' upper-bound qualifier and broadens the regressor to property-rights enforcement and economic institutions.",t="MAP GAP: this finding targets the hub restatement of the field-6 magnitude, not map field 6.",m="AJR-E2 (p. 1387) vs HB-E1 (WP 10481 p. 29).",c="Most of the rich–poor gap is due to economic institutions.",fm="claim mutation",sev="moderate",ct="NARROWS",sl="material — surviving claim: up to about a 7-fold gap, an upper bound.",ev="I08; I09; AJR-E2; HB-E1.",et="author inference",vs="CROSS-SOURCE-CONFIRMED",ie="Syntheses paraphrase; the published chapter may differ from the WP.",ww="The published Handbook text restoring the qualifier.",fl="CITATION — self-authored hub",st="confirmed"),
dict(f="Direct tests of field 6 and of the disease/geography rival exist, and their results conflict.",t="L3 (MAP GAP) and the robustness of the estimate in map field 6.",m="ADJUDICATION-1: 24/58 DIRECT; ADJ09, ADJ18, ADJ38 and Sachs report direct geography or malaria effects; Rodrik and Easterly–Levine report institutions dominate; ADJ01 (unreviewed deposit) reports weak-IV-robust sets unbounded under Albouy revisions.",c="Institutions, not geography or disease, are the fundamental cause.",fm="other: contested evidence base",sev="moderate",ct="NARROWS",sl="material — surviving claim: institutions a major channel; direct disease effects not excluded.",ev="I11; I12; I15; abstracts in raw/adj1_Q*.json.",et="primary study",vs="ABSTRACT-CONFIRMED; FULL-TEXT-CONFIRMED; CONTESTED",ie="The tests use different samples and controls; conflict may reflect specification choice.",ww="A pre-registered multi-specification comparison resolving the conflict.",fl="MIXED — evidence base",st="contested"),
dict(f="Albouy's data critique is substantively answered by the founding cluster.",t=F6,m="Reply p. 3078 answers both objections; population co-citation 72/3,026 (descriptive).",c="(Prosecutorial hypothesis) the cluster ignores the critique.",fm="none — acquittal on critique uptake",sev="none",ct="SURVIVES",sl="N/A — SURVIVES",ev="I18; I20.",et="primary study",vs="FULL-TEXT-CONFIRMED; CONTESTED",ie="Not applicable to an acquittal.",ww="Evidence that the Reply's answers were later withdrawn or refuted.",fl="CITATION — uptake",st="confirmed"),
dict(f="Inside RECEPTION-1 internal density is low; AJR-team records draw many internal edges, mostly via the conflated N01.",t=F6,m=f"Density {E}/2450 = {d:.2f}%; team in-edges {tshare}/{E}, {toteam_x}/{len(ex)} excluding N01.",c="(Prosecutorial hypothesis) the estimate's authority rests on a closed cluster.",fm="none — acquittal on closure inside the corpus",sev="none",ct="SURVIVES",sl="N/A — SURVIVES",ev="I01; I02; Section A receipts.",et="author inference",vs="RECEPTION-CONFIRMED",ie="Not applicable to an acquittal; closure beyond the corpus is not excluded.",ww="A seed-expanded or matched graph with higher closure.",fl="CITATION — network structure",st="confirmed"),
dict(f="Recent citers mostly cite AJR 2001 without other AJR-team works, and the inspected uses are background.",t=F6,m=f"{len(fc_recent)}/25 cite team works beyond target; 2/2 inspected passages background; 4/6 sampled texts not retrieved.",c="(Prosecutorial hypothesis) recent work recycles the founding cluster.",fm="none — provisional acquittal",sev="none",ct="SURVIVES",sl="N/A — SURVIVES",ev="I04; I05; I06 (INSUFFICIENT).",et="author inference",vs="RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (2 passages)",ie="Not applicable to an acquittal.",ww="The 4 unretrieved sampled passages showing premise use of the estimate.",fl="CITATION — recent reception",st="provisional")]
labels=[('Finding','f'),('Target claim','t'),('What was measured','m'),('What was claimed','c'),('Failure mode','fm'),('Severity','sev'),('Concede test','ct'),('Scope loss if NARROWS','sl'),('Evidence','ev'),('Evidence type','et'),('Verification state','vs'),('Possible innocent explanation','ie'),('What would weaken this','ww'),('Failure location','fl'),('Status','st')]
for i,fd in enumerate(FIND,1):
    P(f"Finding {i}\n"); P("| Field | Entry |"); P("|---|---|")
    for lab,key in labels: P(f"| {lab} | {fd[key]} |")
    P("")
txt="\n".join(o).rstrip()+"\n"
open('out/02c_citation_network_v2cand2.md','w').write(txt)
print(len(txt.splitlines()),len(txt.encode()),full,toteam_x,len(ex),indeg_x.most_common(3))
