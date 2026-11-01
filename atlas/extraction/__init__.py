"""Recorded claim extraction (M1 Increment B): import, source anchors, one evidence check.

A claim-extraction run is executed outside this code by a declared runner (a
model in a chat, a person, a later agent) on a fixed packet: the instrument,
a run prompt and a source document, each pinned by hash. This package records
what came back. It never calls a model.

Two stages, because the source is not redistributed:
  local   with the private full output and the source PDF: verifies the PDF
          and its text extraction, matches every quoted anchor against that
          text, and writes the public anchor-verification record and a
          redacted copy of the output (atlas.extraction.local).
  public  from committed files only: parses the redacted output, links it to
          earlier records, runs the declared evidence check, and writes a
          replayable receipt (atlas.extraction.build). CI runs this stage.
"""

VERSION = "0.1.0"
SCHEMA = "atlas-extraction/0.1"
CONTEXT_SCHEMA = "atlas-extraction-context/0.1"
ANCHOR_SCHEMA = "atlas-anchor-verification/0.1"
