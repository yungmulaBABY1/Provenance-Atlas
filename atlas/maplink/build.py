"""Build, validate and replay a map-link bundle over one pinned claim-link bundle and one upstream map."""

from __future__ import annotations

from pathlib import Path
import platform
import re
import unicodedata

from . import CONTEXT_SCHEMA, SCHEMA, VERSION
from ..claims import link as claimlink
from ..contract import NORMALIZER, ContractError, canonical, load_json, normalize, read_artifact, require, sha256
from ..extraction import output as stage1

PACKAGE = Path(__file__).parent
# Modules this executor reads with (including the claim-link replay it runs); their
# bytes are part of its identity.
SHARED_MODULES = ("__init__.py", "adapter.py", "contract.py", "integrity.py", "native.py", "reviews.py",
                  "sources.py", "ledger.py", "claims/__init__.py", "claims/link.py", "claims/standalone.py",
                  "extraction/__init__.py", "extraction/output.py")

TYPES = {"MapLinkRun", "UpstreamMap", "MapStatement", "TextComparison", "Reconciliation", "TargetAlignment",
         "MapLinkManifest"}
FIELDS = {
    "MapLinkRun": {"operator": str, "purpose": str, "recorded_by": str, "dependency": dict, "upstream_map_id": str,
                   "source_statement": dict, "reconciliation_ids": list, "alignment_ids": list, "counts": dict,
                   "method": str},
    "UpstreamMap": {"map_link_run_id": str, "origin": str, "provenance": dict, "output": dict, "instrument": dict,
                    "preflight": dict, "work": dict, "audit_output_reference": dict, "fields": dict,
                    "designated_field_6_id": (str, type(None)), "anchors": dict, "parse_issues": list},
    "MapStatement": {"map_link_run_id": str, "field": str, "role": str, "text": str, "text_sha256": str,
                     "normalized_text": str, "anchor": dict, "status": str, "statement_kind": str,
                     "written_by": dict, "producer_verification_state": (str, type(None))},
    "TextComparison": {"map_link_run_id": str, "subject_id": str, "object_id": str, "exact_match": bool,
                       "normalized_match": bool, "result": str, "semantic_equivalence": str, "basis": str},
    "Reconciliation": {"map_link_run_id": str, "field": str, "audit_output_statement_id": (str, type(None)),
                       "map_statement_id": (str, type(None)), "comparison_id": (str, type(None)), "state": str,
                       "claim_identity": str},
    "TargetAlignment": {"map_link_run_id": str, "finding_id": str, "finding_number": str,
                        "claim_link_alignment_id": str, "claim_link_identity": str, "target_kind": str,
                        "map_gap_form": (str, type(None)), "finding_target_id": (str, type(None)),
                        "designated_target_id": (str, type(None)), "comparison_ids": list,
                        "field_mentions": list, "claim_identity": str},
    "MapLinkManifest": {"map_link_run_id": str, "executor": dict, "parser": dict, "normalizer": str,
                        "input_context": dict, "declared_input_receipts": list, "dependency": dict,
                        "environment": dict, "execution": dict, "record_ids": list,
                        "records_before_manifest_sha256": str},
}
IDENTITIES = {"SAME_TEXT", "SAME_TEXT_AFTER_NORMALIZATION", "DECLARED_BY_REFERENCE", "DECLARED_NOT_FIELD_6",
              "DECLARED_NOT_ON_MAP", "UNRESOLVED_REQUIRES_REVIEW", "NO_TARGET_STATED"}
LABELS = {
    ("TextComparison", "result"): {"MATCH", "NORMALIZED_MATCH_ONLY", "MISMATCH"},
    ("TextComparison", "semantic_equivalence"): {"NOT_ASSESSED_IDENTICAL_TEXT", "UNASSESSED"},
    ("MapStatement", "status"): {"USABLE", "NOT_USABLE"},
    ("MapStatement", "statement_kind"): {"UPSTREAM_MAP_TEXT"},
    ("UpstreamMap", "origin"): {"UPSTREAM_STAGE_1_OUTPUT"},
    ("Reconciliation", "state"): {"TEXT_COMPARED", "NOT_COMPARABLE_AUDIT_OUTPUT_STATEMENT_MISSING",
                                  "NOT_COMPARABLE_MAP_STATEMENT_MISSING"},
    ("Reconciliation", "claim_identity"): {"SAME_TEXT", "SAME_TEXT_AFTER_NORMALIZATION",
                                           "UNRESOLVED_REQUIRES_REVIEW", "NOT_COMPARABLE"},
    ("TargetAlignment", "target_kind"): {"TEXT", "FIELD_6_REFERENCE", "MAP_GAP_DECLARED", "ABSENT"},
    ("TargetAlignment", "map_gap_form"): {None, "NOT_FIELD_6", "NOT_ON_MAP", "WORDING_DIFFERS_FROM_INSTRUMENT_FORMS"},
    ("TargetAlignment", "claim_identity"): IDENTITIES,
}
PRODUCER_KINDS = {"MODEL_AGENT", "PERSON", "UNKNOWN"}
# No record may carry a judgment of the audit, the paper or the map.
FORBIDDEN_KEYS = {"score", "scores", "verdict", "rating", "ratings", "credibility", "trust", "trust_score",
                  "consensus", "confidence_score", "weight", "rank", "stance", "position"}
IDENTITY_FROM_RESULT = {"SAME_TEXT": "MATCH", "SAME_TEXT_AFTER_NORMALIZATION": "NORMALIZED_MATCH_ONLY"}
RESULT_TO_IDENTITY = {"MATCH": "SAME_TEXT", "NORMALIZED_MATCH_ONLY": "SAME_TEXT_AFTER_NORMALIZATION",
                      "MISMATCH": "UNRESOLVED_REQUIRES_REVIEW"}
# The citation-network instrument's two MAP GAP forms (2-citation-network.txt), matched as written.
GAP_NOT_FIELD_6 = re.compile(r"MAP GAP: this finding targets (.+), not map field 6\.", re.DOTALL)
GAP_NOT_ON_MAP = re.compile(r"MAP GAP: this finding concerns (.+), which does not appear on the claim map\."
                            r"(?: The map may be incomplete\.)?", re.DOTALL)
FIELD_MENTION = re.compile(r"\bmap field (1|2|3|4|5A|5B|6)\b")
BLOB_NAMED = re.compile(r"\bblob(?:/hash)? ([0-9a-f]{40})\b")
SHA256_NAMED = re.compile(r"\bsha256 ([0-9a-f]{64})\b")
# Audit-output restatements (atlas.claims roles) reconciled against map statements.
RECONCILE = (("1", "CONFIRMATION_FIELD_1", "TABLE_FIELD_1"), ("3", "CONFIRMATION_FIELD_3", "TABLE_FIELD_3"),
             ("6", "CONFIRMATION_FIELD_6", "FIELD_6_SECTION"))


def record(record_type: str, id: str, **fields) -> dict:
    if record_type not in TYPES:
        raise ContractError(f"UNKNOWN_RECORD_TYPE: {record_type}")
    return {"schema_version": SCHEMA, "type": record_type, "id": id, **fields}


def jsonl(records: list[dict]) -> bytes:
    return ("\n".join(canonical(r) for r in sorted(records, key=lambda r: r["id"])) + "\n").encode("utf-8")


def forbidden_keys(node, path: str = "") -> list[str]:
    found = []
    if isinstance(node, dict):
        for key, value in node.items():
            if key in FORBIDDEN_KEYS:
                found.append(f"{path}.{key}".lstrip("."))
            found.extend(forbidden_keys(value, f"{path}.{key}"))
    elif isinstance(node, list):
        for index, value in enumerate(node):
            found.extend(forbidden_keys(value, f"{path}[{index}]"))
    return found


def validate_context(context: dict) -> None:
    require(context, {"schema_version": str, "run": dict, "claim_link_bundle": dict, "upstream_map": dict}, "context")
    if context["schema_version"] != CONTEXT_SCHEMA:
        raise ContractError("UNSUPPORTED_SCHEMA")
    require(context["run"], {"id": str, "operator": str, "purpose": str, "recorded_by": str}, "run")
    require(context["claim_link_bundle"], {"claim_link_run_id": str, "manifest": dict, "records": dict},
            "claim_link_bundle")
    up = context["upstream_map"]
    require(up, {"output": dict, "instrument": dict, "work_id": str, "producer": dict, "declared_by": str,
                 "basis": str}, "upstream_map")
    require(up["producer"], {"kind": str, "identity": str, "verification": str}, "upstream_map.producer")
    if up["producer"]["kind"] not in PRODUCER_KINDS:
        raise ContractError(f"INVALID_LABEL: upstream_map.producer.kind={up['producer']['kind']}")
    # 0.1 covers maps with no run receipt. A receipted Stage-1 run belongs in atlas.extraction.
    if up.get("run_prompt") is not None or up.get("run_receipt") is not None:
        raise ContractError("RECEIPTED_RUN_NOT_SUPPORTED: record a receipted Stage-1 run with atlas.extraction")


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
        bad = forbidden_keys(item)
        if bad:
            raise ContractError(f"JUDGMENT_FIELD_NOT_ALLOWED: {item['id']}: {', '.join(bad)}")
        for key, kind in FIELDS[item["type"]].items():
            kinds = kind if isinstance(kind, tuple) else (kind,)
            if key not in item or type(item[key]) not in kinds:
                raise ContractError(f"INVALID_CONTRACT: {item['type']}.{key}: {item['id']}")
        for (rtype, key), allowed in LABELS.items():
            if item["type"] == rtype and item[key] not in allowed:
                raise ContractError(f"INVALID_LABEL: {rtype}.{key}={item[key]}")
        if len(item["refs"]) != len(set(item["refs"])):
            raise ContractError(f"INVALID_CONTRACT: duplicate refs: {item['id']}")
        for ref in item["refs"]:
            if ref not in by_id and ref not in external_ids:
                raise ContractError(f"UNRESOLVED_REFERENCE: {item['id']} -> {ref}")
        kind = item["type"]
        if kind == "MapStatement":
            if sha256(item["text"].encode("utf-8")) != item["text_sha256"]:
                raise ContractError(f"STATEMENT_HASH_MISMATCH: {item['id']}")
            if item["written_by"].get("producer", {}).get("kind") not in PRODUCER_KINDS:
                raise ContractError(f"UNATTRIBUTED_MAP_STATEMENT: {item['id']}")
        if kind == "UpstreamMap":
            prov = item["provenance"]
            if prov.get("run_prompt") != "NOT_RECORDED" or prov.get("run_receipt") != "NONE":
                raise ContractError(f"INVALID_LABEL: upstream map provenance must state NOT_RECORDED / NONE: {item['id']}")
        if kind == "TextComparison":
            expected = ("MATCH" if item["exact_match"] else
                        "NORMALIZED_MATCH_ONLY" if item["normalized_match"] else "MISMATCH")
            if item["result"] != expected or (item["exact_match"] and not item["normalized_match"]):
                raise ContractError(f"INVALID_LABEL: comparison contradicts its match fields: {item['id']}")
        if kind == "Reconciliation":
            comp = by_id.get(item["comparison_id"]) if item["comparison_id"] else None
            if item["state"] == "TEXT_COMPARED":
                if not comp or comp["subject_id"] != item["audit_output_statement_id"] \
                        or comp["object_id"] != item["map_statement_id"] \
                        or RESULT_TO_IDENTITY[comp["result"]] != item["claim_identity"]:
                    raise ContractError(f"UNSUPPORTED_IDENTITY: {item['id']}")
            elif comp or item["claim_identity"] != "NOT_COMPARABLE":
                raise ContractError(f"INVALID_LABEL: {item['id']} not comparable but carries a comparison")
        if kind == "TargetAlignment":
            identity, form = item["claim_identity"], item["map_gap_form"]
            designated = by_id.get(item["designated_target_id"]) if item["designated_target_id"] else None
            if item["designated_target_id"] and (designated is None or designated.get("role") != "FIELD_6_SECTION"
                                                 or designated.get("status") != "USABLE"):
                raise ContractError(f"INELIGIBLE_LINK_TARGET: {item['id']}")
            if (item["target_kind"] == "MAP_GAP_DECLARED") != (form is not None):
                raise ContractError(f"INVALID_LABEL: map gap form without a MAP GAP target: {item['id']}")
            if identity in IDENTITY_FROM_RESULT:
                backing = [by_id.get(c, {}) for c in item["comparison_ids"]]
                if not designated or item["target_kind"] != "TEXT" or not any(
                        c.get("subject_id") == item["finding_target_id"] and c.get("object_id") == designated["id"]
                        and c.get("result") == IDENTITY_FROM_RESULT[identity] for c in backing):
                    raise ContractError(f"UNSUPPORTED_IDENTITY: {item['id']} {identity}")
            expected_by_form = {"NOT_FIELD_6": "DECLARED_NOT_FIELD_6", "NOT_ON_MAP": "DECLARED_NOT_ON_MAP",
                                "WORDING_DIFFERS_FROM_INSTRUMENT_FORMS": "UNRESOLVED_REQUIRES_REVIEW"}
            if form is not None and identity != expected_by_form[form]:
                raise ContractError(f"UNSUPPORTED_IDENTITY: {item['id']} {identity} for gap form {form}")
            if identity in ("DECLARED_NOT_FIELD_6", "DECLARED_NOT_ON_MAP") and form is None:
                raise ContractError(f"UNSUPPORTED_IDENTITY: {item['id']} {identity} without a MAP GAP declaration")
            if identity == "DECLARED_BY_REFERENCE" and (item["target_kind"] != "FIELD_6_REFERENCE" or not designated):
                raise ContractError(f"UNSUPPORTED_IDENTITY: {item['id']} {identity}")
            for mention in item["field_mentions"]:
                if mention.get("relation") != "MENTIONED_IN_DECLARED_TARGET; not resolved as the target":
                    raise ContractError(f"INVALID_LABEL: field mention treated as a target: {item['id']}")
    manifests = [r for r in records if r["type"] == "MapLinkManifest"]
    if len(manifests) != 1:
        raise ContractError("INVALID_MANIFEST_COVERAGE: exactly one MapLinkManifest required")
    body = [r for r in records if r is not manifests[0]]
    if manifests[0]["record_ids"] != sorted(r["id"] for r in body):
        raise ContractError("INVALID_MANIFEST_COVERAGE: manifest does not list exactly the bundle records")
    if sha256(jsonl(body)) != manifests[0]["records_before_manifest_sha256"]:
        raise ContractError("MANIFEST_RECORD_HASH_MISMATCH")


def load_claim_link(context: dict, root: Path) -> dict:
    """Read the pinned claim-link receipt, re-derive it by content replay, and load its import."""
    pins = context["claim_link_bundle"]
    manifest_bytes = read_artifact(root, pins["manifest"])
    records_bytes = read_artifact(root, pins["records"])
    try:
        claimlink.replay(manifest_bytes, records_bytes, root, "content")
    except ContractError as exc:
        raise ContractError(f"CLAIM_LINK_RECEIPT_NOT_VERIFIED: {exc}") from exc
    records = [load_json(line) for line in records_bytes.splitlines() if line.strip()]
    by_id = {r["id"]: r for r in records}
    manifest = load_json(manifest_bytes)
    run = by_id.get(pins["claim_link_run_id"])
    if run is None or run["type"] != "ClaimLinkRun" or by_id.get(manifest.get("id")) != manifest:
        raise ContractError("CLAIM_LINK_MANIFEST_MISMATCH: pinned files are not this claim-link run's receipt")
    dep = claimlink.load_dependency(manifest["input_context"], root)
    return {"records": records, "by_id": by_id, "run": run, "manifest": manifest, "dep": dep,
            "inputs": [{**pins["manifest"], "bytes": len(manifest_bytes)},
                       {**pins["records"], "bytes": len(records_bytes)}],
            "pins": {"manifest_sha256": sha256(manifest_bytes), "records_sha256": sha256(records_bytes)}}


def lines_naming(text: str, needle: str) -> list[int]:
    return [i + 1 for i, line in enumerate(text.split("\n")) if needle in line]


def build(context: dict, root: Path) -> dict:
    validate_context(context)
    rid = context["run"]["id"]
    cl = load_claim_link(context, root)
    dep, cl_by_id = cl["dep"], cl["by_id"]
    audit_run = dep["run"]
    cmap = cl_by_id[cl["run"]["claim_map_id"]]
    if cmap["state"] != "ABSENT":
        raise ContractError(f"OUTPUT_HAS_ITS_OWN_MAP: claim-link map state {cmap['state']}; "
                            "0.1 links only outputs that carry no map")

    up = context["upstream_map"]
    if up["work_id"] != audit_run["target_work_id"]:
        raise ContractError(f"UPSTREAM_MAP_TARGET_MISMATCH: {up['work_id']} != {audit_run['target_work_id']}")
    contract_pin = cl["manifest"]["input_context"]["claim_extraction_contract"]
    if up["instrument"] != contract_pin:
        raise ContractError("CONTRACT_PIN_MISMATCH: the map's instrument is not the contract the claim links used")
    contract = claimlink.check_contract({"claim_extraction_contract": up["instrument"]}, root)
    map_bytes = read_artifact(root, up["output"])
    map_text = map_bytes.decode("utf-8")
    map_sha = up["output"]["sha256"]
    parsed = stage1.parse(map_text)

    # What each file says about the other, found in their own text.
    pre = parsed["preflight"]
    pre_text = pre["text"] if pre else ""
    blob = BLOB_NAMED.search(pre_text)
    sha = SHA256_NAMED.search(pre_text)
    preflight = {"line": pre["line"] if pre else None, "text": pre_text or None,
                 "disposition": pre["disposition"] if pre else None,
                 "blob_named": ("NOT_NAMED" if not blob else
                                "NAMED_MATCHES_PINNED_INSTRUMENT" if blob.group(1) == contract["git_blob_sha1"]
                                else "NAMED_DIFFERS_FROM_PINNED_INSTRUMENT"),
                 "sha256_named": ("NOT_NAMED" if not sha else
                                  "NAMED_MATCHES_PINNED_INSTRUMENT" if sha.group(1) == contract["sha256"]
                                  else "NAMED_DIFFERS_FROM_PINNED_INSTRUMENT"),
                 "basis": "The map's own preflight line compared with the pinned instrument's hashes. "
                          "It shows which file the map says it used, not that the run used it."}
    doi = up["work_id"].split(":", 1)[1] if up["work_id"].startswith("doi:") else up["work_id"]
    doi_lines = lines_naming(map_text, doi)
    work = {"work_id": up["work_id"], "audit_target_work_id": audit_run["target_work_id"],
            "named_in_map": "NAMED" if doi_lines else "NOT_NAMED", "lines": doi_lines}
    ref_lines = lines_naming(audit_run["raw_output_text"], up["output"]["path"])
    audit_ref = {"state": "PATH_NAMED_IN_AUDIT_OUTPUT" if ref_lines else "NOT_NAMED_LINK_DECLARED_IN_CONTEXT_ONLY",
                 "lines": ref_lines, "audit_output_sha256": audit_run["output_sha256"],
                 "basis": ("DOCUMENTED: the audit output names this file as its upstream map"
                           if ref_lines else f"DECLARED by {up['declared_by']}: {up['basis']}")}

    records = []
    written_by = {"producer": up["producer"], "basis": "DECLARED_IN_CONTEXT", "declared_by": up["declared_by"],
                  "run_prompt": "NOT_RECORDED", "run_receipt": "NONE"}
    map_id = f"{rid}/upstream-map"

    def statement(field: str, role: str, item: dict | None, status: str, state: str | None) -> dict | None:
        if not item:
            return None
        text = item["text"]
        result = record("MapStatement", f"{rid}/map-statement/{role.lower().replace('_', '-')}", map_link_run_id=rid,
                        field=field, role=role, text=text, text_sha256=sha256(text.encode("utf-8")),
                        normalized_text=normalize(text), normalizer=NORMALIZER,
                        anchor={"output_path": up["output"]["path"], "output_sha256": map_sha, "line": item["line"],
                                "char_start": item["char_start"], "char_end": item["char_end"],
                                "char_unit": "unicode_codepoint", "char_interval": "half_open"},
                        status="USABLE" if status == "USABLE" else "NOT_USABLE", statement_kind="UPSTREAM_MAP_TEXT",
                        written_by=written_by, producer_verification_state=state, refs=[rid, map_id])
        records.append(result)
        return result

    def comparison(a: dict, b: dict, name: str) -> dict:
        exact, normalized, result = claimlink.compare(
            {"exact_text": a.get("exact_text", a.get("text")), "normalized_text": a["normalized_text"]},
            {"exact_text": b.get("exact_text", b.get("text")), "normalized_text": b["normalized_text"]})
        item = record("TextComparison", f"{rid}/compare/{name}", map_link_run_id=rid, subject_id=a["id"],
                      object_id=b["id"], exact_match=exact, normalized_match=normalized, result=result,
                      semantic_equivalence="NOT_ASSESSED_IDENTICAL_TEXT" if exact else "UNASSESSED",
                      basis=f"DETERMINISTIC_TEXT_COMPARISON; {NORMALIZER}; no semantic judgment",
                      refs=[rid, a["id"], b["id"]])
        records.append(item)
        return item

    # The map's statements: every table field, the Field 6 section statement, the one-line summary.
    by_role, fields = {}, {}
    for field in stage1.TABLE_ROWS:
        row = parsed["table"].get(field)
        role = f"TABLE_FIELD_{field}"
        item = statement(field, role, row["content"] if row else None, row["status"] if row else "MISSING",
                         row["verification_state"]["text"] if row else None)
        if item:
            by_role[role] = item
        fields[field] = ({"native_label": row["native_label"], "instrument_label": row["instrument_label"],
                          "label_status": row["label_status"], "status": row["status"], "statement_id": item["id"]}
                         if row else {"status": "MISSING", "statement_id": None})
    section = parsed["field_6_section"]
    designated = statement("6", "FIELD_6_SECTION", section, section["status"] if section else "MISSING", None)
    summary = statement("6", "SUMMARY_CLAIM_UNDER_AUDIT", parsed["summaries"].get("CLAIM UNDER AUDIT"), "USABLE", None)
    if designated:
        by_role["FIELD_6_SECTION"] = designated
        for other in (by_role.get("TABLE_FIELD_6"), summary):
            if other:
                comparison(designated, other, f"map-field-6-section~{other['role'].lower().replace('_', '-')}")

    kinds = {}
    for entry in parsed["anchors"]:
        kinds[entry["kind"]] = kinds.get(entry["kind"], 0) + 1
    records.append(record(
        "UpstreamMap", map_id, map_link_run_id=rid, origin="UPSTREAM_STAGE_1_OUTPUT",
        provenance={"producer": up["producer"], "declared_by": up["declared_by"], "basis": up["basis"],
                    "run_prompt": "NOT_RECORDED", "run_receipt": "NONE",
                    "note": ("No run prompt or run receipt exists for this map. Its text is pinned by hash; "
                             "how it was produced rests on the producer's own account.")},
        output={**up["output"], "bytes": len(map_bytes)},
        instrument={"path": contract["path"], "sha256": contract["sha256"], "git_blob_sha1": contract["git_blob_sha1"]},
        preflight=preflight, work=work, audit_output_reference=audit_ref, fields=fields,
        designated_field_6_id=designated["id"] if designated else None,
        sections={k: v["sha256"] for k, v in sorted(parsed["sections"].items())},
        claim_inventory="PRESENT" if "CLAIM INVENTORY" in parsed["sections"] else "ABSENT",
        anchors={"count": len(parsed["anchors"]), "by_kind": dict(sorted(kinds.items())),
                 "verification": ("NOT_VERIFIED_IN_ATLAS: the source text is not among the committed inputs. "
                                  "Quotes in the map are the producer's transcription.")},
        parse_issues=parsed["issues"],
        refs=[rid, *[s["id"] for s in records if s["type"] == "MapStatement"]]))

    # Reconciliation: the audit output's restatement of map fields against the map's own text.
    statements_by_role = {r["role"]: r for r in cl["records"]
                          if r["type"] == "ClaimStatement" and r["field_status"] in claimlink.LINKABLE
                          and r["role"].startswith("CONFIRMATION_FIELD_")}
    reconciliation_ids, rec_counts = [], {}
    for field, audit_role, map_role in RECONCILE:
        audit_stmt, map_stmt = statements_by_role.get(audit_role), by_role.get(map_role)
        comp = comparison(audit_stmt, map_stmt, f"reconcile-field-{field}") if audit_stmt and map_stmt else None
        state = ("TEXT_COMPARED" if comp else
                 "NOT_COMPARABLE_AUDIT_OUTPUT_STATEMENT_MISSING" if not audit_stmt else
                 "NOT_COMPARABLE_MAP_STATEMENT_MISSING")
        identity = RESULT_TO_IDENTITY[comp["result"]] if comp else "NOT_COMPARABLE"
        rec_counts[identity] = rec_counts.get(identity, 0) + 1
        rec_id = f"{rid}/reconciliation/field-{field}"
        reconciliation_ids.append(rec_id)
        records.append(record(
            "Reconciliation", rec_id, map_link_run_id=rid, field=field,
            audit_output_statement_id=audit_stmt["id"] if audit_stmt else None,
            map_statement_id=map_stmt["id"] if map_stmt else None, comparison_id=comp["id"] if comp else None,
            state=state, claim_identity=identity,
            instrument_rule=("2-citation-network.txt: an audit must be reconciled against the upstream map "
                             "before it is combined with others. Only the text level is recorded here."),
            refs=[rid, *[x["id"] for x in (audit_stmt, map_stmt, comp) if x]]))

    # Findings: each target against the map's Field 6.
    alignment_ids, id_counts = [], {}
    alignments = sorted((r for r in cl["records"] if r["type"] == "TargetAlignment"),
                        key=lambda r: int(r["finding_number"]))
    for old in alignments:
        target = cl_by_id.get(old["finding_target_id"]) if old["finding_target_id"] else None
        text = target["exact_text"] if target else None
        kind, form, comparisons, mentions = old["target_kind"], None, [], []
        if kind == "TEXT" and designated:
            comparisons.append(comparison(target, designated, f"finding-{old['finding_number']}-target~map-field-6-section"))
        if kind == "MAP_GAP_DECLARED":
            gap = GAP_NOT_FIELD_6.fullmatch(text) or GAP_NOT_ON_MAP.fullmatch(text)
            form = ("NOT_FIELD_6" if GAP_NOT_FIELD_6.fullmatch(text) else
                    "NOT_ON_MAP" if GAP_NOT_ON_MAP.fullmatch(text) else "WORDING_DIFFERS_FROM_INSTRUMENT_FORMS")
            declared = gap.group(1) if gap else text
            for match in FIELD_MENTION.finditer(declared):
                if match.group(1) == "6" and form != "WORDING_DIFFERS_FROM_INSTRUMENT_FORMS":
                    continue
                stmt = by_role.get(f"TABLE_FIELD_{match.group(1)}")
                mentions.append({"field": match.group(1), "map_statement_id": stmt["id"] if stmt else None,
                                 "text_offset": match.start() + (gap.start(1) if gap else 0),
                                 "relation": "MENTIONED_IN_DECLARED_TARGET; not resolved as the target"})
        if kind == "ABSENT":
            identity = "NO_TARGET_STATED"
        elif kind == "MAP_GAP_DECLARED":
            identity = {"NOT_FIELD_6": "DECLARED_NOT_FIELD_6", "NOT_ON_MAP": "DECLARED_NOT_ON_MAP"}.get(
                form, "UNRESOLVED_REQUIRES_REVIEW")
        elif kind == "FIELD_6_REFERENCE":
            qualifier = claimlink.FIELD_6_REFERENCE.match(text).group(1).strip()
            identity = "DECLARED_BY_REFERENCE" if designated and not qualifier else "UNRESOLVED_REQUIRES_REVIEW"
        else:
            identity = RESULT_TO_IDENTITY[comparisons[0]["result"]] if comparisons else "UNRESOLVED_REQUIRES_REVIEW"
        id_counts[identity] = id_counts.get(identity, 0) + 1
        aid = f"{rid}/alignment/finding-{old['finding_number']}"
        alignment_ids.append(aid)
        mention_refs = [m["map_statement_id"] for m in mentions if m["map_statement_id"]]
        records.append(record(
            "TargetAlignment", aid, map_link_run_id=rid, finding_id=old["finding_id"],
            finding_number=old["finding_number"], claim_link_alignment_id=old["id"],
            claim_link_identity=old["claim_identity"], target_kind=kind, map_gap_form=form,
            finding_target_id=old["finding_target_id"], designated_target_id=designated["id"] if designated else None,
            comparison_ids=[c["id"] for c in comparisons], field_mentions=mentions, claim_identity=identity,
            refs=[rid, old["finding_id"], old["id"], *([old["finding_target_id"]] if old["finding_target_id"] else []),
                  *([designated["id"]] if designated else []), *[c["id"] for c in comparisons],
                  *dict.fromkeys(mention_refs)]))

    field_2 = by_role.get("TABLE_FIELD_2")
    records.append(record(
        "MapLinkRun", rid, operator=context["run"]["operator"], purpose=context["run"]["purpose"],
        recorded_by=context["run"]["recorded_by"],
        dependency={"claim_link_run_id": cl["run"]["id"], "claim_link_map_state": cmap["state"],
                    "audit_run_id": audit_run["id"], "import_records_sha256": dep["pins"]["records_sha256"],
                    **{f"claim_link_{k}": v for k, v in cl["pins"].items()}},
        upstream_map_id=map_id,
        source_statement={"state": "MAP_PRODUCER_RESTATEMENT_ONLY" if field_2 else "NOT_AVAILABLE",
                          "map_field_2_id": field_2["id"] if field_2 else None,
                          "note": ("Field 2 is the map producer's statement of the source's strongest claim. "
                                   "Quoted fragments in it are the producer's transcription; the source text "
                                   "is not among the committed inputs, so Atlas has not checked them.")},
        reconciliation_ids=reconciliation_ids, alignment_ids=alignment_ids,
        counts={"claim_identity": dict(sorted(id_counts.items())),
                "reconciliation": dict(sorted(rec_counts.items()))},
        method=("Deterministic: content-replay the claim-link receipt, parse the pinned Stage-1 output with "
                f"{stage1.NAME}/{stage1.VERSION}, compare text exactly and after {NORMALIZER} normalization, "
                "and classify MAP GAP declarations by the instrument's two forms. No model, no retrieval, "
                "no semantic judgment."),
        refs=[map_id, cl["run"]["id"], audit_run["id"], *reconciliation_ids, *alignment_ids]))

    external = set(cl_by_id) | set(dep["by_id"])
    shared = {name: sha256((PACKAGE.parent / name).read_bytes()) for name in SHARED_MODULES}
    own = {p.name: sha256(p.read_bytes()) for p in sorted(PACKAGE.glob("*.py"))}
    body = list(records)
    manifest = record(
        "MapLinkManifest", f"{rid}/manifest", map_link_run_id=rid,
        executor={"name": "atlas-maplink", "version": VERSION, "code_sha256": own, "shared_code_sha256": shared},
        parser={"name": stage1.NAME, "version": stage1.VERSION}, normalizer=NORMALIZER, input_context=context,
        declared_input_receipts=[*cl["inputs"], {**up["output"], "bytes": len(map_bytes)},
                                 {k: contract[k] for k in ("path", "sha256", "bytes")}],
        dependency={"claim_link_run_id": cl["run"]["id"], "audit_run_id": audit_run["id"], **cl["pins"],
                    "import_records_sha256": dep["pins"]["records_sha256"]},
        environment={"implementation": platform.python_implementation(), "python": platform.python_version(),
                     "unicode": unicodedata.unidata_version},
        execution={"models_invoked": [], "network": "NOT_USED; no OS-level network sandbox is claimed",
                   "semantic_judgment": "NONE", "claim_link_receipt": "CONTENT_REPLAYED_IN_THIS_BUILD",
                   "scope": "deterministic linking of frozen records and one pinned upstream map"},
        record_ids=sorted(r["id"] for r in body), records_before_manifest_sha256=sha256(jsonl(body)), refs=[rid])
    records.append(manifest)
    validate(records, external)
    payload = jsonl(records)
    return {"records": records, "jsonl": payload, "manifest": manifest, "external_ids": external,
            "jsonl_sha256": sha256(payload)}


def without_environment(item: dict) -> dict:
    return {k: v for k, v in item.items() if not (item["type"] == "MapLinkManifest" and k == "environment")}


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
    recorded, replayed = manifest.get("environment", {}), bundle["manifest"]["environment"]
    delta = {k: {"recorded": recorded.get(k), "replayed": replayed.get(k)}
             for k in sorted(recorded.keys() | replayed.keys()) if recorded.get(k) != replayed.get(k)}
    if level == "strict" and delta:
        differing.append("environment: " + ", ".join(delta))
    if level == "strict" and not differing and bundle["jsonl"] != jsonl_bytes:
        differing.append("bytes")
    if differing:
        raise ContractError(f"REPLAY_MISMATCH ({level}): " + "; ".join(differing))
    return {"replay": "PASS", "level": level, "environment_delta": delta,
            "scope": "deterministic map-link replay; no model run reproduced; the source is not read"}
