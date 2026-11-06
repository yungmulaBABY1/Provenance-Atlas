"""Reconstruct a locked-query spec from an executor's log, after the run.

The parameters come from the last successful logged request, with credential
parameters removed. The declaration (which file, which terms) is supplied by
whoever does the reconstruction, because only a reader can say which text
declared the query. A reconstructed spec is labeled reconstructed-after-run, so
'request matches log' holds for it by construction.
"""

from __future__ import annotations

import json
from pathlib import Path
from urllib.parse import parse_qsl, urlsplit

from ..contract import ContractError, sha256
from .core import CREDENTIAL_PARAMS, validate_spec
from .saved import read_log

METHOD = ("parameters of the last successful logged request, mailto removed; "
          "declared terms copied from the declaration by hand (Claude, 2026-11-05)")


def file_sha256(root: Path, path: str) -> str:
    return sha256((root / path).read_bytes())


def spec_from_log(root: Path, log: str, file_key: str, spec_id: str, declared: dict,
                  notes: list[str] | None = None) -> dict:
    entries, _ = read_log(root / log)
    hits = [e for e in entries if e.get("file") == file_key and e.get("status") == 200]
    if not hits:
        raise ContractError(f"NOT_IN_EXECUTOR_LOG: {file_key}")
    entry = hits[-1]
    parts = urlsplit(entry["url"])
    params = [[k, v] for k, v in parse_qsl(parts.query, keep_blank_values=True)
              if k not in CREDENTIAL_PARAMS]
    spec = {"schema": "atlas-retrieval-spec/0.1", "id": spec_id, "provider": "openalex",
            "endpoint": f"{parts.scheme}://{parts.netloc}{parts.path}", "params": params,
            "pages": "first-only", "provenance": "reconstructed-after-run",
            "reconstructed_from": {"executor_log": log, "line": entry["_line"], "method": METHOD},
            "declared": declared}
    if notes:
        spec["notes"] = notes
    return validate_spec(spec)


def write_json(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, indent=1, ensure_ascii=False) + "\n", encoding="utf-8")
