"""python -m atlas.question build|replay — a research question over a declared list of sources.

build   reads a question context, verifies every receipt it pins (the extraction
        receipts by content replay), and writes manifest.json and records.jsonl.
replay  rebuilds the bundle from the manifest's own context and compares.
The page for a question is rendered by atlas.view (see docs/atlas/views/views.json).
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from ..contract import ContractError, canonical, load_json
from .build import build, replay


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
    args = parser.parse_args(argv)
    try:
        if args.command == "build":
            bundle = build(load_json(args.context.read_bytes()), args.root)
            args.out.mkdir(parents=True, exist_ok=True)
            (args.out / "manifest.json").write_text(canonical(bundle["manifest"]) + "\n", encoding="utf-8")
            (args.out / "records.jsonl").write_bytes(bundle["jsonl"])
            print(json.dumps({"records": len(bundle["records"]), "sha256": bundle["jsonl_sha256"]}, sort_keys=True))
        else:
            print(json.dumps(replay(args.manifest.read_bytes(), args.jsonl.read_bytes(), args.root, args.level),
                             sort_keys=True))
        return 0
    except (ContractError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
