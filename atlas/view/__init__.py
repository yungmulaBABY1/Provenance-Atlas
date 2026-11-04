"""Evidence view: one reader-facing view model, rendered as a page and as a text report.

Built only from records that re-derive by content replay. Every item in the view
model carries the IDs of the records it comes from. Atlas adds no paraphrase of
content: what the paper says is quoted from public excerpts, what a model wrote is
quoted and attributed, and plain-language wording appears only through the fixed
label table in labels.py, always beside the native label it translates.
"""

VERSION = "0.1.0"
SCHEMA = "atlas-view/0.1"
