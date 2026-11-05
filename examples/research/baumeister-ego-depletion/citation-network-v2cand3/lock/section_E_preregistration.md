# SECTION E preregistration (adjacent-field engagement), written and hashed before the queries below were run

Exposure: the target's full text was NOT accessed in this run (no authorized copy); its reference list has not
been inspected (the OpenAlex target record fetched so far carried no referenced_works). The auditor has general
prior knowledge of the ego-depletion literature (declared in 00a). This lock fixes the candidate sources
mechanically so that prior knowledge cannot choose them.

Claim layers L1-L4 and rivals R1-R4 as in lock/ADJUDICATION-1_search_record.md.

Fields, adjudicating observation, and the rival/claim they come from:
- F1 motivation / mental fatigue research (from R2): O1 whether incentives or motivation remove post-effort performance decrements.
- F2 learned helplessness / persistence after uncontrollable failure (from both L1 and R4): O2 whether prior aversive or uncontrollable experience shortens persistence on unsolvable tasks without any self-control demand.
- F3 mood and persistence (from R4): O3 whether induced mood changes persistence on the same kind of outcome task.
- F4 experimenter expectancy effects (from R4): O4 whether non-blind experimenters shift timed behavioural outcomes.
- F5 mental effort / attentional capacity (from L3): O5 whether a limited general capacity is depleted by prior effort.

SOURCE-LOCK METHOD: LOCKED QUERY
SOURCE-LOCK DATABASE: OpenAlex works API (select omits abstract_inverted_index)
SOURCE-LOCK QUERY OR SOURCE LIST: filter=title.search:<terms>,to_publication_date:1998-04-30,type:article,
  sort=cited_by_count:desc, per-page=3; terms: F1 "mental fatigue" ; F2 "learned helplessness" ;
  F3 "mood persistence" ; F4 "experimenter expectancy" ; F5 "mental effort"
SOURCE-LOCK DATE CUTOFF: 1998-04-30 (before the JPSP May 1998 issue)
SOURCE-LOCK RANKING RULE: OpenAlex cited_by_count descending at query time
SOURCE-LOCK N: 15 (top 3 per field x 5 fields)
SOURCE-LOCK DEDUPLICATION RULE: by OpenAlex work ID; off-topic items retained and flagged, never replaced
Engagement is then checked against the target's OpenAlex reference list (METADATA; the target body is not
accessible, so substantive engagement in the text is UNASSESSED) and against named later hub papers where read.
Flip test: F1 is generated from rival R2; F3 and F4 from R4; F2 from both L1 and R4; F5 from L3 (audited claim).
