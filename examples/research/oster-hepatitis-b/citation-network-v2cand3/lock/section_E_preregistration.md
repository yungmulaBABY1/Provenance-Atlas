# SECTION E preregistration (adjacent-field engagement), written and hashed before the queries below were run

Exposure: the auditor read the target's full text and bibliography in Stages 1, 2a and 2b of this run,
so a lock before bibliography inspection is impossible. This lock fixes the candidate sources mechanically
so that the auditor's knowledge of the bibliography cannot choose them.

Claim layers L1-L4 and rivals R1-R4 as in lock/ADJUDICATION-1_search_record.md.

Fields, adjudicating observation, and the rival/claim they come from:
- F1 son preference and sex-selection demography (from R1): O1 parity-specific SRB patterns in China/India.
- F2 hepatitis B and offspring sex (from L1 and R2): O2 individual carrier vs non-carrier offspring sex.
- F3 sex ratio at birth determinants / mortality benchmark (from R4): O3 natural SRB variation with mortality or development.
- F4 missing-women accounting (from L3, both): O4 the size of the female deficit under alternative benchmarks.

SOURCE-LOCK METHOD: LOCKED QUERY
SOURCE-LOCK DATABASE: OpenAlex works API (select omits abstract_inverted_index)
SOURCE-LOCK QUERY OR SOURCE LIST: filter=title.search:<terms>,to_publication_date:2005-06-30,type:article,
  sort=cited_by_count:desc, per-page=3; terms: F1 "son preference" ; F2 "hepatitis B sex ratio" ;
  F3 "sex ratio at birth" ; F4 "missing women"
SOURCE-LOCK DATE CUTOFF: 2005-06-30 (before the JPE issue, Dec 2005)
SOURCE-LOCK RANKING RULE: OpenAlex cited_by_count descending at query time
SOURCE-LOCK N: 12 (top 3 per field x 4 fields)
SOURCE-LOCK DEDUPLICATION RULE: by OpenAlex work ID; off-topic items retained and flagged, never replaced
Engagement is then checked against the target's reference list (JPE version, full text) and text.
Flip test: F1 and F3 are generated from rivals R1 and R4; F2 from both L1 and R2; F4 from L3 (both).
