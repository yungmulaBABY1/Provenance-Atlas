#!/usr/bin/env python3
"""Remove abstract text from the Acemoglu v1 run's committed JSON (rights cleanup, 2026-11-05).

    python3 -I strip_abstracts.py SOURCE --write
    python3 -I strip_abstracts.py SOURCE --check COMMITTED

SOURCE is the run folder (examples/research/acemoglu-colonial-origins) as it was before the
cleanup, for example extracted with `git archive 6c651d7 <folder>`. --write edits SOURCE in
place. --check edits nothing: it computes the cleanup from SOURCE and confirms that COMMITTED
(the folder as committed after the cleanup) holds exactly that result, and that no abstract
value is left in COMMITTED.

Why: OpenAlex abstract_inverted_index values, Crossref abstracts and the plain-text abstracts in
the run's coding inputs are reconstructable abstract text, and this repository is public.

What changes, and nothing else:
  - API responses (citation-network/metadata/raw-api/, sources/reception/): every non-null
    abstract_inverted_index, and every non-empty "abstract" string, becomes null.
  - Coding inputs (metadata/top50_coded_inputs.json, metadata/recent25_coded_inputs.json) and
    metadata/lock_abstracts.json: every non-empty abstract string becomes a non-empty marker,
    "[abstract removed 2026-11-05; N words]". scripts/gen_tables.py labels a row
    ABSTRACT-CONFIRMED or LOCATED by whether that field is non-empty (lines 64 and 82), so the
    marker keeps those labels; null would silently flip them.
Each edit replaces only the value's bytes, so formatting and every other byte are unchanged.
The result is re-parsed and compared with the expected object before anything is written.

Writes ABSTRACTS_STRIPPED.json and ABSTRACTS_STRIPPED.txt in the run folder: per file the
sha256 before and after and the number of fields replaced; per work its identifier and the
abstract's word count (no text).
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
from pathlib import Path

DATE = "2026-11-05"
MARKER_FILES = {"citation-network/metadata/top50_coded_inputs.json",
                "citation-network/metadata/recent25_coded_inputs.json",
                "citation-network/metadata/lock_abstracts.json"}
SCAN_DIRS = ["citation-network/metadata", "sources/reception"]
# Left unchanged: the AJR challenge records (tests/atlas/challenge/ajr2001/) cite these five
# search responses whole, by sha256, as the evidence two reviewers inspected. A stripped copy
# would not be the file they saw, so these keep their abstracts until the owner decides how
# pinned evidence should be handled.
PINNED_KEPT = {f"citation-network/metadata/raw-api/lock_F{n}.json" for n in (1, 2, 3, 4, 6)}
KEYS = ("abstract_inverted_index", "abstract")


def words(value) -> int:
    if isinstance(value, dict):        # OpenAlex inverted index: one position per word
        return sum(len(p) for p in value.values())
    return len(re.sub(r"<[^>]+>", " ", value).split())


def present(value) -> bool:
    return bool(value) and (isinstance(value, dict) or isinstance(value, str))


MARKER_RE = re.compile(r"\[abstract removed \d{4}-\d{2}-\d{2}; \d+ words\]")


def abstract_values(obj, rel: str) -> list:
    """Every non-empty abstract value in a parsed file (markers included)."""
    if rel.endswith("lock_abstracts.json"):
        return [v for v in obj.values() if isinstance(v, str) and v]
    out = []

    def walk(node):
        if isinstance(node, dict):
            for key, value in node.items():
                if key in KEYS and present(value):
                    out.append(value)
                else:
                    walk(value)
        elif isinstance(node, list):
            for value in node:
                walk(value)
    walk(obj)
    return out


def marker(value) -> str:
    return f"[abstract removed {DATE}; {words(value)} words]"


def plan(obj, rel: str):
    """Return (expected object, [(identifier, word count, replacement JSON)] in document order)."""
    found = []
    use_marker = rel in MARKER_FILES

    def ident(node, fallback):
        for key in ("id", "DOI", "node", "rank", "paperId"):
            if isinstance(node, dict) and key in node:
                return str(node[key])
        return fallback

    def walk(node, owner, fallback):
        if isinstance(node, dict):
            out = {}
            here = ident(node, fallback)
            for key, value in node.items():
                if key in KEYS and present(value):
                    new = marker(value) if use_marker else None
                    found.append((here, words(value), json.dumps(new)))
                    out[key] = new
                else:
                    out[key] = walk(value, node, f"{fallback}/{key}")
            return out
        if isinstance(node, list):
            return [walk(v, owner, f"{fallback}[{i}]") for i, v in enumerate(node)]
        return node

    if rel.endswith("lock_abstracts.json"):          # {source key: plain-text abstract}
        expected = {}
        for key, value in obj.items():
            if isinstance(value, str) and value:
                found.append((key, words(value), json.dumps(marker(value))))
                expected[key] = marker(value)
            else:
                expected[key] = value
        return expected, found
    return walk(obj, None, ""), found


def value_spans(raw: str, rel: str, obj) -> list[tuple[int, int]]:
    decoder = json.JSONDecoder()
    if rel.endswith("lock_abstracts.json"):
        names = [k for k, v in obj.items() if isinstance(v, str) and v]
    else:
        names = list(KEYS)
    pattern = re.compile("|".join(r'(?<!\\)"' + re.escape(n) + r'"\s*:\s*' for n in names))
    spans = []
    for m in pattern.finditer(raw):
        if spans and m.start() < spans[-1][1]:
            continue                                  # inside a value already taken
        value, end = decoder.raw_decode(raw, m.end())
        if present(value):
            spans.append((m.end(), end))
    return spans


def strip_file(path: Path, rel: str):
    raw = path.read_text(encoding="utf-8")
    obj = json.loads(raw)
    expected, found = plan(obj, rel)
    if not found:
        return None
    spans = value_spans(raw, rel, obj)
    if len(spans) != len(found):
        raise SystemExit(f"{rel}: {len(spans)} value spans in the text, {len(found)} in the object")
    out, last = [], 0
    for (start, end), (_, _, replacement) in zip(spans, found):
        out += [raw[last:start], replacement]
        last = end
    new = "".join(out) + raw[last:]
    if json.loads(new) != expected:
        raise SystemExit(f"{rel}: edited text does not parse to the expected object")
    return new, found, hashlib.sha256(raw.encode()).hexdigest(), \
        hashlib.sha256(new.encode()).hexdigest()


def main() -> int:
    if len(sys.argv) < 3 or sys.argv[2] not in {"--write", "--check"}:
        raise SystemExit(__doc__)
    root = Path(sys.argv[1])
    check = sys.argv[2] == "--check"
    files, works, edits, kept = [], [], {}, []
    for scan in SCAN_DIRS:
        for path in sorted((root / scan).rglob("*.json")):
            rel = path.relative_to(root).as_posix()
            if rel in PINNED_KEPT:
                kept.append({"file": rel, "fields_left": len(plan(
                    json.loads(path.read_text(encoding="utf-8")), rel)[1]),
                    "sha256": hashlib.sha256(path.read_bytes()).hexdigest()})
                continue
            result = strip_file(path, rel)
            if result is None:
                continue
            new, found, before, after = result
            edits[path] = new
            files.append({"file": rel, "sha256_before": before, "sha256_after": after,
                          "fields_replaced": len(found),
                          "replacement": "marker" if rel in MARKER_FILES else "null"})
            works += [{"file": rel, "id": i, "words": n} for i, n, _ in found]
    manifest = {"date": DATE, "reason": "abstract text (OpenAlex abstract indexes, Crossref "
                "abstracts, plain-text abstracts) removed: reconstructable abstract text in a "
                "public repository", "files": files, "works": works,
                "fields_replaced": sum(f["fields_replaced"] for f in files),
                "kept_pinned": kept, "kept_reason": "cited whole, by sha256, as reviewer "
                "evidence in tests/atlas/challenge/ajr2001/ (challenge records)"}
    text = render(manifest)
    if check:
        committed = Path(sys.argv[3])
        problems = [rel for rel in (p.relative_to(root).as_posix() for p in edits)
                    if (committed / rel).read_text(encoding="utf-8") != edits[root / rel]]
        if json.loads((committed / "ABSTRACTS_STRIPPED.json").read_text()) != manifest:
            problems.append("ABSTRACTS_STRIPPED.json")
        if (committed / "ABSTRACTS_STRIPPED.txt").read_text() != text:
            problems.append("ABSTRACTS_STRIPPED.txt")
        for scan in SCAN_DIRS:                        # nothing left behind
            for path in sorted((committed / scan).rglob("*.json")):
                rel = path.relative_to(committed).as_posix()
                if rel in PINNED_KEPT:
                    continue
                left = abstract_values(json.loads(path.read_text(encoding="utf-8")), rel)
                if rel in MARKER_FILES:
                    left = [v for v in left if not MARKER_RE.fullmatch(str(v))]
                if left:
                    problems.append(f"{rel}: {len(left)} abstract value(s) left")
        print("CHECK " + ("PASS" if not problems else "FAIL"))
        for problem in problems:
            print("  " + problem)
        return 0 if not problems else 1
    for path, new in edits.items():
        path.write_text(new, encoding="utf-8")
    (root / "ABSTRACTS_STRIPPED.json").write_text(json.dumps(manifest, indent=1) + "\n")
    (root / "ABSTRACTS_STRIPPED.txt").write_text(text)
    print(f"{len(files)} files, {manifest['fields_replaced']} fields replaced")
    return 0


def render(m: dict) -> str:
    lines = [
        "ABSTRACTS STRIPPED: Acemoglu v1 run (examples/research/acemoglu-colonial-origins/)",
        f"Date: {m['date']}. Made by tools/strip_abstracts.py; ABSTRACTS_STRIPPED.json holds the",
        "same record in machine-readable form.",
        "",
        "Reason: OpenAlex abstract indexes, Crossref abstracts and the plain-text abstracts in the",
        "coding inputs are reconstructable abstract text, and this repository is public.",
        "",
        "What changed: only the abstract values. API responses get null. The coding inputs and",
        "lock_abstracts.json get a non-empty marker, because scripts/gen_tables.py labels a row",
        "ABSTRACT-CONFIRMED or LOCATED by whether the field is non-empty; the marker keeps those",
        "labels. No receipt pins any of the files changed.",
        "",
        "The run's retrieval log (citation-network/retrieval/retrieval_log.jsonl, pinned by the",
        "import receipt) is unchanged: it keeps the hashes of the responses as retrieved. For",
        "the raw-api files, those are the 'before' hashes below.",
        "",
        "Not changed: git history. The originals remain in commits before this one; removing them",
        "from history is the repository owner's decision.",
        "",
        f"Total: {len(m['files'])} files, {m['fields_replaced']} abstract fields replaced, "
        f"{len({w['id'] for w in m['works']})} distinct identifiers.",
        "",
        "Per file (sha256 before, sha256 after, fields replaced, replacement)",
        "====================================================================",
    ]
    for f in m["files"]:
        lines += [f["file"], f"  before {f['sha256_before']}", f"  after  {f['sha256_after']}",
                  f"  {f['fields_replaced']} replaced with {f['replacement']}"]
    lines += ["", "Kept unchanged (abstracts remain)", "=================================",
              "These five search responses are cited whole, by sha256, as the evidence two",
              "reviewers inspected (tests/atlas/challenge/ajr2001/, challenge records). A stripped",
              "copy would not be the file they saw. How to handle pinned evidence is the",
              "repository owner's decision."]
    lines += [f"{k['file']}\t{k['fields_left']} abstract fields\tsha256 {k['sha256']}"
              for k in m["kept_pinned"]]
    lines += ["", "Per work (file, identifier, word count; no text)",
              "================================================"]
    lines += [f"{w['file']}\t{w['id']}\t{w['words']}" for w in m["works"]]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    sys.exit(main())
