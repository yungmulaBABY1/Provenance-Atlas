"""How ChatGPT (GPT-6)'s answer was transcribed into three challenge artifacts.

Source: source/chatgpt-gpt6-answer-2026-11-04.txt, a byte copy of the answer the
repository owner supplied on 4 November 2026 (sha256 09267a8f...).

Every text field is one line of that file, chosen by line number below, with any
leading "* " bullet dropped. One exception: tables that arrived flattened, one cell
per line, are joined into one field in the order received. The invisible link
characters and the citation chips from the reviewer's interface (for example
"epge.fgv.br +1") are kept. atlas.challenge checks again at build time that every text
field occurs in the source.

This reviewer gives outcomes per part only for item 2, in two tables. Items 1 and 3
discuss their questions (1a/1b, 3a/3b) without a label, so they are recorded with no
parts, and no outcome is assigned that the reviewer did not give.

What the recorder arranged, and you should check:
  - which lines go to reasons;
  - the item 2 parts. Each part's first line is the reviewer's table row, and this
    script asserts that the row's label is the part's outcome;
  - the evidence list, built from each "Evidence relied upon" block. Prose pointers
    such as "particularly steps 31-37" are kept as notes on the file.

Run from the repository root: python tests/atlas/challenge/ajr2001/challenges/transcribe_chatgpt_gpt6.py
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

SOURCE = HERE / "source/chatgpt-gpt6-answer-2026-11-04.txt"
LINES = SOURCE.read_text(encoding="utf-8").split("\n")
A = "examples/research/acemoglu-colonial-origins/"
C = A + "citation-network/"
GENERAL = [14, 336, 338]  # statements the reviewer makes about all three items


def line(n: int) -> str:
    text = LINES[n - 1]
    assert text.strip(), f"line {n} is empty"
    return text[2:] if text.startswith("* ") else text


def joined(first: int, last: int) -> str:
    """A table that arrived one cell per line, in the order received."""
    return " ".join(LINES[i - 1].strip() for i in range(first, last + 1) if LINES[i - 1].strip())


def texts(*items) -> list[str]:
    return [joined(*i) if isinstance(i, tuple) else line(i) for i in items]


def file(path: str, first: int | None = None, last: int | None = None, note: str | None = None) -> dict:
    entry = {"kind": "FILE", "path": path, "sha256": sha256((ROOT / path).read_bytes())}
    if first is not None:
        entry["lines"] = [first, last if last is not None else first]
    if note:
        entry["note"] = note
    return entry


def external(identifier: str, note: str) -> dict:
    return {"kind": "EXTERNAL", "identifier": identifier, "note": note}


def part(name: str, outcome: str, ns: list[int]) -> dict:
    row = LINES[ns[0] - 1]
    assert row.split("\t")[-1] == outcome, f"part {name}: the table row says {row.split(chr(9))[-1]!r}"
    return {"part": name, "outcome": outcome, "reasons": texts(*ns)}


COMMON = {
    "challenger": {"identity": "ChatGPT (GPT-6)",
                   "kind": "MODEL_AGENT",
                   "context": ("As stated by the reviewer: 'ChatGPT, GPT-6, MODEL_AGENT'. Supplied by the repository "
                               "owner on 4 November 2026. The reviewer states that it previously reviewed the "
                               "Acemoglu audit in the same conversation (see prior position).")},
    "relation_to_run": {"producer": "NO", "atlas_code_author": "NO",
                        "basis": "DECLARED_BY_CHALLENGER: " + line(19) + " " + line(20)},
    "recorded_by": ("Claude (Anthropic), Claude Code session 017YUqUaM2ka4XtLriA1p3fD, which is the code author. "
                    "It transcribed the reviewer's answer as supplied by the repository owner, pinned in "
                    "transcribed_from. Text fields are copied verbatim, line by line; tables that arrived "
                    "flattened are joined in the order received; citation chips from the reviewer's interface are "
                    "kept as received. The recorder arranged which lines are reasons, the item 2 parts (each part's "
                    "first line is the reviewer's own table row) and the evidence list, using "
                    "transcribe_chatgpt_gpt6.py. Items 1 and 3 carry no parts because the reviewer gave no "
                    "per-part outcome for them. Lines 14, 336 and 338 concern all three items and are repeated in "
                    "each. performed_at is the date the owner supplied the answer (US/Pacific); the reviewer "
                    "stated no time."),
    "performed_at": "2026-11-04",
    "exposure": {"seen_before_deciding": texts(5, 22, 23, 25), "prior_position": line(21)},
    "transcribed_from": {"path": str(SOURCE.relative_to(ROOT)), "sha256": sha256(SOURCE.read_bytes())},
}

ITEMS = {
    1: {"outcome": "CONDITION_MET_WITH_QUALIFICATION",
        "reasons": [10, 29, 31, 33, 35, (37, 41), 43, 45, 47, 49, 51, 53, 55, 57, (59, 83), 85, 87, 89, 109,
                    *GENERAL],
        "parts": [], "change": [105, 107],
        "evidence": [file(C + "02c_citation_network.md", 5, 9), file(C + "02c_citation_network.md", 154, 169),
                     file(C + "lock/section_E_preregistration.md", note="particularly steps 31–37"),
                     file(C + "lock/section_E_lock_time.txt"), file(C + "lock/locked_sources.json"),
                     *[file(C + f"metadata/raw-api/lock_{f}.json", note="lock_F1.json through lock_F6.json, excluding F5")
                       for f in ("F1", "F2", "F3", "F4", "F6")],
                     file(C + "retrieval/retrieval_log.jsonl", note="first five requests"),
                     external("git commits b108bab and 693175d", line(101))]},
    2: {"outcome": "CONDITION_MET_WITH_QUALIFICATION",
        "reasons": [11, 113, 115, 117, 119, 120, 121, 122, 124, 126, 128, 130, 132, 134, 136, 138, 140, 142, 144,
                    146, 148, 150, 152, 154, 156, 157, 158, 159, 161, 163, 165, 167, 169, 171, 173, 174, 175, 177,
                    179, 181, 183, 185, 187, 189, 191, 193, 195, 197, 199, 201, 203, 205, 207, 231, *GENERAL],
        "parts": [("Sachs (2003), R1: 2a", "CONDITION_MET", [120, 124, 126, 128]),
                  ("Sachs (2003), R1: 2b", "CONDITION_MET", [121, 130, 132, 134]),
                  ("Sachs (2003), R1: 2c", "CONDITION_MET_WITH_QUALIFICATION",
                   [122, 136, 138, 140, 142, 144, 146, 148, 150, 152]),
                  ("Glaeser et al. (2004), R2: 2a", "CONDITION_MET_WITH_QUALIFICATION", [157, 161, 163, 165, 167]),
                  ("Glaeser et al. (2004), R2: 2b", "CONDITION_MET_WITH_QUALIFICATION",
                   [158, 169, 171, 173, 174, 175, 177, 179]),
                  ("Glaeser et al. (2004), R2: 2c", "CONDITION_MET_WITH_QUALIFICATION",
                   [159, 181, 183, 185, 187, 189, 191, 193, 195, 197])],
        "change": [225, 227, 229],
        "evidence": [file(C + "02c_citation_network.md", 184, 199), file(C + "02c_citation_network.md", 431, 448),
                     file(C + "sources/SACHS2003-excerpts.txt", note="SA-E1"),
                     file(C + "sources/GLAESER2004-excerpts.txt", note="GL-E1 and GL-E2"),
                     file(C + "02c_citation_network.md", 292, 306, note="particularly Finding 6"),
                     external("Sachs (2003), NBER Working Paper 9490", line(220)),
                     external("Glaeser et al. (2004), Journal of Economic Growth", line(221) + " Recorder's note: "
                              "this is the published journal version. GLAESER2004-excerpts.txt records NBER WP 10568 "
                              "(PDF SHA-256 a3176149a0ca2bdd31e3fbace1ef745418d64c8dedeba63d88a4ca2c64d6c092), "
                              "and the other reviewer cites that working paper. The two versions were not "
                              "compared here.")]},
    3: {"outcome": "CONDITION_NOT_MET",
        "reasons": [12, 235, 237, 239, 241, 243, 245, 247, 249, 251, 253, 255, 257, 259, 260, 261, 263, (265, 279),
                    281, 283, 285, 287, 289, 291, 293, 295, 297, 299, 301, 303, 305, 306, 307, 309, 311, 322, 330,
                    *GENERAL],
        "parts": [], "change": [326, 328],
        "evidence": [file(C + "02c_citation_network.md", 203, 215), file(C + "02c_citation_network.md", 282, 310),
                     file(C + "02c_citation_network.md", 461, 475),
                     file(C + "sources/HB2004-excerpts.txt", note="HB-E1"),
                     file(C + "sources/AJR2001-excerpts.txt", note="AJR-E2"),
                     file(C + "metadata/recent_cocite_counts.json"),
                     file(C + "metadata/raw-api/recent_all_HB.json"),
                     file(C + "metadata/raw-api/recent_cocite_HB.json")]},
}


def main() -> None:
    context = load_json((HERE.parent / "context.json").read_bytes())
    blank = build({**context, "challenges": []}, ROOT)
    for number, spec in ITEMS.items():
        first = line(spec["reasons"][0])
        assert re.search(rf"(?<![A-Z_]){spec['outcome']}(?![A-Z_])", first), (number, first)
        art = template(blank, number)
        art.update(COMMON)
        art.update(challenge_id=f"ajr2001-item-{number}-chatgpt-gpt6", outcome=spec["outcome"],
                   reasons=texts(*spec["reasons"]), parts=[part(*p) for p in spec["parts"]],
                   evidence=spec["evidence"], what_would_change=texts(*spec["change"]))
        out = HERE / f"item-{number}-chatgpt-gpt6.json"
        out.write_text(json.dumps(art, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(out.relative_to(ROOT), sha256(out.read_bytes()))


if __name__ == "__main__":
    main()
