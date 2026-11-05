# Checker runs — Stage 2c (Baumeister et al. 1998), instrument 2-citation-network v2-candidate.3

Commands (from /workspace/baum/cn, pinned checkers, unedited):
- python3 -I check-citation-network-output.py v2cand3/02c_citation_network_v2cand3.md
- python3 -I check-citation-network-v2-gates.py --require-v2 v2cand3/02c_citation_network_v2cand3.md

| Run | v1 checker | gate checker | What changed before this run |
|---|---|---|---|
| try1 | STRUCTURAL PASS; CONTENT FAIL (18 DIRECT_ADJUDICATION_FORM_FAIL: Section E F2 rows X04–X06, lines 335–337 and 690–692, had "—" for explanation favored / weakened / revision) | FAIL failures=10 (LOCATOR_MISSING X18–X20; I18 ABSENCE declared CORPUS scope; I21 member range "X01–X15" not parsed; SCORED_ON_INSUFFICIENT for adjacent-field neglect and decisive tests as a consequence; Finding 1 and Finding 7 on INSUFFICIENT inferences; BAND_ISSUED_BELOW_GATE as a consequence) | first generation |
| try2 | PASS-WITH-REVIEW items=2 | FAIL failures=1 (I18 DISPOSITION_MISMATCH) | Genuine errors fixed against the instrument: (a) F2 rows now read "not determined: results not read (METADATA only)" (no secondhand content invented); (b) X18–X20 given evidence IDs SC-E1, LS-E1, AP-E1 pointing to Stage 1 sources (build_ledger.py notes; no code changed); (c) I18 rescoped to WITHIN-SAMPLE / SCREENED with 59/59 screened, as instrument line 1406–1410 requires when known-item recall is below 12/12 (instrument lines 594–595); (d) I21 members listed explicitly; (e) Finding 7 basis reduced to I25, attrition facts cited as recorded facts; (f) RECORD QUALITY note added on three same-title records (N09, A48, A50). |
| try3 = final | PASS-WITH-REVIEW items=2 | PASS-WITH-REVIEW items=13 | I18 disposition set to SUPPORTED-WITHIN-SAMPLE (instrument scope vocabulary). |

No ledger row was removed or recoded to clear a checker item. Scores, dispositions and band were unchanged between try1 and final except that the band is now issued after Gate B coverage is 7/10 (70%), conditional on five review items.
