"""python -m atlas.maplink build|replay|show — link findings to an upstream Stage-1 map; no models.

show verifies before it renders: it replays the bundle at content level (which itself
content-replays the claim-link receipt it depends on) and refuses to display labels it
cannot re-derive. With --unverified it renders the stored assertions under a banner.
Neither mode says whether a claim, finding or map entry is correct.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import textwrap

from ..contract import ContractError, canonical, load_json, read_artifact
from .build import build, replay

WRAP = 88


def wrap(text: str, indent: str = "    ") -> str:
    return textwrap.fill(" ".join(text.split()), WRAP, initial_indent=indent, subsequent_indent=indent)


UNVERIFIED_BANNER = (
    "=" * WRAP + "\n"
    "UNVERIFIED RENDERING OF STORED ASSERTIONS\n"
    "Nothing below was validated or replayed. Labels are shown as written in the file.\n"
    "For a verified view: python -m atlas.maplink show <records.jsonl> --root <repo>\n"
    + "=" * WRAP + "\n\n")


def verified_banner(result: dict, manifest: dict) -> str:
    dep = manifest["dependency"]
    delta = ", ".join(f"{k} {v['recorded']} -> {v['replayed']}" for k, v in result["environment_delta"].items())
    return ("VERIFIED RENDERING: every record below was re-derived by content replay from the inputs\n"
            f"this bundle pins (claim-link records sha256 {dep['records_sha256'][:16]}..., itself content-replayed;\n"
            f"executor {manifest['executor']['version']}). Environment delta: {delta or 'none'}.\n"
            "Verification covers recording only, not the correctness of any claim, finding or map entry.\n\n")


def show(records: list[dict], linked: list[dict] | None = None) -> str:
    """linked: the claim-link records this bundle pins, for the audit output's own text."""
    by_id = {r["id"]: r for r in records}
    ext = {r["id"]: r for r in linked or []}
    run = next(r for r in records if r["type"] == "MapLinkRun")
    up = by_id[run["upstream_map_id"]]
    prov, pre, ref = up["provenance"], up["preflight"], up["audit_output_reference"]
    out = [f"MAP LINKS    {run['id']}",
           f"Claim links  {run['dependency']['claim_link_run_id']} (its own claim map: "
           f"{run['dependency']['claim_link_map_state']})",
           f"Audit        {run['dependency']['audit_run_id']}",
           "",
           f"UPSTREAM MAP {up['output']['path']}",
           f"  sha256 {up['output']['sha256']}",
           wrap(f"produced by {prov['producer']['identity']} ({prov['producer']['kind']}; "
                f"{prov['producer']['verification']})", "  "),
           f"  run prompt {prov['run_prompt']}; run receipt {prov['run_receipt']}",
           wrap(prov["note"], "  "),
           f"  link from the audit: {ref['state']}" + (f" (output line {', '.join(map(str, ref['lines']))})"
                                                        if ref["lines"] else ""),
           wrap(ref["basis"], "    "),
           wrap(f"instrument {up['instrument']['path']} blob {up['instrument']['git_blob_sha1'][:12]}...; the map's "
                f"own preflight line: blob {pre['blob_named']}, sha256 {pre['sha256_named']}, stated "
                f"disposition {pre['disposition']}", "  "),
           f"  target work {up['work']['work_id']}: {up['work']['named_in_map']} in the map"
           + (f" (line {up['work']['lines'][0]})" if up["work"]["lines"] else ""),
           f"  source anchors: {up['anchors']['count']} ({', '.join(f'{k} {v}' for k, v in up['anchors']['by_kind'].items())})",
           wrap(up["anchors"]["verification"], "    "),
           "", "MAP FIELDS (the producer's text and its own verification column; not checked by Atlas)"]
    for field, info in up["fields"].items():
        if not info["statement_id"]:
            out.append(f"  {field}: {info['status']}")
            continue
        st = by_id[info["statement_id"]]
        out += [f"  {field}. {info['native_label']} ({info['status']}, line {st['anchor']['line']})",
                wrap(st["text"], "      "),
                wrap(f"producer's verification state: {st['producer_verification_state']}", "      ")]
    if up["designated_field_6_id"]:
        st = by_id[up["designated_field_6_id"]]
        out += [f"  Field 6 section statement (designated, line {st['anchor']['line']}):", wrap(st["text"], "      ")]
    for c in (r for r in records if r["type"] == "TextComparison" and "/compare/map-field-6-section~" in r["id"]):
        out.append(f"      vs {by_id[c['object_id']]['role']}: {c['result']}")
    out += ["", "PAPER STATEMENT  " + run["source_statement"]["state"], wrap(run["source_statement"]["note"])]
    out += ["", "RECONCILIATION (the audit output's restatement vs the map; text only)"]
    for rid in run["reconciliation_ids"]:
        rec = by_id[rid]
        out.append(f"  field {rec['field']}: {rec['state']}; claim identity {rec['claim_identity']}")
        if rec["comparison_id"]:
            comp = by_id[rec["comparison_id"]]
            out.append(f"    text comparison with the map's {by_id[rec['map_statement_id']]['role']}: {comp['result']}")
        if rec["audit_output_statement_id"] in ext:
            st = ext[rec["audit_output_statement_id"]]
            out += [f"    the audit output's restatement (line {st['anchor']['first_line']}):",
                    wrap(st["exact_text"], "      ")]
    for aid in run["alignment_ids"]:
        al = by_id[aid]
        out += ["", f"FINDING {al['finding_number']}  target {al['target_kind']}"
                + (f", MAP GAP form {al['map_gap_form']}" if al["map_gap_form"] else "")]
        out.append(f"  claim identity: {al['claim_identity']}  (claim links without the map: {al['claim_link_identity']})")
        for cid in al["comparison_ids"]:
            out.append(f"  vs map Field 6 section: {by_id[cid]['result']}")
        for m in al["field_mentions"]:
            out.append(f"  mentions map field {m['field']}: {m['relation']}")
    counts = run["counts"]
    out += ["", "Counts are of findings and fields by label, not a score:",
            "  findings: " + ", ".join(f"{k} {v}" for k, v in counts["claim_identity"].items()),
            "  reconciliation: " + ", ".join(f"{k} {v}" for k, v in counts["reconciliation"].items()),
            "Text comparison only. Whether differently worded statements are the same claim is not decided here."]
    return "\n".join(out) + "\n"


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build", help="link one claim-link bundle to one upstream map; writes manifest.json, records.jsonl")
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
    s.add_argument("--root", type=Path, default=Path.cwd())
    s.add_argument("--unverified", action="store_true")
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
            print(json.dumps(replay(args.manifest.read_bytes(), args.jsonl.read_bytes(), args.root, args.level),
                             sort_keys=True))
        else:
            data = args.jsonl.read_bytes()
            records = [load_json(line) for line in data.splitlines() if line.strip()]
            if args.unverified:
                sys.stdout.write(UNVERIFIED_BANNER + show(records))
            else:
                manifests = [r for r in records if r.get("type") == "MapLinkManifest"]
                if len(manifests) != 1:
                    raise ContractError("NOT_VERIFIED: bundle must contain exactly one MapLinkManifest")
                try:
                    result = replay((canonical(manifests[0]) + "\n").encode("utf-8"), data, args.root, "content")
                except ContractError as exc:
                    raise ContractError(f"NOT_VERIFIED: {exc}. Nothing was rendered; "
                                        "use --unverified to see the stored assertions as written") from exc
                pins = manifests[0]["input_context"]["claim_link_bundle"]["records"]
                linked = [load_json(line) for line in read_artifact(args.root, pins).splitlines() if line.strip()]
                sys.stdout.write(verified_banner(result, manifests[0]) + show(records, linked))
        return 0
    except (ContractError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
