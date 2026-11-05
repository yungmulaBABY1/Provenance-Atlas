# ADJUDICATION-1 search record (written and hashed before any search result was retrieved or screened)

Run: Batch 2, Baumeister, Bratslavsky, Muraven & Tice (1998) "Ego depletion: Is the active self a limited resource?",
JPSP 74(5):1252-1265, doi:10.1037/0022-3514.74.5.1252, OpenAlex W2123817056.
Instrument: 2-citation-network v2-candidate.3. Author: Grok Bot (executor).
Written: see lock/ADJUDICATION-1_lock.txt (UTC timestamp and sha256 of this file).

## Claim layers and rivals (copied from Stage 1, out/01_claim_extraction.md)
- L1 Original depletion effect (map field 6): resisting chocolate / eating radishes causes much faster quitting on unsolvable puzzles (about 8 vs about 19-21 min; d about 1.8-2.0), replicable in that paradigm.
- L2 General sequential-task effect: across varied first and outcome tasks, an initial act of self-control reliably reduces subsequent self-control (nonzero, at least small-to-moderate).
- L3 Mechanism: self-control draws on a limited common resource (later specified as glucose).
- L4 Interpretive/applied: willpower works "like a muscle"; decision fatigue and everyday self-control failures follow from depletion.
- R1 Null or inflated effect (small samples, selective publication).
- R2 Motivation/attention shift (process model; opportunity cost), no resource consumed.
- R3 Beliefs/expectancy (lay theories of willpower; demand).
- R4 Task-specific confounds (affect, frustration, hunger, non-blind experimenter delivery).

## Purpose
Find studies that test any claim layer or rival, whether or not they cite the target:
(a) replications of the sequential-task effect, especially preregistered / multi-site (L1, L2 vs R1);
(b) meta-analyses and bias-corrected estimates (L2 vs R1);
(c) glucose tests of the resource mechanism (L3);
(d) motivation / process-model / opportunity-cost tests (R2);
(e) implicit theories / beliefs about willpower (R3);
(f) affect, fatigue, frustration or manipulation-check tests in depletion paradigms (R4);
(g) decision-fatigue or strength-model applied tests (L4).

## Database and access
OpenAlex works API (https://api.openalex.org/works), one request per query, executed once (retries only on 429/5xx).
select=id,doi,display_name,publication_year,type,cited_by_count,authorships,primary_location,referenced_works
(abstract_inverted_index is NOT requested; any abstract field is nulled before the file is written).
Searching uses OpenAlex's title_and_abstract.search filter server-side; no abstract text is retrieved.

## Common bounds (every query)
- filter: from_publication_date:1998-01-01, to_publication_date:2026-11-05
- filter: type:article|preprint|book-chapter|review
- ranking: OpenAlex relevance_score descending (default for a search filter); per-page=10, page 1 only (N = 10 per query)

## Exact queries (title_and_abstract.search, OpenAlex boolean syntax)
- Q1 (a): "ego depletion" AND (replication OR "registered replication" OR "multilab" OR "multi-site" OR preregistered)
- Q2 (b): "ego depletion" AND ("meta-analysis" OR "publication bias" OR "small-study")
- Q3 (c): ("ego depletion" OR "self-control") AND glucose
- Q4 (d): "ego depletion" AND (motivation OR "process model" OR "opportunity cost")
- Q5 (e): ("ego depletion" OR willpower) AND ("implicit theories" OR "lay theories" OR beliefs)
- Q6 (f): "ego depletion" AND (fatigue OR frustration OR mood OR "manipulation check")
- Q7 (g): ("decision fatigue" OR "strength model of self-control" OR "self-control strength")

## Deduplication
By OpenAlex work ID. A work returned by several queries is one member listing every query that returned it.
Distinct OpenAlex records of the same work (e.g. a preprint and its published version, or an erratum record
of the same article) are one ledger row listing every record ID (instrument Gate A rule).
The target itself, if returned, is recorded in one row (T01) and coded BACKGROUND (target).

## Screening rule (applied to every member)
Screening uses the OpenAlex title and record metadata and, where already retrieved this run from an authorized
source, the full text. Abstracts are NOT used (rights rule of the brief).
- DIRECT (L1): tests the food-temptation -> persistence effect itself.
- DIRECT (L2) / DIRECT (R1): replication, multi-site test or bias-corrected meta-analysis of the sequential-task effect.
- DIRECT (L3): tests glucose (consumption, rinse, levels) as the resource.
- DIRECT (R2): tests motivation / incentive / process-model accounts against resource depletion.
- DIRECT (R3): tests willpower beliefs or expectancy as a moderator / cause.
- DIRECT (R4): tests affect, fatigue or frustration as the cause of the decrement.
- DIRECT (L4): tests decision fatigue or applied depletion in the field.
- ADJACENT: addresses ego depletion / self-control mechanisms without such a test (reviews, theory, trait self-control).
- BACKGROUND: uses depletion or self-control for another question.
- UNRELATED: not about the subject.
- UNKNOWN: title and metadata insufficient and no full text retrieved. No guessing.

## Known items listed BEFORE the search (from 00a_preregistration_LOCKED.txt only)
- K1 Hagger, Wood, Stiff & Chatzisarantis 2010, Psychological Bulletin (meta-analysis)
- K2 Carter & McCullough 2014, Frontiers in Psychology (publication-bias analysis)
- K3 Carter, Kofler, Forster & McCullough 2015, JEP: General (meta-analysis)
- K4 Hagger, Chatzisarantis et al. 2016, Perspectives on Psychological Science (RRR)
- K5 Vohs, Schmeichel et al. 2021, Psychological Science (paradigmatic multi-site)
- K6 Dang et al. 2021, Social Psychological and Personality Science (multi-site)
- K7 Dang 2018, Psychonomic Bulletin & Review (meta-analysis)
- K8 Gailliot et al. 2007, JPSP (glucose)
- K9 Job, Dweck & Walton 2010, Psychological Science (willpower beliefs)
- K10 Inzlicht & Schmeichel 2012, Perspectives on Psychological Science (process model)
- K11 Baumeister & Vohs 2016, Perspectives on Psychological Science (reply to RRR)
- K12 Kurzban 2010 (glucose critique), Evolutionary Psychology
Known-item recall will be reported against this list only. Known items the search misses enter only as POST HOC.

## Inclusion for analysis
Every deduplicated result is a member of ADJUDICATION-1 with one ledger row, whatever its screening code.
Only DIRECT members may enter decisive-test or absence inferences. Absence statements are bounded by this
search and stated as screened/total.

## Post hoc rule
Any source located after this lock enters only as POST HOC, named as such in Supported inference.
