"""Build, validate and replay a research-question bundle from committed, pinned receipts."""

from __future__ import annotations

from pathlib import Path
import platform
import unicodedata

from . import CONTEXT_SCHEMA, SCHEMA, VERSION
from ..claims import link as claimlink
from ..contract import ContractError, canonical, digest, load_json, read_artifact, require, sha256
from ..extraction import build as extraction

PACKAGE = Path(__file__).parent
TYPES = {"ResearchQuestion", "QuestionMember", "QuestionClaim", "QuestionCoverage", "QuestionManifest"}
FIELDS = {
    "ResearchQuestion": {"text": str, "short_title": str, "wording": dict, "corpus": dict, "as_of": str, "recorded_by": str,
                         "member_ids": list, "claim_ids": list, "claim_links": list},
    "QuestionMember": {"question_id": str, "label": str, "work_id": str, "title": str, "citation": str,
                       "source_versions": list, "retrieved": bool, "record_state": str, "passages": list,
                       "described_in": list, "checks": list, "audit_records": list, "human_decisions": int},
    "QuestionClaim": {"question_id": str, "statement_id": str, "text": str, "written_by": dict,
                      "target_member": str, "identity_records": list},
    "QuestionCoverage": {"question_id": str, "denominator": int, "denominator_definition": str, "rows": list},
    "QuestionManifest": {"question_id": str, "executor": dict, "input_context": dict, "declared_input_receipts": list,
                         "environment": dict, "execution": dict, "record_ids": list,
                         "records_before_manifest_sha256": str},
}
WORDING_ORIGINS = {"DRAFTED_BY_ASSISTANT", "DECLARED_BY_OPERATOR"}
CONFIRMATIONS = {"NOT_CONFIRMED", "CONFIRMED"}
CORPUS_KINDS = {"DECLARED_LIST"}
RECORD_STATES = {"METADATA_ONLY", "RETRIEVED_NO_PASSAGES", "PASSAGES_ON_RECORD"}
RELATIONS = {"TARGET_OF_IMPORTED_AUDIT", "TARGET_OF_EXTRACTION_RUN", "PASSAGES_CITED_IN_IMPORTED_AUDIT",
             "PASSAGES_REVIEWED"}
# Cross-source claim identity may only be declared and attributed here. Text-identity
# labels need a recorded comparison, which this package does not make.
LINK_IDENTITIES = {"DECLARED_BY_REFERENCE", "UNRESOLVED_REQUIRES_REVIEW"}
NOT_RECORDED = "NOT_RECORDED"
# A question bundle holds records, not judgments. These keys may not appear anywhere in it.
FORBIDDEN_KEYS = {"score", "scores", "verdict", "rating", "ratings", "credibility", "trust", "trust_score",
                  "support_count", "consensus", "confidence_score", "weight", "rank", "stance", "position"}
COVERAGE_ROWS = [
    ("retrieved", "Retrieved copy"),
    ("passages", "Passages on record"),
    ("described", "Described in another source's words"),
    ("extraction", "Recorded claim extraction"),
    ("imported-audit-target", "Target paper of an imported audit"),
    ("human", "Decision by a person on record"),
]
SHARED_MODULES = ("__init__.py", "contract.py", "integrity.py", "native.py", "reviews.py", "adapter.py",
                  "sources.py", "claims/__init__.py", "claims/link.py", "claims/standalone.py",
                  "extraction/__init__.py", "extraction/build.py", "extraction/output.py", "extraction/stats.py")


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
                found.append(f"{path}.{key}" if path else key)
            found += forbidden_keys(value, f"{path}.{key}" if path else key)
    elif isinstance(node, list):
        for i, item in enumerate(node):
            found += forbidden_keys(item, f"{path}[{i}]")
    return found


def coverage_rows(members: list[dict]) -> list[dict]:
    """Recompute every coverage row from the member records. Stored counts are never trusted."""
    tests = {
        "retrieved": lambda m: m["retrieved"],
        "passages": lambda m: bool(m["passages"]),
        "described": lambda m: bool(m["described_in"]),
        "extraction": lambda m: any(a["relation"] == "TARGET_OF_EXTRACTION_RUN" for a in m["audit_records"]),
        "imported-audit-target": lambda m: any(a["relation"] == "TARGET_OF_IMPORTED_AUDIT" for a in m["audit_records"]),
        "human": lambda m: m["human_decisions"] > 0,
    }
    rows = []
    for row_id, phrase in COVERAGE_ROWS:
        hits = [m for m in members if tests[row_id](m)]
        rows.append({"id": row_id, "phrase": phrase, "count": len(hits), "members": [m["label"] for m in hits],
                     "refs": [m["id"] for m in hits]})
    return rows


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
            if key not in item or type(item[key]) is not kind:
                raise ContractError(f"INVALID_CONTRACT: {item['type']}.{key}: {item['id']}")
        bad = forbidden_keys(item)
        if bad:
            raise ContractError(f"JUDGMENT_FIELD_NOT_ALLOWED: {item['id']}: {', '.join(bad)}")
        for ref in item["refs"]:
            if ref not in by_id and ref not in external_ids:
                raise ContractError(f"UNRESOLVED_REFERENCE: {item['id']} -> {ref}")

    questions = [r for r in records if r["type"] == "ResearchQuestion"]
    if len(questions) != 1:
        raise ContractError("INVALID_QUESTION_COVERAGE: exactly one ResearchQuestion required")
    q = questions[0]
    wording = q["wording"]
    if wording.get("origin") not in WORDING_ORIGINS or wording.get("operator_confirmation") not in CONFIRMATIONS:
        raise ContractError("INVALID_LABEL: question wording origin/confirmation")
    if wording["origin"] == "DECLARED_BY_OPERATOR" and wording["operator_confirmation"] != "CONFIRMED":
        raise ContractError("INVALID_LABEL: operator-declared wording is confirmed by definition")
    if q["corpus"].get("kind") not in CORPUS_KINDS:
        raise ContractError(f"INVALID_LABEL: corpus kind {q['corpus'].get('kind')!r}")

    members = [by_id.get(i) for i in q["member_ids"]]
    if any(m is None or m["type"] != "QuestionMember" for m in members):
        raise ContractError("INVALID_QUESTION_COVERAGE: member_ids must name QuestionMember records")
    if sorted(q["member_ids"]) != sorted(r["id"] for r in records if r["type"] == "QuestionMember"):
        raise ContractError("INVALID_QUESTION_COVERAGE: every member is listed by the question, once")
    labels = [m["label"] for m in members]
    if len(set(labels)) != len(labels) or q["corpus"].get("members") != labels:
        raise ContractError("INVALID_QUESTION_COVERAGE: member labels must match the declared corpus order")
    by_label = {m["label"]: m for m in members}

    for m in members:
        if m["question_id"] != q["id"]:
            raise ContractError(f"INVALID_QUESTION_COVERAGE: {m['id']} belongs to another question")
        for p in m["passages"]:
            if p["speaker"] != m["label"]:
                raise ContractError(f"MISATTRIBUTED_PASSAGE: {p['native_id']} is listed under {m['label']} "
                                    f"but its speaker is {p['speaker']}")
            if p["about"] is not None:
                if p["about"] == m["label"] or p["about"] not in by_label:
                    raise ContractError(f"MISATTRIBUTED_PASSAGE: {p['native_id']} about {p['about']!r}")
                if not any(d["passage_id"] == p["passage_id"] for d in by_label[p["about"]]["described_in"]):
                    raise ContractError(f"MISATTRIBUTED_PASSAGE: {p['native_id']} missing from "
                                        f"{p['about']}'s described_in")
        for d in m["described_in"]:
            speaker = by_label.get(d["speaker"])
            if speaker is None or d["speaker"] == m["label"]:
                raise ContractError(f"MISATTRIBUTED_PASSAGE: {d['native_id']} described_in speaker {d['speaker']!r}")
            if not any(p["passage_id"] == d["passage_id"] and p["about"] == m["label"] for p in speaker["passages"]):
                raise ContractError(f"MISATTRIBUTED_PASSAGE: {d['native_id']} is not {d['speaker']}'s passage "
                                    f"about {m['label']}")
        # Attribution is checked first: it is the more specific failure.
        expected = ("PASSAGES_ON_RECORD" if m["passages"] else
                    "RETRIEVED_NO_PASSAGES" if m["retrieved"] else "METADATA_ONLY")
        if m["record_state"] not in RECORD_STATES or m["record_state"] != expected:
            raise ContractError(f"INVALID_LABEL: record_state contradicts access and passages: {m['id']}")
        if m["passages"] and not m["retrieved"]:
            raise ContractError(f"INCONSISTENT_ACCESS: passages without a retrieved copy: {m['id']}")
        for a in m["audit_records"]:
            if a["relation"] not in RELATIONS:
                raise ContractError(f"INVALID_LABEL: audit relation {a['relation']!r}")
            if a["record_id"] not in external_ids or a["record_id"] not in m["refs"]:
                raise ContractError(f"UNRESOLVED_REFERENCE: {m['id']} audit record {a['record_id']}")
        recorded = sum(1 for a in m["audit_records"] for k in ("human_review", "human_adjudication")
                       if a["detail"].get(k) not in (None, NOT_RECORDED))
        if m["human_decisions"] != recorded:
            raise ContractError(f"INVALID_COUNT: human_decisions for {m['id']}")

    for c in (r for r in records if r["type"] == "QuestionClaim"):
        if c["question_id"] != q["id"] or c["id"] not in q["claim_ids"]:
            raise ContractError(f"INVALID_QUESTION_COVERAGE: claim {c['id']}")
        if c["target_member"] not in by_label:
            raise ContractError(f"INVALID_QUESTION_COVERAGE: claim's run targets unknown member {c['target_member']!r}")
        if c["written_by"].get("kind") != "MODEL_RUN" or c["statement_id"] not in external_ids:
            raise ContractError(f"UNATTRIBUTED_CLAIM: {c['id']}")
    if sorted(q["claim_ids"]) != sorted(r["id"] for r in records if r["type"] == "QuestionClaim"):
        raise ContractError("INVALID_QUESTION_COVERAGE: every claim is listed by the question, once")

    for link in q["claim_links"]:
        require(link, {"from_claim_id": str, "to_claim_id": str, "identity": str, "declared_by": str, "basis": str},
                "claim link")
        if link["identity"] not in LINK_IDENTITIES:
            raise ContractError(f"UNSUPPORTED_IDENTITY: {link['identity']} needs a recorded text comparison")
        if link["from_claim_id"] not in q["claim_ids"] or link["to_claim_id"] not in q["claim_ids"]:
            raise ContractError("UNRESOLVED_REFERENCE: claim link")
        if not link["declared_by"].strip() or not link["basis"].strip():
            raise ContractError("UNATTRIBUTED_CLAIM_LINK")

    coverages = [r for r in records if r["type"] == "QuestionCoverage"]
    if len(coverages) != 1:
        raise ContractError("INVALID_QUESTION_COVERAGE: exactly one QuestionCoverage required")
    cov = coverages[0]
    if cov["denominator"] != len(members):
        raise ContractError("INVALID_COUNT: coverage denominator is not the number of declared sources")
    if cov["rows"] != coverage_rows(members):
        raise ContractError("INVALID_COUNT: coverage rows do not recompute from the member records")

    manifests = [r for r in records if r["type"] == "QuestionManifest"]
    if len(manifests) != 1:
        raise ContractError("INVALID_MANIFEST_COVERAGE: exactly one QuestionManifest required")
    body = [r for r in records if r is not manifests[0]]
    if manifests[0]["record_ids"] != sorted(r["id"] for r in body):
        raise ContractError("INVALID_MANIFEST_COVERAGE: manifest does not list exactly the bundle records")
    if sha256(jsonl(body)) != manifests[0]["records_before_manifest_sha256"]:
        raise ContractError("MANIFEST_RECORD_HASH_MISMATCH")


def load_bundle(root: Path, pins: dict) -> tuple[list[dict], bytes, bytes]:
    manifest_bytes = read_artifact(root, pins["manifest"])
    records_bytes = read_artifact(root, pins["records"])
    return [load_json(line) for line in records_bytes.splitlines() if line.strip()], manifest_bytes, records_bytes


def build(context: dict, root: Path) -> dict:
    require(context, {"schema_version": str, "question": dict, "corpus": dict, "passage_subjects": list,
                      "claim_links": list, "dependencies": dict}, "context")
    if context["schema_version"] != CONTEXT_SCHEMA:
        raise ContractError("UNSUPPORTED_SCHEMA")
    q, deps = context["question"], context["dependencies"]
    require(q, {"id": str, "text": str, "short_title": str, "wording": dict, "recorded_by": str, "as_of": str},
            "question")
    require(context["corpus"], {"kind": str, "selection_rule": str, "members": list}, "corpus")
    qid = q["id"]
    inputs = []

    # 1. The imported sources bundle: works, versions, read receipts, passages, findings, reviews.
    dep = claimlink.load_dependency({"dependency": deps["import_bundle"]}, root)
    inputs += dep["inputs"]
    imp, run = dep["records"], dep["run"]
    ictx_bytes = read_artifact(root, deps["import_context"])
    ictx = load_json(ictx_bytes)
    if digest(ictx) != run["context_sha256"]:
        raise ContractError("IMPORT_CONTEXT_MISMATCH: context file is not the one the import run recorded")
    inputs.append({**deps["import_context"], "bytes": len(ictx_bytes)})
    src_bytes = read_artifact(root, deps["sources_json"])
    if not any(d["path"] == deps["sources_json"]["path"] and d["sha256"] == deps["sources_json"]["sha256"]
               for d in ictx["declared_inputs"]):
        raise ContractError("SOURCES_NOT_PINNED_BY_IMPORT")
    packet = load_json(src_bytes)["sources"]
    inputs.append({**deps["sources_json"], "bytes": len(src_bytes)})

    # 2. The provisional claim map made from the imported run (unchanged, validated against the import).
    prov, prov_m, prov_r = load_bundle(root, deps["provisional_map_bundle"])
    try:
        claimlink.validate(prov, set(dep["by_id"]))
    except ContractError as exc:
        raise ContractError(f"PROVISIONAL_MAP_BUNDLE_INVALID: {exc}") from exc
    inputs += [{**deps["provisional_map_bundle"]["manifest"], "bytes": len(prov_m)},
               {**deps["provisional_map_bundle"]["records"], "bytes": len(prov_r)}]

    # 3. Recorded extraction runs: each is content-replayed, and must link the same bundles.
    xruns = []
    for pins in deps["extraction_receipts"]:
        xrecs, xm, xr = load_bundle(root, pins)
        try:
            extraction.replay(xm, xr, root, "content")
        except ContractError as exc:
            raise ContractError(f"EXTRACTION_RECEIPT_NOT_VERIFIED: {pins['records']['path']}: {exc}") from exc
        links = load_json(xm)["input_context"]["links"]
        if links["import_bundle"] != deps["import_bundle"] or links["provisional_map_bundle"] != deps["provisional_map_bundle"]:
            raise ContractError(f"LINKED_BUNDLE_MISMATCH: {pins['records']['path']}")
        xruns.append(xrecs)
        inputs += [{**pins["manifest"], "bytes": len(xm)}, {**pins["records"], "bytes": len(xr)}]

    external = set(dep["by_id"]) | {r["id"] for r in prov} | {r["id"] for x in xruns for r in x}

    # 4. Members.
    declared = context["corpus"]["members"]
    labels = [m["label"] for m in declared]
    ictx_passages = {p["id"]: p for p in ictx["passages"]}
    subjects = {}
    checks_by_id = {c["id"]: c for c in ictx["checks"]}
    for s in context["passage_subjects"]:
        require(s, {"passage": str, "about": str, "basis_check": str}, "passage subject")
        check = checks_by_id.get(s["basis_check"])
        if (check is None or s["about"] not in labels or
                not any(s["passage"] in req["passage_ids"] for req in check["requirements"])):
            raise ContractError(f"SUBJECT_BASIS_INVALID: {s}")
        subjects[s["passage"]] = s
    findings = [r for r in imp if r["type"] == "AuditFinding"]
    reviews = [r for r in imp if r["type"] == "ReviewDecision" and r.get("target_binding") == "MATCH"]

    members = []
    for m in declared:
        require(m, {"label": str, "work_id": str}, "member")
        work = dep["by_id"].get(m["work_id"])
        if work is None or work["type"] != "Work":
            raise ContractError(f"MEMBER_NOT_IN_IMPORT: {m['work_id']}")
        entry = packet.get(m["label"])
        if entry is None or f"doi:{entry['doi']}" != m["work_id"]:
            raise ContractError(f"MEMBER_LABEL_MISMATCH: {m['label']} is not {m['work_id']} in the source packet")
        versions = [r for r in imp if r["type"] == "SourceVersion" and r["work_id"] == m["work_id"]]
        version_ids = {v["id"] for v in versions}
        reads = {r["source_version_id"]: r for r in imp if r["type"] == "SourceReadReceipt"
                 and r["source_version_id"] in version_ids}
        retrieved = any(r["access_outcome"] == "AVAILABLE" for r in reads.values())
        own = sorted((r for r in imp if r["type"] == "Passage" and r["source_version_id"] in version_ids),
                     key=lambda r: (r["source_version_id"], r["locator"]["start"]))
        passages = []
        for p in own:
            meta = ictx_passages[p["native_id"]]
            subj = subjects.get(p["native_id"])
            passages.append({"passage_id": p["id"], "native_id": p["native_id"], "label": meta["label"],
                             "page": meta.get("pdf_page"), "speaker": m["label"],
                             "about": subj["about"] if subj else None,
                             "about_basis": subj["basis_check"] if subj else None,
                             "match": p["match"], "public_release": p["public_release"], "text_shown": False})
        checks = [{"check_id": c["id"], "kind": c["kind"], "scope": c["scope"],
                   "eligibility": run["adapter_source_eligibility"][c["id"]]}
                  for c in ictx["checks"] if any(req["source_version_id"] in version_ids for req in c["requirements"])]
        audit = []
        if run["target_work_id"] == m["work_id"]:
            audit.append({"relation": "TARGET_OF_IMPORTED_AUDIT", "record_id": run["id"],
                          "detail": {"origin": run["origin"], "instrument": run["historical_instrument"]["verification"],
                                     "human_review": run["human_review"]}})
        for x in xruns:
            for xr in (r for r in x if r["type"] == "ExtractionRun" and r["source"]["work_id"] == m["work_id"]):
                audit.append({"relation": "TARGET_OF_EXTRACTION_RUN", "record_id": xr["id"],
                              "detail": {"runner": xr["runner"]["identity"], "runner_basis": xr["runner"]["basis"],
                                         "human_review": NOT_RECORDED,
                                         "human_review_basis": "no review record in the extraction bundle"}})
        own_ids = {p["id"] for p in own}
        for f in findings:
            if own_ids & set(f["evidence_passage_ids"]):
                audit.append({"relation": "PASSAGES_CITED_IN_IMPORTED_AUDIT", "record_id": f["id"],
                              "detail": {"assessment": f["assessment"], "import_status": f["import_status"]}})
        own_native = {p["native_id"] for p in own}
        for rv in reviews:
            if own_native & set(rv["review"]["target"]["passages"]):
                audit.append({"relation": "PASSAGES_REVIEWED", "record_id": rv["id"],
                              "detail": {"disposition": rv["imported_disposition"], "reviewer": rv["reviewer"],
                                         "independence": rv["independence"],
                                         "human_adjudication": rv["human_adjudication"]}})
        human = sum(1 for a in audit for k in ("human_review", "human_adjudication")
                    if a["detail"].get(k) not in (None, NOT_RECORDED))
        members.append({"id": f"{qid}/member/{m['label']}", "label": m["label"], "work_id": m["work_id"],
                        "title": work["metadata"]["title"], "citation": entry["citation"],
                        "source_versions": [{"id": v["id"], "version": v["version"], "basis": v["version_basis"],
                                             "access_outcome": reads[v["id"]]["access_outcome"] if v["id"] in reads
                                             else "NOT_ATTEMPTED"} for v in versions],
                        "retrieved": retrieved, "passages": passages, "checks": checks, "audit_records": audit,
                        "human_decisions": human,
                        "refs": [m["work_id"], *sorted(version_ids), *sorted(r["id"] for r in reads.values()),
                                 *sorted(own_ids), *sorted({a["record_id"] for a in audit})]})
    for m in members:
        m["described_in"] = [{"passage_id": p["passage_id"], "native_id": p["native_id"], "label": p["label"],
                              "page": p["page"], "speaker": other["label"], "about_basis": p["about_basis"]}
                             for other in members for p in other["passages"] if p["about"] == m["label"]]
        m["refs"] += [d["passage_id"] for d in m["described_in"]]
        m["record_state"] = ("PASSAGES_ON_RECORD" if m["passages"] else
                             "RETRIEVED_NO_PASSAGES" if m["retrieved"] else "METADATA_ONLY")
    by_work = {m["work_id"]: m["label"] for m in members}

    # 5. Claims already on record about these sources: quoted from the runs that wrote them.
    claims = []
    prov_map = next(r for r in prov if r["type"] == "ClaimMap")
    old_f6 = next((r for r in prov if r["type"] == "ClaimStatement" and r["role"] == "MAP_FIELD_6"
                   and r["field_status"] == "USABLE"), None)
    crosses = [r for x in xruns for r in x if r["type"] == "CrossMapAlignment"]
    if old_f6 and run["target_work_id"] in by_work:
        claims.append({"id": f"{qid}/claim/imported-audit-map-field-6", "statement_id": old_f6["id"],
                       "text": old_f6["exact_text"], "target_member": by_work[run["target_work_id"]],
                       "written_by": {"kind": "MODEL_RUN", "run_id": run["id"],
                                      "instrument": prov_map["producer"]["instrument"],
                                      "mode": prov_map["producer"]["mode"],
                                      "native_label": prov_map["producer"]["native_label"],
                                      "note": prov_map["producer"]["note"]},
                       "identity_records": [{"record_id": c["id"], "relation": c["relation"],
                                             "claim_identity": c["claim_identity"]}
                                            for c in crosses if c["historical_statement_id"] == old_f6["id"]],
                       "refs": [old_f6["id"], run["id"], *[c["id"] for c in crosses
                                                         if c["historical_statement_id"] == old_f6["id"]]]})
    for x in xruns:
        xr = next(r for r in x if r["type"] == "ExtractionRun")
        cmap = next(r for r in x if r["type"] == "ExtractedClaimMap")
        if not cmap["designated_field_6_id"] or xr["source"]["work_id"] not in by_work:
            continue
        f6 = next(r for r in x if r["id"] == cmap["designated_field_6_id"])
        label = by_work[xr["source"]["work_id"]]
        claims.append({"id": f"{qid}/claim/{label.lower()}-extraction-field-6", "statement_id": f6["id"],
                       "text": f6["text"], "target_member": label,
                       "written_by": {"kind": "MODEL_RUN", "run_id": xr["id"],
                                      "instrument": cmap["producer"]["instrument"], "mode": cmap["producer"]["mode"],
                                      "runner": xr["runner"]["identity"], "runner_basis": xr["runner"]["basis"]},
                       "identity_records": [{"record_id": c["id"], "relation": c["relation"],
                                             "claim_identity": c["claim_identity"]}
                                            for c in crosses if c["new_statement_id"] == f6["id"]],
                       "refs": [f6["id"], xr["id"], *[c["id"] for c in crosses if c["new_statement_id"] == f6["id"]]]})

    records = [record("QuestionMember", m.pop("id"), question_id=qid, **m) for m in members]
    records += [record("QuestionClaim", c.pop("id"), question_id=qid, **c) for c in claims]
    member_ids = [f"{qid}/member/{label}" for label in labels]
    claim_ids = [r["id"] for r in records if r["type"] == "QuestionClaim"]
    member_records = [r for r in records if r["type"] == "QuestionMember"]
    records.append(record(
        "QuestionCoverage", f"{qid}/coverage", question_id=qid, denominator=len(members),
        denominator_definition="sources in the declared list", rows=coverage_rows(member_records),
        refs=member_ids))
    records.append(record(
        "ResearchQuestion", qid, text=q["text"], short_title=q["short_title"], wording=q["wording"], recorded_by=q["recorded_by"],
        as_of=q["as_of"],
        corpus={"kind": context["corpus"]["kind"], "selection_rule": context["corpus"]["selection_rule"],
                "members": labels, "imported_corpus_id": run["corpus_scope_id"],
                "imported_corpus_selection": ictx["corpus"]["selection"],
                "imported_corpus_boundary": ictx["corpus"]["boundary"]},
        member_ids=member_ids, claim_ids=claim_ids, claim_links=context["claim_links"],
        refs=[*member_ids, *claim_ids, f"{qid}/coverage", run["corpus_scope_id"]]))

    shared = {name: sha256((PACKAGE.parent / name).read_bytes()) for name in SHARED_MODULES}
    own_code = {p.name: sha256(p.read_bytes()) for p in sorted(PACKAGE.glob("*.py"))}
    body = list(records)
    manifest = record(
        "QuestionManifest", f"{qid}/manifest", question_id=qid,
        executor={"name": "atlas-question", "version": VERSION, "code_sha256": own_code, "shared_code_sha256": shared},
        input_context=context, declared_input_receipts=inputs,
        environment={"implementation": platform.python_implementation(), "python": platform.python_version(),
                     "unicode": unicodedata.unidata_version},
        execution={"models_invoked": [], "network": "NOT_USED",
                   "scope": "deterministic build from committed, pinned receipts; adds no judgment"},
        record_ids=sorted(r["id"] for r in body), records_before_manifest_sha256=sha256(jsonl(body)), refs=[qid])
    records.append(manifest)
    validate(records, external)
    payload = jsonl(records)
    return {"records": records, "jsonl": payload, "manifest": manifest, "external_ids": external,
            "jsonl_sha256": sha256(payload)}


def without_environment(item: dict) -> dict:
    return {k: v for k, v in item.items() if not (item["type"] == "QuestionManifest" and k == "environment")}


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
            "scope": "deterministic question-bundle replay from pinned receipts"}
