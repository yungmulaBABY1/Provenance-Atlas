"""Research questions: one declared question over a declared list of sources.

A ResearchQuestion is the Research counterpart of a Media story family: the unit
that a question-level view is built from. It records what was asked (and who
worded it), which sources are in scope and why, and, for each source, what Atlas
already holds about it: access, recorded passages, checks, audit runs, reviews.

It adds no judgment. No source is given a position on the question, no claims are
merged, and every count is recomputed from the member records with its
denominator. Positions, claim identity and lineage are later, attributed steps.
"""

VERSION = "0.1.0"
SCHEMA = "atlas-question/0.1"
CONTEXT_SCHEMA = "atlas-question-context/0.1"
