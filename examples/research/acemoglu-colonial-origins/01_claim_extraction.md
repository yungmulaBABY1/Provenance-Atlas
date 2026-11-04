**INSTRUMENT PREFLIGHT:** prompts/1-claim-extraction.txt @ commit ce028e1294873df0143ca1ae00d6abf74a910563 | blob 894579a79e67508bdc4026b77c0a104681f903ad (sha256 656b11c301931726a5435b231774f40797a10fd0cab950224616fc18951c035f) | 1038 lines | 44072 bytes | markers PRESENT | IDENTITY CONFIRMED

Identity basis: the head of the remote branch was looked up with `git ls-remote` (origin HEAD = refs/heads/main = ce028e1…), separately from fetching the content. The instrument was then read from the clone at that immutable commit, and the blob SHA was computed by `git rev-parse HEAD:prompts/1-claim-extraction.txt`. Retrieval form: IMMUTABLE REMOTE (cloned at a commit). The marker present is "CLAIM EXTRACTION / INFLATION MAP".

Runner disclosure: a single AI agent (Grok Bot executor) ran this stage and every later stage in one session. Its pre-registered prior exposure is recorded in 00a_preregistration_LOCKED.txt. Process independence is NOT_ESTABLISHED. The output is model-produced and is not an established finding.

Target: Acemoglu, Daron; Johnson, Simon; Robinson, James A. (2001). "The Colonial Origins of Comparative Development: An Empirical Investigation." American Economic Review 91(5): 1369–1401. doi:10.1257/aer.91.5.1369. Version read: the published journal version, a JSTOR-stamped scan (JSTOR stable 2677930) hosted by MIT Economics, 34 PDF pages. PDF page 1 is the JSTOR cover, so journal page = PDF page + 1367. Text was extracted with pdftotext 25.03.0 (poppler). The OCR text layer drops many inter-word spaces, so the quotes below reproduce the text layer character for character, including those dropped spaces ("institutionsis", "standarderrorof").

## 1. WHAT WAS LITERALLY MEASURED

- **Unit and sample.** The unit is a country. The base sample is 64 former European colonies with settler-mortality, expropriation-risk and GDP data (Appendix Table A2) [A1.1].
- **Outcome.** Log GDP per capita (PPP) in 1995 (Appendix Table A2 column header) [A1.1].
- **Endogenous regressor ("institutions").** Average protection against expropriation risk, 1985–1995, from Political Risk Services. The authors use it "as a proxy for institutions" [A1.2]. Per footnote [A1.3], the variable is constructed for foreign investment.
- **Instrument.** Log settler mortality: annualized deaths per 1,000 mean strength, mainly among European soldiers, with bishops (Latin America) and other sources benchmarked in. The authors use the "earliest available number for each country" [A1.4] and combine sources [A1.5].
- **Estimator.** 2SLS. The first stage regresses expropriation risk on log mortality; the second stage regresses log GDP per capita on instrumented expropriation risk [A1.6]. The identifying assumption is stated as an exclusion restriction [A1.7].
- **Reported quantity.** The 2SLS coefficient is 0.94 with a standard error of 0.16 (Table 4, column 1) [A1.6].
- **What is not measured directly.** Settler mortality where settlers actually were, in most countries. Albouy (2012) reports that 36 of 64 countries have rates conjectured from other places or benchmarked. AJR (2012) describe dropping them as discarding "almost 60 percent of our original sample" and dispute the coding and its significance, not the existence of cross-country assignment. That count comes from the critique, not from the 2001 paper. Within the 2001 paper, the measurement basis for each country is given only via Appendix Table A1 sources and the unretrieved Appendix B of AJR (2000) [A1.5].

**Analysis.** Cross-sectional IV. Robustness variants are reported in Tables 4–8: latitude, excluding the neo-Europes, excluding Africa, continent dummies, output per worker, and controls for geography, disease, religion, colonizer identity and other factors. Overidentification tests use early-institutions measures [A1.8].

**PUBLICATION STATUS:** published in AER (December 2001). No retraction is flagged (OpenAlex is_retracted=false, retrieved 2026-11-04). A published Comment (Albouy 2012, AER 102(6):3059–76) and Reply (AJR 2012, AER 102(6):3077–3110) exist and were retrieved. No erratum to the 2001 article was found in the limited search conducted, which is not an exhaustive search.

## 2. STRONGEST CLAIM THE SOURCE ITSELF MAKES

- Abstract: "we estimate large effects of institutions on income per capita" [A2.1], and, once institutions are controlled for, Africa and distance from the equator do not lower income [A2.2].
- Section IV: "Overall,the resultsin Table4 show a largeeffect of institutionson economic performance" [A2.3]. The Nigeria-to-Chile counterfactual is "as much as a 7-fold increase" [A2.4]. The paper itself bounds this as "an upperbound" [A2.5].
- Conclusion: the instrument is "arguably exogenous", and the results "suggest substantial economic gains from improving institutions" (p. 28, Conclusion; quoted from the text layer, anchor not separately listed).
- Identification claims: the exclusion restriction is "plausible" [A2.6]; the overidentification tests let the authors "rule out all three of the above possibilities" [A2.7]. The paper qualifies this with the caveat that such tests "may not lead to a rejection if all instrumentsare invalid" [A2.8].

## 3. WEAKER DEFENSIBLE CLAIM THE EVIDENCE ACTUALLY SUPPORTS

Author reconstruction from Field 1, extracted rather than evaluated. In the 64-country base sample, using the authors' settler-mortality series as the instrument, 2SLS gives a coefficient of 0.94 (SE 0.16) on the 1985–95 PRS expropriation-risk index for 1995 log GDP per capita. Two things are conditional:
- the causal reading depends on the stated exclusion restriction;
- the reading as "institutions" depends on expropriation risk proxying a broader "cluster of institutions".

The magnitude interpretation (the 7-fold Nigeria–Chile gap) is, per the source, an upper bound.

## 4. BROADER CLAIM ATTACHED DOWNSTREAM

RETRIEVED, one item. The Royal Swedish Academy of Sciences press release for the 2024 Sveriges Riksbank Prize, awarded "for studies of how institutions are formed and affect prosperity", states: "The laureates have shown that one explanation for differences in countries' prosperity is the societal institutions that were introduced during colonisation." (nobelprize.org/prizes/economic-sciences/2024/press-release/, fetched 2026-11-04, HTML sha256 in SOURCES_MANIFEST.) This sentence attributes the result to the laureates' body of work. It does not name AJR 2001 in the retrieved passage, so attribution to this specific paper is PROVISIONAL.

RECALLED: no item entered. I have training exposure to wide downstream use of this paper (textbooks, policy documents, and its role as a standard IV teaching example). Under the run rules, memory is not a source.

## 5. WHERE THE INFLATION BEGINS

**5A. Within-source.** Candidate inflation points, mapped and not judged:
- (i) The step from "protection against expropriation risk" (a PRS index built for foreign investors [A1.3]) to "institutions" in the abstract and conclusion [A1.2], [A2.1]. PAPER.
- (ii) The step from "settler mortality" as measured (mostly soldiers; partly assigned across countries [A1.5]) to the theoretical "potential settler mortality". PAPER.
- (iii) "large effects" [A2.1] alongside the paper's own "upperbound" qualifier [A2.5]. The qualifier is present in the source, so this may be a wording point rather than an inflation. Ambiguous, not classified.
- (iv) A within-source numeric inconsistency: the baseline is 0.94 on p. 18 [A1.6] but "0.95 reportedin Table 4" on p. 26 [A5.1]. This is a wording or transcription point. Its materiality is assessed by the prosecutors.

**5B. Downstream.** The 2024 press-release sentence generalizes to "the laureates have shown". Whether it inflates AJR 2001 specifically is not assessable without a retrieved downstream item that cites the paper by name. NOT ASSESSED BEYOND ONE ITEM.

## CLAIM INVENTORY

| Claim | Quantified? | Why it might be inflated | Selected for Field 6? |
|---|---|---|---|
| 2SLS effect of expropriation-risk index on 1995 log GDP pc = 0.94 (SE 0.16), base sample (Table 4 col 1) | Yes | Depends on instrument validity and mortality-data construction; restated downstream as "institutions cause prosperity" | YES |
| Settler mortality explains over 25% of the variation in current institutions (first stage) | Yes (R² 0.27) | Measurement and assignment of mortality rates; clustering | No (DEFERRED) |
| Nigeria→Chile institutions imply up to a 7-fold income increase | Yes | Point-estimate extrapolation; the source labels it an upper bound | No (DEFERRED) |
| Africa / latitude do not matter once institutions are controlled for | Partly (Table 4 cols 2, 8, 9) | A null on controls in a small sample read as an absence of effect | No (DEFERRED) |
| Overidentification tests rule out direct effects of mortality | No (test outcomes only) | Low power; the source's own caveat | No (DEFERRED) |
| Colonial settlement strategy → early institutions → current institutions (the mechanism chain) | Partly (Table 3) | A mechanism claim distinct from the effect claim | No (DEFERRED) |

Field 6 selection reason: Rule 2 (the most precisely quantified version). The Table 4 column 1 coefficient is the paper's headline estimate. It is restated at multiple precision levels in the abstract and conclusion, and the critique literature targets its robustness directly.

## 6. WHICH CLAIM IS THIS AUDIT EVALUATING?

**Claim.** In the base sample of 64 former colonies, the 2SLS estimate of the effect of average protection against expropriation risk (1985–1995) on log GDP per capita (PPP) in 1995, instrumenting with log settler mortality, is 0.94 with a standard error of 0.16 (Table 4, column 1).

This audit evaluates the SOURCE'S quantified claim (#2 at its quantified form), not a downstream restatement.

## REQUIRED OUTPUT TABLE

| Field | Content | Verification state |
|---|---|---|
| 1. Literally measured | 64 former colonies; outcome log GDP pc PPP 1995; regressor PRS average protection against expropriation risk 1985–95 (built for foreign investors); instrument log settler mortality (soldiers/bishops/laborers, earliest available, partly assigned across countries); 2SLS | FULL-TEXT-CONFIRMED (published article); data assignments per country FULL-TEXT-CONFIRMED in Table A2 and posted data |
| 2. Source's strongest claim | "large effects of institutions on income per capita"; exclusion restriction "plausible"; overid tests "rule out" the alternatives (with caveat) | FULL-TEXT-CONFIRMED |
| 3. Weaker defensible claim | Coefficient 0.94 (SE 0.16) on the PRS expropriation index in this sample with this instrument; causal and "institutions" readings conditional; 7-fold gap an upper bound | author reconstruction from Field 1 |
| 4. Downstream claim | 2024 Prize press release: "The laureates have shown that one explanation for differences in countries' prosperity is the societal institutions that were introduced during colonisation." | RETRIEVED (one item); attribution to AJR 2001 specifically PROVISIONAL |
| 5A. Within-source inflation point + failure location | Expropriation index → "institutions"; measured soldier/bishop mortality → potential settler mortality; 0.94 vs "0.95" baseline inconsistency. PAPER | FULL-TEXT-CONFIRMED (wording read; materiality not assessed here) |
| 5B. Downstream inflation point + failure location | Not assessed beyond one body-of-work press-release item | PROVISIONAL |
| 6. Claim under audit | Table 4 col 1: 2SLS 0.94 (SE 0.16), base sample of 64 | FULL-TEXT-CONFIRMED that the source states it; numerically re-derived from posted data in Stage 2 (not part of this map) |

## CONSTRUCT-SIDE HANDOFF SUB-SCHEMA

| Check | Object | Retrieval status / basis | Result | Verification state | Evidence |
|---|---|---|---|---|---|
| Construct establishment | PREVALENCE | N/A | The construct properties PREVALENCE/WRONGNESS/HARM are designed for belief or attitude constructs; AJR's constructs are institutional and macroeconomic | N/A | — |
| Construct establishment | FORM | ESTABLISHED-CITED | "Institutions" = a "cluster of institutions" (expropriation, judiciary, property rights, civil liberties); expropriation risk is "related to all these institutionalfeatures" (fn 3, p. 4) | FULL-TEXT-CONFIRMED (assertion read; cited support not retrieved) | p. 4 fn 3 |
| Construct establishment | DOMAIN | ESTABLISHED-REPORTED | Former European colonies, 1985–95 institutions, 1995 income | FULL-TEXT-CONFIRMED | Table A2 |
| Construct establishment | WRONGNESS | N/A | Not a belief construct | N/A | — |
| Construct establishment | HARM | N/A | Not a belief construct | N/A | — |
| Definition-operationalization | PRS "risk of expropriation" index as "institutions" | ITEMS-INFERRED (PRS codebook/items not retrieved) | UNKNOWN | PROVISIONAL | [A1.2], [A1.3] |
| Definition-operationalization | settler-mortality series as "potential settler mortality" | ITEMS-RETRIEVED (Table A2 values; posted data; Albouy 2012 and AJR 2012 source-by-source coding read) | narrower (soldiers in barracks/on campaign, bishops, laborers; partly assigned across countries) | FULL-TEXT-CONFIRMED | [A1.4], [A1.5]; Albouy 2012 pp. 3060–64; AJR 2012 Appendix |
| Grade-before-assert | N/A | N/A | N/A — no belief graded | N/A | P2 VOID / N/A |

**CLAIM UNDER AUDIT:** In the base sample of 64 former colonies, the 2SLS estimate of the effect of the 1985–95 protection-against-expropriation index on 1995 log GDP per capita, instrumented by log settler mortality, is 0.94 (SE 0.16).

**WITHIN-SOURCE FAILURE LOCATION:** paper (candidate points mapped in 5A; not judged here) — FULL-TEXT-CONFIRMED wording.

**DOWNSTREAM FAILURE LOCATION:** not assessed beyond one retrieved body-of-work item — PROVISIONAL.

**GAP TYPE:** neither apparent at the level of the map. Candidate within-source gaps (proxy and instrument construction) are handed to the prosecutors. The map does not decide them.

**MAP CONFIDENCE:** moderate. It would rise with the PRS codebook, the AJR (2000) Appendix B/Table A5 (cited, not retrieved), and downstream items that cite AJR 2001 by name.

## SOURCE ANCHORS

PDF pages are 1-based as the viewer counts them; PDF p. 1 is the JSTOR cover. Journal page = PDF page + 1367.

**A1.1** · Field 1: sample and outcome · author reconstruction from Field 1 (Appendix Table A2 is a table; header and rows read in pdftotext -layout; no single text-layer passage)

**A1.2** · Field 1: regressor is a proxy for institutions · p. 3, Introduction
> we use the protection against "risk of expropriation"index from Political Risk Services as a proxy for institutions.

**A1.3** · Field 1: index constructed for foreign investment · p. 11, Section II footnote
> The protection against expropriationvariable is specifically for foreign investment

**A1.4** · Field 1: earliest available mortality figure · p. 16, Section III
> earliest available number for each country,

**A1.5** · Field 1: combining sources introduces measurement error · p. 16, Section III footnote 17
> this measurement error does not lead to inconsistent estimates of the effect of institutions on performance.

**A1.6** · Field 1 and Field 6: reported coefficient · p. 18, Section IV
> per capita is 0.94. This estimate is highly significantwith a standarderrorof 0.16

**A1.7** · Field 1: exclusion restriction · p. 4, Introduction
> The exclusion restrictionimplied by our instrumental variable regression is that, conditional on the controlsincludedin the regression, the mortality rates of European settlers more than 100 years ago have no effect on GDP per capita today, other than their effect through institutional development.

**A1.8** · Field 1: overidentification caveat · p. 26, Section VI
> such tests may not lead to a rejection if all instrumentsare invalid, but still highly correlated with each other.

**A1.9** · Field 1: clustering footnote · p. 18, Section IV footnote 18
> clustering has little effect on the standarderrors, and does not change our results.

**A1.10** · Field 1: within-Africa first stage · p. 20, Section IV footnote 21
> we conclude that the relationship between settler mortality and institutionsis weaker within Africa.

**A2.1** · Field 2: abstract, large effects · p. 2, Abstract
> differencesin Europeanmortalityrates as an instrumentfor currentinstitutions,we estimate large effects of institutions on income per capita.

**A2.2** · Field 2: abstract, Africa/equator · p. 2, Abstract
> Once the effect of institutionsis controlledfor, countriesin Africa or those closer to the equatordo not have lower incomes.

**A2.3** · Field 2: Table 4 summary · p. 20, Section IV
> Overall,the resultsin Table4 show a largeeffect of institutionson economic performance.

**A2.4** · Field 2: Nigeria–Chile counterfactual · p. 4, Introduction
> lead to as much as a 7-fold increase in Nigeria's income

**A2.5** · Field 2/3: upper-bound qualifier · p. 20, Section IV
> 7-fold differenceis an upperbound.

**A2.6** · Field 2: exclusion restriction plausible · p. 4, Introduction
> We believe that this is unlikely to be the case and that our exclusion restriction is plausible.

**A2.7** · Field 2: overidentification conclusion · p. 26, Section VI
> we can rule out all three of the above possibilities.

**A2.8** · Field 2: overidentification caveat · same passage as A1.8

**A2.9** · Field 2: robustness claim in introduction · p. 5, Introduction
> excluding Australia,New Zealand,Canada,and the United States does not change the results, nor does excluding Africa.

**A5.1** · Field 5A: baseline restated as 0.95 · p. 26, Section VI
> The estimate in our base sample is 0.91 (s.e. = 0.24) comparable to our baseline estimate of 0.95 reportedin Table 4.

**A6.1** · Field 6: claim under audit · same passage as A1.6

## READ RECORD

- Read: the full published article, all 34 PDF pages (text layer and pdftotext -layout), including Tables 1–8 and Appendix Tables A1–A3 as extracted text. Table cells were read from -layout output, and multi-column tables carry an extraction risk.
- Not read: AJR (2000) NBER WP 7771 was retrieved but only spot-checked, not read in full. AJR (2000) Appendix B and Appendix Table A5 are cited as "available from the authors" and were not retrieved. The PRS/ICRG codebook was not retrieved. Figures were read only as captions.
- Garbled text: the OCR text layer drops many inter-word spaces. Quotes reproduce it as extracted. Equations are garbled in the text layer.
- Unsure how to classify: whether "large effects" (abstract) is an inflation of a coefficient the paper itself bounds. I left it ambiguous (5A iii).
- Tools: pdftotext 25.03.0; grep; the repo's own anchor matcher (atlas.extraction.anchors.match) to check that each quote occurs in the extraction; OpenAlex API for retraction/reception metadata; curl for one downstream press release.
