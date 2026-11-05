# 05 — Final assessment: Baumeister, Bratslavsky, Muraven & Tice (1998), "Ego depletion: Is the active self a limited resource?"

Status: exploratory, single-agent, model-produced.
- The same executor ran every stage, including the pre-registration and the counter-audit.
- No finding below is established until a human reviewer has checked it.
- No composite score is given.

Target: Roy F. Baumeister, Ellen Bratslavsky, Mark Muraven & Dianne M. Tice (1998), JPSP 74(5):1252–1265, DOI 10.1037/0022-3514.74.5.1252 (OpenAlex W2123817056).
- RESTRICTED-ACCESS RUN: the target was read at ABSTRACT level only (PubMed 9599441).
- The publisher returned HTTP 403, OpenAlex lists it as closed, and the author and repository pages are metadata only. Unauthorized copies were found by search and excluded under the rights rule.
- Body-level facts are secondhand: the first author's 2012 LSE slides, Schimmack 2016, the 2016 RRR p.548, and the Carter et al. 2015 Table 1 coding.

Run date: 2026-11-05 (America/Los_Angeles; box clock UTC, PST = UTC−8). Effort: high for 2a/2b/2c; maximum for 3 and 05.

## Chain completeness

| Stage | File | Status |
|---|---|---|
| Pre-registration | 00a_preregistration_LOCKED.txt | LOCKED before Stage 1 (11:11Z); sha256 a76bf588154ce8d7214ee6de4b8d66ae0f5aece8197e0813235961e037cc3d28, re-verified before unblinding |
| 1 Claim extraction | 01_claim_extraction.md | COMPLETE (restricted access; map confidence low). Regenerated after the box-restore file loss (see 00, Deviations) |
| Replication | replication/NOT_ASSESSABLE.txt | NOT ASSESSABLE: no public data for the 1998 experiments; no reconstruction from reported statistics |
| 2a Internal validity | 02a_internal_validity.md | COMPLETE (INDEPENDENT; no sibling input). Regenerated after the file loss |
| 2b Construct validity | 02b_construct_validity.md | COMPLETE (independent of 02a). Regenerated after the file loss |
| 2c Citation network (candidate rev. 3) | citation-network-v2cand3/02c_citation_network_v2cand3.md | COMPLETE. v1 checker STRUCTURAL PASS / CONTENT PASS-WITH-REVIEW items=2; gate checker PASS-WITH-REVIEW items=13. RISK BAND >20%–40%, PROVISIONAL (coverage exactly 70%; 20% if review items are withdrawn) |
| 3 Counter-audit | 03_counter_audit.md | COMPLETE. Internal validity SUPPLIED AND CONSUMED; 02b and 02c supplied; Input 5 not supplied (FIDELITY CHECK N/A) |

## Field 6 (claim under audit)

Restated (not a quotation; secondhand numbers): in Experiment 1, participants who ate radishes while resisting chocolate persisted about 8.35 min on unsolvable figure-tracing puzzles, vs 18.90 (chocolate) and 20.86 (no food); N ≈ 67; t(44) = 6.03, d ≈ 1.8 radish vs chocolate.
- Carter et al. 2015 independently code the same experiment as g = 1.31 (n 25 vs 44 pooled controls).
- The N discrepancy (67 vs 69) is unresolved without the body.

## Unblinding the pre-registration

00a was written at 11:11Z (03:11 PST; the file's own label "11:11 PST" is wrong, see Deviations) before Stage 1. It was not edited.

| Expectation (00a) | Observed | Tell | Fired? |
|---|---|---|---|
| E1: field 6 = Exp 1 persistence, about 8 vs 19–21 min, roughly 20–25 per cell (total 65–70) | Field 6 = 8.35 vs 18.90 vs 20.86 min, N ≈ 67 (S1/S2); Carter codes 25 vs 44 | T1 | No |
| E2: 2a finds the central effect DEFEATED by external evidence (grade E or D, INVALID or near it); paper-alone threats serious but not fatal | 2a: INVALID, grade E. DEFEATS = IV-2 (Vohs 2021); paper-alone threats IV-1, IV-6, IV-7 PROVISIONAL (NARROWS) | T2 | No. Stage 3 then re-aimed IV-2 to NARROWS for field 6 itself (paradigm mismatch), so the end-of-chain disposition is weaker than E2 |
| E3: dominant construct concern = the unmeasured resource (FORM / proxy); secondary: persistence confounded with motivation, frustration, mood, fatigue; manipulations may not share one construct | 2b: CV-1 FORM (resource unmeasured), CV-2 DOMAIN (unity), CV-3 persistence proxy, CV-4 hunger/affect/experimenter confounds | T3 | No |
| E4: no posted data; NOT_ASSESSABLE most likely; later replication data do not reproduce field 6 | NOT_ASSESSABLE; later OSF data noted and not used | T4 | No |
| E5 dimensions: density 1/UNASSESSED; founding 1/0; recent 1/UNASSESSED; hub 1/UNASSESSED; proxy UNASSESSED/1; mutation 1; adjacent 0/1; decisive 0; uptake 1; ratchet N/A/UNASSESSED; non-updating 1/0. Band moderate (20–40%) or WITHHELD | Density SCORED 0; founding SCORED 2; recent SCORED 2; hub UNASSESSED; proxy SCORED 1; mutation UNASSESSED; adjacent SCORED 1; **decisive SCORED 1**; uptake SCORED 1; ratchet N/A; non-updating UNASSESSED. Band >20%–40% PROVISIONAL (8/21 = 38.1%) | T5 (any of: density, founding and uptake all 0; **decisive SCORED 1+**; healthy band) | **Yes (one clause).** Lack of decisive tests SCORED 1, not 0: L2 was tested decisively, but 0/59 locked-search works test the field-6 paradigm (I18). Band matched. Dimension-level matches 5/11 (hub, proxy, adjacent, uptake, ratchet); misses are density (0 vs 1/UNASSESSED), founding and recent (2, above the expected range), mutation and non-updating (UNASSESSED, not scored) |
| E6: most 2a/2b findings survive; authors' RRR objections narrow "defeated by replication" to "contested, with the weight of large tests against"; at least one finding downgraded as hindsight-driven | E0: 0 DEFEATED, 3 NARROWED, 2 RECHARACTERIZED, 16 UNAFFECTED (21 rows). "Defeated" was narrowed, but by the paradigm mismatch (the large tests did not re-run the food protocol). The authors' RRR objection was judged largely answered by Vohs 2021. Hindsight: only a partial instance (IV-6's relevance rests on a post-2015 effect estimate); no severity changed for hindsight | T6 (Stage 3 overturns a majority, or finds no hindsight-driven finding) | **Partly.** Outcome matched (narrowing; most findings survive). The predicted mechanism (authors' objections) did not carry it. The hindsight downgrade was not found in a form that changed severity. Caveat: 00a was opened during Stage 3 preparation (disclosed in 03 J2), so the narrowing may be influenced by the expectation |

Given the declared exposure (00a: "Independence from prior knowledge is NOT established"), matches are not evidence that the instruments are valid. The informative results are the departures: T5 (decisive tests), the founding and recent dimensions scoring above expectation, and the Stage 3 mechanism.

## Findings by stage, with counter-audit disposition

| Stage | Finding | Stage result | Counter-audit (E0 / G2) | Net |
|---|---|---|---|---|
| 1 | 5A within-source inflation: behaviour → mechanism; hedge drift "may" → "suggest … share"; unity | PAPER, ABSTRACT-CONFIRMED | consistent; CV-1 and CV-2 recharacterized (hedged inference) | upheld at abstract level |
| 1 | 5B author lecture (D1/D1b) and APA page (D2) | PR/MEDIA, RETRIEVED | G2: "the failure is at the PR layer" (CV-5) | upheld (downstream) |
| 1 | 5B "Citing-literature layer: no inflation found in D3" | — | **MAP DISAGREEMENT**: 2c F3 and F4 show citation-layer inflation | map corrected by 2c (not edited) |
| 2a | IV-1 d ≈ 1.8–2.0 with ~22 per cell | NARROWS, PROVISIONAL | UNAFFECTED by E0 (science-fair note does not answer); restated with Carter's g = 1.31 | upheld, restated (PROVISIONAL) |
| 2a | IV-2 Vohs 2021 d = 0.06 (figure tracing 0.15) | DEFEATS | UNAFFECTED by E0; **G2 re-aimed**: fatal for the L2 inference, major NARROWS for field 6 itself | upheld for L2; narrowed for field 6 |
| 2a | IV-3 RRR d = 0.04 | NARROWS | UNAFFECTED; reception-checked (top threat #2) | upheld (one lever with IV-2) |
| 2a | IV-4 Dang 2021 d = 0.10 | NARROWS | UNAFFECTED; reception not checked (capped) | upheld (one lever) |
| 2a | IV-5 bias-corrected meta-analysis ≈ 0 | NARROWS | UNAFFECTED; reception CONTESTED (comment LOCATED) | upheld at moderate (one lever) |
| 2a | IV-6 power ≈ .10 at d = 0.2 | NARROWS, PROVISIONAL | UNAFFECTED; premise partly hindsight-dependent; nested with IV-1 | upheld (minor, provisional) |
| 2a | IV-7 field-level selective reporting | NARROWS, PROVISIONAL | UNAFFECTED; not paper-specific | upheld (minor, provisional) |
| 2a | IV-8 authors contest the RRR | SURVIVES (as to IV-2) | not a threat; largely answered by Vohs 2021 | narrows IV-3 only |
| 2b | CV-1 FORM: resource unmeasured | NARROWS (provisional) | **RECHARACTERIZED**: hedged inference, not tested against rivals | upheld, recharacterized |
| 2b | CV-2 DOMAIN: unity inferred | NARROWS (provisional) | **RECHARACTERIZED**: tested by convergence without a crossed design; aimed at field 2, not field 6 | upheld for field 2 |
| 2b | CV-3 persistence as capacity proxy | NARROWS (provisional) | **NARROWED**: all outcomes behavioural (Exp 3/4 not persistence) | upheld, narrowed |
| 2b | CV-4 hunger/affect/experimenter confounds | NARROWS (provisional) | **NARROWED**: mood reportedly checked (secondhand); chocolate control; non-blind experimenter remains | upheld, narrowed |
| 2b | CV-5 lecture overextension | SURVIVES (PR layer) | UNAFFECTED; PR/MEDIA layer | upheld (downstream) |
| 2b | CV-6 definition–operationalization UNKNOWN | NARROWS (provisional) | UNAFFECTED; nested with CV-3 | unresolved |
| 2c | F1 paradigm untested at scale; general effect near zero to small | NARROWS (major) | UNAFFECTED; consistent with IV-2 re-aimed | upheld |
| 2c | F2 founding-cluster-centred reception | SURVIVES | UNAFFECTED; CITATION layer | upheld |
| 2c | F3 recent premise use | SURVIVES (MAP GAP) | UNAFFECTED; "the source is defensible on this point; the failure is at the citation layer" | upheld (citation layer) |
| 2c | F4 resource stated as shown | SURVIVES (MAP GAP) | UNAFFECTED; citation layer (abstract hedges support the finding) | upheld (citation layer) |
| 2c | F5 mixed critique uptake | SURVIVES | UNAFFECTED; F: engaged, no suppression | upheld |
| 2c | F6 no helplessness/expectancy works in the reference list | SURVIVES (MAP GAP) | **NARROWED**: stress-aftereffect, perceived-control, persistence and mood works are cited; helplessness is constant across cells | upheld, narrowed (minor) |
| 2c | F7 retrieval and record limits | SURVIVES (MAP GAP) | process limit | upheld (retrieval layer) |

## What the stages support

- **Field 6's magnitude is not credible as a reproducible effect.**
  - Three preregistered multi-lab tests of the general sequential-task effect found d = 0.04 (RRR), 0.10 (Dang 2021, VERSION-SUBSTITUTE) and 0.06 (Vohs 2021, proponent-designed). The RRR and Vohs 2021 are reception-checked.
  - Vohs's persistence outcome was d = 0.15 [0.02, 0.29].
  - The target's Exp 1 is among the largest effects in its outcome family in Carter's coding: g = 1.31 vs a random-effects mean of 0.79 and a PEESE of 0.22 with a CI including 0 (contested method).
- **Field 6 itself is narrowed, not refuted.** No large test re-ran the food-temptation protocol. The RRR declined it for experimenter involvement, and the locked search found 0/59 L1 tests (recall 8/12). What survives is a one-lab, non-blind, small-sample result, implying a small effect if any.
- **Field 2 (mechanism and unity) remains inference.** The resource was never measured. The abstract hedges ("may", "suggest"), and the hedges are dropped in the author's lecture and the APA page (PR/MEDIA) and in citing passages (CITATION).
- **Citation network:** founding-cluster-centred, with recent premise use. Critiques were engaged (2016 dispute; 2021 concession co-signed by a founding author), so there is no suppression. Band >20%–40% PROVISIONAL, with coverage exactly at the 70% gate.
- **Charge against the 1998 paper:** a large effect from small single-lab cells, a mechanism inferred from behaviour, and no blinding control as described. These are paper-layer weaknesses; their defeat as a general effect came from later data.

## Needs human adjudication

1. **02a vs Stage 3 on IV-2.** 2a scores IV-2 DEFEATS (verdict INVALID). Stage 3 re-aims it to major NARROWS for field 6 because the tests used other manipulations. The single assumption most likely to be wrong (03 J2) is whether the paper's own unity claim makes those tests count as tests of field 6.
2. **Field 6's numbers.** S2 gives N ≈ 67, t(44) = 6.03, d ≈ 1.8; Carter gives g = 1.31 with n 25/44. This needs the target's body (authorized access; e.g. an institutional APA PsycNET session).
3. **CV-4 narrowing.** It rests on two secondhand citing passages (one from the founding cluster's own review) saying mood was checked.
4. **The 15 checker review items** (13 gate, 2 v1), listed verbatim in RUN_REPORT.txt. Note especially:
   - the 70% coverage gate is met only if review items resolve;
   - the POSSIBLE_DUPLICATE_WORK flag on N09/A48/A50 (distinct works; instrument problem);
   - CODED_FROM_METADATA (87 rows).
5. **Unread reception sources:** the Inzlicht, Gervais & Berkman comment on Carter 2015; reception of Dang 2021; the 2024 review (I24).
6. **The E6 / 00a exposure.** 00a was opened during Stage 3 preparation. Whether the Stage 3 narrowing was influenced by the pre-registered expectation needs checking.
7. **The box-restore regeneration of 01/02a/02b** (11:53–11:57Z), after 2c's corpora were retrieved (see 00 Deviations).
8. **The INSTRUMENT PROBLEMS** listed in RUN_REPORT.txt.

An audit of a famous replication-crisis case run by an executor with declared prior exposure mainly tests the chain, not the paper. Results that match the pre-registration should be read as such.
