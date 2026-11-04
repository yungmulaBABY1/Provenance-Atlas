"""Two renderings of one view model: an HTML page and a plain-text report."""

from __future__ import annotations

import html
import json
import textwrap

KIND = {"checked": "Checked", "limited": "Limited", "not-done": "Not done"}


def e(value) -> str:
    return html.escape(str(value), quote=True)


def chip(label: dict) -> str:
    return (f'<span class="label" title="{e(label["plain"])} ({e(label["table"])})">'
            f'<span class="plain">{e(label["plain"])}</span> <code>{e(label["native"])}</code></span>')


def native_only(label: dict) -> str:
    return f'<code class="native" title="{e(label["plain"])}">{e(label["native"])}</code>'


def refs(ids: list[str], present: set[str]) -> str:
    """Link records listed on this page; name the others (they live in linked bundles)."""
    items = [f'<a href="#rec-{e(slug(i))}">{e(short(i))}</a>' if i in present
             else f'<span title="{e(i)}">{e(short(i))}</span>' for i in ids]
    return '<span class="refs">' + " ".join(items) + "</span>"


def short(record_id: str) -> str:
    """Readable link text: the record path after its run, or the run's own name."""
    if "/" in record_id:
        return record_id.split("/", 1)[1]
    return record_id.rsplit(":", 2)[-2] + (" question" if ":question:" in record_id else " run")


def slug(record_id: str) -> str:
    return "".join(c if c.isalnum() else "-" for c in record_id)


def number(value) -> str:
    if isinstance(value, list):
        return "[" + ", ".join(number(v) for v in value) + "]"
    return str(value)


CSS = """
:root {
  /* Paper-and-ink: the paper's words in serif, model text in sans, Atlas labels in mono. */
  --paper: #f3f4f0; --surface: #ffffff; --ink: #1c222a; --muted: #59626e; --rule: #d5d9d0;
  --accent: #2b5b86; --checked: #2d6a4c; --limited: #8f5f10; --notdone: #8a3a3a;
  --tint-checked: #e6f0ea; --tint-limited: #f6eedf; --tint-notdone: #f5e6e6; --quote: #fbfaf6;
  --font-display: "Newsreader", Georgia, "Times New Roman", serif;
  --font-body: "IBM Plex Sans", system-ui, -apple-system, "Segoe UI", sans-serif;
  --font-mono: "IBM Plex Mono", ui-monospace, "SFMono-Regular", Menlo, monospace;
  color-scheme: light;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --paper: #11151a; --surface: #181d24; --ink: #e3e7ec; --muted: #9aa4af; --rule: #2b323b;
    --accent: #8db6df; --checked: #7cc39d; --limited: #e0b065; --notdone: #e39a9a;
    --tint-checked: #16271e; --tint-limited: #2a2214; --tint-notdone: #2c1a1a; --quote: #1c2128;
    color-scheme: dark;
  }
}
:root[data-theme="dark"] {
  --paper: #11151a; --surface: #181d24; --ink: #e3e7ec; --muted: #9aa4af; --rule: #2b323b;
  --accent: #8db6df; --checked: #7cc39d; --limited: #e0b065; --notdone: #e39a9a;
  --tint-checked: #16271e; --tint-limited: #2a2214; --tint-notdone: #2c1a1a; --quote: #1c2128;
  color-scheme: dark;
}
* { box-sizing: border-box; }
/* Grid and flex children may shrink below their longest word: hashes and IDs wrap, tables scroll. */
main > *, section > *, .card > *, .row > *, .subs > *, .crumb > *, details > div > *, blockquote > * { min-width: 0; }
code, .refs, .tag, .mono { overflow-wrap: anywhere; }
html, body { margin: 0; }
body { background: var(--paper); color: var(--ink); font: 16px/1.55 var(--font-body); }
main { max-width: 46rem; margin: 0 auto; padding: 2rem max(16px, env(safe-area-inset-left)) 4rem; display: grid; gap: 2.25rem; }
header { display: grid; gap: .6rem; }
.eyebrow { font: 500 .75rem/1 var(--font-mono); letter-spacing: .06em; text-transform: uppercase; color: var(--muted); }
h1 { font: 600 clamp(1.6rem, 5vw, 2.1rem)/1.15 var(--font-display); margin: 0; text-wrap: balance; }
h2 { font: 600 1.25rem/1.2 var(--font-display); margin: 0 0 .75rem; text-wrap: balance; }
h3 { font: 600 1rem/1.3 var(--font-body); margin: 0; }
p { margin: 0; max-width: 65ch; }
.citation { color: var(--muted); font-size: .95rem; }
.legend { display: flex; flex-wrap: wrap; gap: .5rem 1.25rem; font-size: .85rem; color: var(--muted); }
.legend .serif { font-family: var(--font-display); font-size: 1rem; color: var(--ink); }
.legend .mono { font-family: var(--font-mono); color: var(--ink); }
section { display: grid; gap: .9rem; }
.card { background: var(--surface); border: 1px solid var(--rule); border-radius: 10px; padding: 1rem 1.1rem; display: grid; gap: .6rem; }
.claim { border-left: 4px solid var(--accent); }
.claim p { font-size: 1.05rem; }
.tag { justify-self: start; font: 500 .72rem/1 var(--font-mono); text-transform: uppercase; letter-spacing: .05em; color: var(--muted); border: 1px solid var(--rule); border-radius: 999px; padding: .3rem .55rem; }
.glance { display: grid; gap: .5rem; }
.row { display: grid; grid-template-columns: 6.5rem 1fr; gap: .25rem .9rem; align-items: start; padding: .75rem .9rem; border-radius: 8px; background: var(--surface); border: 1px solid var(--rule); }
.row .topic { font-weight: 600; grid-column: 2; }
.row .fact, .row .labels { grid-column: 2; }
.kind { grid-row: 1 / span 3; font: 600 .72rem/1 var(--font-mono); text-transform: uppercase; letter-spacing: .04em; padding: .35rem .5rem; border-radius: 6px; justify-self: start; }
.kind.checked { color: var(--checked); background: var(--tint-checked); }
.kind.limited { color: var(--limited); background: var(--tint-limited); }
.kind.not-done { color: var(--notdone); background: var(--tint-notdone); }
.labels { display: flex; flex-wrap: wrap; gap: .35rem; }
.label { font-size: .8rem; color: var(--muted); border: 1px solid var(--rule); border-radius: 6px; padding: .15rem .45rem; }
.label code, code { font-family: var(--font-mono); font-size: .78em; color: var(--ink); }
blockquote { margin: 0; background: var(--quote); border: 1px solid var(--rule); border-left: 3px solid var(--ink); border-radius: 6px; padding: .85rem 1rem; display: grid; gap: .45rem; }
blockquote p { font: 1.08rem/1.5 var(--font-display); }
.where { font-size: .82rem; color: var(--muted); display: flex; flex-wrap: wrap; gap: .3rem .8rem; align-items: center; }
.note { font-size: .88rem; color: var(--muted); }
.result { display: flex; flex-wrap: wrap; align-items: center; gap: .5rem; }
.subs { display: grid; gap: .6rem; }
.table-wrap { overflow-x: auto; }
table { border-collapse: collapse; width: 100%; font-size: .85rem; font-variant-numeric: tabular-nums; }
th, td { text-align: left; padding: .35rem .5rem; border-bottom: 1px solid var(--rule); vertical-align: top; }
th { font-weight: 600; color: var(--muted); }
td code { white-space: nowrap; }
.model p { font-size: .95rem; }
.model .state { font-size: .8rem; color: var(--muted); }
.reviews { display: grid; gap: .75rem; grid-template-columns: repeat(auto-fit, minmax(17rem, 1fr)); }
.reviews ul, .missing ul { margin: 0; padding-left: 1.1rem; display: grid; gap: .35rem; }
.crumb { font-size: .88rem; color: var(--muted); display: flex; flex-wrap: wrap; gap: .3rem .6rem; align-items: baseline; }
.parts li { font-size: .9rem; }
.refs { font: .72rem/1.4 var(--font-mono); color: var(--muted); display: inline-flex; flex-wrap: wrap; gap: .2rem .5rem; }
.refs a, a { color: var(--accent); }
a:focus-visible, summary:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; border-radius: 4px; }
details { background: var(--surface); border: 1px solid var(--rule); border-radius: 10px; padding: .7rem 1rem; min-width: 0; }
details + details { margin-top: .6rem; }
summary { cursor: pointer; font-weight: 600; }
details > div { margin-top: .75rem; display: grid; gap: .6rem; }
.mono { font-family: var(--font-mono); font-size: .78rem; overflow-wrap: anywhere; }
footer { font-size: .85rem; color: var(--muted); display: grid; gap: .4rem; border-top: 1px solid var(--rule); padding-top: 1rem; }
@media (max-width: 30rem) { .row { grid-template-columns: 1fr; } .kind { grid-row: auto; } .row .topic, .row .fact, .row .labels { grid-column: 1; } }
@media (prefers-reduced-motion: reduce) { * { scroll-behavior: auto; } }
"""


def html_page(view: dict) -> str:
    present = {r["id"] for r in view["technical"]["records"]}

    def R(ids):
        return refs(ids, present)

    out = []
    w = out.append
    w("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
      "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
      "<title>Power posing and testosterone: the record</title>\n"
      "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n"
      "<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600"
      "&amp;family=IBM+Plex+Sans:wght@400;500;600&amp;family=Newsreader:opsz,wght@6..72,400;6..72,600&amp;display=swap\">\n"
      f"<style>{CSS}</style>\n</head>\n<body>\n<main>\n")

    claim = view["claim"]
    ctx = view.get("context")
    if ctx:
        w(f'<nav class="crumb" aria-label="Question"><a href="{e(ctx["href"])}">&larr; The question</a>'
          f'<span>This paper is {e(ctx["member_label"])}, one of {e(ctx["denominator"])} declared sources for: '
          f'&ldquo;{e(ctx["question_text"])}&rdquo;</span>{chip(ctx["wording"])}{chip(ctx["confirmation"])}'
          f'{R(ctx["refs"])}</nav>\n')
    w('<header>\n<div class="eyebrow">Provenance Atlas &middot; one claim, one paper</div>\n'
      "<h1>Power posing and testosterone: what the record shows</h1>\n"
      f'<p class="citation">{e(view["paper"]["citation"])}</p>\n'
      '<div class="legend"><span><span class="serif">Serif</span>: the paper\'s own words</span>'
      '<span>Sans, tagged: written by a model</span><span><span class="mono">Mono</span>: Atlas checks and labels</span>'
      "</div>\n</header>\n")

    w('<section aria-labelledby="h-claim">\n<h2 id="h-claim">The claim being checked</h2>\n'
      f'<div class="card claim"><span class="tag">{e(claim["written_by"])}</span>'
      f'<p>{e(claim["text"])}</p>{R(claim["refs"])}</div>\n'
      '<p class="note">Atlas does not say whether this claim is true. It shows what was checked, what held up, '
      "what is missing, and who disagrees. You judge.</p>\n</section>\n")

    w('<section aria-labelledby="h-glance">\n<h2 id="h-glance">At a glance</h2>\n<div class="glance">\n')
    for g in view["at_a_glance"]:
        labels = "".join(chip(l) for l in g["labels"])
        w(f'<div class="row"><span class="kind {e(g["kind"])}">{e(KIND[g["kind"]])}</span>'
          f'<span class="topic">{e(g["topic"])}</span><p class="fact">{e(g["fact"])}</p>'
          f'<div class="labels">{labels}{R(g["refs"])}</div></div>\n')
    w("</div>\n</section>\n")

    w('<section aria-labelledby="h-paper">\n<h2 id="h-paper">What the paper itself says</h2>\n')
    for p in view["paper_says"]:
        w(f'<blockquote id="q-{e(p["anchor_id"])}"><p>{e(p["text"])}</p>'
          f'<div class="where"><span>p. {e(p["page"])}, {e(p["section"])}</span>{chip(p["match"])}'
          f'<code>{e(p["anchor_id"])}</code>{R(p["refs"])}</div></blockquote>\n')
    w(f'<p class="note">{e(view["paper_says_note"])}</p>\n</section>\n')

    check = view["check"]
    w('<section aria-labelledby="h-check">\n<h2 id="h-check">Do the numbers add up?</h2>\n'
      f'<div class="card"><div class="result">{chip(check["result"])}<code>{e(check["name"])}</code></div>'
      f'<p class="note">Checked against the paper\'s Results sentence (quote {e(check["evidence_anchor"])} above). '
      f'{e(check["scope"])}</p><div class="subs">\n')
    for sub in check["sub_checks"]:
        w(f'<div><h3>{e(sub["question"])}</h3><div class="result">{chip(sub["result"])}</div>')
        d = sub["detail"]
        if "rows" in d:
            w('<div class="table-wrap"><table><thead><tr><th scope="col">Statistic</th><th scope="col">In the claim</th>'
              '<th scope="col">In the paper</th><th scope="col">Same</th></tr></thead><tbody>')
            for r in d["rows"]:
                w(f"<tr><td>{e(r['statistic'].replace('_', ' '))}</td><td><code>{e(number(r['claim']))}</code></td>"
                  f"<td><code>{e(number(r['paper']))}</code></td><td>{'yes' if r['same'] else 'no'}</td></tr>")
            w("</tbody></table></div>")
        elif "recomputed" in d:
            w(f'<p class="note">Recomputed p: <code>{e(number(d["recomputed"]))}</code>; reported p, as a rounding '
              f'range: <code>{e(number(d["reported"]))}</code>; degrees of freedom <code>{e(d["df"])}</code>.</p>')
        elif "implied" in d:
            w(f'<p class="note">t implied by the interval: <code>{e(number(d["implied"]))}</code>; reported t, as a '
              f'rounding range: <code>{e(number(d["reported"]))}</code>. Interval centred on the mean difference: '
              f'{"yes" if d["ci_centred_on_mean"] else "no"}.</p>')
        w("</div>\n")
    w('</div><p class="note">Not checked: ' + "; ".join(e(n) for n in check["not_checked"]) + ".</p>"
      f'{R(check["refs"])}</div>\n</section>\n')

    w('<section aria-labelledby="h-run">\n<h2 id="h-run">What the extraction run found</h2>\n'
      '<p class="note">A model read the paper using the claim-extraction instrument and wrote this map. '
      "It is quoted as written. No person has reviewed it.</p>\n")
    for f in view["run_findings"]:
        label = f["native_label"] + ("" if f["label_status"] == "EXACT" else f" (label {f['label_status'].lower()})")
        w(f'<div class="card model"><h3>{e(f["title"])}</h3><span class="tag">Model-written &middot; field '
          f'{e(f["field"])}: {e(label)}</span><p>{e(f["content"])}</p>'
          f'<p class="state">The run\'s own label: <code>{e(f["verification_state"])}</code></p>{R(f["refs"])}</div>\n')
    w("</section>\n")

    w('<section aria-labelledby="h-reviews">\n<h2 id="h-reviews">Earlier reviews of the same passages</h2>\n'
      '<p class="note">Two model reviews were made for an earlier audit of a different paper. Four of the quotes above '
      "lie inside the passages they were given. They are shown as they are, including where they differ.</p>\n"
      '<div class="reviews">\n')
    for r in view["reviews"]:
        parts = "".join(f'<li>{e(p["text"])} {chip(p["disposition"])}</li>' for p in r["parts"])
        w(f'<div class="card"><h3>Review {e(r["review_id"].rsplit("-", 1)[-1])}</h3>'
          f'<span class="tag">{e(r["reviewer"])}</span><div class="result">{chip(r["disposition"])}</div>'
          f'<p>Sentence reviewed: &ldquo;{e(r["proposition"])}&rdquo;</p><ul class="parts">{parts}</ul>'
          f'<div class="labels">{chip(r["independence"])}{chip(r["human_adjudication"])}</div>'
          f'<p class="note">Paper quotes inside its passages: {e(", ".join(r["paper_quotes_inside_its_passages"]))}. '
          f'{e(r["context"])}</p>{R(r["refs"])}</div>\n')
    w("</div>\n</section>\n")

    w('<section aria-labelledby="h-missing" class="missing">\n<h2 id="h-missing">What is missing or unverified</h2>\n'
      '<div class="card"><ul>')
    for m in view["missing"]:
        labels = "".join(chip(l) for l in m.get("labels", []))
        w(f"<li>{e(m['item'])} {labels}</li>")
    w("</ul></div>\n</section>\n")

    w('<section aria-labelledby="h-related">\n<h2 id="h-related">Related records</h2>\n')
    for r in view["related"]:
        w(f'<div class="card"><p>{e(r["text"])}</p><div class="labels">{chip(r["relation"])}{chip(r["identity"])}</div>'
          f'<p class="note">That map is {e(r["state"].lower())}.</p>{R(r["refs"])}</div>\n')
    w("</section>\n")

    t = view["technical"]
    w('<section aria-labelledby="h-tech">\n<h2 id="h-tech">Technical record</h2>\n'
      f'<p class="note">This page was generated from the records below after they were re-derived by '
      f'{e(t["replay"]["level"])} replay ({e(t["replay"]["result"])}). '
      "Regenerate it with <code>python -m atlas.view build</code>.</p>\n")
    w('<details><summary>All 60 source anchors</summary><div><div class="table-wrap"><table><thead><tr>'
      '<th scope="col">Anchor</th><th scope="col">Field</th><th scope="col">Kind</th><th scope="col">Page</th>'
      '<th scope="col">Match</th><th scope="col">On stated page</th><th scope="col">Shown</th></tr></thead><tbody>')
    for a in t["anchors"]:
        state = f'<code title="{e(a["state_plain"])}">{e(a["state"])}</code>' if a["state_plain"] else "&mdash;"
        w(f'<tr id="rec-{e(slug(a["record_id"]))}"><td><code>{e(a["anchor_id"])}</code></td><td>{e(a["field"])}</td>'
          f'<td>{e(a["kind"].lower())}</td><td>{e(a["page"] if a["page"] is not None else "—")}</td><td>{state}</td>'
          f'<td>{"yes" if a["page_consistent"] else ("no" if a["page_consistent"] is False else "—")}</td>'
          f'<td>{"quoted" if a["published"] else ("withheld" if a["state"] else "—")}</td></tr>')
    w("</tbody></table></div>")
    for a in t["anchors"]:
        if a["diagnostic"]:
            first = "; ".join(f'{d["op"]}: quote {json.dumps(d["quote"])}, text {json.dumps(d["extraction"])}'
                              for d in a["diagnostic"]["first_differences"][:2])
            w(f'<p class="note"><code>{e(a["anchor_id"])}</code> not found exactly. {e(a["diagnostic"]["basis"])}. '
              f'{e(first)}</p>')
    w("</div></details>\n")
    w('<details><summary>Fingerprints and receipt</summary><div class="mono">')
    for k, v in t["pins"].items():
        w(f"<div>{e(k)}: {e(v)}</div>")
    for k, v in t["receipt"].items():
        w(f"<div>receipt {e(k)}: {e(v)}</div>")
    w("</div></details>\n")
    w(f'<details><summary>All {len(t["records"])} records in this bundle</summary><div class="mono">')
    for r in t["records"]:
        if r["type"] != "SourceAnchor":
            w(f'<div id="rec-{e(slug(r["id"]))}">{e(r["type"])} &middot; {e(r["id"])}</div>')
    w("</div></details>\n</section>\n")

    w("<footer>" + "".join(f"<p>{e(rule)}</p>" for rule in view["rules"]) +
      f'<p>Generated by {e(view["generator"]["name"])} {e(view["generator"]["version"])} '
      f'&middot; labels {e(view["labels_table"])} &middot; It points; you judge.</p></footer>\n'
      "</main>\n"
      "<script>\n"
      "/* A record link into the technical section opens the section that holds it. */\n"
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


def wrap(text: str, indent: str = "") -> str:
    # A bullet marker starts the first line only; continuation lines align under the text.
    rest = indent[:-2] + "  " if indent.endswith("- ") else indent
    return textwrap.fill(" ".join(str(text).split()), 88, initial_indent=indent, subsequent_indent=rest)


def lab(label: dict) -> str:
    return f"{label['plain']} [{label['native']}]"


def text_report(view: dict) -> str:
    ctx = view.get("context")
    crumb = ([wrap(f"Part of a question ({ctx['href']}): this paper is {ctx['member_label']}, one of "
                   f"{ctx['denominator']} declared sources for “{ctx['question_text']}”"),
              f"  Question wording: {lab(ctx['wording'])}; {lab(ctx['confirmation'])}", ""] if ctx else [])
    out = [*crumb, "POWER POSING AND TESTOSTERONE: WHAT THE RECORD SHOWS", wrap(view["paper"]["citation"]), "",
           "Atlas does not say whether this claim is true. It shows what was checked, what held up, what is",
           "missing, and who disagrees. You judge.", "",
           "THE CLAIM BEING CHECKED", wrap(view["claim"]["written_by"], "  "), wrap(view["claim"]["text"], "    "), "",
           "AT A GLANCE"]
    for g in view["at_a_glance"]:
        out += [f"  [{KIND[g['kind']]}] {g['topic']}", wrap(g["fact"], "      ")]
        for l in g["labels"]:
            out.append("      - " + lab(l))
    out += ["", "WHAT THE PAPER ITSELF SAYS"]
    for p in view["paper_says"]:
        out += [wrap(p["text"], "    "), f"      p. {p['page']}, {p['section']} | {p['anchor_id']} | {lab(p['match'])}"]
    out += [wrap(view["paper_says_note"], "  "), "", "DO THE NUMBERS ADD UP?",
            f"  {lab(view['check']['result'])} ({view['check']['name']})", wrap(view["check"]["scope"], "  ")]
    for sub in view["check"]["sub_checks"]:
        out.append(f"  - {sub['question']} {lab(sub['result'])}")
        d = sub["detail"]
        if "rows" in d:
            for r in d["rows"]:
                out.append(f"      {r['statistic']}: claim {number(r['claim'])} | paper {number(r['paper'])} | "
                           f"{'same' if r['same'] else 'different'}")
        elif "recomputed" in d:
            out.append(f"      recomputed p {number(d['recomputed'])}; reported {number(d['reported'])}; df {d['df']}")
        elif "implied" in d:
            out.append(f"      implied t {number(d['implied'])}; reported {number(d['reported'])}; "
                       f"CI centred: {'yes' if d['ci_centred_on_mean'] else 'no'}")
    out += ["  Not checked: " + "; ".join(view["check"]["not_checked"]), "", "WHAT THE EXTRACTION RUN FOUND",
            "  A model wrote this map. Quoted as written; not reviewed by a person."]
    for f in view["run_findings"]:
        out += [f"  {f['title']} (field {f['field']}: {f['native_label']})", wrap(f["content"], "      "),
                f"      run's own label: {f['verification_state']}"]
    out += ["", "EARLIER REVIEWS OF THE SAME PASSAGES"]
    for r in view["reviews"]:
        out += [f"  Review {r['review_id']} by {r['reviewer']}: {lab(r['disposition'])}",
                wrap(f"Sentence reviewed: “{r['proposition']}”", "      ")]
        out += [f"      part {p['part']}: {p['text']} | {lab(p['disposition'])}" for p in r["parts"]]
        out += [f"      {lab(r['independence'])}; {lab(r['human_adjudication'])}",
                f"      paper quotes inside its passages: {', '.join(r['paper_quotes_inside_its_passages'])}"]
    out += ["", "WHAT IS MISSING OR UNVERIFIED"]
    out += [wrap(m["item"], "  - ") for m in view["missing"]]
    out += ["", "RELATED RECORDS"]
    for r in view["related"]:
        out += [wrap(r["text"], "  "), f"    {lab(r['relation'])}; {lab(r['identity'])}"]
    t = view["technical"]
    out += ["", "TECHNICAL RECORD", f"  replay: {t['replay']['result']} ({t['replay']['level']})"]
    out += [f"  {k}: {v}" for k, v in t["pins"].items()]
    out += [f"  receipt {k}: {v}" for k, v in t["receipt"].items()]
    out += ["", *[wrap(rule) for rule in view["rules"]],
            f"Generated by {view['generator']['name']} {view['generator']['version']}; labels {view['labels_table']}."]
    return "\n".join(out) + "\n"
