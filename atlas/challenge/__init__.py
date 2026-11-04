"""Challenges: attributed decisions on the items an imported audit leaves for review.

Deterministic and offline. Starts from one committed import receipt, re-derives it by
content replay, re-runs the vendored checker on the run's own output bytes, and records
each REVIEW_ITEM the checker leaves for human review. Each item carries an explicit
challenge state; NOT_CHALLENGED is a stated state, not a missing one.

A challenge is a JSON artifact written for one item and pinned by hash. It binds to
that item's exact identities: run, output bytes, checker bytes, item number, code and
text. It also records who decided, how they relate to the run, what they saw first,
the outcome from a closed set, their reasons, the evidence they cite and what would
change their mind. A challenge whose target no longer matches is kept and shown,
detached from the item. Nothing replaces the imported run, its checker status or its
findings; challenges are appended alongside them.

Code here never decides an outcome. The producer of the run and the declared author of
this code cannot record one (PRODUCER_CANNOT_CHALLENGE_OWN_RUN,
CODE_AUTHOR_CANNOT_DECIDE). Relations are as declared by the challenger, not verified.
"""

VERSION = "0.1.0"
SCHEMA = "atlas-challenge/0.1"
CONTEXT_SCHEMA = "atlas-challenge-context/0.1"
ARTIFACT_SCHEMA = "atlas-challenge-artifact/0.1"
