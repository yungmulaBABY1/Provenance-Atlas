"""Map links: connect an imported audit's findings to a separately produced Stage-1 claim map.

Deterministic and offline. Starts from one committed claim-link bundle (atlas.claims),
re-derives it by content replay, and adds the upstream claim map that bundle could not
see, because the audit output relies on a separate Stage-1 output instead of carrying a
map of its own (ClaimMap ABSENT).

What it records, without judging meaning:

  - the upstream map as written: its table fields, its Field 6 statement, its own
    verification-state column, and its preflight line;
  - where that map came from, as declared: who produced it and that no run prompt or
    run receipt exists for it;
  - whether the audit output itself names the map's path, and whether the map names the
    audit's target work;
  - exact and normalized text comparisons between the audit output's restatement of
    map fields 1, 3 and 6 and the map's own text (the reconciliation the citation-
    network instrument requires, at the level of text only);
  - each finding's target against the map's Field 6, with MAP GAP declarations kept in
    the instrument's two forms.

Two differently worded statements are never treated as the same claim here; that stays
UNRESOLVED_REQUIRES_REVIEW. Quotes inside the map are the producer's transcription and
are not checked against the source, which is not among the committed inputs.

Separate package on purpose: atlas.claims and atlas.extraction receipts pin their own
code, so changing them would break every receipt they have produced.
"""

VERSION = "0.1.0"
SCHEMA = "atlas-maplink/0.1"
CONTEXT_SCHEMA = "atlas-maplink-context/0.1"
