# Stage 1 — Claim Extraction / Inflation Map

Target: Baumeister, Roy F., Ellen Bratslavsky, Mark Muraven & Dianne M. Tice. 1998. "Ego depletion: Is the active self a limited resource?" *Journal of Personality and Social Psychology* 74(5): 1252–1265. DOI 10.1037/0022-3514.74.5.1252. PMID 9599441.
Run: Batch 2, audit/baumeister-ego-depletion. Executor: Grok Bot (audit run). Run date 2026-11-05 (box clock UTC; operator TZ America/Los_Angeles, PST = UTC−8).

INSTRUMENT PREFLIGHT: prompts/1-claim-extraction.txt @ commit a58d165d9a986edca220f8143fc0c0d9316c8a13 | blob/hash 894579a79e67508bdc4026b77c0a104681f903ad / sha256 656b11c301931726a5435b231774f40797a10fd0cab950224616fc18951c035f | 1038 lines | 44072 bytes | markers PRESENT ("CLAIM EXTRACTION / INFLATION MAP") | IDENTITY CONFIRMED against operator-pinned immutable commit + blob + sha256 (retrieval form: IMMUTABLE REMOTE, raw.githubusercontent at the pinned commit, HTTP 200; independently cross-checked by `git rev-parse a58d165:prompts/1-claim-extraction.txt` in a separate clone).

REGENERATION NOTICE: the first version of this file was written at 11:18Z (03:18 PST) and lost when the box was restored at about 11:32Z (03:32 PST). This version was rewritten at 11:53Z (03:53 PST; worklog stage1-regen) with the same pinned instrument and the same sources, which were retrieved 11:13–11:18Z and are listed below. No new source about the target was retrieved for it. By then the runner had seen Stage 2c corpus metadata and Semantic Scholar citation contexts; none of them is used below. Disclosed in 00 under Deviations.

## Inputs and access state (RESTRICTED-ACCESS RUN)

- **Target full text: NOT ACCESSED.** No authorized copy was found.
  - The APA PsycNET DOI page and full-text PDF both returned HTTP 403.
  - Unpaywall and OpenAlex report the target closed (`is_oa` false, `oa_status` closed, `any_repository_has_fulltext` false).
  - The first author's publication page and the SUNY Albany repository record (Muraven) carry metadata only, with no file.
  - Copies were excluded as **unauthorized** under the rights rule (course copy, third-party mirror, crawler cache, social repository):
    - a university course-page copy;
    - a third-party mirror site;
    - CiteSeerX / pdfs.semanticscholar.org (crawler cache);
    - a third-party FOIA attachment;
    - ResearchGate.
  - Disclosure: some search snippets from those copies were displayed while retrieval was attempted. No number or wording from them is used here (see 00, Exposure).
- **Abstract:** read via PubMed 9599441. It is not committed; short quotations below are under 25 words.
- **Authorized secondary descriptions of the target's design and results** (each read in full; none is committed):
  - **S1.** Baumeister, LSE public lecture slides "Willpower: self-control, decision fatigue, and energy depletion" (2012; lse.ac.uk, HTTP 200). Gives the Experiment 1 means.
  - **S2.** Schimmack (2016), "The Replicability of Ego-Depletion…", Replicability-Index blog (WebFetch 200). A critic's reading of Experiment 1 procedure, N, t and d.
  - **S3.** APA public page "Is Willpower a Limited Resource?" (apa.org, HTTP 200). A lay restatement.
  - **S4.** Hagger et al. (2016) RRR, PPS 11(4) p.548 (Maastricht University repository, HTTP 200). Describes the original tasks.
- Document type: peer-reviewed journal article (social psychology), four laboratory experiments.
- Downstream uses: none supplied. Field 4 was searched actively.
- The claim that prompted this audit: the operator brief names the paper (Batch 2). No downstream claim was supplied.

Consequence: every statement about the target's body (Ns, statistics, procedures, hedges) is at most secondhand (PROVISIONAL). Statements about the abstract are ABSTRACT-CONFIRMED.

## Publication status

PUBLICATION STATUS: no correction, corrigendum, retraction or expression of concern found.
- Crossref record for 10.1037/0022-3514.74.5.1252: `relation` is empty and `update-to`/`updated-by` are absent. `filter=updates:` returns 0 results (HTTP 200; raw/crossref_target.json, raw/crossref_updates.json).
- The publisher landing page returned HTTP 403.
- Check basis: Crossref only. Critiques and replications belong to Stage 2c and Stage 3, not here.

## Field 1 — Literally measured

From the abstract (ABSTRACT-CONFIRMED) and the secondary descriptions (PROVISIONAL):

1. **Experiment 1 (food temptation → persistence).**
   - Participants were seated before freshly baked chocolate cookies/chocolates and radishes. Each ate radishes (resisting chocolate), ate chocolate, or was in a no-food control.
   - They then worked on unsolvable figure-tracing puzzles. The outcome was the time before quitting (S2).
   - N = 67, about 22 per cell (S2).
   - Mean persistence: radish 8.35 min, chocolate 18.90, no-food 20.86 (S1 slide "Perseverance Despite Frustrating Failure").
   - Radish vs chocolate t(44) = 6.03, d = 1.80; radish vs no-food t(44) = 6.88, d = 2.04 (S2, computed by the critic from reported statistics).
2. **Experiment 2 (choice → persistence).** A meaningful personal choice to perform attitude-relevant behaviour (a counter-attitudinal speech) caused "a similar decrement in persistence" (abstract). N and statistics were not retrieved.
3. **Experiment 3 (emotion suppression → anagrams).** Suppressing emotion during a film led to a drop in performance on solvable anagrams (abstract; S4 p.548 names unsolvable-anagram persistence as a Study 3 measure). N and statistics were not retrieved.
4. **Experiment 4 (habit-breaking → passivity).** An initial letter-crossing task requiring high self-regulation (S4 p.548: the letter "e" task, Study 4) made people more prone to favour the passive-response option (abstract). N and statistics were not retrieved.

What is literally measured: between-condition differences in behaviour (persistence time, anagram performance, choice of a passive option) after different first tasks, in small single-lab samples of undergraduates. The "inner resource" is not measured. It is inferred from the common direction of the four contrasts.

### Definition–operationalization check
- Named central construct: a "common inner resource" for volition, i.e. the self's "capacity for active volition" (abstract).
- Operationalization (ITEMS-INFERRED: abstract plus S1/S2/S4 descriptions; Method not read): quitting time on unsolvable puzzles (Exp 1–2), anagram performance (Exp 3), and passive-option choice (Exp 4).
- Scope result: UNKNOWN. A resource-level construct is inferred from task-level behaviour; no independent resource marker was found. MAP CONTENT, not a verdict.

### Construct-establishment check (triggered: mechanism escalation, from behaviour to "common inner resource")
- PREVALENCE: not applicable.
- FORM (acts of volition deplete a limited resource): UNKNOWN. The introduction and the cited establishing work were not fetched. The abstract asserts the mechanism.
- DOMAIN (which acts share the resource): UNKNOWN. The abstract asserts unity across "seemingly different, unrelated acts".
- WRONGNESS: not applicable (no belief is graded).
- HARM: not applicable (no harm claim).

## Field 2 — Source's strongest claim (hedges preserved)

- Abstract opening: choice, active response, self-regulation and other volition "may all draw on a common inner resource" (hedged: "may").
- Abstract conclusion: the results "suggest that the self's capacity for active volition is limited and that a range of seemingly different, unrelated acts share a common resource."
- Title: "Is the active self a limited resource?" (posed as a question).
- Body-level hedges: UNKNOWN (body not read). S2 quotes a passage reporting an independent science-fair replication. Per S2, the passage says it "strengthen[s] confidence in the present findings" (secondhand).
- Hedge pattern: the opening "may" becomes "suggest … is limited" plus "share a common resource". The second hedge is weaker than the first, and the unity claim is stated without qualification inside the "suggest" clause.

## Field 3 — Weaker defensible claim (author reconstruction from Field 1)

In one laboratory, with about 22 undergraduates per cell and an experimenter-delivered food manipulation, participants who had eaten radishes while resisting chocolate quit unsolvable figure-tracing puzzles sooner (about 8 vs about 19–21 min) than chocolate or no-food controls. Three further small experiments with different first tasks and outcomes showed same-direction decrements.

The pattern is consistent with a shared limited capacity. It is equally consistent, at this evidential level, with motivational, affective, expectancy or task-specific accounts. The resource itself was not measured.

## Field 4 — Downstream claim (searched)

Searches this stage: web search for author, press and lay restatements. Retrieved pages are logged with HTTP status (logs/retrieval_log.jsonl, stage "stage1").

| ID | Layer | Provenance | Quoted restatement (<25 words) | Locator |
|---|---|---|---|---|
| D1 | PR / media (author's public lecture) | RETRIEVED | "Willpower is limited" … "'Ego depletion' effects"; then the radish 8.35 / chocolate 18.90 / no-food 20.86 slide | S1 slides 2012, slides "Willpower is limited" and "Perseverance Despite Frustrating Failure" |
| D1b | PR / media (author's public lecture) | RETRIEVED | "Like a Muscle • Gets tired after exertion • Conserving energy • Exercise increases strength !"; "One Willpower, not Many" | S1, consecutive slides |
| D2 | PR / media (professional association lay page) | RETRIEVED | "Drawing on willpower to resist the cookies, it seemed, drained the subjects' self-control for subsequent situations." | S3, APA "Is Willpower a Limited Resource?", para 2 |
| D2b | PR / media | RETRIEVED | "Since that work was published in 1998, numerous studies have built a case for willpower depletion" | S3, para 3 |
| D3 | citing literature (replication) | RETRIEVED | the original tests "required participants to taste radishes and resist cookies (Baumeister et al., 1998, Study 1)" | S4, RRR p.548 |

- RECALLED: popular-book restatements (e.g. *Willpower*, 2011) are believed to exist. They were not retrieved this run and do not anchor anything.
- Scope note: no exhaustive enumeration of press coverage was attempted.

Attribution and scope arithmetic:
- **D1 / D1b.** The author's lecture drops the abstract's "may" and "suggest". It states "Willpower is limited" as a heading, and adds muscle-training ("Exercise increases strength") and unity ("One Willpower, not Many") claims that the abstract does not contain. The Exp 1 means match S2's reading.
- **D2.** Says participants had "30 minutes to complete a difficult geometric puzzle" and gave up after "about 8 minutes" vs "nearly 19 minutes". This drops "unsolvable" (S2), and "drained … self-control" is stated as the mechanism, softened only by "it seemed".
- **D3.** Faithful description of the task.

## Field 5A — Within-source inflation point + failure location

Candidate within-source transitions (MAP CONTENT, not verdicts):

1. **Behaviour → mechanism.** The abstract moves from four behavioural contrasts to "the self's capacity for active volition is limited" and "share a common resource". No resource was measured. The step from four same-direction contrasts to one shared resource is inferential.
2. **Hedge drift.** "May all draw on" (opening) becomes "suggest … is limited … share a common resource" (closing). The unity claim strengthens across the abstract.
3. **Construct unity.** "Seemingly different, unrelated acts" share a resource. The evidence is four different manipulations, each paired with a different outcome. No experiment crossed manipulations with outcomes to show shared variance.

Failure location: PAPER. Basis: ABSTRACT-CONFIRMED (assertion level only). Body-level hedges and analyses are UNKNOWN.

## Field 5B — Downstream inflation point + failure location

PR / MEDIA, anchored on D1/D1b (author lecture) and D2 (APA lay page). Both are RETRIEVED and ANCHOR-ELIGIBLE.
- The moves:
  - hedged "suggest" becomes "Willpower is limited";
  - "like a muscle", trainability and "One Willpower, not Many" are added;
  - the unsolvable-puzzle detail is lost, and "drained … self-control" is stated as the mechanism.
- Verification: D1, D2 RETRIEVED. The target is compared at abstract level only.

Citing-literature layer: no inflation found in D3.

### Anchoring table

| Item | Provenance state | Quotation present? | Locator present? | Attribution cross-source-confirmed, if applicable? | Anchor eligibility |
|---|---|---|---|---|---|
| D1 LSE slides 2012 | RETRIEVED | yes | yes | N/A (not classified MISATTRIBUTED) | ELIGIBLE |
| D1b LSE slides 2012 | RETRIEVED | yes | yes | N/A | ELIGIBLE |
| D2 APA lay page | RETRIEVED | yes | yes | N/A | ELIGIBLE |
| D2b APA lay page | RETRIEVED | yes | yes | N/A | ELIGIBLE |
| D3 Hagger et al. 2016 p.548 | RETRIEVED | yes | yes | N/A | ELIGIBLE (no inflation found) |
| *Willpower* (2011) book | RECALLED | no | no | N/A | NOT ELIGIBLE — recalled only |

## Claim inventory

| Claim | Quantified? | Why it might be inflated | Selected for Field 6? |
|---|---|---|---|
| C1 Exp 1: radish/resist-chocolate participants persisted about 8.35 min vs 18.90 (chocolate) and 20.86 (no food) on unsolvable puzzles; d ≈ 1.8–2.0 | yes | ~22 per cell; implausibly large d; experimenter-delivered manipulation; single lab | **YES** |
| C2 Exp 2: a meaningful choice reduces subsequent persistence | yes (not retrieved) | small N; choice manipulation confounded with dissonance | deferred |
| C3 Exp 3: emotion suppression reduces anagram performance | yes (not retrieved) | small N; affect confound | deferred |
| C4 Exp 4: a self-regulation task increases passivity | yes (not retrieved) | outcome is a new construct (passivity) | deferred |
| C5 The four acts share a common inner resource | no | inferred from direction alone; no crossed design | deferred (feeds L3) |
| C6 The self's capacity for active volition is limited | no | mechanism escalation from behaviour | deferred (feeds L3) |

Field 6 selection reason:
- C1 is the only quantified central result available at a verifiable level (Rule 2). It is the paradigm's canonical demonstration (D1, D2, D3 all restate it).
- C5/C6 are interpretive escalations from C1–C4.

## CLAIM LAYERS AND RIVALS (codes reused verbatim by Stage 2c)

Claim layers:

- **L1 — Original depletion effect (map field 6).** Resisting chocolate and eating radishes causes much faster quitting on unsolvable puzzles (about 8 vs about 19–21 min; d about 1.8–2.0), replicable in that paradigm.
- **L2 — General sequential-task effect.** Across varied first and outcome tasks, an initial act of self-control reliably reduces subsequent self-control (nonzero, at least small-to-moderate).
- **L3 — Mechanism.** Self-control draws on a limited common resource (later specified as glucose).
- **L4 — Interpretive/applied.** Willpower works "like a muscle"; decision fatigue and everyday self-control failures follow from depletion.

Strongest rivals:

- **R1 — Null or inflated effect.** Small samples and selective publication.
- **R2 — Motivation/attention shift.** The process model and opportunity-cost accounts; no resource is consumed.
- **R3 — Beliefs/expectancy.** Lay theories of willpower; demand.
- **R4 — Task-specific confounds.** Affect, frustration, hunger, non-blind experimenter delivery.

## Required output table

| Field | Content | Verification state |
|---|---|---|
| 1. Literally measured | Between-condition behavioural differences after different first tasks: Exp 1 persistence on unsolvable figure-tracing (radish 8.35, chocolate 18.90, no-food 20.86 min; N = 67); Exp 2 persistence after choice; Exp 3 anagram performance after emotion suppression; Exp 4 passive-option choice after letter-crossing | ABSTRACT-CONFIRMED (designs); PROVISIONAL (numbers via S1/S2) |
| 2. Source's strongest claim | "suggest that the self's capacity for active volition is limited and that a range of seemingly different, unrelated acts share a common resource" (abstract) | ABSTRACT-CONFIRMED |
| 3. Weaker defensible claim | In one lab, ~22 per cell, radish-eaters quit unsolvable puzzles sooner; three further small same-direction contrasts; consistent with but not specific to a shared resource | author reconstruction from Field 1 |
| 4. Downstream claim | D1/D1b author lecture: "Willpower is limited", "Like a Muscle", "One Willpower, not Many"; D2 APA: "drained the subjects' self-control"; D3 RRR faithful | RETRIEVED (D1–D3); target abstract-level only |
| 5A. Within-source inflation point + failure location | Behaviour → resource mechanism; "may" → "suggest … share"; unity across four unrelated paradigms asserted → PAPER | ABSTRACT-CONFIRMED (body UNKNOWN) |
| 5B. Downstream inflation point + failure location | Hedge removal and added muscle/trainability/unity claims; "unsolvable" dropped → PR / MEDIA | RETRIEVED (D1, D2) |
| 6. Claim under audit | In Experiment 1, participants who ate radishes while resisting chocolate persisted about 8.35 min on unsolvable puzzles vs 18.90 (chocolate) and 20.86 (no food); N ≈ 67; t(44) = 6.03 (d ≈ 1.8) radish vs chocolate. | PROVISIONAL (secondhand: S1 means; S2 N/t/d) |

## Required construct-side handoff sub-schema

| Check | Object | Retrieval status / basis | Result | Verification state | Evidence |
|---|---|---|---|---|---|
| Construct establishment | PREVALENCE | not applicable | — | — | — |
| Construct establishment | FORM | UNKNOWN (introduction and cited establishing work not fetched; abstract-only target) | resource mechanism asserted in abstract; establishment not checkable | ABSTRACT-CONFIRMED (assertion only) | abstract |
| Construct establishment | DOMAIN | UNKNOWN (same reason) | unity across "seemingly different, unrelated acts" asserted | ABSTRACT-CONFIRMED (assertion only) | abstract |
| Construct establishment | WRONGNESS | not applicable (no belief graded) | — | — | — |
| Construct establishment | HARM | not applicable (no harm claim) | — | — | — |
| Definition-operationalization | "capacity for active volition" / "common inner resource" ↔ quitting time, anagram score, passive choice | ITEMS-INFERRED (abstract + S1/S2/S4 descriptions; Method not read) | UNKNOWN | PROVISIONAL | abstract; S1; S2; S4 p.548 |
| Grade-before-assert | none triggered (no belief graded as wrong or pathologized) | — | — | — | P2 strength gate: VOID (no belief graded) |

- CLAIM UNDER AUDIT: In Experiment 1, radish/resist-chocolate participants persisted about 8.35 min on unsolvable tracing puzzles vs 18.90 (chocolate) and 20.86 (no food); N ≈ 67; t(44) = 6.03.
- WITHIN-SOURCE FAILURE LOCATION: paper — ABSTRACT-CONFIRMED (behaviour → mechanism; hedge drift; construct unity). Body-level UNKNOWN.
- DOWNSTREAM FAILURE LOCATION: PR-media — RETRIEVED, ANCHOR-ELIGIBLE (author LSE lecture 2012; APA lay page). Target compared at abstract level only.
- GAP TYPE: both.
- MAP CONFIDENCE: low. Raising it requires an authorized copy of the full text (APA closed; no repository copy), which would confirm Ns, test statistics, exclusions, the Method of Exp 2–4, and body-level hedges.

Unselected claims C2–C6 are DEFERRED, not dismissed.
