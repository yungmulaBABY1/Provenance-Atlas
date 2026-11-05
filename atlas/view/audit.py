"""Paper page for one imported audit: the paper, the claim under audit, the findings, the
review items and their challenges, and the sources, from verified map-link and challenge bundles.

This is a paper page, the side entry under the question-first path. No research question
record exists for this paper yet, and the page says so rather than inventing one. Every
item names the records it comes from. Model-written text is quoted and attributed. Plain
language comes only from the declared label table. No source text is shown, and no
outcome is merged, ranked or scored.
"""

from __future__ import annotations

from collections import Counter
from pathlib import Path

from . import SCHEMA, VERSION
from .labels import TABLE_ID, plain
from .model import check_refs
from .render import CSS, KIND, chip, e, lab, refs, slug, wrap
from ..challenge.build import replay as challenge_replay
from ..contract import ContractError, load_json, normalize, sha256
from ..maplink.build import replay as maplink_replay

MODEL_WRITTEN = "Written by a model run. Not the paper's words."
# Source-light: model-written text that quotes this many consecutive words of a source
# passage is withheld here, because no passage is reviewed for public release.
WINDOW = 8
AUDIT_CSS = """
.item h3, .finding h3 { display: flex; flex-wrap: wrap; gap: .4rem .6rem; align-items: baseline; }
.item h3 .id, .finding h3 .id { font: 600 .9rem/1 var(--font-mono); color: var(--accent); }
.check { font: .84rem/1.45 var(--font-mono); color: var(--ink); }
.differ { border-left: 4px solid var(--limited); background: var(--tint-limited); padding: .55rem .8rem; border-radius: 6px; font-size: .92rem; }
.challenge { border: 1px solid var(--rule); border-radius: 8px; padding: .75rem .9rem; display: grid; gap: .45rem; }
.challenge ul, .finding ul, .sources ul { margin: 0; padding-left: 1.1rem; display: grid; gap: .3rem; font-size: .9rem; }
.words p { font-size: .92rem; }
.sources td:first-child { min-width: 12rem; }
.sources td code { white-space: normal; overflow-wrap: anywhere; }
"""


def load_bundle(receipt_dir: Path) -> tuple[bytes, bytes, list[dict]]:
    manifest_bytes = (receipt_dir / "manifest.json").read_bytes()
    records_bytes = (receipt_dir / "records.jsonl").read_bytes()
    return manifest_bytes, records_bytes, [load_json(l) for l in records_bytes.splitlines() if l.strip()]


def import_pins(maplink_manifest: dict, challenge_manifest: dict, root: Path) -> tuple[dict, dict]:
    """Both bundles must rest on the same import: through the claim links, and directly."""
    claim_pins = maplink_manifest["input_context"]["claim_link_bundle"]
    claim_manifest = load_json((root / claim_pins["manifest"]["path"]).read_bytes())
    via_maplink = claim_manifest["input_context"]["dependency"]
    via_challenge = challenge_manifest["input_context"]["import_bundle"]
    if via_maplink != via_challenge:
        raise ContractError("AUDIT_RECEIPTS_DISAGREE: the map-link and challenge bundles pin different imports")
    return via_challenge, claim_pins


def verify_audit(page: dict, root: Path) -> dict:
    """Content-replay both bundles; each re-verifies what it pins. They must pin the same import."""
    bundles, results = {}, {}
    for key, replay in (("maplink", maplink_replay), ("challenge", challenge_replay)):
        directory = root / page[f"{key}_receipt"]
        manifest_bytes, records_bytes, records = load_bundle(directory)
        try:
            results[key] = replay(manifest_bytes, records_bytes, root, "content")
        except ContractError as exc:
            raise ContractError(f"NOT_VERIFIED: {key}: {exc}") from exc
        bundles[key] = {"records": records, "manifest": load_json(manifest_bytes),
                        "receipt": {"path": page[f"{key}_receipt"], "manifest_sha256": sha256(manifest_bytes),
                                    "records_sha256": sha256(records_bytes)}}
    via_challenge, claim_pins = import_pins(bundles["maplink"]["manifest"], bundles["challenge"]["manifest"], root)
    imported = [load_json(l) for l in (root / via_challenge["records"]["path"]).read_bytes().splitlines() if l.strip()]
    claims = [load_json(l) for l in (root / claim_pins["records"]["path"]).read_bytes().splitlines() if l.strip()]
    return {**bundles, "import": imported, "claims": claims, "replay": results,
            "pins": {"import": via_challenge, "claim_links": claim_pins}}


class Withholder:
    """Withholds any displayed text that carries WINDOW consecutive words of a source passage."""

    def __init__(self, passages: list[dict]):
        self.windows = {}
        for p in passages:
            words = normalize(p["quote"]).split()
            for i in range(0, max(1, len(words) - WINDOW + 1)):
                self.windows.setdefault(" ".join(words[i:i + WINDOW]), set()).add(p["native_id"])
        self.withheld = []

    def __call__(self, text: str | None, where: str) -> str | None:
        if text is None:
            return None
        # Substring, not word, match: a quotation mark or bracket attached to a word must not hide it.
        flat = normalize(text)
        hit = sorted({pid for window, pids in self.windows.items() if window in flat for pid in pids})
        if not hit:
            return text
        self.withheld.append({"where": where, "passages": hit})
        return (f"[Withheld here: this model-written text quotes {WINDOW} or more consecutive words of source "
                f"passage {', '.join(hit)}, which is not reviewed for public release. It is in the committed "
                "audit output.]")


def field_label(field: str, value: str) -> dict:
    return plain(value, field)


def build_audit_view(v: dict, root: Path) -> dict:
    imp = {r["id"]: r for r in v["import"]}
    cl = {r["id"]: r for r in v["claims"]}
    ml = {r["id"]: r for r in v["maplink"]["records"]}
    ch = {r["id"]: r for r in v["challenge"]["records"]}
    run = next(r for r in v["import"] if r["type"] == "AuditRun")
    work = imp[run["target_work_id"]]
    reads = [r for r in v["import"] if r["type"] == "SourceReadReceipt"]
    passages = [r for r in v["import"] if r["type"] == "Passage"]
    findings = sorted((r for r in v["import"] if r["type"] == "AuditFinding"), key=lambda r: r["native"]["number"])
    mrun = next(r for r in v["maplink"]["records"] if r["type"] == "MapLinkRun")
    umap = ml[mrun["upstream_map_id"]]
    crun = next(r for r in v["challenge"]["records"] if r["type"] == "ChallengeRun")
    items = [ch[i] for i in crun["item_ids"]]
    target_read = next(r for r in reads if r["work_id"] == work["id"])
    W = Withholder(passages)

    # The paper and the run.
    paper = {"work_id": work["id"], "title": work["metadata"]["title"], "read": plain(target_read["state"]),
             "note": "The paper's own words are not shown on this page.", "refs": [work["id"], target_read["id"]]}
    corpus = next(r for r in v["import"] if r["type"] == "CorpusScope")
    audit = {"run_id": run["id"], "producer": run["model"]["identity"],
             "producer_verification": plain(run["model"]["verification"]),
             "instrument": run["validation_instrument"]["path"], "checker": plain(run["checker_status"]),
             "human_review": field_label("human_review", run["human_review"]),
             "boundary": W(corpus["declared"]["boundary"], "corpus boundary"),
             "limitations": [W(x, "corpus limitation") for x in corpus["declared"]["limitations"]],
             "refs": [run["id"], corpus["id"]]}

    # At a glance: caveats sit beside what was checked; each row is a count from the records.
    matches = Counter(p["match"] for p in passages)
    states = Counter(r["state"] for r in reads)
    counts = crun["counts"]
    idents = Counter(a["claim_identity"] for a in (ml[i] for i in mrun["alignment_ids"]))
    recon = [ml[i] for i in mrun["reconciliation_ids"]]
    differ = [i for i in items if len({o["outcome"] for o in i["outcomes"]}) > 1]
    reviewers = sorted({ch[o["challenge_id"]]["challenger"]["identity"] for i in items for o in i["outcomes"]})
    kinds = sorted({o["decision_by"] for i in items for o in i["outcomes"]})
    quotes = umap["anchors"]["by_kind"].get("QUOTE", 0)
    glance = [
        {"kind": "checked", "topic": "Mechanical check of the audit output",
         "fact": f"The instrument's checker passes the output's form and leaves {counts['items']} items for review.",
         "labels": [plain(run["checker_status"])], "refs": [run["id"], crun["id"]]},
        {"kind": "checked", "topic": "Passages the audit cites",
         "fact": f"{matches.get('MATCH', 0)} of {len(passages)} match their retrieved copy word for word.",
         "labels": [plain(m) for m in sorted(matches)], "refs": [run["id"]]},
        {"kind": "limited", "topic": "Who ran and reviewed it",
         "fact": (f"Produced by {run['model']['identity']}, as the run reports it. The {counts['items']} review items "
                  f"have {counts['challenges']} challenges from {len(reviewers)} reviewers ({', '.join(reviewers)}). "
                  f"{counts['items_with_a_decision_by_a_person']} of {counts['items']} have a decision by a person."),
         "labels": [plain(run["model"]["verification"]), *[plain(k) for k in kinds]], "refs": [run["id"], crun["id"]]},
        *[{"kind": "limited", "topic": f"Reviewers disagree on item {i['item_number']}",
           "fact": "; ".join(f"{ch[o['challenge_id']]['challenger']['identity']}: {o['outcome']}" for o in i["outcomes"])
                   + ". Both are kept; nothing merges them.",
           "labels": [plain(o) for o in sorted({o["outcome"] for o in i["outcomes"]})], "refs": [i["id"]]}
          for i in differ],
        {"kind": "limited", "topic": "The claim under audit",
         "fact": (f"The claim map words it in {1 + len(map_variants(v['maplink']['records'], umap))} places, and they "
                  f"differ from each other. The audit restates {len(recon)} map fields; "
                  f"{sum(1 for r in recon if r['claim_identity'] != 'SAME_TEXT')} of {len(recon)} differ from the "
                  "map's text."),
         "labels": [plain("UNRESOLVED_REQUIRES_REVIEW")], "refs": [umap["id"], *mrun["reconciliation_ids"]]},
        {"kind": "limited", "topic": "Findings against the claim",
         "fact": (f"{idents.get('DECLARED_NOT_FIELD_6', 0)} of {len(findings)} say they target something other than "
                  f"the claim under audit; {idents.get('UNRESOLVED_REQUIRES_REVIEW', 0)} of {len(findings)} need a "
                  "person to judge."),
         "labels": [plain(k) for k in sorted(idents)], "refs": [mrun["id"]]},
        {"kind": "limited", "topic": "Sources",
         "fact": "; ".join(f"{n} of {len(reads)} {phrase}" for state, n, phrase in
                           [(s, states[s], {"PARTIAL_READ": "partly read",
                                            "RETRIEVAL_FAILED": "could not be retrieved"}[s]) for s in sorted(states)])
                 + ".",
         "labels": [plain(s) for s in sorted(states)], "refs": [run["id"]]},
        {"kind": "not-done", "topic": "Quotes in the claim map",
         "fact": f"{quotes} quotes are not checked against the paper; its text is not among the committed files.",
         "labels": [], "refs": [umap["id"]]},
        {"kind": "not-done", "topic": "Other audit stages",
         "fact": ("Atlas holds one stage of this audit, the citation-network run. No replication, internal-validity "
                  "or construct-validity record exists in Atlas."),
         "labels": [], "refs": [run["id"]]},
    ]

    # The claim under audit, as the map words it, and the audit's restatements.
    designated = ml[umap["designated_field_6_id"]]
    claim = {"text": W(designated["text"], "claim under audit"), "written_by": "Written by the claim map's producer, a model. Not the paper's words.",
             "producer": umap["provenance"]["producer"]["identity"],
             "producer_verification": umap["provenance"]["producer"]["verification"],
             "producer_state": ml[umap["fields"]["6"]["statement_id"]]["producer_verification_state"],
             "provenance": [plain(umap["origin"]), field_label("run_prompt", umap["provenance"]["run_prompt"]),
                            field_label("run_receipt", umap["provenance"]["run_receipt"]),
                            plain(umap["audit_output_reference"]["state"])],
             "source_statement": plain(mrun["source_statement"]["state"]),
             "source_note": mrun["source_statement"]["note"],
             "variants": [{"role": ml[c["object_id"]]["role"], "where": ROLE_WHERE[ml[c["object_id"]]["role"]],
                           "text": W(ml[c["object_id"]]["text"], "claim map wording"),
                           "result": field_label("text_comparison", c["result"]), "refs": [c["id"], c["object_id"]]}
                          for c in map_variants(v["maplink"]["records"], umap)],
             "restatements": [{"field": r["field"], "text": W(cl[r["audit_output_statement_id"]]["exact_text"],
                                                              "audit restatement"),
                               "line": cl[r["audit_output_statement_id"]]["anchor"]["first_line"],
                               "result": field_label("text_comparison", ml[r["comparison_id"]]["result"]),
                               "identity": plain(r["claim_identity"]), "refs": [r["id"], r["comparison_id"]]}
                              for r in recon if r["comparison_id"]],
             "refs": [umap["id"], designated["id"]]}

    # Findings, with their native labels and how each lines up with the map.
    aligned = {ml[i]["finding_id"]: ml[i] for i in mrun["alignment_ids"]}
    finding_views = []
    for f in findings:
        labels = f["native"]["labels"]
        al = aligned[f["id"]]
        finding_views.append({
            "number": f["native"]["number"],
            "title": W(f["native"]["fields"]["Finding"], f"finding {f['native']['number']}"),
            "labels": [plain(labels["Concede test"]), field_label("status", labels["Status"]),
                       field_label("severity", labels["Severity"]),
                       *[plain(s) for s in labels["Verification state"]], plain(labels["Failure location"])],
            "record": [plain(f["import_status"]), plain(f["assessment"])],
            "alignment": [plain(al["claim_identity"]),
                          *([plain(al["map_gap_form"])] if al["map_gap_form"] == "WORDING_DIFFERS_FROM_INSTRUMENT_FORMS"
                            else [])],
            "without_map": plain(al["claim_link_identity"]),
            "target": W(cl[al["finding_target_id"]]["exact_text"] if al["finding_target_id"] else None,
                        f"finding {f['native']['number']} target"),
            "refs": [f["id"], al["id"]]})

    # Review items and challenges.
    item_views = []
    for item in items:
        challenges = []
        for o in item["outcomes"]:
            c = ch[o["challenge_id"]]
            rel = c["relation_to_run"]
            challenges.append({
                "outcome": plain(c["outcome"]), "challenger": c["challenger"]["identity"],
                "kind": plain(c["decision_by"]), "performed_at": c["performed_at"],
                "relation": [field_label("producer", rel["producer"]),
                             field_label("atlas_code_author", rel["atlas_code_author"])],
                "prior_position": W(c["exposure"]["prior_position"], "prior position"),
                "seen_before": [W(x, "exposure") for x in c["exposure"]["seen_before_deciding"]],
                "transcription": plain(c["transcription"]["state"]),
                "reasons": [W(x, "challenge reason") for x in c["reasons"]],
                "parts": [{"part": p["part"], "outcome": plain(p["outcome"]),
                           "reasons": [W(x, "challenge part reason") for x in p["reasons"]]} for p in c["parts"]],
                "what_would_change": [W(x, "what would change") for x in c["what_would_change"]],
                "evidence": [ev["id"] if ev["kind"] == "RECORD" else
                             f"{ev['identifier']} (external, as cited)" if ev["kind"] == "EXTERNAL" else
                             ev["path"].replace("examples/research/acemoglu-colonial-origins/", "")
                             + (f" lines {ev['lines'][0]}-{ev['lines'][1]}" if ev.get("lines") else "")
                             + (f" ({ev['note']})" if ev.get("note") else "")
                             for ev in c["evidence"]],
                "refs": [c["id"]]})
        item_views.append({
            "number": item["item_number"], "code": item["item_code"], "instruction": item["instruction"],
            "state": plain(item["challenge_state"]),
            "differ": len({o["outcome"] for o in item["outcomes"]}) > 1,
            "challenges": challenges, "refs": [item["id"]]})

    # Sources.
    titles = {r["id"]: r["metadata"]["title"] for r in v["import"] if r["type"] == "Work"}
    versions = {r["id"]: r["work_id"] for r in v["import"] if r["type"] == "SourceVersion"}
    per_work = Counter(versions.get(p["source_version_id"]) for p in passages)
    sources = [{"work_id": r["work_id"], "title": titles[r["work_id"]], "read": plain(r["state"]),
                "target": r["work_id"] == work["id"], "passages": per_work.get(r["work_id"], 0),
                "refs": [r["work_id"], r["id"]]}
               for r in sorted(reads, key=lambda r: (r["work_id"] != work["id"], titles[r["work_id"]]))]
    rights = sorted(Counter(r["rights"] for r in reads).items())
    rights_text = "; ".join(f"{n} of {len(reads)} sources are marked {mark}" for mark, n in rights)

    unresolved = [str(a["finding_number"]) for a in (ml[i] for i in mrun["alignment_ids"])
                  if a["claim_identity"] == "UNRESOLVED_REQUIRES_REVIEW"]
    not_established = [
        {"item": f"No person has decided any review item ({counts['items_with_a_decision_by_a_person']} of "
                 f"{counts['items']}). The challenges on record are models' decisions.", "refs": [crun["id"]]},
        {"item": "Which wording is the claim under audit is not settled: the map's wordings and the audit's "
                 "restatement differ as text.", "refs": [umap["id"], *mrun["reconciliation_ids"]]},
        {"item": f"Whether findings {', '.join(unresolved)} target the claim under audit needs a person to judge.",
         "refs": [mrun["id"]]},
        {"item": f"The {quotes} quotes in the claim map are not verified against the paper.", "refs": [umap["id"]]},
        {"item": "The reviewers' identities, independence and exposure are as they declared them, not verified.",
         "refs": [crun["id"]]},
        {"item": f"Rights to republish the sources' excerpts are not reviewed: {rights_text}.", "refs": [run["id"]]},
        {"item": "No research question record exists for this paper yet. This page is a paper page.", "refs": []},
    ]

    present = {r["id"] for r in v["maplink"]["records"]} | {r["id"] for r in v["challenge"]["records"]}
    view = {
        "schema": SCHEMA, "kind": "audit", "generator": {"name": "atlas-view", "version": VERSION},
        "labels_table": TABLE_ID, "paper": paper, "audit": audit, "glance": glance, "claim": claim,
        "findings": finding_views, "items": item_views, "sources": sources,
        "passage_text_note": (f"No source text is shown. {rights_text[0].upper()}{rights_text[1:]}."
                              + (f" {len(W.withheld)} model-written text(s) are withheld because they quote a source "
                                 "passage: " + "; ".join(f"{x['where']} ({', '.join(x['passages'])})"
                                                         for x in W.withheld) + "." if W.withheld else "")),
        "not_established": not_established,
        "withheld": W.withheld,
        "technical": {
            "replay": {k: {"level": r["level"], "result": r["replay"]} for k, r in v["replay"].items()},
            "receipts": {"import": v["pins"]["import"], "claim_links": v["pins"]["claim_links"],
                         "maplink": v["maplink"]["receipt"], "challenge": v["challenge"]["receipt"]},
            "records": [{"id": r["id"], "type": r["type"]} for r in
                        sorted([*v["maplink"]["records"], *v["challenge"]["records"]], key=lambda r: r["id"])]},
        "rules": ["Nothing on this page is a verdict on the paper, the audit or its findings. No score is computed.",
                  "Model-written text is quoted and attributed. The paper's own words are not shown.",
                  f"Model-written text that quotes {WINDOW} or more consecutive words of a source passage is withheld.",
                  "Plain-language wording comes only from the declared label table, beside the native label.",
                  "Where reviewers disagree, every outcome is shown; none is merged or ranked."],
    }
    check_refs(view, present | set(imp) | set(cl))
    return view


ROLE_WHERE = {"TABLE_FIELD_6": "its output table, field 6", "SUMMARY_CLAIM_UNDER_AUDIT": "its one-line summary"}


def map_variants(records: list[dict], umap: dict) -> list[dict]:
    """The map's other wordings of Field 6, compared with its designated statement."""
    return [r for r in records if r["type"] == "TextComparison"
            and r["subject_id"] == umap["designated_field_6_id"] and "/compare/map-field-6-section~" in r["id"]]


def html_audit(view: dict) -> str:
    present = {r["id"] for r in view["technical"]["records"]}

    def R(ids):
        return refs(ids, present)

    p, a, c = view["paper"], view["audit"], view["claim"]
    out = []
    w = out.append
    w("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n<meta charset=\"utf-8\">\n"
      "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
      f"<title>{e(p['title'])}: one imported audit</title>\n"
      "<link rel=\"preconnect\" href=\"https://fonts.googleapis.com\">\n"
      "<link rel=\"stylesheet\" href=\"https://fonts.googleapis.com/css2?family=IBM+Plex+Mono:wght@400;500;600"
      "&amp;family=IBM+Plex+Sans:wght@400;500;600&amp;family=Newsreader:opsz,wght@6..72,400;6..72,600&amp;display=swap\">\n"
      f"<style>{CSS}{AUDIT_CSS}</style>\n</head>\n<body>\n<main>\n")
    w('<header>\n<div class="eyebrow">Provenance Atlas &middot; one paper, one imported audit</div>\n'
      f"<h1>{e(p['title'])}</h1>\n"
      f'<p class="citation"><code>{e(p["work_id"])}</code> {chip(p["read"])}</p>\n'
      '<div class="legend"><span>Sans, tagged: written by a model</span>'
      '<span><span class="mono">Mono</span>: Atlas checks and labels</span>'
      f"<span>{e(p['note'])}</span></div>\n</header>\n")

    w('<section aria-labelledby="h-glance">\n<h2 id="h-glance">At a glance</h2>\n<div class="glance">\n')
    for row in view["glance"]:
        w(f'<div class="row"><span class="kind {e(row["kind"])}">{e(KIND[row["kind"]])}</span>'
          f'<span class="topic">{e(row["topic"])}</span><span class="fact">{e(row["fact"])}</span>'
          f'<span class="labels">{"".join(chip(l) for l in row["labels"])}{R(row["refs"])}</span></div>\n')
    w('</div>\n<p class="note">Atlas does not say whether the paper or the audit is right. It shows what is on '
      "record, what was checked, and what is missing. You judge.</p>\n</section>\n")

    w('<section aria-labelledby="h-audit">\n<h2 id="h-audit">The audit on record</h2>\n'
      f'<div class="card"><p>Run by <strong>{e(a["producer"])}</strong> with <code>{e(a["instrument"])}</code>.</p>'
      f'<div class="labels">{chip(a["producer_verification"])}{chip(a["checker"])}{chip(a["human_review"])}</div>'
      f'<div class="card model"><span class="tag">The run’s own words: corpus</span><p>{e(a["boundary"])}</p></div>'
      f'<details><summary>The run’s stated limitations ({len(a["limitations"])})</summary><div class="words">'
      + "".join(f"<p>{e(x)}</p>" for x in a["limitations"]) + f"</div></details>{R(a['refs'])}</div>\n</section>\n")

    w('<section aria-labelledby="h-claim">\n<h2 id="h-claim">The claim under audit</h2>\n'
      f'<div class="card claim model"><span class="tag">{e(c["written_by"])}</span><p>{e(c["text"])}</p>'
      f'<p class="state">Producer: {e(c["producer"])} ({e(c["producer_verification"])}). '
      f'The map’s own verification column: {e(c["producer_state"])}</p>'
      f'<div class="labels">{"".join(chip(l) for l in c["provenance"])}</div>{R(c["refs"])}</div>\n'
      f'<div class="card"><div class="labels">{chip(c["source_statement"])}</div><p class="note">{e(c["source_note"])}</p></div>\n'
      '<details><summary>Other wordings of the same claim</summary><div>')
    for var in c["variants"]:
        w(f'<div class="card model"><span class="tag">The map, {e(var["where"])} ({e(var["role"])})</span><p>{e(var["text"])}</p>'
          f'<div class="labels">{chip(var["result"])}{R(var["refs"])}</div></div>')
    for r in c["restatements"]:
        w(f'<div class="card model"><span class="tag">The audit output, line {e(r["line"])}: map field {e(r["field"])}</span>'
          f'<p>{e(r["text"])}</p><div class="labels">{chip(r["result"])}{chip(r["identity"])}{R(r["refs"])}</div></div>')
    w("</div></details>\n</section>\n")

    w('<section aria-labelledby="h-findings">\n<h2 id="h-findings">Findings</h2>\n'
      '<p class="note">Each finding as the run wrote it, with its own labels, and how its stated target lines up '
      "with the claim under audit. No one has ruled on any of them.</p>\n")
    for f in view["findings"]:
        w(f'<div class="card finding model" id="finding-{e(f["number"])}"><h3><span class="id">Finding {e(f["number"])}</span></h3>'
          f'<span class="tag">{e(MODEL_WRITTEN)}</span><p>{e(f["title"])}</p>'
          f'<div class="labels">{"".join(chip(l) for l in f["labels"])}</div>'
          f'<div class="labels">{"".join(chip(l) for l in f["record"])}</div>'
          f'<div class="labels">Against the claim map: {"".join(chip(l) for l in f["alignment"])}</div>')
        if f["target"]:
            w(f'<details><summary>Its stated target</summary><div class="words"><p>{e(f["target"])}</p>'
              f'<p class="note">Without the map this was {lab(f["without_map"])}.</p></div></details>')
        w(f"{R(f['refs'])}</div>\n")
    w("</section>\n")

    w('<section aria-labelledby="h-items">\n<h2 id="h-items">Review items and challenges</h2>\n'
      '<p class="note">The checker leaves these items for review. A challenge is one reviewer’s decision on one '
      "item, kept beside the audit. It replaces nothing.</p>\n")
    for item in view["items"]:
        w(f'<div class="card item" id="item-{e(item["number"])}"><h3><span class="id">Item {e(item["number"])}</span>'
          f'<code>{e(item["code"])}</code></h3><p class="check">{e(item["instruction"])}</p>'
          f'<div class="labels">{chip(item["state"])}{R(item["refs"])}</div>')
        if item["differ"]:
            w('<p class="differ">The reviewers disagree on this item. Both outcomes are kept; nothing here '
              "merges or ranks them.</p>")
        for ch in item["challenges"]:
            w(f'<div class="challenge"><div class="labels">{chip(ch["outcome"])}</div>'
              f'<p>By <strong>{e(ch["challenger"])}</strong>, {e(ch["performed_at"])}</p>'
              f'<div class="labels">{chip(ch["kind"])}{"".join(chip(l) for l in ch["relation"])}{chip(ch["transcription"])}</div>'
              f'<details><summary>Prior position and what it saw first</summary><div class="words">'
              f'<p>{e(ch["prior_position"])}</p>' + "".join(f"<p>{e(s)}</p>" for s in ch["seen_before"]) +
              "</div></details>")
            if ch["parts"]:
                w("<ul>" + "".join(f'<li>{e(pt["part"])}: {chip(pt["outcome"])}</li>' for pt in ch["parts"]) + "</ul>")
            w(f'<details><summary>Its reasons, in its own words ({len(ch["reasons"])})</summary><div class="words">'
              + "".join(f"<p>{e(r)}</p>" for r in ch["reasons"]) + "</div></details>")
            w('<details><summary>What would change its answer, and its evidence</summary><div class="words">'
              + "".join(f"<p>{e(x)}</p>" for x in ch["what_would_change"])
              + "<ul>" + "".join(f"<li><code>{e(x)}</code></li>" for x in ch["evidence"]) + "</ul></div></details>"
              f"{R(ch['refs'])}</div>")
        w("</div>\n")
    w("</section>\n")

    w('<section aria-labelledby="h-src" class="sources">\n<h2 id="h-src">The sources</h2>\n'
      f'<p class="note">{e(view["passage_text_note"])}</p>\n<div class="table-wrap"><table>'
      "<thead><tr><th>Source</th><th>Read</th><th>Passages cited</th></tr></thead><tbody>")
    for s in view["sources"]:
        w(f'<tr><td>{"<strong>" if s["target"] else ""}{e(s["title"])}{"</strong>" if s["target"] else ""}'
          f'<br><code>{e(s["work_id"])}</code></td><td>{chip(s["read"])}</td><td>{e(s["passages"])}</td></tr>')
    w("</tbody></table></div>\n</section>\n")

    w('<section aria-labelledby="h-missing" class="missing">\n<h2 id="h-missing">Not established</h2>\n'
      '<div class="card"><ul>')
    for item in view["not_established"]:
        w(f"<li>{e(item['item'])} {R(item['refs'])}</li>")
    w("</ul></div>\n</section>\n")

    t = view["technical"]
    w('<section aria-labelledby="h-tech">\n<h2 id="h-tech">Technical record</h2>\n'
      '<p class="note">This page was generated after both bundles were re-derived by content replay ('
      + ", ".join(f"{e(k)} {e(r['result'])}" for k, r in t["replay"].items())
      + "). Each replay re-verified the bundles it pins. Regenerate with <code>python -m atlas.view build-all</code>.</p>\n"
      '<details><summary>Receipts</summary><div class="mono">')
    for name, pins in t["receipts"].items():
        if "path" in pins:
            w(f"<div>{e(name)}: {e(pins['path'])} records {e(pins['records_sha256'])}</div>")
        else:
            w(f"<div>{e(name)}: {e(pins['records']['path'])} records {e(pins['records']['sha256'])}</div>")
    w("</div></details>\n")
    w(f'<details><summary>The {len(t["records"])} map-link and challenge records</summary><div class="mono">')
    for r in t["records"]:
        w(f'<div id="rec-{e(slug(r["id"]))}">{e(r["type"])} &middot; {e(r["id"])}</div>')
    w("</div></details>\n</section>\n")
    w("<footer>" + "".join(f"<p>{e(rule)}</p>" for rule in view["rules"]) +
      f'<p>Generated by {e(view["generator"]["name"])} {e(view["generator"]["version"])} '
      f'&middot; labels {e(view["labels_table"])} &middot; It points; you judge.</p></footer>\n'
      "</main>\n</body>\n</html>\n")
    return "".join(out)


def text_audit(view: dict) -> str:
    p, a, c = view["paper"], view["audit"], view["claim"]
    out = [p["title"].upper(), f"{p['work_id']}  |  {lab(p['read'])}", p["note"], "",
           "Atlas does not say whether the paper or the audit is right. It shows what is on record, what was",
           "checked, and what is missing. You judge.", "", "AT A GLANCE"]
    for row in view["glance"]:
        out += [f"  [{KIND[row['kind']]}] {row['topic']}", wrap(row["fact"], "    ")]
        out += [f"    {lab(l)}" for l in row["labels"]]
    out += ["", "THE AUDIT ON RECORD", wrap(f"Run by {a['producer']} with {a['instrument']}.", "  "),
            f"  {lab(a['producer_verification'])}", f"  {lab(a['checker'])}", f"  {lab(a['human_review'])}",
            "  The run's own words, corpus:", wrap(a["boundary"], "    "), "  The run's stated limitations:"]
    out += [wrap(x, "    - ") for x in a["limitations"]]
    out += ["", "THE CLAIM UNDER AUDIT", f"  {c['written_by']}", wrap(c["text"], "    "),
            wrap(f"Producer: {c['producer']} ({c['producer_verification']}).", "  "),
            wrap(f"The map's own verification column: {c['producer_state']}", "  "),
            *[f"  {lab(l)}" for l in c["provenance"]], f"  {lab(c['source_statement'])}", wrap(c["source_note"], "    "),
            "  Other wordings:"]
    for var in c["variants"]:
        out += [f"    The map, {var['where']} ({var['role']}): {lab(var['result'])}", wrap(var["text"], "      ")]
    for r in c["restatements"]:
        out += [f"    The audit output, line {r['line']}, map field {r['field']}: {lab(r['result'])}; {lab(r['identity'])}",
                wrap(r["text"], "      ")]
    out += ["", "FINDINGS (as the run wrote them; no one has ruled on any)"]
    for f in view["findings"]:
        out += [f"  Finding {f['number']}  [{MODEL_WRITTEN}]", wrap(f["title"], "    "),
                *[f"    {lab(l)}" for l in f["labels"] + f["record"]],
                "    Against the claim map: " + "; ".join(lab(l) for l in f["alignment"])
                + f" (without the map: {lab(f['without_map'])})"]
    out += ["", "REVIEW ITEMS AND CHALLENGES"]
    for item in view["items"]:
        out += ["", f"  ITEM {item['number']}  {item['code']}  {lab(item['state'])}", wrap(item["instruction"], "    ")]
        if item["differ"]:
            out.append("    The reviewers disagree on this item. Both outcomes are kept; nothing merges or ranks them.")
        for ch in item["challenges"]:
            out += [f"    {lab(ch['outcome'])}", f"      by {ch['challenger']}, {ch['performed_at']}; {lab(ch['kind'])}",
                    *[f"      {lab(l)}" for l in ch["relation"]], f"      {lab(ch['transcription'])}",
                    wrap("Prior position: " + ch["prior_position"], "      ")]
            out += [f"      {pt['part']}: {lab(pt['outcome'])}" for pt in ch["parts"]]
            out.append(f"      Reasons ({len(ch['reasons'])}), in its own words:")
            out += [wrap(r, "        ") for r in ch["reasons"]]
            out.append("      What would change its answer:")
            out += [wrap(x, "        ") for x in ch["what_would_change"]]
            out.append("      Evidence: " + "; ".join(ch["evidence"]))
    out += ["", "THE SOURCES", wrap(view["passage_text_note"], "  ")]
    for s in view["sources"]:
        out.append(f"  {'*' if s['target'] else ' '} {s['title']} ({s['work_id']}): {lab(s['read'])}; "
                   f"passages cited: {s['passages']}")
    out += ["", "NOT ESTABLISHED", *[wrap(i["item"], "  - ") for i in view["not_established"]], "",
            "TECHNICAL", "  " + ", ".join(f"{k} replay {r['result']} ({r['level']})" for k, r in view["technical"]["replay"].items())]
    out += [f"  {rule}" for rule in view["rules"]]
    out.append(f"  Generated by {view['generator']['name']} {view['generator']['version']}; labels {view['labels_table']}.")
    return "\n".join(out) + "\n"
