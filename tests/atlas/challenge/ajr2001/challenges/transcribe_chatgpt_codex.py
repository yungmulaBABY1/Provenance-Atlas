"""How ChatGPT/Codex's answer was transcribed into three challenge artifacts.

Source: source/chatgpt-codex-answer-2026-11-04.txt, a byte copy of the answer the
repository owner supplied on 4 November 2026 (sha256 36dbb0c3...).

Every text field is one line of that file, chosen by line number below. A leading
"* " bullet is dropped, and nothing else is changed; the invisible link characters
are kept. atlas.challenge checks again at build time that every text field occurs in
the source.

What the recorder arranged, and you should check:
  - the split into parts;
  - the outcome given to each part. Each part's first line is the reviewer's own
    labelled line, and this script asserts that the label matches;
  - the evidence list, built from each "Evidence relied on" block. Commits and
    working papers are EXTERNAL because the build cannot resolve them.

Run from the repository root: python tests/atlas/challenge/ajr2001/challenges/transcribe_chatgpt_codex.py
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import sys

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[4]
sys.path.insert(0, str(ROOT))

from atlas.challenge.__main__ import template  # noqa: E402
from atlas.challenge.build import build  # noqa: E402
from atlas.contract import load_json, sha256  # noqa: E402

SOURCE = HERE / "source/chatgpt-codex-answer-2026-11-04.txt"
LINES = SOURCE.read_text(encoding="utf-8").split("\n")
A = "examples/research/acemoglu-colonial-origins/"
C = A + "citation-network/"
INSTRUMENT = "prompts/research-analysis/2-citation-network.txt"


def line(n: int) -> str:
    text = LINES[n - 1]
    assert text.strip(), f"line {n} is empty"
    return text[2:] if text.startswith("* ") else text


def lines(*ns: int) -> list[str]:
    return [line(n) for n in ns]


def span(a: int, b: int) -> list[int]:
    return list(range(a, b + 1))


def file(path: str, first: int | None = None, last: int | None = None) -> dict:
    entry = {"kind": "FILE", "path": path, "sha256": sha256((ROOT / path).read_bytes())}
    if first is not None:
        entry["lines"] = [first, last if last is not None else first]
    return entry


def external(identifier: str, note: str) -> dict:
    return {"kind": "EXTERNAL", "identifier": identifier, "note": note}


def part(name: str, outcome: str, ns: list[int]) -> dict:
    first = line(ns[0])
    assert re.search(rf"— {outcome}[.:]", first), f"part {name}: {outcome} is not the label in {first[:60]!r}"
    return {"part": name, "outcome": outcome, "reasons": lines(*ns)}


COMMON = {
    "challenger": {"identity": "ChatGPT/Codex",
                   "kind": "MODEL_AGENT",
                   "context": ("This review session, as stated by the reviewer. Run separately and supplied by the "
                               "repository owner on 4 November 2026. Reviewed the repository at commit 9f371b0.")},
    "relation_to_run": {"producer": "NO", "atlas_code_author": "NO",
                        "basis": "DECLARED_BY_CHALLENGER: " + line(12)},
    "recorded_by": ("Claude (Anthropic), Claude Code session 017YUqUaM2ka4XtLriA1p3fD, which is the code author. "
                    "It transcribed the reviewer's plain-language answer as supplied by the repository owner, "
                    "pinned in transcribed_from. Text fields are copied verbatim, line by line. The recorder "
                    "arranged the parts, the outcome per part (each part's first line is the reviewer's own "
                    "labelled line) and the evidence list, using transcribe_chatgpt_codex.py. performed_at is "
                    "the date the owner supplied the answer (US/Pacific); the reviewer stated no date. The "
                    "reviewer states that one exposure declaration applies to all three records."),
    "performed_at": "2026-11-04",
    "exposure": {"seen_before_deciding": lines(14, 18, 20), "prior_position": line(16)},
    "transcribed_from": {"path": str(SOURCE.relative_to(ROOT)), "sha256": sha256(SOURCE.read_bytes())},
}

ITEMS = {
    1: {"outcome": "CANNOT_DETERMINE", "overall": 26,
        "reasons": [26, 28, 30, *span(32, 36), 38, 40, 42, 44, 46, 48],
        "parts": [("1a", "CANNOT_DETERMINE", [28, 30, *span(32, 36), 38, 40, 42]),
                  ("1b", "CONDITION_MET_WITH_QUALIFICATION", [44, 46, 48])],
        "change": [60],
        "evidence": [file(C + "02c_citation_network.md", 9), file(C + "02c_citation_network.md", 154, 169),
                     file(C + "lock/section_E_preregistration.md", 5, 10),
                     file(C + "lock/section_E_preregistration.md", 39, 52),
                     file(C + "lock/section_E_lock_time.txt", 1), file(C + "lock/section_E_preregistration.sha256", 1),
                     file(C + "lock/locked_sources.json", 1, 92), file(C + "retrieval/retrieval_log.jsonl", 1, 8),
                     *[file(C + f"metadata/raw-api/lock_{f}.json", 1) for f in ("F1", "F2", "F3", "F4", "F6")],
                     external("git commit b108bab", "in this repository's history; " + line(58)),
                     external("git commit 693175d", "in this repository's history; " + line(58)),
                     file(A + "00a_preregistration_LOCKED.txt")]},
    2: {"outcome": "CONDITION_MET_WITH_QUALIFICATION", "overall": 64,
        "reasons": [64, 66, 68, 70, 71, 72, 74, 76, 78, 79, 80, 82, 84, 86, 88, 99],
        "parts": [("Sachs 2003: 2a", "CONDITION_MET", [70]), ("Sachs 2003: 2b", "CONDITION_MET", [71]),
                  ("Sachs 2003: 2c", "CONDITION_MET_WITH_QUALIFICATION", [72, 74]),
                  ("Glaeser et al. 2004: 2a", "CONDITION_MET_WITH_QUALIFICATION", [78]),
                  ("Glaeser et al. 2004: 2b", "CONDITION_MET_WITH_QUALIFICATION", [79]),
                  ("Glaeser et al. 2004: 2c", "CONDITION_MET_WITH_QUALIFICATION", [80, 82])],
        "change": [101],
        "evidence": [file(C + "02c_citation_network.md", 196, 199), file(C + "02c_citation_network.md", 301, 304),
                     file(C + "02c_citation_network.md", 445, 448),
                     file(C + "sources/SACHS2003-excerpts.txt", 5, 11),
                     file(C + "sources/GLAESER2004-excerpts.txt", 5, 16),
                     external("NBER Working Paper 9490 (Sachs 2003)", line(95) + " Recorder's note: the PDF SHA-256 "
                              "recorded at line 2 of SACHS2003-excerpts.txt is d8c218e3b3ed20379c99ea2b2bb1e341843d60d7"
                              "4a5f97fa53ba57330ae3cbc4; the reviewer states the downloaded copy matched."),
                     external("NBER Working Paper 10568 (Glaeser et al. 2004)", line(96) + " Recorder's note: the PDF "
                              "SHA-256 recorded at line 2 of GLAESER2004-excerpts.txt is a3176149a0ca2bdd31e3fbace1ef7"
                              "45418d64c8dedeba63d88a4ca2c64d6c092; the reviewer states the downloaded copy matched."),
                     file(INSTRUMENT, 784, 796)]},
    3: {"outcome": "CONDITION_NOT_MET", "overall": 105,
        "reasons": [105, 107, 109, 111, 113, 115, 117, 118, 119, 121, 123, 125, 127],
        "parts": [("3a", "CONDITION_MET", [107, 109]),
                  ("3b", "CONDITION_NOT_MET", [111, 113, 115, 117, 118, 119, 121, 123, 125, 127])],
        "change": [138],
        "evidence": [file(C + "02c_citation_network.md", 203, 210), file(C + "02c_citation_network.md", 286),
                     file(C + "02c_citation_network.md", 310), file(C + "02c_citation_network.md", 468, 470),
                     file(C + "sources/HB2004-excerpts.txt", 5, 17), file(C + "sources/AJR2001-excerpts.txt", 12, 25),
                     file(C + "metadata/raw-api/recent_all_HB.json", 1),
                     file(C + "metadata/raw-api/recent_cocite_HB.json", 1),
                     file(C + "retrieval/retrieval_log.jsonl", 146), file(C + "retrieval/retrieval_log.jsonl", 159),
                     file(INSTRUMENT, 1099, 1118)]},
}


def main() -> None:
    context = load_json((HERE.parent / "context.json").read_bytes())
    blank = build({**context, "challenges": []}, ROOT)
    for number, spec in ITEMS.items():
        assert re.search(rf"Overall outcome: {spec['outcome']}[.,]", line(spec["overall"])), number
        art = template(blank, number)
        art.update(COMMON)
        art.update(challenge_id=f"ajr2001-item-{number}-chatgpt-codex", outcome=spec["outcome"],
                   reasons=lines(*spec["reasons"]), parts=[part(*p) for p in spec["parts"]],
                   evidence=spec["evidence"], what_would_change=lines(*spec["change"]))
        out = HERE / f"item-{number}-chatgpt-codex.json"
        out.write_text(json.dumps(art, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(out.relative_to(ROOT), sha256(out.read_bytes()))


if __name__ == "__main__":
    main()
