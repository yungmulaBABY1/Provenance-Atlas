"""Declared plain-language translations of native labels. Versioned; never inferred.

A label missing from this table is an error, not a pass-through: the view must
not show a native label without saying what it means, or invent a meaning for it.
Every rendering shows the plain text and the native label together.
"""

from ..contract import ContractError

TABLE_ID = "atlas-plain-labels/0.1"

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
}


# Labels whose meaning depends on the field they sit in.
PLAIN_IN_FIELD = {
    ("independence", "NOT_ESTABLISHED"): "Independence: not established",
    ("human_adjudication", "NOT_RECORDED"): "No person has ruled on this",
}


def plain(native: str, field: str | None = None) -> dict:
    if field is not None:
        if (field, native) not in PLAIN_IN_FIELD:
            raise ContractError(f"UNTRANSLATED_LABEL: {field}={native!r} is not in {TABLE_ID}")
        return {"native": f"{field}: {native}", "plain": PLAIN_IN_FIELD[(field, native)], "table": TABLE_ID}
    if native not in PLAIN:
        raise ContractError(f"UNTRANSLATED_LABEL: {native!r} is not in {TABLE_ID}")
    return {"native": native, "plain": PLAIN[native], "table": TABLE_ID}
