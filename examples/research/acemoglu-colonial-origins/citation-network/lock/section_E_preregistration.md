# Section E preregistration (instrument steps 31-37) — written BEFORE citation inspection

Written at: see lock hash file. Instrument: prompts/research-analysis/2-citation-network.txt @ ce028e1 (blob 7ac79f0da337c4d52e39e1490088d06c82a9d42b).

Exposure disclosure: the executor read the AJR 2001 full text (including its reference list) in the
earlier stages of this audit (claim extraction, internal/construct validity, counter-audit), and read
Albouy (2012) and the AJR (2012) reply. The OpenAlex citing-work record (who cites AJR 2001, and what
they cite) has NOT been inspected for this stage at lock time. Because the AJR bibliography was seen
earlier, nominated sources are fixed by a reproducible LOCKED QUERY whose output, not executor choice,
determines the source list; the choice of query terms may still reflect that prior exposure.

## Step 31 — claim layers (locked)
- L1 exact source claim (map Field 6): Table 4 col 1, 2SLS 0.94 (SE 0.16), base sample of 64, log settler mortality instrument, PRS 1985-95 expropriation-protection index, 1995 log GDP pc.
- L2 weaker defensible claim (map Field 3): coefficient 0.94 (SE 0.16) on the PRS expropriation index in this sample with this instrument; causal and "institutions" readings conditional.
- L3 downstream citation claim (map Field 4 class): "institutions introduced during colonisation explain differences in countries' prosperity" / "institutions are the fundamental cause of income differences".
- L4 public/policy claim: 2024 Prize press release wording (map Field 4).

## Step 32 — rival explanations (locked)
- R1 (geography/disease, direct channel): settler mortality proxies a disease/geographic environment that affects income today directly, not only through institutions.
- R2 (human capital carried by settlers): settler presence transmitted human capital; the expropriation index partly stands in for that channel.
- Strongest live rival used for the flip test: R1.

## Step 33 — adjudicating observations (locked)
- O1: income/productivity effects of disease burden (especially malaria) measured where institutions are held fixed or are not the varying factor.
- O2: effect of geography on income conditional on institutions measured independently of the IV sample.
- O3: decomposition of colonial-settler effects into human-capital vs institutional channels.
- O4: reliability of 2SLS inference when the first stage is weak or the instrument data are noisy (determines whether L1/L2 can discriminate the explanations at all).

## Steps 34-35 — candidate fields and qualification test (locked)
| ID | Candidate field | Generated from | Measurement relevance | Adjudicative capacity | Independence | Qualifies? |
|---|---|---|---|---|---|---|
| F1 | Economics/epidemiology of malaria and tropical disease | rival R1 | measures disease burden and productivity | could weaken L3 if disease effects are large with institutions fixed | independent of AJR data | yes |
| F2 | Geography and economic development | rival R1 | measures geographic correlates of income | could weaken L3 | independent of AJR data | yes |
| F3 | Human capital and growth empirics | rival R2 | measures schooling/human capital effects on income | could weaken L3 | independent of AJR data | yes |
| F4 | Weak-instrument econometrics | both | determines inferential validity of L1/L2 | could narrow L1/L2 inference | independent | yes |
| F5 | Historical epidemiology of European troop mortality | both | defines instrument construct | could not adjudicate independently: it IS the instrument's data source (Curtin) | NOT independent | no — excluded (data source, not an adjacent check) |
| F6 | Measurement of institutional quality for cross-country tests | audited claim | defines regressor construct | construct-defining only | partly shared data provider (PRS/ICRG) | yes (construct-defining) |

## Step 36 — LOCKED QUERY definition (locked before execution)
- SOURCE-LOCK METHOD: LOCKED QUERY
- Database: OpenAlex works API (api.openalex.org), executed once; raw JSON responses saved and hashed.
- Query per field (filter=title.search:<terms>,to_publication_date:2000-12-31,type:article; sort=cited_by_count:desc; per-page=2):
  - F1: "malaria economic"
  - F2: "geography economic development"
  - F3: "human capital growth"
  - F4: "weak instruments"
  - F6: "institutions economic performance"
- Date cutoff: publication on or before 2000-12-31 (historically available to the source layer; the AER article appeared Dec 2001; NBER WP 7771 is dated June 2000 — cutoff is conservative by six months for the WP and one year for the article).
- Ranking: OpenAlex cited_by_count descending at query time.
- N: top 2 per field, 5 fields => up to 10 sources.
- Deduplication: by OpenAlex work ID; exact duplicates across fields counted once; if an item is not a research article on the field's topic (e.g. an erratum), it is retained and flagged, NOT replaced.
- Downstream layer (L3/L4): engagement checked only through OpenAlex referenced_works of the locked graph corpus (Section A) — no separate downstream adjacent-source query; this layer's downstream nomination is therefore UNASSESSED beyond that.

## Step 37 — flip test (locked)
If the result had favored R1 (direct disease/geography effects dominate), would F1/F2 still be nominated? Yes — they were generated from R1 itself.
If it had favored L3, would F3/F4 still be nominated? Yes — F4 is generated from both; F3 from R2.
Flip test: PASS (field set does not depend on which explanation is favored).
