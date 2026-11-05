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
