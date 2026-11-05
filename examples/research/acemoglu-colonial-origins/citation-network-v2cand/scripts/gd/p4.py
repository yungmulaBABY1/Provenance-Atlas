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
