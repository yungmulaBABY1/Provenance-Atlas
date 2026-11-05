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
