"""Check candidate quotes against a pdftotext extraction using the repo's own matcher (atlas.extraction.anchors)."""
import sys, json
sys.path.insert(0, "/workspace/Provenance-Atlas")
from atlas.extraction.anchors import NormalizedIndex, match
src = sys.argv[1]; quotes = [l.rstrip("\n") for l in open(sys.argv[2], encoding="utf-8") if l.strip()]
text = open(src, encoding="utf-8").read(); idx = NormalizedIndex(text)
for q in quotes:
    r = match(q, text, idx); print(r["state"], r["location"], r["found_page"], "|", q[:90])
