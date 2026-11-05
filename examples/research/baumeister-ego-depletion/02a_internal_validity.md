# Stage 2a — Internal Validity & Replication Audit

INSTRUMENT PREFLIGHT: prompts/research-analysis/2-internal-validity.txt @ commit a58d165d9a986edca220f8143fc0c0d9316c8a13 | blob/hash ff54b2a6e88d25cfef37c4626aee256d2d2442e8 / sha256 55e8aa1635c33088f91178c275d2776cbb378a95abd0fd9196efec08fbdb5007 | 970 lines | 46009 bytes | markers PRESENT ("INTERNAL VALIDITY & REPLICATION AUDIT PROMPT") | IDENTITY CONFIRMED (operator-pinned commit + blob + sha256; retrieval at the immutable commit, HTTP 200; independently cross-checked by git rev-parse in a separate clone)

SIBLING-PROSECUTOR INPUT: NONE
INDEPENDENCE STATUS: INDEPENDENT

Effort: high (as briefed). The full pinned prompt was read before the first version was written (11:23Z).

REGENERATION NOTICE: the first version (11:23Z / 03:23 PST) was lost in the box restore at about 11:32Z (03:32 PST). This version was rewritten at 11:55Z (03:55 PST; worklog stage2a-regen) from the same instrument and the same sources. Some passages of the lost version survived in the session record: the header, the inputs list, the closing standardized table, and one set of locator corrections. Those passages were re-checked against the sources and reused where they verified. By then the runner had also seen Stage 2c corpus metadata and Semantic Scholar contexts; none is used as evidence below. Disclosed in 00 under Deviations.

## Inputs

1. **Foundational paper.** Baumeister, Bratslavsky, Muraven & Tice (1998), JPSP 74(5):1252–1265.
   - Full text NOT ACCESSED: no authorized copy exists (APA 403; Unpaywall/OpenAlex closed; author and repository pages are metadata-only).
   - Abstract read via PubMed 9599441 (not committed).
   - Design detail and magnitudes come from authorized secondary sources:
     - S1: the first author's LSE lecture slides 2012 (means);
     - S2: Schimmack 2016, a critic's reading (N, t, d, procedure);
     - S4: Hagger et al. 2016, describing the paradigm.
   - Every statement about the target's internals is therefore at most ABSTRACT-CONFIRMED or secondhand.
2. **Central finding.** Taken from the Stage 1 map (supplied: 01_claim_extraction.md).
3. **Downstream use.** Stage 1 Field 4: author lecture, APA lay page, citing literature.
4. **Known replication attempts.** Retrieved this run from authorized copies, each read in full:
   - Hagger, Chatzisarantis et al. 2016, RRR, PPS 11(4):546–573. Maastricht University repository (HTTP 200).
   - Vohs, Schmeichel et al. 2021, Psych Sci 32(10):1566–1581. eScholarship, CC BY (HTTP 200).
   - Dang et al. 2021, SPPS 12(1):14–24. PMC8186735 (HTTP 200).
   - Carter, Kofler, Forster & McCullough 2015, JEP:G 144(4):796–815. Author copy (HTTP 200).
   - Baumeister & Vohs 2016 comment on the RRR, PPS 11(4):574–575. APS-hosted manuscript (HTTP 200).
   - Schimmack 2016 replicability analysis (WebFetch 200).
5. **Pre-registration.** None. This is a 1998 laboratory study, before registration practice existed in the field. No registration is reported (the abstract and secondary sources mention none).
6. **Construct-validity output.** NONE.

## Claim-map confirmation

- **Claim under audit** (map field 6): In Experiment 1, radish/resist-chocolate participants persisted about 8.35 min on unsolvable puzzles vs 18.90 (chocolate) and 20.86 (no food); N ≈ 67; t(44) = 6.03 (d ≈ 1.8).
- **Literally measured** (map field 1): between-condition persistence time after an experimenter-delivered food-temptation manipulation, in one lab, with about 22 per cell. The three further experiments use different manipulations and outcomes.
- **Weaker defensible claim** (map field 3): one small lab demonstration plus three small same-direction contrasts. Consistent with, but not specific to, a shared resource.
- **Target layer:** source claim (L1), with L2 as the generalization that later tests address.

Load-bearing chain for Field 6:
- A single between-subjects contrast (radish vs chocolate/no-food) on one timed DV.
- Secondhand: means from S1, N and t from S2.
- L1's generality (L2) rests on the paradigm being replicable. Later tests probe it mostly with different manipulations (e-crossing, Stroop, writing) rather than the food task.

## Section A — Data generation audit

| Data source | Collection method | Selection bias risk | Missingness pattern | Incentive structure risk | AI-analysis check run |
|---|---|---|---|---|---|
| Exp 1 laboratory sessions (N = 67, about 22 per cell; S2) | Experimenter-run sessions: cookies baked in the room, food tasting, then unsolvable figure-tracing. Time to bell is the DV (S2) | Moderate: undergraduate convenience sample; single lab | Cannot assess (exclusions not retrieved; t(44) for a 2-group contrast implies about 46 in the two cells compared) | Moderate: non-blind experimenter delivering the manipulation and timing the DV (R4; S2 description; blinding not reported in any source read) | N/A |
| Exp 2–4 sessions | Laboratory; different manipulations and outcomes (abstract) | Moderate | Cannot assess (body not read) | Moderate | N/A |

Determination basis: secondary report (S2, S4) and the abstract. Body not read: PROVISIONAL.

## Section B — Pre-registration and analysis plan

| Pre-registration status | Analysis match | Outcomes tested | Outcomes reported | Post-hoc subgroups | P-hacking risk |
|---|---|---|---|---|---|
| None (era-typical) | Cannot assess | Exp 1: persistence time (also number of attempts, per S2's procedure description; PROVISIONAL) | Persistence time contrasts | Cannot assess | Moderate (cannot assess within-paper; field-level bias evidence in Section E) |

## Section C — Effect size and statistical power

| Reported effect size | Field typical range | Corrected meta-analysis estimate | Sample size | Estimated power | Winner's curse risk |
|---|---|---|---|---|---|
| Radish vs chocolate d = 1.80; radish vs no-food d = 2.04 (S2, from t(44) = 6.03 and 6.88) | Social-psychology between-subjects effects are typically d ≈ 0.2–0.5 (field context; PROVISIONAL). Uncorrected depletion meta-analysis d ≈ 0.62 (Hagger 2010, as reported by S2 and the RRR p.547) | Carter et al. 2015 Table 7: impossible-puzzles data set PET −0.16 (−0.76, 0.43), PEESE 0.22 (−0.16, 0.60); combined PET −0.27, PEESE 0.003 | about 22 per cell | Normal approximation, n = 22 per cell, α = .05 two-tailed: power ≈ .10 at d = 0.2, ≈ .38 at d = 0.5, ≈ .76 at d = 0.8 | High |

Derivation mode: COMPUTED-FROM-RETRIEVED. d = t·√(1/n₁ + 1/n₂) with n = 23 per compared cell gives 1.78 and 2.03, matching S2. Power is computed with the normal approximation and is slightly optimistic. A d of 1.8 is about 3× the uncorrected literature average and an order of magnitude above later large-sample estimates. With power near .1 for realistic effects, a significant small-sample result implies a large inflation (winner's curse).

## Section D — HARKing

| Hypothesis type | Pre-registered? | HARKing indicators | HARKing risk |
|---|---|---|---|
| Directional (self-control → reduced subsequent persistence), framed by a strength/energy model | No | Cannot assess within-paper (introduction not read). The construct-unity conclusion is drawn post hoc across four different paradigms (abstract) | Low–moderate (PROVISIONAL) |

## Section D2 — Forking paths

| Decision point | Choice made | Pre-specified? | Defensible alternatives | Result under alternatives | Fragility |
|---|---|---|---|---|---|
| Outcome operationalization (Exp 1) | Time to quit | No | Number of attempts (also recorded per S2's procedure description) | Untested in sources read | Untested |
| Comparison | Radish vs each control in separate t-tests | No | Omnibus 3-group test | Untested (both contrasts large) | Untested |
| Which experiments reported | Four same-direction experiments | No | Inclusion of unreported studies (Section E) | Cannot assess | Untested |

Integration: fragility cannot be assessed without the body. The untested forking points combine with low power and the bias evidence (Section E) into one inference: the published estimate is likely inflated (IV-1, IV-6, IV-7).

## Section E — Selective reporting

| Outcomes registered | Outcomes reported | Missing outcomes | Subgroup selectivity | Publication bias indicators |
|---|---|---|---|---|
| None | Persistence time (Exp 1); four same-direction experiments | Cannot assess within-paper | Cannot assess | S2: 128 of 165 ego-depletion articles (78%; 429 studies) showed evidence of bias or low replicability. S2 quotes the first author's 2016 essay: "I suspect the published report may leave out a few other studies that failed" (general practice; not specific to 1998). Carter 2015: small-study effects in the combined set (Table 7) |

## Section F — Replication status

| Direct replications | Success rate | Pre-registered reps | Independent reps | Meta-analytic estimate | Effect shrinkage | Verification state |
|---|---|---|---|---|---|---|
| No direct replication of the food-temptation → figure-tracing protocol found among the sources read. Conceptual multi-site replications of L2 read in full: RRR 2016 (23 labs, N = 2,141); Vohs 2021 (36 labs, N = 3,531; proponent-led protocols, includes a figure-tracing outcome); Dang 2021 (12 labs, N = 1,775) | 0/3 reproduce an effect near the target's magnitude: RRR d = 0.04 [−0.07, 0.15]; Vohs 2021 d = 0.06 [−0.02, 0.14] overall, figure-tracing duration d = 0.15 [0.02, 0.29] (n = 1,216); Dang 2021 d = 0.10 [0.01, 0.19] | 3 | RRR and Dang independent of the original lab; Vohs 2021 led by proponents with an independent advisory board and blinded analysis | Carter 2015 bias-corrected: PET/PEESE ≈ 0 (combined PEESE 0.003; impossible puzzles PEESE 0.22, CI includes 0) | From d ≈ 1.8 to ≈ 0.0–0.15 | FULL-TEXT-CONFIRMED and RECEPTION-CONFIRMED (all read in authorized copies) |

- Locators:
  - RRR abstract; p.554; Table (full-sample row d = 0.04).
  - Vohs 2021 abstract; Table 4 (figure-tracing rows); p.1568 (design governance).
  - Dang 2021 abstract; Results.
  - Carter 2015 Table 7.
- Current best estimate for L2 (sequential-task effect): d ≈ 0.0–0.1, at most small.
- The original food-temptation protocol itself has not been tested in a registered multi-site study among the sources read. The RRR explains it rejected the radish task as requiring "extensive experimenter involvement" (p.548).

## Section G — Data and code availability

| Data available | Code available | Reanalysis attempted | Reanalysis result | PubPeer flags | Corrections issued | Verification state |
|---|---|---|---|---|---|---|
| No public data for the 1998 experiments (replication/NOT_ASSESSABLE.txt) | No | This audit: NOT ASSESSABLE (no data; reconstruction from tables prohibited) | — | Not checked (PubPeer not queried this run) | None (Crossref, Stage 1) | Data absence: searched (OSF, Dataverse, OpenAlex datasets, web) |

## Section H — Summary table

| Dimension | Assessment | Severity | Notes |
|---|---|---|---|
| Data generation quality | Small single-lab sessions with experimenter-delivered manipulation | Moderate | IV-1, R4 |
| Selection bias | Convenience sample | Minor | |
| Missingness handling | Cannot assess | Cannot assess | Body not read |
| Incentive structure risk | Non-blind experimenter timing the DV | Moderate | PROVISIONAL |
| Pre-registration | None | Minor | Era-typical |
| Analysis plan compliance | Cannot assess | Cannot assess | |
| P-hacking risk | Moderate (field-level evidence) | Moderate | IV-7 |
| Effect size plausibility | d ≈ 1.8–2.0 implausible | Major | IV-1 |
| Statistical power | ≈ .10 for d = 0.2 | Major | IV-6 |
| Winner's curse risk | High | Major | IV-6 |
| HARKing risk | Low–moderate | Minor | |
| Forking-paths fragility | Untested | Cannot assess | |
| Selective reporting | Field-level bias indicators | Moderate | IV-7 |
| Replication success rate | 0/3 large multi-site tests near the original magnitude | Fatal (for the strong claim) | IV-2–IV-4 |
| Effect size trajectory | ≈1.8 → ≈0–0.15 | Fatal (for the strong claim) | IV-2, IV-5 |
| Data/code availability | None | Cannot assess | NOT_ASSESSABLE |
| Post-publication flags | Authors contest the RRR's manipulation | Minor | IV-8 |

## Section H2 — Concede test

| Finding | Verification state | Technical outcome status | Conditional concede result | Verdict eligibility | Eligibility basis | Surviving claim if NARROWS |
|---|---|---|---|---|---|---|
| IV-1 Exp 1 reports d ≈ 1.8–2.0 with about 22 per cell (S1 means; S2 N/t/d) | PROVISIONAL (secondhand) | UNVERIFIED (target body not read) | NARROWS | PENDING VERIFICATION | Needs the target's Results section | A real but much smaller effect cannot be excluded by this finding alone |
| IV-2 Proponent-led 36-lab preregistered test with blinded analysis (Vohs 2021, N = 3,531) finds d = 0.06 [−0.02, 0.14]. The figure-tracing persistence outcome closest to Exp 1 gives d = 0.15 [0.02, 0.29] | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | INDEPENDENT-REANALYSIS-CONFIRMED (independent data, method and result stated; abstract, Table 4) | DEFEATS (for d ≈ 1.8 and for a reliable moderate L2 effect) | ELIGIBLE | Large preregistered test by the theory's proponents; persistence outcome included | — |
| IV-3 RRR (23 labs, N = 2,141) finds d = 0.04 [−0.07, 0.15] | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | INDEPENDENT-REANALYSIS-CONFIRMED | NARROWS (different paradigm: e-crossing → MSIT; contested manipulation, IV-8) | ELIGIBLE | RRR abstract; p.554 | L2 not shown with a computerized e-task paradigm |
| IV-4 Dang 2021 (12 labs, N = 1,775) finds d = 0.10 [0.01, 0.19] (Stroop → antisaccade) | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | INDEPENDENT-REANALYSIS-CONFIRMED | NARROWS | ELIGIBLE | Abstract; Results | A small effect (d ≈ 0.1) may exist in one paradigm |
| IV-5 Bias-corrected meta-analysis (Carter 2015, 116 experiments) finds PET/PEESE estimates near zero; impossible-puzzles PEESE 0.22 with CI including 0 | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | INDEPENDENT-REANALYSIS-CONFIRMED | NARROWS | ELIGIBLE | Table 7 | Literature-level evidence does not support a nonzero effect after correction |
| IV-6 Power ≈ .10 at d = 0.2 with 22 per cell; significance at this n implies large inflation | PROVISIONAL (computed from secondhand N) | COMPUTED | NARROWS | PENDING VERIFICATION | Section C computation | — |
| IV-7 Field-level selective-reporting evidence (S2: 78% of 165 articles show bias; first author's 2016 essay acknowledges unreported failed studies as general practice) | PROVISIONAL (not specific to the 1998 paper) | UNVERIFIED for this paper | NARROWS | PENDING VERIFICATION | Paper-specific file drawer unknown | — |
| IV-8 Authors argue the RRR manipulation failed and "did not test ego depletion" (B&V 2016) | FULL-TEXT-CONFIRMED | AUTHOR-RESPONSE | SURVIVES (as to IV-2: Vohs 2021 used the authors' preferred paradigms) | ELIGIBLE | B&V 2016 manuscript | — |

| Finding | Scope-loss level | Original claim | Surviving claim | What practical or inferential work is lost? |
|---|---|---|---|---|
| IV-3 | Material | General sequential-task effect | Not shown in RRR paradigm | Generality across paradigms |
| IV-4 | Material | Moderate-to-large effect | d ≈ 0.1 in one paradigm | Practical magnitude |
| IV-5 | Material | Robust literature | Near-zero after bias correction | Literature as evidence |

## Section I — Verdict

- Claim under audit: INVALID
- Eligible DEFEATS finding(s): IV-2 (INDEPENDENT-REANALYSIS-CONFIRMED)
- Eligible MATERIAL NARROWING finding(s): IV-3, IV-4, IV-5
- Findings pending verification:
  - IV-1 | NARROWS | target body not read | authorized full text of the target
  - IV-6 | NARROWS | N secondhand | target Method/Results
  - IV-7 | NARROWS | paper-specific file drawer unknown | authors' study log
- Pending-evidence effect on assessability: NONE (the verdict rests on IV-2)
- Surviving residual: no effect near d ≈ 1.8. A narrow residual survives for L2: a small sequential-task effect (d ≈ 0.10–0.15) appears in some paradigms (Dang 2021; Vohs 2021 figure-tracing duration). That residual does not carry the claim of a large, general resource effect.
- Internal-validity grade: E

Answers:
1. Is the foundational finding likely real at the reported magnitude? No (IV-2, IV-5).
2. Even if a small effect is real, is it sufficient for the downstream claims ("Willpower is limited", "One Willpower")? No.
3. Best current estimate: d ≈ 0.0–0.15 for sequential-task effects.
4. What would upgrade the grade: a registered multi-site test of the original food-temptation protocol showing a large effect.
5. Decisive test not run: a direct registered replication of Exp 1's food-temptation protocol.
6. AI-assisted analysis: N/A.
7. Fragile to analytical choices: cannot assess.
8. Usable residual: "surviving residual: none" at the claimed magnitude; small L2 residual as stated.

## Section J — Integration with construct validity

SIBLING-PROSECUTOR INPUT: NONE
INDEPENDENCE STATUS: INDEPENDENT

No construct-validity output was formally supplied to this run. The following reasons only from general construct concerns and does not adopt any specific sibling finding or verdict visible elsewhere in session context.

The foundational finding is not likely real at the magnitude reported, on the eligible internal-validity evidence. Even if the construct interpretation is accepted, the large effect does not survive large preregistered tests. Any specific construct-validity compounding claim remains outside this independent run.

## Section K — Summary

- **Verdict.** The Experiment 1 finding (d ≈ 1.8; about 8 vs 19–21 min) is INVALID on internal-validity grounds (grade E).
- **Why.** Three large preregistered multi-site tests read in this run give d = 0.04 (RRR), 0.06 (Vohs 2021; proponent-led; figure-tracing 0.15) and 0.10 (Dang 2021). Bias-corrected meta-analysis gives ≈ 0.
- **Paper-alone threats.** About 22 per cell; power ≈ .1 for realistic effects; a non-blind experimenter delivers the manipulation and times the DV; field-level selective-reporting evidence.
- **Concede test.** Eligible DEFEATS: IV-2.
- **Surviving residual.** A small (d ≈ 0.1) sequential-task effect in some paradigms. It does not support the strong resource claim.
- **Replication.** NOT ASSESSABLE: no data.
- **Decisive test not run.** A registered multi-site replication of the original food-temptation protocol.

## Standardized finding table

| Field | IV-1 | IV-2 | IV-3 | IV-4 | IV-5 | IV-6 | IV-7 | IV-8 |
|---|---|---|---|---|---|---|---|---|
| Finding | Implausibly large d (≈1.8–2.0) with ~22 per cell | Proponent-led 36-lab test finds d = 0.06 | RRR finds d = 0.04 | Dang 2021 finds d = 0.10 | Bias-corrected meta-analysis ≈ 0 | Power ≈ .10 at d = 0.2 | Field-level selective reporting | Authors contest RRR manipulation |
| Target claim | Field 6 | Field 6 (via L1/L2) | Field 6 (via L2) | Field 6 (via L2) | Field 6 (via L2) | Field 6 | Field 6 | Field 6 |
| What was measured | Persistence time, 3 cells | Persistence/figure-tracing after e-task or writing | MSIT RTV after e-task | Antisaccade errors after Stroop | Random-effects + PET/PEESE by outcome type | Computation | Article-level bias tests | Commentary |
| What was claimed | d ≈ 1.8 | Depletion effect | Depletion effect | Depletion effect | Literature effect | Reliable effect | Complete reporting | RRR not a valid test |
| Failure mode | effect size implausibility | failed replication / effect shrinkage | failed replication | effect shrinkage | publication bias | low power / winner's curse | selective reporting | replication dispute |
| Severity | moderate (pending) | fatal-for-strong-claim | moderate | moderate | moderate | minor (pending) | minor (pending) | minor |
| Concede test | NARROWS | DEFEATS | NARROWS | NARROWS | NARROWS | NARROWS | NARROWS | SURVIVES (as to IV-2) |
| Scope loss if NARROWS | material | — | material | material | material | material | material | — |
| Evidence | S1 slide; S2 | Vohs 2021 Table 4; abstract | RRR abstract; p.554 | Dang 2021 Results | Carter 2015 Table 7 | computed | S2 | B&V 2016 MS |
| Evidence type | secondary report | replication | replication | replication | meta-analysis | computation | critique | author response |
| Verification state | PROVISIONAL | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | PROVISIONAL | PROVISIONAL | FULL-TEXT-CONFIRMED |
| Possible innocent explanation | Genuinely strong manipulation (live food temptation) | Manipulation differs (e-crossing vs food); figure-tracing still significant at d = 0.15 | Paradigm may not induce depletion (B&V 2016) | Paradigm-specific | Bias correction can overcorrect under heterogeneity | Large true effect would be detected | Statements not about 1998 | Valid critique of RRR |
| What would weaken this | Full text showing smaller d | Large direct food-temptation replication with large effect | Valid RRR-type test with large effect | — | Unbiased large-sample evidence of d ≈ 0.6 | Larger N in target | Evidence of complete reporting | — |
| Failure location | PAPER | PAPER | PAPER | PAPER | PAPER | PAPER | PAPER | PAPER |
| Status | provisional | confirmed | confirmed | confirmed | confirmed | provisional | provisional | contested |
