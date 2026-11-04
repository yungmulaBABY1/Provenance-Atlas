# Stage 2c: citation-network audit of AJR 2001 (run 2026-11-04)

Output: `02c_citation_network.md` (instrument `prompts/research-analysis/2-citation-network.txt`, git blob 7ac79f0d…, unchanged).
The earlier `../02c_citation_network_NOT_RUN.txt` is kept unchanged.

Validation boundary: the instrument is validated only on supplied packets (≤26 sources, ≤70 edges). This is an open-retrieval run (OpenAlex top-50 citers, 136 internal edges), so it falls outside that boundary.
The checker result is mechanical (PASS-WITH-REVIEW), not scientific verification.

| Path | Contents |
|---|---|
| checker/checker_attempts.log | Every checker run, verbatim (attempts 1–3) |
| checker/native_parse.log | atlas.native parse: 0 issues |
| sources/ | Bounded excerpts (10 sources, 20 passages) and their manifest. PDFs are not committed; their hashes are in retrieval/ |
| retrieval/retrieval_log.jsonl | All 163 HTTP retrieval events, including failures |
| retrieval/fulltext_hashes_not_committed.sha256 | SHA-256 of the retrieved PDFs and text layers that are not redistributed |
| lock/ | Section E preregistration and locked query results, with their hashes and lock time |
| metadata/ | Graph, coded inputs, co-citation counts, and the raw OpenAlex/Crossref/S2 JSON |
| scripts/, generator/ | Code and templates that produced the tables and the Atlas context |
| atlas-context.json → atlas-receipt/ | `python -m atlas import` bundle (replay PASS, strict and content) |
| claims-context.json → claims-receipt/ | `python -m atlas.claims build` bundle (replay PASS, content) |
| atlas_*.log | Exact commands, outputs and exit codes |

Proposed changes to the earlier findings are in `../proposed-revisions-after-citation-network.{md,json}`. They are not applied.
