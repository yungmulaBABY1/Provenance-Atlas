# Proposed revisions after the citation-network stage (2c)

**Status: PROPOSED, NOT APPLIED.** The earlier audit (02a, 02b), counter-audit (03), final assessment (05) and findings.json are unchanged.

Basis: citation-network/02c_citation_network.md (sha256 884887fe5a7b98d77921fbc31b488c7c9b7dc8406eb60340e4d5881436f3016c); Atlas import urn:atlas:import:ajr2001-citation-network:1.

Validation boundary: The citation-network instrument is validated only on supplied packets (<=26 sources, <=70 edges); this open-retrieval run is outside that boundary. Mechanical checker PASS-WITH-REVIEW is not scientific verification.

| Item | Change | Proposed outcome / note |
|---|---|---|
| IV-1 | ADD_RECEPTION_NOTE | UPHELD-NARROWED (unchanged) |
| IV-2 | NONE | unchanged |
| IV-3 | NONE | unchanged |
| IV-4 | NONE | unchanged |
| IV-5 | NONE | unchanged |
| IV-6 | UPGRADE_VERIFICATION | UNRESOLVED (CONTESTED IN THE LITERATURE); non-anchoring for field 6 |
| IV-7 | NONE | unchanged |
| IV-A | NONE | Field-6 acquittal stands; citation-network Finding 7 (closure acquittal) is consistent with it. |
| CV-1 | ADD_DOWNSTREAM_PROPAGATION; FAILURE_LOCATION_PAPER_TO_MIXED (proposed) | UPHELD-NARROWED (unchanged) |
| CV-2 | NONE | Downstream reuse of the same mortality series inherits its narrowness (citation-network Finding 2). |
| CV-3 | NONE | Intervention-evidence ratchet scored N/A at network level. |
| CV-A | NONE | unchanged |
| OVERALL_VERDICT | NONE | Stage 2c is now run (was NOT_RUN). The verdict and the field-6 acquittal stand. The new scorecard gives 7/24 = 29.2% (band >20%-40%), mechanism: shared-data pseudo-convergence plus self-authored hub qualifier loss; no closure found. |

## Detail

### IV-1

Reception note: the Albouy critique is engaged by the AJR team (2012 Reply) but rarely carried by the citing mass: Albouy 2012 is co-cited by 50 of 2,695 recent AJR citers (1.9%) and appears in 3.0% of 2013+ citers in the OpenAlex union. The critique's survival in the literature is CONTESTED, not resolved.

Evidence: citation-network Finding 5, union_citers_2013plus_albouy.json, recent_cocite_AL.json, NS-E2.

### IV-6

The rival-channel challenge is now read in full text: Glaeser et al. 2004 (GL-E1, GL-E2) report malaria risk and human capital as rival channels for the settler-mortality instrument; Sachs 2003 (SA-E1) frames the null; the Nobel scientific background (NS-E3) states that the channels are very hard to disentangle. AJR 2001 itself reports that controlling for malaria leaves 0.69 (SE 0.25) vs 0.94 (AJR-E4). The challenge is real, engaged, and unresolved; it does not defeat the field-6 estimate as reported.

Evidence: GL-E1, GL-E2, SA-E1, NS-E3, AJR-E4, citation-network Finding 6.

Verification: PROVISIONAL → FULL-TEXT-CONFIRMED; CONTESTED.

### CV-1

Downstream propagation: the AJR team's own Handbook chapter broadens the proxy into 'institutions' and drops the upper-bound qualifier (HB-E1 vs AJR-E2); independent reusers (DML-E1, HW-E1) keep the narrower proxy wording. Failure location: MIXED (PAPER + CITATION), the citation part being self-authored.

Evidence: HB-E1, AJR-E2, DML-E1, HW-E1, citation-network Findings 2-3.

## Not changed

No new evidence defeats map field 6. The field-6 acquittal (IV-A) and the overall verdict stand. IV-2..5, IV-7, CV-2, CV-3 and CV-A are unchanged.
