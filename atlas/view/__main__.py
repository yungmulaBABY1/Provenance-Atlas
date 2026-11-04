"""python -m atlas.view build|check RECEIPT_DIR OUT_DIR — reader view of an extraction bundle.

build  verifies the bundle by content replay, then writes view.json, index.html and
       report.txt to OUT_DIR. Nothing is written if verification fails.
check  does the same in memory and requires the files in OUT_DIR to be identical.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from ..contract import ContractError
from .model import build_view, verify, view_json
from .render import html_page, text_report


def render(receipt: Path, root: Path) -> dict[str, bytes]:
    view = build_view(verify(receipt, root), root)
    return {"view.json": view_json(view), "index.html": html_page(view).encode("utf-8"),
            "report.txt": text_report(view).encode("utf-8")}


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "check"))
    parser.add_argument("receipt", type=Path)
    parser.add_argument("out", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        files = render(args.receipt, args.root)
        if args.command == "build":
            args.out.mkdir(parents=True, exist_ok=True)
            for name, data in files.items():
                (args.out / name).write_bytes(data)
            print(json.dumps({"written": sorted(files), "out": str(args.out)}))
        else:
            stale = [n for n, data in files.items()
                     if not (args.out / n).is_file() or (args.out / n).read_bytes() != data]
            if stale:
                raise ContractError(f"VIEW_STALE: {stale} differ from a fresh render; run build")
            print(json.dumps({"check": "PASS", "files": sorted(files)}))
        return 0
    except (ContractError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
