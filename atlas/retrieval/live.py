"""Run a locked query live and record every attempt.

Retries happen only on HTTP 429 and 5xx. A network or proxy error is recorded
and not retried, because a policy denial must not be retried. A run with no
successful attempt still returns a record (status FAILED).
"""

from __future__ import annotations

from datetime import datetime, timezone
import json
import time
import urllib.error
import urllib.request

from ..contract import ContractError, sha256
from . import RECORD_SCHEMA, VERSION
from .core import canonical_request, check_page_policy, response_summary, strip_secret

USER_AGENT = f"atlas.retrieval/{VERSION} (+https://github.com/yungmulaBABY1/Provenance-Atlas)"
RETRY_STATUSES = {429} | set(range(500, 600))
TIMEOUT = 60


def utc_now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def urllib_opener(url: str, headers: dict, timeout: int) -> tuple[int, bytes]:
    request = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            return response.status, response.read()
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read() or b""


def run_live(spec: dict, spec_sha256: str, *, api_key: str | None = None, opener=urllib_opener,
             clock=utc_now, sleep=time.sleep, max_attempts: int = 3,
             backoff: tuple[int, ...] = (5, 20)) -> tuple[dict, dict | None]:
    """(record, response data with nothing removed) for one spec. No secret is recorded."""
    url = canonical_request(spec)
    headers = {"User-Agent": USER_AGENT, "Accept": "application/json"}
    if api_key:
        headers["Authorization"] = f"Bearer {api_key}"
    attempts, data, raw = [], None, None
    for number in range(1, max_attempts + 1):
        at = clock()
        try:
            status, body = opener(url, headers, TIMEOUT)
        except (urllib.error.URLError, OSError, TimeoutError) as exc:
            reason = strip_secret(str(getattr(exc, "reason", exc)), api_key)
            attempts.append({"attempt": number, "at": at, "outcome": "NETWORK_ERROR",
                             "status": None, "detail": reason[:200]})
            break
        entry = {"attempt": number, "at": at, "status": status, "bytes": len(body),
                 "body_sha256": sha256(body)}
        if status == 200:
            try:
                data = json.loads(body)
                if not isinstance(data, dict):
                    raise ValueError("not an object")
            except ValueError as exc:
                entry["outcome"] = "INVALID_JSON"
                entry["detail"] = str(exc)[:200]
                attempts.append(entry)
                data = None
                break
            entry["outcome"] = "OK"
            attempts.append(entry)
            raw = body
            break
        entry["outcome"] = "HTTP_ERROR"
        attempts.append(entry)
        if status not in RETRY_STATUSES or number == max_attempts:
            break
        sleep(backoff[min(number - 1, len(backoff) - 1)])
    record = {
        "schema": RECORD_SCHEMA,
        "id": spec["id"],
        "spec_sha256": spec_sha256,
        "provenance": spec["provenance"],
        "request": {"canonical_url": url, "request_sha256": sha256(url.encode("utf-8")),
                    "credentials": ("api key sent in Authorization header; value not recorded"
                                    if api_key else "none")},
        "mode": "live",
        "retrieval_performed_by": f"atlas.retrieval {VERSION}",
        "checked_by": f"atlas.retrieval {VERSION}",
        "attempts": attempts,
        "response": None,
        "checks": {},
        "status": "FAILED",
        "failed_checks": ["no_successful_attempt"],
    }
    if data is not None:
        summary = response_summary(data)
        checks = check_page_policy(spec, summary)
        checks["abstracts_absent_or_stripped"] = summary["abstracts"] != "PRESENT"
        failed = sorted(k for k, v in checks.items() if v is False)
        record.update(response=dict(summary, body_sha256=sha256(raw)), checks=checks,
                      status="OK" if not failed else "INCONSISTENT", failed_checks=failed)
    if api_key and api_key in json.dumps(record):
        raise ContractError("SECRET_IN_RECORD")
    return record, data
