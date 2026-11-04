"""Build the view model from a verified extraction bundle. No paraphrase of content."""

from __future__ import annotations

from pathlib import Path

from . import SCHEMA, VERSION
from .labels import TABLE_ID, plain
from ..contract import ContractError, canonical, load_json, read_artifact, sha256
from ..extraction import output
from ..extraction.build import replay

WRITTEN_BY_RUN = "Written by the extraction run (model output). Not the paper's words."
SUB_CHECK_QUESTIONS = {
    "TRANSCRIPTION": "Does the claim repeat the paper's numbers exactly?",
    "P_FROM_T": "Recomputing p from the test statistic and its degrees of freedom: does it match the reported p?",
    "T_FROM_CI": "Is the test statistic consistent with the reported mean difference and 95% confidence interval?",
}
FIELD_ORDER = ["1", "2", "3", "4", "5A", "5B", "6"]
FIELD_TITLES = {"1": "What the study measured", "2": "The paper's strongest statement",
                "3": "The narrower claim the evidence supports", "4": "How others use the paper",
                "5A": "Where the wording grows inside the paper", "5B": "Where it grows downstream",
                "6": "The claim chosen for checking"}


def verify(receipt_dir: Path, root: Path) -> dict:
    """Content-replay the extraction bundle (and, through it, every linked bundle)."""
    manifest_bytes = (receipt_dir / "manifest.json").read_bytes()
    records_bytes = (receipt_dir / "records.jsonl").read_bytes()
    try:
        result = replay(manifest_bytes, records_bytes, root, "content")
    except ContractError as exc:
        raise ContractError(f"NOT_VERIFIED: {exc}") from exc
    records = [load_json(line) for line in records_bytes.splitlines() if line.strip()]
    return {"records": records, "manifest": load_json(manifest_bytes), "replay": result,
            "receipt": {"path": receipt_dir.resolve().relative_to(root.resolve()).as_posix(),
                        "manifest_sha256": sha256(manifest_bytes),
                        "records_sha256": sha256(records_bytes)}}


def first(records: list[dict], kind: str, **match) -> dict:
    found = [r for r in records if r["type"] == kind and all(r.get(k) == v for k, v in match.items())]
    if len(found) != 1:
        raise ContractError(f"VIEW_INPUT: expected one {kind} {match or ''}, found {len(found)}")
    return found[0]


def build_view(verified: dict, root: Path, crumb: dict | None = None, crumb_ids: set[str] | None = None) -> dict:
    """crumb: an optional question breadcrumb (atlas.view.question.question_context), whose
    refs must be in crumb_ids. It changes nothing else on the page."""
    records = verified["records"]
    by_id = {r["id"]: r for r in records}
    context = verified["manifest"]["input_context"]
    run = first(records, "ExtractionRun")
    cmap = first(records, "ExtractedClaimMap")
    f6 = by_id[cmap["designated_field_6_id"]]
    check = first(records, "EvidenceCheck")
    anchors = sorted((r for r in records if r["type"] == "SourceAnchor"), key=lambda r: r["anchor_id"])
    links = [r for r in records if r["type"] == "PassageLink"]
    crosses = [r for r in records if r["type"] == "CrossMapAlignment"]

    packet = load_json(read_artifact(root, context["source"]["sources_json"]))["sources"][context["source"]["packet_source_id"]]
    redacted = read_artifact(root, context["public"]["redacted_output"]).decode("utf-8")
    published = {a["id"]: a["quote"]["text"] for a in output.parse(redacted)["anchors"] if a["quote"]}
    imported = [load_json(line) for line in
                read_artifact(root, context["links"]["import_bundle"]["records"]).splitlines() if line.strip()]
    reviewers = {r["id"]: r for r in imported if r["type"] == "ReviewDecision"}
    provisional = [load_json(line) for line in
                   read_artifact(root, context["links"]["provisional_map_bundle"]["records"]).splitlines() if line.strip()]
    # Linked bundles were re-verified by the replay above; their IDs may be referenced.
    linked_ids = {r["id"] for r in imported} | {r["id"] for r in provisional}

    # What the paper says: only quotes already public, in the paper's order.
    paper_says = []
    for a in anchors:
        if a["anchor_id"] not in published:
            continue
        v = a["verification"]
        paper_says.append({"anchor_id": a["anchor_id"], "page": a["stated_page"], "section": a["stated_section"],
                           "text": published[a["anchor_id"]], "match": plain(v["state"]),
                           "extraction_start": v["extraction_span"][0], "refs": [a["id"]]})
    paper_says.sort(key=lambda p: p["extraction_start"])
    for p in paper_says:
        del p["extraction_start"]

    states = run["counts"]["by_state"]
    quotes = sum(states.get(k, 0) for k in ("MATCH", "NORMALIZED_MATCH_ONLY", "MISMATCH"))
    located = [a for a in anchors if a["verification"].get("found_page")]
    on_page = sum(1 for a in located if a["verification"]["page_consistent"])
    subs = check["detail"]["sub_checks"]
    review_ids = sorted({r["review_id"] for link in links for r in link["reviews"]})
    dispositions = sorted({r["disposition"] for link in links for r in link["reviews"]})
    not_read = packet.get("sections_not_accessible", [])

    glance = [
        {"topic": "The paper", "kind": "checked",
         "fact": (f"The run was given the full {packet['retrieval']['pdf_pages']}-page article. Atlas confirmed the "
                  "file is byte-identical to the copy on record and that its text extracts the same way."),
         "labels": [], "refs": [run["id"]]},
        {"topic": "Quotes", "kind": "checked",
         "fact": (f"{quotes} quotes from the run were checked against the paper's text: {states.get('MATCH', 0)} word "
                  f"for word, {states.get('NORMALIZED_MATCH_ONLY', 0)} differing only in spacing, "
                  f"{states.get('MISMATCH', 0)} not found exactly. {on_page} of {len(located)} located quotes are on "
                  "the page the run gave."),
         "labels": [plain("MATCH"), plain("NORMALIZED_MATCH_ONLY"), plain("MISMATCH")], "refs": [run["id"]]},
        {"topic": "The numbers", "kind": "checked",
         "fact": f"{sum(1 for s in subs if s['result'] == 'CONSISTENT')} of {len(subs)} arithmetic checks agree.",
         "labels": [plain(check["result"])], "refs": [check["id"]]},
        {"topic": "Earlier reviews", "kind": "limited",
         "fact": (f"{len(review_ids)} model reviews judged a sentence about what this paper reports. They gave "
                  "different results: "
                  + " and ".join("\u201c" + plain(d)["plain"].removeprefix("Reviewer: the passage ") + "\u201d"
                                 for d in dispositions)
                  + ". Neither is independent of the other."),
         "labels": [plain(d) for d in dispositions] + [plain("NOT_ESTABLISHED", "independence")], "refs": [l["id"] for l in links]},
        {"topic": "A person's ruling", "kind": "not-done", "fact": "No person has ruled on this claim or on the reviews.",
         "labels": [plain("NOT_RECORDED", "human_adjudication")], "refs": [check["id"], *[l["id"] for l in links]]},
        {"topic": "Who ran the extraction", "kind": "limited",
         "fact": (f"{run['runner']['identity']} on {run['runner']['interface']}, as stated by the person who ran it. "
                  f"The run reports it had seen this paper before, in training."),
         "labels": [plain(run["runner"]["basis"]), plain(run["exposure"]["independence"], "independence")],
         "refs": [run["id"]]},
        {"topic": "How others use this paper", "kind": "not-done",
         "fact": "Not searched. The run had no web access, by design.",
         "labels": [plain(cmap["fields"]["4"]["verification_state"])], "refs": [cmap["id"]]},
    ]

    findings = []
    for field in FIELD_ORDER:
        row = cmap["fields"].get(field)
        if not row:
            continue
        findings.append({"field": field, "title": FIELD_TITLES[field], "native_label": row["native_label"],
                         "label_status": row["label_status"], "content": row["table_content"],
                         "verification_state": row["verification_state"], "written_by": WRITTEN_BY_RUN,
                         "refs": [cmap["id"]]})

    sub_view = []
    for sub in subs:
        item = {"name": sub["sub_check"], "question": SUB_CHECK_QUESTIONS[sub["sub_check"]],
                "result": plain(sub["result"]), "detail": {}}
        if sub["sub_check"] == "TRANSCRIPTION":
            item["detail"] = {"rows": [{"statistic": r["statistic"], "claim": r["claim"], "paper": r["source"],
                                        "same": r["result"] == "SAME"} for r in sub["rows"]]}
        elif sub["sub_check"] == "P_FROM_T":
            item["detail"] = {"recomputed": sub["recomputed_p_interval"], "reported": sub["reported_p_interval"],
                              "df": sub["df"]}
        elif sub["sub_check"] == "T_FROM_CI":
            item["detail"] = {"implied": sub["implied_t_interval"], "reported": sub["reported_t_interval"],
                              "ci_centred_on_mean": sub["ci_centred_on_mean"]}
        sub_view.append(item)
    evidence_anchor = by_id[check["evidence"]["anchor"]]["anchor_id"]

    reviews = []
    for rid in review_ids:
        decision = reviewers[rid]
        sample = next(r for link in links for r in link["reviews"] if r["review_id"] == rid)
        within = sorted({by_id[l["source_anchor_id"]]["anchor_id"] for l in links
                         if any(r["review_id"] == rid for r in l["reviews"])})
        reviews.append({"review_id": rid.rsplit("/", 1)[1], "reviewer": decision["reviewer"],
                        "disposition": plain(sample["disposition"]), "proposition": sample["proposition"],
                        "parts": [{"part": p["part"], "text": p["text"], "disposition": plain(p["disposition"])}
                                  for p in sample["parts"]],
                        "independence": plain(sample["independence"], "independence"),
                        "human_adjudication": plain(sample["human_adjudication"], "human_adjudication"),
                        "paper_quotes_inside_its_passages": within,
                        "context": ("Made for an earlier audit whose target is a different paper. It judged whether "
                                    "passages from this paper support a sentence about what this paper reports."),
                        "refs": [rid, *[l["id"] for l in links if any(r["review_id"] == rid for r in l["reviews"])]]})

    missing = [{"item": f"Not available: {s}", "refs": [run["id"]]} for s in not_read]
    missing += [
        {"item": "How other papers, media or policy use this paper: not searched.", "refs": [cmap["id"]]},
        {"item": ("Which version of its instructions the model had: the model could not confirm it. The person who "
                  "ran it states the pinned file was attached."), "refs": [run["id"]],
         "labels": [plain(run["preflight"]["run_disposition"])]},
        {"item": f"{states.get('MISMATCH', 0)} quotes do not match the paper's text exactly; they are listed in the "
                 "technical record with the reason found.", "refs": [a["id"] for a in anchors
                                                                     if a["verification"].get("state") == "MISMATCH"]},
        *[{"item": f"Not checked: {n}.", "refs": [check["id"]]} for n in check["detail"]["not_checked"]],
        {"item": "No person has reviewed this extraction or the evidence check.", "refs": [run["id"]]},
    ]

    related = [{"text": ("An earlier claim map exists, made by a different audit. It is about a different paper, "
                         f"{c['historical_target_work_id']}, so it is not the same claim."),
                "relation": plain(c["relation"]), "identity": plain(c["claim_identity"]),
                "state": c["historical_map"]["state"], "refs": [c["id"], c["historical_statement_id"]]}
               for c in crosses]

    technical = {
        "anchors": [{"anchor_id": a["anchor_id"], "field": a["field"], "kind": a["kind"], "page": a["stated_page"],
                     "section": a["stated_section"], "state": a["verification"].get("state"),
                     "state_plain": plain(a["verification"]["state"])["plain"]
                     if a["verification"].get("state") in ("MATCH", "NORMALIZED_MATCH_ONLY", "MISMATCH") else None,
                     "page_consistent": a["verification"].get("page_consistent"),
                     "published": a["published_verbatim"],
                     "quote_sha256": a["verification"].get("quote_sha256"),
                     "diagnostic": a["verification"].get("diagnostic"), "record_id": a["id"]} for a in anchors],
        "records": [{"id": r["id"], "type": r["type"]} for r in sorted(records, key=lambda r: r["id"])],
        "receipt": verified["receipt"],
        # The interpreter that replays is not part of the view: only the result and level are.
        "replay": {"result": verified["replay"]["replay"], "level": verified["replay"]["level"]},
        "pins": {"pdf_sha256": run["source"]["pdf"]["sha256"],
                 "extraction_sha256": run["source"]["extraction"]["output_sha256"],
                 "full_output_sha256": run["output"]["full_sha256"],
                 "redacted_output_sha256": context["public"]["redacted_output"]["sha256"],
                 "instrument_sha256": run["method"]["instrument"]["sha256"],
                 "run_prompt_sha256": run["method"]["run_prompt"]["sha256"]},
    }

    view = {
        "schema": SCHEMA, "generator": {"name": "atlas-view", "version": VERSION}, "labels_table": TABLE_ID,
        "question": "What does the record show about this claim?",
        "paper": {"citation": packet["citation"], "work_id": context["source"]["work_id"],
                  "version": packet["version"], "refs": [run["id"]]},
        "claim": {"text": f6["text"], "written_by": WRITTEN_BY_RUN, "refs": [f6["id"], cmap["id"]]},
        "paper_says": paper_says,
        "paper_says_note": (f"{len(paper_says)} passages are shown because they are already public excerpts. "
                            f"The other {quotes - len(paper_says)} quoted passages were checked against the paper "
                            "but are not reproduced here."),
        "at_a_glance": glance,
        "check": {"name": check["check"], "result": plain(check["result"]), "evidence_anchor": evidence_anchor,
                  "scope": check["scope"], "sub_checks": sub_view, "not_checked": check["detail"]["not_checked"],
                  "refs": [check["id"], check["target_statement_id"], check["evidence"]["anchor"]]},
        "run_findings": findings,
        "reviews": reviews,
        "missing": missing,
        "related": related,
        "technical": technical,
        "rules": ["Atlas does not paraphrase content. The paper's words are quoted; model-written text is quoted "
                  "and labelled; plain-language labels come from a fixed table and sit beside the original label.",
                  "Nothing here is a score or a verdict on whether the claim is true.",
                  "Every item links to the records it comes from (technical record, below)."],
    }
    if crumb is not None:
        view["context"] = crumb
    check_refs(view, set(by_id) | linked_ids | (crumb_ids or set()))
    return view


def check_refs(view: dict, ids: set[str]) -> None:
    """Every ref anywhere in the view must name a record in the verified bundle."""
    linked = set()
    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key == "refs":
                    linked.update(value)
                else:
                    walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)
    walk({k: v for k, v in view.items() if k != "technical"})
    unknown = sorted(linked - ids)
    if unknown:
        raise ContractError(f"VIEW_REF_UNRESOLVED: {unknown}")


def view_json(view: dict) -> bytes:
    return (canonical(view) + "\n").encode("utf-8")
