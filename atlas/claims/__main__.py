"""python -m atlas.claims build|replay|show — deterministic claim links; no models.

show verifies before it renders: it replays the bundle at content level from the
inputs the bundle names and refuses to display labels it cannot re-derive. With
--unverified it renders the stored assertions as they are, under a banner that
says so. Neither mode says anything about whether a claim or review is correct.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import textwrap

from ..contract import ContractError, canonical, load_json
from .link import build, replay

WRAP = 88


def wrap(text: str, indent: str = "    ") -> str:
    return textwrap.fill(" ".join(text.split()), WRAP, initial_indent=indent, subsequent_indent=indent)


UNVERIFIED_BANNER = (
    "=" * WRAP + "\n"
    "UNVERIFIED RENDERING OF STORED ASSERTIONS\n"
    "Nothing below was validated or replayed. Labels such as VERIFIED, MATCH or\n"
    "SAME_TEXT are shown as written in the file and may have been edited.\n"
    "For a verified view: python -m atlas.claims show <records.jsonl> --root <repo>\n"
    + "=" * WRAP + "\n\n")


def verified_banner(result: dict, manifest: dict) -> str:
    dep = manifest["dependency"]
    delta = ", ".join(f"{k} {v['recorded']} -> {v['replayed']}" for k, v in result["environment_delta"].items())
    return ("VERIFIED RENDERING: every record below was re-derived by content replay from\n"
            f"the inputs this bundle pins (import bundle records sha256 {dep['records_sha256'][:16]}..., "
            f"executor {manifest['executor']['version']}, parser {manifest['parser']['version']}).\n"
            f"Environment delta: {delta or 'none'}.\n"
            "Verification covers recording only, not the correctness of any claim, finding or review.\n\n")


def show(records: list[dict]) -> str:
    by_id = {r["id"]: r for r in records}
    run = next(r for r in records if r["type"] == "ClaimLinkRun")
    cmap = by_id[run["claim_map_id"]]
    dep = run["dependency"]
    out = [f"CLAIM LINKS  {run['id']}",
           f"Dependency   {dep['audit_run_id']}  (syntax {dep['syntax']}; findings "
           f"{', '.join(dep['finding_import_statuses'])}; producing-instrument compliance "
           f"{dep['producing_instrument_compliance']}; native projection {dep['native_projection']})",
           "",
           f"CLAIM MAP    {cmap['state']}"
           + (f"  {cmap['producer']['native_label']!r}, citation-network degraded standalone mode"
              if cmap["state"] == "PRESENT" else ""),
           f"  present: {', '.join(cmap['fields_present']) or 'none'}"]
    for field, reason in cmap["fields_absent"].items():
        out.append(f"  absent {field}: {reason}")
    for field, status in cmap["field_status"].items():
        if status != "USABLE":
            out.append(f"  field {field} {status}: not used as a linking target")
            for sid in cmap["field_statement_ids"].get(field, []):
                st = by_id[sid]
                out.append(f"    line {st['anchor']['first_line']}, label {st['native_label']!r}:")
                out.append(wrap(st["exact_text"], "      "))
    out += [f"  claim-extraction output: {cmap['producer']['claim_extraction_output']}; "
            f"claim inventory: {cmap['claim_inventory']}",
            f"  reconciliation: {cmap['reconciliation']}"]
    if cmap["parse_issues"]:
        out.append(f"  parse issues: {canonical(cmap['parse_issues'])}")
    out += ["", "PAPER STATEMENT  " + run["source_statement"]["state"]]
    out += [wrap(reason) for reason in run["source_statement"]["reasons"]]
    comparisons = [r for r in records if r["type"] == "TextComparison"]
    for c in comparisons:
        if c["id"].split("/compare/")[1].startswith("map-field-"):
            a, b = by_id[c["subject_id"]], by_id[c["object_id"]]
            out += ["", f"{a['role']} (lines {a['anchor']['first_line']}-{a['anchor']['last_line_inclusive']})",
                    wrap(a["exact_text"]),
                    f"  vs {b['role']}: {c['result']}; semantic equivalence {c['semantic_equivalence']}",
                    wrap(b["exact_text"])]
    for aid in run["alignment_ids"]:
        al = by_id[aid]
        out += ["", f"FINDING {al['finding_number']}  {al['finding_import_status']}, {al['finding_assessment']}"]
        if al["finding_target_id"]:
            target = by_id[al["finding_target_id"]]
            out += [f"  target claim ({al['target_kind']}, line {target['anchor']['first_line']}):",
                    wrap(target["exact_text"])]
        for cid in al["comparison_ids"]:
            c = by_id[cid]
            out.append(f"  vs {by_id[c['object_id']]['role']}: {c['result']}")
        out.append(f"  claim identity: {al['claim_identity']}")
        if al["designated_target_state"] != "MAP_FIELD_6_IN_OUTPUT":
            out.append(f"  designated target: none ({al['designated_target_state']})"
                       + (f"; {len(al['designated_target_candidate_ids'])} candidate entries kept, not linked"
                          if al["designated_target_candidate_ids"] else ""))
        for m in al["native_field_6_mentions"]:
            out.append(f"  output mentions field 6 in '{m['field']}' (line {m['line']}): {m['text']}")
        for sid in al["reviewer_decomposition_ids"] + al["detached_review_ids"]:
            s = by_id[sid]
            out.append(f"  review {s['review_id'].rsplit('/', 1)[1]} [{s['binding']}] {s['disposition']}"
                       f" by {s['reviewer']['identity']} ({s['reviewer']['kind']})")
            if s["reviewed_field"]:
                out.append(f"    reviews field '{s['reviewed_field']}' chars [{s['reviewed_span'][0]}, {s['reviewed_span'][1]}): "
                           f"{s['relation_to_finding_target']}")
                out.append(wrap(s["proposition"], "      "))
            for part in s["parts"]:
                out.append(f"      part {part['part']} {part['disposition']}: {part['text']}")
            out.append(f"    independence {s['independence']}; human adjudication {s['human_adjudication']}")
    out += ["", "Counts are of findings by claim identity, not a score: "
            + ", ".join(f"{k} {v}" for k, v in run["counts"].items()),
            "Text comparison only. Whether differently worded statements are the same claim is not decided here."]
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build", help="link one pinned import bundle; writes manifest.json and records.jsonl")
    b.add_argument("context", type=Path)
    b.add_argument("--root", type=Path, default=Path.cwd())
    b.add_argument("--out", type=Path, required=True)
    r = sub.add_parser("replay", help="rebuild from the manifest's context and compare")
    r.add_argument("manifest", type=Path)
    r.add_argument("jsonl", type=Path)
    r.add_argument("--root", type=Path, default=Path.cwd())
    r.add_argument("--level", choices=("strict", "content"), default="strict")
    s = sub.add_parser("show", help="plain-text view; verifies by content replay unless --unverified")
    s.add_argument("jsonl", type=Path)
    s.add_argument("--root", type=Path, default=Path.cwd(),
                   help="directory the bundle's pinned inputs are resolved from")
    s.add_argument("--unverified", action="store_true",
                   help="render stored assertions without validation or replay, under a banner")
    args = parser.parse_args(argv)
    try:
        if args.command == "build":
            bundle = build(load_json(args.context.read_bytes()), args.root)
            args.out.mkdir(parents=True, exist_ok=True)
            (args.out / "manifest.json").write_text(canonical(bundle["manifest"]) + "\n", encoding="utf-8")
            (args.out / "records.jsonl").write_bytes(bundle["jsonl"])
            print(json.dumps({"records": len(bundle["records"]), "sha256": bundle["jsonl_sha256"],
                              "semantic_judgment": "NONE"}, sort_keys=True))
        elif args.command == "replay":
            print(json.dumps(replay(args.manifest.read_bytes(), args.jsonl.read_bytes(), args.root,
                                    args.level), sort_keys=True))
        else:
            data = args.jsonl.read_bytes()
            records = [load_json(line) for line in data.splitlines() if line.strip()]
            if args.unverified:
                sys.stdout.write(UNVERIFIED_BANNER + show(records))
            else:
                manifests = [r for r in records if r.get("type") == "ClaimLinkManifest"]
                if len(manifests) != 1:
                    raise ContractError("NOT_VERIFIED: bundle must contain exactly one ClaimLinkManifest")
                manifest = manifests[0]
                try:
                    result = replay((canonical(manifest) + "\n").encode("utf-8"), data, args.root, "content")
                except ContractError as exc:
                    raise ContractError(f"NOT_VERIFIED: {exc}. Nothing was rendered; "
                                        "use --unverified to see the stored assertions as written") from exc
                sys.stdout.write(verified_banner(result, manifest) + show(records))
        return 0
    except (ContractError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
