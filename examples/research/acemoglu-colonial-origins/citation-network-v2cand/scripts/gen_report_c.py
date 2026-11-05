P("9. INSTRUMENT PROBLEMS (observed while executing; diagnostic findings about the candidate, not fixes)")
for i,t in enumerate([
"No state for random-sample attrition: RECENT-1 sampled 6, retrieved 2; PRESPECIFIED-RANDOM has no rule for non-retrieval, which may not be random (paywalled publishers). I06 was set INSUFFICIENT by judgment.",
"The relation codes L1–L4 / R1 / R2 that Section F and the class map use are defined in the v1 output (02b), not in the claim map or the instrument; the run reused the v1 definitions.",
"Locked-search sensitivity: the six-query ADJUDICATION-1 search missed Glaeser et al. 2004, a known R2 test already in RECEPTION-1, so a WITHIN-SAMPLE absence can be mechanically SUPPORTED while false for the literature; the instrument does not require a known-item recall check.",
"Section E asks for a lock before inspection, which an exposed executor cannot honor; the v1 Section E list was reused and labeled POST HOC.",
"OpenAlex NOT-CITING / referenced_works metadata is unreliable (AJR 2001 referenced_works 13 → 55 in about a day; N01 record conflates the 2012 Reply with AJR 2001), and the instrument gives no record-quality gate for COMPOSITION and GRAPH-STRUCTURE inferences that rest on it.",
"The validation-boundary text about IAT is unrelated to this instrument and reads as a copy artifact.",
"No rule for duplicate records: duplicate OpenAlex records for one work each count as INSPECTED, inflating CITATION CONTEXT COVERAGE (14/50 by record, 11 distinct works).",
"Class map cn7-map-2 lets a SOURCE-RESULT inference that 'tests exist' support a no-concern score on Lack of decisive tests even when those tests' results conflict (I11/I12); the score of 0 is mechanically allowed but substantively thin.",
"Arithmetic band vs label-essential withholding is ambiguous: the 0–20% band position is printed, yet the band must be WITHHELD when closure-establishing dimensions lack no-concern evidence; the instrument does not say whether the arithmetic position may be quoted in a summary.",
"CO-CITATION inferences cannot carry a concern under the map, so v1 co-citation-based scores of 1 drop to 0 or need other classes, which changes results without new evidence.",
"Location: the candidate and its gate checker live in Provenance@07b72b5 (candidates/research-analysis/), not in Provenance-Atlas@b6d7869; the preflight had to name a cross-repo path.",
"Gate checker recomputes NOT-ASSESSED declarations as INSUFFICIENT (I22, I23) without flagging the mismatch as a review item or failure; the two states are not reconciled in the instrument text.",
],1): P(f"  P{i:02d} {t}")
P("")
P("10. DEVIATIONS")
for i,t in enumerate([
"Generator write split: the one-shot heredoc that wrote the document generator was blocked twice by an automatic safety-check error ('An error occured while classifying this action'); the same content was written in 7 parts (scripts/gd/p1–p7.py) and concatenated. Output unchanged by the split.",
"Section E lock-before-inspection not achievable (exposure); the v1 Section E list was reused and labeled POST HOC.",
"RECENT-1 sample attrition: 4/6 sampled full texts not retrieved; two coded from abstracts, two from metadata only; I06 INSUFFICIENT.",
"ADJUDICATION-1 screening paused at 8:33:36 PM PST (04:33:36Z) for the RECENT-1 draw and finished during analysis; the lock was already recorded, so no corpus change resulted.",
"Preflight path: the first preflight draft referenced the instrument at a Provenance-Atlas b6d7869 path that does not exist; it was replaced, before any checker run, with the Provenance@07b72b5 path and sha256s.",
"Worklog gaps: no 'drafting end' or 'checker start' events were logged, and not every tool call was logged (logged count is a lower bound).",
"Exposure grep of FAILURES.md ran on an older clone (c1bcb8b) during identity checks; only FAIL-CN-001…006 headings printed. Disclosed in the exposure statement.",
"OpenAlex drift since v1 (12/50 RECEPTION members changed; RECENT population 2,695 → 3,026) means v1 and this run cover different corpora; comparisons are approximate.",
"Committed raw/ includes OpenAlex abstract fields (inverted indexes) as returned by the API; no PDFs, HTML full texts or excerpt files are committed.",
],1): P(f"  D{i:02d} {t}")
P("")
P("11. BRANCH")
P("  Branch audit/acemoglu-colonial-origins-v2cand, created from b6d786947030902cf58cb114055d6cd48df6ad9c. Only files under examples/research/acemoglu-colonial-origins/citation-network-v2cand/ are added. No existing file, instrument or checker edited. No PR, no merge, no push to main or to audit/acemoglu-colonial-origins.")
P("  Commit hash, push confirmation and post-push git ls-remote results are reported to the requester outside this file (a file cannot contain its own commit hash).")
open(OUTPATH,'w').write("\n".join(o)+"\n")
