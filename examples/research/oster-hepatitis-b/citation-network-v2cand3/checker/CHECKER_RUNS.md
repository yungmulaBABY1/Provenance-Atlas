# Checker runs — Stage 2c (Oster 2005), instrument 2-citation-network v2-candidate.3

Commands (from /workspace/oster/cn, pinned checkers):
- python3 -I check-citation-network-output.py out/citation-network-v2cand3/02c_citation_network_v2cand3.md
- python3 -I check-citation-network-v2-gates.py --require-v2 out/citation-network-v2cand3/02c_citation_network_v2cand3.md

| Run | v1 checker | gate checker | What changed before this run |
|---|---|---|---|
| try1 | STRUCTURAL PASS; CONTENT FAIL (18 DIRECT_ADJUDICATION_FORM_FAIL: lines 290–292 and 586–588 lacked explanation favored / weakened / revision) | PASS-WITH-REVIEW items=10 | first generation |
| try2 | PASS-WITH-REVIEW items=2 | PASS-WITH-REVIEW items=10 | Genuine error: the three Section E F2 rows (X01, A06, A03) were classed DIRECTLY-ADJUDICATING with "—" for favored/weakened/revision. Filled from the target's own tabulation of those studies (JP-E2), marked secondhand ("source text not read"). |
| try3 | PASS-WITH-REVIEW items=2 | PASS-WITH-REVIEW items=10 (identical non-INFO output) | Genuine error found on read-through: I23 and three other places named A10 (an R1 one-child-policy paper) as a DIRECT (L1) member; corrected to A09 (the actual DIRECT (L1) member). |
| try4 = final | PASS-WITH-REVIEW items=2 | PASS-WITH-REVIEW items=10 (identical to try3) | Genuine gap against instrument lines 585 and 594: known items not returned by the ADJUDICATION-1 search (N04 K7, N45 K3, N46 K5) and R03 now say "POST HOC adjudication member" in Supported inference. |

No ledger row was removed or recoded to clear a checker item. The 10 gate-checker review items and 2 v1 review items stand and are reported verbatim in RUN_REPORT.txt.
