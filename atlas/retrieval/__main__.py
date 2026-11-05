"""python -m atlas.retrieval build|check|run-live|drift — locked queries recorded by code.

build     rebuild a set's saved-response records, sample checks and report from
          committed files; --write updates them in place.
check     fail if any committed output differs from a fresh build (CI runs this).
run-live  send every spec in a set to the provider and record each attempt; then
          compare with the saved records. Needs network access. Reads an optional
          key from OPENALEX_API_KEY, sends it only in the Authorization header and
          never writes it.
drift     recompute drift.json and DRIFT.txt from committed live records, offline.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import sys

from ..contract import ContractError
from .sets import check, drift_from_files, outputs, run_live_set

ROOT = Path(__file__).resolve().parents[2]


def write(files: dict[Path, bytes]) -> None:
    for path, data in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(data)
        print(f"wrote {path.relative_to(ROOT) if path.is_relative_to(ROOT) else path}")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(prog="python -m atlas.retrieval", description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--root", type=Path, default=ROOT)
    sub = parser.add_subparsers(dest="command", required=True)
    b = sub.add_parser("build")
    b.add_argument("set", type=Path)
    b.add_argument("--write", action="store_true")
    c = sub.add_parser("check")
    c.add_argument("sets", type=Path, nargs="+")
    lv = sub.add_parser("run-live")
    lv.add_argument("set", type=Path)
    lv.add_argument("--out", type=Path, required=True)
    d = sub.add_parser("drift")
    d.add_argument("set", type=Path)
    d.add_argument("live_records", type=Path)
    args = parser.parse_args(argv)
    root = args.root.resolve()
    try:
        if args.command == "build":
            files = outputs(root, args.set.resolve())
            if args.write:
                write(files)
            else:
                report = next(v for k, v in files.items() if k.name.endswith(".txt"))
                sys.stdout.write(report.decode("utf-8"))
        elif args.command == "check":
            problems = []
            for path in args.sets:
                problems += check(root, path.resolve())
                print(f"checked {path}")
            if problems:
                print("\n".join(problems), file=sys.stderr)
                return 1
        elif args.command == "run-live":
            key = os.environ.get("OPENALEX_API_KEY") or None
            write(run_live_set(root, args.set.resolve(), args.out.resolve(), api_key=key))
        elif args.command == "drift":
            write(drift_from_files(root, args.set.resolve(), args.live_records.resolve()))
    except ContractError as exc:
        print(f"ERROR {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
