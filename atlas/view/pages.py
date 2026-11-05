"""The committed pages, declared in one file (docs/atlas/views/views.json).

Each page names its receipt and output folder. A question page may link a member's
audit record to another page; a paper page may name the question it belongs to,
which adds a breadcrumb with the question's declared denominator. An audit page names
a map-link and a challenge receipt over the same imported audit. Every page is
rendered only after its receipts (and the question's, where named) are re-verified.
"""

from __future__ import annotations

import os
from pathlib import Path

from ..contract import ContractError, load_json
from .audit import build_audit_view, html_audit, text_audit, verify_audit
from .model import build_view, verify, view_json
from .question import build_question_view, external_ids, html_question, question_context, text_question, verify_question
from .render import html_page, text_report

PAGES_SCHEMA = "atlas-view-pages/0.1"


def href(from_out: str, to_out: str) -> str:
    return Path(os.path.relpath(Path(to_out) / "index.html", Path(from_out))).as_posix()


def render_all(pages_file: Path, root: Path) -> dict[str, dict[str, bytes]]:
    spec = load_json(pages_file.read_bytes())
    if spec.get("schema") != PAGES_SCHEMA:
        raise ContractError("UNSUPPORTED_PAGES_SCHEMA")
    pages = {p["id"]: p for p in spec["pages"]}
    if len(pages) != len(spec["pages"]):
        raise ContractError("DUPLICATE_PAGE_ID")
    verified_questions = {}

    def question(page_id: str) -> dict:
        page = pages.get(page_id)
        if page is None or page["kind"] != "question":
            raise ContractError(f"UNKNOWN_QUESTION_PAGE: {page_id}")
        if page_id not in verified_questions:
            verified_questions[page_id] = verify_question(root / page["receipt"], root)
        return verified_questions[page_id]

    files = {}
    for page in spec["pages"]:
        if page["kind"] == "question":
            links = {}
            for record_id, target in page.get("links", {}).items():
                if target not in pages:
                    raise ContractError(f"UNKNOWN_PAGE_LINK: {target}")
                links[record_id] = href(page["out"], pages[target]["out"])
            view = build_question_view(question(page["id"]), root, links)
            files[page["out"]] = {"view.json": view_json(view), "index.html": html_question(view).encode("utf-8"),
                                  "report.txt": text_question(view).encode("utf-8")}
        elif page["kind"] == "extraction":
            verified = verify(root / page["receipt"], root)
            context = ids = None
            if page.get("question"):
                qv = question(page["question"])
                run_id = next(r["id"] for r in verified["records"] if r["type"] == "ExtractionRun")
                context = question_context(qv, run_id, href(page["out"], pages[page["question"]]["out"]))
                ids = {r["id"] for r in qv["records"]} | external_ids(qv, root)
            view = build_view(verified, root, context, ids)
            files[page["out"]] = {"view.json": view_json(view), "index.html": html_page(view).encode("utf-8"),
                                  "report.txt": text_report(view).encode("utf-8")}
        elif page["kind"] == "audit":
            view = build_audit_view(verify_audit(page, root), root)
            files[page["out"]] = {"view.json": view_json(view), "index.html": html_audit(view).encode("utf-8"),
                                  "report.txt": text_audit(view).encode("utf-8")}
        else:
            raise ContractError(f"UNKNOWN_PAGE_KIND: {page['kind']}")
    return files
