"""Locked literature queries run and recorded by code (atlas.retrieval).

A locked query is a search an audit declares before it looks at results: the
endpoint, the exact parameters and the page policy. This package writes the
search record itself, from events it observes, instead of relying on an
executor's account of what it searched.

It never calls a model, and it never records credentials.
- An OpenAlex API key, if one is supplied, travels only in the Authorization
  header. The record says that a key was used, never which key.
- mailto is not sent. When an executor's log shows one, the record keeps only
  the fact that it was present.

Two modes:
  saved  An executor already ran the query and saved the response. The code
         checks that four things agree: the declared query (a pre-run lock or
         the run output), the request the executor logged, the file the
         executor logged, and the committed file. The retrieval itself remains
         executor-performed, and the record says so.
  live   The code sends the request, retries only on HTTP 429 and 5xx, records
         every attempt (including failures), and computes the digests itself.

The response digest is computed the same way as SEARCH_DIGESTS in Provenance
#14: sha256 of canonical JSON, with every abstract_inverted_index key removed.
Stripping an abstract therefore never changes the digest.

What a record does not establish: that the ranking OpenAlex applied is the
ranking the audit declared, that the results are complete, or that any result
is relevant. Those are questions for the instrument and for review.
"""

VERSION = "0.1.0"
SPEC_SCHEMA = "atlas-retrieval-spec/0.1"
RECORD_SCHEMA = "atlas-retrieval-record/0.1"
SET_SCHEMA = "atlas-retrieval-set/0.1"
DRIFT_SCHEMA = "atlas-retrieval-drift/0.1"
