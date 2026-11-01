"""Build, validate and replay a claim-link bundle over one pinned import bundle."""

from __future__ import annotations

from pathlib import Path
import platform
import re
import unicodedata

from . import CONTEXT_SCHEMA, SCHEMA, VERSION
from . import standalone
from ..contract import (NORMALIZER, ContractError, canonical, digest, load_json, normalize,
                        read_artifact, require, sha256, validate_records)
from ..adapter import git_blob_sha1
from ..integrity import verify_records

PACKAGE = Path(__file__).parent
# Shared modules this code reads dependency bundles with; their bytes are part of
# this executor's identity.
SHARED_MODULES = ("__init__.py", "adapter.py", "contract.py", "integrity.py", "native.py",
                  "reviews.py", "sources.py", "ledger.py")

# The claim-extraction instrument's output table (prompts/1-claim-extraction.txt,
# REQUIRED OUTPUT TABLE). Checked against the pinned contract bytes on every build.
CONTRACT_ROWS = {"1": "| 1. Literally measured |", "2": "| 2. Source's strongest claim |",
                 "3": "| 3. Weaker defensible claim |", "4": "| 4. Downstream claim |",
                 "5A": "| 5A. Within-source inflation point + failure location |",
                 "5B": "| 5B. Downstream inflation point + failure location |",
                 "6": "| 6. Claim under audit |"}

TYPES = {"ClaimLinkRun", "ClaimMap", "ClaimStatement", "TextComparison", "TargetAlignment",
         "ReviewScope", "ClaimLinkManifest"}
FIELDS = {
    "ClaimLinkRun": {"dependency": dict, "method": str, "source_statement": dict,
                     "claim_map_id": str, "alignment_ids": list, "counts": dict},
    "ClaimMap": {"claim_link_run_id": str, "state": str, "producer": dict, "fields_present": list,
                 "fields_absent": dict, "field_statement_ids": dict, "reconciliation": str,
                 "parse_issues": list},
    "ClaimStatement": {"claim_link_run_id": str, "role": str, "exact_text": str,
                       "exact_text_sha256": str, "normalized_text": str, "anchor": dict,
                       "written_by": dict, "statement_kind": str},
    "TextComparison": {"claim_link_run_id": str, "subject_id": str, "object_id": str,
                       "exact_match": bool, "normalized_match": bool, "result": str,
                       "semantic_equivalence": str, "basis": str},
    "TargetAlignment": {"claim_link_run_id": str, "finding_id": str, "target_kind": str,
                        "designated_target_id": (str, type(None)), "finding_target_id": (str, type(None)),
                        "comparison_ids": list, "claim_identity": str, "native_field_6_mentions": list,
                        "reviewer_decomposition_ids": list, "detached_review_ids": list,
                        "finding_import_status": str},
    "ReviewScope": {"claim_link_run_id": str, "review_id": str, "binding": str,
                    "finding_id": (str, type(None)), "reviewed_field": (str, type(None)),
                    "reviewed_span": (list, type(None)), "proposition": (str, type(None)),
                    "parts": list, "disposition": str, "reviewer": dict,
                    "relation_to_finding_target": str, "relation_to_audited_claim": str,
                    "dependency_record_sha256": str},
    "ClaimLinkManifest": {"claim_link_run_id": str, "executor": dict, "parser": dict,
                          "normalizer": str, "input_context": dict, "declared_input_receipts": list,
                          "dependency": dict, "environment": dict, "execution": dict,
                          "record_ids": list, "records_before_manifest_sha256": str},
}
LABELS = {
    ("TextComparison", "result"): {"MATCH", "NORMALIZED_MATCH_ONLY", "MISMATCH"},
    ("TextComparison", "semantic_equivalence"): {"NOT_ASSESSED_IDENTICAL_TEXT", "UNASSESSED"},
    ("TargetAlignment", "target_kind"): {"TEXT", "FIELD_6_REFERENCE", "MAP_GAP_DECLARED", "ABSENT"},
    ("TargetAlignment", "claim_identity"): {"SAME_TEXT", "SAME_TEXT_AFTER_NORMALIZATION",
                                            "DECLARED_BY_REFERENCE", "DECLARED_NOT_ON_MAP",
                                            "UNRESOLVED_REQUIRES_REVIEW", "NO_TARGET_STATED"},
    ("ClaimStatement", "role"): {"MAP_FIELD_1", "MAP_FIELD_3", "MAP_FIELD_6", "CONFIRMATION_FIELD_1",
                                 "CONFIRMATION_FIELD_3", "CONFIRMATION_FIELD_6",
                                 "CONFIRMATION_TARGET_LAYER", "FINDING_TARGET_CLAIM"},
    ("ReviewScope", "binding"): {"MATCH", "TARGET_MISMATCH"},
}
FIELD_6_REFERENCE = re.compile(r"claim map field 6\b(.*)", re.IGNORECASE | re.DOTALL)


def validate_context(context: dict) -> None:
    require(context, {"schema_version": str, "run": dict, "dependency": dict,
                      "claim_extraction_contract": dict}, "context")
    if context["schema_version"] != CONTEXT_SCHEMA:
        raise ContractError("UNSUPPORTED_SCHEMA")
    require(context["run"], {"id": str, "operator": str, "purpose": str}, "run")
    require(context["dependency"], {"audit_run_id": str, "manifest": dict, "records": dict}, "dependency")
    require(context["claim_extraction_contract"], {"path": str, "sha256": str}, "claim_extraction_contract")


def record(record_type: str, id: str, **fields) -> dict:
    if record_type not in TYPES:
        raise ContractError(f"UNKNOWN_RECORD_TYPE: {record_type}")
    return {"schema_version": SCHEMA, "type": record_type, "id": id, **fields}


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
            if key not in item:
                raise ContractError(f"MISSING: {item['type']}.{key}: {item['id']}")
            kinds = kind if isinstance(kind, tuple) else (kind,)
            if type(item[key]) not in kinds:
                raise ContractError(f"INVALID_CONTRACT: {item['type']}.{key}: {item['id']}")
        for (rtype, key), allowed in LABELS.items():
            if item["type"] == rtype and item[key] not in allowed:
                raise ContractError(f"INVALID_LABEL: {rtype}.{key}={item[key]}")
        if len(item["refs"]) != len(set(item["refs"])):
            raise ContractError(f"INVALID_CONTRACT: duplicate refs: {item['id']}")
        for ref in item["refs"]:
            if ref not in by_id and ref not in external_ids:
                raise ContractError(f"UNRESOLVED_REFERENCE: {item['id']} -> {ref}")
        if item["type"] == "ClaimStatement" and sha256(item["exact_text"].encode("utf-8")) != item["exact_text_sha256"]:
            raise ContractError(f"STATEMENT_HASH_MISMATCH: {item['id']}")
        if item["type"] == "TextComparison":
            # A displayed MATCH must be an exact code-point match, as for Passage.
            expected = ("MATCH" if item["exact_match"] else
                        "NORMALIZED_MATCH_ONLY" if item["normalized_match"] else "MISMATCH")
            if item["result"] != expected or (item["exact_match"] and not item["normalized_match"]):
                raise ContractError(f"INVALID_LABEL: comparison contradicts its match fields: {item['id']}")
    manifests = [r for r in records if r["type"] == "ClaimLinkManifest"]
    if len(manifests) != 1:
        raise ContractError("INVALID_MANIFEST_COVERAGE: exactly one ClaimLinkManifest required")
    manifest = manifests[0]
    covered = sorted(r["id"] for r in records if r is not manifest)
    if manifest["record_ids"] != covered:
        raise ContractError("INVALID_MANIFEST_COVERAGE: manifest does not list exactly the bundle records")
    if sha256(jsonl([r for r in records if r is not manifest])) != manifest["records_before_manifest_sha256"]:
        raise ContractError("MANIFEST_RECORD_HASH_MISMATCH")


def jsonl(records: list[dict]) -> bytes:
    return ("\n".join(canonical(r) for r in sorted(records, key=lambda r: r["id"])) + "\n").encode("utf-8")


def compare(a: dict, b: dict) -> tuple[bool, bool, str]:
    exact = a["exact_text"] == b["exact_text"]
    normalized = a["normalized_text"] == b["normalized_text"]
    return exact, normalized, ("MATCH" if exact else "NORMALIZED_MATCH_ONLY" if normalized else "MISMATCH")


def load_dependency(context: dict, root: Path) -> dict:
    dep = context["dependency"]
    manifest_bytes = read_artifact(root, dep["manifest"])
    records_bytes = read_artifact(root, dep["records"])
    records = [load_json(line) for line in records_bytes.splitlines() if line.strip()]
    try:
        validate_records(records)
        verified = verify_records(records)
    except ContractError as exc:
        raise ContractError(f"DEPENDENCY_INVALID: {exc}") from exc
    by_id = {r["id"]: r for r in records}
    run = by_id.get(dep["audit_run_id"])
    if run is None or run["type"] != "AuditRun":
        raise ContractError("DEPENDENCY_INVALID: audit_run_id not in bundle")
    manifest = load_json(manifest_bytes)
    stored = by_id.get(manifest.get("id"))
    if stored is None or stored != manifest or manifest.get("audit_run_id") != run["id"]:
        raise ContractError("DEPENDENCY_MANIFEST_MISMATCH: manifest file is not this bundle's run manifest")
    return {"records": records, "by_id": by_id, "run": run, "manifest": manifest,
            "native_projection": ("VERIFIED" if run["id"] in verified["native_projection_verified"]
                                  else "UNVERIFIED"),
            "inputs": [{**dep["manifest"], "bytes": len(manifest_bytes)},
                       {**dep["records"], "bytes": len(records_bytes)}],
            "pins": {"manifest_sha256": sha256(manifest_bytes), "records_sha256": sha256(records_bytes)}}


def check_contract(context: dict, root: Path) -> dict:
    data = read_artifact(root, context["claim_extraction_contract"])
    text = data.decode("utf-8")
    missing = [field for field, row in CONTRACT_ROWS.items() if row not in text]
    if missing:
        raise ContractError(f"CONTRACT_TABLE_MISMATCH: rows {missing} not in pinned contract")
    return {**context["claim_extraction_contract"], "bytes": len(data), "git_blob_sha1": git_blob_sha1(data)}


def build(context: dict, root: Path) -> dict:
    validate_context(context)
    rid = context["run"]["id"]
    dep = load_dependency(context, root)
    contract = check_contract(context, root)
    run = dep["run"]
    raw = run["raw_output_text"]
    parsed = standalone.parse(raw)
    output_sha = run["output_sha256"]
    written_by = {"audit_run_id": run["id"], "model": run["model"], "runner": run["runner"],
                  "historical_instrument": run["historical_instrument"]}
    records, statements = [], {}

    def statement(role: str, span: dict, suffix: str, extra_refs=()) -> dict:
        text = raw[span["char_start"]:span["char_end"]]
        text_sha = sha256(text.encode("utf-8"))
        item = record("ClaimStatement", f"{rid}/statement/{suffix}/{text_sha[:16]}",
                      claim_link_run_id=rid, role=role, exact_text=text, exact_text_sha256=text_sha,
                      normalized_text=normalize(text), normalizer=NORMALIZER,
                      anchor={"output_sha256": output_sha, "first_line": span["line_start"],
                              "last_line_inclusive": span["line_end"], "char_start": span["char_start"],
                              "char_end": span["char_end"], "char_unit": "unicode_codepoint",
                              "char_interval": "half_open"},
                      written_by=written_by, statement_kind="AUDIT_OUTPUT_TEXT",
                      refs=[rid, run["id"], *extra_refs])
        records.append(item)
        return item

    def comparison(a: dict, b: dict, name: str) -> dict:
        exact, normalized, result = compare(a, b)
        item = record("TextComparison", f"{rid}/compare/{name}", claim_link_run_id=rid,
                      subject_id=a["id"], object_id=b["id"], exact_match=exact,
                      normalized_match=normalized, result=result,
                      semantic_equivalence="NOT_ASSESSED_IDENTICAL_TEXT" if exact else "UNASSESSED",
                      basis=f"DETERMINISTIC_TEXT_COMPARISON; {NORMALIZER}; no semantic judgment",
                      refs=[rid, a["id"], b["id"]])
        records.append(item)
        return item

    for number, item in parsed["map"]["fields"].items():
        if number in standalone.FALLBACK_FIELDS:
            statements[f"MAP_FIELD_{number}"] = statement(f"MAP_FIELD_{number}", item, f"map-field-{number}")
    for key, item in parsed["confirmation"]["items"].items():
        role = "CONFIRMATION_TARGET_LAYER" if key == "target_layer" else f"CONFIRMATION_{key.upper()}"
        statements[role] = statement(role, item, f"confirmation-{key.replace('_', '-')}")
    for number in standalone.FALLBACK_FIELDS:
        a, b = statements.get(f"MAP_FIELD_{number}"), statements.get(f"CONFIRMATION_FIELD_{number}")
        if a and b:
            comparison(a, b, f"map-field-{number}~confirmation-field-{number}")

    map_state = parsed["map"]["state"]
    claim_map_id = f"{rid}/claim-map"
    present = sorted(parsed["map"]["fields"]) if map_state == "PRESENT" else []
    absent = {}
    for field in CONTRACT_ROWS:
        if field in present:
            continue
        if map_state == "PRESENT" and field not in standalone.FALLBACK_FIELDS:
            absent[field] = "NOT_IN_STANDALONE_FALLBACK: the instrument defines only fields 1, 3 and 6"
        elif map_state == "PRESENT":
            absent[field] = "FALLBACK_FIELD_NOT_FOUND_IN_OUTPUT"
        else:
            absent[field] = "NO_CLAIM_MAP_IN_OUTPUT"
    records.append(record(
        "ClaimMap", claim_map_id, claim_link_run_id=rid, state=map_state,
        producer={"instrument": "citation-network", "mode": "DEGRADED_STANDALONE" if map_state == "PRESENT" else None,
                  "native_label": parsed["map"]["native_label"], "heading_line": parsed["map"]["heading_line"],
                  "standalone_warning": parsed["warning"],
                  "claim_extraction_output": False,
                  "note": ("Self-generated by the auditing run; not produced by the claim-extraction "
                           "instrument and not equivalent to an upstream map.")},
        compared_contract={"path": contract["path"], "sha256": contract["sha256"],
                           "git_blob_sha1": contract["git_blob_sha1"], "fields": list(CONTRACT_ROWS)},
        fields_present=present, fields_absent=absent,
        claim_inventory="NOT_PRODUCED",
        field_statement_ids={f: statements[f"MAP_FIELD_{f}"]["id"] for f in present
                             if f"MAP_FIELD_{f}" in statements},
        confirmation={"state": parsed["confirmation"]["state"],
                      "heading_line": parsed["confirmation"]["heading_line"]},
        reconciliation=("NOT_PERFORMED: the instrument requires reconciliation against an upstream map "
                        "before combining this audit with others" if map_state == "PRESENT"
                        else "NOT_APPLICABLE: no map in output"),
        parse_issues=parsed["issues"], output_map_gap_lines=parsed["map_gap_lines"],
        refs=[rid, run["id"], *[statements[f"MAP_FIELD_{f}"]["id"] for f in present
                                if f"MAP_FIELD_{f}" in statements]]))

    # Reviews: structured evidence reviews bind to a span of one finding field.
    review_scopes: dict[str, list[dict]] = {}
    for item in sorted((r for r in dep["records"] if r["type"] == "ReviewDecision"
                        and r["id"].startswith(f"{run['id']}/review/")), key=lambda r: r["id"]):
        structured = "review_schema" in item
        target = item["review"]["target"] if structured else None
        finding_id = f"{run['id']}/finding/{target['finding_number']}" if structured else None
        if finding_id and finding_id not in dep["by_id"]:
            finding_id = None
        reviewed_field = target["proposition_field"] if structured else None
        on_target = reviewed_field == "Target claim"
        scope = record(
            "ReviewScope", f"{rid}/review-scope/{item['id'].rsplit('/review/', 1)[1]}",
            claim_link_run_id=rid, review_id=item["id"], binding=item["target_binding"],
            finding_id=finding_id if item["target_binding"] == "MATCH" else None,
            declared_finding_number=target["finding_number"] if structured else None,
            reviewed_field=reviewed_field,
            reviewed_span=[target["proposition_start"], target["proposition_end"]] if structured else None,
            proposition=target["proposition"] if structured else None,
            parts=[{"part": p["part"], "text": p["text"], "disposition": p["disposition"]}
                   for p in item["review"]["part_dispositions"]] if structured else [],
            disposition=item["imported_disposition"],
            reviewer=({"identity": item["review"]["reviewer"]["identity"], "kind": item["review"]["reviewer"]["kind"]}
                      if structured else {"identity": item["reviewer"], "kind": "UNSTRUCTURED"}),
            exposure=item["exposure"], independence=item["independence"],
            human_adjudication=item["human_adjudication"],
            relation_to_finding_target=("REVIEWS_TARGET_CLAIM_FIELD" if on_target else
                                        "DOES_NOT_REVIEW_TARGET_CLAIM" if structured else
                                        "UNSTRUCTURED_REVIEW_NO_SPAN"),
            relation_to_audited_claim=("NOT_BOUND_TO_CLAIM_MAP: review schema binds finding fields only"
                                       if structured else "UNSTRUCTURED_REVIEW_NO_SPAN"),
            dependency_record_sha256=digest(item),
            refs=[rid, item["id"], *([finding_id] if finding_id and item["target_binding"] == "MATCH" else [])])
        records.append(scope)
        key = finding_id or (f"{run['id']}/finding/{target['finding_number']}" if structured else None)
        if key:
            review_scopes.setdefault(key, []).append(scope)

    designated = statements.get("MAP_FIELD_6")
    confirmation = statements.get("CONFIRMATION_FIELD_6")
    alignment_ids, counts = [], {}
    findings = sorted((r for r in dep["records"] if r["type"] == "AuditFinding" and r["audit_run_id"] == run["id"]),
                      key=lambda r: int(r["id"].rsplit("/", 1)[1]))
    for finding in findings:
        ordinal = finding["id"].rsplit("/", 1)[1]
        native = finding["native"]
        value = native["fields"].get("Target claim")
        target, comparisons, kind = None, [], "ABSENT"
        if value is not None:
            span = standalone.locate_cell(raw, native["field_lines"]["Target claim"], value)
            if span is None:
                raise ContractError(f"TARGET_SPAN_UNRESOLVED: {finding['id']}")
            target = statement("FINDING_TARGET_CLAIM", span, f"finding-{ordinal}-target", [finding["id"]])
            if value.startswith("MAP GAP:"):
                kind = "MAP_GAP_DECLARED"
            elif FIELD_6_REFERENCE.match(value):
                kind = "FIELD_6_REFERENCE"
            else:
                kind = "TEXT"
        if kind == "TEXT":
            for other, name in ((designated, "map-field-6"), (confirmation, "confirmation-field-6")):
                if other:
                    comparisons.append(comparison(target, other, f"finding-{ordinal}-target~{name}"))
        if kind == "ABSENT":
            identity = "NO_TARGET_STATED"
        elif kind == "MAP_GAP_DECLARED":
            identity = "DECLARED_NOT_ON_MAP"
        elif kind == "FIELD_6_REFERENCE":
            qualifier = FIELD_6_REFERENCE.match(value).group(1).strip()
            identity = "UNRESOLVED_REQUIRES_REVIEW" if qualifier else "DECLARED_BY_REFERENCE"
        else:
            vs_designated = comparisons[0]["result"] if designated else None
            identity = {"MATCH": "SAME_TEXT", "NORMALIZED_MATCH_ONLY": "SAME_TEXT_AFTER_NORMALIZATION"}.get(
                vs_designated, "UNRESOLVED_REQUIRES_REVIEW")
        counts[identity] = counts.get(identity, 0) + 1
        mentions = [{"field": f, "text": v, "line": native["field_lines"].get(f),
                     "basis": "DOCUMENTED_IN_OUTPUT; the output's own words, not a verified relation"}
                    for f, v in sorted(native["fields"].items())
                    if f != "Target claim" and re.search(r"\bfield 6\b", v, re.IGNORECASE)]
        scopes = review_scopes.get(finding["id"], [])
        attached = [s["id"] for s in scopes if s["binding"] == "MATCH"]
        detached = [s["id"] for s in scopes if s["binding"] != "MATCH"]
        aid = f"{rid}/alignment/finding-{ordinal}"
        alignment_ids.append(aid)
        records.append(record(
            "TargetAlignment", aid, claim_link_run_id=rid, finding_id=finding["id"],
            finding_number=str(native["number"]), target_kind=kind,
            designated_target_id=designated["id"] if designated else None,
            designated_target_state=("MAP_FIELD_6_IN_OUTPUT" if designated else
                                     "FIELD_6_TEXT_NOT_IN_INPUTS"),
            finding_target_id=target["id"] if target else None,
            comparison_ids=[c["id"] for c in comparisons], claim_identity=identity,
            native_field_6_mentions=mentions, reviewer_decomposition_ids=attached,
            detached_review_ids=detached, finding_import_status=finding["import_status"],
            finding_assessment=finding["assessment"],
            layers={"paper_statement": "see ClaimLinkRun.source_statement",
                    "audited_claim": designated["id"] if designated else None,
                    "finding_target": target["id"] if target else None,
                    "reviewer_decompositions": attached},
            refs=[rid, finding["id"], *([designated["id"]] if designated else []),
                  *([target["id"]] if target else []), *[c["id"] for c in comparisons], *attached, *detached]))

    target_work = run["target_work_id"]
    reads = sorted({r["state"] for r in dep["records"]
                    if r["type"] == "SourceReadReceipt" and r["audit_run_id"] == run["id"]
                    and r["work_id"] == target_work})
    reasons = []
    if "2" not in present:
        reasons.append(f"claim-map field 2 (source's strongest claim): {absent.get('2')}")
    reasons.append(f"target work {target_work} read state(s) in dependency: {', '.join(reads) or 'NONE_RECORDED'}")
    records.append(record(
        "ClaimLinkRun", rid, operator=context["run"]["operator"], purpose=context["run"]["purpose"],
        dependency={"audit_run_id": run["id"], "output_sha256": output_sha, "syntax": run["syntax"],
                    "producing_instrument_compliance": run["producing_instrument_compliance"],
                    "finding_import_statuses": sorted({f["import_status"] for f in findings}),
                    "native_projection": dep["native_projection"],
                    "manifest_record_id": dep["manifest"]["id"], **dep["pins"]},
        method=("Deterministic: parse the output's own claim statements, compare their text "
                "exactly and after nfc-whitespace/2 normalization, and record review bindings. "
                "No model, no retrieval, no semantic judgment."),
        source_statement={"state": "NOT_AVAILABLE", "reasons": reasons},
        claim_map_id=claim_map_id, alignment_ids=alignment_ids, counts=dict(sorted(counts.items())),
        refs=[run["id"], dep["manifest"]["id"], target_work]))

    external = set(dep["by_id"])
    shared = {name: sha256((PACKAGE.parent / name).read_bytes()) for name in SHARED_MODULES}
    own = {p.name: sha256(p.read_bytes()) for p in sorted(PACKAGE.glob("*.py"))}
    body = list(records)
    manifest = record(
        "ClaimLinkManifest", f"{rid}/manifest", claim_link_run_id=rid,
        executor={"name": "atlas-claimlink", "version": VERSION, "code_sha256": own,
                  "shared_code_sha256": shared},
        parser={"name": standalone.NAME, "version": standalone.VERSION,
                "code_sha256": sha256(Path(standalone.__file__).read_bytes())},
        normalizer=NORMALIZER, input_context=context,
        declared_input_receipts=[*dep["inputs"], {k: contract[k] for k in ("path", "sha256", "bytes")}],
        dependency={"audit_run_id": run["id"], "manifest_record_id": dep["manifest"]["id"],
                    "adapter": dep["manifest"]["adapter"]["version"], "schema": run["schema_version"],
                    "native_projection": dep["native_projection"], **dep["pins"]},
        environment={"implementation": platform.python_implementation(),
                     "python": platform.python_version(), "unicode": unicodedata.unidata_version},
        execution={"models_invoked": [], "network": "NOT_USED; no OS-level network sandbox is claimed",
                   "semantic_judgment": "NONE", "scope": "deterministic linking of frozen records"},
        record_ids=sorted(r["id"] for r in body),
        records_before_manifest_sha256=sha256(jsonl(body)),
        refs=[rid])
    records.append(manifest)
    validate(records, external)
    payload = jsonl(records)
    return {"records": records, "jsonl": payload, "manifest": manifest, "dependency_ids": external,
            "jsonl_sha256": sha256(payload)}


def without_environment(item: dict) -> dict:
    return {k: v for k, v in item.items() if not (item["type"] == "ClaimLinkManifest" and k == "environment")}


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
        validate(stored, bundle["dependency_ids"])
    except ContractError as exc:
        raise ContractError(f"REPLAY_MISMATCH: records: {exc}") from exc
    differing = []
    old = {r["id"]: without_environment(r) for r in stored}
    new = {r["id"]: without_environment(r) for r in bundle["records"]}
    changed = sorted(i for i in old.keys() | new.keys() if old.get(i) != new.get(i))
    if changed:
        differing.append("records: " + ", ".join(changed))
    fresh = bundle["manifest"]
    if without_environment(manifest) != without_environment(fresh):
        differing.append("manifest")
    delta = {k: {"recorded": manifest.get("environment", {}).get(k), "replayed": fresh["environment"].get(k)}
             for k in sorted(manifest.get("environment", {}).keys() | fresh["environment"].keys())
             if manifest.get("environment", {}).get(k) != fresh["environment"].get(k)}
    if level == "strict":
        if delta:
            differing.append("environment: " + ", ".join(delta))
        if not differing and bundle["jsonl"] != jsonl_bytes:
            differing.append("bytes")
    if differing:
        raise ContractError(f"REPLAY_MISMATCH ({level}): " + "; ".join(differing))
    return {"replay": "PASS", "level": level, "environment_delta": delta,
            "scope": "deterministic claim-link replay; no model run reproduced"}
