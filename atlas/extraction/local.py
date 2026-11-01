"""Local stage: needs the private full output and the source PDF. Not run in CI.

Verifies the PDF and its pdftotext extraction against pinned hashes, matches
every quoted anchor against the extraction, and produces the public files:
anchor-verification.json, the redacted output, and the bounded evidence
excerpts. `verify` recomputes them and compares with the committed copies.
"""

from __future__ import annotations

from pathlib import Path
import subprocess
import tempfile

from . import ANCHOR_SCHEMA, VERSION
from . import anchors as matcher
from . import output
from ..contract import ContractError, canonical, load_json, read_artifact, require, sha256


def run_pdftotext(pdf: bytes, expected_tool: str, command: list[str]) -> str:
    version = subprocess.run(["pdftotext", "-v"], capture_output=True, text=True, check=False)
    tool = (version.stderr or version.stdout).splitlines()[0].strip()
    if tool != expected_tool:
        raise ContractError(f"EXTRACTION_TOOL_MISMATCH: have {tool!r}, pinned {expected_tool!r}")
    with tempfile.TemporaryDirectory(prefix="atlas-extract-") as directory:
        src, out = Path(directory) / "source.pdf", Path(directory) / "out.txt"
        src.write_bytes(pdf)
        argv = [str(src) if a == "<pdf>" else str(out) if a == "<out>" else a for a in command]
        result = subprocess.run(argv, capture_output=True, text=True, timeout=60, check=False)
        if result.returncode != 0:
            raise ContractError(f"EXTRACTION_FAILED: {result.stderr.strip()}")
        return out.read_bytes().decode("utf-8")


def committed_excerpts(context: dict, root: Path) -> list[dict]:
    """Excerpt spans already public for this source version, from the source packet."""
    data = read_artifact(root, context["source"]["sources_json"])
    source = load_json(data)["sources"][context["source"]["packet_source_id"]]
    return [{"id": e["id"], "start": e["extraction_start"], "end": e["extraction_end"], "sha256": e["sha256"]}
            for e in source["excerpts"]]


def produce(context: dict, root: Path, full_output: bytes, pdf: bytes) -> dict:
    local = context["local"]
    require(local, {"full_output_sha256": str, "pdf_sha256": str, "evidence_anchor_ids": list,
                    "excerpt_dir": str}, "local")
    if sha256(full_output) != local["full_output_sha256"]:
        raise ContractError("FULL_OUTPUT_HASH_MISMATCH")
    if sha256(pdf) != local["pdf_sha256"]:
        raise ContractError("SOURCE_PDF_HASH_MISMATCH")
    extraction_pin = context["source"]["extraction"]
    text = run_pdftotext(pdf, extraction_pin["tool"], extraction_pin["command"])
    if sha256(text.encode("utf-8")) != extraction_pin["output_sha256"]:
        raise ContractError("EXTRACTION_HASH_MISMATCH")
    raw = full_output.decode("utf-8")
    parsed = output.parse(raw)
    index = matcher.NormalizedIndex(text)
    public = committed_excerpts(context, root)
    evidence_ids = local["evidence_anchor_ids"]

    # Pass 1: match every quote and cut the declared evidence excerpts.
    entries, evidence_files = [], {}
    for anchor in parsed["anchors"]:
        entry = {"id": anchor["id"], "field": anchor["field"], "kind": anchor["kind"],
                 "stated_page": anchor["stated_page"], "stated_section": anchor["stated_section"],
                 "refers_to": anchor["refers_to"], "match": None, "page_consistent": None,
                 "within_public_excerpts": [], "published_verbatim": False}
        if anchor["kind"] == "QUOTE":
            result = matcher.match(anchor["quote"]["text"], text, index)
            entry["match"] = result
            if result["found_page"] is not None:
                entry["page_consistent"] = result["found_page"] == anchor["stated_page"]
            span = result["extraction_span"]
            if anchor["id"] in evidence_ids:
                if not span:
                    raise ContractError(f"EVIDENCE_ANCHOR_UNLOCATED: {anchor['id']} ({result['state']})")
                excerpt = text[span[0]:span[1]].encode("utf-8")
                evidence_files[f"{local['excerpt_dir']}/{anchor['id']}-excerpt.txt"] = excerpt
                public.append({"id": f"evidence:{anchor['id']}", "start": span[0], "end": span[1],
                               "sha256": sha256(excerpt)})
        entries.append(entry)
    missing = [a for a in evidence_ids if not any(e["id"] == a and e["match"] for e in entries)]
    if missing:
        raise ContractError(f"EVIDENCE_ANCHOR_MISSING: {missing}")
    # Pass 2: which quotes lie inside an excerpt that is public (packet or declared evidence).
    for entry in entries:
        span = entry["match"]["extraction_span"] if entry["match"] else None
        if span:
            entry["within_public_excerpts"] = sorted(
                e["id"] for e in public if e["start"] <= span[0] and span[1] <= e["end"])
            entry["published_verbatim"] = bool(entry["within_public_excerpts"])
    keep = {e["id"] for e in entries if e["published_verbatim"]}
    redacted = output.redact(raw, keep)
    record = {"schema": ANCHOR_SCHEMA, "producer": {"name": "atlas-extraction-local", "version": VERSION,
                                                   "code_sha256": sha256(Path(__file__).read_bytes()),
                                                   "matcher_sha256": sha256(Path(matcher.__file__).read_bytes()),
                                                   "parser": parsed["parser"]},
              "full_output_sha256": local["full_output_sha256"], "pdf_sha256": local["pdf_sha256"],
              "extraction": {**extraction_pin, "verified": "OUTPUT_HASH_MATCH",
                             "is_nfc": True, "pages": text.count("\f") + (0 if text.endswith("\f") else 1)},
              "public_excerpts": public, "redaction_rule": (
                  "A quote is published verbatim only if its extraction span lies inside an excerpt that is "
                  "already public (source packet) or is committed here as declared evidence. All other quotes "
                  "are replaced by their SHA-256 and length."),
              "redacted_output_sha256": sha256(redacted.encode("utf-8")),
              "anchors": entries}
    return {"anchor_verification": (canonical(record) + "\n").encode("utf-8"),
            "redacted_output": redacted.encode("utf-8"), "evidence_files": evidence_files}


def write(context: dict, root: Path, full_output: bytes, pdf: bytes) -> dict:
    produced = produce(context, root, full_output, pdf)
    paths = context["local"]["public_paths"]
    (root / paths["anchor_verification"]).write_bytes(produced["anchor_verification"])
    (root / paths["redacted_output"]).write_bytes(produced["redacted_output"])
    for path, data in produced["evidence_files"].items():
        (root / path).write_bytes(data)
    return produced


def verify(context: dict, root: Path, full_output: bytes, pdf: bytes) -> dict:
    """Recompute the public files from private inputs; every committed byte must match."""
    produced = produce(context, root, full_output, pdf)
    paths = context["local"]["public_paths"]
    differing = []
    if (root / paths["anchor_verification"]).read_bytes() != produced["anchor_verification"]:
        differing.append(paths["anchor_verification"])
    if (root / paths["redacted_output"]).read_bytes() != produced["redacted_output"]:
        differing.append(paths["redacted_output"])
    for path, data in produced["evidence_files"].items():
        if not (root / path).is_file() or (root / path).read_bytes() != data:
            differing.append(path)
    if differing:
        raise ContractError("LOCAL_VERIFY_MISMATCH: " + ", ".join(differing))
    return {"local_verify": "PASS", "files": [paths["anchor_verification"], paths["redacted_output"],
                                              *produced["evidence_files"]]}
