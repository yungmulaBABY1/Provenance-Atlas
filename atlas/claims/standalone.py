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
the same line or start on indented continuation lines. Anything else is
reported as an issue and left unparsed; nothing is repaired or guessed.
Offsets are Unicode code points into the exact output text, half-open.
"""

from __future__ import annotations

import re

NAME = "atlas-citation-network-claim-statements"
VERSION = "1"
FALLBACK_FIELDS = ("1", "3", "6")

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


def item_span(lines, index: int, match: re.Match, text_group: int) -> tuple[dict, int]:
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
            "line_end": last + 1, "char_start": start, "char_end": end}, cursor


def parse(text: str) -> dict:
    lines = lines_with_offsets(text)
    issues = []
    warning_lines = [i + 1 for i, (_, line) in enumerate(lines) if top_level(line) and WARNING.match(line)]
    heading_lines = [i + 1 for i, (_, line) in enumerate(lines)
                     if top_level(line) and MAP_HEADING.fullmatch(line.rstrip())]
    result = {"parser": {"name": NAME, "version": VERSION},
              "warning": {"present": bool(warning_lines), "lines": warning_lines},
              "map": {"state": "ABSENT", "heading_line": None, "native_label": None, "fields": {}},
              "confirmation": {"state": "ABSENT", "heading_line": None, "items": {}},
              "map_gap_lines": [i + 1 for i, (_, line) in enumerate(lines) if "MAP GAP:" in line],
              "issues": issues}

    if len(heading_lines) > 1:
        issues.append({"code": "DUPLICATE_MAP_HEADING", "lines": heading_lines})
        result["map"]["state"] = "MALFORMED"
    elif heading_lines:
        index = heading_lines[0] - 1
        result["map"].update(state="PRESENT", heading_line=index + 1, native_label=lines[index][1].rstrip())
        cursor = index + 1
        while cursor < len(lines):
            line = lines[cursor][1]
            if not line.strip():
                cursor += 1
                continue
            match = MAP_ITEM.fullmatch(line.rstrip())
            if not match:
                break
            span, cursor = item_span(lines, cursor, match, 3)
            number = match.group(1)
            if span["char_start"] is None:
                issues.append({"code": "EMPTY_MAP_FIELD", "field": number, "line": span["line_start"]})
                continue
            if number in result["map"]["fields"]:
                issues.append({"code": "DUPLICATE_MAP_FIELD", "field": number, "line": span["line_start"]})
                continue
            if number not in FALLBACK_FIELDS:
                issues.append({"code": "FIELD_OUTSIDE_FALLBACK", "field": number, "line": span["line_start"]})
            result["map"]["fields"][number] = {"native_label": match.group(2).strip(), **span,
                                               "text": text[span["char_start"]:span["char_end"]]}
        missing = [f for f in FALLBACK_FIELDS if f not in result["map"]["fields"]]
        if missing:
            issues.append({"code": "FALLBACK_FIELD_MISSING", "fields": missing})
    if result["map"]["state"] == "PRESENT" and not warning_lines:
        issues.append({"code": "STANDALONE_WARNING_MISSING"})

    confirmation_lines = [i + 1 for i, (_, line) in enumerate(lines)
                          if top_level(line) and line.rstrip() == CONFIRMATION_HEADING]
    if len(confirmation_lines) > 1:
        issues.append({"code": "DUPLICATE_CONFIRMATION_HEADING", "lines": confirmation_lines})
        result["confirmation"]["state"] = "MALFORMED"
    elif confirmation_lines:
        index = confirmation_lines[0] - 1
        items = result["confirmation"]["items"]
        cursor = index + 1
        recognized_any = False
        while cursor < len(lines):
            line = lines[cursor][1]
            if not line.strip():
                cursor += 1
                continue
            stripped = line.rstrip()
            for key, pattern in CONFIRMATION_ITEMS:
                match = pattern.fullmatch(stripped)
                if match:
                    break
            else:
                match = None
            if match:
                recognized_any = True
                span, cursor = item_span(lines, cursor, match, 2)
                if span["char_start"] is None:
                    issues.append({"code": "EMPTY_CONFIRMATION_LINE", "item": key, "line": span["line_start"]})
                elif key in items:
                    issues.append({"code": "DUPLICATE_CONFIRMATION_LINE", "item": key, "line": span["line_start"]})
                else:
                    items[key] = {"native_label": match.group(1), **span,
                                  "text": text[span["char_start"]:span["char_end"]]}
                continue
            if OTHER_BULLET.match(line):
                # Other bullets (e.g. the standalone warning repeat) are allowed and skipped.
                cursor += 1
                while cursor < len(lines) and lines[cursor][1].startswith("  ") and lines[cursor][1].strip():
                    cursor += 1
                continue
            break
        result["confirmation"]["heading_line"] = index + 1
        if not recognized_any:
            result["confirmation"]["state"] = "UNRECOGNIZED_FORMAT"
            issues.append({"code": "CONFIRMATION_FORMAT_UNRECOGNIZED", "line": index + 1})
        else:
            result["confirmation"]["state"] = "PRESENT"
            missing = [k for k, _ in CONFIRMATION_ITEMS if k not in items]
            if missing:
                issues.append({"code": "CONFIRMATION_LINE_MISSING", "items": missing})
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
