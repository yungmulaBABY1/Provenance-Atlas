"""Declared plain-language translations of native labels. Versioned; never inferred.

A label missing from this table is an error, not a pass-through: the view must
not show a native label without saying what it means, or invent a meaning for it.
Every rendering shows the plain text and the native label together.
"""

from ..contract import ContractError

TABLE_ID = "atlas-plain-labels/0.3"
# 0.2 (2026-11-04): adds the labels a research-question page needs (access, record
# state, eligibility, question wording, audit relations). No 0.1 entry changed.
# 0.3 (2026-11-04): adds the labels a paper page for an imported citation-network audit
# needs: read state, the instrument's own finding labels (meanings from
# prompts/research-analysis/2-citation-network.txt), map links (atlas.maplink) and
# challenges (atlas.challenge). No 0.2 entry changed.

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
    # 0.3: imported runs and their sources (atlas.adapter, atlas.sources)
    "PARTIAL_READ": "Text was read, but not every requested part, or with a warning",
    "SELF_REPORTED_NOT_INDEPENDENTLY_VERIFIED": "As the run reports it; not independently verified",
    "PASS-WITH-REVIEW": "Passes the instrument's mechanical checks; some judgments are left for review",
    "IMPORTED_UNADJUDICATED": "Imported as the run wrote it; no one has ruled on it",
    # 0.3: the citation-network instrument's own finding labels
    "SURVIVES": "The run's concede test: the audited claim still stands",
    "NARROWS": "The run's concede test: the claim stands only in a narrower scope",
    "DEFEATS": "The run's concede test: the audited claim does not follow",
    "RECEPTION-CONFIRMED": "The run says it checked replies, replications or citation records against retrieved sources",
    "CROSS-SOURCE-CONFIRMED": "The run says it read both the citing text and the cited source and compared them",
    "CONTESTED": "The run says credible disagreement exists and who is right is unresolved",
    "PAPER": "Where the run locates the failure: the paper itself",
    "CITATION": "Where the run locates the failure: later literature",
    "PR-MEDIA": "Where the run locates the failure: communications or coverage",
    "MODEL-RETRIEVAL": "Where the run locates the failure: summarizers or search systems",
    "MIXED": "Where the run locates the failure: more than one layer",
    # 0.3: findings against a separately produced claim map (atlas.maplink)
    "DECLARED_NOT_FIELD_6": "The finding says it targets something other than the claim under audit",
    "DECLARED_NOT_ON_MAP": "The finding says its target is not on the claim map",
    "DECLARED_BY_REFERENCE": "The finding points to the claim under audit by reference",
    "SAME_TEXT": "Worded exactly like the claim under audit",
    "SAME_TEXT_AFTER_NORMALIZATION": "Worded like the claim under audit, apart from spacing",
    "NO_TARGET_STATED": "The finding states no target",
    "WORDING_DIFFERS_FROM_INSTRUMENT_FORMS": "Its map-gap note is worded unlike both forms the instrument defines",
    "UPSTREAM_STAGE_1_OUTPUT": "A separate claim-extraction output, not part of this audit run",
    "PATH_NAMED_IN_AUDIT_OUTPUT": "The audit output names this file as its claim map",
    "NOT_NAMED_LINK_DECLARED_IN_CONTEXT_ONLY": "The audit output does not name this file; the link is only declared",
    "MAP_PRODUCER_RESTATEMENT_ONLY": "Only the map's statement of the paper's claim is on record, not the paper's words",
    # 0.3: challenges on review items (atlas.challenge)
    "CHALLENGED": "At least one reviewer has recorded a decision on this item",
    "NOT_CHALLENGED": "No reviewer has recorded a decision on this item",
    "CONDITION_MET": "Reviewer: what the item asks to verify holds",
    "CONDITION_MET_WITH_QUALIFICATION": "Reviewer: it holds, within limits the reviewer states",
    "CONDITION_NOT_MET": "Reviewer: it does not hold",
    "CANNOT_DETERMINE": "Reviewer: the available material does not settle it",
    "MODEL_AGENT": "Decided by a model, not a person",
    "PERSON": "Decided by a person",
    "TEXT_FIELDS_FOUND_VERBATIM_IN_SOURCE": "Transcribed: every text field is found word for word in the reviewer's answer",
    "NOT_A_TRANSCRIPTION": "Written as a record directly, not transcribed",
}


# Labels whose meaning depends on the field they sit in.
PLAIN_IN_FIELD = {
    ("independence", "NOT_ESTABLISHED"): "Independence: not established",
    ("human_adjudication", "NOT_RECORDED"): "No person has ruled on this",
    ("human_review", "NOT_RECORDED"): "No person has reviewed this",
    ("operator_confirmation", "NOT_CONFIRMED"): "Not yet confirmed by the person running the investigation",
    ("operator_confirmation", "CONFIRMED"): "Confirmed by the person running the investigation",
    # 0.3
    ("run_prompt", "NOT_RECORDED"): "No run prompt was recorded",
    ("run_receipt", "NONE"): "No run receipt exists",
    ("text_comparison", "MATCH"): "Same wording, character for character",
    ("text_comparison", "NORMALIZED_MATCH_ONLY"): "Same wording, apart from spacing or line breaks",
    ("text_comparison", "MISMATCH"): "Worded differently",
    ("status", "confirmed"): "The run marks this finding confirmed",
    ("status", "contested"): "The run marks this finding contested",
    ("status", "provisional"): "The run marks this finding provisional",
    ("severity", "none"): "The run rates its severity: none",
    ("severity", "minor"): "The run rates its severity: minor",
    ("severity", "moderate"): "The run rates its severity: moderate",
    ("severity", "major"): "The run rates its severity: major",
    ("severity", "fatal-for-strong-claim"): "The run rates its severity: fatal for the strong claim",
    ("producer", "NO"): "Declares it is not the run's producer",
    ("producer", "UNKNOWN"): "Its relation to the run's producer is unknown",
    ("atlas_code_author", "NO"): "Declares it is not the author of this code",
    ("atlas_code_author", "UNKNOWN"): "Its relation to the author of this code is unknown",
}


def plain(native: str, field: str | None = None) -> dict:
    if field is not None:
        if (field, native) not in PLAIN_IN_FIELD:
            raise ContractError(f"UNTRANSLATED_LABEL: {field}={native!r} is not in {TABLE_ID}")
        return {"native": f"{field}: {native}", "plain": PLAIN_IN_FIELD[(field, native)], "table": TABLE_ID}
    if native not in PLAIN:
        raise ContractError(f"UNTRANSLATED_LABEL: {native!r} is not in {TABLE_ID}")
    return {"native": native, "plain": PLAIN[native], "table": TABLE_ID}
