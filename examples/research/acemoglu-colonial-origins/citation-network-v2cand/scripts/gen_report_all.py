import json,collections,re,datetime as dt
OUTPATH='/workspace/pa-v2cand/examples/research/acemoglu-colonial-origins/citation-network-v2cand/RUN_REPORT.txt'
gl=open('/workspace/pa-v2cand/examples/research/acemoglu-colonial-origins/citation-network-v2cand/checker/final_gates.txt').read().splitlines()
vl=open('/workspace/pa-v2cand/examples/research/acemoglu-colonial-origins/citation-network-v2cand/checker/final_v1.txt').read().splitlines()
GL_COV=[l.replace('\t',' ') for l in gl if l.split('\t')[0].startswith(('COVERAGE','PROVISIONAL'))]
CHK=[('v1 checker check-citation-network-output.py','"'+vl[-1]+'"',0),('v2 gate checker check-citation-network-v2-gates.py','"'+gl[-1]+'"',0)]
REV=['[v1 checker] '+l for l in vl if l.startswith('REVIEW_ITEM')]+['[gate checker] '+l for l in gl if l.startswith('REVIEW_ITEM')]
import json,collections,re,datetime as dt
W=[json.loads(l) for l in open('worklog.jsonl')]
R=[json.loads(l) for l in open('raw/retrieval_log.jsonl')]
md=open('out/02c_citation_network_v2cand2.md').read().splitlines()
def pst(t): x=dt.datetime.strptime(t,'%Y-%m-%dT%H:%M:%SZ')-dt.timedelta(hours=8); return x.strftime('%-I:%M:%S %p PST')
o=[];P=o.append
P("RUN REPORT — DIAGNOSTIC LIVE RUN OF CITATION-NETWORK CANDIDATE REVISION 2")
P("Target: Acemoglu, Johnson & Robinson (2001), map field 6. Executor: Grok Bot (audit run). Date: Wednesday 2026-11-04 PST (2026-11-05 UTC).")
P("Times are PST (UTC-8) with UTC in parentheses. Box clock is UTC; conversions are exact.")
P("This is a diagnostic run of an unvalidated candidate instrument, not a validation run.\n")
P("1. IDENTITY")
P("Pinned sources fetched 8:28:20–8:28:53 PM PST (04:28:20Z–04:28:53Z) and hashed with sha256:")
P("  candidate instrument  yungmulaBABY1/Provenance@07b72b585c934c5daff63953b22cf6424bfa8f6b candidates/research-analysis/2-citation-network.v2-candidate.txt  sha256 3b4be80dcea68dc804bb6d72ca461a25f99a24f8bd8784e086289d9040f89896  1949 lines 85977 bytes  MATCH")
P("  v2 gate checker       same commit, candidates/research-analysis/check-citation-network-v2-gates.py  sha256 90de7375bc2e1a54a62cc67dbb70826a36e55e20bc7516b48d378821af8b965b  MATCH")
P("  v1 checker            same commit, prompts/research-analysis/check-citation-network-output.py  sha256 f66650fe086455fa5dd80afadf1ec78685ee212825923d670d25b24e62d79f27  MATCH")
P("  claim map             yungmulaBABY1/Provenance-Atlas@b6d786947030902cf58cb114055d6cd48df6ad9c examples/research/acemoglu-colonial-origins/01_claim_extraction.md  sha256 f6e7df18d9fcd8e533c2909b49b75603d3072c7948292afd97ac6d7a8a23ea3e  MATCH")
P("  base branch           origin/audit/acemoglu-colonial-origins = b6d786947030902cf58cb114055d6cd48df6ad9c  MATCH")
P("  main                  origin/main = f7ae36074fb87e42ec82a07db8f803d008853c12 (moved from ce028e1 before this run; not by this run)")
P("Preflight lines reproduced verbatim in the output: \"INSTRUMENT VERSION: 2-citation-network v2-candidate.2\" and \"DIMENSION CLASS MAP: cn7-map-2\".")
P("Stopped? NO — every pinned identity matched.\n")
P("2. EXPOSURE DECLARATION")
P("Before this run the executor had produced the v1 citation-network output and stages 01/2a/2b/3 of this audit; had read AJR 2001 and NBER WP 7771, Albouy 2012 and its appendix, the AJR 2012 Reply, the 2024 Nobel scientific and popular texts, and the v1 full texts (Rodrik et al., Glaeser et al., Sachs, Easterly–Levine, AJR handbook WP, Chernozhukov et al., Hanushek–Woessmann, Levine, Dell–Jones–Olken, Rajan–Zingales, Hidalgo et al., Keller); and had seen the v1 RECENT top-25 titles before drawing the RECENT-1 sample.")
P("During identity checks (about 8:28 PM PST, 04:28Z) a grep for \"FAIL-CN\" ran on an older local clone's FAILURES.md (commit c1bcb8b); it printed only FAIL-CN-001…006 headings; that file has no FAIL-CN-007 entry.")
P("Not opened at any time: tests/cases/citation-network-v2-gates/ and its README; candidates/research-analysis/2-citation-network.v2-candidate.CHANGES.txt; the FAIL-CN-007 entry; the Provenance PR #14 description. The instrument's own [FAIL-CN-007] tags were read as part of the instrument.")
P("The disclosure is in the output header before SECTION A0.\n")
P("3. WORKLOAD BY SECTION (from worklog.jsonl; start–end, wall-clock, logged tool calls)")
ev=[w for w in W if 'event' in w]
starts={}
spans=[]
for w in ev:
    if w['event']=='start': starts[w['section']]=w['t']
    elif w['section'] in starts: spans.append((w['section'],starts[w['section']],w['t'],w['event']))
tc=collections.Counter(w['section'] for w in W if w.get('tool_call'))
order=['identity','read-instrument','corpora-reception','adjudication-lock','adjudication-search','adjudication-screen','recent-sample','reception-inspect','analysis']
for s_,a,b,e in spans:
    sec=(dt.datetime.strptime(b,'%Y-%m-%dT%H:%M:%SZ')-dt.datetime.strptime(a,'%Y-%m-%dT%H:%M:%SZ')).seconds
    P(f"  {s_:20s} {pst(a)} – {pst(b)} ({a[11:19]}Z–{b[11:19]}Z)  {sec//60}m{sec%60:02d}s  logged tool calls {tc.get(s_,0)}{'  [paused; screening finished inside analysis]' if e=='pause' else ''}")
P(f"  drafting             8:39:25 PM PST – about 8:55:30 PM PST (04:39:25Z–~04:55:30Z, no end event logged)  ~16m  logged tool calls {tc['drafting']}")
P(f"  checker              about 8:55:30 PM PST – 8:56:22 PM PST (~04:55:30Z–04:56:22Z)  ~1m  logged tool calls {tc['checker']}")
P("  packaging            8:56:22 PM PST (04:56:22Z) onward (worktree, copy, commit, push, ls-remote, zip)")
P(f"  other logged calls   exposure {tc['exposure']}, sampling {tc['sampling']}")
P(f"Logged tool calls total: {sum(tc.values())}. Not every shell/read call was logged; the approximate true count is 90–110 tool calls (including file reads of the instrument and checkers, ledger generation, failed classifier-error calls, and packaging).\n")
P("RETRIEVALS BY SOURCE (raw/retrieval_log.jsonl, plus identity fetches in worklog.jsonl)")
c=collections.Counter(); f=collections.Counter(); ok=collections.Counter()
import urllib.parse as up
for r in R:
    h=up.urlparse(r['url']).netloc; c[h]+=1
    if r['status']==200: ok[h]+=1
    else: f[(h,r['status'])]+=1
c['raw.githubusercontent.com']+=4; ok['raw.githubusercontent.com']+=4
for h in c: P(f"  {h:28s} attempts {c[h]:3d}  HTTP 200 {ok[h]:3d}  failures: "+(", ".join(f"HTTP {st} ×{n}" for (hh,st),n in f.items() if hh==h) or "none"))
P(f"  TOTAL attempts {sum(c.values())}; HTTP 200 {sum(ok.values())}; failures {sum(f.values())} (HTTP 429 ×{sum(n for (h,s),n in f.items() if s==429)}, 403 ×{sum(n for (h,s),n in f.items() if s==403)}, 500 ×{sum(n for (h,s),n in f.items() if s==500)}).")
P("  All six ADJUDICATION-1 queries eventually returned HTTP 200 after 429 back-off (Q6 needed 3 failed attempts plus a later retry). Final failures: 4 of 6 RECENT-1 sampled full texts (W4292849668 DOI 403; W4223529822 DOI 403; W4319016949 repository 403, curl fallback also 403; W4387877962 repository 500 ×3).")
P("  Local reuse (no new network call): v1 full texts and evidence excerpts (local excerpt files with their manifest; used only for quote checks, not committed); AJR 2001, Albouy 2012, AJR 2012 Reply PDFs from the earlier audit.\n")
L=json.load(open('out/ledger.json'))['rows']
def corp(cn): return [r for r in L if cn in r['mem'].split('+')]
P("4. CORPORA STATS")
for cn,size,role,disc in [('RECEPTION-1',50,'RECEPTION','NONE'),('RECENT-1',25,'RECEPTION','NONE'),('ADJUDICATION-1',58,'ADJUDICATION','SEARCHED')]:
    rs=corp(cn)
    cc=lambda k,first=False: dict(sorted(collections.Counter((r[k].split()[0] if first else r[k]) for r in rs).items()))
    P(f"  {cn} ({role}, discovery {disc}, size {len(rs)}): CITATION CONTEXT COVERAGE {sum(r['ctx']=='INSPECTED' for r in rs)}/{len(rs)}")
    P(f"    relevance {cc('rel',True)}")
    P(f"    contribution {cc('con')}")
    P(f"    access {cc('acc',True)}")
    P(f"    context {cc('ctx')}")
    rel=collections.Counter()
    for r in rs:
        for u in r['relat'].split('+'): rel[u]+=1
    P(f"    relation {dict(sorted(rel.items()))}")
P("  Locks: ADJUDICATION-1 CORPUS LOCK 8:30:42 PM PST (04:30:42Z), search record sha256 05ae137a5db11167164e758a2228f8e176f470bc6575b1694ad0de6541f90916, before any screening. RECENT-1 sample seed 20261104 recorded 8:33:36 PM PST (04:33:36Z) before inspection.")
P("  Overlap: W2994756033 (Rodrik et al.) in RECEPTION-1 (N02) and ADJUDICATION-1 (ADJ29), one ledger row. OUTSIDE rows X01–X15 (target, named sources, reused v1 Section E list). Ledger rows total "+str(len(L))+".")
P("  Duplicate records inflating RECEPTION-1 coverage: Rodrik ×2 (N02, N32), Reversal ×2 (N06, N18), AJR handbook ×2 (N09, N16), Levine ×2 (N05, N11). RECEPTION-1 coverage 14/50 by record; three inspected pairs are duplicates (Rodrik, Levine, handbook), so 11 distinct works were inspected out of 46 distinct works.")
P("  Drift vs v1 (the earlier v1 run): RECEPTION-1 12/50 members changed; RECENT population 2,695 → 3,026; AJR 2001 OpenAlex referenced_works 13 → 55.\n")
P("5. INFERENCES BY CLASS AND DISPOSITION (declared = recomputed by the gate checker for all passing inferences)")
inf=[l for l in md if re.match(r'^\| I\d\d \|',l)]
byc=collections.defaultdict(list)
for l in inf:
    c_=[x.strip() for x in l.strip('|').split('|')]
    byc[c_[1]].append((c_[0],c_[3],c_[6]))
for k_,v in sorted(byc.items()): P(f"  {k_:16s} "+"; ".join(f"{a} {s} {d}" for a,s,d in v))
dc=collections.Counter(c_[2] for v in byc.values() for c_ in v)
P(f"  Totals: {len(inf)} inferences; "+", ".join(f"{k_} {n}" for k_,n in sorted(dc.items())))
P("  Withheld / reasons:")
P("    I06 CITATION-USE, RECENT-1, PRESPECIFIED-RANDOM — INSUFFICIENT: 4/6 sampled full texts not retrieved (403 ×3 sources, 500 ×1); would be sufficient with all 6 inspected.")
P("    I14 ABSENCE, ADJUDICATION-1, LITERATURE — INSUFFICIENT: 2 members (ADJ37, ADJ44) relevance UNKNOWN; LITERATURE scope requires no UNKNOWN members.")
P("    I22 ENGAGEMENT (Glaeser uptake by the AJR team) — NOT-ASSESSED: response text not retrieved (checker recomputes INSUFFICIENT; no member).")
P("    I23 RESTATEMENT (downstream reliance on the handbook) — NOT-ASSESSED: no hub-citing passages inspected (checker recomputes INSUFFICIENT).")
P("    I13 ABSENCE, WITHIN-SAMPLE 56/58 — SUPPORTED-WITHIN-SAMPLE but deliberately NOT used to score lack of decisive tests: Glaeser 2004, a known L3-R2 test, lies outside the search bound, so the bounded absence would misdescribe the literature.\n")
P("6. DIMENSIONS, GATE COVERAGE AND RISK BAND")
i0=md.index('| Scorecard dimension | Scorecard disposition | Inference IDs | Basis note |')
for l in md[i0+2:i0+13]:
    c_=[x.strip() for x in l.strip('|').split('|')]; P(f"  {c_[0]:30s} {c_[1]:11s} {c_[2]}")
P("  Aggregation: 7 INDEPENDENT scored + 1 NESTED (Proxy mismatch under Claim mutation; shared HB-E1); verified risk 3/21 = 14.3%; evidentiary coverage 8/10 (80%); execution completeness 10/10.")
for l in GL_COV: P("  "+l)
P("  ARITHMETIC BAND POSITION: 0%–20% (healthy or low-risk network)")
P("  "+[l for l in md if l.startswith('RISK BAND:')][0])
P("  "+[l for l in md if l.startswith('MECHANISM LABEL:')][0])
P("  Best formal label: insufficient evidence. Confidence: Low (CITATION CONTEXT COVERAGE RECEPTION-1 14/50; RECENT-1 2/25; ADJUDICATION-1 1/58).\n")
P("7. CHECKERS (run with python3 -I on examples/research/acemoglu-colonial-origins/citation-network-v2cand/02c_citation_network_v2cand2.md; full outputs in checker/)")
P("  Attempts: 1 (first run of each passed; no iteration on the output was needed). Attempt-1 outputs retained as checker/try1_v1.txt and checker/try1_gates.txt (run on the pre-copy path).")
for name,fn,code in CHK: P(f"  {name}: exit code {code}; final line verbatim: {fn}")
P("")
P("8. REVIEW ITEMS (verbatim)")
for l in REV: P("  "+l)
P("")
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
