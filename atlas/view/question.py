"""Question page: one research question over its declared sources, from a verified question bundle.

The page shows what was asked and by whom, how the sources were chosen, what Atlas
holds about each source, the claims already written about them, and what has not
been established. It gives no source a position and merges no claims.
"""

from __future__ import annotations

from pathlib import Path

from . import SCHEMA, VERSION
from .labels import TABLE_ID, plain
from .model import check_refs
from .render import CSS, chip, e, refs, slug, wrap, lab
from ..contract import ContractError, load_json, sha256
from ..question.build import replay

MODEL_WRITTEN = "Written by a model run. Not a source's words."
QUESTION_CSS = """
.counts { display: grid; gap: .4rem; }
.count { display: grid; grid-template-columns: 4.2rem 1fr; gap: .2rem .8rem; align-items: baseline; padding: .55rem .8rem; border: 1px solid var(--rule); border-radius: 8px; background: var(--surface); }
.count .n { font: 600 1.05rem/1.2 var(--font-mono); font-variant-numeric: tabular-nums; }
.count .who { grid-column: 2; font-size: .8rem; color: var(--muted); }
.source h3 { display: flex; flex-wrap: wrap; gap: .4rem .6rem; align-items: baseline; }
.source h3 .id { font: 600 .9rem/1 var(--font-mono); color: var(--accent); }
.source ul { margin: 0; padding-left: 1.1rem; display: grid; gap: .35rem; font-size: .92rem; }
.source .sub { font-size: .78rem; font-weight: 600; color: var(--muted); text-transform: uppercase; letter-spacing: .05em; margin-top: .2rem; }
.open { font-weight: 600; }
"""


def verify_question(receipt_dir: Path, root: Path) -> dict:
    manifest_bytes = (receipt_dir / "manifest.json").read_bytes()
    records_bytes = (receipt_dir / "records.jsonl").read_bytes()
    try:
        result = replay(manifest_bytes, records_bytes, root, "content")
    except ContractError as exc:
        raise ContractError(f"NOT_VERIFIED: {exc}") from exc
    records = [load_json(line) for line in records_bytes.splitlines() if line.strip()]
    return {"records": records, "manifest": load_json(manifest_bytes), "replay": result,
            "receipt": {"path": receipt_dir.resolve().relative_to(root.resolve()).as_posix(),
                        "manifest_sha256": sha256(manifest_bytes), "records_sha256": sha256(records_bytes)}}


def external_ids(verified: dict, root: Path) -> set[str]:
    """IDs of the pinned bundles the question was built from (already re-verified by replay)."""
    deps = verified["manifest"]["input_context"]["dependencies"]
    ids = set()
    for pins in [deps["import_bundle"], deps["provisional_map_bundle"], *deps["extraction_receipts"]]:
        data = (root / pins["records"]["path"]).read_bytes()
        ids |= {load_json(line)["id"] for line in data.splitlines() if line.strip()}
    return ids


def question_context(verified: dict, run_id: str, href: str) -> dict:
    """Breadcrumb for a paper page reached from this question: same corpus, same denominator."""
    records = verified["records"]
    q = next(r for r in records if r["type"] == "ResearchQuestion")
    members = [r for r in records if r["type"] == "QuestionMember"]
    hits = [m for m in members if any(a["relation"] == "TARGET_OF_EXTRACTION_RUN" and a["record_id"] == run_id
                                      for a in m["audit_records"])]
    if len(hits) != 1:
        raise ContractError(f"QUESTION_CONTEXT_MISMATCH: {run_id} is not the extraction run of one member")
    return {"question_id": q["id"], "question_text": q["text"],
            "wording": plain(q["wording"]["origin"]),
            "confirmation": plain(q["wording"]["operator_confirmation"], "operator_confirmation"),
            "member_label": hits[0]["label"], "denominator": len(members), "href": href,
            "refs": [q["id"], hits[0]["id"]]}


def audit_item(a: dict, links: dict) -> dict:
    d = a["detail"]
    chips, text = [plain(a["relation"])], None
    if a["relation"] == "TARGET_OF_IMPORTED_AUDIT":
        chips += [plain(d["origin"]), plain(d["instrument"]), plain(d["human_review"], "human_review")]
    elif a["relation"] == "TARGET_OF_EXTRACTION_RUN":
        text = f"Runner: {d['runner']}"
        chips += [plain(d["runner_basis"]), plain(d["human_review"], "human_review")]
    elif a["relation"] == "PASSAGES_CITED_IN_IMPORTED_AUDIT":
        chips += [plain(d["assessment"]), plain(d["import_status"])]
    elif a["relation"] == "PASSAGES_REVIEWED":
        text = f"Reviewer: {d['reviewer']}"
        chips += [plain(d["disposition"]), plain(d["independence"], "independence"),
                  plain(d["human_adjudication"], "human_adjudication")]
    return {"record_id": a["record_id"], "labels": chips, "text": text, "href": links.get(a["record_id"]),
            "refs": [a["record_id"]]}


def build_question_view(verified: dict, root: Path, links: dict | None = None) -> dict:
    links = links or {}
    records = verified["records"]
    by_id = {r["id"]: r for r in records}
    q = next(r for r in records if r["type"] == "ResearchQuestion")
    cov = next(r for r in records if r["type"] == "QuestionCoverage")
    members = [by_id[i] for i in q["member_ids"]]
    claims = [by_id[i] for i in q["claim_ids"]]
    unknown = sorted(set(links) - {a["record_id"] for m in members for a in m["audit_records"]})
    if unknown:
        raise ContractError(f"VIEW_LINK_UNRESOLVED: no member holds {unknown}")

    sources = []
    for m in members:
        versions = m["source_versions"]
        sources.append({
            "label": m["label"], "citation": m["citation"], "work_id": m["work_id"],
            "access": [plain(v["access_outcome"]) for v in versions],
            "version_notes": [v["basis"] for v in versions],
            "state": plain(m["record_state"]),
            "passages": [{"native_id": p["native_id"], "label": p["label"], "page": p["page"],
                          "about": p["about"], "match": plain(p["match"])} for p in m["passages"]],
            "described_in": [{"native_id": d["native_id"], "label": d["label"], "page": d["page"],
                              "speaker": d["speaker"]} for d in m["described_in"]],
            "checks": [{"check_id": c["check_id"], "scope": c["scope"], "eligibility": plain(c["eligibility"])}
                       for c in m["checks"]],
            "audit": [audit_item(a, links) for a in m["audit_records"]],
            "refs": [m["id"]]})

    claim_view = []
    for c in claims:
        w = c["written_by"]
        who = (f"Written by the imported audit run ({w['instrument']} instrument, {w['mode'].lower().replace('_', ' ')} "
               f"mode). The run labels its own map: {w['native_label']}." if "native_label" in w else
               f"Written by the extraction run ({w['instrument']} instrument). Runner: {w['runner']}.")
        claim_view.append({"text": c["text"], "target": c["target_member"], "written_by": MODEL_WRITTEN, "who": who,
                           "labels": [l for i in c["identity_records"]
                                      for l in (plain(i["relation"]), plain(i["claim_identity"]))],
                           "refs": [c["id"], c["statement_id"], *[i["record_id"] for i in c["identity_records"]]]})

    rows = {r["id"]: r for r in cov["rows"]}
    missing_copy = [m for m in members if not m["retrieved"]]
    blocked = [c["check_id"] for m in missing_copy for c in m["checks"]
               if c["eligibility"] == "INELIGIBLE_MISSING_EVIDENCE"]
    not_established = []
    if q["wording"]["operator_confirmation"] == "NOT_CONFIRMED":
        not_established.append({"item": "The wording of the question has not been confirmed by the person running "
                                         "the investigation.", "refs": [q["id"]]})
    not_established += [
        {"item": "Atlas holds no record giving any source a position on this question (supports, contradicts or "
                 "qualifies). Positions are a later, attributed step.", "refs": [q["id"]]},
        {"item": ("No claim is recorded as the same claim across sources." if not q["claim_links"] else
                  f"{len(q['claim_links'])} declared links between claims; see the records."), "refs": [q["id"]]},
        {"item": "Whether these sources are independent of each other, or share data or authors, has not been "
                 "assessed.", "refs": [q["id"]]},
    ]
    if missing_copy:
        not_established.append({
            "item": (f"No retrieved copy: {len(missing_copy)} of {cov['denominator']} sources "
                     f"({', '.join(m['label'] for m in missing_copy)}). Checks that need their text did not run: "
                     f"{', '.join(blocked)}."),
            "refs": [m["id"] for m in missing_copy]})
    if rows["human"]["count"] == 0:
        not_established.append({"item": "No person has made a decision on any record here.", "refs": [cov["id"]]})
    not_established.append({
        "item": ("The passages on record were chosen for the imported audit, not for this question. Its own note: "
                 f"“{q['corpus']['imported_corpus_selection']}”"),
        "refs": [q["id"], q["corpus"]["imported_corpus_id"]]})

    view = {
        "schema": SCHEMA, "generator": {"name": "atlas-view", "version": VERSION}, "labels_table": TABLE_ID,
        "page": "question",
        "question": {"text": q["text"], "short_title": q["short_title"], "wording": plain(q["wording"]["origin"]),
                     "confirmation": plain(q["wording"]["operator_confirmation"], "operator_confirmation"),
                     "basis": q["wording"]["basis"], "recorded_by": q["recorded_by"], "as_of": q["as_of"],
                     "refs": [q["id"]]},
        "corpus": {"kind": plain(q["corpus"]["kind"]), "selection_rule": q["corpus"]["selection_rule"],
                   "denominator": cov["denominator"], "refs": [q["id"]]},
        "coverage": [{"count": r["count"], "denominator": cov["denominator"], "phrase": r["phrase"],
                      "members": r["members"], "refs": [cov["id"], *r["refs"]]} for r in cov["rows"]],
        "sources": sources,
        "passage_text_note": ("Passage text is held in the import bundle as bounded excerpts that have not been "
                              "reviewed for public release, so it is not shown here. Each passage is listed by its "
                              "label, page and match result."),
        "claims": claim_view,
        "claims_note": ("Each claim below was chosen for checking by a model run. The two runs had different target "
                        "papers, so Atlas records them as different claims. Neither is the question, and neither is "
                        "a source's own words."),
        "not_established": not_established,
        "technical": {"records": [{"id": r["id"], "type": r["type"]} for r in sorted(records, key=lambda r: r["id"])],
                      "receipt": verified["receipt"],
                      "replay": {"result": verified["replay"]["replay"], "level": verified["replay"]["level"]}},
        "rules": ["Atlas adds no judgment here: no source is given a position, no claims are merged, and every count "
                  "is recomputed from the records with its denominator.",
                  "Model-written text is quoted and labelled. Plain-language labels come from a fixed table and sit "
                  "beside the original label.",
                  "Every item links to the records it comes from (technical record, below)."],
    }
    check_refs(view, set(by_id) | external_ids(verified, root))
    return view


def html_question(view: dict) -> str:
    present = {r["id"] for r in view["technical"]["records"]}

    def R(ids):
        return refs(ids, present)

    out = []
    w = out.append
    q = view["question"]
    w("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
      "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
      f"<title>{e(q['short_title'])}: one question, {e(view['corpus']['denominator'])} sources</title>\n"
      "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n"
      "<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600"
      "&amp;family=IBM+Plex+Sans:wght@400;500;600&amp;family=Newsreader:opsz,wght@6..72,400;6..72,600&amp;display=swap\">\n"
      f"<style>{CSS}{QUESTION_CSS}</style>\n</head>\n<body>\n<main>\n")
    w('<header>\n<div class="eyebrow">Provenance Atlas &middot; one question, '
      f'{e(view["corpus"]["denominator"])} sources</div>\n'
      f"<h1>{e(q['short_title'])}: what Atlas holds about each source</h1>\n"
      '<div class="legend"><span>Sans, tagged: written by a model or by Claude</span>'
      '<span><span class="mono">Mono</span>: Atlas checks and labels</span>'
      "<span>No source text is shown on this page</span></div>\n</header>\n")

    w('<section aria-labelledby="h-q">\n<h2 id="h-q">The question</h2>\n'
      f'<div class="card claim"><span class="tag">{e(q["wording"]["plain"])}</span><p>{e(q["text"])}</p>'
      f'<div class="labels">{chip(q["wording"])}{chip(q["confirmation"])}</div>'
      f'<p class="note">{e(q["basis"])}</p>{R(q["refs"])}</div>\n'
      '<p class="note">Atlas does not answer this question. It shows what is on record about each source, what was '
      "checked, and what is missing. You judge.</p>\n</section>\n")

    c = view["corpus"]
    w('<section aria-labelledby="h-corpus">\n<h2 id="h-corpus">How the sources were chosen</h2>\n'
      f'<div class="card"><div class="labels">{chip(c["kind"])}</div><p>{e(c["selection_rule"])}</p>'
      f'<p class="note">As of {e(q["as_of"])}. {e(q["recorded_by"])}</p>{R(c["refs"])}</div>\n</section>\n')

    w('<section aria-labelledby="h-cov">\n<h2 id="h-cov">At a glance</h2>\n<div class="counts">\n')
    for row in view["coverage"]:
        who = ", ".join(row["members"]) if row["members"] else "none"
        w(f'<div class="count"><span class="n">{e(row["count"])} of {e(row["denominator"])}</span>'
          f'<span>{e(row["phrase"])}</span><span class="who">{e(who)} {R(row["refs"])}</span></div>\n')
    w("</div>\n</section>\n")

    w('<section aria-labelledby="h-src">\n<h2 id="h-src">The sources</h2>\n'
      f'<p class="note">{e(view["passage_text_note"])}</p>\n')
    for s in view["sources"]:
        w(f'<div class="card source" id="src-{e(s["label"])}"><h3><span class="id">{e(s["label"])}</span>'
          f'<span>{e(s["citation"])}</span></h3>'
          f'<div class="labels">{"".join(chip(a) for a in s["access"])}{chip(s["state"])}</div>')
        for note in s["version_notes"]:
            w(f'<p class="note">Version: {e(note)}</p>')
        if s["passages"]:
            w('<div class="sub">Passages on record</div><ul>')
            for p in s["passages"]:
                about = (f' &middot; <strong>{e(s["label"])}’s words about {e(p["about"])}</strong>'
                         if p["about"] else "")
                w(f'<li><code>{e(p["native_id"])}</code> p. {e(p["page"])} &middot; {e(p["label"])}{about} '
                  f'{chip(p["match"])}</li>')
            w("</ul>")
        if s["described_in"]:
            w('<div class="sub">Described in another source</div><ul>')
            for d in s["described_in"]:
                w(f'<li><code>{e(d["native_id"])}</code> in {e(d["speaker"])}, p. {e(d["page"])}: '
                  f'{e(d["speaker"])}’s words about {e(s["label"])}, not {e(s["label"])}’s own.</li>')
            w("</ul>")
        if s["checks"]:
            w('<div class="sub">Checks that need this source</div><ul>')
            for k in s["checks"]:
                w(f'<li>{e(k["scope"])} {chip(k["eligibility"])} <code>{e(k["check_id"])}</code></li>')
            w("</ul>")
        w('<div class="sub">Audit records</div>')
        if s["audit"]:
            w("<ul>")
            for a in s["audit"]:
                opener = (f' <a class="open" href="{e(a["href"])}">Open this record &rarr;</a>' if a["href"] else "")
                text = f' {e(a["text"])}' if a["text"] else ""
                w(f'<li>{chip(a["labels"][0])}{text}<div class="labels">'
                  f'{"".join(chip(l) for l in a["labels"][1:])}{R(a["refs"])}</div>{opener}</li>')
            w("</ul>")
        else:
            w('<p class="note">None.</p>')
        w(f'{R(s["refs"])}</div>\n')
    w("</section>\n")

    w('<section aria-labelledby="h-claims">\n<h2 id="h-claims">Claims already written about these sources</h2>\n'
      f'<p class="note">{e(view["claims_note"])}</p>\n')
    for cl in view["claims"]:
        w(f'<div class="card model"><span class="tag">{e(cl["written_by"])}</span>'
          f'<p>{e(cl["text"])}</p><p class="state">{e(cl["who"])} That run\u2019s target paper: '
          f'<a href="#src-{e(cl["target"])}">{e(cl["target"])}</a>.</p>'
          f'<div class="labels">{"".join(chip(l) for l in cl["labels"])}</div>{R(cl["refs"])}</div>\n')
    w("</section>\n")

    w('<section aria-labelledby="h-missing" class="missing">\n<h2 id="h-missing">Not established</h2>\n'
      '<div class="card"><ul>')
    for item in view["not_established"]:
        w(f"<li>{e(item['item'])} {R(item['refs'])}</li>")
    w("</ul></div>\n</section>\n")

    t = view["technical"]
    w('<section aria-labelledby="h-tech">\n<h2 id="h-tech">Technical record</h2>\n'
      f'<p class="note">This page was generated from the records below after they were re-derived by '
      f'{e(t["replay"]["level"])} replay ({e(t["replay"]["result"])}), which also re-verified every bundle they pin. '
      "Regenerate it with <code>python -m atlas.view build-all</code>.</p>\n"
      '<details><summary>Receipt</summary><div class="mono">')
    for k, v in t["receipt"].items():
        w(f"<div>receipt {e(k)}: {e(v)}</div>")
    w("</div></details>\n")
    w(f'<details><summary>All {len(t["records"])} records in this bundle</summary><div class="mono">')
    for r in t["records"]:
        w(f'<div id="rec-{e(slug(r["id"]))}">{e(r["type"])} &middot; {e(r["id"])}</div>')
    w("</div></details>\n</section>\n")
    w("<footer>" + "".join(f"<p>{e(rule)}</p>" for rule in view["rules"]) +
      f'<p>Generated by {e(view["generator"]["name"])} {e(view["generator"]["version"])} '
      f'&middot; labels {e(view["labels_table"])} &middot; It points; you judge.</p></footer>\n'
      "</main>\n"
      "<script>\n"
      "function openTarget() {\n"
      "  var id = decodeURIComponent(location.hash.slice(1));\n"
      "  var el = id && document.getElementById(id);\n"
      "  if (!el) return;\n"
      "  for (var d = el.closest('details'); d; d = d.parentElement && d.parentElement.closest('details')) d.open = true;\n"
      "  el.scrollIntoView({block: 'center'});\n"
      "}\n"
      "window.addEventListener('hashchange', openTarget);\n"
      "openTarget();\n"
      "</script>\n</body>\n</html>\n")
    return "".join(out)


def text_question(view: dict) -> str:
    q, c = view["question"], view["corpus"]
    out = [f"{q['short_title'].upper()}: WHAT ATLAS HOLDS ABOUT EACH SOURCE", "",
           "Atlas does not answer this question. It shows what is on record about each source, what was",
           "checked, and what is missing. You judge.", "",
           "THE QUESTION", wrap(q["text"], "    "), f"  {lab(q['wording'])}", f"  {lab(q['confirmation'])}",
           wrap(q["basis"], "  "), "",
           "HOW THE SOURCES WERE CHOSEN", f"  {lab(c['kind'])}", wrap(c["selection_rule"], "  "),
           f"  As of {q['as_of']}.", "", "AT A GLANCE"]
    for row in view["coverage"]:
        out.append(f"  {row['phrase']}: {row['count']} of {row['denominator']} sources"
                   + (f" ({', '.join(row['members'])})" if row["members"] else ""))
    out += ["", "THE SOURCES", wrap(view["passage_text_note"], "  ")]
    for s in view["sources"]:
        out += ["", f"  {s['label']}  " + s["citation"], *[f"    {lab(a)}" for a in s["access"]], f"    {lab(s['state'])}"]
        out += [wrap(f"Version: {n}", "    ") for n in s["version_notes"]]
        if s["passages"]:
            out.append("    Passages on record:")
            for p in s["passages"]:
                about = f"; {s['label']}'s words about {p['about']}" if p["about"] else ""
                out.append(f"      {p['native_id']} p. {p['page']}: {p['label']}{about} | {lab(p['match'])}")
        for d in s["described_in"]:
            out.append(f"    Described in {d['speaker']} ({d['native_id']}, p. {d['page']}): "
                       f"{d['speaker']}'s words, not {s['label']}'s own.")
        if s["checks"]:
            out.append("    Checks that need this source:")
            out += [f"      {k['check_id']}: {lab(k['eligibility'])}" for k in s["checks"]]
        out.append("    Audit records:" if s["audit"] else "    Audit records: none.")
        for a in s["audit"]:
            out.append(f"      {lab(a['labels'][0])}" + (f" {a['text']}" if a["text"] else ""))
            out += [f"        - {lab(l)}" for l in a["labels"][1:]]
            if a["href"]:
                out.append(f"        page: {a['href']}")
    out += ["", "CLAIMS ALREADY WRITTEN ABOUT THESE SOURCES", wrap(view["claims_note"], "  ")]
    for cl in view["claims"]:
        out += [f"  {cl['written_by']}", wrap(cl["text"], "    "),
                wrap(f"{cl['who']} That run's target paper: {cl['target']}.", "    ")]
        out += [f"    - {lab(l)}" for l in cl["labels"]]
    out += ["", "NOT ESTABLISHED"] + [wrap(i["item"], "  - ") for i in view["not_established"]]
    t = view["technical"]
    out += ["", "TECHNICAL RECORD", f"  replay: {t['replay']['result']} ({t['replay']['level']})"]
    out += [f"  receipt {k}: {v}" for k, v in t["receipt"].items()]
    out += ["", *[wrap(rule) for rule in view["rules"]],
            f"Generated by {view['generator']['name']} {view['generator']['version']}; labels {view['labels_table']}."]
    return "\n".join(out) + "\n"
