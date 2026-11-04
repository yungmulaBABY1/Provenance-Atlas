"""Declared plain-language translations of native labels. Versioned; never inferred.

A label missing from this table is an error, not a pass-through: the view must
not show a native label without saying what it means, or invent a meaning for it.
Every rendering shows the plain text and the native label together.
"""

from ..contract import ContractError

TABLE_ID = "atlas-plain-labels/0.2"
# 0.2 (2026-11-04): adds the labels a research-question page needs (access, record
# state, eligibility, question wording, audit relations). No 0.1 entry changed.

PLAIN = {
    # Quote matching (atlas.extraction.anchors)
    "MATCH": "Found word for word in the paper's text",
    "NORMALIZED_MATCH_ONLY": "Found in the paper's text, differing only in spacing or line breaks",
    "MISMATCH": "Not found exactly in the paper's text",
    # Evidence check (atlas.extraction.stats)
    "CONSISTENT": "The reported numbers agree with each other",
    "INCONSISTENT": "The reported numbers do not agree with each other",
    "PARTIALLY_CHECKABLE": "Only part of this could be checked",
    "NOT_CHECKABLE": "This could not be checked",
    # Evidence reviews (atlas-evidence-review/2)
    "SUPPORTS": "Reviewer: the passage supports this",
    "SUPPORTS_WITH_QUALIFICATION": "Reviewer: the passage supports this, with qualifications",
    "CONTRADICTS": "Reviewer: the passage contradicts this",
    "INSUFFICIENT_EVIDENCE": "Reviewer: not enough evidence to say",
    "PENDING": "Review not finished",
    # Provenance states
    "OPERATOR_STATED": "As stated by the person who ran it; not verified",
    "INSTRUMENT VERSION UNVERIFIED": "The model could not confirm which version of its instructions it had",
    "PROVISIONAL": "Provisional: not enough was available to settle this",
    "FULL-TEXT-CONFIRMED": "The run says it read the full text for this",
    "QUARANTINED": "Kept on record, but its format failed the current checks",
    "UNREVIEWED": "Not reviewed by a person",
    # Claim identity (atlas.claims / atlas.extraction)
    "NOT_THE_SAME_AUDIT_TARGET": "About a different paper, so not the same claim",
    "DIFFERENT_TARGET_WORKS": "Different papers",
    "UNRESOLVED_REQUIRES_REVIEW": "Not decided: needs a person to judge",
    # Links
    "ANCHOR_WITHIN_IMPORTED_PASSAGE": "This quote lies inside the passage the reviewers were given",
    # Source access and what Atlas holds (atlas.sources, atlas.question)
    "AVAILABLE": "A copy was retrieved",
    "RETRIEVAL_FAILED": "No copy could be retrieved",
    "METADATA_ONLY": "Only the title and identifier are on record",
    "RETRIEVED_NO_PASSAGES": "A copy was retrieved, but no passages are on record",
    "PASSAGES_ON_RECORD": "Passages from a retrieved copy are on record",
    # Per-check eligibility (C-03 source-read gate)
    "ELIGIBLE_WITH_LIMITATIONS": "Could be checked, within stated limits",
    "INELIGIBLE_MISSING_EVIDENCE": "Could not be checked: the text it needs is not on record",
    # Research questions (atlas.question)
    "DRAFTED_BY_ASSISTANT": "Wording drafted by Claude, not by the person running the investigation",
    "DECLARED_BY_OPERATOR": "Wording given by the person running the investigation",
    "DECLARED_LIST": "A declared list of sources, not a literature search",
    "TARGET_OF_IMPORTED_AUDIT": "An archived audit imported into Atlas was about this paper",
    "TARGET_OF_EXTRACTION_RUN": "A recorded claim extraction was run on this paper",
    "PASSAGES_CITED_IN_IMPORTED_AUDIT": "Passages from this paper are cited as evidence in an imported audit finding",
    "PASSAGES_REVIEWED": "A model review judged passages from this paper",
    "ARCHIVED_COMPLIANCE_PILOT_OUTPUT": "Output of an archived pilot run, imported as it was",
}


# Labels whose meaning depends on the field they sit in.
PLAIN_IN_FIELD = {
    ("independence", "NOT_ESTABLISHED"): "Independence: not established",
    ("human_adjudication", "NOT_RECORDED"): "No person has ruled on this",
    ("human_review", "NOT_RECORDED"): "No person has reviewed this",
    ("operator_confirmation", "NOT_CONFIRMED"): "Not yet confirmed by the person running the investigation",
    ("operator_confirmation", "CONFIRMED"): "Confirmed by the person running the investigation",
}


def plain(native: str, field: str | None = None) -> dict:
    if field is not None:
        if (field, native) not in PLAIN_IN_FIELD:
            raise ContractError(f"UNTRANSLATED_LABEL: {field}={native!r} is not in {TABLE_ID}")
        return {"native": f"{field}: {native}", "plain": PLAIN_IN_FIELD[(field, native)], "table": TABLE_ID}
    if native not in PLAIN:
        raise ContractError(f"UNTRANSLATED_LABEL: {native!r} is not in {TABLE_ID}")
    return {"native": native, "plain": PLAIN[native], "table": TABLE_ID}
