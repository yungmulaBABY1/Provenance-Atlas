"""Public stage: build, validate and replay an extraction bundle from committed files only."""

from __future__ import annotations

from pathlib import Path
import platform
import unicodedata

from . import ANCHOR_SCHEMA, CONTEXT_SCHEMA, SCHEMA, VERSION
from . import output, stats
from ..claims import link as claimlink
from ..contract import NORMALIZER, ContractError, canonical, digest, load_json, normalize, read_artifact, require, sha256

PACKAGE = Path(__file__).parent
TYPES = {"ExtractionRun", "ExtractedClaimMap", "FieldStatement", "TextComparison", "SourceAnchor",
         "PassageLink", "CrossMapAlignment", "EvidenceCheck", "ExtractionManifest"}
FIELDS = {
    "ExtractionRun": {"method": dict, "runner": dict, "conditions": dict, "exposure": dict,
                      "source": dict, "output": dict, "preflight": dict, "counts": dict},
    "ExtractedClaimMap": {"extraction_run_id": str, "producer": dict, "fields": dict, "fields_present": list,
                          "designated_field_6_id": (str, type(None)), "parse_issues": list},
    "FieldStatement": {"extraction_run_id": str, "field": str, "role": str, "text": str, "text_sha256": str,
                       "normalized_text": str, "anchor": dict, "status": str},
    "TextComparison": {"extraction_run_id": str, "subject_id": str, "object_id": str, "exact_match": bool,
                       "normalized_match": bool, "result": str, "semantic_equivalence": str},
    "SourceAnchor": {"extraction_run_id": str, "anchor_id": str, "field": str, "kind": str,
                     "published_verbatim": bool, "verification": dict},
    "PassageLink": {"extraction_run_id": str, "source_anchor_id": str, "packet_excerpt_id": str,
                    "passage_id": str, "relation": str, "relation_basis": str, "reviews": list},
    "CrossMapAlignment": {"extraction_run_id": str, "new_statement_id": str, "historical_statement_id": str,
                          "new_target_work_id": str, "historical_target_work_id": str, "relation": str,
                          "text_comparison": dict, "claim_identity": str},
    "EvidenceCheck": {"extraction_run_id": str, "check": str, "target_statement_id": str,
                      "evidence": dict, "result": str, "detail": dict, "scope": str},
    "ExtractionManifest": {"extraction_run_id": str, "executor": dict, "input_context": dict,
                           "declared_input_receipts": list, "environment": dict, "execution": dict,
                           "record_ids": list, "records_before_manifest_sha256": str},
}
LABELS = {
    ("TextComparison", "result"): {"MATCH", "NORMALIZED_MATCH_ONLY", "MISMATCH"},
    ("FieldStatement", "status"): {"USABLE", "NOT_USABLE"},
    ("EvidenceCheck", "result"): {"CONSISTENT", "INCONSISTENT", "PARTIALLY_CHECKABLE", "NOT_CHECKABLE"},
    ("CrossMapAlignment", "relation"): {"DIFFERENT_TARGET_WORKS", "SAME_TARGET_WORK"},
    ("SourceAnchor", "kind"): {"QUOTE", "SAME_AS", "ABSENCE", "RECONSTRUCTION", "UNCLASSIFIED", "DUPLICATE_ID"},
}
SHARED_MODULES = ("__init__.py", "contract.py", "integrity.py", "native.py", "reviews.py", "adapter.py",
                  "sources.py", "claims/__init__.py", "claims/link.py", "claims/standalone.py")


def record(record_type: str, id: str, **fields) -> dict:
    if record_type not in TYPES:
        raise ContractError(f"UNKNOWN_RECORD_TYPE: {record_type}")
    return {"schema_version": SCHEMA, "type": record_type, "id": id, **fields}


def jsonl(records: list[dict]) -> bytes:
    return ("\n".join(canonical(r) for r in sorted(records, key=lambda r: r["id"])) + "\n").encode("utf-8")


def validate(records: list[dict], external_ids: set[str]) -> None:
    by_id = {}
    for item in records:
        require(item, {"id": str, "schema_version": str, "type": str, "refs": list}, "record")
        if item["id"] in by_id or item["id"] in external_ids:
            raise ContractError(f"DUPLICATE_ID: {item['id']}")
        by_id[item["id"]] = item
    for item in records:
        if item["schema_version"] != SCHEMA or item["type"] not in TYPES:
            raise ContractError(f"UNSUPPORTED_RECORD: {item['id']}")
        for key, kind in FIELDS[item["type"]].items():
            kinds = kind if isinstance(kind, tuple) else (kind,)
            if key not in item or type(item[key]) not in kinds:
                raise ContractError(f"INVALID_CONTRACT: {item['type']}.{key}: {item['id']}")
        for (kind, key), allowed in LABELS.items():
            if item["type"] == kind and item[key] not in allowed:
                raise ContractError(f"INVALID_LABEL: {kind}.{key}={item[key]}")
        for ref in item["refs"]:
            if ref not in by_id and ref not in external_ids:
                raise ContractError(f"UNRESOLVED_REFERENCE: {item['id']} -> {ref}")
        if item["type"] == "FieldStatement" and sha256(item["text"].encode("utf-8")) != item["text_sha256"]:
            raise ContractError(f"STATEMENT_HASH_MISMATCH: {item['id']}")
        if item["type"] == "TextComparison":
            expected = ("MATCH" if item["exact_match"] else
                        "NORMALIZED_MATCH_ONLY" if item["normalized_match"] else "MISMATCH")
            if item["result"] != expected:
                raise ContractError(f"INVALID_LABEL: comparison contradicts its match fields: {item['id']}")
        if item["type"] == "EvidenceCheck":
            target = by_id.get(item["target_statement_id"], {})
            if target.get("status") != "USABLE":
                raise ContractError(f"INELIGIBLE_CHECK_TARGET: {item['id']}")
        if item["type"] == "CrossMapAlignment":
            same = item["new_target_work_id"] == item["historical_target_work_id"]
            if item["relation"] != ("SAME_TARGET_WORK" if same else "DIFFERENT_TARGET_WORKS"):
                raise ContractError(f"INVALID_LABEL: target-work relation: {item['id']}")
            if not same and item["claim_identity"] != "NOT_THE_SAME_AUDIT_TARGET":
                raise ContractError(f"UNSUPPORTED_IDENTITY: {item['id']}")
    manifests = [r for r in records if r["type"] == "ExtractionManifest"]
    if len(manifests) != 1:
        raise ContractError("INVALID_MANIFEST_COVERAGE: exactly one ExtractionManifest required")
    body = [r for r in records if r is not manifests[0]]
    if manifests[0]["record_ids"] != sorted(r["id"] for r in body):
        raise ContractError("INVALID_MANIFEST_COVERAGE: manifest does not list exactly the bundle records")
    if sha256(jsonl(body)) != manifests[0]["records_before_manifest_sha256"]:
        raise ContractError("MANIFEST_RECORD_HASH_MISMATCH")


def check_public_files(context: dict, root: Path) -> dict:
    """Everything CI can verify about the local stage's public files, without the source."""
    public = context["public"]
    av_bytes = read_artifact(root, public["anchor_verification"])
    redacted_bytes = read_artifact(root, public["redacted_output"])
    av = load_json(av_bytes)
    if av.get("schema") != ANCHOR_SCHEMA:
        raise ContractError("UNSUPPORTED_ANCHOR_SCHEMA")
    for key, pinned in (("full_output_sha256", context["output"]["full_sha256"]),
                        ("pdf_sha256", context["source"]["pdf"]["sha256"]),
                        ("redacted_output_sha256", public["redacted_output"]["sha256"])):
        if av[key] != pinned:
            raise ContractError(f"ANCHOR_VERIFICATION_PIN_MISMATCH: {key}")
    if av["extraction"]["output_sha256"] != context["source"]["extraction"]["output_sha256"]:
        raise ContractError("ANCHOR_VERIFICATION_PIN_MISMATCH: extraction")
    packet = load_json(read_artifact(root, context["source"]["sources_json"]))["sources"][context["source"]["packet_source_id"]]
    texts = {e["id"]: (e["extraction_start"], e["text"]) for e in packet["excerpts"]}
    for item in public["evidence_excerpts"]:
        data = read_artifact(root, item)
        entry = next((e for e in av["public_excerpts"] if e["id"] == f"evidence:{item['anchor_id']}"), None)
        if entry is None or entry["sha256"] != item["sha256"] or len(data.decode("utf-8")) != entry["end"] - entry["start"]:
            raise ContractError(f"EVIDENCE_EXCERPT_MISMATCH: {item['anchor_id']}")
        texts[entry["id"]] = (entry["start"], data.decode("utf-8"))
    redacted = redacted_bytes.decode("utf-8")
    parsed = output.parse(redacted)
    if [(a["id"], a["kind"]) for a in parsed["anchors"]] != [(a["id"], a["kind"]) for a in av["anchors"]]:
        raise ContractError("REDACTED_OUTPUT_ANCHOR_SET_MISMATCH")
    checked = 0
    for mine, recorded in zip(parsed["anchors"], av["anchors"]):
        if mine["kind"] != "QUOTE":
            continue
        match = recorded["match"]
        if recorded["published_verbatim"]:
            quote = mine["quote"]["text"] if mine["quote"] else None
            if quote is None or sha256(quote.encode("utf-8")) != match["quote_sha256"]:
                raise ContractError(f"PUBLISHED_QUOTE_MISMATCH: {mine['id']}")
            start, end = match["extraction_span"]
            for excerpt_id in recorded["within_public_excerpts"]:
                origin, text = texts[excerpt_id]
                piece = text[start - origin:end - origin]
                if (len(piece) != end - start or normalize(piece) != normalize(quote)
                        or (match["state"] == "MATCH" and piece != quote)):
                    raise ContractError(f"PUBLISHED_QUOTE_NOT_IN_EXCERPT: {mine['id']} / {excerpt_id}")
            checked += 1
        elif not mine["withheld"] or mine["withheld"]["quote_sha256"] != match["quote_sha256"] \
                or mine["withheld"]["chars"] != match["quote_chars"]:
            raise ContractError(f"WITHHELD_QUOTE_MISMATCH: {mine['id']}")
    return {"anchor_verification": av, "redacted": redacted, "parsed": parsed, "excerpt_texts": texts,
            "published_quotes_rechecked": checked,
            "inputs": [{**public["anchor_verification"], "bytes": len(av_bytes)},
                       {**public["redacted_output"], "bytes": len(redacted_bytes)}]}


def statement(rid: str, field: str, role: str, item: dict | None, redacted_sha: str, refs: list) -> dict | None:
    if not item:
        return None
    text = item["text"]
    return record("FieldStatement", f"{rid}/statement/{role.lower().replace('_', '-')}",
                  extraction_run_id=rid, field=field, role=role, text=text,
                  text_sha256=sha256(text.encode("utf-8")), normalized_text=normalize(text),
                  anchor={"output_sha256": redacted_sha, "output": "REDACTED_PUBLIC_COPY", "line": item["line"],
                          "char_start": item["char_start"], "char_end": item["char_end"],
                          "char_unit": "unicode_codepoint", "char_interval": "half_open"},
                  status=item.get("status", "USABLE") if item.get("status", "USABLE") == "USABLE" else "NOT_USABLE",
                  refs=refs)


def comparison(rid: str, a: dict, b: dict, name: str) -> dict:
    exact, normalized, result = claimlink.compare(
        {"exact_text": a["text"], "normalized_text": a["normalized_text"]},
        {"exact_text": b.get("text", b.get("exact_text")), "normalized_text": b["normalized_text"]})
    return record("TextComparison", f"{rid}/compare/{name}", extraction_run_id=rid, subject_id=a["id"],
                  object_id=b["id"], exact_match=exact, normalized_match=normalized, result=result,
                  semantic_equivalence="NOT_ASSESSED_IDENTICAL_TEXT" if exact else "UNASSESSED",
                  basis=f"DETERMINISTIC_TEXT_COMPARISON; {NORMALIZER}; no semantic judgment", refs=[rid, a["id"], b["id"]])


def build(context: dict, root: Path) -> dict:
    require(context, {"schema_version": str, "run": dict, "source": dict, "output": dict, "local": dict,
                      "public": dict, "links": dict, "evidence_check": dict}, "context")
    if context["schema_version"] != CONTEXT_SCHEMA:
        raise ContractError("UNSUPPORTED_SCHEMA")
    run, rid = context["run"], context["run"]["id"]
    method_inputs = []
    for key in ("instrument", "run_prompt"):
        data = read_artifact(root, run["method"][key])
        method_inputs.append({**run["method"][key], "bytes": len(data)})
    public = check_public_files(context, root)
    parsed, av = public["parsed"], public["anchor_verification"]
    redacted_sha = context["public"]["redacted_output"]["sha256"]

    # Linked bundles: the reviewed import (passages, reviews) and the provisional map.
    links = context["links"]
    dep = claimlink.load_dependency({"dependency": links["import_bundle"]}, root)
    prov_bytes = read_artifact(root, links["provisional_map_bundle"]["records"])
    read_artifact(root, links["provisional_map_bundle"]["manifest"])
    prov = [load_json(line) for line in prov_bytes.splitlines() if line.strip()]
    try:
        claimlink.validate(prov, set(dep["by_id"]))
    except ContractError as exc:
        raise ContractError(f"PROVISIONAL_MAP_BUNDLE_INVALID: {exc}") from exc
    prov_by_id = {r["id"]: r for r in prov}
    external = set(dep["by_id"]) | set(prov_by_id)

    records = []
    # Field 6: the section statement is designated; the table cell and one-line summary are restatements.
    designated = statement(rid, "6", "FIELD_6_SECTION", parsed["field_6_section"], redacted_sha, [rid])
    cell = statement(rid, "6", "FIELD_6_TABLE_CELL", parsed["table"].get("6", {}).get("content"), redacted_sha, [rid])
    summary = statement(rid, "6", "SUMMARY_CLAIM_UNDER_AUDIT", parsed["summaries"].get("CLAIM UNDER AUDIT"),
                        redacted_sha, [rid])
    for item in (designated, cell, summary):
        if item:
            records.append(item)
    if designated:
        for other in (cell, summary):
            if other:
                records.append(comparison(rid, designated, other, f"field-6-section~{other['role'].lower().replace('_', '-')}"))

    fields = {}
    for field, row in parsed["table"].items():
        fields[field] = {"native_label": row["native_label"], "instrument_label": row["instrument_label"],
                         "label_status": row["label_status"], "status": row["status"],
                         "table_content": row["content"]["text"], "verification_state": row["verification_state"]["text"]}
    records.append(record(
        "ExtractedClaimMap", f"{rid}/claim-map", extraction_run_id=rid,
        producer={"instrument": "claim-extraction", "claim_extraction_output": True,
                  "mode": "STANDALONE_STAGE_1_RUN", "work_id": context["source"]["work_id"]},
        fields=fields, fields_present=sorted(fields), designated_field_6_id=designated["id"] if designated else None,
        sections={k: v["sha256"] for k, v in sorted(parsed["sections"].items())},
        claim_inventory="PRESENT" if "CLAIM INVENTORY" in parsed["sections"] else "ABSENT",
        parse_issues=parsed["issues"], refs=[rid, *([designated["id"]] if designated else [])]))

    # Source anchors.
    anchor_ids = {}
    for entry in av["anchors"]:
        aid = f"{rid}/anchor/{entry['id']}"
        anchor_ids[entry["id"]] = aid
        match = entry["match"]
        records.append(record(
            "SourceAnchor", aid, extraction_run_id=rid, anchor_id=entry["id"], field=entry["field"],
            kind=entry["kind"], stated_page=entry["stated_page"], stated_section=entry["stated_section"],
            refers_to=entry["refers_to"], published_verbatim=entry["published_verbatim"],
            within_public_excerpts=entry["within_public_excerpts"],
            verification=({"basis": "LOCAL: matched against the pinned extraction by atlas.extraction.local; "
                                    "re-run requires the PDF. Published quotes re-checked in this build "
                                    "against public excerpts.",
                           "state": match["state"], "location": match["location"],
                           "extraction_span": match["extraction_span"], "found_page": match["found_page"],
                           "page_consistent": entry["page_consistent"], "quote_sha256": match["quote_sha256"],
                           "normalized_quote_sha256": match["normalized_quote_sha256"],
                           "quote_chars": match["quote_chars"], "diagnostic": match["diagnostic"]}
                          if match else {"basis": "NO_QUOTE", "state": "NOT_APPLICABLE"}),
            refs=[rid]))

    # Passage links: anchors inside packet excerpts that imported passages and reviews are bound to.
    imported_run = links["import_bundle"]["audit_run_id"]
    reviews = [r for r in dep["records"] if r["type"] == "ReviewDecision" and r.get("target_binding") == "MATCH"
               and r["id"].startswith(f"{imported_run}/review/")]
    link_count = 0
    for entry in av["anchors"]:
        for excerpt_id in entry["within_public_excerpts"]:
            passage_id = f"{imported_run}/passage/{excerpt_id}"
            if passage_id not in dep["by_id"]:
                continue
            bound = [r for r in reviews if excerpt_id in r["review"]["target"]["passages"]]
            records.append(record(
                "PassageLink", f"{rid}/passage-link/{entry['id']}~{excerpt_id}", extraction_run_id=rid,
                source_anchor_id=anchor_ids[entry["id"]], packet_excerpt_id=excerpt_id, passage_id=passage_id,
                relation="ANCHOR_WITHIN_IMPORTED_PASSAGE",
                relation_basis=("DOCUMENTED: offsets in the same pdftotext extraction "
                                f"({context['source']['extraction']['output_sha256'][:16]}...); "
                                "says nothing about support or meaning"),
                layers={"paper_statement": anchor_ids[entry["id"]],
                        "audited_claim_in_this_run": designated["id"] if designated else None,
                        "reviewer_decompositions": [r["id"] for r in bound]},
                reviews=[{"review_id": r["id"], "disposition": r["imported_disposition"],
                          "proposition": r["review"]["target"]["proposition"],
                          "parts": [{"part": p["part"], "text": p["text"], "disposition": p["disposition"]}
                                    for p in r["review"]["part_dispositions"]],
                          "independence": r["independence"], "human_adjudication": r["human_adjudication"]}
                         for r in bound],
                refs=[rid, anchor_ids[entry["id"]], passage_id, *[r["id"] for r in bound]]))
            link_count += 1

    # The historical provisional map is kept as it is and compared, not merged.
    old_f6 = next((r for r in prov if r["type"] == "ClaimStatement" and r["role"] == "MAP_FIELD_6"
                   and r["field_status"] == "USABLE"), None)
    old_run = next(r for r in prov if r["type"] == "ClaimLinkRun")
    old_target = dep["run"]["target_work_id"]
    if designated and old_f6:
        text_cmp = claimlink.compare({"exact_text": designated["text"], "normalized_text": designated["normalized_text"]},
                                     old_f6)
        same_work = context["source"]["work_id"] == old_target
        records.append(record(
            "CrossMapAlignment", f"{rid}/cross-map/provisional-field-6", extraction_run_id=rid,
            new_statement_id=designated["id"], historical_statement_id=old_f6["id"],
            new_target_work_id=context["source"]["work_id"], historical_target_work_id=old_target,
            relation="SAME_TARGET_WORK" if same_work else "DIFFERENT_TARGET_WORKS",
            text_comparison={"exact_match": text_cmp[0], "normalized_match": text_cmp[1], "result": text_cmp[2]},
            claim_identity="UNRESOLVED_REQUIRES_REVIEW" if same_work else "NOT_THE_SAME_AUDIT_TARGET",
            historical_map={"claim_link_run_id": old_run["id"], "state": "UNCHANGED; read from its pinned receipt",
                            "producer": "citation-network degraded standalone fallback"},
            refs=[rid, designated["id"], old_f6["id"], old_run["id"]]))

    # The declared evidence check.
    check_decl = context["evidence_check"]
    evidence = next(e for e in context["public"]["evidence_excerpts"] if e["anchor_id"] == check_decl["evidence_anchor_id"])
    excerpt_text = public["excerpt_texts"][f"evidence:{check_decl['evidence_anchor_id']}"][1]
    clause_at = normalize(excerpt_text).find(check_decl["source_clause_from"])
    if clause_at < 0 or not designated:
        raise ContractError("EVIDENCE_CHECK_INPUT_UNAVAILABLE")
    clause = normalize(excerpt_text)[clause_at:]
    result = stats.check(designated["text"], clause)
    records.append(record(
        "EvidenceCheck", f"{rid}/evidence-check/1", extraction_run_id=rid, check=result["check"],
        target_statement_id=designated["id"],
        evidence={"anchor": anchor_ids[check_decl["evidence_anchor_id"]], "excerpt": evidence,
                  "source_clause": clause, "clause_rule": f"normalized excerpt from {check_decl['source_clause_from']!r} to its end"},
        result=result["result"], detail={k: v for k, v in result.items() if k not in ("check", "result", "scope")},
        scope=result["scope"], declared_reason=check_decl["why_this_check"],
        refs=[rid, designated["id"], anchor_ids[check_decl["evidence_anchor_id"]]]))

    states = {}
    for entry in av["anchors"]:
        key = entry["match"]["state"] if entry["match"] else entry["kind"]
        states[key] = states.get(key, 0) + 1
    records.append(record(
        "ExtractionRun", rid, method=run["method"], runner=run["runner"], conditions=run["conditions"],
        executed_at=run["executed_at"], exposure=run["exposure"], operator=run["operator"],
        recorded_by=run["recorded_by"], source=context["source"], output=context["output"],
        preflight={"run_line": parsed["preflight"]["text"] if parsed["preflight"] else None,
                   "run_disposition": parsed["preflight"]["disposition"] if parsed["preflight"] else None,
                   "operator_attestation": run["conditions"]["attachments"],
                   "note": ("The run could not hash the instrument and reported INSTRUMENT VERSION UNVERIFIED. "
                            "The operator states the attached file was the one supplied (sha256 pinned above). "
                            "That is an attestation, not a verification by the run.")},
        counts={"anchors": len(av["anchors"]), "by_state": dict(sorted(states.items())),
                "published_verbatim": sum(1 for e in av["anchors"] if e["published_verbatim"]),
                "published_quotes_rechecked_in_build": public["published_quotes_rechecked"],
                "passage_links": link_count},
        refs=[f"{rid}/claim-map", f"{rid}/evidence-check/1"]))

    shared = {name: sha256((PACKAGE.parent / name).read_bytes()) for name in SHARED_MODULES}
    own = {p.name: sha256(p.read_bytes()) for p in sorted(PACKAGE.glob("*.py"))}
    body = list(records)
    manifest = record(
        "ExtractionManifest", f"{rid}/manifest", extraction_run_id=rid,
        executor={"name": "atlas-extraction", "version": VERSION, "code_sha256": own, "shared_code_sha256": shared,
                  "parser": parsed["parser"]},
        input_context=context,
        declared_input_receipts=[*method_inputs, *public["inputs"], *dep["inputs"],
                                 {**links["provisional_map_bundle"]["records"], "bytes": len(prov_bytes)}],
        environment={"implementation": platform.python_implementation(), "python": platform.python_version(),
                     "unicode": unicodedata.unidata_version},
        execution={"models_invoked": [], "network": "NOT_USED", "source_pdf": "NOT_READ_IN_THIS_STAGE",
                   "scope": "deterministic build from committed files"},
        record_ids=sorted(r["id"] for r in body), records_before_manifest_sha256=sha256(jsonl(body)), refs=[rid])
    records.append(manifest)
    validate(records, external)
    payload = jsonl(records)
    return {"records": records, "jsonl": payload, "manifest": manifest, "external_ids": external,
            "jsonl_sha256": sha256(payload)}


def without_environment(item: dict) -> dict:
    return {k: v for k, v in item.items() if not (item["type"] == "ExtractionManifest" and k == "environment")}


def replay(manifest_bytes: bytes, jsonl_bytes: bytes, root: Path, level: str = "strict") -> dict:
    if level not in ("strict", "content"):
        raise ContractError(f"UNSUPPORTED_REPLAY_LEVEL: {level}")
    manifest = load_json(manifest_bytes)
    try:
        bundle = build(manifest["input_context"], root)
    except (ContractError, KeyError) as exc:
        raise ContractError(f"REPLAY_MISMATCH: input: {exc}") from exc
    stored = [load_json(line) for line in jsonl_bytes.splitlines() if line.strip()]
    try:
        validate(stored, bundle["external_ids"])
    except ContractError as exc:
        raise ContractError(f"REPLAY_MISMATCH: records: {exc}") from exc
    old = {r["id"]: without_environment(r) for r in stored}
    new = {r["id"]: without_environment(r) for r in bundle["records"]}
    differing = []
    changed = sorted(i for i in old.keys() | new.keys() if old.get(i) != new.get(i))
    if changed:
        differing.append("records: " + ", ".join(changed))
    if without_environment(manifest) != without_environment(bundle["manifest"]):
        differing.append("manifest")
    delta = {k: {"recorded": manifest.get("environment", {}).get(k), "replayed": bundle["manifest"]["environment"].get(k)}
             for k in sorted(manifest.get("environment", {}).keys() | bundle["manifest"]["environment"].keys())
             if manifest.get("environment", {}).get(k) != bundle["manifest"]["environment"].get(k)}
    if level == "strict" and delta:
        differing.append("environment: " + ", ".join(delta))
    if level == "strict" and not differing and bundle["jsonl"] != jsonl_bytes:
        differing.append("bytes")
    if differing:
        raise ContractError(f"REPLAY_MISMATCH ({level}): " + "; ".join(differing))
    return {"replay": "PASS", "level": level, "environment_delta": delta,
            "scope": "deterministic extraction-bundle replay; the model run and the PDF are not reproduced"}
