# 05 — Final assessment: Oster (2005), "Hepatitis B and the Case of the Missing Women"

Status: exploratory, single-agent, model-produced.
- The same executor ran every stage, including the pre-registration and the counter-audit.
- No finding below is established until a human reviewer has checked it.
- No composite score is given.

Target: Emily Oster (2005), JPE 113(6):1163–1216, DOI 10.1086/498588. Published version read in full (institutional copy, not committed).
Run date: 2026-11-05 (America/Los_Angeles).

## Chain completeness

| Stage | File | Status |
|---|---|---|
| Pre-registration | 00a_preregistration_LOCKED.txt | LOCKED before Stage 1; hash in 00 |
| 1 Claim extraction | 01_claim_extraction.md | COMPLETE |
| Replication | replication/NOT_ASSESSABLE.txt | NOT ASSESSABLE in this run: the publisher's supplementary dataset is listed but returned HTTP 403; no data reconstructed |
| 2a Internal validity | 02a_internal_validity.md | COMPLETE (INDEPENDENT; no sibling input) |
| 2b Construct validity | 02b_construct_validity.md | COMPLETE (independent of 02a) |
| 2c Citation network (candidate rev. 3) | citation-network-v2cand3/02c_citation_network_v2cand3.md | COMPLETE. v1 checker STRUCTURAL PASS / CONTENT PASS-WITH-REVIEW items=2; gate checker PASS-WITH-REVIEW items=10. RISK BAND WITHHELD |
| 3 Counter-audit | 03_counter_audit.md | COMPLETE. Internal validity SUPPLIED AND CONSUMED; 02b and 02c supplied; Input 5 not supplied (FIDELITY CHECK N/A) |

## Field 6 (claim under audit)

Restated (not a quotation): HBV-elevated sex ratios at birth account for 47.24% (95% CI 13.5–71.5%) of Coale's (1991) 60.26 million missing women in seven Asian/North-African units, mid-1980s (Table 11, Panel A).

## Unblinding the pre-registration

| Expectation (00a) | Observed | Tell | Fired? |
|---|---|---|---|
| E1: field 6 is the share of missing women explained, about 45% overall, about 75% China, ≤20% India, built from SR ≈1.5 × prevalence | Field 6 = 47.24% of Coale's 60.26M (abstract "about 45 percent"); China 76.40%; India, Pakistan and Nepal under 20%; SR_HBV 1.54 × prevalence among pregnant women | T1 | No |
| E2: 2a finds the population-scale causal attribution weakly identified and the calibration step the main threat; "SERIOUS / major, not fatal from the paper alone" | 2a: the calibration input (1.54) is the main threat (IV-1, IV-4: paper-internal, NARROWS). The verdict is INVALID (grade E), but the DEFEATS come from external large-sample tests (IV-2) and the author's correction (IV-3), not from the paper alone | T2 (large representative samples; no serious threat) | No. Note: the expectation was right about the paper-internal evidence, but the overall verdict is stronger than "serious" because of post-publication evidence |
| E3: main construct concerns are the benchmark and carrier-prevalence measurement; mother vs father carrier a key ambiguity | 2b's dominant finding is CV-1, the FORM of the carrier effect: the causal, transferable 1.54 proxy. The benchmark (CV-4, moderate) and prevalence (CV-6, minor) are secondary; mother vs father appears in the level-of-analysis bridge and the confound table | T3 ("a different construct problem dominant") | **Yes (partly).** The dominant construct problem was the carrier-effect proxy, not the benchmark or prevalence; the mother/father ambiguity was found as expected |
| E4: no authors' posted data; NOT_ASSESSABLE most likely | A publisher supplement "31452.dataset.zip" appears to exist (search snippet) but returned HTTP 403. The prevalence study list on the author's page also returned 403. No reproduction | T4 (data found and reproduce field 6) | No. Note: the expectation that no data exist was probably wrong; data appear to exist but were not retrievable |
| E5: density 0; founding 0; recent 0/UNASSESSED; hub UNASSESSED; proxy 0/UNASSESSED; mutation 1/UNASSESSED; adjacent 0; decisive 0; uptake 0; ratchet N/A; non-updating 0/N/A; band low or WITHHELD | Density SCORED 0; founding SCORED 0; recent SCORED 0; hub UNASSESSED; proxy UNASSESSED; mutation SCORED 1; adjacent SCORED 0; decisive SCORED 0; uptake SCORED 0; ratchet N/A; non-updating SCORED 0. Arithmetic band 0–20%; RISK BAND WITHHELD | T5 | No. Every disposition matched. Given the declared exposure, this is not evidence that the instrument is valid; it shows only that the instrument did not contradict a well-known outcome |
| E6: most 2a/2b findings survive; "author conceded" sustains rather than overturns; at least one finding downgraded as hindsight-driven | E0: 1 of 22 rows DEFEATED (CV-3), 2 NARROWED, 5 RECHARACTERIZED, 13 UNAFFECTED, 1 NESTED. The author's concession sustains the verdict (G, J). Hindsight downgrade: CV-1's paper-culpability framing and the 2b §16 "missing decisive test (at the time)" | T6 | No. Caveat: the expectation and the counter-audit were written by the same executor, so the hindsight downgrade may be self-fulfilling. See human adjudication |

## Findings by stage, with counter-audit disposition

| Stage | Finding | Stage result | Counter-audit (E0 / G2) | Net |
|---|---|---|---|---|
| 1 | 5A within-source inflation (abstract scope and caveats; "31 million … explained"; abstract ranges vs table; "new evidence") | PAPER, FULL-TEXT-CONFIRMED | consistent with G2 (no MAP DISAGREEMENT) | upheld |
| 1 | 5B Slate 2005 baseline substitution + hedge removal | PR/MEDIA, RETRIEVED | G2: "the failure is at the PR layer" (CV-8) | upheld (downstream layer) |
| 2a | IV-1 1.54 from six small studies | NARROWS | RECHARACTERIZED: disclosed and inadequately defended (p.1181, p.1198) | upheld, recharacterized |
| 2a | IV-2 Lin & Luoh maternal +0.10–0.25 pp | DEFEATS | UNAFFECTED; reception-checked (top threat #1) | upheld |
| 2a | IV-3 author's successor: no China effect | DEFEATS | UNAFFECTED; reception-checked (top threat #2); nested with IV-2/CV-1/2c F1 as one lever | upheld (one lever) |
| 2a | IV-4 own Taiwan 1.25 set aside | NARROWS | NARROWED: considered and set aside; the share at 1.25 would be at or below the CI floor (not recomputed) | upheld, narrowed |
| 2a | IV-5 "31 million … explained" vs 31.79M remaining | SURVIVES (minor) | UNAFFECTED | upheld (minor) |
| 2a | IV-6 ecological L2 | NARROWS (L2) | RECHARACTERIZED: tested inadequately; nested with CV-5 | upheld for L2 only |
| 2a | IV-7 paternal not maternal (provisional) | PENDING | UNAFFECTED; still PROVISIONAL | unresolved |
| 2a | IV-8 parity pattern (provisional) | PENDING | RECHARACTERIZED; still PROVISIONAL | unresolved |
| 2b | CV-1 FORM contested (CV-2 nested) | DEFEATS | UNAFFECTED for claim validity; the paper-culpability framing is downgraded (hindsight) | upheld for field 6; charge against the 2005 paper narrowed |
| 2b | CV-3 total-effect assumption | NARROWS | **DEFEATED** (p.1165; partial effect p.1203–04) | removed |
| 2b | CV-4 benchmark | NARROWS | NARROWED to the life-expectancy gradient (n.26–27 defend the level) | upheld, narrowed; moot for field 6 |
| 2b | CV-5 ecological | NARROWS (L2) | RECHARACTERIZED; nested with IV-6 | upheld for L2 |
| 2b | CV-6 prevalence inputs | SURVIVES | RECHARACTERIZED: disclosed, list unretrievable | upheld (minor) |
| 2b | CV-7 abstract scope | SURVIVES | UNAFFECTED; G2: aimed at field 2, not field 6 | upheld (minor, other version) |
| 2b | CV-8 Slate (§9) | — | G2: PR/MEDIA layer | upheld (downstream) |
| 2c | F1 decisive tests defeat L1 | DEFEATS | UNAFFECTED, but the wording is restated: R03 (Banyeh 2024; 40 carrier mothers) is small, so there are two large tests, not three | upheld, wording narrowed |
| 2c | F2 no closure; critique taken up (acquittal) | SURVIVES | F: field updated; no suppression | upheld |
| 2c | F3 certainty/mechanism drift | SURVIVES (minor) | MAP GAP; the source is defensible, the failure is at the citation layer | upheld (citation layer) |
| 2c | F4 post-refutation restatement (provisional) | SURVIVES | MAP GAP; PROVISIONAL | unresolved |
| 2c | F5 OpenAlex record quality | SURVIVES | MAP GAP; MODEL/RETRIEVAL layer | upheld (retrieval layer) |
| 2c | F6 small recent reception (provisional acquittal) | SURVIVES | — | provisional |

## What the stages support

- **Field 6 is not supported.** Its only quantitative input, the 1.54 carrier offspring sex ratio, is contradicted by two large individual-level tests in the target region, both reception-checked:
  - Lin & Luoh 2008 (Taiwan, about 3M births): maternal +0.10–0.25 pp on P(male), against about +9.4 pp implied by 1.54.
  - Oster, Chen, Yu & Lin 2008/2010 (China, about 67,000): no maternal or paternal effect; the target's author withdraws the China conclusion.
  - Both were read as working papers (VERSION-SUBSTITUTE).
- **A narrower residual survives.** The ecological association between HBV prevalence and the sex ratio at birth (L2) is contested, but it does no accounting work.
- **Inflation layers:**
  - Within the paper, the abstract drops the CI, the total-effect caveat and the Coale-only denominator, and one body sentence mislabels 31M.
  - At the media layer, Slate 2005 says "established the fate of roughly 50 million of Amartya Sen's missing women".
- **Citation network:** it updated. The critiques are its most-cited nodes and the author accepted the null. A few later citers restate the effect without the refutation (provisional). The candidate instrument WITHHELD the band, with an arithmetic position of 0–20%.
- **Charge against the 2005 paper:** load-bearing reliance on an input the paper itself called "not conclusive". This is not concealment, and its defeat came from later data.

## Needs human adjudication

1. Whether the 2c Finding 1 wording ("three large individual-level tests") should be corrected in a later revision. It was not edited here because the 2c output and checker runs are final. Stage 3 restates it as two large tests plus one small consistent study.
2. Whether the hindsight downgrade of CV-1's culpability framing is right. It was produced by the same executor that pre-registered E6.
3. The 12 checker review items (10 gate, 2 v1), listed verbatim in RUN_REPORT.txt. They are especially relevant for "Lack of decisive tests" SCORED 0, which rests on I13 and includes R03 (small) and POST HOC N45.
4. Retrieval of the JPE supplementary dataset (31452.dataset.zip) by an authorized human session, to reproduce Table 9 (1.54) and Table 11A (47.24%).
5. Reading of the provisional items:
   - the Das Gupta 2005 / Oster 2006 / Das Gupta 2006 PDR exchange (IV-8, I21);
   - Chen, Oster, Yu & Lin 2008 (IV-7);
   - Chahnazarian 1986;
   - A04, A07, A09 and Lin, Chen & Luoh 2012 (I23).
6. Comparison of the published AER (2008) and Economics Letters (2010) versions against the working papers read.
7. The INSTRUMENT PROBLEMS listed in RUN_REPORT.txt.

An audit of a paper whose central claim was already withdrawn by its author mainly tests the chain, not the paper. Results that match the pre-registration should be read as such.
