
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
