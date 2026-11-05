#!/bin/bash
# S2 citations of the target, paged (contexts = EXCERPT; s2/ not committed)
for off in 0 1000 2000 3000 4000 5000; do
  python3 scripts/fetch.py stage2c-s2 "https://api.semanticscholar.org/graph/v1/paper/DOI:10.1037/0022-3514.74.5.1252/citations?fields=title,year,externalIds,contexts,intents&limit=1000&offset=$off" s2/cit_$off.json
  sleep 5
done
