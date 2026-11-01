"""Match quoted anchors against a source text extraction. Deterministic; no repair.

States, as for Passage records:
  MATCH                  the quote is an exact code-point substring of the extraction;
  NORMALIZED_MATCH_ONLY  equal only after nfc-whitespace/2 (NFC + whitespace collapse);
  MISMATCH               neither.
No dehyphenation, soft-hyphen removal, stamp removal, NFKC or fuzzy matching is
applied: each can make scientifically distinct strings equal. A MISMATCH may carry
a diagnostic from a heuristic alignment; it is labelled as such and never changes
the state.
"""

from __future__ import annotations

import difflib
import unicodedata

from ..contract import NORMALIZER, normalize, sha256

DIAGNOSTIC = "DIAGNOSTIC_ONLY: heuristic alignment (difflib) of normalized texts; does not change the match state"


class NormalizedIndex:
    """nfc-whitespace/2 view of a text with a map back to original code points."""

    def __init__(self, text: str):
        if not unicodedata.is_normalized("NFC", text):
            raise ValueError("EXTRACTION_NOT_NFC: offset mapping requires NFC text")
        chars, origin = [], []
        pending_space = False
        for index, ch in enumerate(text):
            if ch.isspace():
                pending_space = bool(chars)
                continue
            if pending_space:
                chars.append(" ")
                origin.append(index - 1)
                pending_space = False
            chars.append(ch)
            origin.append(index)
        self.text = "".join(chars)
        self.origin = origin
        assert self.text == normalize(text)

    def spans(self, needle: str) -> list[tuple[int, int]]:
        found, start = [], 0
        while (hit := self.text.find(needle, start)) != -1:
            found.append((self.origin[hit], self.origin[hit + len(needle) - 1] + 1))
            start = hit + 1
        return found


def exact_spans(text: str, needle: str) -> list[tuple[int, int]]:
    found, start = [], 0
    while (hit := text.find(needle, start)) != -1:
        found.append((hit, hit + len(needle)))
        start = hit + 1
    return found


def page_of(text: str, offset: int) -> int:
    """1-based page: pdftotext separates pages with form feed."""
    return text.count("\f", 0, offset) + 1


def describe(chars: str) -> dict:
    if len(chars) <= 3:
        return {"length": len(chars), "code_points": [f"U+{ord(c):04X}" for c in chars]}
    return {"length": len(chars)}


def diagnose(quote: str, index: NormalizedIndex) -> dict:
    nq = normalize(quote)
    matcher = difflib.SequenceMatcher(None, nq, index.text, autojunk=False)
    longest = matcher.find_longest_match(0, len(nq), 0, len(index.text))
    # Start before the aligned position and run well past the quote's length, so
    # insertions in the extraction (soft hyphens, page stamps) do not clip the window.
    lo = max(0, longest.b - longest.a - 40)
    window = index.text[lo:lo + len(nq) + 400]
    ops = difflib.SequenceMatcher(None, nq, window, autojunk=False).get_opcodes()
    trimmed = [op for op in ops if op[0] != "equal"]
    # Trailing text after the aligned quote is window slack, not a difference.
    if trimmed and trimmed[-1][0] == "insert" and trimmed[-1][1] == len(nq):
        trimmed = trimmed[:-1]
    # Leading text before the alignment start likewise.
    if trimmed and trimmed[0][0] == "insert" and trimmed[0][1] == 0:
        trimmed = trimmed[1:]
    return {"basis": DIAGNOSTIC, "aligned_extraction_start": index.origin[lo] if index.origin else None,
            "difference_count": len(trimmed),
            "first_differences": [{"op": tag, "quote": describe(nq[i1:i2]), "extraction": describe(window[j1:j2])}
                                  for tag, i1, i2, j1, j2 in trimmed[:4]]}


def match(quote: str, text: str, index: NormalizedIndex) -> dict:
    exact = exact_spans(text, quote)
    normalized = index.spans(normalize(quote))
    state = "MATCH" if exact else "NORMALIZED_MATCH_ONLY" if normalized else "MISMATCH"
    spans = exact or normalized
    result = {"state": state, "exact_occurrences": len(exact), "normalized_occurrences": len(normalized),
              "quote_sha256": sha256(quote.encode("utf-8")),
              "normalized_quote_sha256": sha256(normalize(quote).encode("utf-8")),
              "quote_chars": len(quote), "normalizer": NORMALIZER, "extraction_span": None,
              "extraction_span_normalized_sha256": None, "found_page": None, "location": None,
              "diagnostic": None}
    if len(spans) == 1:
        start, end = spans[0]
        result.update(extraction_span=[start, end], found_page=page_of(text, start), location="UNIQUE",
                      extraction_span_normalized_sha256=sha256(normalize(text[start:end]).encode("utf-8")))
    elif len(spans) > 1:
        result["location"] = "AMBIGUOUS_MULTIPLE_OCCURRENCES"
    else:
        result["location"] = "NOT_FOUND"
        result["diagnostic"] = diagnose(quote, index)
    return result
