"""Specs, canonical requests, digests and checks against the declared query."""

from __future__ import annotations

from pathlib import Path
from urllib.parse import parse_qsl, quote, urlsplit

from ..contract import ContractError, canonical, digest, load_json, normalize, sha256
from . import SPEC_SCHEMA

PROVIDERS = {"openalex": "https://api.openalex.org/"}
# Never part of a query's identity, never sent, never recorded with a value.
CREDENTIAL_PARAMS = {"api_key", "mailto"}
PER_PAGE_KEYS = ("per-page", "per_page")
PROVENANCE = {"locked-before-run", "reconstructed-after-run"}
DECLARED_KINDS = {"pre-run-lock", "run-output"}


def _text(value, where: str) -> str:
    if not isinstance(value, str) or not value:
        raise ContractError(f"INVALID_SPEC: {where} must be a non-empty string")
    return value


def validate_spec(spec: dict) -> dict:
    if spec.get("schema") != SPEC_SCHEMA:
        raise ContractError(f"INVALID_SPEC: schema must be {SPEC_SCHEMA}")
    _text(spec.get("id"), "id")
    provider = spec.get("provider")
    if provider not in PROVIDERS:
        raise ContractError(f"INVALID_SPEC: unknown provider {provider!r}")
    endpoint = _text(spec.get("endpoint"), "endpoint")
    if not endpoint.startswith(PROVIDERS[provider]) or "?" in endpoint:
        raise ContractError("INVALID_SPEC: endpoint must be a provider URL without a query")
    params = spec.get("params")
    if not isinstance(params, list) or not params:
        raise ContractError("INVALID_SPEC: params must be a non-empty list of [name, value]")
    names = []
    for item in params:
        if (not isinstance(item, list) or len(item) != 2
                or not all(isinstance(x, str) and x for x in item)):
            raise ContractError("INVALID_SPEC: each param must be [name, value] strings")
        if item[0] in CREDENTIAL_PARAMS:
            raise ContractError(f"INVALID_SPEC: credential parameter {item[0]} in a spec")
        names.append(item[0])
    if len(set(names)) != len(names):
        raise ContractError("INVALID_SPEC: duplicate parameter name")
    if spec.get("pages") != "first-only":
        raise ContractError("INVALID_SPEC: pages must be first-only (cursor paging is not supported)")
    if dict(params).get("page", "1") != "1" or "cursor" in names:
        raise ContractError("INVALID_SPEC: only the first page may be requested")
    per_page = [dict(params)[k] for k in PER_PAGE_KEYS if k in names]
    if len(per_page) != 1 or not per_page[0].isdigit() or not 1 <= int(per_page[0]) <= 200:
        raise ContractError("INVALID_SPEC: exactly one per-page between 1 and 200 is required")
    if spec.get("provenance") not in PROVENANCE:
        raise ContractError(f"INVALID_SPEC: provenance must be one of {sorted(PROVENANCE)}")
    declared = spec.get("declared")
    if not isinstance(declared, dict):
        raise ContractError("INVALID_SPEC: declared is required")
    _text(declared.get("path"), "declared.path")
    if len(declared.get("sha256", "")) != 64:
        raise ContractError("INVALID_SPEC: declared.sha256 must be a sha256")
    if declared.get("kind") not in DECLARED_KINDS:
        raise ContractError(f"INVALID_SPEC: declared.kind must be one of {sorted(DECLARED_KINDS)}")
    requires = declared.get("requires")
    if not isinstance(requires, list) or not requires or not all(isinstance(x, str) and x for x in requires):
        raise ContractError("INVALID_SPEC: declared.requires must list the declared query terms")
    if "response_sha256" in declared and len(declared["response_sha256"]) != 64:
        raise ContractError("INVALID_SPEC: declared.response_sha256 must be a sha256")
    return spec


def load_spec(path: Path) -> tuple[dict, str]:
    data = path.read_bytes()
    return validate_spec(load_json(data)), sha256(data)


def per_page(spec: dict) -> int:
    params = dict(spec["params"])
    return int(next(params[k] for k in PER_PAGE_KEYS if k in params))


def canonical_query(params) -> str:
    """Encoded query string, parameters sorted by name. Credentials are excluded."""
    items = sorted((k, v) for k, v in params if k not in CREDENTIAL_PARAMS)
    return "&".join(f"{quote(k, safe='-_.')}={quote(v, safe='')}" for k, v in items)


def canonical_request(spec: dict) -> str:
    return f"{spec['endpoint']}?{canonical_query(spec['params'])}"


def decoded_query(params) -> str:
    """Human-readable form used for substring checks against the declaration."""
    items = sorted((k, v) for k, v in params if k not in CREDENTIAL_PARAMS)
    return "&".join(f"{k}={v}" for k, v in items)


def url_params(url: str) -> tuple[str, list[list[str]], list[str]]:
    """(endpoint, non-credential params in logged order, credential names present)."""
    parts = urlsplit(url)
    pairs = parse_qsl(parts.query, keep_blank_values=True)
    creds = sorted({k for k, _ in pairs if k in CREDENTIAL_PARAMS})
    return (f"{parts.scheme}://{parts.netloc}{parts.path}",
            [[k, v] for k, v in pairs if k not in CREDENTIAL_PARAMS], creds)


def without_abstracts(value):
    if isinstance(value, dict):
        return {k: without_abstracts(v) for k, v in value.items() if k != "abstract_inverted_index"}
    if isinstance(value, list):
        return [without_abstracts(v) for v in value]
    return value


def response_digest(data: dict) -> str:
    """The Provenance #14 SEARCH_DIGESTS convention."""
    return digest(without_abstracts(data))


def results_digest(data: dict) -> str:
    return digest(without_abstracts(data.get("results", [])))


def abstract_state(value) -> str:
    """ABSENT, STRIPPED (only a removal marker or null) or PRESENT (abstract text)."""
    found = []

    def walk(v):
        if isinstance(v, dict):
            for k, x in v.items():
                if k == "abstract_inverted_index":
                    found.append(x)
                else:
                    walk(x)
        elif isinstance(v, list):
            for x in v:
                walk(x)
    walk(value)
    if not found:
        return "ABSENT"
    if any(isinstance(x, (dict, list)) and x for x in found):
        return "PRESENT"
    return "STRIPPED"


def short_id(openalex_id: str) -> str:
    return openalex_id.rsplit("/", 1)[-1]


def ranked(data: dict) -> list[dict]:
    rows = []
    for rank, work in enumerate(data.get("results", []), 1):
        if not isinstance(work, dict) or not isinstance(work.get("id"), str):
            raise ContractError(f"INVALID_RESPONSE: result {rank} has no id")
        row = {"rank": rank, "id": short_id(work["id"]),
               "year": work.get("publication_year"), "title": work.get("display_name")}
        if "relevance_score" in work:
            row["score"] = work["relevance_score"]
        rows.append(row)
    return rows


def ranking_basis(spec: dict) -> dict:
    """What decides the order, and whether the response carries the field that decides it.

    'checkable' means the sort key is selected, so the order can be recomputed from
    the response. It does not mean the provider's tie-breaking is known.
    """
    params = dict(spec["params"])
    selected = None if "select" not in params else set(params["select"].split(","))
    searched = "search" in params or ".search:" in params.get("filter", "")
    if "sort" in params:
        key = params["sort"].split(":", 1)[0]
        basis = f"explicit sort {params['sort']}"
    elif searched:
        key, basis = "relevance_score", "provider default (relevance for a search)"
    else:
        key, basis = None, "provider default"
    return {"basis": basis, "sort_key": key,
            "checkable": key is not None and (selected is None or key in selected)}


def response_summary(data: dict) -> dict:
    meta = data.get("meta") if isinstance(data.get("meta"), dict) else {}
    results = data.get("results")
    if not isinstance(results, list):
        raise ContractError("INVALID_RESPONSE: no results list")
    return {"meta": {k: meta.get(k) for k in ("count", "page", "per_page")},
            "n_results": len(results),
            "response_digest": response_digest(data),
            "results_digest": results_digest(data),
            "abstracts": abstract_state(data),
            "ranked": ranked(data)}


def declared_checks(root: Path, spec: dict) -> dict:
    declared = spec["declared"]
    path = root / declared["path"]
    if not path.is_file():
        raise ContractError(f"MISSING_DECLARATION: {declared['path']}")
    data = path.read_bytes()
    text = normalize(data.decode("utf-8"))
    request = normalize(decoded_query(spec["params"]))
    missing_decl = [t for t in declared["requires"] if normalize(t) not in text]
    missing_req = [t for t in declared["requires"] if normalize(t) not in request]
    return {"declared_file_sha256_matches": sha256(data) == declared["sha256"],
            "declared_terms_in_declaration": not missing_decl,
            "declared_terms_in_request": not missing_req,
            "missing": {"declaration": missing_decl, "request": missing_req}}


def check_page_policy(spec: dict, summary: dict) -> dict:
    meta = summary["meta"]
    return {"first_page": meta.get("page") in (1, None),
            "within_per_page": summary["n_results"] <= per_page(spec)}


def to_bytes(value: object) -> bytes:
    return (canonical(value) + "\n").encode("utf-8")


def strip_secret(text: str, secret: str | None) -> str:
    return text.replace(secret, "[redacted]") if secret else text

