import json,re,subprocess
from collections import Counter
L=json.load(open('out/ledger.json')); rows=L['rows']; sid=L['sid']
G=json.load(open('graph_v2cand.json'))
r1=json.load(open('raw/reception1_top50.json'))['results']; rc=json.load(open('raw/recent1_top25.json'))['results']
W=lambda u:u.split('/')[-1]
S=lambda w:sid[w]
edges=[tuple(e) for e in G['edges']]; team=G['team']
E=len(edges)
ex=[(a,b) for a,b in edges if 'N01' not in (a,b)]
team_x=[t for t in team if t!='N01']
toteam_x=sum(1 for a,b in ex if b in team_x)
indeg=Counter(b for a,b in edges); indeg_x=Counter(b for a,b in ex)
es=set(edges); recip=sorted({tuple(sorted(e)) for e in edges if (e[1],e[0]) in es})
cite_any=len({a for a,b in edges})
rec=G['recent']; fc_recent=[S(r[0]) for r in rec if r[2]]
rodrik_recent=sum(1 for r in rec if r[3]); gl_recent=sum(1 for r in rec if r[4]); al_recent=sum(1 for r in rec if r[5])
hb_recent=sum(1 for r in rec if set(r[2])&{'W1580107285','W2108614304'})
def corp(c): return [r for r in rows if c in r['mem'].split('+')]
def cnt(c,k): return Counter((r[k].split()[0] if k in('rel','acc') else r[k]) for r in corp(c))
INS={c:sum(r['ctx']=='INSPECTED' for r in corp(c)) for c in ['RECEPTION-1','RECENT-1','ADJUDICATION-1']}
HB=S('W2108614304'); HBC=S('W1580107285'); RD=S('W2994756033'); RDW=S('W1977433163'); GL=S('W2890314743'); EL=S('W3122513675'); DML=S('W3123436326'); HW=S('W1480274481'); REPLY=S('W3124131699')
LEVR=S('W2113844427'); LEVC=S('W1588189399'); DJO=S('W2104834906'); HID=S('W2064927380'); RZ=S('W3122778615')
SAMPLE=['W4223529822','W4292663674','W4292849668','W4319016949','W4387877962','W4391180104']; SAMP=sorted(S(w) for w in SAMPLE)
r1ins=[r['sid'] for r in corp('RECEPTION-1') if r['ctx']=='INSPECTED']
def comp(iid,c,col,key):
    cc=cnt(c,key); return f"COMPOSITION: {iid} | {col} | "+"; ".join(f"{k}={v}" for k,v in sorted(cc.items()))+f" | TOTAL={sum(cc.values())}"
uc=Counter()
for r in corp('RECEPTION-1'):
    if r['ctx']=='INSPECTED':
        for u in r['relat'].split('+'): uc[u]+=1
d=E/2450*100; dx=len(ex)/(49*48)*100; tshare=sum(1 for a,b in edges if b in team)
k=INS['RECEPTION-1']
X,Y=3,21; rate=X/Y*100
o=[]; P=o.append
full=subprocess.run(['git','-C','/workspace/Provenance-Atlas','rev-parse','b6d7869:prompts/research-analysis/2-citation-network.v2-candidate.txt'],capture_output=True,text=True).stdout.strip() or 'UNRESOLVED'
