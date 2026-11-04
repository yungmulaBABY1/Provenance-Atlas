"""PROBE, not an Atlas import. Reads 01_claim_extraction.md with the repo's strict reader
(atlas.extraction.output.parse) and matches each anchor quote against the declared pdftotext
extraction with the repo's matcher (atlas.extraction.anchors.match). Writes no Atlas receipt,
ledger, or bundle. Mechanical only: a MATCH says the string occurs in the extraction, nothing more."""
import sys, json, hashlib, subprocess
sys.path.insert(0, "/workspace/Provenance-Atlas")
from atlas.extraction.output import parse
from atlas.extraction.anchors import NormalizedIndex, match
out_path, src_path = sys.argv[1], sys.argv[2]
raw = open(out_path, "rb").read(); text = raw.decode("utf-8")
src = open(src_path, "rb").read(); stext = src.decode("utf-8"); idx = NormalizedIndex(stext)
parsed = parse(text)
rows = []
for a in parsed["anchors"]:
    e = {k: a[k] for k in ("id", "field", "kind", "stated_page", "stated_section")}
    if a["kind"] == "QUOTE" and a["quote"]:
        r = match(a["quote"]["text"], stext, idx)
        e.update(state=r["state"], location=r["location"], found_page=r["found_page"],
                 page_consistent=(r["found_page"] == a["stated_page"]) if r["found_page"] else None,
                 quote_sha256=r["quote_sha256"])
    rows.append(e)
ver = subprocess.run(["pdftotext", "-v"], capture_output=True, text=True).stderr.splitlines()[0]
res = {"probe": "anchor_probe/1 (scratch; not an Atlas contract)", "output_file": out_path,
       "output_sha256": hashlib.sha256(raw).hexdigest(), "extraction_file": src_path,
       "extraction_sha256": hashlib.sha256(src).hexdigest(), "extraction_tool": ver,
       "parser": parsed["parser"], "parse_issues": parsed["issues"],
       "preflight_disposition": parsed["preflight"]["disposition"] if parsed["preflight"] else None,
       "table_fields": sorted(parsed["table"]), "field_6_status": (parsed["field_6_section"] or {}).get("status"),
       "summaries": sorted(parsed["summaries"]), "anchors": rows,
       "counts": {s: sum(1 for r in rows if r.get("state") == s) for s in ("MATCH", "NORMALIZED_MATCH_ONLY", "MISMATCH")},
       "page_inconsistent": [r["id"] for r in rows if r.get("page_consistent") is False]}
print(json.dumps(res, indent=1))
