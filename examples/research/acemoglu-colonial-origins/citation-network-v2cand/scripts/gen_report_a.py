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
