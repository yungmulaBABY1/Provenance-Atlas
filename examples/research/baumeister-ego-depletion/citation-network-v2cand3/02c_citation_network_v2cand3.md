# Citation-Network Audit, v2-candidate.3 run — Baumeister, Bratslavsky, Muraven & Tice (1998), "Ego depletion: Is the active self a limited resource?"

INSTRUMENT PREFLIGHT: yungmulaBABY1/Provenance @ a58d165d9a986edca220f8143fc0c0d9316c8a13 : candidates/research-analysis/2-citation-network.v2-candidate.txt | git blob fcbf4e80cfbaf1558784d052d3b8933b594310c7 | sha256 efc1a9fc336c30a67645ac9257701aa2ebe07dcc0be59f8e28523b0800d53064 | 2001 lines | 89337 bytes | markers: version line "2-citation-network v2-candidate.3", map "cn7-map-3" | IDENTITY CONFIRMED (gate checker blob b75a27e7…, sha256 ce6661a5…; v1 checker blob a3da0827…, sha256 f66650fe…)

INSTRUMENT VERSION: 2-citation-network v2-candidate.3

DIMENSION CLASS MAP: cn7-map-3

Run metadata. LIVE RUN of citation-network candidate revision 3 (not a validation run), Batch 2 of the four-paper brief. Target: JPSP 74(5):1252–1265, doi:10.1037/0022-3514.74.5.1252, OpenAlex W2123817056. Executor: Grok Bot (audit run), branch audit/baumeister-ego-depletion from Provenance-Atlas main 6c651d7593abfb5c4b6d2eb9f6846a5212fe001c. Execution date 2026-11-05 UTC (early morning PST). Clock times are UTC with PST (UTC-8) where useful. Mode: full sequence; upstream claim map ../01_claim_extraction.md (this run). Tools: OpenAlex works API with select= lists omitting abstract_inverted_index (corpora, graph, reference lists); Semantic Scholar citation contexts as EXCERPT access; authorized full texts (Hagger et al. 2016 RRR, Maastricht University repository; Vohs et al. 2021, eScholarship, CC BY; Dang et al. 2021, PMC8186735 author manuscript; Carter et al. 2015, author faculty page; Baumeister & Vohs 2016 comment, psychologicalscience.org; Englert & Bertrams 2021, Frontiers). The target body is not available from an authorized source (publisher HTTP 403); the target is held at ABSTRACT level (PubMed 9599441). Recent window: from 2021-11-05. Abstracts other than the target's own (Stage 1 source) were not read, coded from, or written to any file.

VALIDATION BOUNDARY. This instrument revision is a candidate. It has not been validated for open retrieval. This run used open retrieval over three registered corpora (50 + 25 + 59 works). Every percentage, band and label below is an unvalidated open-retrieval application, not a validated verdict.

EXPOSURE DISCLOSURE. Before this stage the executor had read the target abstract and the Stage 1 secondary sources (author lecture slides, an APA public page, the 2016 RRR, a replicability blog analysis), and the full texts of Vohs et al. 2021, Dang et al. 2021, Carter et al. 2015, Baumeister & Vohs 2016 and Englert & Bertrams 2021 (all retrieved in Stage 1, 11:13–11:16Z). The executor knew from prior reading (declared in 00a) that preregistered multi-site tests report small or null depletion effects and that the founding authors disputed the 2016 RRR. The 00a known-item list was written before the ADJUDICATION-1 search. Stage files 01, 02a and 02b were regenerated at 11:53–11:57Z after a box-restore file loss, i.e. after this stage's corpora had been retrieved (run deviation, recorded in 00 and RUN_REPORT); the claim layers and rivals used here are the ones locked in lock/ADJUDICATION-1_search_record.md at 11:28:23Z. The Section E lock was written before the target reference list was inspected and is mechanical: sources are fixed by a ranked query, not chosen.

PRE-AUDIT CLAIM CONFIRMATION

- Claim under audit (map field 6): In Experiment 1, participants who ate radishes while resisting chocolate persisted about 8.35 min on unsolvable puzzles vs 18.90 (chocolate) and 20.86 (no food); N ≈ 67; t(44) = 6.03 (d ≈ 1.8) radish vs chocolate. (PROVISIONAL in the map: secondhand numbers.)
- What was literally measured (map field 1): between-condition behavioural differences after different first tasks: persistence on unsolvable figure-tracing after radish/chocolate/no food (Exp 1); persistence after a choice (Exp 2); anagram performance after emotion suppression (Exp 3); passive-option choice after letter crossing (Exp 4). The inner resource is not measured; it is inferred.
- Weaker defensible claim (map field 3): in one lab, about 22 per cell, radish-eaters quit unsolvable puzzles sooner; three further small same-direction contrasts; consistent with but not specific to a shared resource.
- Target layer: field 6 (layer L1 below) for the network verdict; layers L1–L4 and rivals R1–R4 are defined below.

The map is upstream-generated, not self-generated.

SECTION A0: CORPUS REGISTER AND SOURCE ELIGIBILITY

Corpus planning. Questions: (a) how the target is received (RECEPTION-1, RECENT-1); (b) what the evidence base testing the layers and rivals contains (ADJUDICATION-1). Proposed inferences were tested in SECTION K0 before use; those that fail stay there as INSUFFICIENT or NOT-ASSESSED.

CLAIM LAYERS AND RIVALS

CLAIM LAYER: L1 — Original depletion effect (map field 6): resisting chocolate and eating radishes causes much faster quitting on unsolvable puzzles (d about 1.8–2.0), replicable in that paradigm.
CLAIM LAYER: L2 — General sequential-task effect: an initial act of self-control reliably reduces subsequent self-control (nonzero, at least small-to-moderate).
CLAIM LAYER: L3 — Mechanism: self-control draws on a limited common resource (later specified as glucose).
CLAIM LAYER: L4 — Interpretive/applied: willpower works like a muscle; decision fatigue and everyday self-control failures follow from depletion.
RIVAL: R1 — Null or inflated effect (small samples, selective publication).
RIVAL: R2 — Motivation/attention shift (process model; opportunity cost); no resource consumed.
RIVAL: R3 — Beliefs/expectancy (lay theories of willpower; demand).
RIVAL: R4 — Task-specific confounds (affect, frustration, hunger, non-blind experimenter delivery).

CORPUS REGISTER

CORPUS ID: RECEPTION-1
CORPUS ROLE: RECEPTION
CORPUS QUESTION: How the most-cited works citing the target relate to it and to each other.
CORPUS SELECTION RULE: OpenAlex works API, /works?filter=cites:W2123817056&sort=cited_by_count:desc&per-page=50, page 1, executed 2026-11-05T11:31:57Z (3:31:57 AM PST); population 5359; no date or type bounds; no screening; one row per work; response raw/reception1_top50.json sha256 dc54ce7c6ef2fb6440b0a4bf9ac0b54acd48cc57b823c8f6c0160cd602916a25.
CORPUS DISCOVERY: SEARCHED — ranked citation query (top 50 by cited_by_count); request, execution time and response hash recorded above
SELECTED ON TARGET CITATION: YES
CORPUS SIZE: 50
CITATION CONTEXT COVERAGE: RECEPTION-1 22/50
RECORD QUALITY: the corpus is dominated by highly cited works from other fields (emotion regulation, conservation of resources, personality economics, ABCD imaging protocol) that cite the target in passing; no duplicate records found; OpenAlex reference lists were present for all 50. A stray file raw/reception_exec_time.txt reads 11:46:38Z; the retrieval log (11:31:57Z) and the response hash govern.
CORPUS LOCK: 2026-11-05T11:31:57Z; response sha256 dc54ce7c6ef2fb6440b0a4bf9ac0b54acd48cc57b823c8f6c0160cd602916a25

CORPUS ID: RECENT-1
CORPUS ROLE: RECEPTION
CORPUS QUESTION: How recent (2021-11-05 onward) citing works use the target.
CORPUS SELECTION RULE: OpenAlex works API, /works?filter=cites:W2123817056,from_publication_date:2021-11-05&sort=cited_by_count:desc&per-page=25, executed 2026-11-05T11:32:05Z; population 1530; the top 25 form the corpus and all 25 were to be inspected (census of the corpus, lock/SAMPLES_draw.txt). Response raw/recent1_top25.json sha256 7101107597f4ebf092df16ef755aca5e216fe786ea4efa52c664a7e38cec6c60.
CORPUS DISCOVERY: SEARCHED — ranked citation query; request, execution time and response hash recorded above
SELECTED ON TARGET CITATION: YES
CORPUS SIZE: 25
CITATION CONTEXT COVERAGE: RECENT-1 12/25
RECORD QUALITY: ranked by cited_by_count, so the corpus over-represents organisational behaviour and consumer-research reviews; R05 (Baumeister et al. 2024 status review) is also an ADJUDICATION-1 member; the remaining 1505 recent citers are outside the corpus.
CORPUS LOCK: 2026-11-05T11:32:05Z; response sha256 7101107597f4ebf092df16ef755aca5e216fe786ea4efa52c664a7e38cec6c60

CORPUS ID: ADJUDICATION-1
CORPUS ROLE: ADJUDICATION
CORPUS QUESTION: What tests of claim layers L1–L4 and rivals R1–R4 exist, whether or not they cite the target, and what they find.
CORPUS SELECTION RULE: OpenAlex works API, seven title_and_abstract.search queries Q1–Q7 (exact strings, date bounds 1998-01-01 to 2026-11-05 and types article|preprint|book-chapter|review in lock/ADJUDICATION-1_search_record.md), relevance ranking, top 10 per query, select= without abstract_inverted_index; one row per work; screening from title and record metadata (and full texts already retrieved from authorized sources) only, abstracts not used; codes DIRECT (L1)/(L2)/(L3)/(L4)/(R1)/(R2)/(R3)/(R4), ADJACENT, BACKGROUND, UNRELATED, UNKNOWN.
CORPUS DISCOVERY: SEARCHED — lock/ADJUDICATION-1_search_record.md (raw/adj1_Q1..Q7.json, executed 2026-11-05T11:28:49Z–11:31:39Z; Q6 and Q7 after HTTP 429 retries)
SELECTED ON TARGET CITATION: NO
CORPUS SIZE: 59
CITATION CONTEXT COVERAGE: ADJUDICATION-1 21/59
RECORD QUALITY: Vohs et al. 2021 returned as the published record and a preprint record (row A03); the Stroop multilab replication as a 2018 record and a 2024 record (row A05); Dang et al. 2021 carries publication year 2020 in OpenAlex; Dang 2017 meta-analysis is listed in 00a as "Dang 2018" (00a governs the label, OpenAlex the year); Q7 returned no decision-fatigue-specific work; three records share the title "The Strength Model of Self-Control" (N09, 2007, Baumeister, Vohs & Tice; A48, 2013, a Chinese-language review; A50, 2021, a chapter); they are distinct works by year, venue and authorship and are kept as separate rows; relevance codes are METADATA-coded from titles.
CORPUS LOCK: 2026-11-05T11:28:23Z (3:28:23 AM PST); search record sha256 d1e398eacd9045935a0a110659281f7c44970e6d9d4e46ff44d1b5fef938d7f7
KNOWN-ITEM RECALL: ADJUDICATION-1 8/12 (returned: K1 Hagger et al. 2010 [N16], K2 Carter & McCullough 2014 [A09], K4 Hagger et al. 2016 RRR [N45], K5 Vohs et al. 2021 [A03], K6 Dang et al. 2021 [A01], K7 Dang meta-analysis [A08], K9 Job, Dweck & Walton 2010 [A32], K10 Inzlicht & Schmeichel 2012 [N47]; not returned: K3 Carter et al. 2015, K8 Gailliot et al. 2007, K11 Baumeister & Vohs 2016, K12 Kurzban 2010). K3 and K11 enter only as POST HOC rows X16 and X17; K8 is RECEPTION-1 member N41 and enters adjudication only as POST HOC; K12 was not retrieved.

Overlap. N09, N16, N33, N45 and N47 are in RECEPTION-1 and ADJUDICATION-1, and R05 is in RECENT-1 and ADJUDICATION-1; each is recorded once with both corpus IDs. Reception rank does not weight the adjudication role. Duplicate records of one work are merged into one row with every identifier listed (A03, A05). Rows T01 and X01–X20 are OUTSIDE every registered corpus (the target, Section E locked sources and named POST HOC sources); they carry no corpus count.

SOURCE ELIGIBILITY LEDGER

| Source | Corpus membership | Question relevance | Relation to target | Evidence contribution | Source access | Citation context | Supported inference |
|---|---|---|---|---|---|---|---|
| N01 W2096423181 The Emerging Field of Emotion Regulation: An Integra… (1998) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; integrative review of emotion regulation; citation present in OpenAlex refs, use not inspected |
| N02 W2048385562 The Influence of Culture, Community, and the Nested‐… (2001) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; conservation-of-resources theory, culture and the nested self; citation present in OpenAlex refs, use not inspected |
| N03 W2066785847 Working memory: looking back and looking forward (2003) | RECEPTION-1 | BACKGROUND | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E1: self-control rests on a system "limited in capacity and subject to fatigue-like decline" (working-memory review) |
| N04 W2128126978 Emotion regulation: Affective, cognitive, and social… (2002) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; emotion regulation consequences review; citation present in OpenAlex refs, use not inspected |
| N05 W1997397294 Social and Psychological Resources and Adaptation (2002) | RECEPTION-1 | BACKGROUND | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E2: willpower as a resource; "this cognitive capacity is diminished with use" |
| N06 W2113390049 Self-regulation and depletion of limited resources:… (2000) | RECEPTION-1 | ADJACENT (L3) | SUPPORTS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E3: founding-cluster review: food-temptation test run "to help rule out moods as a potential explanation" |
| N07 W1968689002 TARGET ARTICLE: Hope Theory: Rainbows in the Mind (2002) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; hope theory target article; citation present in OpenAlex refs, use not inspected |
| N08 W2130142026 The unbearable automaticity of being. (1999) | RECEPTION-1 | ADJACENT | PREMISE | THEORY | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E4: "Given the severe limitations of conscious selfregulation capacity" (Baumeister et al., 1998) as premise for automaticity |
| N09 W2108897328 The Strength Model of Self-Control (2007) | RECEPTION-1+ADJUDICATION-1 | ADJACENT (L3) | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; founding-cluster strength-model review (Baumeister, Vohs & Tice 2007); also ADJUDICATION-1 (Q7); citation present in OpenAlex refs, use not inspected |
| N10 W2022472850 Emotional regulation in the workplace: A new way to… (2000) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; emotional regulation in the workplace; S2 found no context; citation present in OpenAlex refs, use not inspected |
| N11 W2093761921 Development and Validation of the Short Grit Scale (… (2009) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | METHOD | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Short Grit Scale validation; citation present in OpenAlex refs, use not inspected |
| N12 W2161497363 Getting to the “COR” (2014) | RECEPTION-1 | BACKGROUND | PREMISE | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E5: "self-regulation in and of itself is a drain on resources" (COR theory review) |
| N13 W1818536883 Implementation Intentions and Goal Achievement: A Me… (2006) | RECEPTION-1 | ADJACENT | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E6: restates Experiment 1: radish eaters "persisted for less time on a subsequent unsolvable puzzles task" (faithful to Stage 1 field 6) |
| N14 W2912633426 How to SHIFT Consumer Behaviors to be More Sustainab… (2019) | RECEPTION-1 | BACKGROUND | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E7: people find it hard to "forgo benefits in the present" (sustainability review) |
| N15 W2089594500 Cues to deception. (2003) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; cues to deception meta-analysis; citation present in OpenAlex refs, use not inspected |
| N16 W2060763381 Ego depletion and the strength model of self-control… (2010) | RECEPTION-1+ADJUDICATION-1 | DIRECT (L2) | SUPPORTS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E8: Baumeister and coworkers "provided initial support for the ego-depletion effect"; meta-analysis built on the dual-task paradigm "outlined by Baumeister et al. (1998)"; K1; also ADJUDICATION-1 (Q2) |
| N17 W2519766541 The Intention–Behavior Gap (2016) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; intention-behaviour gap review; citation present in OpenAlex refs, use not inspected |
| N18 W2789530810 The Adolescent Brain Cognitive Development (ABCD) st… (2018) | RECEPTION-1 | BACKGROUND | MENTIONS | METHOD | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E9: a demanding task "has been associated with diminished performance on subsequent tasks" (ABCD imaging protocol) |
| N19 W2134469114 Self-control as a limited resource: Regulatory deple… (1998) | RECEPTION-1 | ADJACENT (L2) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; founding-cluster companion paper (Muraven, Tice & Baumeister 1998); cited by the target and citing it (reciprocal pair); S2 found no context |
| N20 W2058490785 Dealing with feeling: A meta-analysis of the effecti… (2012) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; emotion-regulation strategies meta-analysis; citation present in OpenAlex refs, use not inspected |
| N21 W2158359335 Executive functions and self-regulation (2012) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; executive functions and self-regulation review; citation present in OpenAlex refs, use not inspected |
| N22 W2105538889 Enriching or Depleting? The Dynamics of Engagement i… (2001) | RECEPTION-1 | BACKGROUND | PREMISE | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E10: suppressing emotion "may use up resources that might otherwise be used for coping" |
| N23 W2171838050 The automated will: Nonconscious activation and purs… (2001) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | NOT-INSPECTED | S2 context retrieved but the returned passage does not show the citation; use not inspected |
| N24 W2123821623 Recovery, work engagement, and proactive behavior: A… (2003) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; recovery and work engagement; citation present in OpenAlex refs, use not inspected |
| N25 W2045934080 Emotional intelligence: An integrative meta-analysis… (2010) | RECEPTION-1 | BACKGROUND | PREMISE | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E11: "Emotion regulation demands can drain resources from task performance" |
| N26 W2077057247 Taking Stock of Self-Control (2011) | RECEPTION-1 | ADJACENT | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E12: "evidence confirms" capacity for self-control is susceptible to previous attempts (founding-author co-written meta-analysis) |
| N27 W1976788357 Self‐Regulation and the Problem of Human Autonomy: D… (2006) | RECEPTION-1 | ADJACENT (R2) | QUALIFIES | THEORY | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E13: new experiments found "true choice was not depleting" contra the target's high-choice condition |
| N28 W2100482303 Yielding to Temptation: Self‐Control Failure, Impuls… (2002) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; founding-author consumer self-control essay; citation present in OpenAlex refs, use not inspected |
| N29 W2030988365 Psychology as the Science of Self-Reports and Finger… (2007) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | COMMENTARY | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | NOT-INSPECTED | S2 context retrieved but the returned passage is a reference-list fragment; use not inspected |
| N30 W2560821290 The Economics and Psychology of Personality Traits (2008) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; economics and psychology of personality traits; citation present in OpenAlex refs, use not inspected |
| N31 W1977835193 Impulse and Self-Control From a Dual-Systems Perspec… (2009) | RECEPTION-1 | ADJACENT | SUPPORTS | THEORY | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E14: Baumeister and colleagues "have established the importance of selfregulatory resource[s]" |
| N32 W2097442078 Benefits of mindfulness at work: The role of mindful… (2012) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; mindfulness at work; S2 found no context; citation present in OpenAlex refs, use not inspected |
| N33 W2125068113 Self‐Regulation, Ego Depletion, and Motivation (2007) | RECEPTION-1+ADJUDICATION-1 | ADJACENT (L3) | SUPPORTS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E15: founding-cluster review: regulating the self "appears to depend on a limited resource"; also ADJUDICATION-1 (Q4) |
| N34 W4241540074 Emotion regulation and memory: The cognitive costs o… (2000) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; emotion regulation and memory; S2 found no context; citation present in OpenAlex refs, use not inspected |
| N35 W1997682147 Resource loss, resource gain, and emotional outcomes… (2003) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; resource loss among inner-city women; citation present in OpenAlex refs, use not inspected |
| N36 W1996918954 Social exclusion impairs self-regulation. (2005) | RECEPTION-1 | ADJACENT | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E16: founding-cluster study: the target "replicated a study on ego depletion using solvable rather than unsolvable anagrams" |
| N37 W2164682760 An opportunity cost model of subjective effort and t… (2013) | RECEPTION-1 | ADJACENT (R2) | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; opportunity-cost model of subjective effort (Kurzban et al. 2013); citation present in OpenAlex refs, use not inspected |
| N38 W2112868206 Emotional distress regulation takes precedence over… (2001) | RECEPTION-1 | ADJACENT | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; founding-cluster study of emotional distress and impulse control; citation present in OpenAlex refs, use not inspected |
| N39 W3122622199 Personality Psychology and Economics (2011) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; personality psychology and economics handbook chapter; citation present in OpenAlex refs, use not inspected |
| N40 W2105985103 On the costs and benefits of emotional labor: A meta… (2011) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | NOT-INSPECTED | S2 context retrieved but the returned passages do not show the citation; use not inspected |
| N41 W2146569853 Self-control relies on glucose as a limited energy s… (2007) | RECEPTION-1 | DIRECT (L3) | SUPPORTS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E17: founding-cluster glucose study: the depleted resource "has been a puzzle since the earliest findings"; POST HOC adjudication member (known item K8, not returned by the ADJUDICATION-1 search) |
| N42 W2122634808 Interdependence, Interaction, and Relationships (2002) | RECEPTION-1 | BACKGROUND | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E18: listed for constrained cognitive capacity (passage truncated at the citation) |
| N43 W1871370349 Work–Family Conflict and Flexible Work Arrangements:… (2012) | RECEPTION-1 | BACKGROUND | PREMISE | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E19: "These acts of volition draw upon ego resources" |
| N44 W2081900501 The effects of choice on intrinsic motivation and re… (2008) | RECEPTION-1 | ADJACENT | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E20: "making choices is one form of self-regulation that can result in ego-depletion" |
| N45 W2499154041 A Multilab Preregistered Replication of the Ego-Depl… (2016) | RECEPTION-1+ADJUDICATION-1 | DIRECT (L2) | CHALLENGES | INDEPENDENT-DATA | FULL-TEXT (Hagger et al. 2016, Maastricht University CRIS repository PDF, HTTP 200; not committed) | INSPECTED | RRR-E1 p. 548: Study 1 "required participants to taste radishes and resist cookies"; RRR-E2 p. 554: pooled d = 0.04 across 23 labs; K4; also ADJUDICATION-1 (Q1) |
| N46 W2144397230 A justification-suppression model of the expression… (2003) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; justification-suppression model of prejudice; citation present in OpenAlex refs, use not inspected |
| N47 W2000141755 What Is Ego Depletion? Toward a Mechanistic Revision… (2012) | RECEPTION-1+ADJUDICATION-1 | ADJACENT (R2) | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; process-model revision of the resource model (Inzlicht & Schmeichel 2012); K10; also ADJUDICATION-1 (Q4); citation present in OpenAlex refs, use not inspected |
| N48 W2600886565 Toward a Rational and Mechanistic Account of Mental… (2017) | RECEPTION-1 | ADJACENT (R2) | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; rational account of mental effort; citation present in OpenAlex refs, use not inspected |
| N49 W2153950939 Spent Resources: Self‐Regulatory Resource Availabili… (2007) | RECEPTION-1 | ADJACENT (L4) | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E21: depletion listed across "overeating, procrastination, intellectual un-derachievement" |
| N50 W1853636458 Measurement Matters (2015) | RECEPTION-1 | BACKGROUND | CITES-UNINSPECTED | METHOD | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; measurement of personal qualities; citation present in OpenAlex refs, use not inspected |
| R01 W4385606438 The Impact of Social Media on the Mental Health of A… (2023) | RECENT-1 | BACKGROUND | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E22: attributes "displaced behavior theory" to Baumeister; self-control "a limited resource that can be drained over time" |
| R02 W4214866453 AI increases unethical consumer behavior due to redu… (2022) | RECENT-1 | BACKGROUND | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E23: time spent choosing used "as a proxy of service engagement" (Baumeister et al., 1998) |
| R03 W4291001390 A neuro-metabolic account of why daylong cognitive w… (2022) | RECENT-1 | ADJACENT (L3) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; neuro-metabolic account of daylong cognitive work; citation present in OpenAlex refs, use not inspected |
| R04 W3217148206 Psychological and biological resilience modulates th… (2021) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; resilience and stress effects; citation present in OpenAlex refs, use not inspected |
| R05 W4402300076 Self-control and limited willpower: Current status o… (2024) | RECENT-1+ADJUDICATION-1 | ADJACENT (L2) | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; founding-author status review (Baumeister et al. 2024); full text not retrieved; also ADJUDICATION-1 (Q3) |
| R06 W4283313664 The Determinants of Impulsive Buying Behavior in Ele… (2022) | RECENT-1 | BACKGROUND | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E24: "Some scholars have proposed a 'strength' or 'limited resource' model" |
| R07 W4291535426 Abusive supervision: a systematic literature review (2022) | RECENT-1 | BACKGROUND | PREMISE | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E25: victims "exhaust their limited resources" and experience ego-depletion |
| R08 W4323652556 Workflow interruption and nurses’ mental workload in… (2023) | RECENT-1 | BACKGROUND | PREMISE | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E26: difficult tasks leave "insufficient personal resources … under the limited strength model" |
| R09 W4310804025 Self-regulation and goal-directed behavior: A system… (2022) | RECENT-1 | ADJACENT | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; systematic review of self-regulation and goal-directed behaviour; citation present in OpenAlex refs, use not inspected |
| R10 W4220818821 Restoration of Attention by Rest in a Multitasking W… (2022) | RECENT-1 | ADJACENT (R2) | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; restoration of attention by rest; citation present in OpenAlex refs, use not inspected |
| R11 W4402676278 AI in the spotlight: The impact of artificial intell… (2024) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; AI in the workplace; citation present in OpenAlex refs, use not inspected |
| R12 W4409103534 Origins and consequences of cognitive fatigue (2025) | RECENT-1 | ADJACENT (L3) | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; origins and consequences of cognitive fatigue; citation present in OpenAlex refs, use not inspected |
| R13 W4281731168 Does Techno-invasion Lead to Employees’ Deviant Beha… (2022) | RECENT-1 | BACKGROUND | PREMISE | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E27: "All acts of self-regulation are empowered by a limited, metaphorical strength" |
| R14 W4390011768 Inclusive leadership, employee performance and well-… (2023) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; inclusive leadership review; citation present in OpenAlex refs, use not inspected |
| R15 W4311667985 Metacognition and self-control: An integrative frame… (2022) | RECENT-1 | ADJACENT (R3) | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; metacognition and self-control framework; S2 found no context; citation present in OpenAlex refs, use not inspected |
| R16 W4311640673 When Are We More Ethical? A Review and Categorizatio… (2022) | RECENT-1 | BACKGROUND | QUALIFIES | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E28: review chose "to exclude ego-depletion studies" unless strong evidence was given |
| R17 W3211993193 The Intention-Behavior gap in Ethical Consumption: M… (2021) | RECENT-1 | BACKGROUND | PREMISE | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E29: "striving to achieve one goal can compromise the pursuit of subsequent goals" |
| R18 W4205581247 The relationship between self-control and procrastin… (2022) | RECENT-1 | BACKGROUND | PREMISE | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E30: "theoretical foundation … built on a strength model of self-control known as ego depletion theory" |
| R19 W4321368994 Interindividual Variability in Mental Fatigue-Relate… (2023) | RECENT-1 | ADJACENT | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E31: ego depletion listed as one name for mental fatigue |
| R20 W4200151748 Toward a Theory of Emotions in Competitive Sports (2021) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; emotions in competitive sports; citation present in OpenAlex refs, use not inspected |
| R21 W4308964018 The association between academic stress, social supp… (2022) | RECENT-1 | BACKGROUND | PREMISE | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E32: effortful behaviour can "use a significant amount of their own regulatory resources" |
| R22 W4302307858 Supervisor incivility and turnover intention of the… (2022) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; supervisor incivility and turnover; citation present in OpenAlex refs, use not inspected |
| R23 W4285800368 Why People Do What They Do: An Interdisciplinary Syn… (2022) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; interdisciplinary synthesis of motivation; S2 found no context; citation present in OpenAlex refs, use not inspected |
| R24 W4280566821 Physical Activity and Academic Procrastination among… (2022) | RECENT-1 | BACKGROUND | CITES-UNINSPECTED | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | NOT-INSPECTED | S2 context retrieved but the returned passages carry bracket numbers that cannot be tied to the target; use not inspected |
| R25 W4366496226 Event-Oriented Organizational Behavior Research: A M… (2023) | RECENT-1 | BACKGROUND | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E33: resource gains and losses as mediators (Baumeister et al., 1998 in a list) |
| A01 W3014898655 A Multilab Replication of the Ego Depletion Effect (2020) | ADJUDICATION-1 | DIRECT (L2) | QUALIFIES | INDEPENDENT-DATA | FULL-TEXT (VERSION-SUBSTITUTE: PMC8186735 author manuscript HTML, pmc.ncbi.nlm.nih.gov; SPPS version not retrieved; not committed) | INSPECTED | DA-E1 Introduction: the target "reported the ego depletion effect for the first time" and is "cited over 5,000 times"; DA-E2 Results, Table 3: error-rate d = 0.10, 95% CI [0.01, 0.19] (12 labs); K6 |
| A02 W2580798662 Extending a Multilab Preregistered Replication of th… (2017) | ADJUDICATION-1 | DIRECT (R1) | NOT-CITING | REANALYSIS | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q1; extends the RRR to a research program; OpenAlex refs (14) omit the target |
| A03 W3119325546 + W4256555852 (preprint record) A Multisite Preregistered Paradigmatic Test of the E… (2021) | ADJUDICATION-1 | DIRECT (L2) | CHALLENGES | INDEPENDENT-DATA | FULL-TEXT (Vohs et al. 2021, eScholarship UC repository PDF, CC BY; not committed) | INSPECTED | VO-E1 p. 1568: "The seminal article" (the target) "has had 'transformational' impact"; VO-E2 p. 1574: d = 0.06, 95% CI [−0.02, 0.14]; VO-E3 p. 1577: depletion "not as reliable or robust as previously assumed"; founding-cluster first author (Vohs); merged with preprint record W4256555852 (Q1); K5 |
| A04 W2476382243 Introduction to a Registered Replication Report on E… (2016) | ADJUDICATION-1 | DIRECT (L2) | NOT-CITING | COMMENTARY | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q1; editorial introduction to the RRR; OpenAlex refs (7) omit the target |
| A05 W2780490182 + W7160480298 (2024 record) Multilab replication: Ego depletion with Stroop as t… (2017) | ADJUDICATION-1 | DIRECT (L2) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q1; multilab Stroop replication; one work under two records (W2780490182 2017 registration, W7160480298 2024 report); no OpenAlex refs; result not read |
| A06 W3157428216 Again, No Evidence for or Against the Existence of E… (2021) | ADJUDICATION-1 | DIRECT (L2) | MENTIONS | COMMENTARY | FULL-TEXT (Frontiers in Human Neuroscience HTML, publisher OA; not committed) | INSPECTED | EN-E1 (Method summary): the e-crossing task "(… Baumeister et al., 1998) served as the initial task" in the 2021 multisite test; opinion title states "no evidence for or against" |
| A07 W2896535558 Ego Depletion Replication (2016) | ADJUDICATION-1 | DIRECT (L2) | UNKNOWN | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q1; replication dataset record; no OpenAlex refs |
| A08 W2604293295 An updated meta-analysis of the ego depletion effect (2017) | ADJUDICATION-1 | DIRECT (L2) | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E34: "over 300 independent studies have replicated this effect … since it was first reported"; K7 |
| A09 W2007393966 Publication bias and the limited strength model of s… (2014) | ADJUDICATION-1 | DIRECT (R1) | CITES-UNINSPECTED | REANALYSIS | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q2; publication-bias reanalysis of the strength model (Carter & McCullough 2014); K2 |
| A10 W2984573913 The effect of ego depletion or mental fatigue on sub… (2019) | ADJUDICATION-1 | ADJACENT (L2) | NOT-CITING | REVIEW | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q2; meta-analysis of depletion and physical endurance; OpenAlex refs (104) omit the target |
| A11 W2794580436 Is Ego Depletion Real? An Analysis of Arguments (2018) | ADJUDICATION-1 | DIRECT (R1) | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q2; "Is Ego Depletion Real?" analysis of arguments (Friese et al. 2019) |
| A12 W2612478318 The influence of ego depletion on sporting performan… (2017) | ADJUDICATION-1 | ADJACENT (L2) | UNKNOWN | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q2; sport-performance meta-analysis; no OpenAlex refs |
| A13 W2588069705 The Debate on the Ego-Depletion Effect: Evidence fro… (2017) | ADJUDICATION-1 | DIRECT (R1) | QUALIFIES | REANALYSIS | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E35: "Such convergence does not show up for the so-called ego-depletion effect" |
| A14 W4411356972 How does ego depletion reduce sports performance in… (2025) | ADJUDICATION-1 | ADJACENT (L2) | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q2; athletes meta-analysis (2025) |
| A15 W1989768409 Is ego depletion too incredible? Evidence for the ov… (2013) | ADJUDICATION-1 | DIRECT (R1) | MENTIONS | REANALYSIS | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E36: defines "the so-called depletion effect" (Baumeister et al. 1998) in a commentary on overestimation |
| A16 W1964342261 Sweet delusion. Glucose drinks fail to counteract eg… (2014) | ADJUDICATION-1 | DIRECT (L3) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; glucose drinks "fail to counteract" depletion (title) |
| A17 W2779009122 Glucose hypothesis of ego-depletion (2016) | ADJUDICATION-1 | DIRECT (L3) | UNKNOWN | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; encyclopedia-type entry on the glucose hypothesis; no OpenAlex refs |
| A18 W2152858830 The Role of Glucose in Self-Control (2011) | ADJUDICATION-1 | DIRECT (L3) | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E37: "resisting the temptation to eat chocolate (Baumeister et al., 1998, Study 1)" listed among depletion tasks |
| A19 W2003102314 Unsuccessful attempts to replicate effects of self c… (2014) | ADJUDICATION-1 | DIRECT (L3) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; unsuccessful replications of self-control and glucose effects (title) |
| A20 W1546584494 The Nature of Self-Regulatory Fatigue and “Ego Deple… (2015) | ADJUDICATION-1 | ADJACENT (L3) | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; nature of self-regulatory fatigue review |
| A21 W2058765236 If ego depletion cannot be studied using identical t… (2014) | ADJUDICATION-1 | ADJACENT (R4) | CITES-UNINSPECTED | COMMENTARY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; identical-tasks critique (Lange 2014) |
| A22 W1966401421 The Physiology of Willpower: Linking Blood Glucose t… (2007) | ADJUDICATION-1 | ADJACENT (L3) | SUPPORTS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E38: founding-author review: "resisting the temptation to eat cookies caused participants subsequently to give up faster" |
| A23 W2130284887 Sweetened blood sweetens behavior. Ego depletion, gl… (2014) | ADJUDICATION-1 | ADJACENT (L3) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q3; glucose, guilt and prosocial behaviour |
| A24 W2533887486 Motivational Tuning in Response to Ego Depletion (2016) | ADJUDICATION-1 | ADJACENT (R2) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q4; motivational tuning after depletion; OpenAlex refs (83) omit the target |
| A25 W2058867658 Ego Depletion and the Humean Theory of Motivation (2014) | ADJUDICATION-1 | BACKGROUND | NOT-CITING | THEORY | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q4; philosophy of motivation; OpenAlex refs (11) omit the target |
| A26 W2796459004 Can Ego-Depletion Be Helpful? Testing the Process Mo… (2018) | ADJUDICATION-1 | DIRECT (R2) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; test of a process-model implication |
| A27 W2538010233 Too Depleted to Try? Testing the Process Model of Eg… (2016) | ADJUDICATION-1 | DIRECT (R2) | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E39: "The e-crossing task was used to manipulate ego depletion (Baumeister et al., 1998 …)" |
| A28 W212211297 The Importance of Restraint in Gauging the Effects o… (2015) | ADJUDICATION-1 | ADJACENT (R2) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; restraint and alcohol motivation |
| A29 W2513456674 Moderators of the Ego Depletion Effect (2016) | ADJUDICATION-1 | ADJACENT (R2) | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q4; moderators of the depletion effect |
| A30 W2893842868 Lay theories of willpower (2018) | ADJUDICATION-1 | ADJACENT (R3) | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q5; lay theories of willpower review |
| A31 W2522685630 Implicit Theories About Willpower (2016) | ADJUDICATION-1 | ADJACENT (R3) | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q5; implicit theories about willpower chapter |
| A32 W2118108696 Ego Depletion—Is It All in Your Head? (2010) | ADJUDICATION-1 | DIRECT (R3) | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E40: task "adopted from previous research to manipulate ego depletion (Baumeister et al., 1998 …)"; K9 |
| A33 W1792116546 Implicit Theories About Willpower Predict Subjective… (2015) | ADJUDICATION-1 | ADJACENT (R3) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q5; willpower theories and well-being; OpenAlex refs (55) omit the target |
| A34 W1976771764 Implicit theories about willpower predict self-regul… (2015) | ADJUDICATION-1 | ADJACENT (R3) | PREMISE | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E41: strength model "posits that selfcontrol relies on a limited energy resource" |
| A35 W2905871268 Can faith move mountains? How implicit theories abou… (2018) | ADJUDICATION-1 | ADJACENT (R3) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q5; willpower theories as moderator at work |
| A36 W2270668874 Implicit theories about willpower predict the activa… (2015) | ADJUDICATION-1 | ADJACENT (R3) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q5; willpower theories and rest goals; OpenAlex refs (50) omit the target |
| A37 W2739641472 Implicit Theories About Willpower in Resisting Tempt… (2017) | ADJUDICATION-1 | DIRECT (R3) | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E42: "We adapted a study design involving resistance to tempting food as the depletion manipulation" |
| A38 W2900405707 Who Believes in Nonlimited Willpower? In Search of C… (2018) | ADJUDICATION-1 | ADJACENT (R3) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q5; correlates of willpower theories |
| A39 W2922399599 Too exhausted to go to bed: Implicit theories about… (2019) | ADJUDICATION-1 | ADJACENT (R3) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q5; willpower theories and bedtime procrastination |
| A40 W2144295133 Ego Depletion Is Not Just Fatigue (2010) | ADJUDICATION-1 | DIRECT (R4) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q6; "Ego Depletion Is Not Just Fatigue" (Vohs et al. 2011; founding-cluster member) |
| A41 W2035672781 Too fatigued to care: Ego depletion, guilt, and pros… (2012) | ADJUDICATION-1 | ADJACENT (R4) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q6; fatigue, guilt and prosocial behaviour |
| A42 W2110882073 Natural resistance: Exposure to nature and self-regu… (2014) | ADJUDICATION-1 | ADJACENT (R4) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q6; nature exposure after depletion; OpenAlex refs (57) omit the target |
| A43 W1988113868 Choice and Ego-Depletion: The Moderating Role of Aut… (2006) | ADJUDICATION-1 | ADJACENT (R2) | QUALIFIES | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E43: "According to the Baumeister et al. (1998) model … making choices would necessarily result in ego-depletion" (tests the autonomy moderator) |
| A44 W3159013860 Reconceptualizing Ego Depletion as Transient Cogniti… (2021) | ADJUDICATION-1 | DIRECT (R4) | CITES-UNINSPECTED | THEORY | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q6; depletion reconceptualised as transient cognitive fatigue |
| A45 W1992322615 Ostracism and Ego Depletion: The Strains of Silence (2001) | ADJUDICATION-1 | ADJACENT | MENTIONS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E44: founding-author co-written study: the target "proposed the term 'ego depletion'" |
| A46 W2986926076 The Limits of Ego Depletion (2019) | ADJUDICATION-1 | ADJACENT (R1) | CITES-UNINSPECTED | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q6; "The Limits of Ego Depletion" |
| A47 W2150495553 Conserving self-control strength. (2006) | ADJUDICATION-1 | ADJACENT (L3) | SUPPORTS | INDEPENDENT-DATA | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E45: founding-author study: "Consistent with Baumeister et al. (1998), the incorrect/missing solutions did not occur at random" |
| A48 W2313439080 The Strength Model of Self-Control (2013) | ADJUDICATION-1 | BACKGROUND | CITES-UNINSPECTED | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q7; strength-model review (Chinese journal) |
| A49 W2301647011 The Strength Model of Self-Control in Sport and Exer… (2016) | ADJUDICATION-1 | ADJACENT (L4) | MENTIONS | REVIEW | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E46: effects "not caused by … mood differences (e.g., Baumeister et al., 1998 …)" (sport review) |
| A50 W3170796682 The Strength Model of Self-Control (2021) | ADJUDICATION-1 | BACKGROUND | UNKNOWN | REVIEW | METADATA (OpenAlex record) | NOT-INSPECTED | title-coded from METADATA; Q7; strength-model chapter; no OpenAlex refs |
| A51 W1608074949 Integrating attentional control theory and the stren… (2015) | ADJUDICATION-1 | ADJACENT (L4) | PREMISE | THEORY | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E47: "Like a muscle, one's self-control strength can become exhausted and depleted" |
| A52 W2170958357 Neuroenhancement and the strength model of self-cont… (2015) | ADJUDICATION-1 | ADJACENT (L4) | PREMISE | THEORY | EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed) | INSPECTED | CTX-E48: "We identified the strength model of selfcontrol (Baumeister et al., 1998) as a promising candidate theory" |
| A53 W2182110160 Sleep Deprivation, Low Self-Control, and Delinquency… (2013) | ADJUDICATION-1 | ADJACENT (L4) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Q7; sleep deprivation and delinquency test of the strength model; OpenAlex refs (64) omit the target |
| T01 W2123817056 Ego depletion: Is the active self a limited resource? (1998) — target | OUTSIDE | DIRECT (L1) | NOT-CITING | INDEPENDENT-DATA | ABSTRACT (PubMed 9599441; publisher full text HTTP 403, not retrieved) | NOT-APPLICABLE | target source; not returned by ADJUDICATION-1; TA-E1 (abstract): results "suggest that the self's capacity for active volition is limited"; body text not read |
| X01 W2084221958 On Leaping to Conclusions When Feeling Tired: Mental Fatigue… (1996) | OUTSIDE | ADJACENT (R4) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F1; predates target; mental fatigue and judgement; not in the target's OpenAlex reference list |
| X02 W2319902335 Blocking: A New Principle of Mental Fatigue (1931) | OUTSIDE | ADJACENT (R4) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F1; predates target; blocking as a principle of mental fatigue (1931); not in the target's OpenAlex reference list |
| X03 W4253912427 The Mental Health of Patients With a Chief Complaint of Chro… (1988) | OUTSIDE | BACKGROUND | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F1; predates target; fatigue in chronic-fatigue patients; off-topic hit retained; not in the target's OpenAlex reference list |
| X04 W2029487046 Learned helplessness in humans: Critique and reformulation. (1978) | OUTSIDE | ADJACENT (R3) | NOT-CITING | THEORY | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F2; predates target; learned helplessness reformulation; not in the target's OpenAlex reference list |
| X05 W2022987442 Learned helplessness: Theory and evidence. (1976) | OUTSIDE | ADJACENT (R3) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F2; predates target; learned helplessness, depression and persistence; not in the target's OpenAlex reference list |
| X06 W2139986071 The role of expectations and attributions in the alleviation… (1975) | OUTSIDE | ADJACENT (R3) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F2; predates target; learned helplessness in humans; not in the target's OpenAlex reference list |
| X07 W2119926219 The relationship between breast feeding persistence, sexuali… (1988) | OUTSIDE | UNRELATED | NOT-CITING | NONE | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F3; predates target; off-topic hit (breastfeeding) retained, not replaced; not in the target's OpenAlex reference list |
| X08 W1537717563 Mood, Persistence, and success (1987) | OUTSIDE | ADJACENT (R4) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F3; predates target; mood and persistence; not in the target's OpenAlex reference list |
| X09 W2012786194 The effects of children's goal structures and performance fe… (1991) | OUTSIDE | ADJACENT (R4) | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F3; predates target; mood, goal structures and persistence in children; not in the target's OpenAlex reference list |
| X10 W1981707533 Magnitude of teacher expectancy effects on pupil IQ as a fun… (1984) | OUTSIDE | ADJACENT (R4) | NOT-CITING | REVIEW | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F4; predates target; teacher expectancy effects; not in the target's OpenAlex reference list |
| X11 W2068172336 Experimenter expectancy and the reassuring nature of the nul… (1968) | OUTSIDE | ADJACENT (R4) | NOT-CITING | METHOD | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F4; predates target; experimenter expectancy; not in the target's OpenAlex reference list |
| X12 W2059803871 Alcohol and the balanced-placebo design: The role of experim… (1986) | OUTSIDE | ADJACENT (R4) | NOT-CITING | METHOD | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F4; predates target; balanced-placebo design (expectancy control); not in the target's OpenAlex reference list |
| X13 W2074791822 Television is "easy" and print is "tough": The differential… (1984) | OUTSIDE | BACKGROUND | NOT-CITING | INDEPENDENT-DATA | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F5; predates target; invested mental effort, TV vs print; not in the target's OpenAlex reference list |
| X14 W2098813016 The Efficiency of Instructional Conditions: An Approach to C… (1993) | OUTSIDE | BACKGROUND | NOT-CITING | METHOD | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F5; predates target; mental-effort efficiency measure; not in the target's OpenAlex reference list |
| X15 W2129275476 Vegetative response during imagined movement is proportional… (1991) | OUTSIDE | UNRELATED | NOT-CITING | NONE | METADATA (OpenAlex record) | NOT-APPLICABLE | title-coded from METADATA; Section E locked source F5; predates target; vegetative response to imagined movement; off-topic hit; not in the target's OpenAlex reference list |
| X16 Carter, Kofler, Forster & McCullough 2015, A Series of Meta-Analytic Tests of the Depletion Effect (JEP:General) | OUTSIDE | DIRECT (R1) | CHALLENGES | REANALYSIS | FULL-TEXT (author copy, pages.ucsd.edu faculty page PDF; not committed) | INSPECTED | CA-E1 p. 1: "(the depletion effect; Baumeister et al., 1998)"; CA-E2 p. 16: PET and PEESE estimates "indistinguishable from zero"; K3; POST HOC (not returned by ADJUDICATION-1) |
| X17 Baumeister & Vohs 2016, comment on the RRR (APS-hosted manuscript) | OUTSIDE | DIRECT (L2) | NOT-CITING | COMMENTARY | FULL-TEXT (psychologicalscience.org PDF; not committed) | NOT-APPLICABLE | text read: no citation of the 1998 article found; BV-E1 p. 2: the RRR "did not test ego depletion" (manipulation failure); founding authors; K11; POST HOC |
| X18 Schimmack 2016, replicability analysis of ego depletion (Replicability-Index blog) | OUTSIDE | DIRECT (R1) | CHALLENGES | REANALYSIS | FULL-TEXT (replicationindex.com HTML; not committed) | INSPECTED | SC-E1 (Study 1 analysis section; Stage 1 source S2): computes Experiment 1 effect sizes from reported statistics (d = 1.80 / 2.04); POST HOC |
| X19 Baumeister 2012, LSE public lecture slides "Willpower" | OUTSIDE | ADJACENT (L4) | SUPPORTS | COMMENTARY | FULL-TEXT (lse.ac.uk PDF; not committed) | INSPECTED | LS-E1 (slide headings; Stage 1 D1/D1b): slides "Willpower is limited", "Like a Muscle"; founding author; POST HOC |
| X20 APA public page "Is Willpower a Limited Resource?" | OUTSIDE | ADJACENT (L4) | SUPPORTS | COMMENTARY | FULL-TEXT (apa.org PDF; not committed) | INSPECTED | AP-E1 (Stage 1 D2/D2b): describes the study as having "drained the subjects' self-control"; POST HOC |

Coding notes. CTX-E ids resolve to Semantic Scholar citation contexts (requests /graph/v1/paper/DOI:10.1037/0022-3514.74.5.1252/citations?fields=title,year,externalIds,contexts,intents&limit=1000 at offsets 0–5000, 2026-11-05T11:46:57Z–11:47:33Z, HTTP 200; response sha256 offset 0 fa01fc13afde2ebebd3b45e3adb9a7521fbfbb17e35340a854d277b49b31d192, 1000 506bd23a…b869, 2000 aee93a2e…757e, 3000 bbd0daa7…a7ff, 4000 3e809623…2e15, 5000 735212ae…9929; three earlier offset-0 attempts at 11:45:37–11:46:10Z were logged without an HTTP status (rate-limited retries); responses not committed). Relation for ADJUDICATION-1 non-reception members: OpenAlex reference list contains W2123817056 → CITES-UNINSPECTED; reference list empty or sparse → UNKNOWN; non-empty list without the target → NOT-CITING (NOT-APPLICABLE). Relevance and contribution for METADATA rows are coded from the title only (abstracts were not used under the rights rules). TA-E1 resolves to the target abstract (PubMed 9599441). RRR-E, VO-E, DA-E, CA-E, BV-E and EN-E ids resolve to the pages or sections given in each row. SC-E1, LS-E1 and AP-E1 resolve to Stage 1 sources S2, D1/D1b and D2/D2b as located in ../01_claim_extraction.md.

SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION

GRAPH CORPUS AND RECEIPTS

GRAPH CORPUS DEFINITION: RECEPTION-1 as registered in SECTION A0 (OpenAlex, filter=cites:W2123817056, sort=cited_by_count:desc, top 50 records, executed 2026-11-05T11:31:57Z, no date or type bounds, no screening). Nodes are works, n = 50. The target is outside the density corpus; citer -> target edges hold by construction and are not counted.
GRAPH CORPUS NODE LIST: N01=W2096423181; N02=W2048385562; N03=W2066785847; N04=W2128126978; N05=W1997397294; N06=W2113390049; N07=W1968689002; N08=W2130142026; N09=W2108897328; N10=W2022472850; N11=W2093761921; N12=W2161497363; N13=W1818536883; N14=W2912633426; N15=W2089594500; N16=W2060763381; N17=W2519766541; N18=W2789530810; N19=W2134469114; N20=W2058490785; N21=W2158359335; N22=W2105538889; N23=W2171838050; N24=W2123821623; N25=W2045934080; N26=W2077057247; N27=W1976788357; N28=W2100482303; N29=W2030988365; N30=W2560821290; N31=W1977835193; N32=W2097442078; N33=W2125068113; N34=W4241540074; N35=W1997682147; N36=W1996918954; N37=W2164682760; N38=W2112868206; N39=W3122622199; N40=W2105985103; N41=W2146569853; N42=W2122634808; N43=W1871370349; N44=W2081900501; N45=W2499154041; N46=W2144397230; N47=W2000141755; N48=W2600886565; N49=W2153950939; N50=W1853636458
INTERNAL EDGE LIST: N02 -> N08; N03 -> N06; N04 -> N01; N04 -> N34; N05 -> N08; N06 -> N19; N08 -> N19; N09 -> N19; N09 -> N41; N09 -> N49; N10 -> N01; N11 -> N19; N12 -> N02; N12 -> N05; N13 -> N06; N13 -> N23; N14 -> N06; N14 -> N28; N15 -> N19; N16 -> N06; N16 -> N09; N16 -> N19; N16 -> N31; N16 -> N33; N16 -> N38; N16 -> N41; N16 -> N49; N17 -> N06; N17 -> N13; N17 -> N41; N20 -> N01; N20 -> N09; N20 -> N19; N20 -> N23; N20 -> N34; N21 -> N01; N21 -> N16; N21 -> N31; N21 -> N41; N23 -> N08; N23 -> N19; N24 -> N22; N25 -> N01; N25 -> N06; N25 -> N10; N25 -> N19; N25 -> N28; N26 -> N06; N26 -> N13; N26 -> N19; N26 -> N31; N26 -> N49; N28 -> N19; N28 -> N38; N30 -> N41; N31 -> N01; N31 -> N23; N31 -> N41; N32 -> N01; N32 -> N10; N32 -> N40; N33 -> N06; N33 -> N41; N34 -> N01; N34 -> N19; N36 -> N06; N36 -> N19; N36 -> N38; N37 -> N06; N37 -> N09; N37 -> N16; N37 -> N19; N37 -> N21; N37 -> N31; N37 -> N33; N37 -> N41; N37 -> N47; N38 -> N06; N38 -> N19; N39 -> N30; N40 -> N01; N40 -> N10; N40 -> N19; N40 -> N34; N41 -> N06; N41 -> N19; N43 -> N06; N43 -> N33; N44 -> N06; N44 -> N19; N45 -> N09; N45 -> N16; N45 -> N19; N45 -> N26; N45 -> N47; N46 -> N19; N47 -> N06; N47 -> N16; N47 -> N19; N47 -> N21; N47 -> N31; N47 -> N33; N47 -> N41; N47 -> N49; N48 -> N16; N48 -> N19; N48 -> N37; N48 -> N41; N48 -> N45; N48 -> N47; N50 -> N16; N50 -> N26; N50 -> N30
DERIVATION MODE: COMPUTED-FROM-RETRIEVED
DENSITY CALCULATION: directed density = directed internal edges u -> v (u, v work nodes, u != v, v in OpenAlex referenced_works of u) / n(n-1), n = 50; computed by scripts/build_2c.py from raw/reception1_top50.json (cross-check raw/graph_edges.json).
DENSITY NUMERATOR: 113 directed internal edges among the 50 work nodes.
DENSITY DENOMINATOR: 2450 possible directed edges (50 × 49).
DENSITY INPUT COVERAGE: 50/50 record reference lists obtained from OpenAlex (8,132 indexed references across the 50 works). No Crossref cross-check.
DENSITY INFERENCE SCOPE: the density result applies only to RECEPTION-1. Because RECEPTION-1 is selected on target citation, it can establish density inside that target-citing corpus; it cannot establish or exclude field-wide, founding-cluster or premise-subnetwork closure. No seed-expanded or matched comparison graph was built.

Closure is not established and not excluded beyond the defined corpus.

Density results. Work-level directed density 113/2450 = 4.61%. 40/50 works cite at least one other member. Reciprocal pairs: 0. In-degree leaders: N19 22, N06 15, N41 10, N01 9, N16 6, N31 5, N49 4, N09 4. Founding-cluster works (any of the four target authors on the byline: N06, N09, N19, N26, N28, N29, N33, N36, N38, N41; 10/50) receive 62/113 internal edges, 46 of them from works outside the founding cluster.

1. Top 50 most-cited works citing the target: RECEPTION-1 (Artifact 1 lists the top 15). Relevance composition: ADJACENT=20; BACKGROUND=27; DIRECT=3.
2. Founding cluster: the four target authors (Baumeister, Bratslavsky, Muraven, Tice) and works they co-author. In RECEPTION-1: N06, N09, N19, N26, N28, N29, N33, N36, N38, N41. The founding authors also co-author ADJUDICATION-1 members A03 (Vohs et al. 2021, Muraven on the byline), A22, A45, A47 and R05.
3. Founding papers' evidence type: the target reports four small single-lab experiments (map field 1; ABSTRACT-level, TA-E1); founding-cluster follow-ups in RECEPTION-1 are primary studies (N19, N36, N41) and reviews (N06, N09, N26, N33).
4. Hubs: N19 Muraven, Tice & Baumeister 1998 (in-degree 22) and N06 Muraven & Baumeister 2000 review (15) lead; both are founding-cluster works. N41 Gailliot et al. 2007 (10, founding cluster) and N01 Gross 1998 (9, emotion regulation) follow.
5. Hub substitution: within RECEPTION-1, 22/50 works cite N19 and 15/50 cite N06 alongside the target (co-citation, not use).
6. Small cluster citing itself: founding-cluster works cite each other (16 internal edges among them); the corpus overall is sparse (density 4.61%).
7. Gatekeeping roles: no editorial or referee data retrieved; UNASSESSED.
8. Self-citation in the founding cluster: present (founding-cluster members of RECEPTION-1 cite the target by construction); its rate relative to field norms was not measured.
9. Concentration by lab/journal/funder: authorship only (SECTION I).
10. Citation count vs independent confirmation: target cited_by_count 5374 at retrieval; DA-E1 reports "cited over 5,000 times". The preregistered multi-site tests of L2 with new data report d = 0.04 (RRR-E2), 0.06 (VO-E2) and 0.10 (DA-E2) (I13, I14); no direct test of L1 was found in ADJUDICATION-1 (I18).

SECTION B: EVIDENCE TYPE CODING

Every corpus member is coded in the SOURCE ELIGIBILITY LEDGER. Questions 11–16 describe the evidence base only on ADJUDICATION-1, the SEARCHED adjudication corpus; on RECEPTION-1 they describe the citing set.

ADJUDICATION-1 composition (evidence base, bounded by the locked search; METADATA-coded):
COMPOSITION: I15 | relevance | ADJACENT=32; BACKGROUND=3; DIRECT=24 | TOTAL=59
COMPOSITION: I16 | contribution | COMMENTARY=3; INDEPENDENT-DATA=28; REANALYSIS=4; REVIEW=19; THEORY=5 | TOTAL=59
RECEPTION-1 composition (citing set only):
COMPOSITION: I17 | relevance | ADJACENT=20; BACKGROUND=27; DIRECT=3 | TOTAL=50

11. Primary empirical tests in ADJUDICATION-1: DIRECT codes DIRECT (L2) 9; DIRECT (L3) 4; DIRECT (R1) 5; DIRECT (R2) 2; DIRECT (R3) 2; DIRECT (R4) 2. DIRECT (L1): 0 — no member tests the food-temptation → persistence paradigm itself (I18). The RRR chose another first task, citing "extensive experimenter involvement" in the original (RRR-E1, p. 548).
12. Reviews/syntheses: REVIEW and COMMENTARY members are counted in I16; of the bias-corrected syntheses only Carter et al. 2015 (X16, POST HOC) was read in full.
13. Theory-only: THEORY members are counted in I16 (for example A44, A51, A52).
14. Unknown: relevance or relation UNKNOWN where OpenAlex reference lists are empty (A05, A07, A12, A17, A50).
15. Evidence-to-claim ratio: field 6 rests on one single-lab experiment of about 67 participants; the large later tests of L2 (23-lab RRR, multi-site Vohs et al. 2021, 12-lab Dang et al. 2021) use new data under preregistered protocols (I14).
16. On RECEPTION-1 the same questions describe citers: ADJACENT=20; BACKGROUND=27; DIRECT=3 (of 50).

SECTION C: CITATION POLARITY AND CLAIM USE

Citing passages inspected: CITATION CONTEXT COVERAGE: RECEPTION-1 22/50 (N03, N05, N06, N08, N12, N13, N14, N16, N18, N22, N25, N26, N27, N31, N33, N36, N41, N42, N43, N44, N45, N49); CITATION CONTEXT COVERAGE: RECENT-1 12/25 (R01, R02, R06, R07, R08, R13, R16, R17, R18, R19, R21, R25); CITATION CONTEXT COVERAGE: ADJUDICATION-1 21/59. Most passages are EXCERPT (Semantic Scholar contexts). The prespecified random sample of 12 lost 8 members (I05). Percentages use inspected passages only.

17. Supportive: SUPPORTS 5/22 in RECEPTION-1 (N06, N16, N31, N33, N41).
18. Critical: CHALLENGES 1/22 (N45 RRR); QUALIFIES 1/22 (N27: true choice "was not depleting", CTX-E13).
19. Perfunctory/background: MENTIONS 10/22. RECENT-1: PREMISE 6/12, MENTIONS 5/12, QUALIFIES 1/12 (R16 excludes ego-depletion studies, CTX-E28).
20. Premise use: RECEPTION-1 N08, N12, N22, N25, N43 and RECENT-1 R07, R08, R13, R17, R18, R21 use the limited-resource model as a premise for their own argument (for example CTX-E4, CTX-E25, CTX-E27, CTX-E30).
21. Data/instrument reuse: the target's e-crossing manipulation is reused as a depletion task (A27 CTX-E39, A32 CTX-E40, A06 EN-E1); R02 reuses choice time as a proxy (CTX-E23).
22. Polarity inflation: several passages state a drained resource as what the target showed (CTX-E2, CTX-E5, CTX-E19, CTX-E22, CTX-E27), while the target abstract states the resource as an inference (TA-E1, "suggest"). A08 states that "over 300 independent studies have replicated this effect" (CTX-E34). Graded under proxy mismatch (I10, I11); the restatement comparison against the target text is INSUFFICIENT (I12).

SECTION D: CLAIM MUTATION TRACKING

23–30. Original: the target is held at ABSTRACT level only (TA-E1); its body, where field 6's numbers sit, was not read (publisher HTTP 403; no authorized copy). The RESTATEMENT class needs FULL-TEXT or EXCERPT access to both texts, so no mutation is graded. Candidate restatements recorded for review: hedge loss from "suggest" (TA-E1) to "Willpower is limited" (X19, founding-author slides) and "drained the subjects' self-control" (X20); A08 "over 300 independent studies have replicated" (CTX-E34); R01 attributes "displaced behavior theory" to Baumeister (CTX-E22); N13 restates Experiment 1 faithfully (CTX-E6). Claim mutation is UNASSESSED (I12 INSUFFICIENT).

| Original source | Original claim | Hub restatement | Downstream restatement | Mutation severity | Note |
|---|---|---|---|---|---|
| Target abstract (TA-E1) | results "suggest" a limited capacity for volition | N33: "appears to depend on a limited resource" (CTX-E15) | X19 slides "Willpower is limited"; X20 "drained the subjects' self-control" | not graded | target body not read; RESTATEMENT minimum unmet |
| Target Experiment 1 (field 6, PROVISIONAL) | radish eaters quit sooner, one lab | none found | N13 faithful (CTX-E6); A22 faithful (CTX-E38) | not graded | as above |
| Target and follow-ups | depletion effect first reported | none found | A08 "over 300 independent studies have replicated this effect" (CTX-E34) | not graded | compare RRR-E2, VO-E2, CA-E2 |
| Target | ego depletion / limited resource | none found | R01 "displaced behavior theory" attributed to Baumeister (CTX-E22) | not graded | possible misattribution |

SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT

Steps 31–37. Layers L1–L4 and rivals R1–R4 are locked in lock/ADJUDICATION-1_search_record.md; fields F1–F5 and observations O1–O5 in lock/section_E_preregistration.md, hashed before the Section E queries ran. The lock was written before the target reference list was inspected; the executor's prior knowledge is declared in 00a. Sources are fixed mechanically by a ranked query.

SOURCE-LOCK METHOD: LOCKED QUERY
SOURCE-LOCK DATABASE: OpenAlex works API (select omits abstract_inverted_index)
SOURCE-LOCK QUERY OR SOURCE LIST: filter=title.search:<terms>,to_publication_date:1998-04-30,type:article, sort=cited_by_count:desc, per-page=3; terms F1 "mental fatigue", F2 "learned helplessness", F3 "mood persistence", F4 "experimenter expectancy", F5 "mental effort"
SOURCE-LOCK DATE CUTOFF: 1998-04-30 (before the JPSP May 1998 issue)
SOURCE-LOCK RANKING RULE: OpenAlex cited_by_count descending at query time
SOURCE-LOCK N: 15 (top 3 per field × 5 fields)
SOURCE-LOCK DEDUPLICATION RULE: by OpenAlex work ID; off-topic items retained and flagged, never replaced
SOURCE-LOCK TIMESTAMP OR HASH: 2026-11-05T11:28:40Z (3:28:40 AM PST); preregistration sha256 791e03ac0bbe7ff3abe4e806ce0d17b57c1bc3e55d7816afe5d5c86ea6bed737; queries executed after the lock (F1–F5 11:45:13Z–11:46:48Z; F2 retrieved twice, the retained response sha256 a0bba566a2f0a91c2500… is the one on disk)

Flip test (step 37): PASS. F1 is generated from rival R2; F3 and F4 from R4; F2 from both L1 and R4; F5 from L3 (the audited claim). Innocent explanations: F3 exemplars include an off-topic breast-feeding paper (X07); F5 exemplars include an off-topic motor-imagery paper (X15).

Engagement check. The target body is not accessible, so engagement is checked against the target's OpenAlex reference list (58 IDs; 57 resolved, raw/target_reflist_titles.json, retrieved 12:05:02Z after the lock, METADATA). It contains 0/15 locked sources. It does list adjacent works outside the lock: stress aftereffects (Glass & Singer 1969; Cohen 1980), persistence (Feather 1961; McFarlin 1985), mood (Mayer & Gaschke 1988), self-reported effort (Johnson & Saccuzzo 1995), thought suppression, reactance and dissonance works. It lists no learned-helplessness (F2) or experimenter-expectancy (F4) work.

Falsification-relevant literature preregistration table:

| Claim layer | Audited explanation | Strongest plausible rival explanation | Adjudicating observation | Candidate field | Generated from audited claim, rival, or both? | Measurement relevance | Adjudicative capacity | Independence | Publication-date cutoff | Historically available? | Flip-test result | Source-lock method | Lock timestamp / hash | Final engagement classification |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1/L3 | a limited resource is spent | R2 motivation/attention shift | O1 incentives remove post-effort decrements | F1 mental fatigue | rival | outcome-task performance after effort | could narrow L3 | independent | 1998-04-30 | yes | PASS | LOCKED QUERY | 791e03ac…d737 | no locked source cited; related stress-aftereffect works cited (reference list only; text UNASSESSED) |
| L1 | depletion shortens persistence | R4 aversive/uncontrollable experience shortens persistence | O2 persistence on unsolvable tasks after uncontrollable failure | F2 learned helplessness | both | the same outcome (unsolvable-task persistence) | could defeat L1's specificity | independent | 1998-04-30 | yes | PASS | LOCKED QUERY | as above | not cited; no learned-helplessness work in the reference list; text engagement UNASSESSED |
| L1 | resource, not affect | R4 affect | O3 induced mood changes persistence | F3 mood and persistence | rival | same outcome | could narrow L1 | independent | 1998-04-30 | yes | PASS | LOCKED QUERY | as above | no locked source cited; Mayer & Gaschke 1988 mood work cited (reference list only) |
| L1 | manipulation drives behaviour | R4 non-blind experimenter delivery | O4 non-blind experimenters shift timed outcomes | F4 experimenter expectancy | rival | experimenter-delivered manipulation | could narrow L1 | independent | 1998-04-30 | yes | PASS | LOCKED QUERY | as above | not cited; no expectancy work in the reference list; text engagement UNASSESSED |
| L3 | one limited general capacity | capacity is task-specific | O5 a general capacity depleted by effort | F5 mental effort | audited claim | construct definition | could narrow L3 | independent | 1998-04-30 | yes | PASS | LOCKED QUERY | as above | no locked source cited; self-reported effort work cited (reference list only) |

Adjacent-literature neglect table:

| Claim layer | Adjacent field | Nominated source and stable identifier | Verification state | Source class: CONSTRUCT-DEFINING / MECHANISM-SUPPORTING / DIRECTLY-ADJUDICATING | Actual result | Explanation favored | Explanation weakened | Precise revision required | Pre-inspection lock status or POST HOC | Cited by dominant cluster? | Engagement quality | Effect of omission |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1/L3 | F1 mental fatigue | X01 W2084221958 On Leaping to Conclusions When Feeling Tired: Mental Fatigue | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L1/L3 | F1 mental fatigue | X02 W2319902335 Blocking: A New Principle of Mental Fatigue (1931) | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L1/L3 | F1 mental fatigue | X03 W4253912427 The Mental Health of Patients With a Chief Complaint of Chro | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L1 | F2 learned helplessness | X04 W2029487046 Learned helplessness in humans: Critique and reformulation.  | LOCATED | DIRECTLY-ADJUDICATING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L1 | F2 learned helplessness | X05 W2022987442 Learned helplessness: Theory and evidence. (1976) | LOCATED | DIRECTLY-ADJUDICATING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L1 | F2 learned helplessness | X06 W2139986071 The role of expectations and attributions in the alleviation | LOCATED | DIRECTLY-ADJUDICATING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L1 | F3 mood and persistence | X07 W2119926219 The relationship between breast feeding persistence, sexuali | LOCATED | MECHANISM-SUPPORTING | off-topic (title) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | none (off-topic exemplar) |
| L1 | F3 mood and persistence | X08 W1537717563 Mood, Persistence, and success (1987) | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L1 | F3 mood and persistence | X09 W2012786194 The effects of children's goal structures and performance fe | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L1 | F4 experimenter expectancy | X10 W1981707533 Magnitude of teacher expectancy effects on pupil IQ as a fun | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L1 | F4 experimenter expectancy | X11 W2068172336 Experimenter expectancy and the reassuring nature of the nul | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L1 | F4 experimenter expectancy | X12 W2059803871 Alcohol and the balanced-placebo design: The role of experim | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L3 | F5 mental effort | X13 W2074791822 Television is "easy" and print is "tough": The differential… | LOCATED | CONSTRUCT-DEFINING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L3 | F5 mental effort | X14 W2098813016 The Efficiency of Instructional Conditions: An Approach to C | LOCATED | CONSTRUCT-DEFINING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L3 | F5 mental effort | X15 W2129275476 Vegetative response during imagined movement is proportional | LOCATED | CONSTRUCT-DEFINING | off-topic (title) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | none (off-topic exemplar) |
| L2 | R1 test | N45 W2499154041 Hagger et al. 2016 RRR | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | pooled d = 0.04 across 23 labs (RRR-E2) | R1 | L2 | L2 effect near zero for the RRR paradigm | LOCKED (ADJUDICATION-1 search) | founding authors replied (X17) | disputed by founding authors (BV-E1) | not omitted |
| L2 | R1 test | A03 W3119325546 Vohs et al. 2021 | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | d = 0.06, 95% CI [−0.02, 0.14] (VO-E2) | R1 | L2 | depletion "not as reliable or robust as previously assumed" (VO-E3) | LOCKED (ADJUDICATION-1 search) | founding-cluster co-authored (Muraven) | the update itself | not omitted |
| L2 | R1 test | X16 Carter et al. 2015 | FULL-TEXT-CONFIRMED | DIRECTLY-ADJUDICATING | PET and PEESE estimates indistinguishable from zero (CA-E2) | R1 | L2 | bias-corrected effect not distinguishable from zero | POST HOC (known item K3, not returned by the locked search) | not determined | — | not omitted |

At the reference-list level the target engages stress-aftereffect, persistence and mood work but no learned-helplessness or experimenter-expectancy source, although F2 shares the outcome (persistence on unsolvable tasks) and F4 addresses the experimenter involvement the RRR cites (RRR-E1). Whether the text addresses these rivals is UNASSESSED (I22). GRAPH-STRUCTURE I21 carries the score; the multi-site R1 tests post-date the target and are scored under decisive tests and critique uptake.

SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING

40. Hubs inside RECEPTION-1: N19 Muraven, Tice & Baumeister 1998 (in-degree 22), N06 Muraven & Baumeister 2000 review (15), N41 Gailliot et al. 2007 glucose study (10), N01 Gross 1998 emotion-regulation review (9), N16 Hagger et al. 2010 meta-analysis (6). Review-type founding-cluster works: N06, N09, N26, N33.
41. Recent papers citing the hubs (RECENT-1, 25): N09 7/25, N06 6/25, N16 5/25, N19 3/25.
42. Recent papers citing primary evidence directly: 25/25 cite the target by construction.
43. Hub substitution for inspection: not measurable from reference lists; no passage citing a hub in place of the target was inspected (I26 NOT-ASSESSED).
44–45. Hub accuracy: N06 states the food-temptation test was run "to help rule out moods" (CTX-E3); N33 hedges ("appears to depend", CTX-E15); N16 says the target "provided initial support" (CTX-E8). These are founding-cluster or synthesis restatements; RESTATEMENT comparison against the target body is not possible (ABSTRACT only).
46. Adjacent literatures in hubs: N01 is emotion regulation; N16 is a meta-analysis later reanalysed for publication bias (A09, X16).
47. Hub as substitute for primary evidence: UNASSESSED (I26).

| Hub paper | Recent papers citing hub | Recent papers citing primary evidence directly | Adjacent-field citation rate | Hub accuracy | Hub risk |
|---|---|---|---|---|---|
| Muraven, Tice & Baumeister 1998 (N19) | 3/25 RECENT-1 | 25/25 by construction | 22/50 RECEPTION-1 co-cite | not inspected | founding-cluster hub; UNASSESSED |
| Muraven & Baumeister 2000 (N06) | 6/25 RECENT-1 | 25/25 by construction | 15/50 RECEPTION-1 co-cite | mood rule-out claim (CTX-E3); not graded | founding-cluster hub; UNASSESSED |
| Baumeister, Vohs & Tice 2007 (N09) | 7/25 RECENT-1 | 25/25 by construction | — | not inspected | UNASSESSED |
| Hagger et al. 2010 (N16) | 5/25 RECENT-1 | 25/25 by construction | — | "provided initial support" (CTX-E8); bias-corrected reanalyses disagree (CA-E2) | UNASSESSED |

SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR

48. Proxy treated as construct: persistence and performance differences stand in for a depleted inner resource; several later passages state the resource as what was shown (CTX-E19, CTX-E22, CTX-E27), where the target abstract says the results "suggest" it (TA-E1). Graded under proxy mismatch (I10, I11).
49. Export from low-stakes settings: laboratory persistence in about 67 students is exported to workplace, consumer and health settings (R07, R13, R17, R18, N43; L4); applied claims are a paper-level and Stage 2b issue.
50. Ignored natural experiments: not assessed.
51. Model updating: mixed. A 2021 multi-site test co-authored by Muraven concludes depletion is "not as reliable or robust as previously assumed" (VO-E3); the founding authors' 2016 comment says the RRR "did not test ego depletion" (BV-E1); the 2024 status review (R05) was not read.
52. Intervention expansion: no intervention claim at field 6; N/A.
53–55. Falsification criteria: not stated in the target abstract; 55 N/A.
56. Expansion over testing: L4 applications grew while the L1 paradigm was not re-tested at scale (I18; Section E; recent premise use I09).

Ratchet scoring route. Intervention-evidence ratchet: N/A (no intervention claim). Model non-updating four-link gate: link 1 (model stated: a limited resource, TA-E1) met; link 2 (verified later disconfirming evidence) met for L2, RRR-E2, VO-E2, DA-E2, CA-E2 (I13, I14); link 3 (reception opportunity) met, founding authors replied to the RRR (X17) and Muraven co-authored A03; link 4 (non-updating) NOT DETERMINABLE: the founding cluster both disputes (BV-E1, 2016) and co-signs a downgrade (VO-E3, 2021), and its latest position (R05, 2024) was not read (I24 NOT-ASSESSED). Model non-updating UNASSESSED.

SECTION H: IGNORED CRITIQUE AND NON-UPTAKE

1. Precondition: critique production strongly expected (highly cited JPSP paradigm paper; large effect from small cells; later replication debate).
2. Retrieval: RRR (N45, FULL-TEXT); Vohs et al. 2021 (A03, FULL-TEXT); Dang et al. 2021 (A01, FULL-TEXT version substitute); Carter et al. 2015 (X16, FULL-TEXT, POST HOC); Baumeister & Vohs 2016 comment (X17, FULL-TEXT, POST HOC); Inzlicht & Schmeichel 2012 and Kurzban et al. 2013 (N47, N37, METADATA).
3. Reception opportunity: verified; the founding authors replied to the RRR (X17) and Muraven co-authored A03.
4. Uptake in the uptake population: founding authors dispute the RRR manipulation (BV-E1; ENGAGEMENT I19) and a founding author co-signs the 2021 downgrade (VO-E3; I20). Co-citation carries no score: 1/3 RECEPTION-1 works published 2017 or later cite a listed critique (I23, descriptive); in RECENT-1, 8/25 cite a listed critique or null test and 13/25 cite a founding-cluster work beyond the target. Six inspected recent passages use the limited-resource model as a premise (R07, R08, R13, R17, R18, R21; I09); one recent review excludes ego-depletion studies (R16, CTX-E28).

57. Serious critiques: RRR 2016 (N45); Carter & McCullough 2014 and Carter et al. 2015 (A09, X16); Vohs et al. 2021 (A03); Dang et al. 2021 (A01); process-model and opportunity-cost revisions (N47, N37; R2); lay theories of willpower (A32; R3).
58. Cited by the dominant cluster: founding authors cite and dispute the RRR (X17); R05 (2024) not read.
59. Mode: disputed (2016), then partially accepted (2021 co-authored multi-site test).
60. Network update: partial; RRR and process-model works are inside RECEPTION-1, while recent citers still use the model as a premise (I09).
61. Recent papers: R16 qualifies (excludes depletion studies); R07, R08, R13, R17, R18, R21 use the model as a premise.
62–63. Practitioner warnings: not searched; UNASSESSED.

| Expected-production precondition | Critique / contrary evidence | Year | Source type | Main objection | Verification state | Reception opportunity | Cited by dominant cluster? | Uptake status | Dimension disposition | Effect on consensus |
|---|---|---|---|---|---|---|---|---|---|---|
| strong | Hagger et al. RRR (N45, W2499154041) | 2016 | preregistered multi-lab test | pooled d = 0.04 across 23 labs (RRR-E2) | FULL-TEXT-CONFIRMED | verified | yes; founding authors replied (X17) | disputed: "did not test ego depletion" (BV-E1) | SCORED 1 (I19, under review) | effect contested |
| strong | Vohs et al. (A03, W3119325546) | 2021 | preregistered multi-site test | d = 0.06, 95% CI [−0.02, 0.14] (VO-E2) | FULL-TEXT-CONFIRMED | verified | co-authored by Muraven | accepted: "not as reliable or robust as previously assumed" (VO-E3) | counts against concern (I20) | downgrade from inside the cluster |
| strong | Dang et al. (A01, W3014898655) | 2021 | preregistered multi-lab test | d = 0.10, 95% CI [0.01, 0.19] (DA-E2) | FULL-TEXT-CONFIRMED (version substitute) | verified | not determined | UNASSESSED | not scored separately | small effect |
| strong | Carter et al. 2015 (X16) | 2015 | bias-corrected meta-analysis | PET and PEESE "indistinguishable from zero" (CA-E2) | FULL-TEXT-CONFIRMED; POST HOC | verified | not determined | UNASSESSED | not scored separately | effect size contested |
| moderate | Inzlicht & Schmeichel 2012; Kurzban et al. 2013 (N47, N37) | 2012–2013 | theory | motivation/opportunity-cost rival (R2) | RECEPTION-CONFIRMED; METADATA | verified | not determined | UNASSESSED | not scored separately | rival mechanism inside RECEPTION-1 |

SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING

64. Recurring authors: the four target authors appear on 10/50 RECEPTION-1 works (N06, N09, N19, N26, N28, N29, N33, N36, N38, N41; I03), on R05 in RECENT-1, and on A03, A22, A45, A47 and R05 in ADJUDICATION-1 (plus overlap members N09, N33).
65. Venues in RECEPTION-1 (top six): Journal of Personality and Social Psychology 7; Psychological Bulletin 6; Perspectives on Psychological Science 4; Journal of Applied Psychology 3; Review of General Psychology 2; Journal of Occupational Health Psychology 2.
66–67. Institutions, funding: not derived; UNASSESSED.
68. Dissent venues: Perspectives on Psychological Science (RRR), Journal of Experimental Psychology: General (Carter et al. 2015), Psychological Science (Vohs et al. 2021), Social Psychological and Personality Science (Dang et al. 2021).
69–70. Gatekeeping and ideology: not assessable.

Closure type: authorship concentration around the founding cluster inside RECEPTION-1 (10/50 works, 62/113 internal in-edges); no journal, funding or advocacy closure established.

SECTION J: FALSE-POSITIVE AND BASELINE CHECK

71. Small field: no (self-control research is large; the target has more than 5,000 citers). 72. Baseline comparison: none built. 73. Adjacent expertise: the target's reference list includes stress, persistence and mood works, but none from the learned-helplessness or experimenter-expectancy queries (Section E). 74. Only people studying the question: no; most of RECEPTION-1 is from other fields. 75. Strong primary evidence: no; four small single-lab experiments (map field 1). 76. Repeated independent tests: yes for L2, with new data and near-zero to small effects (I13, I14); none for L1 in the locked search (I18). 77. Limitations preserved: partly; several premise uses state the resource as established (I09, I10). 78–80. Failed predictions acknowledged, critics engaged, updating: mixed (I19, I20).

Answers are mixed; this is not a cartel signature. The founding cluster is central to the reception, but critiques sit inside the corpus and part of the founding cluster has updated.

SECTION J2: THE CONCEDE TEST

| Finding | Declared target claim | Matches map field 6? | Same mechanism as another row? | Count separately? |
|---|---|---|---|---|
| 1 Field-6 paradigm untested at scale; general effect near zero to small | field 6 via L1 and L2 | yes | no | yes |
| 2 Founding-cluster-centred reception | field 6 network support | yes | no | yes |
| 3 Recent premise use | later use of the target | no — MAP GAP: targets downstream use, not map field 6 | no | yes |
| 4 Resource stated as shown | restatements of the target | no — MAP GAP: targets downstream restatements, not map field 6 | no | yes |
| 5 Mixed critique uptake | field 6 network support | yes | no | yes |
| 6 Rival literatures absent from the reference list | the target's reference list | no — MAP GAP: targets the source's engagement, not map field 6 | no | yes |
| 7 Retrieval and record limits | the retrieval record | no — MAP GAP: targets the retrieval record, not map field 6 | no | yes |

| Finding | Concede test: SURVIVES / NARROWS / DEFEATS | Surviving claim if NARROWS |
|---|---|---|
| 1 | NARROWS | In one lab with about 22 per cell, radish eaters quit unsolvable puzzles sooner; the magnitude is not supported as a general effect, and the paradigm has no high-powered direct replication in the locked search |
| 2 | SURVIVES | — |
| 3 | SURVIVES | — |
| 4 | SURVIVES | — |
| 5 | SURVIVES | — |
| 6 | SURVIVES | — |
| 7 | SURVIVES | — |

| Finding | Scope-loss level | Original claim | Surviving claim | What epistemic or practical work is lost? |
|---|---|---|---|---|
| 1 | major | d about 1.8 food-temptation effect showing a limited self-control resource | a single-lab small-sample difference; the general effect is near zero to small in preregistered multi-site tests (RRR-E2, VO-E2, DA-E2) | the large effect size and its use as evidence for a general limited resource |

Finding 1 NARROWS field 6. Its failure location is the PAPER (small single-lab cells; numbers PROVISIONAL from secondhand sources); the network carries the claim forward (Findings 2–5).

SECTION K0: EVIDENCE SUFFICIENCY LEDGER

Gate B was applied to every inference before any score or finding used it. Inferences that fail stay listed with what would make them sufficient.

INFERENCE LEDGER

| Inference | Class | Corpus | Claimed scope | Sampling rule | Members used | Disposition | Statement |
|---|---|---|---|---|---|---|---|
| I01 | GRAPH-STRUCTURE | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Directed internal density 113/2450 = 4.61% at work level (50/50 reference lists); no dense closed cluster inside RECEPTION-1. |
| I02 | GRAPH-STRUCTURE | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Founding-cluster works (10/50 nodes) receive 62/113 internal edges, 46 from outside the cluster; the two top in-degree nodes are founding-cluster works (N19 22, N06 15). |
| I03 | DATABASE-RECORD | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | 10/50 works list Baumeister, Bratslavsky, Muraven or Tice as an author (N06, N09, N19, N26, N28, N29, N33, N36, N38, N41). |
| I04 | GRAPH-STRUCTURE | RECENT-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | 13/25 recent citers cite a founding-cluster work beyond the target; 8/25 cite a listed critique or null test; 6/25 cite founding-cluster work and no listed critique (R04, R06, R09, R13, R21, R24). |
| I05 | CITATION-USE | RECEPTION-1 | CORPUS | PRESPECIFIED-RANDOM | N07, N09, N10, N11, N20, N27, N28, N39, N40, N41, N42, N44 | INSUFFICIENT | How RECEPTION-1 uses the target cannot be estimated from the random sample: 4/12 sampled passages were inspectable (S2 contexts; no other authorized full text retrieved). Sufficient with all 12 passages. |
| I06 | CITATION-USE | RECEPTION-1 | WITHIN-SAMPLE | CONVENIENCE | N27, N41, N42, N44 | SUPPORTED-WITHIN-SAMPLE | The four inspectable sampled passages: N27 QUALIFIES (CTX-E13), N41 SUPPORTS (CTX-E17), N42 and N44 MENTIONS (CTX-E18, CTX-E20). |
| I07 | CITATION-USE | RECEPTION-1 | WITHIN-SAMPLE | CONVENIENCE | N03, N05, N06, N08, N12, N13, N14, N16, N18, N22, N25, N26, N27, N31, N33, N36, N41, N42, N43, N44, N45, N49 | SUPPORTED-WITHIN-SAMPLE | Among 22 inspected passages: SUPPORTS 5, PREMISE 5, CHALLENGES 1, QUALIFIES 1, MENTIONS 10. |
| I08 | CITATION-USE | RECENT-1 | CORPUS | EXHAUSTIVE | ALL | INSUFFICIENT | How the recent corpus uses the target: 12/25 passages inspected. Sufficient with all 25 passages. |
| I09 | CITATION-USE | RECENT-1 | WITHIN-SAMPLE | CONVENIENCE | R01, R02, R06, R07, R08, R13, R16, R17, R18, R19, R21, R25 | SUPPORTED-WITHIN-SAMPLE | 6/12 inspected recent passages use the limited-resource model as a premise (R07, R08, R13, R17, R18, R21); R16 excludes depletion studies (CTX-E28). |
| I10 | CITATION-USE | — | NAMED | NOT-APPLICABLE | N05, N12, N22, N25, N43, R01, R07, R13 | SUPPORTED | Eight passages state resource drain as an established fact when citing the target (CTX-E2, CTX-E5, CTX-E10, CTX-E11, CTX-E19, CTX-E22, CTX-E25, CTX-E27). |
| I11 | SOURCE-RESULT | — | NAMED | NOT-APPLICABLE | T01 | SUPPORTED | The target measured behavioural differences; it states the limited resource as an inference: results "suggest" a limited capacity (TA-E1). |
| I12 | RESTATEMENT | — | NAMED | NOT-APPLICABLE | T01, N13, N33, A08, R01 | INSUFFICIENT | Whether downstream restatements mutate the target claim. The target body was not read (publisher 403; ABSTRACT only), so the RESTATEMENT minimum is unmet. Sufficient with the target full text from an authorized source. |
| I13 | SOURCE-RESULT | — | NAMED | NOT-APPLICABLE | N45, A03, A01 | SUPPORTED | Three preregistered multi-site tests of L2 find near-zero to small effects: d = 0.04 (RRR-E2), d = 0.06 [−0.02, 0.14] (VO-E2), d = 0.10 [0.01, 0.19] (DA-E2). |
| I14 | DATA-ORIGIN | — | NAMED | NOT-APPLICABLE | N45, A03, A01, T01 | SUPPORTED | The three tests use new data collected under preregistered protocols across 23, multiple and 12 labs, independent of the target's single-lab data. |
| I15 | COMPOSITION | ADJUDICATION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Relevance composition of the evidence base within the locked search (METADATA-coded). |
| I16 | COMPOSITION | ADJUDICATION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Contribution composition within the locked search (METADATA-coded). |
| I17 | COMPOSITION | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | Relevance composition of the citing set; describes citers, not the evidence base. |
| I18 | ABSENCE | ADJUDICATION-1 | WITHIN-SAMPLE | EXHAUSTIVE | SCREENED | SUPPORTED-WITHIN-SAMPLE | Within the screened members of the locked search (59/59 screened), none tests L1 (the food-temptation → persistence paradigm): 0 are DIRECT (L1). Bounded by queries Q1–Q7, top 10 each; known-item recall 8/12, so no statement is made beyond the search. The RRR chose another task (RRR-E1). |
| I19 | ENGAGEMENT | — | NAMED | NOT-APPLICABLE | X17 | SUPPORTED | The founding authors' 2016 comment says the RRR "did not test ego depletion" (BV-E1): critique engaged and disputed. X17 is a named POST HOC source (K11); under review. |
| I20 | ENGAGEMENT | — | NAMED | NOT-APPLICABLE | A03 | SUPPORTED | A 2021 multi-site test co-authored by Muraven concludes depletion is "not as reliable or robust as previously assumed" (VO-E3): partial update inside the founding cluster. |
| I21 | GRAPH-STRUCTURE | — | NAMED | NOT-APPLICABLE | T01, X01, X02, X03, X04, X05, X06, X07, X08, X09, X10, X11, X12, X13, X14, X15 | SUPPORTED | The target's OpenAlex reference list (57/58 resolved) contains 0/15 Section E locked sources and no learned-helplessness (F2) or experimenter-expectancy (F4) work. |
| I22 | ENGAGEMENT | — | NAMED | NOT-APPLICABLE | T01 | NOT-ASSESSED | Whether the target text addresses helplessness, expectancy or motivation rivals. Not assessed: target body not read; sufficient with the full text. |
| I23 | CO-CITATION | RECEPTION-1 | CORPUS | EXHAUSTIVE | ALL | SUPPORTED | 1/3 RECEPTION-1 works published 2017 or later cite a listed critique. Co-citation, not use; descriptive only. |
| I24 | ENGAGEMENT | — | NAMED | NOT-APPLICABLE | R05 | NOT-ASSESSED | The founding authors' 2024 status review (R05). Not assessed: no authorized full text retrieved; sufficient with its full text. |
| I25 | DATABASE-RECORD | — | NAMED | NOT-APPLICABLE | T01, A01, A03, A05 | SUPPORTED | Target record: cited_by_count 5374 against a citing population of 5359; 58 referenced works, 57 resolved. Dang et al. 2021 carries year 2020; two works appear as duplicate records (A03, A05). |
| I26 | RESTATEMENT | — | NAMED | NOT-APPLICABLE | — | NOT-ASSESSED | Downstream reliance on review hubs (N06, N09, N16) in place of the target. Not assessed: no hub-citing passage inspected; sufficient with inspected passages from a defined hub-citing set. |

COMPOSITION: I15 | relevance | ADJACENT=32; BACKGROUND=3; DIRECT=24 | TOTAL=59
COMPOSITION: I16 | contribution | COMMENTARY=3; INDEPENDENT-DATA=28; REANALYSIS=4; REVIEW=19; THEORY=5 | TOTAL=59
COMPOSITION: I17 | relevance | ADJACENT=20; BACKGROUND=27; DIRECT=3 | TOTAL=50

SAMPLE ATTRITION: I05 4/12

Sample record: ranks 7, 9, 10, 11, 20, 27, 28, 39, 40, 41, 42, 44 drawn with the preregistered seed (lock/SAMPLES_draw.txt, sha256 cddd163f3db599c0ab84b4589764ee2c8f247a09bc8887479803511833df5a2f); inspected N27, N41, N42, N44; the N40 context did not show the citation; the other 7 had no usable context and no authorized full text retrieved.

Withheld inferences: I05 (INSUFFICIENT: sample attrition), I08 (INSUFFICIENT: 12/25 recent passages), I12 (INSUFFICIENT: target body not read), I22, I24 and I26 (NOT-ASSESSED).

DIMENSION EVIDENCE BASIS

DIMENSION CLASS MAP: cn7-map-3

| Scorecard dimension | Scorecard disposition | Inference IDs | Basis note |
|---|---|---|---|
| Founding-cluster dominance | SCORED 2 | I02 (+), I03 (+) | founding works 10/50 nodes take 62/113 internal edges; top two hubs are founding works |
| Internal citation density | SCORED 0 | I01 (-) | 4.61% inside RECEPTION-1 only; closure not excluded beyond it |
| Recent-paper dependence | SCORED 2 | I04 (+), I09 (+), I08 (?) | 13/25 recent citers cite founding work beyond the target; 6/12 inspected passages premise use; census 12/25 inspected |
| Review-hub laundering | UNASSESSED | — | I26 NOT-ASSESSED: no hub-citing passage inspected; RESTATEMENT minimum unmet |
| Proxy mismatch | SCORED 1 | I10 (+), I11 (+), I12 (?) | behavioural differences restated as a shown resource drain; restatement comparison INSUFFICIENT |
| Claim mutation | UNASSESSED | — | I12 INSUFFICIENT: target held at ABSTRACT level |
| Adjacent-field neglect | SCORED 1 | I21 (+), I22 (?) | 0/15 locked sources and no F2/F4 work in the reference list; text engagement not assessed |
| Lack of decisive tests | SCORED 1 | I18 (+), I13 (-), I14 (-) | L2 tested decisively with new data (near zero to small); L1 paradigm 0/59 in the locked search |
| Poor critique uptake | SCORED 1 | I19 (+), I20 (-), I24 (?) | founding authors disputed the RRR (2016) and one co-signed a downgrade (2021); 2024 review not read |
| Intervention-evidence ratchet | N/A | — | no intervention claim at field 6 or in the traced network |
| Model non-updating | UNASSESSED | — | four-link gate: link 4 not determinable (I19, I20 mixed; I24 NOT-ASSESSED) |

FINDING EVIDENCE BASIS

| Finding | Finding status | Inference IDs |
|---|---|---|
| Finding 1 | confirmed | I11, I13, I14, I18 |
| Finding 2 | confirmed | I01, I02, I03 |
| Finding 3 | provisional | I04, I09, I08 |
| Finding 4 | provisional | I10, I11, I12 |
| Finding 5 | provisional | I19, I20, I24 |
| Finding 6 | provisional | I21, I22 |
| Finding 7 | confirmed | I25 |

SECTION K: CARTEL-RISK SCORING

Scores are in Artifact 8. All seven scored dimensions are INDEPENDENT: no two rest on the same passage or test. Founding-cluster dominance and internal density use the same RECEPTION-1 edge list but answer different questions (in-edge concentration and authorship vs overall density); recent-paper dependence uses the separate RECENT-1 corpus.

- Verified risk score: 8/21
- Verified scored-dimension risk rate: 38.1
- Independent scored dimensions: 7
- Nested scored dimensions: 0
- Verified risk denominator: 21
- Evidentiary coverage: 7/10 applicable dimensions scored (70%)
- Execution completeness: 7/10 applicable dimensions completed (70%)
- Dimension inventory: 7 INDEPENDENT SCORED + 0 NESTED SCORED + 0 UNINFORMATIVE + 3 UNASSESSED + 1 N/A = 11 total dimensions; 10 applicable
- Unscored dimensions: Review-hub laundering — UNASSESSED (I26); Claim mutation — UNASSESSED (I12 INSUFFICIENT); Model non-updating — UNASSESSED (link 4 not determinable); Intervention-evidence ratchet — N/A (no intervention claim)

Verified scored-dimension risk: 38.1%, calculated from 7 independent scored dimensions; 0 additional scored dimensions are NESTED; 7 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.

Formal-label gate: coverage 7/10 (70%) declared, exactly at the PROVISIONAL 70% gate (engineering threshold, not validated). Recent-paper dependence, proxy mismatch, adjacent-field neglect, lack of decisive tests and poor critique uptake carry open review items, so coverage is 2/10 (20%) if those items are withdrawn: the gate is met only if the review items resolve. Label-essential check: the arithmetic position is the >20%–40% band, which is not a closure, laundering or healthy label; no closure or laundering label is proposed, because review-hub laundering, claim mutation and model non-updating are UNASSESSED. The rate is 1.9 points below the 40% boundary, so the band position is sensitive to any one score.

ARITHMETIC BAND POSITION: >20%–40% (normal field clustering with some weaknesses)
RISK BAND: >20%–40% normal field clustering with some weaknesses — computed over 7 independent scored dimensions; breadth requirement PASSED. PROVISIONAL: coverage meets the 70% gate exactly and only if five review items resolve (20% without them); no closure or laundering label is supported because review-hub laundering, claim mutation and model non-updating are UNASSESSED.
MECHANISM LABEL: a founding-cluster-centred reception: the founding authors' own works are the main internal hubs and recent citers keep using the limited-resource model as a premise, while independent preregistered multi-site tests of the general effect found near-zero to small effects and the founding cluster has only partly updated; the field-6 paradigm itself was not re-tested at scale

ARTIFACT 1: TOP 15 CITATION SPINE TABLE

| Rank | Paper | Year | Citation count | Evidence type | Role in network | Source of citation count |
|---:|---|---:|---:|---|---|---|
| 1 | N01 James J. Gross: The Emerging Field of Emotion Regulation: An Integrative Review (W2096423181) | 1998 | 10430 | review article | ADJACENT; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 2 | N02 Stevan E. Hobfoll: The Influence of Culture, Community, and the Nested‐Self in the Stress (W2048385562) | 2001 | 7346 | theory | BACKGROUND; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 3 | N03 Alan Baddeley: Working memory: looking back and looking forward (W2066785847) | 2003 | 5224 | review article | BACKGROUND; MENTIONS | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 4 | N04 James J. Gross: Emotion regulation: Affective, cognitive, and social consequences (W2128126978) | 2002 | 5022 | review article | ADJACENT; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 5 | N05 Stevan E. Hobfoll: Social and Psychological Resources and Adaptation (W1997397294) | 2002 | 4678 | review article | BACKGROUND; MENTIONS | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 6 | N06 Mark Muraven, Roy Frederick Baumeister: Self-regulation and depletion of limited resources: Does self-control  (W2113390049) | 2000 | 4522 | review article | ADJACENT (L3); SUPPORTS; founding cluster | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 7 | N07 Charles R. R. Snyder: TARGET ARTICLE: Hope Theory: Rainbows in the Mind (W1968689002) | 2002 | 3865 | theory | BACKGROUND; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 8 | N08 John A. Bargh, Tanya L. Chartrand: The unbearable automaticity of being. (W2130142026) | 1999 | 3825 | theory | ADJACENT; PREMISE | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 9 | N09 Roy Frederick Baumeister, Kathleen D. Vohs, Dianne M. Tice: The Strength Model of Self-Control (W2108897328) | 2007 | 3711 | review article | ADJACENT (L3); CITES-UNINSPECTED; founding cluster | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 10 | N10 Alicia A. Grandey: Emotional regulation in the workplace: A new way to conceptualize emot (W2022472850) | 2000 | 3588 | theory | BACKGROUND; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 11 | N11 Angela Lee Duckworth, Patrick D. Quinn: Development and Validation of the Short Grit Scale (Grit–S) (W2093761921) | 2009 | 3517 | method | BACKGROUND; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 12 | N12 Jonathon R. B. Halbesleben, Jean‐Pierre Neveu, Samantha C. Paustian‐Underdahl et al.: Getting to the “COR” (W2161497363) | 2014 | 3486 | review article | BACKGROUND; PREMISE | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 13 | N13 Peter M. Gollwitzer, Paschal Sheeran: Implementation Intentions and Goal Achievement: A Meta‐analysis of Eff (W1818536883) | 2006 | 3262 | review article | ADJACENT; MENTIONS | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 14 | N14 Katherine White, Rishad Habib, David J. Hardisty: How to SHIFT Consumer Behaviors to be More Sustainable: A Literature R (W2912633426) | 2019 | 2663 | review article | BACKGROUND; MENTIONS | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |
| 15 | N15 Bella M. DePaulo, James J. Lindsay, Brian E. Malone et al.: Cues to deception. (W2089594500) | 2003 | 2523 | review article | BACKGROUND; CITES-UNINSPECTED | OpenAlex cited_by_count, query 2026-11-05T11:31:57Z (raw/reception1_top50.json) |

ARTIFACT 2: FOUNDING CLUSTER TABLE

| Paper | Year | Claim introduced | Evidence type | Verification state | Later role | Risk |
|---|---|---|---|---|---|---|
| Baumeister, Bratslavsky, Muraven & Tice, Ego depletion (T01, W2123817056) | 1998 | acts of volition draw on a limited resource; radish/chocolate persistence effect | four small single-lab experiments | ABSTRACT only (TA-E1) | canonical source; cited by 5,000+ | high for field 6 magnitude (Finding 1) |
| Muraven, Tice & Baumeister, Self-control as a limited resource (N19) | 1998 | regulatory depletion across tasks | primary empirical study | RECEPTION-CONFIRMED; METADATA | top in-degree hub (22) | founding-cluster hub |
| Muraven & Baumeister, Self-regulation and depletion of limited resources (N06) | 2000 | strength model review | review article | RECEPTION-CONFIRMED; EXCERPT (CTX-E3) | second hub (15); 6/25 recent citers | founding-cluster hub |
| Gailliot et al., Self-control relies on glucose (N41) | 2007 | glucose as the resource (L3) | primary empirical study | RECEPTION-CONFIRMED; EXCERPT (CTX-E17) | third hub (10) | L3 mechanism later contested (A16, A19 titles) |
| Vohs et al., multisite preregistered paradigm (A03) | 2021 | depletion "not as reliable or robust as previously assumed" | preregistered multi-site test | FULL-TEXT-CONFIRMED | partial update with founding-author co-author (Muraven) | none |

ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE

"Cites founding cluster?" means a work by Baumeister, Bratslavsky, Muraven or Tice beyond the target (all cite the target by construction). "Cites hub?" means N06, N09, N16 or N19. "Cites adjacent fields?" means a listed critique, null test or rival-mechanism work in the OpenAlex reference list.

| Recent paper | Year | Verification state | Cites founding cluster? | Cites hub? | Cites adjacent fields? | New evidence or recycling? |
|---|---:|---|---|---|---|---|
| R01 The Impact of Social Media on the Mental Health of Adolescents and You (W4385606438) | 2023 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | target only | no | no | mentions (CTX-E22) |
| R02 AI increases unethical consumer behavior due to reduced anticipatory g (W4214866453) | 2022 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | target only | no | no | mentions (CTX-E23) |
| R03 A neuro-metabolic account of why daylong cognitive work alters the con (W4291001390) | 2022 | RECEPTION-CONFIRMED; LOCATED | target only | no | RRR 2016 (N45); Kurzban et al. 2013 (N37) | not determined (no passage inspected) |
| R04 Psychological and biological resilience modulates the effects of stres (W3217148206) | 2021 | RECEPTION-CONFIRMED; LOCATED | yes (N06 Muraven 2000) | N06 | no | not determined (no passage inspected) |
| R05 Self-control and limited willpower: Current status of ego depletion th (W4402300076) | 2024 | RECEPTION-CONFIRMED; LOCATED | yes (N26 Ridder 2011, A03 Vohs 2021, A22 Gailliot 2007, A47 Muraven 2006) | N16 | RRR 2016 (N45); Vohs et al. 2021 (A03); Dang et al. 2021 (A01); Inzlicht & Schmeichel 2012 (N47) | not determined (no passage inspected) |
| R06 The Determinants of Impulsive Buying Behavior in Electronic Commerce (W4283313664) | 2022 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | yes (N28 Baumeister 2002) | no | no | mentions (CTX-E24) |
| R07 Abusive supervision: a systematic literature review (W4291535426) | 2022 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | target only | no | no | recycling: premise use (CTX-E25) |
| R08 Workflow interruption and nurses’ mental workload in electronic health (W4323652556) | 2023 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | target only | no | no | recycling: premise use (CTX-E26) |
| R09 Self-regulation and goal-directed behavior: A systematic literature re (W4310804025) | 2022 | RECEPTION-CONFIRMED; LOCATED | yes (N06 Muraven 2000, N09 Baumeister 2007, N19 Muraven 1998, N28 Baumeister 2002, N33 Baumeister 2007, N36 Baumeister 2005) | N06, N09, N19 | no | not determined (no passage inspected) |
| R10 Restoration of Attention by Rest in a Multitasking World: Theory, Meth (W4220818821) | 2022 | RECEPTION-CONFIRMED; LOCATED | yes (N41 Gailliot 2007, A03 Vohs 2021) | N16 | Vohs et al. 2021 (A03); Inzlicht & Schmeichel 2012 (N47); Kurzban et al. 2013 (N37) | not determined (no passage inspected) |
| R11 AI in the spotlight: The impact of artificial intelligence disclosure  (W4402676278) | 2024 | RECEPTION-CONFIRMED; LOCATED | target only | no | no | not determined (no passage inspected) |
| R12 Origins and consequences of cognitive fatigue (W4409103534) | 2025 | RECEPTION-CONFIRMED; LOCATED | yes (N06 Muraven 2000, N09 Baumeister 2007, N19 Muraven 1998, N33 Baumeister 2007, N41 Gailliot 2007, A03 Vohs 2021, A22 Gailliot 2007) | N06, N09, N19, N16 | Carter & McCullough 2014 (A09); Vohs et al. 2021 (A03); Dang et al. 2021 (A01); Kurzban et al. 2013 (N37); Job et al. 2010 (A32) | not determined (no passage inspected) |
| R13 Does Techno-invasion Lead to Employees’ Deviant Behaviors? (W4281731168) | 2022 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | yes (N33 Baumeister 2007) | no | no | recycling: premise use (CTX-E27) |
| R14 Inclusive leadership, employee performance and well-being: an empirica (W4390011768) | 2023 | RECEPTION-CONFIRMED; LOCATED | target only | no | no | not determined (no passage inspected) |
| R15 Metacognition and self-control: An integrative framework. (W4311667985) | 2022 | RECEPTION-CONFIRMED; LOCATED | yes (N09 Baumeister 2007, N26 Ridder 2011, N33 Baumeister 2007, A03 Vohs 2021, A47 Muraven 2006) | N09 | RRR 2016 (N45); Vohs et al. 2021 (A03); Vohs et al. 2021 preprint (A03); Friese et al. 2018 (A11); Inzlicht & Schmeichel 2012 (N47); Job et al. 2010 (A32) | not determined (no passage inspected) |
| R16 When Are We More Ethical? A Review and Categorization of the Factors I (W4311640673) | 2022 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | target only | no | no | qualifies (CTX-E28) |
| R17 The Intention-Behavior gap in Ethical Consumption: Mediators, Moderato (W3211993193) | 2021 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | target only | no | no | recycling: premise use (CTX-E29) |
| R18 The relationship between self-control and procrastination among adoles (W4205581247) | 2022 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | yes (N06 Muraven 2000, N09 Baumeister 2007, N26 Ridder 2011) | N06, N09, N16 | Friese et al. 2018 (A11); Job et al. 2010 (A32) | recycling: premise use (CTX-E30) |
| R19 Interindividual Variability in Mental Fatigue-Related Impairments in E (W4321368994) | 2023 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | yes (A03 Vohs 2021) | no | RRR 2016 (N45); Vohs et al. 2021 (A03); Dang et al. 2021 (A01) | mentions (CTX-E31) |
| R20 Toward a Theory of Emotions in Competitive Sports (W4200151748) | 2021 | RECEPTION-CONFIRMED; LOCATED | target only | no | no | not determined (no passage inspected) |
| R21 The association between academic stress, social support, and self-regu (W4308964018) | 2022 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | yes (N09 Baumeister 2007, N19 Muraven 1998) | N09, N19 | no | recycling: premise use (CTX-E32) |
| R22 Supervisor incivility and turnover intention of the employees in the h (W4302307858) | 2022 | RECEPTION-CONFIRMED; LOCATED | yes (N06 Muraven 2000, N09 Baumeister 2007, N33 Baumeister 2007) | N06, N09 | Friese et al. 2018 (A11) | not determined (no passage inspected) |
| R23 Why People Do What They Do: An Interdisciplinary Synthesis of Human Ac (W4285800368) | 2022 | RECEPTION-CONFIRMED; LOCATED | target only | N16 | no | not determined (no passage inspected) |
| R24 Physical Activity and Academic Procrastination among Chinese Universit (W4280566821) | 2022 | RECEPTION-CONFIRMED; LOCATED | yes (N06 Muraven 2000, N09 Baumeister 2007, N26 Ridder 2011, N28 Baumeister 2002, N41 Gailliot 2007) | N06, N09 | no | not determined (no passage inspected) |
| R25 Event-Oriented Organizational Behavior Research: A Multilevel Review a (W4366496226) | 2023 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpt) | target only | no | no | mentions (CTX-E33) |

RECENT-1 summary: founding-cluster work beyond the target 13/25; listed critique or null test 8/25; rival-mechanism work 6/25; founding work without any listed critique 6/25; hubs N09 7, N06 6, N16 5, N19 3.

ARTIFACT 4: CITATION POLARITY TABLE

| Citing paper | Cited paper | Verification state | Citation polarity | Claim use | Inflation risk |
|---|---|---|---|---|---|
| N03 W2066785847 Working memory: looking back and looking forward (2003 | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E1: self-control rests on a system "limited in capacity and subject to fatigue-like decline" (working-memory review) | low |
| N05 W1997397294 Social and Psychological Resources and Adaptation (200 | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E2: willpower as a resource; "this cognitive capacity is diminished with use" | moderate |
| N06 W2113390049 Self-regulation and depletion of limited resources:… ( | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive | CTX-E3: founding-cluster review: food-temptation test run "to help rule out moods as a potential explanation" | low |
| N08 W2130142026 The unbearable automaticity of being. (1999) | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E4: "Given the severe limitations of conscious selfregulation capacity" (Baumeister et al., 1998) as premise for aut | low |
| N12 W2161497363 Getting to the “COR” (2014) | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E5: "self-regulation in and of itself is a drain on resources" (COR theory review) | moderate |
| N13 W1818536883 Implementation Intentions and Goal Achievement: A Me…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E6: restates Experiment 1: radish eaters "persisted for less time on a subsequent unsolvable puzzles task" (faithful | low |
| N14 W2912633426 How to SHIFT Consumer Behaviors to be More Sustainab…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E7: people find it hard to "forgo benefits in the present" (sustainability review) | low |
| N16 W2060763381 Ego depletion and the strength model of self-control…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive | CTX-E8: Baumeister and coworkers "provided initial support for the ego-depletion effect"; meta-analysis built on the dua | low |
| N18 W2789530810 The Adolescent Brain Cognitive Development (ABCD) st…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E9: a demanding task "has been associated with diminished performance on subsequent tasks" (ABCD imaging protocol) | low |
| N22 W2105538889 Enriching or Depleting? The Dynamics of Engagement i…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E10: suppressing emotion "may use up resources that might otherwise be used for coping" | moderate |
| N25 W2045934080 Emotional intelligence: An integrative meta-analysis…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E11: "Emotion regulation demands can drain resources from task performance" | moderate |
| N26 W2077057247 Taking Stock of Self-Control (2011) | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E12: "evidence confirms" capacity for self-control is susceptible to previous attempts (founding-author co-written m | low |
| N27 W1976788357 Self‐Regulation and the Problem of Human Autonomy: D…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | qualifying | CTX-E13: new experiments found "true choice was not depleting" contra the target's high-choice condition | none |
| N31 W1977835193 Impulse and Self-Control From a Dual-Systems Perspec…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive | CTX-E14: Baumeister and colleagues "have established the importance of selfregulatory resource[s]" | low |
| N33 W2125068113 Self‐Regulation, Ego Depletion, and Motivation (2007) | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive | CTX-E15: founding-cluster review: regulating the self "appears to depend on a limited resource"; also ADJUDICATION-1 (Q4 | low |
| N36 W1996918954 Social exclusion impairs self-regulation. (2005) | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E16: founding-cluster study: the target "replicated a study on ego depletion using solvable rather than unsolvable a | low |
| N41 W2146569853 Self-control relies on glucose as a limited energy s…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive | CTX-E17: founding-cluster glucose study: the depleted resource "has been a puzzle since the earliest findings"; POST HOC | low |
| N42 W2122634808 Interdependence, Interaction, and Relationships (2002) | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E18: listed for constrained cognitive capacity (passage truncated at the citation) | low |
| N43 W1871370349 Work–Family Conflict and Flexible Work Arrangements:…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E19: "These acts of volition draw upon ego resources" | moderate |
| N44 W2081900501 The effects of choice on intrinsic motivation and re…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E20: "making choices is one form of self-regulation that can result in ego-depletion" | low |
| N45 W2499154041 A Multilab Preregistered Replication of the Ego-Depl…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED | critical | RRR-E1 p. 548: Study 1 "required participants to taste radishes and resist cookies"; RRR-E2 p. 554: pooled d = 0.04 acro | none |
| N49 W2153950939 Spent Resources: Self‐Regulatory Resource Availabili…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E21: depletion listed across "overeating, procrastination, intellectual un-derachievement" | low |
| R01 W4385606438 The Impact of Social Media on the Mental Health of A…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E22: attributes "displaced behavior theory" to Baumeister; self-control "a limited resource that can be drained over | moderate |
| R02 W4214866453 AI increases unethical consumer behavior due to redu…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E23: time spent choosing used "as a proxy of service engagement" (Baumeister et al., 1998) | low |
| R06 W4283313664 The Determinants of Impulsive Buying Behavior in Ele…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E24: "Some scholars have proposed a 'strength' or 'limited resource' model" | low |
| R07 W4291535426 Abusive supervision: a systematic literature review (2 | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E25: victims "exhaust their limited resources" and experience ego-depletion | moderate |
| R08 W4323652556 Workflow interruption and nurses’ mental workload in…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E26: difficult tasks leave "insufficient personal resources … under the limited strength model" | low |
| R13 W4281731168 Does Techno-invasion Lead to Employees’ Deviant Beha…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E27: "All acts of self-regulation are empowered by a limited, metaphorical strength" | moderate |
| R16 W4311640673 When Are We More Ethical? A Review and Categorizatio…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | qualifying | CTX-E28: review chose "to exclude ego-depletion studies" unless strong evidence was given | none |
| R17 W3211993193 The Intention-Behavior gap in Ethical Consumption: M…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E29: "striving to achieve one goal can compromise the pursuit of subsequent goals" | low |
| R18 W4205581247 The relationship between self-control and procrastin…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E30: "theoretical foundation … built on a strength model of self-control known as ego depletion theory" | low |
| R19 W4321368994 Interindividual Variability in Mental Fatigue-Relate…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E31: ego depletion listed as one name for mental fatigue | low |
| R21 W4308964018 The association between academic stress, social supp…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E32: effortful behaviour can "use a significant amount of their own regulatory resources" | low |
| R25 W4366496226 Event-Oriented Organizational Behavior Research: A M…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E33: resource gains and losses as mediators (Baumeister et al., 1998 in a list) | low |
| A01 W3014898655 A Multilab Replication of the Ego Depletion Effect (20 | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED | qualifying | DA-E1 Introduction: the target "reported the ego depletion effect for the first time" and is "cited over 5,000 times"; D | none |
| A03 W3119325546 + W4256555852 (preprint record) A Multisite Preregiste | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED | critical | VO-E1 p. 1568: "The seminal article" (the target) "has had 'transformational' impact"; VO-E2 p. 1574: d = 0.06, 95% CI [ | none |
| A06 W3157428216 Again, No Evidence for or Against the Existence of E…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED | neutral/background | EN-E1 (Method summary): the e-crossing task "(… Baumeister et al., 1998) served as the initial task" in the 2021 multisi | low |
| A08 W2604293295 An updated meta-analysis of the ego depletion effect ( | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E34: "over 300 independent studies have replicated this effect … since it was first reported"; K7 | moderate |
| A13 W2588069705 The Debate on the Ego-Depletion Effect: Evidence fro…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | qualifying | CTX-E35: "Such convergence does not show up for the so-called ego-depletion effect" | none |
| A15 W1989768409 Is ego depletion too incredible? Evidence for the ov…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E36: defines "the so-called depletion effect" (Baumeister et al. 1998) in a commentary on overestimation | low |
| A18 W2152858830 The Role of Glucose in Self-Control (2011) | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E37: "resisting the temptation to eat chocolate (Baumeister et al., 1998, Study 1)" listed among depletion tasks | low |
| A22 W1966401421 The Physiology of Willpower: Linking Blood Glucose t…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive | CTX-E38: founding-author review: "resisting the temptation to eat cookies caused participants subsequently to give up fa | low |
| A27 W2538010233 Too Depleted to Try? Testing the Process Model of Eg…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E39: "The e-crossing task was used to manipulate ego depletion (Baumeister et al., 1998 …)" | low |
| A32 W2118108696 Ego Depletion—Is It All in Your Head? (2010) | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E40: task "adopted from previous research to manipulate ego depletion (Baumeister et al., 1998 …)"; K9 | low |
| A34 W1976771764 Implicit theories about willpower predict self-regul…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E41: strength model "posits that selfcontrol relies on a limited energy resource" | low |
| A37 W2739641472 Implicit Theories About Willpower in Resisting Tempt…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E42: "We adapted a study design involving resistance to tempting food as the depletion manipulation" | low |
| A43 W1988113868 Choice and Ego-Depletion: The Moderating Role of Aut…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | qualifying | CTX-E43: "According to the Baumeister et al. (1998) model … making choices would necessarily result in ego-depletion" (t | none |
| A45 W1992322615 Ostracism and Ego Depletion: The Strains of Silence (2 | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E44: founding-author co-written study: the target "proposed the term 'ego depletion'" | low |
| A47 W2150495553 Conserving self-control strength. (2006) | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive | CTX-E45: founding-author study: "Consistent with Baumeister et al. (1998), the incorrect/missing solutions did not occur | low |
| A49 W2301647011 The Strength Model of Self-Control in Sport and Exer…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | neutral/background | CTX-E46: effects "not caused by … mood differences (e.g., Baumeister et al., 1998 …)" (sport review) | low |
| A51 W1608074949 Integrating attentional control theory and the stren…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E47: "Like a muscle, one's self-control strength can become exhausted and depleted" | low |
| A52 W2170958357 Neuroenhancement and the strength model of self-cont…  | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED (excerpt) | supportive (premise) | CTX-E48: "We identified the strength model of selfcontrol (Baumeister et al., 1998) as a promising candidate theory" | low |
| X16 Carter, Kofler, Forster & McCullough 2015, A Series of Meta-Analyt | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED | critical | CA-E1 p. 1: "(the depletion effect; Baumeister et al., 1998)"; CA-E2 p. 16: PET and PEESE estimates "indistinguishable f | none |
| X18 Schimmack 2016, replicability analysis of ego depletion (Replicabi | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED | critical | SC-E1 (Study 1 analysis section; Stage 1 source S2): computes Experiment 1 effect sizes from reported statistics (d = 1. | none |
| X19 Baumeister 2012, LSE public lecture slides "Willpower" | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED | supportive | LS-E1 (slide headings; Stage 1 D1/D1b): slides "Willpower is limited", "Like a Muscle"; founding author; POST HOC | low |
| X20 APA public page "Is Willpower a Limited Resource?" | Baumeister et al. 1998 | FULL-TEXT-CONFIRMED | supportive | AP-E1 (Stage 1 D2/D2b): describes the study as having "drained the subjects' self-control"; POST HOC | moderate |

Semantic Scholar contexts were used as EXCERPT access; CTX-E ids resolve to Semantic Scholar citation contexts (requests /graph/v1/paper/DOI:10.1037/0022-3514.74.5.1252/citations?fields=title,year,externalIds,contexts,intents&limit=1000 at offsets 0–5000, 2026-11-05T11:46:57Z–11:47:33Z, HTTP 200; response sha256 offset 0 fa01fc13afde2ebebd3b45e3adb9a7521fbfbb17e35340a854d277b49b31d192, 1000 506bd23a…b869, 2000 aee93a2e…757e, 3000 bbd0daa7…a7ff, 4000 3e809623…2e15, 5000 735212ae…9929; three earlier offset-0 attempts at 11:45:37–11:46:10Z were logged without an HTTP status (rate-limited retries); responses not committed).

ARTIFACT 5: CLAIM MUTATION TABLE

| Original source | Original claim | Verification state | Hub restatement | Downstream restatement | Mutation severity |
|---|---|---|---|---|---|
| Target abstract (TA-E1) | results "suggest" a limited capacity for volition | ABSTRACT only | N33 "appears to depend on a limited resource" (CTX-E15) | X19 "Willpower is limited"; X20 "drained the subjects' self-control" | not graded (RESTATEMENT minimum unmet) |
| Target Experiment 1 (field 6, PROVISIONAL) | radish eaters quit sooner, one lab | secondhand (Stage 1) | none found | N13 (CTX-E6), A22 (CTX-E38) faithful | not graded |
| Target and follow-ups | depletion effect first reported | ABSTRACT only | none found | A08 "over 300 independent studies have replicated this effect" (CTX-E34) | not graded |
| Target | ego depletion / limited resource | ABSTRACT only | none found | R01 "displaced behavior theory" attributed to Baumeister (CTX-E22) | not graded |

ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE

Preregistration table as in SECTION E. POST HOC rows anchor no score.

| Claim layer | Adjacent field | Nominated source and stable identifier | Verification state | Source class: CONSTRUCT-DEFINING / MECHANISM-SUPPORTING / DIRECTLY-ADJUDICATING | Actual result | Explanation favored | Explanation weakened | Precise revision required | Pre-inspection lock status or POST HOC | Cited by dominant cluster? | Engagement quality | Effect of omission |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| L1/L3 | F1 mental fatigue | X01 W2084221958 On Leaping to Conclusions When Feeling Tired: Mental Fatigue | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L1/L3 | F1 mental fatigue | X02 W2319902335 Blocking: A New Principle of Mental Fatigue (1931) | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L1/L3 | F1 mental fatigue | X03 W4253912427 The Mental Health of Patients With a Chief Complaint of Chro | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L1 | F2 learned helplessness | X04 W2029487046 Learned helplessness in humans: Critique and reformulation.  | LOCATED | DIRECTLY-ADJUDICATING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L1 | F2 learned helplessness | X05 W2022987442 Learned helplessness: Theory and evidence. (1976) | LOCATED | DIRECTLY-ADJUDICATING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L1 | F2 learned helplessness | X06 W2139986071 The role of expectations and attributions in the alleviation | LOCATED | DIRECTLY-ADJUDICATING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L1 | F3 mood and persistence | X07 W2119926219 The relationship between breast feeding persistence, sexuali | LOCATED | MECHANISM-SUPPORTING | off-topic (title) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | none (off-topic exemplar) |
| L1 | F3 mood and persistence | X08 W1537717563 Mood, Persistence, and success (1987) | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L1 | F3 mood and persistence | X09 W2012786194 The effects of children's goal structures and performance fe | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L1 | F4 experimenter expectancy | X10 W1981707533 Magnitude of teacher expectancy effects on pupil IQ as a fun | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L1 | F4 experimenter expectancy | X11 W2068172336 Experimenter expectancy and the reassuring nature of the nul | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L1 | F4 experimenter expectancy | X12 W2059803871 Alcohol and the balanced-placebo design: The role of experim | LOCATED | MECHANISM-SUPPORTING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | rival not addressed at reference-list level |
| L3 | F5 mental effort | X13 W2074791822 Television is "easy" and print is "tough": The differential… | LOCATED | CONSTRUCT-DEFINING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L3 | F5 mental effort | X14 W2098813016 The Efficiency of Instructional Conditions: An Approach to C | LOCATED | CONSTRUCT-DEFINING | title only; results not read | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | minor context loss |
| L3 | F5 mental effort | X15 W2129275476 Vegetative response during imagined movement is proportional | LOCATED | CONSTRUCT-DEFINING | off-topic (title) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | not determined: results not read (METADATA only) | LOCKED (Section E query) | no (not in the target reference list) | none visible in the reference list; text UNASSESSED | none (off-topic exemplar) |

ARTIFACT 7: CRITIQUE-UPTAKE TABLE

| Expected-production precondition | Critique / contrary evidence | Year | Source type | Main objection | Verification state | Reception opportunity | Cited by dominant cluster? | Uptake status | Dimension disposition | Effect on consensus |
|---|---|---|---|---|---|---|---|---|---|---|
| strong | Hagger et al. RRR (N45, W2499154041) | 2016 | preregistered multi-lab test | pooled d = 0.04 across 23 labs (RRR-E2) | FULL-TEXT-CONFIRMED | verified | yes; founding authors replied (X17) | disputed: "did not test ego depletion" (BV-E1) | SCORED 1 (I19, under review) | effect contested |
| strong | Vohs et al. (A03, W3119325546) | 2021 | preregistered multi-site test | d = 0.06, 95% CI [−0.02, 0.14] (VO-E2) | FULL-TEXT-CONFIRMED | verified | co-authored by Muraven | accepted: "not as reliable or robust as previously assumed" (VO-E3) | counts against concern (I20) | downgrade from inside the cluster |
| strong | Dang et al. (A01, W3014898655) | 2021 | preregistered multi-lab test | d = 0.10, 95% CI [0.01, 0.19] (DA-E2) | FULL-TEXT-CONFIRMED (version substitute) | verified | not determined | UNASSESSED | not scored separately | small effect |
| strong | Carter et al. 2015 (X16) | 2015 | bias-corrected meta-analysis | PET and PEESE "indistinguishable from zero" (CA-E2) | FULL-TEXT-CONFIRMED; POST HOC | verified | not determined | UNASSESSED | not scored separately | effect size contested |
| moderate | Inzlicht & Schmeichel 2012; Kurzban et al. 2013 (N47, N37) | 2012–2013 | theory | motivation/opportunity-cost rival (R2) | RECEPTION-CONFIRMED; METADATA | verified | not determined | UNASSESSED | not scored separately | rival mechanism inside RECEPTION-1 |

ARTIFACT 8: CARTEL-RISK SCORECARD

| Dimension | Applicability | Dimension disposition | Score if SCORED | Evidence / claim state | Evidence supporting disposition and score | Evidence identifiers | Retrieval coverage | AGGREGATION STATUS | Independent evidence and inferential work, or nesting rationale | Reason excluded from denominator | Effect on formal-label gate |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Founding-cluster dominance | applicable | SCORED 2 | 2 | RECEPTION-CONFIRMED (verification state for score 2: computed from 50/50 OpenAlex reference lists and authorships) | 10/50 founding works take 62/113 internal edges; top two hubs founding | I02; I03 | 50/50 reference lists | INDEPENDENT | in-edge concentration and authorship | — | counts toward coverage |
| Internal citation density | applicable | SCORED 0 | 0 | RECEPTION-CONFIRMED | 113/2450 = 4.61% | I01 | 50/50 inputs | INDEPENDENT | overall density | — | affirmative inside RECEPTION-1 only |
| Recent-paper dependence | applicable | SCORED 2 | 2 | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpts) (verification state for score 2: 25/25 reference lists; 12/25 passages) | 13/25 cite founding work beyond target; 6/12 inspected premise use | I04; I09; I08 | 25/25 reference lists; 12/25 passages | INDEPENDENT | separate recent corpus | — | counts toward coverage; under review |
| Review-hub laundering | applicable | UNASSESSED | — | — | hub reliance not traced | I26 | 0 hub-citing passages | — | — | UNASSESSED | not essential to the issued band; closure and laundering labels unavailable |
| Proxy mismatch | applicable | SCORED 1 | 1 | FULL-TEXT-CONFIRMED (excerpts); ABSTRACT for target | resource drain stated as shown (8 passages) vs "suggest" in TA-E1 | I10; I11; I12 | 8 named passages | INDEPENDENT | restated construct vs measured behaviour | — | counts toward coverage; under review |
| Claim mutation | applicable | UNASSESSED | — | — | target body not read | I12 | ABSTRACT only | — | — | UNASSESSED | closure and laundering labels unavailable |
| Adjacent-field neglect | applicable | SCORED 1 | 1 | METADATA (reference list) | 0/15 locked sources; no F2/F4 work cited | I21; I22 | 57/58 references resolved | INDEPENDENT | source-layer reference list | — | counts toward coverage; under review |
| Lack of decisive tests | applicable | SCORED 1 | 1 | FULL-TEXT-CONFIRMED (tests); METADATA (screen) | L2 tested decisively (RRR-E2, VO-E2, DA-E2); L1 0/59 in the locked search | I18; I13; I14 | ADJUDICATION-1 screened by title | INDEPENDENT | named test results and search absence | — | counts toward coverage; under review |
| Poor critique uptake | applicable | SCORED 1 | 1 | FULL-TEXT-CONFIRMED | RRR disputed (BV-E1); 2021 downgrade co-signed (VO-E3) | I19; I20; I24 | X17, A03 full texts | INDEPENDENT | engagement in the uptake population | — | counts toward coverage; under review |
| Intervention-evidence ratchet | not applicable | N/A | — | — | no intervention claim | — | — | — | — | N/A: no intervention claim | none |
| Model non-updating | applicable | UNASSESSED | — | — | link 4 not determinable | I19; I20; I24 | R05 not read | — | — | UNASSESSED | closure label unavailable |

Verified risk score 8/21; rate 38.1%; independent 7; nested 0; denominator 21; coverage 7/10 (70%); completeness 7/10 (70%).

Verified scored-dimension risk: 38.1%, calculated from 7 independent scored dimensions; 0 additional scored dimensions are NESTED; 7 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.

ARTIFACT 9: NETWORK MAP

Receipts as in SECTION A (RECEPTION-1, 50 work nodes, 113 edges, density 113/2450, input coverage 50/50, COMPUTED-FROM-RETRIEVED). Founding-cluster nodes: N06, N09, N19, N26, N28, N29, N33, N36, N38, N41. Closure beyond RECEPTION-1 is not established and not excluded.

Edge list (CSV, citing,cited):

```
source,target
N02,N08
N03,N06
N04,N01
N04,N34
N05,N08
N06,N19
N08,N19
N09,N19
N09,N41
N09,N49
N10,N01
N11,N19
N12,N02
N12,N05
N13,N06
N13,N23
N14,N06
N14,N28
N15,N19
N16,N06
N16,N09
N16,N19
N16,N31
N16,N33
N16,N38
N16,N41
N16,N49
N17,N06
N17,N13
N17,N41
N20,N01
N20,N09
N20,N19
N20,N23
N20,N34
N21,N01
N21,N16
N21,N31
N21,N41
N23,N08
N23,N19
N24,N22
N25,N01
N25,N06
N25,N10
N25,N19
N25,N28
N26,N06
N26,N13
N26,N19
N26,N31
N26,N49
N28,N19
N28,N38
N30,N41
N31,N01
N31,N23
N31,N41
N32,N01
N32,N10
N32,N40
N33,N06
N33,N41
N34,N01
N34,N19
N36,N06
N36,N19
N36,N38
N37,N06
N37,N09
N37,N16
N37,N19
N37,N21
N37,N31
N37,N33
N37,N41
N37,N47
N38,N06
N38,N19
N39,N30
N40,N01
N40,N10
N40,N19
N40,N34
N41,N06
N41,N19
N43,N06
N43,N33
N44,N06
N44,N19
N45,N09
N45,N16
N45,N19
N45,N26
N45,N47
N46,N19
N47,N06
N47,N16
N47,N19
N47,N21
N47,N31
N47,N33
N47,N41
N47,N49
N48,N16
N48,N19
N48,N37
N48,N41
N48,N45
N48,N47
N50,N16
N50,N26
N50,N30
```

COMPLETION LEDGER

| Required heading | Exact heading present? | Status: completed / N/A / omitted | Reason or output location |
|---|---|---|---|
| `PRE-AUDIT CLAIM CONFIRMATION` | yes | completed | this file |
| `SECTION A0: CORPUS REGISTER AND SOURCE ELIGIBILITY` | yes | completed | this file |
| `SECTION A: CITATION NETWORK STRUCTURE AND CARTEL DETECTION` | yes | completed | this file |
| `SECTION B: EVIDENCE TYPE CODING` | yes | completed | this file |
| `SECTION C: CITATION POLARITY AND CLAIM USE` | yes | completed | this file |
| `SECTION D: CLAIM MUTATION TRACKING` | yes | completed | this file |
| `SECTION E: ADJACENT FIELD ENGAGEMENT / NEGLECT` | yes | completed | this file |
| `SECTION F: HUB DEPENDENCY AND REVIEW-PAPER LAUNDERING` | yes | completed | this file |
| `SECTION G: PATTERN RECOGNITION AND RATCHET BEHAVIOR` | yes | completed | this file |
| `SECTION H: IGNORED CRITIQUE AND NON-UPTAKE` | yes | completed | this file |
| `SECTION I: AUTHOR, INSTITUTION, JOURNAL, AND FUNDING CLUSTERING` | yes | completed | this file |
| `SECTION J: FALSE-POSITIVE AND BASELINE CHECK` | yes | completed | this file |
| `SECTION J2: THE CONCEDE TEST` | yes | completed | this file |
| `SECTION K0: EVIDENCE SUFFICIENCY LEDGER` | yes | completed | this file |
| `SECTION K: CARTEL-RISK SCORING` | yes | completed | this file |
| `ARTIFACT 1: TOP 15 CITATION SPINE TABLE` | yes | completed | this file |
| `ARTIFACT 2: FOUNDING CLUSTER TABLE` | yes | completed | this file |
| `ARTIFACT 3: RECENT 5-YEAR CITATION BEHAVIOR TABLE` | yes | completed | this file |
| `ARTIFACT 4: CITATION POLARITY TABLE` | yes | completed | this file |
| `ARTIFACT 5: CLAIM MUTATION TABLE` | yes | completed | this file |
| `ARTIFACT 6: ADJACENT-LITERATURE NEGLECT TABLE` | yes | completed | this file |
| `ARTIFACT 7: CRITIQUE-UPTAKE TABLE` | yes | completed | this file |
| `ARTIFACT 8: CARTEL-RISK SCORECARD` | yes | completed | this file |
| `ARTIFACT 9: NETWORK MAP` | yes | completed | this file |
| `COMPLETION LEDGER` | yes | completed | this file |
| `ARTIFACT 10: FINAL VERDICT` | yes | completed | this file |
| `FINAL SECTION: STANDARDIZED FINDING TABLE` | yes | completed | this file |

Gate result: PASS.

ARTIFACT 10: FINAL VERDICT

- Main founding cluster: the four target authors; 10/50 RECEPTION-1 works, receiving 62/113 internal edges
- Main amplification hub: N19 Muraven, Tice & Baumeister 1998 and N06 Muraven & Baumeister 2000 (founding-cluster works); N09 is the hub most cited by recent works
- Main proxy problem: behavioural persistence differences restated as a shown resource drain (I10, I11)
- Main adjacent fields neglected: learned helplessness (same outcome) and experimenter expectancy at the reference-list level (I21); text engagement not assessed (I22)
- Main claim mutation: not graded (target body not read); candidate certainty upgrades recorded (A08 "over 300 independent studies", X19, X20)
- Most important ignored critique: the 2016 RRR, disputed by the founding authors (BV-E1); later partly accepted (VO-E3)
- Decisive test missing: a high-powered direct replication of the food-temptation → persistence paradigm (0/59 in the locked search); the general effect has been tested (I13, I14)
- Verified risk score: 8/21
- Verified scored-dimension risk rate: 38.1
- Independent scored dimensions: 7
- Nested scored dimensions: 0
- Verified risk denominator: 21
- Evidentiary coverage: 7/10 (70%)
- Execution completeness: 7/10 (70%)
- Dimension inventory: 7 INDEPENDENT SCORED + 0 NESTED SCORED + 0 UNINFORMATIVE + 3 UNASSESSED + 1 N/A
- Unscored dimensions and reasons: Review-hub laundering UNASSESSED (I26); Claim mutation UNASSESSED (I12); Model non-updating UNASSESSED (link 4); Intervention-evidence ratchet N/A
- N-of-M scope statement: Verified scored-dimension risk: 38.1%, calculated from 7 independent scored dimensions; 0 additional scored dimensions are NESTED; 7 of 10 applicable dimensions were assessed. This describes average concern among independently aggregated dimensions; it is not a full-coverage estimate of network-wide risk or breadth.
- Arithmetic band position: >20%–40% (normal field clustering with some weaknesses)
- Risk band: >20%–40% normal field clustering with some weaknesses — computed over 7 independent scored dimensions; breadth requirement PASSED. PROVISIONAL: coverage meets the 70% gate exactly and only if five review items resolve (20% without them); no closure or laundering label is supported because review-hub laundering, claim mutation and model non-updating are UNASSESSED.
- Mechanism label: a founding-cluster-centred reception: the founding authors' own works are the main internal hubs and recent citers keep using the limited-resource model as a premise, while independent preregistered multi-site tests of the general effect found near-zero to small effects and the founding cluster has only partly updated; the field-6 paradigm itself was not re-tested at scale
- Formal-label gate status: coverage 70% declared (exactly at the PROVISIONAL threshold); 20% if open review items are withdrawn; MET ONLY IF REVIEW ITEMS RESOLVE
- Load-bearing finding(s): Finding 1 (field-6 magnitude NARROWS); Finding 2 (founding-cluster-centred reception)
- Concede-test result: field 6 NARROWED by Finding 1 (scope loss major); Findings 2–7 SURVIVE
- Failure location: PAPER (Findings 1, 6); CITATION (Findings 2, 3, 4, 5); MODEL-RETRIEVAL (Finding 7)
- Best formal label: normal field clustering with some weaknesses (the >20%–40% band; field size is not small), provisional at the 70% gate; no cartel or laundering label supported
- Confidence level: Low to moderate. CITATION CONTEXT COVERAGE: RECEPTION-1 22/50; CITATION CONTEXT COVERAGE: RECENT-1 12/25; CITATION CONTEXT COVERAGE: ADJUDICATION-1 21/59
- What evidence would change this assessment: the target full text from an authorized source; the 8 uninspectable sampled RECEPTION-1 passages; the 13 uninspected RECENT-1 passages; the 2024 status review (R05); inspected passages citing N06, N09 or N16; a direct high-powered replication of the food-temptation paradigm
- Density inference scope: RECEPTION-1 only (OpenAlex cites:W2123817056, top 50 records, executed 2026-11-05T11:31:57Z); closure is not established and not excluded beyond the defined corpus

FINAL SECTION: STANDARDIZED FINDING TABLE

Finding 1

| Field | Entry |
|---|---|
| Finding | The field-6 paradigm has no high-powered direct replication in the locked search, and preregistered multi-site tests of the general effect find near-zero to small effects, so the large field-6 effect does not hold as a general result. |
| Target claim | In Experiment 1, participants who ate radishes while resisting chocolate persisted about 8.35 min on unsolvable puzzles vs 18.90 (chocolate) and 20.86 (no food); N ≈ 67; t(44) = 6.03 (d ≈ 1.8) radish vs chocolate. |
| What was measured | full texts of N45 (RRR-E1, RRR-E2), A03 (VO-E2, VO-E3), A01 (DA-E2); ADJUDICATION-1 screen; TA-E1 |
| What was claimed | size and generality of the depletion effect |
| Failure mode | other: unreplicated paradigm with a small general effect |
| Severity | major |
| Concede test | NARROWS |
| Scope loss if NARROWS | major — surviving claim: in one lab with about 22 per cell, radish eaters quit unsolvable puzzles sooner; the magnitude is not supported as a general effect |
| Evidence | I11; I13; I14; I18; RRR-E2; VO-E2; DA-E2. |
| Evidence type | primary study |
| Verification state | FULL-TEXT-CONFIRMED; CROSS-SOURCE-CONFIRMED; field-6 numbers PROVISIONAL |
| Possible innocent explanation | The multi-site tests used other first tasks (e-crossing, writing) and the RRR cited the original task's experimenter involvement; the original paradigm may behave differently. |
| What would weaken this | A preregistered high-powered replication of the food-temptation paradigm with an effect near the original. |
| Failure location | PAPER — small single-lab cells |
| Status | confirmed |

Finding 2

| Field | Entry |
|---|---|
| Finding | The reception is founding-cluster-centred: 10/50 RECEPTION-1 works are by the target authors and receive 62/113 internal edges, though overall density is low. |
| Target claim | In Experiment 1, participants who ate radishes while resisting chocolate persisted about 8.35 min on unsolvable puzzles vs 18.90 (chocolate) and 20.86 (no food); N ≈ 67; t(44) = 6.03 (d ≈ 1.8) radish vs chocolate. |
| What was measured | RECEPTION-1 edge list (50/50 reference lists) and authorships |
| What was claimed | founding-cluster dominance and closure |
| Failure mode | founding-cluster dominance |
| Severity | moderate |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I01; I02; I03; Section A receipts. |
| Evidence type | author inference |
| Verification state | RECEPTION-CONFIRMED |
| Possible innocent explanation | Founding authors are prolific in a large field; their reviews are natural hubs. |
| What would weaken this | A matched comparison graph showing the same in-edge concentration for other influential papers. |
| Failure location | CITATION — network structure |
| Status | confirmed |

Finding 3

| Field | Entry |
|---|---|
| Finding | Recent citers rely on founding-cluster work and use the limited-resource model as a premise: 13/25 cite founding work beyond the target; 6/12 inspected passages use it as a premise. |
| Target claim | MAP GAP: this finding targets downstream use of the target, not map field 6. |
| What was measured | RECENT-1 reference lists (25/25); 12/25 passages |
| What was claimed | recent-paper dependence |
| Failure mode | other: recent premise recycling |
| Severity | moderate |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I04; I09; I08 (INSUFFICIENT); CTX-E25; CTX-E27; CTX-E30. |
| Evidence type | author inference |
| Verification state | RECEPTION-CONFIRMED; FULL-TEXT-CONFIRMED (excerpts); PROVISIONAL |
| Possible innocent explanation | Ranking by citation count favours applied reviews; premise use may be framed with caveats elsewhere. |
| What would weaken this | Full recent passages showing caveats, or a random recent sample with less premise use. |
| Failure location | CITATION — recent reception |
| Status | provisional |

Finding 4

| Field | Entry |
|---|---|
| Finding | Several citing passages state resource drain as shown, where the target abstract states it as an inference. |
| Target claim | MAP GAP: this finding targets downstream restatements of the target, not map field 6. |
| What was measured | S2 contexts CTX-E2, E5, E10, E11, E19, E22, E25, E27 against TA-E1 |
| What was claimed | proxy-to-construct mismatch |
| Failure mode | proxy-to-construct mismatch |
| Severity | minor |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I10; I11; I12 (INSUFFICIENT); TA-E1. |
| Evidence type | author inference |
| Verification state | FULL-TEXT-CONFIRMED (excerpts); ABSTRACT for target; PROVISIONAL |
| Possible innocent explanation | Excerpts are short; the target body may state the resource more strongly than the abstract. |
| What would weaken this | The target full text stating the resource as demonstrated. |
| Failure location | CITATION — downstream restatement |
| Status | provisional |

Finding 5

| Field | Entry |
|---|---|
| Finding | Critique uptake is mixed: the founding authors disputed the RRR in 2016, and a founding-author co-signed multi-site test conceded in 2021 that the effect is less reliable than assumed. |
| Target claim | In Experiment 1, participants who ate radishes while resisting chocolate persisted about 8.35 min on unsolvable puzzles vs 18.90 (chocolate) and 20.86 (no food); N ≈ 67; t(44) = 6.03 (d ≈ 1.8) radish vs chocolate. |
| What was measured | full texts X17 (BV-E1), A03 (VO-E3) |
| What was claimed | critique uptake |
| Failure mode | critique non-uptake (partial) |
| Severity | minor |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I19; I20; I24 (NOT-ASSESSED); BV-E1; VO-E3. |
| Evidence type | author inference |
| Verification state | FULL-TEXT-CONFIRMED; PROVISIONAL |
| Possible innocent explanation | Disputing a manipulation check is a legitimate scientific response. |
| What would weaken this | The 2024 status review (R05) fully accepting or rejecting the null results. |
| Failure location | CITATION — uptake by the founding cluster |
| Status | provisional |

Finding 6

| Field | Entry |
|---|---|
| Finding | The target's reference list contains 0/15 locked adjacent sources and no learned-helplessness or experimenter-expectancy work, though both bear on the field-6 outcome. |
| Target claim | MAP GAP: this finding targets the source's engagement, not map field 6. |
| What was measured | raw/target_reflist_titles.json (57/58 resolved) against the Section E lock |
| What was claimed | adjacent-field neglect |
| Failure mode | adjacent-field neglect |
| Severity | minor |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I21; I22 (NOT-ASSESSED); Section E table. |
| Evidence type | author inference |
| Verification state | METADATA; PROVISIONAL |
| Possible innocent explanation | The text may address these rivals without citing the locked works; the lock picks the most-cited titles, not the most relevant. |
| What would weaken this | The target text discussing helplessness or expectancy explanations. |
| Failure location | PAPER — reference list |
| Status | provisional |

Finding 7

| Field | Entry |
|---|---|
| Finding | Retrieval limits bound this audit: the target body is not authorized-accessible, the random sample lost 8/12 passages, and OpenAlex records carry duplicates and a wrong year. |
| Target claim | MAP GAP: this finding targets the retrieval record, not map field 6. |
| What was measured | retrieval log; lock/SAMPLES_draw.txt; raw/target_work.json; ADJUDICATION-1 records |
| What was claimed | retrieval and record quality |
| Failure mode | other: retrieval and database record limits |
| Severity | moderate |
| Concede test | SURVIVES |
| Scope loss if NARROWS | N/A — SURVIVES |
| Evidence | I25; SAMPLE ATTRITION I05 4/12 and RECENT-1 coverage 12/25 (SECTION K0, recorded facts, not inferences). |
| Evidence type | author inference |
| Verification state | RECEPTION-CONFIRMED |
| Possible innocent explanation | Paywalls and database merges are general, not specific to this paper. |
| What would weaken this | Authorized access to the target and to the sampled passages. |
| Failure location | MODEL-RETRIEVAL — access and database record |
| Status | confirmed |
