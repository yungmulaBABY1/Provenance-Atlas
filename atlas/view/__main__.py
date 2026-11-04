"""python -m atlas.view build-all|check-all [PAGES] | build|check RECEIPT_DIR OUT_DIR — reader views.

build-all  renders every page declared in PAGES (default docs/atlas/views/views.json)
           after verifying its receipts, and writes view.json, index.html and
           report.txt into each page's folder. Nothing is written if any check fails.
check-all  does the same in memory and requires the committed files to be identical.
build/check render one extraction bundle on its own, without a question breadcrumb;
           the committed pages come from build-all.
"""

from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from ..contract import ContractError
from .model import build_view, verify, view_json
from .pages import render_all
from .render import html_page, text_report

DEFAULT_PAGES = Path("docs/atlas/views/views.json")


def render(receipt: Path, root: Path) -> dict[str, bytes]:
    view = build_view(verify(receipt, root), root)
    return {"view.json": view_json(view), "index.html": html_page(view).encode("utf-8"),
            "report.txt": text_report(view).encode("utf-8")}


def stale(out: Path, files: dict[str, bytes]) -> list[str]:
    return [str(out / n) for n, data in files.items() if not (out / n).is_file() or (out / n).read_bytes() != data]


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("command", choices=("build", "check", "build-all", "check-all"))
    parser.add_argument("paths", nargs="*", type=Path)
    parser.add_argument("--root", type=Path, default=Path.cwd())
    args = parser.parse_args(argv)
    try:
        if args.command in ("build-all", "check-all"):
            if len(args.paths) > 1:
                parser.error("build-all/check-all take at most one PAGES file")
            pages = args.paths[0] if args.paths else args.root / DEFAULT_PAGES
            outputs = {args.root / out: files for out, files in render_all(pages, args.root).items()}
        else:
            if len(args.paths) != 2:
                parser.error("build/check take RECEIPT_DIR OUT_DIR")
            outputs = {args.paths[1]: render(args.paths[0], args.root)}
        if args.command.startswith("build"):
            for out, files in outputs.items():
                out.mkdir(parents=True, exist_ok=True)
                for name, data in files.items():
                    (out / name).write_bytes(data)
            print(json.dumps({"written": sorted(str(o) for o in outputs)}))
        else:
            bad = [p for out, files in outputs.items() for p in stale(out, files)]
            if bad:
                raise ContractError(f"VIEW_STALE: {bad} differ from a fresh render; run build-all")
            print(json.dumps({"check": "PASS", "pages": sorted(str(o) for o in outputs)}))
        return 0
    except (ContractError, OSError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
