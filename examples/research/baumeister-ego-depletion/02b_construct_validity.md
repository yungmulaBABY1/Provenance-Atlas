# Stage 2b — Construct-Validity Audit: Claim vs. Measurement

INSTRUMENT PREFLIGHT: prompts/research-analysis/2-construct-validity.txt @ commit a58d165d9a986edca220f8143fc0c0d9316c8a13 | blob/hash 7f3db5ed66db3cb4c5ca84f9e71760d134ced9c8 / sha256 8f87676ae76ecf745748a58a7e68b285255c324da25a92a22f3d1a797f6feadb | 1255 lines | 44222 bytes | markers PRESENT ("CONSTRUCT-VALIDITY AUDIT PROMPT:", "CLAIM VS. MEASUREMENT") | IDENTITY CONFIRMED (operator-pinned commit + blob + sha256; immutable-commit retrieval HTTP 200; independently cross-checked by git rev-parse)

Effort: high (as briefed). The full pinned prompt was read before the first version was written (11:24Z). Sibling prosecutor output (02a) was not used as an input. This is an independent Stage-2 run that uses only the Stage 1 map and the sources listed below.

REGENERATION NOTICE: the first version (11:26Z / 03:26 PST) was lost in the box restore at about 11:32Z (03:32 PST). This version was rewritten at 11:57Z (03:57 PST; worklog stage2b-regen) from the same instrument and sources. Surviving passages of the lost version were re-checked and reused where they verified: header, source basis, and closing table rows. The verdict rules (Sections 1A, 13, 14) were re-read in the pinned instrument for this rewrite. Disclosed in 00 under Deviations.

SOURCE RETRIEVAL BASIS: mixed.
- **Target (Baumeister et al. 1998).**
  - ABSTRACT ONLY, via PubMed 9599441. No authorized full text exists (APA 403; no OA copy; unauthorized copies excluded by the rights rule).
  - Introduction, Method, items and Results NOT fetched.
  - Design facts come from authorized secondary descriptions: S1 (first author's LSE slides 2012), S2 (Schimmack 2016), S4 (Hagger et al. 2016, p.548).
- **External sources read in full:**
  - Vohs et al. 2021 (eScholarship, CC BY);
  - Hagger et al. 2016 RRR (Maastricht repository);
  - Dang et al. 2021 (PMC8186735);
  - Carter et al. 2015 (author copy);
  - Baumeister & Vohs 2016 comment (APS-hosted manuscript).
- Nothing load-bearing is recalled from training data.
- Consequence under [P1]: target construct properties are UNKNOWN and target operationalization is ITEMS-INFERRED. Every target-dependent construct-side finding below is therefore PROVISIONAL, not load-bearing, and capped below MAJOR.

| Specific figure | Value stated | Verification state | Source |
|---|---|---|---|
| Exp 1 persistence means (radish / chocolate / no food) | 8.35 / 18.90 / 20.86 min | PROVISIONAL (author slide, secondhand) | S1 |
| Exp 1 N; radish vs chocolate test | 67; t(44) = 6.03, d = 1.80 | PROVISIONAL (critic's reading) | S2 |
| Vohs 2021 manipulation check: effort index | d = 1.31 [1.22, 1.40] (fixed effects) | FULL-TEXT-CONFIRMED | Vohs 2021 Table 3 |
| Vohs 2021 frustration; fatigue; motivation | d = 0.99; 0.25; 0.05 | FULL-TEXT-CONFIRMED | Vohs 2021 Table 3 |
| Vohs 2021 overall depletion effect | d = 0.06 [−0.02, 0.14] | FULL-TEXT-CONFIRMED | Vohs 2021 abstract; Table 4 |
| RRR overall effect | d = 0.04 [−0.07, 0.15] | FULL-TEXT-CONFIRMED | RRR abstract; p.554 |

Applicable-checks note:
- Target document type: peer-reviewed empirical journal article (four experiments).
- Sections that apply: 1, 1A, 2–16. Target-side items are limited by abstract-only access.
- Section 9 (citation use) is limited to the items retrieved in Stage 1 Field 4.

## 1. Claim map (received)

- **Claim under audit** (map field 6): In Experiment 1, participants who ate radishes while resisting chocolate persisted about 8.35 min on unsolvable puzzles vs 18.90 (chocolate) and 20.86 (no food); N ≈ 67; t(44) = 6.03 (d ≈ 1.8).
- **Literally measured** (map field 1): between-condition behavioural differences after different first tasks. The inner resource was not measured.
- **Weaker defensible claim** (map field 3): one small lab demonstration plus three same-direction contrasts, consistent with but not specific to a shared resource.
- **Target layer:** source claim. The map links field 6 to the mechanism layer (L3) through the abstract's conclusion.

No MAP DISAGREEMENT.

## 1A. Construct establishment

Triggered: the abstract escalates from behaviour to mechanism ("common inner resource"; "capacity for active volition is limited").

Assessed from the abstract only. The introduction and the cited establishing work were not fetched.

| Property | Claim-map status | Does the normative / causal claim depend on it? | ESTABLISHED-CITED prosecutor split | Evidence and exact inferential load | Finding disposition |
|---|---|---|---|---|---|
| PREVALENCE | not applicable | No | N/A | — | — |
| FORM | UNKNOWN | Yes: the interpretation of field 6 as depletion of a resource depends on it | N/A (not ESTABLISHED-CITED) | Abstract asserts it. External: in Vohs 2021 the manipulation is strongly felt as effortful (effort d = 1.31) yet produces no downstream decrement (d = 0.06). This is inconsistent with "effort consumes a resource that lowers the next performance" | PROVISIONAL (CV-1) |
| DOMAIN | UNKNOWN | Yes: "a range of seemingly different, unrelated acts share a common resource" | N/A | Inferred from four separate paradigms; no crossed design | PROVISIONAL (CV-2) |
| WRONGNESS | not applicable | No | N/A | No belief graded | — |
| HARM | not applicable | No | N/A | — | — |

Not-firing condition: does not apply. FORM and DOMAIN are load-bearing but UNKNOWN, so [P1] caps them as PROVISIONAL.

## 2. Measurement extraction

- Sample: N = 67, about 22 per cell; undergraduates; single lab (S2).
- Manipulation: eat radishes while resisting chocolate vs eat chocolate vs no food. An experimenter delivers it in a room smelling of baked cookies (S2).
- Instrument: unsolvable figure-tracing puzzles. Participants ring a bell to stop (S2).
- Time scale: one session.
- Outcome: minutes to quitting.
- Controls: cannot assess (body not read). Mood measures are reported to have been taken in the original experiments, per citing works; not verified (PROVISIONAL).
- Exclusions: cannot assess.
- Not measured:
  - any marker of the hypothesized resource;
  - motivation to continue;
  - frustration/affect (cannot assess);
  - hunger;
  - experimenter blinding (not reported in sources read).

The "resource" is not measured. It is inferred from the persistence difference.

Definition–operationalization check:
- Definition: the self's "capacity for active volition", a "common inner resource" (abstract).
- Operationalization: persistence time (Exp 1–2), anagram performance (Exp 3), passive-option choice (Exp 4).
- Retrieval basis: ITEMS-INFERRED. Scope result: UNKNOWN (per [P1]).

## 3. Claim vs. measurement table

| Measured variable | Claimed construct | Are they the same? | Gap | Severity | Notes |
|---|---|---|---|---|---|
| Minutes before quitting unsolvable puzzles | Remaining self-control capacity (resource level) | No | Proxy gap: persistence also reflects motivation, frustration tolerance, boredom, and expectations about the task (R2, R3) | moderate (capped: PROVISIONAL) | CV-3 |
| Four different first-task/outcome pairs | One common resource across "unrelated acts" | No | Domain gap: unity inferred from same-direction results in separate experiments | moderate (capped) | CV-2 |
| Between-condition difference after experimenter-delivered food task | Effect of self-control exertion | Partly | Confounds: hunger, affect, frustration, experimenter expectancy (R4) | moderate (capped) | CV-4 |
| Lecture/lay restatements | "Willpower is limited"; "Like a Muscle"; "One Willpower, not Many" | No | Downstream overextension | moderate | CV-5 (PR-MEDIA) |

## 4. Level-of-analysis check

- Evidence level: short-term within-session behaviour in a lab.
- Claim levels: a general property of the self (abstract), and everyday life (S1, S3).
- Bridging assumptions:
  - (a) the persistence decrement reflects reduced capacity, not reduced willingness;
  - (b) the same capacity serves all acts of volition;
  - (c) lab depletion generalizes to daily life.
- Tested: none, in the target (abstract-level reading).
- External evidence: Vohs 2021 shows a large felt-effort manipulation with no decrement, which weakens (a). (b) and (c) were not tested in sources read.

## 5. Confound audit

| Confound | Domain obvious? | Controlled? | Acknowledged? | Impact if omitted |
|---|---|---|---|---|
| Motivation / opportunity cost (R2) | Yes | Cannot assess | Cannot assess | High |
| Beliefs about willpower / demand (R3) | Yes | No (era) | Cannot assess | Moderate |
| Affect / frustration after resisting food (R4) | Yes | Mood reportedly measured (PROVISIONAL) | Cannot assess | Moderate |
| Non-blind experimenter delivering the manipulation and timing the DV (R4) | Yes | Not reported in sources read | Cannot assess | Moderate |
| Hunger / food intake (radish vs chocolate vs none) | Yes | Cannot assess (pre-session food instructions not retrieved) | Cannot assess | Moderate |

## 6. Ecological validity check

- The lab tasks (radish tasting, unsolvable tracing) are remote from the everyday self-control claims made downstream (S1: daily-life desire resistance; S3: social interactions).
- The time scale is minutes.
- Verdict: **Not ecologically valid for the downstream claim.** Ecologically valid only for a narrower lab-persistence claim.

## 7. Decisive-test check

- What the test measures: an independent marker of the hypothesized resource, measured before and after self-control exertion. Alternatively, a large preregistered sequential-task test that includes manipulation checks separating effort from motivation.
- Supports the claim if: the exertion lowers the marker and the marker mediates the persistence decrement.
- Falsifies the claim if: a strongly effortful manipulation produces no decrement.
- Has it been run? Partly. Vohs 2021 (36 labs; proponent-led) found effort d = 1.31 but outcome d = 0.06. The RRR found d = 0.04. The resource marker itself (glucose) is a separate L3 line not read for this stage.

"The decisive test would be: a large preregistered multi-site sequential-task study with manipulation checks for effort, motivation and affect, and an independent resource marker, testing whether the marker mediates any decrement."

## 8. Cross-reanalysis object check

- **Vohs 2021 vs the target.**
  - Different manipulations (e-crossing, writing) but the same object class (sequential-task decrement). Includes a figure-tracing persistence outcome, the same DV family as Exp 1.
  - Persistence duration d = 0.15 vs ≈ 1.8: same object, much smaller effect.
- **RRR vs the target.** Different paradigm (computerized e-task → MSIT). Authors dispute the manipulation (B&V 2016). Partial object match only.
- **B&V 2016 vs RRR.** The dispute concerns whether the manipulation induced depletion. Vohs 2021 used the authors' preferred paradigms, which narrows this dispute.

## 9. Citation-use audit

| Downstream item | Classification | Note |
|---|---|---|
| LSE slides 2012 (D1/D1b) | Major inflation | Hedge removal ("Willpower is limited") plus added unity ("One Willpower, not Many") and trainability ("Exercise increases strength") |
| APA lay page (D2/D2b) | Moderate inflation | "drained the subjects' self-control" stated as mechanism; "unsolvable" dropped |
| Hagger et al. 2016 p.548 (D3) | Accurate citation | |

## 10. Ignored-literature check

| Ignored literature / evidence | Why it matters | Was it cited? | Effect of omission |
|---|---|---|---|
| Motivation and mental-fatigue literature (R2) | Rival account of persistence decrements | Cannot assess (reference list not read in full; see Stage 2c Section E for metadata-level check) | PROVISIONAL |
| Learned helplessness / uncontrollable failure (R4) | Unsolvable puzzles themselves shorten persistence | Cannot assess | PROVISIONAL |

## 11. Evidence-type / verification / failure-location table

| Claim or evidence item | Evidence type | Measurement role | Verification state | Failure location | Directly measured / inferred / speculative | Source audit required? |
|---|---|---|---|---|---|---|
| Exp 1 persistence decrement | Primary empirical evidence | Proxy evidence | PROVISIONAL (secondhand) | PAPER | Directly measured | Yes (target full text) |
| Common inner resource | Author inference | Citation-dependent premise | ABSTRACT-CONFIRMED (assertion) | PAPER | Inferred | Yes |
| Vohs 2021 effort vs outcome | Primary empirical evidence | Direct measure | FULL-TEXT-CONFIRMED | — | Directly measured | No |
| LSE slides restatement | Public reporting | Other measurement role (restatement) | FULL-TEXT-CONFIRMED | PR-MEDIA | — | No |

## 12. Internal consistency check

The verdict is stated as provisional throughout, because target construct properties are UNKNOWN. No contradictory language was found.

## 13. Concede test

| Finding | Concede test | Surviving claim if NARROWS |
|---|---|---|
| CV-1 FORM (resource) UNKNOWN; external evidence of effort without decrement | NARROWS (capped; PROVISIONAL) | Persistence decrement, mechanism unestablished |
| CV-2 DOMAIN unity inferred across four separate paradigms | NARROWS (capped) | Four task-specific decrements |
| CV-3 Persistence as proxy for capacity | NARROWS (capped) | Persistence, not capacity |
| CV-4 Confounds (hunger, affect, experimenter) | NARROWS (capped) | Condition difference, cause unresolved |
| CV-5 Downstream overextension (lecture/lay) | SURVIVES as to field 6 (PR-MEDIA layer) | — |
| CV-6 Definition–operationalization scope UNKNOWN | NARROWS (capped) | — |

| Finding | Scope-loss level | Original claim | Surviving claim | What practical or inferential work is lost? |
|---|---|---|---|---|
| CV-1 | Material | Resource depleted | Behaviour changed | Mechanism |
| CV-2 | Material | One resource | Task-specific effects | Generality |
| CV-3 | Material | Capacity reduced | Persistence reduced | Construct interpretation |

## 14. Verdict

- Claim under audit: USEFUL-FOR-NARROWER (provisional)
- DEFEATS finding(s): none (target-dependent findings are capped by [P1])
- Failure mechanism: insufficient information
- Surviving residual: "In one small lab experiment, participants who resisted chocolate and ate radishes quit unsolvable puzzles sooner than controls." This is a behavioural persistence difference; the resource and unity interpretations are unestablished.
- Residual usefulness grade: G

Explanation: abstract-only access leaves FORM, DOMAIN and the operationalization scope UNKNOWN. Under [P1], no construct finding can be load-bearing, MAJOR or FATAL. The external evidence (Vohs 2021: a strongly effortful manipulation with no decrement) points against the resource reading, but it cannot convert an UNKNOWN target property into a confirmed failure. Grade G reflects insufficient information, not validity.

## 15. Paper-safe wording

A. Baumeister et al. (1998) reported that participants who resisted chocolate quit unsolvable puzzles sooner, and interpreted this as depletion of a common resource.

B. The resource was not measured; the inference rests on same-direction results across four separate small experiments.

C. Persistence time measures willingness or ability to continue a frustrating task, not a resource level; later large tests found strongly effortful manipulations without subsequent decrements.

D. The construct question would be settled by a large preregistered study with an independent resource marker and manipulation checks for effort, motivation and affect.

## 16. Failure-mode classification

- [x] Untested premise: a limited common resource is assumed, not measured.
- [x] Proxy problem: persistence stands in for capacity (PROVISIONAL).
- [ ] Fatal proxy failure (cannot be confirmed under [P1])
- [x] Level-of-analysis error: lab minutes → general property of the self / daily life (downstream).
- [x] Ecological-validity failure (downstream claims).
- [x] Omitted confound: motivation, affect, hunger, experimenter expectancy (PROVISIONAL).
- [ ] Citation laundering
- [ ] Premise laundering
- [ ] Ignored adjacent literature (cannot assess)
- [x] Missing decisive test (at the time): no resource marker.
- [ ] Intervention ratchet
- [ ] Institutional measurement gap
- [ ] Definition-operationalization mismatch (scope UNKNOWN)
- [ ] Operationalization pathologizes an accurate version
- [x] Construct-establishment gap: FORM and DOMAIN UNKNOWN, load-bearing.
- [ ] Motive claim unsupported

Verification flags:
- [x] Load-bearing evidence remains PROVISIONAL
- [x] Full source required (target full text)
- [ ] Reception check required (Stage 2c)

## 17. Final summary

- Claim under audit status: USEFUL-FOR-NARROWER (provisional)
- DEFEATS finding(s): none
- Surviving residual: lab persistence difference, mechanism unestablished
- Residual usefulness grade: G
- Strongest defensible claim: resisting chocolate preceded shorter persistence in one small experiment.
- Claim being overextended: a common limited resource for all volition.
- Definition-operationalization mismatch: scope UNKNOWN (ITEMS-INFERRED).
- Construct-establishment gap: FORM, DOMAIN; UNKNOWN; load-bearing; PROVISIONAL.
- Grade-before-assert outcome: not applicable (no belief graded).
- Main proxy problem: persistence time as capacity.
- Main level-of-analysis problem: lab minutes → daily-life willpower (downstream).
- Main omitted confound: motivation (R2) and task-specific affect/experimenter effects (R4).
- Decisive test: large preregistered study with a resource marker and effort/motivation checks (partly run: Vohs 2021, negative on outcome).
- Citation-use verdict: author lecture major inflation; APA moderate; RRR accurate.
- Load-bearing finding(s): none (all capped).
- Concede-test result: NARROWS.
- Failure location: PAPER (PR-MEDIA inflation separately).
- Overall verdict: USEFUL-FOR-NARROWER (provisional); grade G.
- Confidence level: Low (abstract-only target).
- What would change this assessment: the target's full text (Method, manipulation checks, mood measures, blinding), or a resource-marker test.

## Standardized finding table

| Field | CV-1 | CV-2 | CV-3 | CV-4 | CV-5 | CV-6 |
|---|---|---|---|---|---|---|
| Finding | Resource (FORM) unmeasured; effort without decrement externally | Unity across "unrelated acts" inferred | Persistence as capacity proxy | Hunger/affect/experimenter confounds | Lecture overextends ("Willpower is limited", "One Willpower") | Definition–operationalization scope UNKNOWN |
| Target claim | Field 6 (interpretation) | Field 6 (interpretation) | Field 6 | Field 6 | Downstream (D1) | Field 6 |
| What was measured | Persistence decrement | Four separate contrasts | Minutes to quitting | Condition difference | — | Persistence, anagrams, passivity |
| What was claimed | Limited common resource | Common resource across acts | Self-control capacity | Effect of exertion | Willpower limited, muscle-like, single | Capacity for active volition |
| Failure mode | Construct-establishment gap | Construct-establishment gap | Proxy problem | Omitted confound | Ecological-validity failure | Definition-operationalization mismatch |
| Failure-mode subtype | N/A | N/A | N/A | N/A | N/A | N/A |
| Severity | moderate | moderate | moderate | moderate | moderate | minor |
| Concede test | NARROWS | NARROWS | NARROWS | NARROWS | SURVIVES (as to field 6) | NARROWS |
| Scope loss if NARROWS | material: mechanism | material: generality | material: construct | material: cause | — | material |
| Construct property | form | domain | N/A | N/A | N/A | N/A |
| Construct-property status | UNKNOWN | UNKNOWN | N/A | N/A | N/A | N/A |
| ESTABLISHED-CITED prosecutor split | N/A | N/A | N/A | N/A | N/A | N/A |
| Operationalization retrieval basis | N/A | N/A | ITEMS-INFERRED | ITEMS-INFERRED | N/A | ITEMS-INFERRED |
| Operationalization scope result | N/A | N/A | UNKNOWN | UNKNOWN | N/A | UNKNOWN |
| P2 belief grade | N/A | N/A | N/A | N/A | N/A | N/A |
| P2 strength gate | N/A | N/A | N/A | N/A | N/A | N/A |
| Evidence | Abstract; S1; Vohs 2021 Table 3 | Abstract | Abstract; S2; Vohs 2021 Method | S4 p.548; Vohs 2021 Table 3 and abstract | S1 slides | Abstract |
| Evidence type | author inference | author inference | primary study | replication | commentary | primary study |
| Verification state | ABSTRACT-CONFIRMED (assertion); external FULL-TEXT-CONFIRMED | ABSTRACT-CONFIRMED | PROVISIONAL | PROVISIONAL (target); FULL-TEXT-CONFIRMED (external) | FULL-TEXT-CONFIRMED | PROVISIONAL |
| Possible innocent explanation | Introduction may establish FORM from prior work not retrieved | Four different tasks gave parallel results, a reasonable 1998 inference | Persistence is the field's accepted DV, retained by proponents in 2021 | Target may have measured mood and found no difference | Lecture simplification for lay audience | Body may define the construct operationally |
| What would weaken this | Full text showing FORM established or rivals tested | Evidence of a shared marker across tasks | Validation linking persistence to an independent capacity marker | Target manipulation checks showing equal affect and blinded timing | Field evidence of everyday depletion | Retrieved definition matching the DV |
| Failure location | PAPER | PAPER | PAPER | PAPER | PR-MEDIA | PAPER |
| Finding disposition | PROVISIONAL | PROVISIONAL | PROVISIONAL | PROVISIONAL | CONFIRMED | PROVISIONAL |
