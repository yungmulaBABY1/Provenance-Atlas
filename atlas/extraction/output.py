"""Strict reader for a claim-extraction output (prompts/1-claim-extraction.txt) as received.

Reads the instrument's required output table, the Field 6 section statement,
the one-line summaries, the preflight line, and the run-prompt additions
SOURCE ANCHORS and READ RECORD. Markdown emphasis is part of the text as
received and is kept; offsets are Unicode code points into the exact bytes,
half-open. Anything that does not fit is reported, never repaired.
"""

from __future__ import annotations

import re

from ..contract import sha256

NAME = "atlas-claim-extraction-output"
VERSION = "1"

# The instrument's REQUIRED OUTPUT TABLE row labels.
TABLE_ROWS = {"1": "Literally measured", "2": "Source's strongest claim", "3": "Weaker defensible claim",
              "4": "Downstream claim", "5A": "Within-source inflation point + failure location",
              "5B": "Downstream inflation point + failure location", "6": "Claim under audit"}
SUMMARY_LABELS = ("CLAIM UNDER AUDIT", "WITHIN-SOURCE FAILURE LOCATION", "DOWNSTREAM FAILURE LOCATION",
                  "GAP TYPE", "MAP CONFIDENCE")
DISPOSITIONS = ("IDENTITY CONFIRMED", "INSTRUMENT VERSION UNVERIFIED", "VERSION COLLISION — UNRESOLVED")
ROW = re.compile(r"\| (1|2|3|4|5A|5B|6)\. ([^|]+?) \| (.+) \| ([^|]+?) \|")
SECTION_6 = "## 6. WHICH CLAIM IS THIS AUDIT EVALUATING?"
CLAIM_LEAD = "**Claim.** "
ANCHOR_HEAD = re.compile(r"(?:- )?\*\*(A(?:\d|D)\.\d+)\*\* · (.+)")
QUOTE_LINE = re.compile(r"> (.+)")
PAGE = re.compile(r"\bp\. (\d+)(?:, (.+))?$")
WITHHELD = re.compile(r"> \[QUOTE WITHHELD: source-light; sha256 ([0-9a-f]{64}); (\d+) chars\]")


def lines_with_offsets(text: str) -> list[tuple[int, str]]:
    result, offset = [], 0
    for line in text.split("\n"):
        result.append((offset, line))
        offset += len(line) + 1
    return result


def span(text: str, start: int, end: int, line: int) -> dict:
    return {"char_start": start, "char_end": end, "line": line, "text": text[start:end]}


def anchor_field(anchor_id: str) -> str:
    return "DEFINITION_CHECK" if anchor_id.startswith("AD.") else anchor_id[1]


def parse(text: str) -> dict:
    lines = lines_with_offsets(text)
    issues = []
    result = {"parser": {"name": NAME, "version": VERSION}, "preflight": None, "table": {},
              "field_6_section": None, "summaries": {}, "anchors": [], "sections": {}, "issues": issues}

    # Preflight line: the first line naming INSTRUMENT PREFLIGHT.
    pre = [(i, off, line) for i, (off, line) in enumerate(lines) if "INSTRUMENT PREFLIGHT:" in line]
    if pre:
        i, off, line = pre[0]
        found = [d for d in DISPOSITIONS if line.rstrip().endswith(d)]
        result["preflight"] = {**span(text, off, off + len(line), i + 1),
                               "disposition": found[0] if found else None}
        if not found:
            issues.append({"code": "PREFLIGHT_DISPOSITION_UNRECOGNIZED", "line": i + 1})
    else:
        issues.append({"code": "PREFLIGHT_MISSING"})

    # Section boundaries (## headings), recorded by hash so the public copy can be checked.
    heads = [(i, off, line) for i, (off, line) in enumerate(lines) if line.startswith("## ")]
    for n, (i, off, line) in enumerate(heads):
        end = heads[n + 1][1] if n + 1 < len(heads) else len(text)
        title = line[3:].strip()
        if title in result["sections"]:
            issues.append({"code": "DUPLICATE_SECTION", "title": title, "line": i + 1})
            continue
        body = text[off:end]
        result["sections"][title] = {"line": i + 1, "char_start": off, "char_end": end,
                                     "sha256": sha256(body.encode("utf-8"))}

    # Required output table rows.
    for i, (off, line) in enumerate(lines):
        match = ROW.fullmatch(line.rstrip())
        if not match:
            continue
        field, label, content, state = match.groups()
        if field in result["table"]:
            issues.append({"code": "DUPLICATE_TABLE_ROW", "field": field, "line": i + 1})
            result["table"][field]["status"] = "DUPLICATE_ROWS"
            continue
        expected = TABLE_ROWS[field]
        label_status = ("EXACT" if label == expected else
                        "SHORTENED" if expected.startswith(label) else "DIFFERENT")
        if label_status != "EXACT":
            issues.append({"code": f"TABLE_LABEL_{label_status}", "field": field, "line": i + 1,
                           "native_label": label, "instrument_label": expected})
        content_start = off + match.start(3)
        state_start = off + match.start(4)
        result["table"][field] = {"native_label": label, "instrument_label": expected,
                                  "label_status": label_status, "status": "USABLE",
                                  "content": span(text, content_start, content_start + len(content), i + 1),
                                  "verification_state": span(text, state_start, state_start + len(state), i + 1)}
    missing = [f for f in TABLE_ROWS if f not in result["table"]]
    if missing:
        issues.append({"code": "TABLE_ROW_MISSING", "fields": missing})

    # Field 6 section: the one-sentence statement the instrument requires.
    sec = [i for i, (_, line) in enumerate(lines) if line.rstrip() == SECTION_6]
    if len(sec) == 1:
        claims = []
        for j in range(sec[0] + 1, len(lines)):
            off, line = lines[j]
            if line.startswith("## "):
                break
            if line.startswith(CLAIM_LEAD):
                claims.append(span(text, off + len(CLAIM_LEAD), off + len(line.rstrip()), j + 1))
        if len(claims) == 1:
            result["field_6_section"] = {**claims[0], "status": "USABLE"}
        else:
            issues.append({"code": "FIELD_6_STATEMENT_" + ("MISSING" if not claims else "DUPLICATE"),
                           "lines": [c["line"] for c in claims]})
    else:
        issues.append({"code": "FIELD_6_SECTION_" + ("MISSING" if not sec else "DUPLICATE")})

    # One-line summaries.
    for label in SUMMARY_LABELS:
        found = []
        for i, (off, line) in enumerate(lines):
            for lead in (f"**{label}:** ", f"{label}: "):
                if line.startswith(lead):
                    found.append(span(text, off + len(lead), off + len(line.rstrip()), i + 1))
        if len(found) == 1:
            result["summaries"][label] = found[0]
        else:
            issues.append({"code": "SUMMARY_" + ("MISSING" if not found else "DUPLICATE"), "label": label})

    # SOURCE ANCHORS (run-prompt addition).
    start = result["sections"].get("SOURCE ANCHORS")
    end = result["sections"].get("READ RECORD")
    if not start:
        issues.append({"code": "SOURCE_ANCHORS_MISSING"})
    else:
        first = start["line"]
        last = end["line"] - 1 if end else len(lines)
        seen = set()
        i = first
        while i < last:
            off, line = lines[i]
            head = ANCHOR_HEAD.fullmatch(line.rstrip())
            if not head:
                i += 1
                continue
            anchor_id, meta = head.groups()
            entry = {"id": anchor_id, "field": anchor_field(anchor_id), "line": i + 1, "meta": meta,
                     "stated_page": None, "stated_section": None, "kind": None, "quote": None,
                     "withheld": None, "refers_to": re.findall(r"\bA(?:\d|D)\.\d+\b", meta)}
            parts = [p.strip() for p in meta.split(" · ")]
            page = PAGE.search(parts[-1]) if len(parts) > 1 else None
            if page:
                entry["stated_page"] = int(page.group(1))
                entry["stated_section"] = page.group(2)
            j = i + 1
            while j < last and not lines[j][1].strip():
                j += 1
            qoff, qline = lines[j] if j < last else (None, "")
            withheld = WITHHELD.fullmatch(qline.rstrip())
            quote = QUOTE_LINE.fullmatch(qline.rstrip()) if not withheld else None
            if withheld:
                entry["kind"] = "QUOTE"
                entry["withheld"] = {"quote_sha256": withheld.group(1), "chars": int(withheld.group(2)), "line": j + 1}
                i = j + 1
            elif quote and page:
                entry["kind"] = "QUOTE"
                entry["quote"] = span(text, qoff + 2, qoff + len(qline.rstrip()), j + 1)
                i = j + 1
            else:
                lowered = meta.lower()
                entry["kind"] = ("RECONSTRUCTION" if "author reconstruction" in lowered else
                                 "SAME_AS" if "same passage" in lowered else
                                 "ABSENCE" if "no passage" in lowered else "UNCLASSIFIED")
                if entry["kind"] == "UNCLASSIFIED":
                    issues.append({"code": "ANCHOR_UNCLASSIFIED", "anchor": anchor_id, "line": i + 1})
                i += 1
            if anchor_id in seen:
                issues.append({"code": "DUPLICATE_ANCHOR_ID", "anchor": anchor_id, "line": entry["line"]})
                entry["kind"] = "DUPLICATE_ID"
            seen.add(anchor_id)
            result["anchors"].append(entry)
    return result


def withheld_line(quote: str) -> str:
    return f"> [QUOTE WITHHELD: source-light; sha256 {sha256(quote.encode('utf-8'))}; {len(quote)} chars]"


def redact(text: str, keep: set[str]) -> str:
    """Replace every anchor quote line except those in `keep` with a hash placeholder."""
    parsed = parse(text)
    lines = text.split("\n")
    for entry in parsed["anchors"]:
        if entry["quote"] and entry["id"] not in keep:
            index = entry["quote"]["line"] - 1
            lines[index] = withheld_line(entry["quote"]["text"])
    return "\n".join(lines)
