"""Record an executor's saved response and check it against its log and declaration.

The executor performed the retrieval. Everything taken from its log is labeled
executor-logged. The code establishes only whether the pieces agree.
"""

from __future__ import annotations

import json
from pathlib import Path

from ..contract import ContractError, load_json, sha256
from . import RECORD_SCHEMA, VERSION
from .core import (canonical_request, check_page_policy, declared_checks, response_summary,
                   url_params)

SUCCESS = 200


def read_log(path: Path) -> list[dict]:
    entries = []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            entry = json.loads(line)
        except ValueError as exc:
            raise ContractError(f"INVALID_EXECUTOR_LOG: line {number}: {exc}") from exc
        if isinstance(entry, dict):
            entry["_line"] = number
            entries.append(entry)
    return entries


def log_summary(entries: list[dict], file_key: str, spec: dict) -> tuple[dict, dict, str | None]:
    """(checks, observations, sha256 of the file the log says it wrote last)."""
    attempts = [e for e in entries if e.get("file") == file_key]
    if not attempts:
        raise ContractError(f"NOT_IN_EXECUTOR_LOG: {file_key}")
    successes = [e for e in attempts if e.get("status") == SUCCESS]
    last = successes[-1] if successes else None
    statuses = [e.get("status") for e in attempts]
    first_success = statuses.index(SUCCESS) if SUCCESS in statuses else None
    urls = {e.get("url") for e in attempts}
    endpoint, params, creds = url_params(last["url"]) if last else (None, None, [])
    spec_params = sorted(map(tuple, spec["params"]))
    observations = {
        "logged_by": "executor",
        "attempts": len(attempts),
        "statuses": statuses,
        "successes": len(successes),
        "re_executed_after_success": first_success is not None and first_success < len(attempts) - 1,
        "distinct_logged_urls": len(urls),
        "credential_params_logged": creds,
        "first_attempt_at": attempts[0].get("at"),
        "last_success_at": last.get("at") if last else None,
        "log_lines": [e["_line"] for e in attempts],
    }
    checks = {
        "logged_success": last is not None,
        "request_matches_logged": (last is not None and endpoint == spec["endpoint"]
                                   and sorted(map(tuple, params)) == spec_params),
    }
    return checks, observations, (last.get("sha256") if last else None)


def record_saved(root: Path, spec: dict, spec_sha256: str, response: str,
                 executor_log: str | None = None, log_file_key: str | None = None) -> dict:
    path = root / response
    if not path.is_file():
        raise ContractError(f"MISSING_RESPONSE: {response}")
    data = path.read_bytes()
    summary = response_summary(load_json(data))
    checks = declared_checks(root, spec)
    missing = checks.pop("missing")
    checks.update(check_page_policy(spec, summary))
    checks["abstracts_absent_or_stripped"] = summary["abstracts"] != "PRESENT"
    declared_response = spec["declared"].get("response_sha256")
    if declared_response:
        checks["declared_response_sha256_matches"] = sha256(data) == declared_response
    observations = None
    if executor_log:
        log_checks, observations, logged_sha = log_summary(read_log(root / executor_log),
                                                           log_file_key, spec)
        checks.update(log_checks)
        checks["file_matches_logged_sha256"] = logged_sha == sha256(data)
        locked_at = spec["declared"].get("locked_at")
        if locked_at and observations["first_attempt_at"]:
            # Both timestamps are written by the executor; only their order is compared.
            observations["declared_before_first_attempt"] = locked_at < observations["first_attempt_at"]
    failed = sorted(k for k, v in checks.items() if v is False)
    return {
        "schema": RECORD_SCHEMA,
        "id": spec["id"],
        "spec_sha256": spec_sha256,
        "provenance": spec["provenance"],
        "request": {"canonical_url": canonical_request(spec),
                    "request_sha256": sha256(canonical_request(spec).encode("utf-8")),
                    "credentials": "none recorded"},
        "mode": "saved-response",
        "retrieval_performed_by": "executor",
        "checked_by": f"atlas.retrieval {VERSION}",
        "response": dict(summary, file=response, file_sha256=sha256(data)),
        "checks": checks,
        "missing_terms": missing,
        "executor_log": observations,
        "status": "CONSISTENT" if not failed else "INCONSISTENT",
        "failed_checks": failed,
    }
