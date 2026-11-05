# ADJUDICATION-1 search record (written and hashed before any result was retrieved or screened)

Run: diagnostic live run of 2-citation-network v2-candidate.2 on AJR (2001). Author: Grok Bot (executor).
Written: see lock/ADJUDICATION-1_lock.txt (UTC timestamp and sha256 of this file).

## Purpose
Find studies that test the claim layers or their strongest rivals, whether or not they cite AJR 2001:
- (a) direct tests or re-analyses of the field-6 estimate (Table 4 col. 1, 2SLS 0.94, SE 0.16; settler-mortality instrument);
- (b) tests of L3 ("institutions explain cross-country income differences") against R1 (direct geography or disease channel) and R2 (human capital carried by settlers);
- (c) cross-country estimates of the effect of institutions on income that do not use the settler-mortality instrument.

## Database and access
OpenAlex works API (https://api.openalex.org/works), one request per query, executed once.
Fields returned: id, doi, display_name, publication_year, type, cited_by_count, authorships, primary_location, abstract_inverted_index, referenced_works.

## Common bounds (every query)
- filter: from_publication_date:2001-01-01, to_publication_date:2026-11-04
- filter: type:article|preprint
- ranking: OpenAlex relevance_score descending (default ordering for a search filter); per-page=10, page 1 only (N = 10 per query)
- the search filter is title_and_abstract.search with the boolean expression below (OpenAlex boolean syntax)

## Exact queries
- Q1 (a): "settler mortality" AND (replication OR reanalysis OR revisited OR robustness OR comment OR reply)
- Q2 (b, R1): "settler mortality" AND (malaria OR geography OR disease OR tropics)
- Q3 (b, R2): ("settler mortality" OR "colonial origins") AND ("human capital" OR education OR schooling)
- Q4 (b, R1/R2 vs institutions, any instrument): institutions AND geography AND ("deep determinants" OR "fundamental causes" OR primacy OR "institutions rule")
- Q5 (c): institutions AND ("income per capita" OR "economic development") AND ("instrumental variable" OR "instrumental variables" OR "natural experiment") NOT "settler mortality"
- Q6 (c): ("institutional quality" OR "rule of law" OR "property rights") AND ("cross-country" OR "cross-national") AND (income OR growth) AND (causal OR instrument OR identification) NOT "settler mortality"

## Deduplication
By OpenAlex work ID. A work returned by several queries is one member and lists every query that returned it.

## Screening rule (applied to every member, from the OpenAlex title and reconstructed abstract only)
- DIRECT (L1/field 6): re-estimates, replicates, re-analyses or critiques the settler-mortality IV estimate itself.
- DIRECT (L3-R1): tests institutions against a direct geography or disease channel for cross-country income.
- DIRECT (L3-R2): tests institutions against human capital as the channel for cross-country income.
- DIRECT (L3-noSM): estimates the effect of institutions on income across countries with identification other than settler mortality.
- ADJACENT: addresses the subject or mechanism (institutions, geography, disease, human capital and development) without such a test (reviews, theory, single-country or sub-national studies, other outcomes).
- BACKGROUND: uses institutions or AJR for another question.
- UNRELATED: not about the subject.
- UNKNOWN: title and abstract absent or insufficient to apply the rule. No guessing.

## Inclusion criteria for analysis
Every deduplicated result is a member of ADJUDICATION-1 and gets one ledger row, whatever its screening code. Only DIRECT members may enter decisive-test or absence inferences. Absence statements are bounded by this search and stated as screened/total.

## Post hoc rule
Any source found after this lock (for example from reading a member) enters only as POST HOC, named as such in Supported inference.
