"""Build, validate and replay a challenge bundle over one pinned import receipt."""

from __future__ import annotations

from pathlib import Path
import platform
import re
import unicodedata

from . import ARTIFACT_SCHEMA, CONTEXT_SCHEMA, SCHEMA, VERSION
from .. import adapter
from .. import replay as import_replay
from ..claims import link as claimlink
from ..contract import ContractError, canonical, load_json, read_artifact, require, sha256

PACKAGE = Path(__file__).parent
SHARED_MODULES = ("__init__.py", "adapter.py", "contract.py", "integrity.py", "native.py", "reviews.py",
                  "sources.py", "ledger.py", "replay.py", "baseline.json", "claims/__init__.py", "claims/link.py",
                  "claims/standalone.py")

TYPES = {"ChallengeRun", "ReviewItem", "Challenge", "ChallengeManifest"}
FIELDS = {
    "ChallengeRun": {"operator": str, "purpose": str, "recorded_by": str, "dependency": dict, "checker": dict,
                     "item_ids": list, "challenge_ids": list, "counts": dict, "method": str},
    "ReviewItem": {"challenge_run_id": str, "audit_run_id": str, "item_number": int, "item_code": str, "text": str,
                   "text_sha256": str, "instruction": str, "output_sha256": str, "checker": dict,
                   "challenge_state": str, "challenge_ids": list, "detached_challenge_ids": list,
                   "outcomes": list},
    "Challenge": {"challenge_run_id": str, "artifact": dict, "challenge_id": str, "binding": str,
                  "mismatched": list, "item_id": (str, type(None)), "target": dict, "challenger": dict,
                  "relation_to_run": dict, "recorded_by": str, "performed_at": str, "exposure": dict,
                  "outcome": str, "parts": list, "reasons": list, "evidence": list,
                  "what_would_change": list, "decision_by": str, "effect": str},
    "ChallengeManifest": {"challenge_run_id": str, "executor": dict, "input_context": dict,
                          "declared_input_receipts": list, "dependency": dict, "environment": dict,
                          "execution": dict, "record_ids": list, "records_before_manifest_sha256": str},
}
OUTCOMES = {"CONDITION_MET", "CONDITION_MET_WITH_QUALIFICATION", "CONDITION_NOT_MET", "CANNOT_DETERMINE"}
CHALLENGER_KINDS = {"PERSON", "MODEL_AGENT"}
RELATIONS = {"YES", "NO", "UNKNOWN"}
LABELS = {
    ("ReviewItem", "challenge_state"): {"NOT_CHALLENGED", "CHALLENGED"},
    ("Challenge", "binding"): {"MATCH", "TARGET_MISMATCH"},
    ("Challenge", "outcome"): OUTCOMES,
    ("Challenge", "decision_by"): CHALLENGER_KINDS,
}
FORBIDDEN_KEYS = {"score", "scores", "verdict", "rating", "ratings", "credibility", "trust", "trust_score",
                  "consensus", "confidence_score", "weight", "rank", "stance", "position"}
ITEM_LINE = re.compile(r"REVIEW_ITEM_(\d+)\t([A-Z_]+) — (.+)", re.DOTALL)
ARTIFACT = {"schema": str, "challenge_id": str, "target": dict, "challenger": dict, "relation_to_run": dict,
            "recorded_by": str, "performed_at": str, "exposure": dict, "outcome": str, "parts": list,
            "reasons": list, "evidence": list, "what_would_change": list}
TARGET = {"kind": str, "audit_run_id": str, "output_sha256": str, "checker_sha256": str, "item_number": int,
          "item_code": str, "item_text_sha256": str}
SLUG = re.compile(r"[a-z0-9][a-z0-9-]{2,80}")
DATE = re.compile(r"\d{4}-\d{2}-\d{2}(T\d{2}:\d{2}(:\d{2})?Z)?")
EFFECT = ("APPENDED: the imported run, its checker status and its findings are unchanged. This record "
          "states one decision on one review item and is not a finding-level or paper-level judgment.")


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
    require(context, {"schema_version": str, "run": dict, "import_bundle": dict, "code_author": dict,
                      "challenges": list}, "context")
    if context["schema_version"] != CONTEXT_SCHEMA:
        raise ContractError("UNSUPPORTED_SCHEMA")
    require(context["run"], {"id": str, "operator": str, "purpose": str, "recorded_by": str}, "run")
    require(context["import_bundle"], {"audit_run_id": str, "manifest": dict, "records": dict}, "import_bundle")
    require(context["code_author"], {"identity": str, "basis": str}, "code_author")
    for pin in context["challenges"]:
        require(pin, {"path": str, "sha256": str}, "challenges[]")


def load_artifact(data: bytes, code_author: str, producer: str) -> dict:
    """A challenge artifact as written by its challenger. Rejected, never repaired."""
    art = load_json(data)
    require(art, ARTIFACT, "challenge")
    if art["schema"] != ARTIFACT_SCHEMA:
        raise ContractError(f"UNSUPPORTED_CHALLENGE_SCHEMA: {art['schema']}")
    if set(art) != set(ARTIFACT):
        raise ContractError(f"INVALID_CHALLENGE: fields {sorted(set(art) ^ set(ARTIFACT))}")
    if not SLUG.fullmatch(art["challenge_id"]):
        raise ContractError(f"INVALID_CHALLENGE: challenge_id {art['challenge_id']!r}")
    require(art["target"], TARGET, "challenge.target")
    if art["target"]["kind"] != "CHECKER_REVIEW_ITEM":
        raise ContractError(f"UNSUPPORTED_TARGET_KIND: {art['target']['kind']}")
    require(art["challenger"], {"identity": str, "kind": str, "context": str}, "challenge.challenger")
    if art["challenger"]["kind"] not in CHALLENGER_KINDS:
        raise ContractError(f"INVALID_LABEL: challenger kind {art['challenger']['kind']}")
    require(art["relation_to_run"], {"producer": str, "atlas_code_author": str, "basis": str},
            "challenge.relation_to_run")
    rel = art["relation_to_run"]
    if rel["producer"] not in RELATIONS or rel["atlas_code_author"] not in RELATIONS:
        raise ContractError("INVALID_LABEL: relation_to_run")
    identity = art["challenger"]["identity"].strip()
    if rel["producer"] == "YES" or identity == producer:
        raise ContractError("PRODUCER_CANNOT_CHALLENGE_OWN_RUN: the run's producer cannot decide its review items")
    if rel["atlas_code_author"] == "YES" or identity == code_author:
        raise ContractError("CODE_AUTHOR_CANNOT_DECIDE: the author of this code cannot record a decision")
    if art["outcome"] not in OUTCOMES:
        raise ContractError(f"INVALID_LABEL: outcome {art['outcome']}")
    if not art["reasons"] or not all(isinstance(r, str) and r.strip() for r in art["reasons"]):
        raise ContractError("INVALID_CHALLENGE: at least one stated reason is required")
    for part in art["parts"]:
        require(part, {"part": str, "outcome": str, "reasons": list}, "challenge.parts[]")
        if part["outcome"] not in OUTCOMES or not part["reasons"]:
            raise ContractError(f"INVALID_CHALLENGE: part {part['part']!r}")
    require(art["exposure"], {"seen_before_deciding": list, "prior_position": str}, "challenge.exposure")
    if not DATE.fullmatch(art["performed_at"]):
        raise ContractError(f"INVALID_CHALLENGE: performed_at {art['performed_at']!r}")
    for item in art["evidence"]:
        if item.get("kind") == "RECORD":
            require(item, {"kind": str, "id": str}, "challenge.evidence[]")
        elif item.get("kind") == "FILE":
            require(item, {"kind": str, "path": str, "sha256": str}, "challenge.evidence[]")
        else:
            raise ContractError(f"INVALID_CHALLENGE: evidence kind {item.get('kind')!r}")
    if forbidden_keys(art):
        raise ContractError(f"JUDGMENT_FIELD_NOT_ALLOWED: {', '.join(forbidden_keys(art))}")
    return art


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
        if forbidden_keys(item):
            raise ContractError(f"JUDGMENT_FIELD_NOT_ALLOWED: {item['id']}: {', '.join(forbidden_keys(item))}")
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
        if item["type"] == "ReviewItem":
            if sha256(item["text"].encode("utf-8")) != item["text_sha256"]:
                raise ContractError(f"ITEM_HASH_MISMATCH: {item['id']}")
            attached = [by_id.get(c, {}) for c in item["challenge_ids"]]
            if any(c.get("type") != "Challenge" or c.get("binding") != "MATCH" or c.get("item_id") != item["id"]
                   for c in attached):
                raise ContractError(f"DETACHED_CHALLENGE_ATTACHED: {item['id']}")
            if item["challenge_state"] != ("CHALLENGED" if attached else "NOT_CHALLENGED"):
                raise ContractError(f"INVALID_LABEL: challenge state does not follow its challenges: {item['id']}")
            expected = [{"challenge_id": c["id"], "outcome": c["outcome"], "decision_by": c["decision_by"]}
                        for c in attached]
            if item["outcomes"] != expected:
                raise ContractError(f"INVALID_LABEL: item outcomes are not its challenges' own: {item['id']}")
        if item["type"] == "Challenge":
            if (item["binding"] == "MATCH") != (not item["mismatched"]) or \
                    (item["binding"] == "MATCH") != (item["item_id"] is not None):
                raise ContractError(f"INVALID_LABEL: binding contradicts its mismatches: {item['id']}")
            rel = item["relation_to_run"]
            if rel.get("producer") == "YES":
                raise ContractError(f"PRODUCER_CANNOT_CHALLENGE_OWN_RUN: {item['id']}")
            if rel.get("atlas_code_author") == "YES":
                raise ContractError(f"CODE_AUTHOR_CANNOT_DECIDE: {item['id']}")
            if item["decision_by"] != item["challenger"].get("kind"):
                raise ContractError(f"INVALID_LABEL: decision_by is not the challenger's kind: {item['id']}")
            if item["effect"] != EFFECT:
                raise ContractError(f"INVALID_LABEL: a challenge only appends: {item['id']}")
    run = next((r for r in records if r["type"] == "ChallengeRun"), None)
    if run is not None:
        items = [by_id.get(i) for i in run["item_ids"]]
        challenges = [by_id.get(i) for i in run["challenge_ids"]]
        if any(i is None or i["type"] != "ReviewItem" for i in items) or \
                any(c is None or c["type"] != "Challenge" for c in challenges):
            raise ContractError("INVALID_CONTRACT: run lists a record that is not an item or challenge")
        if sorted(r["id"] for r in records if r["type"] == "ReviewItem") != sorted(run["item_ids"]) or \
                sorted(r["id"] for r in records if r["type"] == "Challenge") != sorted(run["challenge_ids"]):
            raise ContractError("INVALID_CONTRACT: run does not list every item and challenge")
        if run["counts"] != counts(items, challenges):
            raise ContractError("INVALID_COUNT: run counts do not follow its records")
    manifests = [r for r in records if r["type"] == "ChallengeManifest"]
    if len(manifests) != 1:
        raise ContractError("INVALID_MANIFEST_COVERAGE: exactly one ChallengeManifest required")
    body = [r for r in records if r is not manifests[0]]
    if manifests[0]["record_ids"] != sorted(r["id"] for r in body):
        raise ContractError("INVALID_MANIFEST_COVERAGE: manifest does not list exactly the bundle records")
    if sha256(jsonl(body)) != manifests[0]["records_before_manifest_sha256"]:
        raise ContractError("MANIFEST_RECORD_HASH_MISMATCH")


def counts(items: list[dict], challenges: list[dict]) -> dict:
    by_outcome = {}
    for c in challenges:
        if c["binding"] == "MATCH":
            by_outcome[c["outcome"]] = by_outcome.get(c["outcome"], 0) + 1
    return {"items": len(items),
            "items_not_challenged": sum(1 for i in items if i["challenge_state"] == "NOT_CHALLENGED"),
            "items_with_a_decision_by_a_person": sum(1 for i in items
                                                     if any(o["decision_by"] == "PERSON" for o in i["outcomes"])),
            "challenges": len(challenges),
            "challenges_detached": sum(1 for c in challenges if c["binding"] != "MATCH"),
            "attached_by_outcome": dict(sorted(by_outcome.items()))}


def load_import(context: dict, root: Path) -> dict:
    pins = context["import_bundle"]
    manifest_bytes = read_artifact(root, pins["manifest"])
    records_bytes = read_artifact(root, pins["records"])
    try:
        import_replay.replay(manifest_bytes, records_bytes, root, "content")
    except ContractError as exc:
        raise ContractError(f"IMPORT_RECEIPT_NOT_VERIFIED: {exc}") from exc
    dep = claimlink.load_dependency({"dependency": pins}, root)
    return {**dep, "inputs": [{**pins["manifest"], "bytes": len(manifest_bytes)},
                              {**pins["records"], "bytes": len(records_bytes)}]}


def review_items(run: dict) -> tuple[dict, list[dict]]:
    """Re-run the vendored checker on the run's own output bytes."""
    raw = run["raw_output_text"].encode("utf-8")
    if sha256(raw) != run["output_sha256"]:
        raise ContractError("OUTPUT_HASH_MISMATCH: AuditRun text does not match its output_sha256")
    baseline = load_json(adapter.BASELINE_PATH.read_bytes())
    pinned = {path: adapter.vendored(entry) for path, entry in sorted(baseline["files"].items())}
    result = adapter.pinned_checker(raw, pinned)
    if result["status"] != run["checker_status"]:
        raise ContractError(f"CHECKER_RESULT_DIFFERS: {result['status']} != recorded {run['checker_status']}")
    entry = baseline["files"][adapter.CHECKER]
    checker = {"path": entry["path"], "sha256": entry["sha256"], "git_blob_sha1": entry["git_blob_sha1"],
               "source": "vendored validation baseline (atlas/baseline.json)", "status": result["status"]}
    items = []
    for line in result["review_items"]:
        match = ITEM_LINE.fullmatch(line)
        if not match:
            raise ContractError(f"REVIEW_ITEM_UNPARSED: {line[:80]!r}")
        number, code, rest = int(match.group(1)), match.group(2), match.group(3)
        instruction = rest.split(": ", 1)[0]
        items.append({"number": number, "code": code, "text": line, "instruction": instruction})
    if [i["number"] for i in items] != list(range(1, len(items) + 1)):
        raise ContractError("REVIEW_ITEM_NUMBERING: items are not numbered 1..n")
    return checker, items


def build(context: dict, root: Path) -> dict:
    validate_context(context)
    rid = context["run"]["id"]
    dep = load_import(context, root)
    run = dep["run"]
    if run["id"] != context["import_bundle"]["audit_run_id"]:
        raise ContractError("DEPENDENCY_INVALID: audit_run_id")
    checker, items = review_items(run)
    producer = run["model"]["identity"].strip()
    code_author = context["code_author"]["identity"].strip()

    records, challenge_records, artifacts = [], [], []
    seen = set()
    for pin in context["challenges"]:
        data = read_artifact(root, pin)
        art = load_artifact(data, code_author, producer)
        if art["challenge_id"] in seen:
            raise ContractError(f"DUPLICATE_ID: challenge {art['challenge_id']}")
        seen.add(art["challenge_id"])
        artifacts.append((pin, data, art))

    item_ids = {i["number"]: f"{rid}/item/{i['number']}" for i in items}
    current = {i["number"]: i for i in items}
    attached: dict[int, list[dict]] = {}
    detached: dict[int, list[str]] = {}
    for pin, data, art in artifacts:
        target = art["target"]
        item = current.get(target["item_number"])
        mismatched = []
        for name, ok in (("audit_run", target["audit_run_id"] == run["id"]),
                         ("output", target["output_sha256"] == run["output_sha256"]),
                         ("checker", target["checker_sha256"] == checker["sha256"]),
                         ("item_number", item is not None),
                         ("item_code", item is not None and target["item_code"] == item["code"]),
                         ("item_text", item is not None
                          and target["item_text_sha256"] == sha256(item["text"].encode("utf-8")))):
            if not ok:
                mismatched.append(name)
        evidence = []
        for ev in art["evidence"]:
            if ev["kind"] == "RECORD":
                if ev["id"] not in dep["by_id"]:
                    raise ContractError(f"EVIDENCE_UNRESOLVED: record {ev['id']}")
                evidence.append({**ev, "resolved": "RECORD_IN_IMPORT_BUNDLE"})
            else:
                body = read_artifact(root, {"path": ev["path"], "sha256": ev["sha256"]})
                lines = ev.get("lines")
                if lines is not None and not (isinstance(lines, list) and len(lines) == 2
                                              and 1 <= lines[0] <= lines[1] <= body.count(b"\n") + 1):
                    raise ContractError(f"EVIDENCE_UNRESOLVED: lines {lines} in {ev['path']}")
                evidence.append({**ev, "resolved": "FILE_PINNED", "bytes": len(body)})
        cid = f"{rid}/challenge/{art['challenge_id']}"
        match = not mismatched
        item_id = item_ids[target["item_number"]] if match else None
        challenge = record(
            "Challenge", cid, challenge_run_id=rid, artifact={**pin, "bytes": len(data)},
            challenge_id=art["challenge_id"], binding="MATCH" if match else "TARGET_MISMATCH",
            mismatched=mismatched, item_id=item_id, target=target, challenger=art["challenger"],
            relation_to_run={**art["relation_to_run"], "verification": "DECLARED_BY_CHALLENGER_NOT_VERIFIED"},
            recorded_by=art["recorded_by"], performed_at=art["performed_at"], exposure=art["exposure"],
            outcome=art["outcome"], parts=art["parts"], reasons=art["reasons"], evidence=evidence,
            what_would_change=art["what_would_change"], decision_by=art["challenger"]["kind"], effect=EFFECT,
            refs=[rid, *([item_id] if item_id else []),
                  *dict.fromkeys(ev["id"] for ev in art["evidence"] if ev["kind"] == "RECORD")])
        challenge_records.append(challenge)
        if match:
            attached.setdefault(target["item_number"], []).append(challenge)
        elif item is not None:
            detached.setdefault(target["item_number"], []).append(cid)

    item_records = []
    for item in items:
        mine = sorted(attached.get(item["number"], []), key=lambda c: c["id"])
        item_records.append(record(
            "ReviewItem", item_ids[item["number"]], challenge_run_id=rid, audit_run_id=run["id"],
            item_number=item["number"], item_code=item["code"], text=item["text"],
            text_sha256=sha256(item["text"].encode("utf-8")), instruction=item["instruction"],
            output_sha256=run["output_sha256"], checker={k: checker[k] for k in ("path", "sha256")},
            challenge_state="CHALLENGED" if mine else "NOT_CHALLENGED",
            challenge_ids=[c["id"] for c in mine], detached_challenge_ids=sorted(detached.get(item["number"], [])),
            outcomes=[{"challenge_id": c["id"], "outcome": c["outcome"], "decision_by": c["decision_by"]}
                      for c in mine],
            refs=[rid, run["id"], *[c["id"] for c in mine], *sorted(detached.get(item["number"], []))]))
    records += item_records + challenge_records
    challenge_records.sort(key=lambda c: c["id"])
    records.append(record(
        "ChallengeRun", rid, operator=context["run"]["operator"], purpose=context["run"]["purpose"],
        recorded_by=context["run"]["recorded_by"],
        dependency={"audit_run_id": run["id"], "producer": producer, **dep["pins"],
                    "import_receipt": "CONTENT_REPLAYED_IN_THIS_BUILD"},
        checker=checker, code_author=context["code_author"],
        item_ids=[r["id"] for r in item_records], challenge_ids=[c["id"] for c in challenge_records],
        counts=counts(item_records, challenge_records),
        method=("Deterministic: content-replay the import receipt, re-run the vendored checker on the run's "
                "own output bytes, record each REVIEW_ITEM, and bind each pinned challenge artifact to its "
                "item by run, output, checker, number, code and text. No model; no decision is made here."),
        refs=[run["id"], *[r["id"] for r in item_records], *[c["id"] for c in challenge_records]]))

    external = set(dep["by_id"])
    shared = {name: sha256((PACKAGE.parent / name).read_bytes()) for name in SHARED_MODULES}
    own = {p.name: sha256(p.read_bytes()) for p in sorted(PACKAGE.glob("*.py"))}
    body = list(records)
    manifest = record(
        "ChallengeManifest", f"{rid}/manifest", challenge_run_id=rid,
        executor={"name": "atlas-challenge", "version": VERSION, "code_sha256": own, "shared_code_sha256": shared,
                  "artifact_schema": ARTIFACT_SCHEMA},
        input_context=context,
        declared_input_receipts=[*dep["inputs"], *[{**pin, "bytes": len(data)} for pin, data, _ in artifacts]],
        dependency={"audit_run_id": run["id"], **dep["pins"]},
        environment={"implementation": platform.python_implementation(), "python": platform.python_version(),
                     "unicode": unicodedata.unidata_version},
        execution={"models_invoked": [], "network": "NOT_USED; no OS-level network sandbox is claimed",
                   "semantic_judgment": "NONE_BY_THIS_CODE; outcomes are the challengers' own",
                   "checker": "vendored checker run in a temporary directory on the run's output bytes",
                   "scope": "deterministic recording of declared challenges"},
        record_ids=sorted(r["id"] for r in body), records_before_manifest_sha256=sha256(jsonl(body)), refs=[rid])
    records.append(manifest)
    validate(records, external)
    payload = jsonl(records)
    return {"records": records, "jsonl": payload, "manifest": manifest, "external_ids": external,
            "jsonl_sha256": sha256(payload), "items": items, "checker": checker}


def without_environment(item: dict) -> dict:
    return {k: v for k, v in item.items() if not (item["type"] == "ChallengeManifest" and k == "environment")}


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
            "scope": "deterministic challenge replay; outcomes are re-read from their pinned artifacts"}
