**INSTRUMENT PREFLIGHT:** prompts/1-claim-extraction.txt (attached as 1-claim-extraction.txt; retrieval form ATTACHED) @ commit 12cb73fe0de8eca063661cf9d0c83d19bef9381a (operator-supplied; not resolved in this run) | blob/hash UNAVAILABLE | UNAVAILABLE lines | UNAVAILABLE bytes | markers PRESENT | INSTRUMENT VERSION UNVERIFIED

- **Hash.** Not computed. This run has no code or hashing tool, so I did not compute the attached file's SHA-256, line count or byte count, and I made no comparison. The operator-supplied values are recorded as supplied: SHA-256 656b11c301931726a5435b231774f40797a10fd0cab950224616fc18951c035f; git blob 894579a79e67508bdc4026b77c0a104681f903ad; 1038 lines; 44072 bytes.
- **Marker.** "CLAIM EXTRACTION / INFLATION MAP" is present.
- **Collision.** None observed. No identity check could be performed, so none could fail.
- **Disposition.** The run names an immutable commit, so it is treated as formal/logged. Because the identity is unverified, exploratory execution proceeds. This output may not be logged as evidence for the instrument at commit 12cb73f… until the attached file's SHA-256 is computed and matched.

---

## 1. WHAT WAS LITERALLY MEASURED

**Design.** A between-subjects laboratory experiment that the authors call a "conceptual replication" of Carney et al. (2010) [A1.1]. Each session had one participant, randomly assigned to a high-power-pose or low-power-pose condition [A1.2].

**Sample.**
- N = 200: 98 women and 102 men [A1.3].
- An initial power analysis on Carney et al.'s effect sizes (power 0.8, α = .05) gave a target of 100 [A1.4].
- A further 100 were added "on the basis of the results of these first 100 observations." The paper does not say which results, or what decision rule, were used [A1.5].
- Not stated in the main text: recruitment source, participant population, age, site or country, data-collection dates, payment currency [A1.6].

**Manipulation.**
- Two body positions "taken from those in Carney et al.", held while doing a filler task [A1.7]. The postures themselves are not described in the main text.
- Each position was held 3 min, versus 1 min in Carney et al. [A1.8].
- Participants were instructed by computer, not configured by the experimenter [A1.9]. The experimenter was blind to condition [A1.10].
- The filler task was constructing words from letters and spaces [A1.11].
- Compliance was checked from recordings [A1.12]. One participant did not fully comply; excluding them "yielded similar results" [A1.13].
- No deception was used. The consent form said the study examined whether physical position influences hormone levels and behavior [A1.14].
- Sessions ran 12:00–6:00 p.m. Participants were told not to eat, drink or brush their teeth in the hour before [A1.15].

**Sequence.** Saliva sample 1 [A1.16] → poses plus filler task → risk task, gain domain then loss domain [A1.17], in fixed order [A1.18] → competition choice [A1.19] → saliva sample 2 and postexperiment questionnaire, before payment [A1.20].

**Outcomes** (unit of analysis: the individual participant).
- **Testosterone and cortisol.**
  - Saliva was collected by passive drool, before and about 17 min after the manipulation, and frozen immediately [A1.21, A1.22].
  - Testosterone was analysed as change, Time 2 − Time 1, in pg/ml [A1.23].
  - For cortisol, the units are not stated, nor whether level or change was analysed. No assay is named for either hormone [A1.24].
  - Two samples were undetectable or lost [A1.25]. Both hormone tests have df = 196.
- **Risk tolerance.**
  - Six binary choices per domain.
  - Gain domain: a predetermined win versus a 50/50 gamble for a greater win or nothing [A1.26].
  - Loss domain: a predetermined loss versus a 50/50 gamble for a greater loss or no loss [A1.27, A1.28].
  - Measure: proportion of risky choices in each domain [A1.29].
  - The tasks were incentivized [A1.30]. Amounts are not given in the main text [A1.31].
- **Willingness to compete.** A binary choice to do math exercises under a tournament or a noncompetitive payment scheme [A1.19, A1.32].
- **Self-reported feelings of power.**
  - Measured in the postexperiment questionnaire on a 4-point scale, from 1 "not at all powerful" to 4 "very powerful."
  - Item wording and number of items are not given [A1.33].
  - Missing for 5 participants [A1.34].

**Analysis.**
- Two-tailed t tests between conditions [A1.35].
- Nonparametric, regression and by-sex analyses appear only in the Supplemental Material [A1.36].
- Carney et al.'s effect sizes, on which both power statements rest, are not reported in the main text [A1.37].
- Subtraction order is stated only for self-report (high minus low). Figure 1's bars, read visually, fit the same order for risk and testosterone [A1.38]:
  - risky-choice proportion ≈ .46 low vs ≈ .43 high;
  - testosterone change ≈ 6.8 vs ≈ 2.7 pg/ml.

**PUBLICATION STATUS:** not checked. There is no retrieval in this run [A1.39].

### Definition-operationalization check

**Power posing** (central construct; the manipulation)
- **Definition:** "physical postures that express power and dominance (power poses)" [AD.1].
- **Items:**
  - "two body positions, taken from those in Carney et al." [A1.7];
  - the only content description is "poses suggesting either high or low power" [AD.2];
  - the postures are given in Carney et al. and the Supplemental Material, and neither is attached.
- **Retrieval basis:** ITEMS-INFERRED. The items were not read, so any scope reading would rest on a related study.
- **Scope result:** UNKNOWN. No classification made.

**Risk tolerance / financial risk taking** (outcome; named in the title)
- **Definition:** no conceptual definition. The operational definition is "Our measure of risk tolerance was the proportion of risky choices made in each domain" [A1.29]. The body also calls this "financial risk taking" [A2.6].
- **Items:** the choice format and coding rule were read [A1.26–A1.29]. Stake amounts are not in the main text [A1.31].
- **Retrieval basis:** ITEMS-RETRIEVED for the format and coding rule; amounts not retrieved.
- **Scope result:** coextensive, by stipulation, because the paper's only definition is the measure itself.

**Hormonal levels** (outcome; "Hormones" in the title)
- **Definition:** none. The body names them as "levels of hormones such as testosterone and cortisol" [AD.3].
- **Items:**
  - salivary testosterone and cortisol, by passive drool, before and about 17 min after posing;
  - testosterone analysed as change in pg/ml [A1.21–A1.23];
  - cortisol units and form not stated [A1.24].
- **Retrieval basis:** ITEMS-RETRIEVED for the sampling procedure and the testosterone change score; partial for cortisol.
- **Scope result:** coextensive with the two analytes the body names. The title's "Hormones" is a broader label. That is recorded in 5A rather than here, because no definition refers to hormones in general.

**Self-reported feelings of power** (outcome; manipulation check)
- **Definition:** none beyond the label.
- **Items:** response anchors read; item stem and number of items not given [A1.33].
- **Retrieval basis:** ITEMS-INFERRED.
- **Scope result:** UNKNOWN.

**Willingness to compete** (outcome)
- **Definition:** "Willingness to compete was measured from this binary choice" [A1.32]. This is operational.
- **Items:** the choice format [A1.19].
- **Retrieval basis:** ITEMS-RETRIEVED.
- **Scope result:** coextensive, by stipulation.

No measure is classified broader, so no definitional scope creep is recorded.

### Construct-establishment check

NOT TRIGGERED. The source makes experimental-effect claims: an effect on self-report, and no significant effect on hormones and behavior. It does not escalate to a normative or causal claim about a construct; there is nothing of the form "this belief is harmful" or "reducing it reduces X." The five property rows are therefore N/A. This is a judgment call, flagged in the Read Record.

---

## 2. STRONGEST CLAIM THE SOURCE ITSELF MAKES

**Strongest form: the title (p. 1).** "No Effect on Hormones and Risk Tolerance in a Large Sample of Men and Women" [A2.1]. It is unhedged and scoped to the sample.

**Summary form: the untitled opening section, which serves as the abstract in this Commentary (p. 1).**
- "we found no significant effect of power posing on hormonal levels or in any of the three behavioral tasks" [A2.2].
- A "significant effect of power posing on self-reported feelings of power" [A2.10].
- Power "more than 95%" to detect an effect of Carney et al.'s magnitude [A2.13].

**Results form (p. 2).**
- "no significant impact of physical position" on gain-domain risk and on testosterone change, with confidence intervals [A2.3].
- "We also found no effect for cortisol" [A2.4]. This is the one Results sentence without "significant."
- The other two tasks showed no "significant differences" [A2.5].
- Self-report was replicated, d = 0.344 [A2.11], which "suggests that the power-posing manipulation worked" [A2.12].

**Discussion form (pp. 2–3).**
- "we failed to confirm an effect of power posing on testosterone, cortisol, and financial risk taking" [A2.6].
- The self-reported power effect "did not yield behavioral effects" [A2.7].
- It is "certainly plausible" that effects arise "only under some specific conditions—and our study failed to include one or two of these" [A2.8].
- "more research is needed to identify the precise conditions necessary for such effects" [A2.9].

**How the hedges differ.** The title is the most categorical. The opening and Results use significance language, except for the cortisol sentence. The Discussion is the most hedged. The text does not settle which of these is "the claim" (Rule 5). Field 6 resolves that by the Rule 2 default, not by judging what the authors meant.

## 3. WEAKER DEFENSIBLE CLAIM THE EVIDENCE ACTUALLY SUPPORTS

*Author reconstruction from Field 1.*

**Setting.** One laboratory study of 200 participants (98 women, 102 men). Population, recruitment, site and dates are not stated. Participants were randomly assigned to hold two high-power or two low-power postures for 3 min each. The postures:
- were taken from Carney et al. and are not described in the main text;
- were instructed by computer, with the experimenter blind to condition;
- were held during a word-construction filler task;
- were run with the study's purpose partly disclosed, in afternoon sessions.

**Results under that setting.**
- **Self-reported power:** higher in the high-power condition on a 4-point self-report taken after all tasks. Mean difference 0.245, 95% CI [0.044, 0.446], d = 0.344, n = 195.
- **Testosterone:** no statistically significant difference (two-tailed t test, α = .05) in change in salivary testosterone from before to about 17 min after posing. −4.077 pg/ml, 95% CI [−9.801, 1.647], d = −0.200, df 196.
- **Cortisol:** no significant difference. −0.028, 95% CI [−0.078, 0.022], d = −0.157, df 196; units and level-versus-change not stated.
- **Gain-domain risk:** no significant difference in the proportion of risky choices across six 50/50 monetary gambles. −0.033, 95% CI [−0.085, 0.019], d = −0.176, df 198.
- **Loss-domain risk and the binary tournament choice:** no significant differences; statistics not in the main text.

**Scope limits.**
- The CIs give the range of condition differences the data remain compatible with.
- The main text does not report Carney et al.'s effect sizes. How these intervals relate to the original estimates therefore rests on the supplement's power computation, which is not attached.
- The finding covers this protocol. The paper itself lists four ways the protocol differs from Carney et al.'s, so the finding does not by itself speak to Carney et al.'s procedure or other conditions.

**Item tracking.**
- **Postures:** ITEMS-INFERRED. The item-level defensible claim (which specific postures produced these results) is UNKNOWN pending retrieval of the posture specification.
- **Self-reported power:** the item-level claim is UNKNOWN pending item retrieval.
- **Risk, competition and hormones:** no definition-operationalization mismatch was recorded, so the measures are tracked as stated.

## 4. BROADER CLAIM ATTACHED DOWNSTREAM

**No downstream uses retrieved — inflation analysis limited to the source itself.**

This reflects NO RETRIEVAL CAPABILITY in this run (run condition A). It is not evidence that no downstream use exists. No searches were run, so NONE FOUND does not apply. Nothing was supplied, so SUPPLIED does not apply.

**RECALLED:** no item entered. I have prior exposure to this paper and to material about it from training data. The run instructions bar memory as a source, so I record no recalled downstream item, quotation or pattern, and nothing recalled informs Field 5.

**Field 4: PROVISIONAL.**

## 5. WHERE THE INFLATION BEGINS

### 5A — Within-source

Established from the paper alone; not provisional.

**Move 1 — qualifier removal.** The closest instrument label is inferential upgrade: a non-rejection at α = .05 becomes, in the title, an unqualified "No Effect."
- **Source wording:**
  - Results: "no significant impact" on testosterone change, CI [−9.801, 1.647] [A2.3];
  - opening: "no significant effect … on hormonal levels" [A2.2];
  - Discussion: "failed to confirm" [A2.6].
- **Title wording:** "No Effect on Hormones and Risk Tolerance in a Large Sample of Men and Women" [A2.1]. The title keeps the sample qualifier.
- **Second occurrence:** the Results use the unqualified form once, for cortisol: "We also found no effect for cortisol" [A2.4].
- **Prominence asymmetry:**
  - the most categorical wording sits in the most prominent place;
  - the Discussion adds that effects may arise only under conditions the study may have omitted [A2.8].
- **Failure location:** PAPER (the title, and one Results sentence).
- **Ambiguity:** the title can be read as a sample-scoped report that nothing was detected, rather than an assertion that no effect exists. The text does not settle which reading is intended.

**Move 2 — label generalization in the title.**
- **What was measured:** change in two salivary analytes, testosterone and cortisol.
- **Title term:** "Hormones."
- **Body term:** "hormones such as testosterone and cortisol" [AD.3].
- **Failure location:** PAPER (title). Whether this is material or conventional title shorthand is for the prosecutors.
- **"Risk Tolerance":** no move is recorded, because the body uses that term as the stipulated name of the measure [A1.29].

**Ambiguous, not classified.** "this did not yield behavioral effects" [A2.7] is unhedged, and its referent is unclear:
- if "this" is the self-reported power change, the sentence states a pathway that was not separately tested in the main text;
- if "this" is the posing manipulation, the sentence restates the condition-level nulls.

### 5B — Downstream

PROVISIONAL; not assessed. No SUPPLIED or RETRIEVED downstream item exists, because the run has no retrieval capability. No layer is SUSPECTED, since no item, recalled or otherwise, was entered. No downstream failure location is assigned.

What would settle it: retrieving citing sentences together with their citations (citing literature, PR/media, policy, model summaries), and running the attribution check on each.

### Anchoring table

| Item | Provenance state | Quotation? | Locator? | Attribution cross-source-confirmed? | Anchor eligibility |
|---|---|---|---|---|---|
| Title (A2.1) | SUPPLIED (audited source) | yes | yes | N/A | ELIGIBLE, within-source |
| Results, testosterone (A2.3) | SUPPLIED (audited source) | yes | yes | N/A | ELIGIBLE, within-source |
| Results, cortisol (A2.4) | SUPPLIED (audited source) | yes | yes | N/A | ELIGIBLE, within-source |
| Discussion, conditions (A2.8) | SUPPLIED (audited source) | yes | yes | N/A | ELIGIBLE, within-source |
| Downstream items | none entered | — | — | — | None exist, so no downstream location can be assigned |

---

## CLAIM INVENTORY

| # | Claim | Quantified? | Why it might be inflated downstream | Field 6? |
|---|---|---|---|---|
| C1 | Title: no effect on hormones and risk tolerance in a large sample of men and women | No (N given in body) | Categorical headline; sample and protocol qualifiers are easy to drop | No. It is the unquantified form of C2–C4 |
| C2 | No significant difference in testosterone change (−4.077, 95% CI [−9.801, 1.647], p = .162, d = −0.200) | Yes | Non-significance can be restated as demonstrated absence; protocol differences can be dropped | **Yes** |
| C3 | "no effect for cortisol" (−0.028, CI [−0.078, 0.022], p = .272, d = −0.157) | Yes | Already worded "no effect"; units and measure form unstated | No (deferred) |
| C4 | No significant difference in gain-domain risk choices (−0.033, CI [−0.085, 0.019], p = .215, d = −0.176) | Yes | Can be generalized to risk-taking at large; the measure uses 6 choices where Carney used 1 | No (deferred; next run) |
| C5 | No significant differences in loss-domain risk or willingness to compete | No (statistics in supplement) | Unquantified null; easily generalized to "no behavioral effects" | No (deferred) |
| C6 | Significant effect on self-reported power (0.245, CI [0.044, 0.446], p = .017, d = 0.344); "suggests … the manipulation worked" | Yes | Can be generalized beyond a 4-point rating taken after all tasks | No (deferred) |
| C7 | Power above 95% to detect an effect of Carney et al.'s magnitude | Yes | Can be restated as a definitive non-replication; the computation is not in the main text | No (deferred; see Field 6) |
| C8 | Self-reported power "did not yield behavioral effects" | No | Can be restated as "feeling powerful doesn't change behavior" | No (deferred) |
| C9 | Blinding "negated potential experimenter effects" | No | Can be restated as ruling out experimenter effects as the explanation of the original result | No (deferred) |
| C10 | The self-report effect "indicates" procedures did not influence at least one measure | No | Can be restated as procedures not mattering for any outcome | No (deferred) |
| C11 | It is plausible that effects arise only under specific conditions; more research is needed | No | Can be restated in either direction, or omitted | No (deferred) |
| C12 | Similar results by sex and in nonparametric, regression and comfort-restricted analyses | No (supplement) | "Men and Women" in the title can be restated as a demonstrated null in each sex | No (deferred) |

The paper's descriptions of other studies (Carney et al., Cuddy et al. 2012, Cesario & McDonald 2013) characterize cited work. They are not findings of this source, so they are not inventoried.

**Selection.**
- Rule 1 bars C1, because it bundles two outcome families. Rule 2 prefers a quantified version, and C2, C3 and C4 are equally quantified.
- C2 gets priority for four reasons:
  - the title names "Hormones" first;
  - testosterone is one of the two outcomes the authors chose to plot in Figure 1;
  - its measurement chain is fully specified in the main text, whereas C3 lacks units and measure form and C4's stakes are in the supplement;
  - its sentence carries the "no significant" wording, so the 5A move can be tested on it directly.
- C4 is the strongest alternative and should be the second run.
- The unselected claims are deferred, not dismissed.

## 6. WHICH CLAIM IS THIS AUDIT EVALUATING?

**Claim.** In this sample, two-tailed t tests indicated no significant impact of physical position (high- versus low-power pose) on change in salivary testosterone from before to about 17 min after the manipulation (mean difference = −4.077 pg/ml, 95% CI = [−9.801, 1.647], t(196) = −1.405, p = .162, Cohen's d = −0.200).

- **Target type.** This is the source's own claim (Field 2 level) at its most precisely quantified form. It needs no downstream material and is not provisional.
- **Relation to the title.** The title's "No Effect on Hormones" is the unquantified form of the same claim. Comparing the two is how a prosecutor tests Move 1 in 5A.
- **The power claim.** C7 bears on how this null is read, but it is a separate claim (Rule 1). A prosecutor who needs it should flag that rather than fold it in.

---

## REQUIRED OUTPUT TABLE

| Field | Content | Verification state |
|---|---|---|
| 1. Literally measured | Randomized two-condition lab experiment, N = 200 (98 women, 102 men), one participant per session. Two postures from Carney et al., held 3 min each. Outcomes: salivary testosterone and cortisol (before and about 17 min after), proportion of risky choices (6 gain, 6 loss, 50/50 gambles), tournament choice, 4-point self-reported power. Two-tailed t tests. Population, site, dates, postures, stakes and item wording not stated in the main text | FULL-TEXT-CONFIRMED (main text). Supplement-dependent details are PROVISIONAL (not attached) |
| 2. Source's strongest claim | Title: "No Effect on Hormones and Risk Tolerance…". Body: "no significant effect", "failed to confirm". Discussion: effects "certainly plausible" under specific conditions; "more research is needed" | FULL-TEXT-CONFIRMED |
| 3. Weaker defensible claim | In this protocol and sample, self-reported power was higher (d = 0.344). No significant difference in testosterone change, cortisol or gain-domain risk (CIs as reported). Other tasks not significant | author reconstruction from Field 1 |
| 4. Downstream claim | None retrieved. Limitation is NO RETRIEVAL CAPABILITY, not absence of use | PROVISIONAL |
| 5A. Within-source | "no significant impact" / "failed to confirm" → title "No Effect" (also once in Results, for cortisol). Secondary: two analytes → "Hormones". PAPER | FULL-TEXT-CONFIRMED (wording read; materiality not assessed) |
| 5B. Downstream | Not assessed; no anchor-eligible items | PROVISIONAL |
| 6. Claim under audit | Testosterone-change null as quantified in Results | FULL-TEXT-CONFIRMED that the source states it. Statistics not recomputed; OSF data not accessed |

## CONSTRUCT-SIDE HANDOFF SUB-SCHEMA

| Check | Object | Retrieval status / basis | Result | Verification state | Evidence |
|---|---|---|---|---|---|
| Construct establishment | PREVALENCE | N/A, check not triggered | — | — | No normative or causal escalation (Field 1) |
| Construct establishment | FORM | N/A, check not triggered | — | — | Same |
| Construct establishment | DOMAIN | N/A, check not triggered | — | — | Same |
| Construct establishment | WRONGNESS | N/A, check not triggered | — | — | Same |
| Construct establishment | HARM | N/A, check not triggered | — | — | Same |
| Definition-operationalization | Power-posture manipulation | ITEMS-INFERRED | UNKNOWN | Definition FULL-TEXT-CONFIRMED; items PROVISIONAL | AD.1, AD.2, A1.7 |
| Definition-operationalization | Risk tolerance: proportion of risky choices | ITEMS-RETRIEVED (format and coding rule; not amounts) | coextensive (by stipulation) | FULL-TEXT-CONFIRMED | A1.26–A1.29, A1.31 |
| Definition-operationalization | Salivary testosterone and cortisol | ITEMS-RETRIEVED (procedure; cortisol units and form unstated) | coextensive with named analytes | FULL-TEXT-CONFIRMED | AD.3, A1.21–A1.24 |
| Definition-operationalization | Self-reported power, 4-point scale | ITEMS-INFERRED | UNKNOWN | PROVISIONAL | A1.33 |
| Definition-operationalization | Willingness to compete: binary choice | ITEMS-RETRIEVED | coextensive (by stipulation) | FULL-TEXT-CONFIRMED | A1.19, A1.32 |
| Grade-before-assert | None; no belief sub-claim at issue | N/A | not graded | — | P2: VOID. No sub-claim exists to grade, and no wrongness or pathologization finding is at issue |

**CLAIM UNDER AUDIT:** In this sample, two-tailed t tests showed no significant difference between the high- and low-power-pose conditions in change in salivary testosterone from before to about 17 min after posing (mean difference = −4.077, 95% CI [−9.801, 1.647], t(196) = −1.405, p = .162, d = −0.200).

**WITHIN-SOURCE FAILURE LOCATION:** paper. The title restates "no significant impact" as "No Effect", as does one Results sentence for cortisol. FULL-TEXT-CONFIRMED (wording read; materiality not assessed).

**DOWNSTREAM FAILURE LOCATION:** not assessed. No SUPPLIED or RETRIEVED items, because the run has no retrieval capability. PROVISIONAL.

**GAP TYPE:** source overclaims, at title wording only, and only if "No Effect" is read as asserting absence rather than reporting non-detection in the named sample. Downstream not assessed.

**MAP CONFIDENCE:** moderate. It would rise with:
- the instrument hash computed;
- the Supplemental Material attached (postures, stakes, questionnaire, the power computation including Carney et al.'s effect sizes, by-sex and comfort analyses);
- retrieval enabled for Field 4;
- a human decision on whether the title or the Results wording is "the claim."

---

## SOURCE ANCHORS

**Conventions.**
- Text is copied from the PDF's text layer. Page images were available for pp. 1 and 3 only, and I checked quotes from those pages against them.
- Line-end typesetting hyphens are removed, as in the text layer. One line break that falls on a genuine compound hyphen is flagged (A1.2).
- Doubled spaces from justified lines (e.g., "et  al.") are rendered as single spaces.
- Italics cannot be shown.
- Quotes end before superscript footnote markers.

**Field 1**

**A1.1** · Design: conceptual replication · p. 1, untitled opening section
> [QUOTE WITHHELD: source-light; sha256 3db5e077fd097412ccb04ae1a89203dd21b87f2a9b89672bea4a0c8330104765; 217 chars]

**A1.2** · Design: random assignment, one participant per session · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 615a59f544213ea24e12e5fa1b0f4f9b43d7f19261389f21f138d09b30c2d144; 114 chars]

(Flag: the page image shows "low-power-" at a line end; the text layer reads "low-powerpose". The hyphen is kept.)

**A1.3** · Sample composition · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 350bc8986302e7019183ba9d70844d88beaf2692f28ae36ae0ad03df40e3cd12; 54 chars]

**A1.4** · Initial power analysis · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 7171d85aecc746a975f739ff176a1e222b94fd000ea4bd74f9541e28af5e16de; 159 chars]

**A1.5** · Second 100 added on interim results · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 58c3381b000c44b9432e4558a99642ef45496f159a5b13d5ebce520328f73faf; 169 chars]

**A1.6** · Population, recruitment, age, site, dates, currency not stated · no passage. This is an absence finding; pp. 1–4 were read in full.

**A1.7** · Two positions from Carney et al. · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 0ef9cdd511312268d375da0fedcbdb84ce4145506e34c8c9c27c11f8d0ecaf9f; 104 chars]

**A1.8** · 3-min hold · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 9e3955d3b44a3e9cd1d4ca5dea071848a30f63ae8965c240c2ccc343f4f94407; 114 chars]

**A1.9** · Computer instructions · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 7dd208c2c8aac1f9745624ae1ae00260ac55a4692e8a3930f4ecc113a33db704; 161 chars]

**A1.10** · Experimenter blind · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 57f89b4bb3e9b58b8064c41ba0516301bc7facc2cd82efb79c0572a6c93940ef; 149 chars]

**A1.11** · Filler task · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 c1d9187ea3475a07fd853c8ee7c62a0368b5ac4390ee652c74a0cb3da0b28372; 157 chars]

**A1.12** · Compliance recordings · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 f43ee0af9fa15af8d8ba9a24bf03ce729aa9675cd0f3ea2fb38589af0194d4ef; 74 chars]

**A1.13** · One partial non-complier · p. 4, Notes (note 1)
> [QUOTE WITHHELD: source-light; sha256 24130889712c73c788cf327c3068ae41dda66e58eed39bc994cfe91b03e913b2; 118 chars]

**A1.14** · No deception; purpose disclosed · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 62a373a548ae65d2bb5c205541d96b4e2eb783a3d5d327348e4b61fa8139748b; 181 chars]

**A1.15** · Session timing and restrictions · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 9ea3b79bb1141fd4f4bf8957aeb0f918e12deb8d1f8eaa293783e551f0726f66; 152 chars]

**A1.16** · First saliva sample · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 2573b81dca2d2f10fd7485973baf2e388547da3278b092ff7a1031e64ab20ee8; 63 chars]

**A1.17** · Risk task in both domains · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 8651303dc0660f8db099173c62b65aa85ccc56e8c9f1d99a83dcf49f951ee4d8; 107 chars]

**A1.18** · Fixed task order · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 7cb336f8d3e1b273f572cfe9b88cd805421d1f80b44f9fba9ac3e311f0156b0f; 115 chars]

**A1.19** · Competition choice · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 54da7011ed97a31690b6f9c221e719e6ff4e50af99ef7134df493e7b6a553f85; 231 chars]

**A1.20** · Second saliva sample and questionnaire · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 5325730263c060d0174a55a9bd15dc91769d6125ff589ad7d99741a894d4c3e3; 166 chars]

**A1.21** · Saliva timing · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 a56a80a1c53aa0d20f215e220eb7ec703ae34e5261fe12ee9b94423012113128; 92 chars]

**A1.22** · Collection procedure · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 50567f75fe78fbdf02c154c3bf35aab57197ebd7bf989bce49402bf54f2332fa; 94 chars]

**A1.23** · Testosterone change score and unit · p. 3, Figure 1 (axis label)
> [QUOTE WITHHELD: source-light; sha256 9f532721940df11cd9235909dbe8627cd15a714917ea7e600bbc7d786d342d0f; 31 chars]

**A1.24** · Cortisol units and form, and assay, not stated · no passage. Absence finding.

**A1.25** · Missing hormone samples · p. 4, Notes (note 3)
> [QUOTE WITHHELD: source-light; sha256 c8b78c4bb434828c58fab26c70ddfe264d64d3dfe8031b1fbe27bd3c38ff7094; 134 chars]

**A1.26** · Gain-domain choice format · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 32f2aad7b9ef6bf631c9b272fa0712d686ce82684c7718e70fc2ce9e9d285672; 185 chars]

**A1.27** · Loss-domain choice format · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 729f14a78cd008d6fba60d969c41c6bd9b629b5acc307b00eb836d674657d68f; 170 chars]

**A1.28** · Six choices per domain · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 409ff6a7597fe0090afc0d162142b655605e227211906bd313847a3a5564da2a; 146 chars]

**A1.29** · Risk measure · p. 1, Method
> [QUOTE WITHHELD: source-light; sha256 4f9cd6ce57baf9302e87d7b709ac5cb395e277ba6069287f46179dddb6e56349; 85 chars]

**A1.30** · Incentivized · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 1ebc5eb7ad88a1cd3829896e2a27a610bb6bbea5c2f8b1639f8a334dda3dd5e6; 92 chars]

**A1.31** · Stake amounts not given · no passage. Absence finding.

**A1.32** · Competition measure · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 8fae89da599c1966ff51fbeac2bda7eeb7112127e5319baa82f855e63927766f; 60 chars]

**A1.33** · Self-report scale · p. 2, Method
> [QUOTE WITHHELD: source-light; sha256 bec136dc98d267783f451cdf2bba94391a79654de31215f5389a678c55f06ee1; 148 chars]

**A1.34** · Missing self-report · p. 4, Notes (note 2)
> [QUOTE WITHHELD: source-light; sha256 e020e41c6e38b053f136a81f039bbeb172eb32347dadcabcf6b37cf3017aff90; 68 chars]

**A1.35** · Two-tailed t tests · same passages as A2.11 and A2.3

**A1.36** · Supplementary analyses · p. 2, Results
> [QUOTE WITHHELD: source-light; sha256 a90fd8ed84bc5d57c4d9fd293e69d135c85e8c6a6b84a419ea167b4bb0751c25; 163 chars]

**A1.37** · Carney et al.'s effect sizes not reported · no passage. Absence finding.

**A1.38** · Subtraction order · same passage as A2.11 for self-report. Figure 1 bar heights on p. 3 were read visually; there is no text passage.

**A1.39** · Publication status · no passage; not checked.

**Field 2**

**A2.1** · Strongest form · p. 1, article title
> [QUOTE WITHHELD: source-light; sha256 2670f7509c929d6ef1dbcc47462493326aba73535a8b831843bee455b6aa91f4; 75 chars]

**A2.2** · Summary null · p. 1, untitled opening section
> However, we found no significant effect of power posing on hormonal levels or in any of the three behavioral tasks.

**A2.3** · Results: risk and testosterone nulls · p. 2, Results
> Two-tailed t tests indicated no significant impact of physical position on either risk-taking in the gain domain (mean difference = −0.033, 95% CI = [−0.085, 0.019]), t(198) = −1.245, p = .215, Cohen’s d = −0.176, or changes in testosterone (mean difference = −4.077, 95% CI = [−9.801, 1.647]), t(196) = −1.405, p = .162, Cohen’s d = −0.200.

**A2.4** · Results: cortisol · p. 2, Results
> [QUOTE WITHHELD: source-light; sha256 cf2e3cd0485461b4464575660d63b36511363fb938c8abd3bebd2a959b3c410b; 137 chars]

**A2.5** · Results: other tasks · p. 2, Results
> [QUOTE WITHHELD: source-light; sha256 2ef0d4c5c6ea511892bcb2a0fae7c418a68f671f04b7fa64815010eab7790c53; 87 chars]

**A2.6** · Discussion: failed to confirm · p. 2, Discussion
> Using a much larger sample size but similar procedures as Carney et al. did, we failed to confirm an effect of power posing on testosterone, cortisol, and financial risk taking.

**A2.7** · Discussion: no behavioral effects · p. 2, Discussion
> We did find that power posing affected self-reported feelings of power; however, this did not yield behavioral effects.

**A2.8** · Discussion: conditional plausibility · p. 3, Discussion (continued)
> [QUOTE WITHHELD: source-light; sha256 2a70dac2acaae6d24b5cb1b32b9516d5ec07c51d037f1d2e249b3ec056f982f3; 236 chars]

**A2.9** · Discussion: conclusion · p. 3, Discussion (continued)
> [QUOTE WITHHELD: source-light; sha256 aafda438812f3a9b8d1f6615343d04790d0ee67695e592146d5b921485cfc844; 103 chars]

**A2.10** · Summary: self-report effect · p. 1, untitled opening section
> Consistent with the findings of Carney et al., our results showed a significant effect of power posing on self-reported feelings of power.

**A2.11** · Results: self-report statistics · p. 2, Results
> [QUOTE WITHHELD: source-light; sha256 d49990cf0aee0e6a8b1f582eac5f56100447bc00d0afcbc50d62a5ace94e909a; 331 chars]

**A2.12** · Manipulation-check hedge · p. 2, Results
> [QUOTE WITHHELD: source-light; sha256 809834be2df81ebf007f92b2a86fef69556cf872a647571fa75b544741391c05; 56 chars]

**A2.13** · Power claim · p. 1, untitled opening section
> [QUOTE WITHHELD: source-light; sha256 4cd0b4f4c4b060c8959643718a39ec1fc9643fff71e24a6777e60eff7d3c942f; 102 chars]

**Field 3**

**A3.1** · author reconstruction from Field 1. The statistics it restates are anchored at A2.3, A2.4, A2.5 and A2.11.

**Field 6**

- **A6.1** · Claim and statistics · same passage as A2.3.
- **A6.2** · Unit (pg/ml) · same passage as A1.23.
- **A6.3** · "about 17 min" · same passage as A1.21.
- **A6.4** · "this sample" · same passage as A1.3.

**Definition-operationalization check**

**AD.1** · Power posing definition · p. 1, untitled opening section
> [QUOTE WITHHELD: source-light; sha256 f1b347ed726248b3442356eb5ee2eef10ab167dc580f16ebf4c5516755138aa3; 64 chars]

**AD.2** · Only description of pose content · p. 1, untitled opening section
> [QUOTE WITHHELD: source-light; sha256 95dc7756c274f24a03d4ce2c3cc8e90b7d96b54abf827730f378a169d98d0576; 67 chars]

**AD.3** · Hormones as named · p. 1, untitled opening section
> [QUOTE WITHHELD: source-light; sha256 9cf368b33e247a9f9f957de7d8aa6814f42f33a1b495455a1fecd41e70948d4c; 52 chars]

**Cross-references:**
- power-posing items: A1.7;
- risk definition: A1.29; risk items: A1.26–A1.28; "financial risk taking": A2.6;
- hormone items: A1.21–A1.23;
- self-report items: A1.33;
- competition definition: A1.32; competition items: A1.19.

---

## READ RECORD

**What I read.** All four PDF pages, in full:
- p. 1: title block and untitled opening section; Method begins;
- p. 2: Method continued, Results, Discussion;
- p. 3: Discussion continued, Figure 1 and caption, Author Contributions, Acknowledgments, Declaration of Conflicting Interests, Funding, Supplemental Material notice, Open Practices;
- p. 4: Open Practices continued, Notes 1–3, References.

**What I could not read.**
- **Supplemental Material**, referred to throughout but not attached. It holds the power computation, instructions, consent form, posture details, stakes, questionnaire, nonparametric, regression and by-sex analyses, and comfort reanalyses.
- **OSF data and materials.**
- **Carney et al. (2010)** and the other cited works.
- **Figure 1** has no numeric labels on its bars; I read the values visually from the p. 3 image, so they are approximate. There are no tables.
- **Page images** were available for pp. 1 and 3 only; pp. 2 and 4 were read from the text layer alone.
- **Text-layer artifacts:** dropped compound hyphens ("low-powerpose" on p. 1, "powerposing" on p. 3), doubled spaces, footnote markers rendered as trailing digits, a metadata string on p. 1, and download stamps on every page. No other garbled text.

**What I was unsure how to classify.**
1. **Which statement is "the claim".** Title, Results and Discussion state it at different strengths (Rule 5).
2. **The title's "No Effect".** It may be a sample-scoped report of non-detection or an assertion of absence.
3. **Construct-establishment check.** "Not triggered" is a judgment. The five properties are built for belief constructs, and the paper makes no normative or harm claim.
4. **ITEMS-INFERRED for the postures.** The binary vocabulary forced this label. I made no inference from the label "power pose."
5. **Risk tolerance.** "Coextensive" holds only by stipulation, because the paper's only definition is the measure.
6. **Cortisol.** The paper does not say whether it was analysed as level or change.
7. **Study framing.** The paper calls it a "conceptual replication" (p. 1) and "originally designed as an extension" of Carney et al. (p. 2).
8. **"this did not yield behavioral effects".** The referent is ambiguous.
9. **Opening section.** I treated the untitled opening section as the abstract-equivalent, since a Commentary has no abstract.
10. **Subtraction order.** The paper states it only for self-report.
11. **Sample extension.** The criterion for adding the second 100 participants is unstated.

**Tool use.**
- No tools were used. No code tool was available, so the instrument hash and counts were not computed.
- No web search, connectors or memory were used as sources.
- I have prior exposure to this paper from training data. I stated the Field 6 selection reasons from the text alone, but I cannot rule out that prior exposure shaped what I attended to.