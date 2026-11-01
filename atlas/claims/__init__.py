"""Claim links: connect an imported audit's claim map, finding targets and reviews.

Deterministic and offline. Reads one committed import bundle (pinned by hash)
and records, without judging meaning:

  - the claim map the audit output itself contains, as written, with the fields
    it lacks;
  - each statement of a claim (map field, pre-audit restatement, finding
    target) at its exact location in the output;
  - exact and whitespace/NFC-normalized text comparisons between them;
  - which reviews are bound to which part of which finding.

Whether two differently worded statements are the same claim is never decided
here; it is recorded as UNRESOLVED_REQUIRES_REVIEW.

This package lives below atlas/ on purpose. Import receipts pin the hash of
every atlas/*.py module (non-recursive); code here does not alter the import
path and so does not invalidate those receipts. Its own receipts pin its own
code and the shared modules it reads with.
"""

# 0.2.0 / schema 0.2: defective map fields kept but never linked (supersedes the
# unmerged 0.1.0 at bb017ec).
VERSION = "0.2.0"
SCHEMA = "atlas-claimlink/0.2"
CONTEXT_SCHEMA = "atlas-claimlink-context/0.1"
