# Stage 3 — Oppositional Citation & Neglected Evidence Counter-Audit

INSTRUMENT PREFLIGHT: prompts/research-analysis/3-counter-audit.txt @ commit a58d165d9a986edca220f8143fc0c0d9316c8a13 | blob/hash 74357f08562a47fa8fdbbde4325657ad3c9cd871 / sha256 291f2339992eeaca83c60281263975d3b5643d64ec6e5d118fa39c44b6c9ede9 | 915 lines | 42287 bytes | markers PRESENT ("OPPOSITIONAL CITATION & NEGLECTED EVIDENCE COUNTER-AUDIT PROMPT (v3)") | IDENTITY CONFIRMED (operator-pinned commit + blob + sha256; retrieval form IMMUTABLE REMOTE at the pinned commit, HTTP 200; independently cross-checked by `git rev-parse` in a separate clone; local sha256 re-computed 12:26Z before writing)

Effort: maximum (as briefed). The full pinned prompt (915 lines) was read before writing.
Run date 2026-11-05 (UTC); operator TZ America/Los_Angeles (PST = UTC−8). Stage 3 started 12:26Z (04:26 PST).

## Inputs

0. Claim map: SUPPLIED — `01_claim_extraction.md` (field 6 below; layers L1–L4, rivals R1–R4). Map confidence: low (target body not read).
1. Foundational paper: Baumeister, Bratslavsky, Muraven & Tice (1998), JPSP 74(5):1252–1265.
   - ABSTRACT ONLY (PubMed 9599441). No authorized full text exists (publisher HTTP 403; OA status closed; author and repository pages metadata-only). Unauthorized copies were excluded under the rights rule.
   - Body-level facts come from authorized secondary readings: S1 (first author's LSE slides 2012), S2 (Schimmack 2016), S4 (Hagger et al. 2016 p.548), and, new in this stage, the coding of the target's Experiments 1 and 3 in Carter et al. (2015) Table 1 (author copy).
   - The target's reference list is available at METADATA level (OpenAlex, 57/58 resolved; 2c raw/target_reflist_titles.json).
2. Citation-network output: SUPPLIED — `citation-network-v2cand3/02c_citation_network_v2cand3.md` (v2-candidate.3, map cn7-map-3). RISK BAND >20%–40%, PROVISIONAL at the 70% gate. Findings 1–7.
3. Construct-validity output: SUPPLIED — `02b_construct_validity.md` (CV-1…CV-6; USEFUL-FOR-NARROWER, provisional; grade G).
4. Internal-validity output: SUPPLIED — `02a_internal_validity.md` (IV-1…IV-8; INVALID, grade E; DEFEATS: IV-2). It is consumed in E0 and G2 on the same terms as the other prosecutors [FAIL-CA-003].
5. Thesis paragraph / draft: NOT SUPPLIED. The FIDELITY CHECK does not run.
6. Central claim being audited (map field 6): "In Experiment 1, participants who ate radishes while resisting chocolate persisted about 8.35 min on unsolvable puzzles vs 18.90 (chocolate) and 20.86 (no food); N ≈ 67; t(44) = 6.03 (d ≈ 1.8) radish vs chocolate." PROVISIONAL (secondhand numbers).
7. Current audit verdict (the thesis being counter-audited):
   - 2a INVALID, grade E (DEFEATS: IV-2, Vohs et al. 2021). Material narrowing: IV-3, IV-4, IV-5.
   - 2b USEFUL-FOR-NARROWER (provisional), grade G. No DEFEATS (all target-dependent findings capped under [P1]).
   - 2c Finding 1 NARROWS field 6 (scope loss major). Findings 2–7 SURVIVE; 3, 4, 6, 7 are MAP GAP. Band >20%–40% PROVISIONAL.
8. Known hub / founding cluster:
   - The four target authors: 10/50 RECEPTION-1 works, receiving 62/113 internal edges (2c I03).
   - Main hubs: N19 Muraven, Tice & Baumeister 1998 (in-degree 22) and N06 Muraven & Baumeister 2000 (15); N16 Hagger et al. 2010 meta-analysis; N41 Gailliot et al. 2007 (glucose).
9. Adjacent fields already suspected (2b §10; 2c Section E): motivation / mental fatigue (R2); learned helplessness (unsolvable outcome task); experimenter expectancy (non-blind delivery and timing); mood and persistence; lay theories of willpower (R3).

Evidence-base note:
- Load-bearing sources read in full this run (authorized copies; not committed): Hagger et al. 2016 RRR (Maastricht repository); Vohs et al. 2021 (eScholarship, CC BY); Dang et al. 2021 (PMC8186735 author manuscript; VERSION-SUBSTITUTE); Carter et al. 2015 (author copy); Baumeister & Vohs 2016 comment (APS-hosted manuscript); Englert & Bertrams 2021 (Frontiers, publisher OA); Schimmack 2016 (blog).
- Stage 3 re-read these files on the box for the passages cited below; no new web retrieval was made in this stage.
- Items known only from reference lists or OpenAlex titles are labelled LOCATED. Nothing load-bearing comes from model memory.

How-found labels used below (DATA-HONESTY RULE):
- cites foundational paper directly — verified by an OpenAlex RECEPTION-1 / ADJUDICATION-1 edge (2c) or in the full text read;
- cited by foundational paper — verified in the OpenAlex reference list of the target (METADATA);
- found through keyword search — 2c ADJUDICATION-1 or Section E locked queries;
- unresolved source lead — named only inside another source's reference list.

Where a citation link was not checked: "Unverified citation relationship."

## A. Oppositional citing papers (ranked, most threatening first)

| Paper | Year | Cites foundational/hub? | Main criticism | Evidence quality | Relationship to claim | Verification state | Field uptake | Strength |
|---|---:|---|---|---:|---|---|---|---|
| A1. Vohs, K. D., Schmeichel, B. J. et al., "A Multisite Preregistered Paradigmatic Test of the Ego-Depletion Effect", Psychological Science 32(10):1566–1581 (2c A03) — replication / failed replication; cites foundational paper directly (VO-E1 p.1568, full text) | 2021 | yes (target: "The seminal article") | Proponent-led, preregistered, 36 labs, N = 3,531, blinded analysis team. Confirmatory d = 0.06; Bayesian data about 4 times more likely under the null (abstract). Figure-tracing duration, the field-6 outcome family, d = 0.15 [0.02, 0.29], n = 1,216 (Table 4). Authors conclude depletion is "not as reliable or robust as previously assumed" (VO-E3) | 4 | weakens L2 (general effect near zero); narrows field 6 (different manipulations: e-crossing and writing, not food temptation) | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED: Englert & Bertrams 2021 (2c A06, full text) contest the writing-task protocol and note analytic degrees of freedom in figure tracing, while saying they are "not picking a side" on whether depletion exists. Standing: strong, contested on operationalization | partial (recent; 2c RECENT-1: 8/25 cite a listed critique or null test) | severe for the magnitude; strong (not decisive) for field 6 |
| A2. Hagger, M. S., Chatzisarantis, N. L. D. et al., "A Multilab Preregistered Replication of the Ego-Depletion Effect", PPS 11(4):546–573 (2c N45) — registered replication; cites foundational paper directly (RRR-E1 p.548) | 2016 | yes (target) | 23 labs, N = 2,141: d = 0.04 [−0.07, 0.15] (abstract; p.554). Explicitly did not use the radish task because it needs "extensive experimenter involvement" (p.548) | 3 | weakens L2 in a computerized e-task → MSIT paradigm; does not test field 6's protocol | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED: the founding authors replied that it "did not test ego depletion" (BV-E1; manipulation critique); A1 then used the authors' preferred paradigms and found a similar null. Standing: strong for its paradigm; the manipulation objection is largely answered by A1 | substantively engaged (disputed 2016, partly accepted 2021) | strong |
| A3. Carter, E. C., Kofler, L. M., Forster, D. E. & McCullough, M. E., "A Series of Meta-Analytic Tests of the Depletion Effect", JEP:General 144(4):796–815 (2c X16) — meta-analysis / methodological critique; cites foundational paper directly (CA-E1) | 2015 | yes (target; and Table 1 codes the target's Exp 1 and Exp 3 as data) | 116 experiments in eight data sets; bias-corrected estimates small or near zero. Impossible-puzzles data set (k = 16): random-effects g = 0.79 [0.56, 1.02]; PET −0.16 [−0.76, 0.43]; PEESE 0.22 [−0.16, 0.60] (PET/PEESE table). Table 1 codes the target's Exp 1 as g = 1.31 (n1 = 25, n2 = 44) and Exp 3 as g = 0.74 (15, 15) | 2 | weakens L2 at literature level; places field 6 among large-g small-n studies | FULL-TEXT-CONFIRMED; reception checked one level: CONTESTED. Inzlicht, Gervais & Berkman, "Bias-correction techniques alone cannot determine whether ego depletion is different from zero" (LOCATED via the reference lists of A1 and of Baumeister & Vohs 2016; not read). A1 reports that the meta-analytic challenge has been criticized on methodological grounds | cited in passing by later multi-site tests (A1 p.1567; Dang 2021 Introduction) | moderate |
| A4. Dang, J. et al., "A Multilab Replication of the Ego Depletion Effect", SPPS 12(1):14–24 (2c A01) — replication; cites foundational paper directly (DA-E1) | 2021 | yes (target) | 12 labs, N = 1,775, Stroop → antisaccade: d = 0.10 [0.01, 0.19]; d = 0.16 after excluding random responders (abstract) | 3 | supports a weaker version (small nonzero L2 in one paradigm); narrows field 6 | FULL-TEXT-CONFIRMED (author manuscript; VERSION-SUBSTITUTE); RECEPTION: not checked this run — capped "contested / needs verification" | unclear / needs verification | moderate (capped) |
| A5. Carter, E. C. & McCullough, M. E., "Publication bias and the limited strength model of self-control", Frontiers in Psychology (2c A09) — bias re-analysis; cites foundational paper per OpenAlex | 2014 | yes (OpenAlex edge; text not read) | Bias re-analysis of Hagger et al. 2010 (title) | 2 | weakens L2 (literature) | LOCATED (metadata); reception not checked; capped | unclear / needs verification | weak (capped) |
| A6. Job, V., Dweck, C. S. & Walton, G. M., "Ego Depletion—Is It All in Your Head?", Psychological Science (2c A32) — primary empirical study; cites foundational paper (CTX-E40 excerpt) | 2010 | yes (excerpt) | Lay theories of willpower moderate depletion (R3) | 1 | complicates L3 | EXCERPT only; reception partly checked: A1's exploratory tests found no moderation by willpower beliefs (abstract), but in a sample with almost no effect to moderate. Standing: contested; capped | cited (premise for R3 work) | weak (capped) |
| A7. Inzlicht, M. & Schmeichel, B. J. 2012, PPS (N47); Kurzban, R., Duckworth, A. L., Kable, J. W. & Myers, J. 2013, BBS (N37) — theoretical papers; cite foundational paper (OpenAlex edges) | 2012–2013 | yes (OpenAlex) | Process / opportunity-cost accounts: no resource is consumed (R2) | 1 | complicates L3 | LOCATED (metadata); reception not checked; capped | inside RECEPTION-1 (2c) | weak as evidence; important as rival theory |
| A8. Ryan, R. M. & Deci, E. L., "Self-Regulation and the Problem of Human Autonomy", Journal of Personality (2c N27) — theoretical paper with new experiments; cites foundational paper (CTX-E13 excerpt) | 2006 | yes (excerpt) | New experiments found "true choice was not depleting" (CTX-E13), against Exp 2's high-choice condition | 1 | narrows C2 (Exp 2), not field 6 | EXCERPT only; capped | unclear | weak |
| A9. Lange, F. & Eggert, F. 2014 (A16); Chatzisarantis, N. L. D. & Hagger, M. S. 2014 (A19), Appetite — primary studies on glucose; cite foundational paper (OpenAlex edges) | 2014 | yes (OpenAlex) | Glucose drinks fail to counteract depletion; unsuccessful replications of glucose effects (titles) | 1 | weakens L3 (glucose version of the mechanism) | LOCATED (titles); capped | unclear | weak (capped) |

**Self-application note (symmetry).**
- A1 and A2 test L2 with manipulations other than food temptation. Neither is a direct test of field 6. Their threat to field 6 runs through the claim that d ≈ 1.8 estimates a reproducible effect, not through a re-run of Experiment 1.
- A3's Table 1 is a second, independent reading of the target's own statistics. It gives g = 1.31 for Exp 1, smaller than S2's d = 1.80. The difference is consistent with Carter comparing the radish cell (n1 = 25) with the two controls pooled (n2 = 44), while S2 compares radish with chocolate (t(44)). Carter's n1 + n2 = 69 differs from S2's N = 67. This discrepancy is unresolved without the target's body; field 6's numbers stay PROVISIONAL.

**Temptation noted (symmetric scoring).** I was tempted to give A2 (the RRR) a 4 as the first registered multi-lab test. I gave it 3 because its manipulation was credibly disputed (BV-E1) and its paradigm differs from field 6. A1 gets 4 because it is larger, proponent-designed and blinded, and includes field 6's outcome family. A4 is scored 3 here as opposition and 3 again in E1 as support: the same evidence gets the same score on both sides.

## B. Non-citing opposition

| Paper / source | Year | Does not cite hub? | Main argument | Why it matters | Evidence quality | Relationship to claim | Reception (if load-bearing) |
|---|---:|---|---|---|---:|---|---|
| B1. Witte, E. H. & Zenker, F., "Extending a Multilab Preregistered Replication of the Ego-Depletion Effect to a Research Program", Basic and Applied Social Psychology (2c A02) — re-analysis; found through keyword search (ADJUDICATION-1) | 2017 | does not cite the target (OpenAlex refs, 14, omit it); hub citation not checked | Extends the RRR to a research-program assessment (title) | Bears on how much the RRR null generalizes | 1 | unclear / needs verification | not load-bearing; LOCATED |
| B2. Jia, L., Yu, R., Hirt, E. R. & Fishbach, A., "Motivational Tuning in Response to Ego Depletion" (2c A24) — primary study; keyword search | 2016 | does not cite the target (OpenAlex refs, 83) | Depletion shifts motivation (R2) (title) | R2 rival from within depletion research | 1 | complicates L3 | not load-bearing; LOCATED |
| B3. Giboin, L.-S. & Wolff, W., "The effect of ego depletion or mental fatigue on subsequent physical endurance performance" (2c A10) — meta-analysis; keyword search | 2019 | does not cite the target (OpenAlex refs, 104) | Treats depletion and mental fatigue together (title) | Mental-fatigue framing (R2/R4) | 1 | complicates L3 | not load-bearing; LOCATED |
| B4. Section E locked adjacent sources (2c X01–X15), e.g. Webster, Richter & Kruglanski 1996 (mental fatigue, X01); Maier & Seligman 1976 and Abramson, Seligman & Teasdale 1978 (learned helplessness, X04–X05); Kavanagh 1987 (mood and persistence, X08); Rosenthal 1968 (experimenter expectancy, X11) — adjacent-field canonical papers; adjacent-field search (Section E lock) | 1968–1996 | predate the target; not in the target's reference list | Rival explanations for persistence decrements | See D | 1 each (titles only) | complicates (R2, R4) | not load-bearing; LOCATED |

Why outside the network: B1–B3 are within-field works whose OpenAlex reference lists omit the target (they cite later reviews instead). B4 predate the target and belong to clinical, educational and methods literatures.

None is load-bearing. Section C covers which ones the target and hubs should have engaged.

## C. Neglected references the hub should have cited

| Neglected source | Year | Relevance | Cited by foundation? | Cited by hub? | Effect of omission | Evidence quality |
|---|---:|---|---|---|---|---:|
| C1. Rosenthal, R., "Experimenter expectancy and the reassuring nature of the null hypothesis decision procedure", Psychological Bulletin (X11); expectancy-control methods (X12, balanced placebo) | 1968 | A non-blind experimenter delivered the food manipulation and timed the DV (2a Section A; 2b §5) | no (OpenAlex reference list, METADATA) | no for N06, N16, N19 (OpenAlex reference lists, METADATA; 129, 184, 83 refs) | moderate weakness: the obvious design control (blind or automated timing) is absent from the method as described; the RRR later rejected the task for this reason (p.548) | 1 |
| C2. Maier & Seligman 1976; Abramson, Seligman & Teasdale 1978 (X04, X05) — learned helplessness | 1976–78 | The outcome is persistence on unsolvable puzzles | no | no (N06, N16, N19; METADATA) | minor context loss: every cell faced the same unsolvable puzzles, so helplessness explains the contrast only if the first task changes susceptibility to it, which is a version of R4 | 1 |
| C3. Kavanagh 1987, "Mood, Persistence, and success" (X08) | 1987 | Mood alters persistence (R4) | no; the target cites Mayer & Gaschke 1988 on mood (reference list) | no (METADATA) | minor: mood was reportedly measured (see E0 CV-4) | 1 |
| C4. Webster, Richter & Kruglanski 1996 (X01) and the older mental-fatigue literature (X02, 1931) | 1931–96 | Fatigue as a non-resource account of performance decrements (R2) | no | no (METADATA) | moderate for L3 (mechanism), none for field 6's observed difference | 1 |

## D. Ignored adjacent fields (4–6)

| Adjacent field | Key sources | Why relevant | Better method / measure | Decisive test suggested | Engagement by target field | Effect of neglect |
|---|---|---|---|---|---|---|
| D1. Experimenter-expectancy and blinding methods | Rosenthal 1968 (X11); balanced-placebo design (X12) | Field 6's manipulation and DV timing were experimenter-run | blind delivery; automated timing; computerized tasks | the food protocol run with blinded experimenters and automated timing, preregistered | adopted later (RRR and A1 use computerized tasks); never applied to the food protocol | moderate (for field 6) |
| D2. Motivation / opportunity-cost and mental-fatigue accounts | Inzlicht & Schmeichel 2012 (N47); Kurzban et al. 2013 (N37); Webster et al. 1996 (X01); Giboin & Wolff 2019 (A10) | R2 explains a persistence drop without a resource | motivation and effort ratings; incentive manipulations | does an incentive or a reason to persist remove the decrement? | engaged inside the network from 2012 (N47 and N37 are RECEPTION-1 members) | moderate (L3); minor (field 6) |
| D3. Meta-science of small-study bias | Carter et al. 2015 (X16); Carter & McCullough 2014 (A09); Schimmack 2016 (X18) | Field 6 is a large effect from small cells | bias-corrected meta-analysis; registered multi-site tests | registered high-powered replication | engaged from 2014; the founding authors dispute it (X17) | major (for the magnitude) |
| D4. Lay theories of willpower | Job, Dweck & Walton 2010 (A32) | R3: beliefs, not a resource, drive decrements | belief measures and manipulations | belief manipulation crossed with the depletion manipulation | engaged (A32 cites the target); A1 found no belief moderation in a near-null sample | minor-to-moderate (L3) |
| D5. Learned helplessness and uncontrollable failure | Maier & Seligman 1976; Abramson et al. 1978 (X04, X05) | Unsolvable puzzles are the outcome task | solvable vs unsolvable outcome tasks | first-task × solvability interaction | not engaged by the target or its hubs (METADATA) | minor (constant across cells) |

## E. Strongest evidence supporting the original claim

### E0. Source self-defense check (run first)

What of the target could be searched:
- the abstract (PubMed 9599441), read in full;
- the reference list (OpenAlex, 57/58 titles; METADATA);
- secondhand descriptions of the body: S1 slides (means), S2 (procedure; and S2's quotation of the target's note on a science-fair replication), S4 p.548 (tasks), Carter et al. 2015 Table 1 (coded effect sizes), and two citing passages describing the target's mood measures (2c CTX-E3, N06 founding-cluster review; CTX-E46, A49 sport review).
- NOT searchable: introduction, method, results, discussion and any limitations paragraph. No authorized copy exists.

Rule a therefore cannot be met in full. Every UNAFFECTED row below means "not answered in the abstract, reference list or the secondhand descriptions"; it does not mean the body is silent.

| Prosecutor finding | Source passage that anticipates it (quote + location) | Type | Does it answer the finding? | Effect on the finding |
|---|---|---|---|---|
| 2a IV-1: d ≈ 1.8–2.0 with about 22 per cell | Target note (quoted by S2): an independent science-fair replication; "These converging results strengthen confidence in the present findings." (secondhand) | sensitivity test (informal replication, reported) | not at all (unpublished, unquantified, a school project) | UNAFFECTED — searched abstract, reference list and secondhand descriptions. External, not E0: Carter Table 1 codes g = 1.31 (25 vs 44 pooled controls). The finding is restated in G2 as "a large effect, g ≈ 1.3 to d ≈ 1.8 depending on comparison", still from small cells |
| 2a IV-2: proponent-led 36-lab test, d = 0.06 | NONE FOUND (post-dates the source) | NONE FOUND | not at all | UNAFFECTED — the source cannot pre-empt 2021 data. Re-aimed in G2 (object mismatch) |
| 2a IV-3: RRR d = 0.04 | NONE FOUND (post-dates) | NONE FOUND | not at all | UNAFFECTED |
| 2a IV-4: Dang 2021 d = 0.10 | NONE FOUND (post-dates) | NONE FOUND | not at all | UNAFFECTED |
| 2a IV-5: bias-corrected meta-analysis near zero | NONE FOUND (post-dates) | NONE FOUND | not at all | UNAFFECTED |
| 2a IV-6: power ≈ .10 at d = 0.2 with 22 per cell | NONE FOUND in the abstract or secondhand descriptions | NONE FOUND | not at all | UNAFFECTED (search limited; body not read) |
| 2a IV-7: field-level selective reporting | NONE FOUND for the 1998 paper; the first author's 2016 remark (via S2) is general, not about this paper | NONE FOUND | not at all | UNAFFECTED (search limited) |
| 2a IV-8: authors contest the RRR manipulation | not a charge against the source (an author defense, 2016) | NONE FOUND | n/a | UNAFFECTED |
| 2b CV-1: FORM — resource unmeasured; effort without decrement externally | Abstract: volition "may all draw on a common inner resource"; results "suggest" the capacity is limited | scope (hedge) | partly | RECHARACTERIZED — the source offers the resource as a hedged inference ("may", "suggest"), not as a measured quantity. New charge: "mechanism inferred from behaviour, hedged, and not tested against rivals", not "mechanism asserted". |
| 2b CV-2: DOMAIN — unity across "unrelated acts" inferred | Abstract: four different manipulations and outcomes produce same-direction decrements, and the results "suggest … a range of seemingly different, unrelated acts share a common resource" | sensitivity test (convergent design across four experiments) + scope (hedge) | partly | RECHARACTERIZED — the source did test unity by convergence across four paradigms. New charge: "tested inadequately: separate experiments, no crossed design, no shared-variance test". |
| 2b CV-3: persistence as a proxy for capacity | Abstract: Exp 3 measured anagram performance, Exp 4 a passive-option choice, not persistence | sensitivity test (different outcome measures) | partly | NARROWED — restated: "every outcome across the four experiments is behavioural; none measures capacity or separates it from willingness". The charge is no longer specific to persistence time. |
| 2b CV-4: hunger, affect and experimenter confounds | Secondhand: N06 (founding-cluster review) says the food test was run "to help rule out moods as a potential explanation" (CTX-E3); A49 says effects were "not caused by … mood differences (e.g., Baumeister et al., 1998 …)" (CTX-E46). Design (S2): a chocolate-eating control as well as a no-food control | sensitivity test (mood measure, reported secondhand) + design control | partly | NARROWED — restated: "affect reportedly checked (PROVISIONAL, two citing passages, one from the founding cluster); food intake partly equated by the chocolate control; non-blind experimenter delivery and timing remain unaddressed". |
| 2b CV-5: downstream overextension (lecture/lay) | The abstract's hedges ("may", "suggest") are absent in D1/D1b | scope | — (the source text supports the finding's PR-layer location) | UNAFFECTED |
| 2b CV-6: definition–operationalization scope UNKNOWN | Abstract defines the construct as "capacity for active volition" | NONE FOUND (no operational definition in the abstract) | not at all | UNAFFECTED (search limited) |
| 2c F1: paradigm untested at scale; general effect near zero to small | NONE FOUND (post-dates); the science-fair note (above) is the only replication the source reports | NONE FOUND | not at all | UNAFFECTED |
| 2c F2: founding-cluster-centred reception | not a paper-layer charge | NONE FOUND | n/a | UNAFFECTED |
| 2c F3: recent premise use | not a paper-layer charge | NONE FOUND | n/a | UNAFFECTED |
| 2c F4: resource stated as shown in citing passages | Abstract hedges: "may", "suggest" | scope | — (supports the finding: the citing restatements are stronger than the source) | UNAFFECTED |
| 2c F5: mixed critique uptake | not a paper-layer charge | NONE FOUND | n/a | UNAFFECTED |
| 2c F6: no learned-helplessness or experimenter-expectancy work in the reference list | Reference list (METADATA) includes stress-aftereffect works (Glass et al. 1969, "Psychic cost of adaptation to an environmental stressor"; Cohen 1980, aftereffects of stress on performance), perceived-control works (Langer 1975; Rothbaum et al. 1982; Burger 1989), persistence and expectation of success (Feather 1961; McFarlin et al. 1985), mood (Mayer & Gaschke 1988) and self-reported effort (Johnson & Saccuzzo 1995) | acknowledged adjacent literature (reference-list level) | partly | NARROWED — restated: "the reference list engages stress-aftereffect, perceived-control, persistence-expectancy and mood literatures that overlap the helplessness and motivation rivals; it lacks learned helplessness proper and any experimenter-expectancy or blinding work". How the body uses these references is unknown. |
| 2c F7: retrieval and record limits | not a paper-layer charge | NONE FOUND | n/a | UNAFFECTED |

E0 RESIDUAL: 21 prosecutor rows. DEFEATED 0; NARROWED 3 (CV-3, CV-4, 2c F6); RECHARACTERIZED 2 (CV-1, CV-2); UNAFFECTED 16 (IV-1–IV-8, CV-5, CV-6, 2c F1–F5, F7).

Most UNAFFECTED rows are post-publication evidence (IV-2–IV-5, 2c F1) or non-paper-layer findings (IV-8, CV-5, 2c F2–F5, F7). For IV-1, IV-6, IV-7 and CV-6 the silence is partly structural: the body could not be searched. That limitation is the main weakness of this E0 and is carried into J2.

Rule-b check:
- The source's only reported robustness evidence on field 6 is the science-fair replication note (secondhand). It is not a sensitivity analysis of the element 2a calls load-bearing (the size of the effect from small cells).
- Severity for IV-1 and IV-6 is therefore not reduced by E0. It is changed only by the external Carter coding (G2).

### E1. External supporting evidence

| Supporting source | Year | What it supports | Answers construct problem? | Runs decisive test? | Strong or narrow claim? | Verification state | Impact on audit |
|---|---:|---|---|---|---|---|---|
| S1. Vohs et al. 2021 (A1) read as support: figure-tracing duration d = 0.15 [0.02, 0.29] (Table 4); exploratory full-sample d = 0.08 with Bayesian evidence "about equally likely" under null and informed prior (abstract) — replication | 2021 | a small persistence decrement after self-control exertion (L2, weak form) | no (effort felt strongly, d = 1.31 on the effort index per 2b; little downstream change) | partly (large, preregistered; not the food protocol) | narrow (d ≈ 0.1–0.15) | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED (A06 contest) | narrows the critique: an L2 residual on the field-6 outcome family survives. Evidence quality 4 as a study; as support for d ≈ 1.8 it gives nothing |
| S2. Dang et al. 2021 (A4) read as support: d = 0.10 [0.01, 0.19]; 0.16 after exclusions — replication | 2021 | small nonzero L2 in one paradigm | no | no (different paradigm) | narrow | FULL-TEXT-CONFIRMED (VERSION-SUBSTITUTE); reception not checked — capped | narrows the critique (2a already keeps this residual). Evidence quality 3 |
| S3. Carter et al. 2015 Table 1 coding of the target (Exp 1 g = 1.31, n 25/44; Exp 3 g = 0.74, n 15/15) — meta-analysis (coding) | 2015 | that the target reported large effects from small cells, read by an independent group from the full text | no | no | describes what the target reported, not whether it is true | FULL-TEXT-CONFIRMED (coding table); the coding itself is not contested in the reception located | narrows IV-1's magnitude range and corroborates field 6's reported direction and size (secondhand). Evidence quality 2 |
| S4. Hagger et al. 2010 meta-analysis (N16): d ≈ 0.62 across 198 tests (as reported by the RRR p.547 and S2) — meta-analysis / systematic review | 2010 | L2 strong form | no | no | strong | LOCATED + EXCERPT (CTX-E8); value secondhand. Reception: CONTESTED/weakened — Carter & McCullough 2014 (A09, LOCATED) and Carter et al. 2015 (full text; revised inclusion criteria and bias tests) | no effect. Evidence quality 1 after reception |
| S5. Baumeister & Vohs 2016 comment (2c X17): the RRR "did not test ego depletion" (BV-E1) — commentary | 2016 | that the RRR null does not bear on depletion | no | no | narrow (about the RRR) | FULL-TEXT-CONFIRMED; reception: answered in large part by A1, which used the authors' preferred paradigms and found d = 0.06 | narrows IV-3 only (already narrowed in 2a). Evidence quality 1 |
| S6. Englert & Bertrams 2021 (2c A06): A1 gives "no evidence for or against" depletion; the writing protocol and figure-tracing scoring are questioned — commentary (opinion) | 2021 | that A1 is inconclusive rather than a refutation | no | no | narrow (about A1) | FULL-TEXT-CONFIRMED; reception not checked — capped | narrows the critique: supports re-aiming IV-2 from DEFEATS (G2). Evidence quality 1 |
| S7. Gailliot et al. 2007 glucose studies (N41) — primary empirical study (founding cluster) | 2007 | L3 (resource = glucose) | partly (a proposed resource marker) | no | strong | EXCERPT (CTX-E17). Reception: weakened — A9 (two 2014 Appetite papers, LOCATED: glucose drinks fail; unsuccessful replications); S2 describes statistical evidence of bias in the glucose studies | no effect on field 6. Evidence quality 1 |
| S8. The target's science-fair replication note (via S2) | 1998 | Exp 1 direction | no | no | narrow | PROVISIONAL (secondhand quotation; unpublished replication) | no effect. Evidence quality 0 |

Honest summary:
- No large or preregistered study supports an effect near field 6's d ≈ 1.8. No direct, high-powered replication of the food-temptation protocol was found (2c I18: 0/59 DIRECT (L1) in ADJUDICATION-1, recall 8/12).
- The strongest support (S1, S2) backs only a small sequential-task effect (d ≈ 0.10–0.15), including on the persistence outcome family. That is a weak version of L2, not field 6.
- S6 is the strongest argument that the large tests are inconclusive rather than refuting. It is an opinion piece and is capped.

## F. Citation-network uptake of opposition

| Opposition / neglected source | Cited by hub? | Later uptake? | Engagement quality | Survived reception check? | Suppression vs. correctly-discounted | Network implication |
|---|---|---|---|---|---|---|
| A1 Vohs et al. 2021 | n/a (post-dates the hubs); co-authored by founding author Muraven (2c I20) | recent; 2c RECENT-1: 8/25 cite a listed critique or null test | incorporated into model revision (in part): "not as reliable or robust as previously assumed" (VO-E3) | yes (contested on operationalization only) | neither: no low-uptake claim | partial uptake |
| A2 RRR 2016 | founding authors replied (X17) | inside RECEPTION-1 (top-50 citers) | cited but dismissed (2016: "did not test ego depletion"), then partly accepted via A1 (2021) | yes | neither | partial uptake |
| A3 Carter et al. 2015 | not determined (hub reference lists predate it) | cited by A1 and Dang 2021 | cited in passing; criticized on method (Inzlicht et al. comment, LOCATED) | CONTESTED | low uptake not established; not assessed | partial uptake |
| A4 Dang et al. 2021 | n/a | not measured | unclear / needs verification | not checked | n/a (too recent to judge) | unclear / needs verification |
| A7 process and opportunity-cost models (N47, N37) | not determined | inside RECEPTION-1 | cited and reframed (not inspected; METADATA) | not checked | n/a | partial uptake |
| C1 experimenter expectancy (Rosenthal 1968) | no (N06, N16, N19 METADATA) | not in the network | not cited | not applicable (canonical method, not a rebuttable finding) | low uptake: (a) neglect of a relevant method and (b) a judgment that it was irrelevant are both possible; neither verified, so no suppression claim | evidence not engaged at the source and hub level; later replications adopted computerized tasks |

Verified conditions:
- (i) Reception survival is verified for A1 and A2.
- (ii) Low uptake is not shown for A1 or A2: both sit in the network and drew author responses.

No "critique marginalized" claim is made. 2c Finding 3 (six inspected recent passages use the resource model as a premise) is incomplete uptake at the citer level, not marginalization by the field.

## G. Summary table — opposition strength

| Category | Number Found | Strongest Example | Evidence Quality | Verification state | Impact on Central Claim |
|---|---:|---|---:|---|---|
| Oppositional citing papers | 9 entries (12 works) | Vohs et al. 2021 (A1) | 4 | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED (contested on operationalization) | strengthens audit on magnitude; weakens audit's DEFEATS framing for field 6 (different paradigm) |
| Non-citing opposition papers | 4 entries (≥8 works, none load-bearing) | Witte & Zenker 2017 (B1) | 1 | LOCATED | needs verification |
| Neglected references | 4 | Rosenthal 1968 (C1) | 1 | LOCATED | narrows claim (experimenter control) |
| Ignored adjacent fields | 5 | Small-study bias meta-science (D3) | 2 | FULL-TEXT-CONFIRMED (Carter); CONTESTED | strengthens audit (magnitude) |
| Strongest support for original claim | 8 | Vohs 2021 figure-tracing d = 0.15 (S1) | 4 (as a study) | FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED | narrows claim (small L2 residual only) |

The three most threatening findings in order of severity are:
1. Vohs et al. 2021: proponent-led, preregistered, 36 labs, d = 0.06 overall and 0.15 on figure-tracing duration. FULL-TEXT-CONFIRMED and RECEPTION-CONFIRMED (contested on operationalization by Englert & Bertrams).
2. Hagger et al. 2016 RRR: 23 labs, d = 0.04. FULL-TEXT-CONFIRMED and RECEPTION-CONFIRMED (manipulation objection largely answered by #1).
3. Carter et al. 2015: bias-corrected estimates near zero, with the target's Exp 1 coded at g = 1.31 from 25 vs 44 participants. FULL-TEXT-CONFIRMED; reception CONTESTED (bias-correction method).

All three bear on field 6 indirectly: none re-ran the food-temptation protocol.

Capped out of the top three:
- Dang et al. 2021 (reception not checked);
- the paper-alone small-cell threat IV-1 / IV-6 (PROVISIONAL: secondhand N and statistics);
- Englert & Bertrams 2021 as support (opinion; reception not checked).

## G2. Did the prosecution attack the strongest version?

Finding-level target gate. Every supplied prosecutor's findings get a row: 2a IV-1…IV-8, 2b CV-1…CV-6, 2c Findings 1–7 (21 rows). Declared targets are read from each stage's standardized finding row.

| Prosecutor | Finding | Declared target claim | Claim-map version attacked | Matches field 6? | Failure location | Severity after re-aiming |
|---|---|---|---|---|---|---|
| internal-validity (2a) | IV-1 implausibly large d with ~22 per cell | Field 6 | field 3 (the one-lab result itself) | yes | PAPER | moderate (PROVISIONAL). Restated after Carter's coding: a large effect (g ≈ 1.3 vs pooled controls to d ≈ 1.8 vs chocolate) from small cells. The g/d discrepancy and N 67 vs 69 stay open |
| internal-validity (2a) | IV-2 Vohs 2021, d = 0.06 (figure tracing 0.15) | Field 6 (via L1/L2) | field 2 / L2 (general effect); not the food protocol | partly — different manipulations (e-crossing, writing); same outcome family (figure-tracing persistence) | PAPER (for the magnitude claim) | RE-AIMED. Fatal for the inference from field 6 to a moderate-or-larger general effect (L2). Major, not DEFEATS, for field 6 itself: the food-temptation protocol was not re-run, the RRR declined it (p.548), 2b §8 calls the match partial, and A06 contests the operationalization |
| internal-validity (2a) | IV-3 RRR, d = 0.04 | Field 6 (via L2) | field 2 / L2 | partly (different paradigm) | PAPER | moderate (unchanged); the manipulation dispute (BV-E1) is largely answered by IV-2 |
| internal-validity (2a) | IV-4 Dang 2021, d = 0.10 | Field 6 (via L2) | field 2 / L2 | partly | PAPER | moderate (unchanged); doubles as weak support (E1 S2) |
| internal-validity (2a) | IV-5 bias-corrected meta-analysis ≈ 0 | Field 6 (via L2) | field 2 / L2 (literature); the target's Exp 1 and Exp 3 are data points in Carter's sets | partly | PAPER | moderate; reception CONTESTED (bias-correction critique, LOCATED), so it cannot carry more than moderate |
| internal-validity (2a) | IV-6 power ≈ .10 at d = 0.2 | Field 6 | field 3 | yes | PAPER | minor (PROVISIONAL). Its relevance depends on a true effect near 0.2, a premise taken from post-2015 tests; nested with IV-1 |
| internal-validity (2a) | IV-7 field-level selective reporting | Field 6 | not a mapped version: field-wide practice (S2, 2016 remarks), not the 1998 paper | partly | PAPER (field-level; not shown for this paper) | minor (PROVISIONAL); not paper-specific |
| internal-validity (2a) | IV-8 authors contest the RRR manipulation | Field 6 | a defense of field 2 against IV-3 | partly | — (author response) | not a threat; narrows IV-3 only |
| construct-validity (2b) | CV-1 FORM: resource unmeasured | Field 6 (interpretation) | field 2 (mechanism, hedged) | partly — bears on what field 6 means, not on the observed contrast | PAPER | moderate, RECHARACTERIZED by E0: hedged inference not tested against rivals |
| construct-validity (2b) | CV-2 DOMAIN: unity inferred | Field 6 (interpretation) | field 2 (unity across four experiments) | no — unity is a field-2 claim across experiments | PAPER | moderate for field 2; none for field 6. RECHARACTERIZED: tested inadequately (convergence without a crossed design) |
| construct-validity (2b) | CV-3 persistence as capacity proxy | Field 6 | field 3 → field 2 step | yes | PAPER | moderate, NARROWED: all four outcomes are behavioural; none measures capacity |
| construct-validity (2b) | CV-4 hunger, affect, experimenter confounds | Field 6 | field 3 | yes | PAPER | moderate → minor-to-moderate, NARROWED: affect reportedly checked (PROVISIONAL), chocolate control; non-blind delivery and timing remain |
| construct-validity (2b) | CV-5 lecture overextension | Downstream (D1) | field 4 | no | PR/MEDIA | moderate at the PR layer; none at the paper layer. The source is defensible on this point; the failure is at the PR layer |
| construct-validity (2b) | CV-6 definition–operationalization UNKNOWN | Field 6 | field 2 → field 1 | partly | PAPER (UNKNOWN) | minor (unchanged); nested with CV-3 |
| citation-network (2c) | F1 paradigm untested at scale; general effect near zero to small | field 6 | field 3 (L1) and L2 | yes | PAPER | major scope loss (NARROWS), unchanged. Consistent with IV-2 re-aimed |
| citation-network (2c) | F2 founding-cluster-centred reception | field 6 | the network's use of field 2 | yes (as declared) | CITATION | moderate (SURVIVES; 2c dimension score 2) |
| citation-network (2c) | F3 recent premise use | MAP GAP (downstream use) | field 4 (citing literature) | MAP GAP | CITATION | moderate at the citation layer; none at the paper layer |
| citation-network (2c) | F4 resource stated as shown | MAP GAP (downstream restatements) | field 4 | MAP GAP | CITATION | moderate at the citation layer; nested with CV-5 only as the same kind of drift (different layer, different evidence; counted separately) |
| citation-network (2c) | F5 mixed critique uptake | field 6 | network handling of opposition | yes (as declared) | CITATION | minor-to-moderate (dispute 2016, concession 2021) |
| citation-network (2c) | F6 adjacent rivals absent from the reference list | MAP GAP (source engagement) | the source's engagement (field 2 rivals) | MAP GAP | PAPER | minor, NARROWED by E0: related literatures cited; helplessness is constant across cells; experimenter expectancy remains the substantive gap |
| citation-network (2c) | F7 retrieval and record limits | MAP GAP (retrieval) | none (audit-process limit) | MAP GAP | MODEL/RETRIEVAL (audit's own retrieval) | caps confidence; not a finding against the source |

### Double-count guard [FAIL-MB-003]

Nested rows, one lever each:
1. **{IV-2, IV-3, IV-4, IV-5, 2c F1}** — large and bias-corrected tests show the general sequential-task effect is near zero to small. One evidentiary mechanism, one contribution to severity, one top-three place (taken by IV-2 / Vohs, with the RRR and Carter as separately reception-gated witnesses in the G list; the G ranking ranks sources, this guard ranks levers).
2. **{IV-1, IV-6}** — a large effect from small cells (winner's-curse logic).
3. **{CV-3, CV-6}** — behavioural outcome stands in for capacity; the definition is not operationalized.

Independent levers retained:
- CV-1 (mechanism unmeasured);
- CV-2 (unity untested);
- CV-4 (non-blind experimenter; residual confounds);
- CV-5 (PR layer);
- 2c F2–F5 (citation layer; F4 kept apart from CV-5 because the layer and evidence differ);
- 2c F6 (paper's reference engagement);
- IV-7 (field-level reporting);
- F7 (process).

IV-8 is not a threat.

### Questions

1. **Which version did each prosecutor attack?**
   - 2a: field 3 (IV-1, IV-6) and field 2 / L2 (IV-2–IV-5); IV-7 attacks field-wide practice (not mapped).
   - 2b: field 2 (CV-1, CV-2), the field 3 → field 2 step (CV-3, CV-6), field 3 (CV-4) and field 4 (CV-5).
   - 2c: field 3 and L2 (F1), network use (F2, F5), field 4 (F3, F4), source engagement and process (F6, F7; MAP GAP).
2. **Was that the version the audit was supposed to evaluate?**
   - Field 6 (the Exp 1 contrast) is attacked directly by IV-1, IV-6, CV-3, CV-4 and 2c F1.
   - The 2a DEFEATS (IV-2) aims at L2. A sound finding aimed at L2 does not establish DEFEATS for field 6 until re-aimed. Re-aimed, it NARROWS field 6 (major).
   - 2a's verdict INVALID therefore rests on L2 evidence, not on any test of the food protocol. 2c F1 (NARROWS) aims more precisely at field 6 and agrees with the re-aimed reading.
3. **Where does each failure live?** MIXED:
   - PAPER: the magnitude from small cells (IV-1, IV-6), behaviour → mechanism (CV-1, CV-3), unity (CV-2), the experimenter control gap (CV-4, F6), and the magnitude not reproducing as a general effect (IV-2–IV-5, F1).
   - CITATION: F2–F5.
   - PR/MEDIA: CV-5.
   - MODEL/RETRIEVAL: F7 (the audit's own retrieval).
4. **Failures outside the paper layer.**
   - "The source is defensible on this point; the failure is at the PR layer" (CV-5: "Willpower is limited", "One Willpower, not Many" vs the abstract's "may" and "suggest").
   - "The source is defensible on this point; the failure is at the citation layer" (F3, F4: citing passages state the resource as shown).
5. **Does severity survive re-aiming?**
   - IV-2 changes from DEFEATS to major NARROWS for field 6. It stays fatal for the L2 inference "field 6 shows a moderate-or-larger general depletion effect".
   - IV-1 survives at moderate (provisional), restated.
   - CV-1 and CV-2 survive at moderate for field 2, with no direct severity against field 6.
   - CV-3 and CV-4 survive, narrowed.
   - CV-5, F3 and F4 establish no paper-layer severity.
   - F6 is reduced to minor.

MAP DISAGREEMENT: the claim map located downstream inflation at PR/MEDIA only ("Citing-literature layer: no inflation found in D3", field 5B). The prosecution's findings indicate citation-layer inflation as well: 2c F4 finds citing passages that state the resource drain as shown, and 2c F3 finds six inspected recent passages using the model as a premise. The map's D3 check covered one citing passage (S4); 2c inspected far more.

Required aggregate table:

| Question | Answer | Supporting prosecutor findings |
|---|---|---|
| Versions attacked | field 3 (one-lab contrast), field 2 / L2 (general effect, mechanism, unity), field 4 (downstream), plus MAP GAP rows on engagement and process | IV-1, IV-6, CV-4, F1 (field 3); IV-2–IV-5, CV-1, CV-2 (field 2 / L2); CV-5, F3, F4 (field 4); F6, F7 (MAP GAP) |
| Version audit targeted (map field 6) | the Exp 1 radish vs chocolate vs no-food persistence contrast (PROVISIONAL numbers) | — |
| Finding-level match rate | 7/21 yes; 8/21 partly; 2/21 no; 4/21 MAP GAP | yes: IV-1, IV-6, CV-3, CV-4, F1, F2, F5; partly: IV-2–IV-5, IV-7, IV-8, CV-1, CV-6; no: CV-2, CV-5; MAP GAP: F3, F4, F6, F7 |
| Failure location(s) | MIXED: PAPER (magnitude, mechanism, unity, experimenter control); CITATION (premise use, restatement); PR/MEDIA (lecture, APA page); MODEL/RETRIEVAL (audit limits) | see rows |
| Severity survives re-aiming? | partly: the magnitude critique survives in full for L2. Against field 6 it is major NARROWS, not DEFEATS. Construct findings survive narrowed or recharacterized. PR and citation findings carry no paper-layer severity | IV-2 (re-aimed), IV-1, CV-1–CV-4, CV-5, F3, F4 |
| Nested findings consolidated | {IV-2, IV-3, IV-4, IV-5, F1}; {IV-1, IV-6}; {CV-3, CV-6} | — |

## H. Revised thesis impact

Category: **F. Mixed.**
- Strengthened: the magnitude critique. An independent full-text coding (Carter Table 1) confirms the target reported a large effect from small cells. The RRR manipulation objection is largely answered by the authors' own preferred-paradigm test (Vohs 2021).
- Narrowed: the 2a DEFEATS/INVALID framing for field 6 itself (paradigm mismatch), and several construct findings (CV-3, CV-4, F6 narrowed; CV-1, CV-2 recharacterized).
- Not "C. Softened" alone: the central critique (field 6's size is not credible as a reproducible effect) got stronger, not weaker.

1. **Claims to remove:**
   - "Field 6 is DEFEATED by replication." No study re-ran the food-temptation protocol at scale; it was declined for experimenter involvement (RRR p.548).
   - The 2b CV-4 wording that implies affect was unchecked (the target reportedly measured mood; PROVISIONAL).
2. **Claims to narrow:**
   - IV-2: DEFEATS the L2 inference; NARROWS field 6 (major).
   - IV-1: g ≈ 1.3–1.8 depending on comparison, not "d ≈ 1.8–2.0".
   - CV-1: hedged inference, untested against rivals.
   - CV-2: tested by convergence, not by a crossed design.
   - CV-3: all outcomes behavioural.
   - CV-4: experimenter control is the remaining confound.
   - 2c F6: helplessness and expectancy literatures absent; stress, control and persistence literatures present.
3. **Claims to strengthen:**
   - The L2 conclusion: the general sequential-task effect is near zero to small (d ≈ 0.04–0.15 across three large preregistered tests, one proponent-led). A founding author co-signed the downgrade.
   - The magnitude point: field 6 is among the largest effects in Carter's impossible-puzzles set (g = 1.31 vs random-effects mean 0.79), from n1 = 25.
4. **Claims requiring better sourcing:**
   - Field 6's exact statistics (N 67 vs 69; d 1.8 vs g 1.31): needs the target's body.
   - IV-6 and IV-7 (PROVISIONAL).
   - The mood-check claim (two citing passages).
   - Dang 2021 reception.
   - The Carter reception (Inzlicht et al. comment, not read).
5. **Survived unchanged:**
   - IV-3, IV-4, IV-5 (as narrowing of L2);
   - CV-5 (PR layer);
   - 2c F1, F2, F3, F4, F5, F7.
6. **Evidence that most improves the thesis:** Vohs et al. 2021. FULL-TEXT-CONFIRMED and RECEPTION-CONFIRMED: proponent-designed, preregistered, d = 0.06, with the founding-cluster concession VO-E3.
7. **Evidence that most threatens the thesis** (the thesis that field 6 is INVALID): the same Vohs 2021 figure-tracing estimate d = 0.15 [0.02, 0.29], read with Englert & Bertrams 2021 (opinion; reception not checked, capped). Together they show the large tests did not re-run field 6's protocol and leave a small persistence effect, so "INVALID" overstates what the evidence shows about the Exp 1 result itself. The second-ranked threat is the absence of any direct test of the food protocol (2c I18, bounded by recall 8/12).

## I. Revised thesis paragraph

Baumeister et al. (1998) measured how long about 22 students per cell kept working on unsolvable figure-tracing puzzles after eating radishes while resisting chocolate, eating chocolate, or eating nothing. Per secondary readings, quitting came after about 8 vs 19–21 minutes (d ≈ 1.8 radish vs chocolate; Carter et al. code g = 1.31 against pooled controls). The abstract infers, with "may" and "suggest", that volition draws on one limited common resource. No resource was measured, and the four experiments used different manipulations and outcomes without a crossed test of shared variance.

The size of this effect is not credible as an estimate of a reproducible phenomenon. Three large preregistered multi-lab tests of the general sequential-task effect found d = 0.04 (RRR, 23 labs), 0.10 (Dang, 12 labs) and 0.06 (Vohs, 36 labs, proponent-designed). Vohs's figure-tracing persistence outcome was 0.15. Bias-corrected meta-analysis puts the impossible-puzzles literature near zero, though that method is itself contested. The founding authors' objection that the RRR "did not test ego depletion" is largely answered by Vohs 2021, which used their preferred paradigms and which a founding author co-signed.

None of these tests re-ran the food-temptation protocol. The RRR declined it because of experimenter involvement, and Englert & Bertrams (opinion, unchecked) read Vohs 2021 as inconclusive. Field 6 is therefore narrowed, not refuted. It survives at most as a one-lab result with a non-blind experimenter, implying a small effect if any. Field 2's mechanism and unity remain inferences.

The decisive test is a preregistered, blinded, automated-timing replication of the food-temptation → unsolvable-puzzle protocol with an incentive or motivation arm (R2) and an affect check (R4).

The citation network did not suppress the opposition. The RRR and Vohs 2021 sit inside the reception and drew founding-author responses, a 2016 dispute followed by a 2021 concession. But recent citing passages still use the resource model as a premise (2c F3, F4), so uptake is partial, at the citation layer.

## J. Final adversarial verdict

- **Strongest opposition to the foundational claim:** Vohs et al. 2021. FULL-TEXT-CONFIRMED; RECEPTION-CONFIRMED, contested on operationalization by Englert & Bertrams 2021 (full text). Assessed from the full text (abstract, Table 4) and the reception check.
- **Strongest support for the foundational claim:** Vohs 2021 figure-tracing duration d = 0.15 [0.02, 0.29]. Same standing. It supports only a small L2 persistence effect, not d ≈ 1.8. Carter's Table 1 coding corroborates what the target reported (g = 1.31), not that it is true.
- **Strongest neglected adjacent-field evidence:** experimenter-expectancy and blinding methods (Rosenthal 1968; LOCATED, title level). Absent from the target's and the hubs' reference lists (METADATA).
- **Strongest paper the hub should have cited:** Rosenthal 1968 (X11), or any experimenter-expectancy control work. Learned helplessness (X04, X05) is the more visible gap but matters less, because every cell faced the same unsolvable task.
- **Most important non-citing opposition:** none load-bearing. Witte & Zenker 2017 (B1, LOCATED) is the most relevant non-citing work.
- **Did the field engage the opposition?** Yes, partially: disputed in 2016 (BV-E1), conceded in part in 2021 (VO-E3). Citing passages still use the model as a premise (2c F3, F4).
- **Suppression check:** no "marginalized or suppressed" claim is made. The candidate sources (RRR, Vohs) survived reception and were engaged.
- **Did the opposition change the thesis?** Yes. DEFEATS/INVALID for field 6 becomes major NARROWS; the L2 critique is strengthened.
- **Source self-defense (E0):**
  - DEFEATED: none.
  - NARROWED:
    - CV-3: the abstract's Exp 3 and Exp 4 use non-persistence outcomes.
    - CV-4: affect reportedly checked, per N06 "to help rule out moods" (CTX-E3) and A49 (CTX-E46); chocolate control (S2).
    - 2c F6: the reference list includes Glass et al. 1969, Cohen 1980, Langer 1975, Feather 1961 and Mayer & Gaschke 1988.
  - RECHARACTERIZED:
    - CV-1: abstract "may all draw on a common inner resource";
    - CV-2: abstract "suggest … a range of seemingly different, unrelated acts share a common resource", tested by convergence.
  - UNAFFECTED (16): IV-1–IV-8, CV-5, CV-6, 2c F1–F5, F7. IV-1 was searched against the science-fair note (secondhand, S2): "These converging results strengthen confidence in the present findings."
  - Body not searchable.
- **Version the prosecution attacked:** mostly the strongest version (field 2 / L2) and the defensible version (field 3); the downstream version for CV-5, F3, F4.
- **Failure location:** MIXED. PAPER for magnitude, mechanism and experimenter control; CITATION for premise use; PR/MEDIA for the lecture and APA page; MODEL/RETRIEVAL for audit limits.
- **Does the severity survive re-aiming to the audited claim?** Partly. Major NARROWS for field 6, not DEFEATS; fatal for the L2 inference.
- **Finding-target alignment (G2):** 7/21 match field 6, 8/21 partly, 2/21 no, 4/21 MAP GAP.
- **Internal-validity coverage:** SUPPLIED AND CONSUMED (IV-1…IV-8 run through E0 and G2).
- **Double-count resolution:** {IV-2, IV-3, IV-4, IV-5, F1}, {IV-1, IV-6} and {CV-3, CV-6} consolidated; CV-1, CV-2, CV-4, CV-5, F2–F7 and IV-7 retained as independent levers.
- **Revised thesis impact category:** F (Mixed).
- **Claims to remove:** "field 6 DEFEATED by replication"; the implication that affect was unchecked.
- **Claims to narrow:** IV-2 (re-aimed), IV-1 (range), CV-1, CV-2, CV-3, CV-4, F6.
- **Claims strengthened:** L2 near zero to small (three large preregistered tests; founding-author concession); the field-6 magnitude among the largest in its outcome family.
- **Three most threatening findings ranked by severity:**
  1. Vohs 2021 (RECEPTION-CONFIRMED; contested on operationalization);
  2. RRR 2016 (RECEPTION-CONFIRMED; manipulation objection largely answered);
  3. Carter 2015 (CONTESTED; bias-correction critique LOCATED).
- **Main remaining source-risk:** the target's body was never read. Field 6's numbers (N 67/69; d 1.8 vs g 1.31), the mood checks and any limitations text are secondhand, so every E0 UNAFFECTED is bounded.
- **Confidence level:** Moderate for the L2 conclusion; Low for field-6-specific dispositions.
- **What evidence would change this assessment:**
  - an authorized copy of the target's body;
  - a preregistered, blinded replication of the food protocol;
  - reading Inzlicht, Gervais & Berkman (the Carter comment) and Dang 2021's reception;
  - evidence that the mood measure or the experimenter's knowledge of condition differed from the secondhand accounts.

## FIDELITY CHECK

Input 5 not supplied. The check did not run.

## J2. Self-tilt disclosure

- **Lean.** Toward the critique on the magnitude, and toward the paper on DEFEATS. Net: slightly toward the critique. The L2 evidence is strong, and I adopted it readily.
- **Least reception-checked findings:**
  - the mood-check narrowing of CV-4 (two citing passages, one from the founding cluster);
  - the science-fair note (secondhand);
  - Englert & Bertrams as support (opinion, reception not checked);
  - Dang 2021 (capped);
  - all LOCATED rows in A5–A9, B and C (titles only).
  - Nothing rests on model memory. The 00a known-items list is memory, but it was used only as 2c's recall benchmark, not as evidence here.
- **Sources introduced and promoted here:**
  - Carter's Table 1 coding (from a file already read in 2a);
  - Englert & Bertrams (2c A06);
  - the Inzlicht, Gervais & Berkman comment (LOCATED only; used solely to mark Carter CONTESTED, which weakens a critique-side witness);
  - Rosenthal 1968.
  - Gating was applied to both sides: Carter (critique side) is CONTESTED and ranked third; Englert & Bertrams (support side) is capped out of the top three.
- **Pre-emptions searched first?** Yes. E0 was done before E1, against:
  - the abstract (full);
  - the reference list (METADATA);
  - the secondhand body descriptions (S1, S2, S4, Carter Table 1, CTX-E3, CTX-E46).
  - Sixteen of 21 rows are UNAFFECTED. For post-2016 evidence and non-paper-layer rows this reflects the source's position in time and layer. For IV-1, IV-6, IV-7 and CV-6 it reflects my inability to search the body, not established silence.
- **Did I let a target stand because it supported my expectation?**
  - I re-aimed IV-2, which weakens the prosecution. The basis predates this stage's reading of 00a: 2c F1 had already scored it NARROWS, 2b §8 called the object match partial, and the RRR p.548 declined the protocol.
  - Disclosure: the locked preregistration (00a) was opened during Stage 3 preparation (about 12:26Z, 04:26 PST, just before the Stage 3 start entry in the worklog) to confirm its wording. Its E6 predicted exactly this narrowing ("contested, with the weight of large tests against") and at least one hindsight-driven downgrade. Seeing it may have made the re-aim feel more natural.
  - On hindsight I found only a partial instance: IV-6's relevance depends on a post-2015 effect estimate. I did not force a downgrade to meet E6.
- **What a counter-audit of this counter-audit would flag first:** treating the secondhand mood-check passages (one from the founding cluster's own review) as enough to narrow CV-4, while treating the founding authors' RRR objection as largely answered. Both are founding-cluster statements, gated differently because one has a later direct test (Vohs 2021) and the other does not.
- **Single assumption most likely to be wrong:** that the food-temptation protocol differs enough from the e-crossing and writing manipulations for the large nulls not to count as tests of field 6. If the field treats all sequential-task manipulations as one construct (the target's own unity claim), IV-2 would again approach DEFEATS. The re-aim leans on the paper's protocol specificity, which the paper itself denies.

## K. Final one-paragraph summary

The strongest counter-evidence is the proponent-led, preregistered 36-lab test (Vohs et al. 2021: d = 0.06; figure-tracing persistence 0.15). It survived its reception check, contested only on operationalization, and a founding author co-signed it. With the 2016 RRR (d = 0.04) and Dang 2021 (d = 0.10), it strengthens the audit's central point: field 6's large effect from about 22 students per cell (d ≈ 1.8, or g = 1.31 as Carter codes it) is not credible as an estimate of a reproducible effect, and the general depletion effect is near zero to small.

The counter-audit weakens one part of the audit. 2a's DEFEATS/INVALID for field 6 rests on tests that never re-ran the food-temptation protocol, so it is re-aimed to a major NARROWS. CV-1 and CV-2 are recharacterized (hedged, untested inference). CV-3, CV-4 and F6 are narrowed (behavioural outcomes throughout; mood reportedly checked; stress and control literatures cited).

The thesis survives narrowed, category F (Mixed). The field engaged the opposition — disputed in 2016, partly conceded in 2021 — so there is no suppression; the residual problem is premise use at the citation layer.

The most defensible position: field 6 is a one-lab, non-blind, small-sample result whose size is not reproducible as a general effect. Its specific protocol is untested at scale, and its mechanism and unity claims are unmeasured inferences.
