"""Strict parser for the citation-network instrument's own claim statements.

Grammar implemented: the DEGRADED STANDALONE MODE fallback and the PRE-AUDIT
CLAIM CONFIRMATION lines of prompts/research-analysis/2-citation-network.txt
(vendored baseline, git blob 7ac79f0d):

    CLAIM MAP MISSING: running in degraded standalone mode. ...
    CLAIM MAP: SELF-GENERATED - PROVISIONAL
    - Field 1 - What was literally measured: <text>
    - Field 3 - Weaker defensible claim: <text>
    - Field 6 - Claim under audit: <text>

    PRE-AUDIT CLAIM CONFIRMATION
    - Claim under audit (map field 6): <text>
    - What was literally measured ... (map field 1): <text>
    - Weaker defensible claim (map field 3): <text>
    - Target layer: <text>

The separator may be a hyphen, en dash or em dash. Text may follow the colon on
the same line or start on indented continuation lines. Offsets are Unicode code
points into the exact output text, half-open.

Every entry is kept, including duplicates and entries whose label does not
belong to their field number. Each field gets a status; only a USABLE field
(exactly one non-empty entry, label matching its number) may serve as a
linking target. Nothing is repaired, merged or guessed.
"""

from __future__ import annotations

import re

NAME = "atlas-citation-network-claim-statements"
# 2: number/label pairing validated; every entry kept; per-field status.
VERSION = "2"
FALLBACK_FIELDS = ("1", "3", "6")
# Labels the instrument assigns to each fallback field number.
EXPECTED_LABELS = {"1": "What was literally measured", "3": "Weaker defensible claim",
                   "6": "Claim under audit"}
FIELD_STATUSES = ("USABLE", "LABEL_MISMATCH", "DUPLICATE_ENTRIES", "EMPTY", "OUTSIDE_FALLBACK")

WARNING = re.compile(r"CLAIM MAP MISSING:")
MAP_HEADING = re.compile(r"CLAIM MAP: SELF-GENERATED\s+[—–-]\s+PROVISIONAL")
MAP_ITEM = re.compile(r"- Field (\d+[AB]?)\s+[—–-]\s+([^:\n]+):(?:[ \t]+(\S.*))?")
CONFIRMATION_HEADING = "PRE-AUDIT CLAIM CONFIRMATION"
CONFIRMATION_ITEMS = (
    ("field_6", re.compile(r"- (Claim under audit \(map field 6\)):(?:[ \t]+(\S.*))?")),
    ("field_1", re.compile(r"- (What was literally measured[^:\n]*\(map field 1\)):(?:[ \t]+(\S.*))?")),
    ("field_3", re.compile(r"- (Weaker defensible claim \(map field 3\)):(?:[ \t]+(\S.*))?")),
    ("target_layer", re.compile(r"- (Target layer):(?:[ \t]+(\S.*))?")),
)
OTHER_BULLET = re.compile(r"- \S")


def lines_with_offsets(text: str) -> list[tuple[int, str]]:
    """(start code-point offset, line text without newline) for each line."""
    result, offset = [], 0
    for line in text.split("\n"):
        result.append((offset, line))
        offset += len(line) + 1
    return result


def top_level(line: str) -> bool:
    return bool(line) and not line[0].isspace() and not line.startswith("|")


def label_match(written: str, expected: str) -> str:
    if written == expected:
        return "EXACT"
    if " ".join(written.split()).casefold() == " ".join(expected.split()).casefold():
        return "CASE_OR_SPACE_ONLY"
    return "MISMATCH"


def item_span(lines, index: int, match: re.Match, text_group: int, text: str) -> tuple[dict, int]:
    """Span from the first text character to the end of the last continuation line."""
    offset, line = lines[index]
    start = end = None
    if match.group(text_group):
        start = offset + match.start(text_group)
        end = offset + len(line.rstrip())
    last = index
    cursor = index + 1
    while cursor < len(lines) and lines[cursor][1].startswith("  ") and lines[cursor][1].strip():
        coff, cline = lines[cursor]
        if start is None:
            start = coff + (len(cline) - len(cline.lstrip()))
        end = coff + len(cline.rstrip())
        last = cursor
        cursor += 1
    if start is None:
        return {"line_start": index + 1, "line_end": index + 1, "char_start": None,
                "char_end": None, "text": None}, cursor
    return {"line_start": index + 1 if match.group(text_group) else index + 2,
            "line_end": last + 1, "char_start": start, "char_end": end,
            "text": text[start:end]}, cursor


def field_status(entries: list[dict], outside: bool = False) -> str:
    if outside:
        return "OUTSIDE_FALLBACK"
    if len(entries) > 1:
        return "DUPLICATE_ENTRIES"
    if entries[0]["text"] is None:
        return "EMPTY"
    if entries[0].get("label_match") == "MISMATCH":
        return "LABEL_MISMATCH"
    return "USABLE"


def parse(text: str) -> dict:
    lines = lines_with_offsets(text)
    issues = []
    warning_lines = [i + 1 for i, (_, line) in enumerate(lines) if top_level(line) and WARNING.match(line)]
    heading_lines = [i + 1 for i, (_, line) in enumerate(lines)
                     if top_level(line) and MAP_HEADING.fullmatch(line.rstrip())]
    result = {"parser": {"name": NAME, "version": VERSION},
              "warning": {"present": bool(warning_lines), "lines": warning_lines},
              "map": {"state": "ABSENT", "heading_line": None, "native_label": None,
                      "entries": {}, "field_status": {}},
              "confirmation": {"state": "ABSENT", "heading_line": None, "entries": {}, "item_status": {}},
              "map_gap_lines": [i + 1 for i, (_, line) in enumerate(lines) if "MAP GAP:" in line],
              "issues": issues}

    if len(heading_lines) > 1:
        issues.append({"code": "DUPLICATE_MAP_HEADING", "lines": heading_lines})
        result["map"]["state"] = "MALFORMED"
    elif heading_lines:
        index = heading_lines[0] - 1
        result["map"].update(heading_line=index + 1, native_label=lines[index][1].rstrip())
        entries = result["map"]["entries"]
        cursor = index + 1
        while cursor < len(lines):
            line = lines[cursor][1]
            if not line.strip():
                cursor += 1
                continue
            match = MAP_ITEM.fullmatch(line.rstrip())
            if not match:
                break
            span, cursor = item_span(lines, cursor, match, 3, text)
            number, written = match.group(1), match.group(2).strip()
            expected = EXPECTED_LABELS.get(number)
            entries.setdefault(number, []).append({
                "native_label": written, "expected_label": expected,
                "label_match": label_match(written, expected) if expected else None, **span})
        status = result["map"]["field_status"]
        for number, items in entries.items():
            status[number] = field_status(items, outside=number not in FALLBACK_FIELDS)
            code = {"LABEL_MISMATCH": "FIELD_LABEL_MISMATCH", "DUPLICATE_ENTRIES": "DUPLICATE_MAP_FIELD",
                    "EMPTY": "EMPTY_MAP_FIELD", "OUTSIDE_FALLBACK": "FIELD_OUTSIDE_FALLBACK"}.get(status[number])
            if code:
                issues.append({"code": code, "field": number, "lines": [e["line_start"] for e in items],
                               "native_labels": [e["native_label"] for e in items]})
        missing = [f for f in FALLBACK_FIELDS if f not in entries]
        if missing:
            issues.append({"code": "FALLBACK_FIELD_MISSING", "fields": missing})
        clean = not missing and all(status[f] == "USABLE" for f in entries)
        result["map"]["state"] = "PRESENT" if clean else "PRESENT_WITH_DEFECTS"
    if result["map"]["state"] in ("PRESENT", "PRESENT_WITH_DEFECTS") and not warning_lines:
        issues.append({"code": "STANDALONE_WARNING_MISSING"})

    confirmation_lines = [i + 1 for i, (_, line) in enumerate(lines)
                          if top_level(line) and line.rstrip() == CONFIRMATION_HEADING]
    if len(confirmation_lines) > 1:
        issues.append({"code": "DUPLICATE_CONFIRMATION_HEADING", "lines": confirmation_lines})
        result["confirmation"]["state"] = "MALFORMED"
    elif confirmation_lines:
        index = confirmation_lines[0] - 1
        entries = result["confirmation"]["entries"]
        cursor = index + 1
        while cursor < len(lines):
            line = lines[cursor][1]
            if not line.strip():
                cursor += 1
                continue
            stripped = line.rstrip()
            found = next(((key, m) for key, pattern in CONFIRMATION_ITEMS
                          if (m := pattern.fullmatch(stripped))), None)
            if found:
                key, match = found
                span, cursor = item_span(lines, cursor, match, 2, text)
                entries.setdefault(key, []).append({"native_label": match.group(1), **span})
                continue
            if OTHER_BULLET.match(line):
                # Other bullets (e.g. the standalone warning repeat) are allowed and skipped.
                cursor += 1
                while cursor < len(lines) and lines[cursor][1].startswith("  ") and lines[cursor][1].strip():
                    cursor += 1
                continue
            break
        result["confirmation"]["heading_line"] = index + 1
        status = result["confirmation"]["item_status"]
        for key, items in entries.items():
            status[key] = field_status(items)
            code = {"DUPLICATE_ENTRIES": "DUPLICATE_CONFIRMATION_LINE",
                    "EMPTY": "EMPTY_CONFIRMATION_LINE"}.get(status[key])
            if code:
                issues.append({"code": code, "item": key, "lines": [e["line_start"] for e in items]})
        if not entries:
            result["confirmation"]["state"] = "UNRECOGNIZED_FORMAT"
            issues.append({"code": "CONFIRMATION_FORMAT_UNRECOGNIZED", "line": index + 1})
        else:
            missing = [k for k, _ in CONFIRMATION_ITEMS if k not in entries]
            if missing:
                issues.append({"code": "CONFIRMATION_LINE_MISSING", "items": missing})
            clean = not missing and all(s == "USABLE" for s in status.values())
            result["confirmation"]["state"] = "PRESENT" if clean else "PRESENT_WITH_DEFECTS"
    return result


def locate_cell(text: str, line_number: int, value: str) -> dict | None:
    """Exact span of a table-cell value on a one-based line, or None if not found once."""
    lines = lines_with_offsets(text)
    if not 1 <= line_number <= len(lines):
        return None
    offset, line = lines[line_number - 1]
    if line.count(value) != 1:
        return None
    start = offset + line.index(value)
    return {"line_start": line_number, "line_end": line_number,
            "char_start": start, "char_end": start + len(value)}
