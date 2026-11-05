# ADJUDICATION-1 search record (written and hashed before any search result was retrieved or screened)

Run: Batch 1, Oster (2005) "Hepatitis B and the Case of the Missing Women", JPE 113(6), doi:10.1086/498588,
OpenAlex W3123222584. Instrument: 2-citation-network v2-candidate.3. Author: Grok Bot (executor).
Written: see lock/ADJUDICATION-1_lock.txt (UTC timestamp and sha256 of this file).

## Claim layers and rivals (copied from Stage 1, out/01_claim_extraction.md)
- L1 Individual carrier effect: offspring sex ratio of HBV carriers about 1.5 (1.54, CI 1.29-1.87).
- L2 Population transmission: HBV prevalence raises the population sex ratio at birth.
- L3 Accounting share (map field 6): HBV accounts for 47.24% of Coale's 60.26M missing women.
- L4 Interpretive: the imbalance is less attributable to discrimination; the remaining problem is concentrated in India and Pakistan.
- R1 Son preference / sex-selective behaviour (parity-specific).
- R2 Null or small individual carrier effect in large samples.
- R3 Ecological confounding of the HBV-SRB association.
- R4 Benchmark misspecification (expected SRB varies with life expectancy / mortality).

## Purpose
Find studies that test any claim layer or rival, whether or not they cite the target:
(a) individual-level tests of parental HBV carrier status on offspring sex (L1 vs R2);
(b) work on HBV and missing women / population sex ratios (L2, L3, L4);
(c) parity-specific son-preference evidence on sex ratios at birth in China / India (R1);
(d) work on the expected/natural sex ratio at birth and its determinants, including mortality or life expectancy, as a benchmark for missing women (R4);
(e) HBV vaccination and sex ratio (L2 vs R3).

## Database and access
OpenAlex works API (https://api.openalex.org/works), one request per query, executed once.
select=id,doi,display_name,publication_year,type,cited_by_count,authorships,primary_location,referenced_works
(abstract_inverted_index is NOT requested; any abstract field is nulled before the file is written).
Searching uses OpenAlex's title_and_abstract.search filter server-side; no abstract text is retrieved.

## Common bounds (every query)
- filter: from_publication_date:1980-01-01, to_publication_date:2026-11-05
- filter: type:article|preprint|book-chapter
- ranking: OpenAlex relevance_score descending (default for a search filter); per-page=10, page 1 only (N = 10 per query)

## Exact queries (title_and_abstract.search, OpenAlex boolean syntax)
- Q1 (a): "hepatitis B" AND ("sex ratio" OR "offspring sex" OR "sex of offspring" OR "sex of the offspring")
- Q2 (b): "missing women" AND ("hepatitis" OR "sex ratio at birth")
- Q3 (c): ("sex ratio at birth" OR "son preference") AND ("birth order" OR parity) AND (China OR India)
- Q4 (d): ("sex ratio at birth" OR "missing women") AND ("life expectancy" OR "natural sex ratio" OR "biological")
- Q5 (e): "hepatitis B" AND (vaccination OR vaccine OR immunization) AND ("sex ratio" OR "male births" OR "proportion male")

## Deduplication
By OpenAlex work ID. A work returned by several queries is one member listing every query that returned it.
Distinct OpenAlex records of the same work (e.g. a working paper and its published version) are one ledger row
listing every record ID (instrument Gate A rule).

## Screening rule (applied to every member)
Screening uses the OpenAlex title and metadata and, where already retrieved this run from an authorized source,
the full text. Abstracts are NOT used (rights rule of the brief).
- DIRECT (L1) / DIRECT (R2): tests parental HBV carrier status against offspring sex at the individual level.
- DIRECT (L2) / DIRECT (R3): tests HBV prevalence or vaccination against population sex ratios.
- DIRECT (L3) / DIRECT (L4): re-computes or disputes the HBV share of missing women.
- DIRECT (R1): tests parity-specific sex selection / son preference as the source of high SRB in China or India.
- DIRECT (R4): estimates the expected SRB or its determinants for the missing-women benchmark.
- ADJACENT: addresses the subject or mechanism without such a test.
- BACKGROUND: uses HBV or sex ratios for another question.
- UNRELATED: not about the subject.
- UNKNOWN: title and metadata insufficient and no full text retrieved. No guessing.

## Known items listed BEFORE the search (from 00a_preregistration_LOCKED.txt only)
- K1 Das Gupta 2005, Population and Development Review 31(3)
- K2 Lin & Luoh 2008, AER 98(5)
- K3 Oster, Chen, Yu & Lin 2010, Economics Letters 107(2)
- K4 Oster reply (uncertain; possibly Demography 2009)
- K5 Das Gupta 2006, Population and Development Review 32(2)
- K6 Klasen 2008 (uncertain)
- K7 Anderson & Ray 2010, Review of Economic Studies (adjacent)
- K8 Blumberg et al. / Chahnazarian 1988
Known-item recall will be reported against this list only. Known items the search misses enter only as POST HOC.

## Inclusion for analysis
Every deduplicated result is a member of ADJUDICATION-1 with one ledger row, whatever its screening code.
Only DIRECT members may enter decisive-test or absence inferences. Absence statements are bounded by this
search and stated as screened/total.

## Post hoc rule
Any source located after this lock enters only as POST HOC, named as such in Supported inference.
