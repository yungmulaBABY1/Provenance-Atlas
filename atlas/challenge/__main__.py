"""python -m atlas.challenge build|replay|show|template — attributed decisions on review items; no models.

show verifies before it renders (content replay, which re-runs the vendored checker and
re-reads every pinned challenge artifact). template prints a blank challenge artifact for
one review item, bound to its exact identities, for a challenger to fill in.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import textwrap

from . import ARTIFACT_SCHEMA
from ..contract import ContractError, canonical, load_json, sha256
from .build import OUTCOMES, build, replay

WRAP = 88


def wrap(text: str, indent: str = "    ") -> str:
    return textwrap.fill(" ".join(text.split()), WRAP, initial_indent=indent, subsequent_indent=indent)


def show(records: list[dict]) -> str:
    by_id = {r["id"]: r for r in records}
    run = next(r for r in records if r["type"] == "ChallengeRun")
    dep, chk, counts = run["dependency"], run["checker"], run["counts"]
    out = [f"CHALLENGES   {run['id']}",
           f"Audit        {dep['audit_run_id']} (produced by {dep['producer']})",
           f"Checker      {chk['path']} sha256 {chk['sha256'][:16]}... re-run on the output: {chk['status']}",
           "",
           f"{counts['items']} review items left by the checker: {counts['items_not_challenged']} not challenged; "
           f"{counts['items_with_a_decision_by_a_person']} with a decision by a person.",
           f"{counts['challenges']} challenges on record ({counts['challenges_detached']} detached)."]
    for iid in run["item_ids"]:
        item = by_id[iid]
        out += ["", f"ITEM {item['item_number']}  {item['item_code']}  [{item['challenge_state']}]",
                wrap(item["instruction"])]
        if not item["challenge_ids"]:
            out.append("    No challenge on record. The audit's own handling of this item stands unreviewed.")
        if len({o["outcome"] for o in item["outcomes"]}) > 1:
            out.append(wrap("Challengers' outcomes differ: " + "; ".join(
                f"{o['outcome']} ({by_id[o['challenge_id']]['challenger']['identity']})" for o in item["outcomes"])
                + ". All are kept; nothing here merges or ranks them.", "    "))
        for cid in item["challenge_ids"]:
            c = by_id[cid]
            rel = c["relation_to_run"]
            out += [f"  {c['outcome']}  by {c['challenger']['identity']} ({c['challenger']['kind']}), "
                    f"{c['performed_at']}",
                    f"    relation to the run: producer {rel['producer']}, Atlas code author "
                    f"{rel['atlas_code_author']} ({rel['verification']})",
                    wrap(f"recorded by: {c['recorded_by']}", "    "),
                    f"    transcription: {c['transcription']['state']}"
                    + (f" ({c['transcription']['checked_fields']} text fields; source "
                       f"{c['transcription']['source']['path']})" if c["transcription"].get("source") else ""),
                    wrap("seen before deciding: " + (" | ".join(c["exposure"]["seen_before_deciding"])
                                                      or "none stated"), "    "),
                    wrap(f"prior position: {c['exposure']['prior_position']}", "    ")]
            out += [wrap("reason: " + r, "    ") for r in c["reasons"]]
            for part in c["parts"]:
                out.append(wrap(f"part {part['part']}: {part['outcome']} — " + " ".join(part["reasons"]), "    "))
            for ev in c["evidence"]:
                if ev["kind"] == "RECORD":
                    out.append(f"    evidence: record {ev['id']}")
                elif ev["kind"] == "EXTERNAL":
                    out.append(wrap(f"evidence (external, not resolved here): {ev['identifier']} — {ev['note']}", "    "))
                else:
                    out.append(wrap(f"evidence: {ev['path']}" + (f" lines {ev['lines'][0]}-{ev['lines'][1]}"
                                                                 if ev.get("lines") else "")
                                    + (f" ({ev['note']})" if ev.get("note") else ""), "    "))
            out += [wrap("would change if: " + w, "    ") for w in c["what_would_change"]]
        for cid in item["detached_challenge_ids"]:
            c = by_id[cid]
            out.append(f"  DETACHED {c['challenge_id']}: target changed ({', '.join(c['mismatched'])}); "
                       "kept, not attached")
    loose = [by_id[c] for c in run["challenge_ids"] if by_id[c]["binding"] != "MATCH"
             and not any(c in by_id[i]["detached_challenge_ids"] for i in run["item_ids"])]
    for c in loose:
        out.append(f"DETACHED {c['challenge_id']}: no current item {c['target']['item_number']} "
                   f"({', '.join(c['mismatched'])})")
    out += ["", "Outcomes are the challengers' own, as written in their pinned artifacts. This code decides none.",
            "A challenge appends; the imported run, its checker status and its findings are unchanged."]
    return "\n".join(out) + "\n"


def template(bundle: dict, number: int) -> dict:
    item = next((i for i in bundle["items"] if i["number"] == number), None)
    if item is None:
        raise ContractError(f"NO_SUCH_ITEM: {number}")
    run = next(r for r in bundle["records"] if r["type"] == "ChallengeRun")
    return {"schema": ARTIFACT_SCHEMA, "challenge_id": "FILL-IN-a-slug",
            "target": {"kind": "CHECKER_REVIEW_ITEM", "audit_run_id": run["dependency"]["audit_run_id"],
                       "output_sha256": next(r for r in bundle["records"] if r["type"] == "ReviewItem")["output_sha256"],
                       "checker_sha256": bundle["checker"]["sha256"], "item_number": item["number"],
                       "item_code": item["code"], "item_text_sha256": sha256(item["text"].encode("utf-8"))},
            "challenger": {"identity": "FILL IN", "kind": "PERSON or MODEL_AGENT", "context": "FILL IN"},
            "relation_to_run": {"producer": "NO, YES or UNKNOWN", "atlas_code_author": "NO, YES or UNKNOWN",
                                "basis": "DECLARED_BY_CHALLENGER"},
            "recorded_by": "FILL IN: who wrote this file, and whether it is the challenger's own words",
            "performed_at": "YYYY-MM-DD",
            "exposure": {"seen_before_deciding": ["FILL IN"], "prior_position": "FILL IN or NONE_STATED"},
            "outcome": " | ".join(sorted(OUTCOMES)),
            "parts": [], "reasons": ["FILL IN"], "evidence": [], "what_would_change": [],
            "transcribed_from": None}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build")
    b.add_argument("context", type=Path)
    b.add_argument("--root", type=Path, default=Path.cwd())
    b.add_argument("--out", type=Path, required=True)
    r = sub.add_parser("replay")
    r.add_argument("manifest", type=Path)
    r.add_argument("jsonl", type=Path)
    r.add_argument("--root", type=Path, default=Path.cwd())
    r.add_argument("--level", choices=("strict", "content"), default="strict")
    s = sub.add_parser("show")
    s.add_argument("jsonl", type=Path)
    s.add_argument("--root", type=Path, default=Path.cwd())
    t = sub.add_parser("template")
    t.add_argument("context", type=Path)
    t.add_argument("item", type=int)
    t.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        if args.command == "build":
            bundle = build(load_json(args.context.read_bytes()), args.root)
            args.out.mkdir(parents=True, exist_ok=True)
            (args.out / "manifest.json").write_text(canonical(bundle["manifest"]) + "\n", encoding="utf-8")
            (args.out / "records.jsonl").write_bytes(bundle["jsonl"])
            print(json.dumps({"records": len(bundle["records"]), "sha256": bundle["jsonl_sha256"]}, sort_keys=True))
        elif args.command == "replay":
            print(json.dumps(replay(args.manifest.read_bytes(), args.jsonl.read_bytes(), args.root, args.level),
                             sort_keys=True))
        elif args.command == "template":
            bundle = build(load_json(args.context.read_bytes()), args.root)
            print(json.dumps(template(bundle, args.item), indent=1, ensure_ascii=False))
        else:
            data = args.jsonl.read_bytes()
            records = [load_json(line) for line in data.splitlines() if line.strip()]
            manifests = [r for r in records if r.get("type") == "ChallengeManifest"]
            if len(manifests) != 1:
                raise ContractError("NOT_VERIFIED: bundle must contain exactly one ChallengeManifest")
            try:
                result = replay((canonical(manifests[0]) + "\n").encode("utf-8"), data, args.root, "content")
            except ContractError as exc:
                raise ContractError(f"NOT_VERIFIED: {exc}. Nothing was rendered") from exc
            delta = ", ".join(f"{k} {v['recorded']} -> {v['replayed']}" for k, v in result["environment_delta"].items())
            sys.stdout.write("VERIFIED RENDERING: re-derived by content replay (import receipt replayed, checker "
                             f"re-run, artifacts re-read). Environment delta: {delta or 'none'}.\n"
                             "Verification covers recording only, not whether any outcome is right.\n\n"
                             + show(records))
        return 0
    except (ContractError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
