# STAGE 3 — OPPOSITIONAL CITATION & NEGLECTED EVIDENCE COUNTER-AUDIT
## Target: AJR (2001), Table 4 col. 1 (claim map Field 6)

INSTRUMENT PREFLIGHT: prompts/research-analysis/3-counter-audit.txt @ commit ce028e1294873df0143ca1ae00d6abf74a910563 | blob 74357f08562a47fa8fdbbde4325657ad3c9cd871 (sha256 291f2339992eeaca83c60281263975d3b5643d64ec6e5d118fa39c44b6c9ede9) | 915 lines | 42287 bytes | markers PRESENT | IDENTITY CONFIRMED

### INPUTS (as declared by the instrument)
0. Claim map: 01_claim_extraction.md (supplied).
1. Foundational paper: AJR 2001 (S1, full text).
2. Citation-network audit output: NOT RUN. See 02c_citation_network_NOT_RUN.txt. Sections A, B, F and the cartel-risk scorecard therefore have no prosecutor input. Here they are limited to the reception checks this stage ran itself (OpenAlex, R1–R2).
3. Construct-validity audit output: 02b_construct_validity.md (supplied).
4. Internal-validity audit output: 02a_internal_validity.md (supplied).
5. Thesis paragraph: not supplied, so the fidelity check is not run.
6. Central claim: the Field 6 statement.
7. Current audit verdict:
   - internal validity: USEFUL-FOR-NARROWER, grade C (borderline B), with one eligible material narrowing (IV-1, contested) and one pending conditional DEFEATS (IV-6);
   - construct validity: VALID for Field 6, residual grade B; the Field 2 relabel is PROVISIONAL.
8. Known hub: AJR 2001 / AJR 2000 (NBER w7771) / AJR 2005, 2006, 2008 replies (not retrieved) / AJR 2012 Reply.
9. Adjacent fields: historical epidemiology (Curtin; Tulloch), and the economic-geography / human-capital debate. The human-capital side was recalled, not retrieved.

Process disclosure: the same agent wrote both prosecutor outputs being balanced here. That is a structural independence failure, and J2 discloses it.

### SOURCE-RECEPTION GATE (load-bearing sources)

| Source | Reception check | Standing |
|---|---|---|
| Albouy 2012 Comment (AER 102(6):3059) | OpenAlex W1969918011, cites AJR 2001. The reply (W3124131699) exists and was read in full | CONTESTED: rebutted by AJR 2012; no Albouy rejoinder retrieved |
| AJR 2012 Reply (AER 102(6):3077) | OpenAlex W3124131699. Read in full with its appendix | CONTESTED: no published counter-reply retrieved; its central claims are tested mechanically in replicate.log Part C |
| AJR 2005 "A Response to Albouy" | OpenAlex title match only | LOCATED; not read |
| 2017 "Graphs as a Tool for the Close Reading of Econometrics (Settler Mortality is not a Valid Instrument for Institutions)" | OpenAlex title only | LOCATED; tenor from title only; PROVISIONAL; may not rank as a top-3 threat |
| Glaeser et al. 2004 (human capital) | recalled only | PROVISIONAL; excluded from ranking |
| 2024 Prize press release (R3) | retrieved HTML | RETRIEVED; downstream; does not name AJR 2001 |

A. OPPOSITIONAL CITING PAPERS
Two were found by a limited OpenAlex title search (filter cites:W3124166904 plus title terms): Albouy 2012 (CONTESTED) and the 2017 "Graphs" paper (LOCATED only). This is not a citation-network sweep. Of the roughly 8,600 citing works, none was screened by context.

B. NON-CITING OPPOSITION PAPERS
Not searched. Recorded as a coverage gap, not as absence.

C. NEGLECTED REFERENCES
Not assessed by retrieval.

D. IGNORED ADJACENT FIELDS
Historical epidemiology is engaged on both sides: AJR's sources are Curtin and Gutierrez, and the reply leans on Tulloch. No ignored field was established.

E0. SOURCE SELF-DEFENSE CHECK (run first)

Sections searched for every row: abstract, Introduction (PDF pp. 2–5), Sections III–VI (pp. 10–26), footnotes 2–4, 16–23 and 31, the Conclusion (pp. 27–28), and Appendix Table A2 (p. 31). Text layer and -layout were both used.

| Prosecutor finding | Source passage that anticipates it (quote + location) | Type | Answers it? | Effect on the finding |
|---|---|---|---|---|
| IV-1 instrument-construction fragility | "Combining data from a variety of sources will introduce measurement error … this measurement error does not lead to inconsistent estimates" (fn 17, PDF p. 16); "alternative methods produce remarkably similar results" (PDF p. 16, citing Table A5, not retrieved) | sensitivity test + stated assumption | partly. The fn 17 argument covers classical error only, not error correlated with campaign status or income. The alternative-benchmark test (Table A5) was not retrieved; my C6/C7 naval and Caribbean benchmark runs agree with it (0.97, 0.96) | RECHARACTERIZED: from "untested" to "tested for benchmarking choice, untested for correlated (campaign/assignment) error in 2001". The AJR 2012 capping test (external, E1) then NARROWS it further |
| IV-2 clustering | "This clustering has little effect on the standarderrors, and does not change our results." (fn 18, PDF p. 18) | sensitivity test | fully, for the no-controls spec | DEFEATED as a charge. The prosecutor already recorded SURVIVES; the source's own claim is corroborated (B1: SE 0.20, AR bounded). Removed from threat ranking |
| IV-3 TZA 280 vs 145 | NONE FOUND (searched Table A2, data appendix text, fn 16–17) | NONE | not at all | UNAFFECTED (minor) |
| IV-4 IDN log GDP in 2011 data | NONE FOUND in 2001 paper (out of scope by date); not mentioned in reply/appendix text (grep "Indonesia") | NONE | not at all | UNAFFECTED (minor; not a 2001 finding) |
| IV-5 0.95 vs 0.94 | NONE FOUND | NONE | not at all | UNAFFECTED (none severity) |
| IV-6 exclusion restriction | "The major concern with this exclusion restrictionis that the mortality rates of settlers could be correlatedwith the current disease environment" (PDF p. 4); malaria control gives "0.69 instead of 0.94" (PDF p. 24); overid tests with the caveat "may not lead to a rejection if all instrumentsare invalid" (PDF p. 26) | stated assumption + sensitivity tests + acknowledged limitation | partly. Specific channels (disease, climate, religion, colonizer) are tested by controls; a general direct effect cannot be tested with this design | RECHARACTERIZED: "disclosed and tested against named channels; untestable in general". It stays PENDING and non-anchoring |
| IV-7 col. 8 weak-IV | "if we limit the sample to African countries only, the first-stagerelationshipusing the protection against expropriationvariable becomes considerably weaker" (fn 21, PDF p. 20) | acknowledged limitation (partial) | partly | NARROWED: "the paper discloses weaker within-continent variation but presents col. 8 as robustness without weak-IV-robust inference" |
| CV-1 index→"institutions" | "Government expropriationis not the only institutional feature that matters" (fn 3, PDF p. 3); "our results hold also with a variety of other measures of institutions" (fn, PDF p. 11) | acknowledged limitation + sensitivity test (cited) | partly (the alternative-measure tables were not retrieved) | RECHARACTERIZED: "disclosed; alternative measures asserted, with tables in an unretrieved companion paper" |
| CV-2 instrument construct narrower | PDF pp. 14–16 describe soldiers, bishops and the earliest-available rule | stated assumption | fully, as disclosure | UNAFFECTED as to severity (none). The construct is disclosed |
| CV-3 intervention ratchet | "Institutionsare treatedlargely as a "black box"" … "do not point out what concrete steps" (PDF p. 28) | acknowledged limitation | partly | NARROWED: "policy-gain sentence in the conclusion, self-caveated in the next paragraph" |

E0 residual: DEFEATED 1 (IV-2); NARROWED 2 (IV-7, CV-3); RECHARACTERIZED 3 (IV-1, IV-6, CV-1); UNAFFECTED 4 (IV-3, IV-4, IV-5, CV-2). The UNAFFECTED rows are UNAFFECTED because the source is silent: the data discrepancies postdate or are invisible in the text. They are not unsearched.

E1. EXTERNAL SUPPORTING EVIDENCE
- AJR 2012 Reply: capping at 250 and dropping Gambia "makes our results robust even in Albouy's smallest sample (i.e., with just 28 and 27 observations, respectively)" (reply text, PDF p. 2).
  - Mechanical check (replicate.log, using AJR's posted rebuttal data): C1, own-country without Gambia, gives 0.74 (0.11), F = 24.2. B2-capped gives 0.83 (0.17), F = 15.6.
  - With latitude, capped own-country (B2) still has a bounded AR set [0.21, 2.02] at F = 6.5.
  - The reply's own caveat "except in the very smallest of his samples" matches B4-capped-latitude (F = 1.84, AR = whole line).
  - Verification: FULL-TEXT-CONFIRMED + COMPUTED-FROM-RETRIEVED. Standing: CONTESTED. Whether capping is legitimate is a judgment, not a computation.
- AJR 2012 recoding of the campaign dummy (campaignsj2): C3, full sample, F = 11.5, AR [0.64, 1.95]. Same standing.
- Weak-IV-robust inference for col. 1 (AR [0.70, 1.43]; HC1 [0.69, 1.61]) is this audit's own computation and supports Field 6 directly.

- IV-3 context (external): both critics' records give Tanzania 145. Albouy's appendix says "The laborer rate of 145 for Kenya, also used for Tanzania, comes from this passage" (AJRrev_App, text line 147). Albouy's Table lists "Tanzania 145", and the AJR 2012 appendix discusses Tanzania within Albouy's dropped set. The posted 2001 maketable4 value of 280 reproduces the printed 0.94, while 145 gives 0.92. The published estimate therefore appears to have used 280. The cause is UNKNOWN (data-entry error versus undocumented revision), and the effect is immaterial.

F. CITATION-NETWORK UPTAKE OF OPPOSITION
NOT ASSESSED: the citation-network stage was not run. No claim of suppression or of correct discounting is made. The OpenAlex count anomaly (the reply showing 6,266 citations) means raw counts cannot be used as uptake evidence without cleaning.

G. SUMMARY TABLE — OPPOSITION STRENGTH

|Category                            |Number Found|Strongest Example|Evidence Quality|Verification state|Impact on Central Claim|
|------------------------------------|-----------:|-----------------|---------------:|------------------|-----------------------|
|Oppositional citing papers          |2 (limited search)|Albouy 2012|High (published comment, data-based)|FULL-TEXT-CONFIRMED; CONTESTED|narrows claim|
|Non-citing opposition papers        |0 (not searched)|—|—|NOT ASSESSED|needs verification|
|Neglected references                |0 (not assessed)|—|—|NOT ASSESSED|needs verification|
|Ignored adjacent fields             |0|—|—|—|no effect|
|Strongest support for original claim|3|AJR 2012 capping/recoding + col. 1 AR set|High (data-based)|FULL-TEXT-CONFIRMED; COMPUTED|weakens audit (of IV-1's "material" label)|

The three most threatening findings in order of severity are:
1. IV-1, instrument-construction fragility. FULL-TEXT-CONFIRMED + COMPUTED; adjudication CONTESTED.
2. IV-6, the exclusion restriction. PROVISIONAL; capped and non-anchoring. It stays listed only as a pending conditional defeat, not as an established threat.
3. CV-1, the "institutions" proxy. PROVISIONAL (items not retrieved); it bears on Field 2, not Field 6.
The 2017 "Graphs" paper is excluded from the top three because it is only LOCATED.

G2. DID THE PROSECUTION ATTACK THE STRONGEST VERSION?

| Finding | Declared target | Bears on Field 6? | Version attacked | Layer | Severity after re-aim |
|---|---|---|---|---|---|
| IV-1 | Field 6 | yes (precision/robustness of the estimate) | Field 6 / Field 2 robustness claim | PAPER (data) + MIXED (dispute) | moderate → minor-to-moderate (see H) |
| IV-2 | Field 6 | yes | Field 6 | PAPER | none |
| IV-3 | Field 6 | yes (the number itself) | Field 6 | PAPER (data vs appendix) | minor |
| IV-4 | Field 6 (rebuttal baseline) | marginal: concerns 2011 data, not the 2001 estimate | MAP GAP (2012 exchange data) | PAPER (2012 dataset) | minor; re-aimed off Field 6 |
| IV-5 | Field 6 | wording only | Field 6 | PAPER | none |
| IV-6 | Field 6 | yes (causal reading) | Field 6 causal interpretation | PAPER (assumption) | pending, non-anchoring |
| IV-7 | Field 6 (robustness context) | no: col. 8, not col. 1 | Field 2 ("robust to continent dummies") | PAPER | minor; re-aimed to Field 2 |
| CV-1 | Field 6 (context Field 2) | no: Field 6 is worded at the index | Field 2 | PAPER | minor, PROVISIONAL |
| CV-2 | Field 6 | no direct effect on the estimate | Field 6 | PAPER | none |
| CV-3 | Field 6 (context conclusion) | no | Field 2 / conclusion | PAPER | minor |

Double-count guard. IV-1 and CV-2 share one evidentiary base (the mortality-series construction) but use different levers: precision/identification versus construct label. CV-2 carries no severity, so there is nothing to double-count. IV-6 and CV-2 are NESTED as one lever (exclusion plausibility given what the instrument measures), and only IV-6 is retained, as pending.

| Question | Answer | Supporting prosecutor findings |
|---|---|---|
| Versions attacked | Field 6 (IV-1, 2, 3, 5, 6; CV-2); Field 2 (IV-7, CV-1, CV-3); MAP GAP (IV-4) | as listed |
| Version audit targeted (map field 6) | Table 4 col. 1 estimate | — |
| Finding-level match rate | 6 of 10 aimed at Field 6; 3 re-aimed to Field 2; 1 MAP GAP | — |
| Failure location(s) | PAPER (data construction, assumption, wording); MIXED for the unresolved coding dispute | IV-1, IV-6, CV-1 |
| Severity survives re-aiming? | Partly: IV-1 survives but is softened; IV-7/CV-1/CV-3 apply to Field 2 only | — |
| Nested findings consolidated | IV-6 + CV-2 (exclusion plausibility) | — |

MAP DISAGREEMENT: none material. The map's candidate 5A points (i) proxy and (ii) instrument construct are confirmed as PAPER-layer. Point (iii), "large effects", sits beside the source's own upper-bound qualifier and was correctly left unclassified.

H. REVISED THESIS IMPACT

Category: C. Thesis softened. The internal-validity stage's "MATERIAL narrowing → grade C" is not upheld as unambiguous. Three things weigh against it:
- the source's own benchmark-sensitivity claim plus my C6/C7 runs;
- the reply's capping/recoding, which restores bounded weak-IV-robust sets in every cell but one;
- point estimates that never leave 0.73–1.15.

The fragility is real only conditional on accepting Albouy's coding and rejecting capping. That is a judgment the record leaves CONTESTED. The counter-audit records the internal-validity grade as "B–C, CONTESTED (depends on the unresolved coding dispute)".

1. Remove: IV-2 as a charge (DEFEATED by fn 18 plus corroboration).
2. Narrow:
   - IV-1, to "identification is weak in the 28-country own-data subsample with geographic controls under Albouy's coding; full-sample and capped/recoded variants are well identified";
   - IV-7 and CV-1, re-aimed to Field 2.
3. Strengthen: the col. 1 acquittal (weak-IV-robust AR set excludes zero; exact reproduction).
4. Better sourcing needed:
   - IV-6 (direct-channel evidence);
   - CV-1 (PRS items; AJR 2000 Tables 4a–e);
   - the 2017 "Graphs" paper;
   - Albouy's own package (to confirm that my Part B approximates his tables).
5. Unchanged: IV-3, IV-5, CV-2.
6. Evidence that most improves the thesis: exact reproduction from posted data, plus AR sets.
7. Evidence that most threatens it: Albouy 2012 (CONTESTED), specifically its own-data subsample with controls, which my computation reproduces qualitatively.

I. REVISED THESIS PARAGRAPH
AJR (2001) measure the 1995 log income of 64 former colonies against a 1985–95 foreign-investor expropriation-risk rating, instrumented by 19th-century soldier, bishop and laborer mortality, much of it assigned across countries. They report a 2SLS coefficient of 0.94 (SE 0.16).
- Direct evidence: the coefficient reproduces exactly from posted data, and its weak-IV-robust 95% set (≈0.70–1.43) excludes zero.
- Construct gap: the gap lies in the abstract's relabel of one rating as "institutions" (disclosed in fn 3; supported by companion tables not retrieved here). It does not lie in the Table 4 estimate.
- Strongest opposition: Albouy (2012, CONTESTED by AJR 2012). It shows that restricting to own-country mortality data and adding campaign/laborer indicators with geographic controls leaves the instrument too weak to bound the effect. This audit reproduces that pattern on AJR's posted data.
- Support for a narrower version: AJR's capping at Tulloch's 250/1,000 or dropping the Gambia outlier restores bounded estimates of about 0.73–0.95 in all but the smallest cell, again reproduced here. Which data construction is historically correct is a judgment the record has not settled.
- Inference not tested: the causal reading rests on an exclusion restriction. The paper tests it against named channels, and it is untestable in general.
- Decisive test: blinded independent recoding of the 36 assigned rates, re-estimated with weak-IV-robust inference and bounded-exclusion sensitivity.
- Citation-network handling of the opposition: not assessed.

J. FINAL ADVERSARIAL VERDICT
- Strongest opposition to the foundational claim: Albouy 2012, CONTESTED (rebutted by AJR 2012; no rejoinder retrieved). Assessed by full-text reading and a mechanical approximation on posted data.
- Strongest support for the foundational claim: exact reproduction plus col. 1 AR set (this audit's computation), and AJR 2012 capping/recoding (CONTESTED; mechanically reproduced).
- Strongest neglected adjacent-field evidence: none established. The human-capital channel was recalled only (PROVISIONAL).
- Strongest paper the hub should have cited: not assessed.
- Most important non-citing opposition: not searched.
- Did the field engage the opposition? Yes, at the author level: the AER published the Comment and Reply together. Field-wide uptake was NOT ASSESSED.
- Suppression: no suppression claim is made. Albouy did not "survive" reception unrebutted. It is contested, which is not marginalization.
- Did the opposition change the thesis? Yes, it narrows the robustness claim for the restricted subsample. It does not change Field 6 in the base sample.
- Source self-defense (E0): DEFEATED IV-2 (fn 18); NARROWED IV-7 (fn 21, PDF p. 20), CV-3 (PDF p. 28); RECHARACTERIZED IV-1 (fn 17, PDF p. 16), IV-6 (PDF pp. 4, 24, 26), CV-1 (fn 3, PDF p. 3; fn PDF p. 11); UNAFFECTED IV-3, IV-4, IV-5, CV-2.
- Version the prosecution attacked: mostly Field 6, with three findings re-aimed to Field 2.
- Failure location: PAPER (data construction; untested-in-general assumption; abstract wording). MIXED for the open coding dispute.
- Does severity survive re-aiming? IV-1 survives at reduced severity, and the rest are minor or none.
- Finding-target alignment (G2): 6/10 on Field 6, 3 re-aimed, 1 MAP GAP.
- Internal-validity coverage: SUPPLIED AND CONSUMED.
- Citation-network coverage: NOT SUPPLIED (stage not run). Any claim about field-wide uptake, suppression or citation laundering is unchecked.
- Double-count resolution: IV-6 and CV-2 nested; IV-1 retained as an independent lever.
- Revised thesis impact category: C (softened).
- Claims to remove: IV-2 as a charge.
- Claims to narrow: IV-1 (subsample + controls + Albouy coding), IV-7, CV-1, CV-3 (Field 2).
- Claims strengthened: the col. 1 reproduction and weak-IV-robust acquittal.
- Three most threatening findings: IV-1 (FULL-TEXT-CONFIRMED + COMPUTED; CONTESTED), IV-6 (PROVISIONAL; capped, pending), CV-1 (PROVISIONAL; Field 2 only).
- Main remaining source-risk:
  - Part B approximates Albouy with AJR's posted dataset rather than Albouy's own package;
  - the mortality-coding history was not independently reviewed;
  - the PRS items were not retrieved.
- Confidence level: Moderate.
- What would change this assessment:
  - Albouy's package showing materially weaker results than my approximation;
  - an independent historical recoding siding with either party;
  - retrieved direct-channel evidence against exclusion.

J2. SELF-TILT DISCLOSURE
- Direction of lean: toward the paper, mildly. I softened IV-1 partly on the strength of the authors' own reply, which is a party to the dispute. I tested the reply mechanically, but whether capping is legitimate is a judgment I did not independently adjudicate.
- Least reception-checked findings: IV-6 and the human-capital alternative (memory); the 2017 "Graphs" paper (title only); the claim that "weak-IV diagnostics were not standard in 2001" (memory).
- Sources introduced and promoted: the AJR 2012 Reply (as support). It was gated as CONTESTED, the same standing as Albouy. My own computations were also introduced, and nobody has gated them: they are a single-run, single-agent analysis.
- Search order: E0 (source self-defense) was run before E1. The sections searched are listed in E0. Not every row came back UNAFFECTED.
- Did I let the prosecution's target stand because it fit expectations? The pre-registration predicted an UNRESOLVED/CONTESTED internal-validity outcome. The final record (B–C, CONTESTED) matches that prediction, and that agreement is itself a risk of confirmation.
- What a counter-audit of this counter-audit would flag first: one agent wrote the prosecutors and the balancer in one session, so there is no structural independence.
- The assumption most likely to be wrong: that my Part B variable mapping (source0 = own-country, campaign/slave = Albouy's indicators, clusters = shared mortality value) faithfully approximates Albouy's specifications.

K. FINAL ONE-PARAGRAPH SUMMARY
The strongest counter-evidence to the Table 4 estimate is Albouy's (2012) mortality-data critique. It is contested by AJR's (2012) reply, and both sides' central quantitative claims reproduce qualitatively on AJR's own posted data. Under Albouy's own-data subsample with campaign indicators and a latitude control, the instrument is too weak to bound the effect. Under AJR's capping or outlier exclusion, it is not, except in the smallest cell. This weakens the internal-validity prosecutor's "material narrowing" label without eliminating it. It leaves the base-sample estimate intact: it reproduces exactly, and its weak-IV-robust set excludes zero. The construct-side concerns apply to the abstract's "institutions" wording rather than to Field 6. The field engaged the opposition at the author level, with the AER publishing the Comment and Reply together. Wider uptake was not assessed because the citation-network stage was not run. The most defensible revised position: the 0.94 estimate is a reproducible, well-identified result in the authors' data construction. Its precision depends on contested historical-coding choices, and its causal reading rests on an exclusion restriction that is tested against named channels but untestable in general. None of these verdicts is established; they are single-agent, model-produced judgments for human adjudication.
