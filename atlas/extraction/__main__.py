"""python -m atlas.extraction local|local-verify|build|replay|show — recorded claim extraction.

local / local-verify need the private full output and the source PDF.
build / replay / show use committed files only. show verifies by content replay
before rendering; --unverified renders stored assertions under a banner.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys
import textwrap

from ..contract import ContractError, canonical, load_json
from . import local
from .build import build, replay

WRAP = 88
UNVERIFIED_BANNER = ("=" * WRAP + "\nUNVERIFIED RENDERING OF STORED ASSERTIONS\n"
                     "Nothing below was validated or replayed. Labels are shown as written in the file.\n"
                     "For a verified view: python -m atlas.extraction show <records.jsonl> --root <repo>\n"
                     + "=" * WRAP + "\n\n")


def wrap(text: str, indent: str = "    ") -> str:
    return textwrap.fill(" ".join(str(text).split()), WRAP, initial_indent=indent, subsequent_indent=indent)


def show(records: list[dict], redacted_text: str | None = None) -> str:
    by_id = {r["id"]: r for r in records}
    run = next(r for r in records if r["type"] == "ExtractionRun")
    cmap = next(r for r in records if r["type"] == "ExtractedClaimMap")
    rid = run["id"]
    out = [f"EXTRACTION  {rid}",
           f"Method      {run['method']['name']}",
           f"Runner      {run['runner']['identity']} via {run['runner']['interface']} "
           f"({run['runner']['basis']}; verification {run['runner']['verification']})",
           f"When        {run['executed_at']['value']} ({run['executed_at']['kind']}, {run['executed_at']['basis']})",
           f"Exposure    {run['exposure']['self_reported']}; independence {run['exposure']['independence']}",
           f"Preflight   run: {run['preflight']['run_disposition']}. {run['preflight']['note']}",
           f"Source      {run['source']['work_id']} PDF {run['source']['pdf']['sha256'][:16]}... "
           f"(not redistributed); extraction {run['source']['extraction']['output_sha256'][:16]}...",
           f"Output      full {run['output']['full_sha256'][:16]}... PRIVATE; public copy has quotes withheld",
           "", "CLAIM MAP (claim-extraction instrument, all seven table rows)"]
    for field, row in sorted(cmap["fields"].items()):
        label = row["native_label"] + ("" if row["label_status"] == "EXACT" else f" [{row['label_status']} label]")
        out.append(f"  {field:>2}. {label}: {row['verification_state']}")
        out.append(wrap(row["table_content"], "      "))
    designated = by_id.get(cmap["designated_field_6_id"])
    if designated:
        out += ["", f"FIELD 6 (designated: section statement, line {designated['anchor']['line']})",
                wrap(designated["text"])]
        for c in (r for r in records if r["type"] == "TextComparison"):
            other = by_id[c["object_id"]]
            out.append(f"  vs {other['role']}: {c['result']}; semantic equivalence {c['semantic_equivalence']}")
            out.append(wrap(other["text"], "      "))
    anchors = [r for r in records if r["type"] == "SourceAnchor"]
    out += ["", f"SOURCE ANCHORS  {run['counts']['anchors']} entries: "
            + ", ".join(f"{k} {v}" for k, v in run["counts"]["by_state"].items()),
            f"  quotes on their stated page: {sum(1 for a in anchors if a['verification'].get('page_consistent'))}"
            f" of {sum(1 for a in anchors if a['verification'].get('found_page'))} located",
            f"  published verbatim: {run['counts']['published_verbatim']} (inside public excerpts); others withheld by hash"]
    for a in anchors:
        v = a["verification"]
        if v.get("state") == "MISMATCH":
            first = v["diagnostic"]["first_differences"][:2]
            out.append(f"  {a['anchor_id']} MISMATCH (p. {a['stated_page']}); diagnostic only: "
                       + "; ".join(f"{d['op']} quote {d['quote']} / extraction {d['extraction']}" for d in first))
    for link in (r for r in records if r["type"] == "PassageLink"):
        anchor = by_id[link["source_anchor_id"]]
        out += ["", f"PASSAGE LINK  {anchor['anchor_id']} lies inside imported passage {link['packet_excerpt_id']}",
                f"  {link['relation_basis']}"]
        quote = published_quote(redacted_text, anchor["anchor_id"]) if redacted_text else None
        if quote:
            out += ["  paper statement:", wrap(quote, "      ")]
        for review in link["reviews"]:
            out.append(f"  review {review['review_id'].rsplit('/', 1)[1]} {review['disposition']} "
                       f"(independence {review['independence']}; human adjudication {review['human_adjudication']})")
            for part in review["parts"]:
                out.append(f"      part {part['part']} {part['disposition']}: {part['text']}")
    for cross in (r for r in records if r["type"] == "CrossMapAlignment"):
        out += ["", f"HISTORICAL PROVISIONAL MAP  {cross['historical_map']['claim_link_run_id']} "
                f"({cross['historical_map']['state']})",
                f"  target works: this run {cross['new_target_work_id']}; provisional map {cross['historical_target_work_id']}",
                f"  {cross['relation']}; Field 6 text {cross['text_comparison']['result']}; claim identity {cross['claim_identity']}"]
    for check in (r for r in records if r["type"] == "EvidenceCheck"):
        out += ["", f"EVIDENCE CHECK  {check['check']}: {check['result']}", wrap(check["scope"])]
        for sub in check["detail"]["sub_checks"]:
            line = f"  {sub['sub_check']}: {sub['result']}"
            if sub["sub_check"] == "P_FROM_T":
                line += f"  recomputed p {sub['recomputed_p_interval']} vs reported {sub['reported_p_interval']}"
            if sub["sub_check"] == "T_FROM_CI":
                line += f"  implied t {sub['implied_t_interval']} vs reported {sub['reported_t_interval']}"
            out.append(line)
        out.append("  not checked: " + "; ".join(check["detail"]["not_checked"]))
    out += ["", "Matching a quote, checking arithmetic and judging support are different acts. "
            "Nothing here judges whether the paper or the claim is correct."]
    return "\n".join(out) + "\n"


def published_quote(redacted: str, anchor_id: str) -> str | None:
    from . import output
    for entry in output.parse(redacted)["anchors"]:
        if entry["id"] == anchor_id and entry["quote"]:
            return entry["quote"]["text"]
    return None


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    for name in ("local", "local-verify"):
        p = sub.add_parser(name, help="needs the private full output and the source PDF")
        p.add_argument("context", type=Path)
        p.add_argument("--output", type=Path, required=True, help="full output as received")
        p.add_argument("--pdf", type=Path, required=True)
        p.add_argument("--root", type=Path, default=Path.cwd())
    b = sub.add_parser("build", help="public stage from committed files")
    b.add_argument("context", type=Path)
    b.add_argument("--root", type=Path, default=Path.cwd())
    b.add_argument("--out", type=Path, required=True)
    r = sub.add_parser("replay")
    r.add_argument("manifest", type=Path)
    r.add_argument("jsonl", type=Path)
    r.add_argument("--root", type=Path, default=Path.cwd())
    r.add_argument("--level", choices=("strict", "content"), default="strict")
    s = sub.add_parser("show", help="verifies by content replay unless --unverified")
    s.add_argument("jsonl", type=Path)
    s.add_argument("--root", type=Path, default=Path.cwd())
    s.add_argument("--unverified", action="store_true")
    args = parser.parse_args(argv)
    try:
        if args.command in ("local", "local-verify"):
            context = load_json(args.context.read_bytes())
            fn = local.write if args.command == "local" else local.verify
            result = fn(context, args.root, args.output.read_bytes(), args.pdf.read_bytes())
            print(json.dumps(result if args.command == "local-verify" else {"written": True}, sort_keys=True))
        elif args.command == "build":
            bundle = build(load_json(args.context.read_bytes()), args.root)
            args.out.mkdir(parents=True, exist_ok=True)
            (args.out / "manifest.json").write_text(canonical(bundle["manifest"]) + "\n", encoding="utf-8")
            (args.out / "records.jsonl").write_bytes(bundle["jsonl"])
            print(json.dumps({"records": len(bundle["records"]), "sha256": bundle["jsonl_sha256"]}, sort_keys=True))
        elif args.command == "replay":
            print(json.dumps(replay(args.manifest.read_bytes(), args.jsonl.read_bytes(), args.root, args.level),
                             sort_keys=True))
        else:
            data = args.jsonl.read_bytes()
            records = [load_json(line) for line in data.splitlines() if line.strip()]
            if args.unverified:
                sys.stdout.write(UNVERIFIED_BANNER + show(records))
                return 0
            manifests = [r for r in records if r.get("type") == "ExtractionManifest"]
            if len(manifests) != 1:
                raise ContractError("NOT_VERIFIED: bundle must contain exactly one ExtractionManifest")
            try:
                result = replay((canonical(manifests[0]) + "\n").encode("utf-8"), data, args.root, "content")
            except ContractError as exc:
                raise ContractError(f"NOT_VERIFIED: {exc}. Nothing was rendered; use --unverified "
                                    "to see the stored assertions as written") from exc
            redacted = (args.root / manifests[0]["input_context"]["public"]["redacted_output"]["path"]).read_text(
                encoding="utf-8")
            delta = ", ".join(f"{k} {v['recorded']} -> {v['replayed']}" for k, v in result["environment_delta"].items())
            sys.stdout.write("VERIFIED RENDERING: every record below was re-derived by content replay from the\n"
                             "committed files this bundle pins. Withheld quotes were verified locally against the\n"
                             f"source and are not re-checkable without it. Environment delta: {delta or 'none'}.\n"
                             "Verification covers recording only, not correctness.\n\n" + show(records, redacted))
        return 0
    except (ContractError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
