"""Generate 02c_citation_network_v2cand3.md for Oster (2005) from raw/, lock/ and ledger rows.
Run from cn/: python3 scripts/build_ledger.py && python3 scripts/build_2c.py"""
import json, collections, hashlib
R=json.load(open('raw/reception1_top50.json'))['results']
C=json.load(open('raw/recent1_top25.json'))['results']
rows=json.load(open('out/ledger_rows.json'))
lab={w['id'][21:]:f'N{i:02d}' for i,w in enumerate(R,1)}
mrg=lambda x:'N09' if x=='N35' else x
# ---- graph (work level: N35 merged into N09) and record level
Erec=[]; 
for w in R:
    u=lab[w['id'][21:]]
    for r in w['referenced_works']:
        v=lab.get(r[21:])
        if v and v!=u: Erec.append((u,v))
E=sorted({(mrg(u),mrg(v)) for u,v in Erec if mrg(u)!=mrg(v)})
nodes=[l for l in sorted(set(lab.values())) if l!='N35']
n=len(nodes); den=n*(n-1)
indeg=collections.Counter(v for u,v in E)
recip=sum(1 for u,v in E if (v,u) in E)//2
citing=len({u for u,v in E})
ost=('N12','N24','N45'); ost_in=sum(1 for u,v in E if v in ost)
refs_total=sum(len(w['referenced_works']) for w in R if lab[w['id'][21:]]!='N35')
LL,O10,DG5,DG6='W1994568240','W2042478072','W1982754848','W2119714514'
def refs(w): return {r[21:] for r in w['referenced_works']}
ws=[w for w in R if lab[w['id'][21:]]!='N35']
cc=lambda ws,x: sum(x in refs(w) for w in ws)
either=lambda ws: sum(bool(refs(w)&{LL,O10}) for w in ws)
post=[w for w in ws if w['publication_year']>=2009]
# ---- ledger-derived numbers
def members(cid): return [r for r in rows if cid in r[2].split('+')]
def head(v): return v.split('(')[0].strip()
def comp(cid,ix):
    c=collections.Counter(head(r[ix]) for r in members(cid)); return '; '.join(f'{k}={v}' for k,v in sorted(c.items())), len(members(cid))
cov={c:(sum(r[7]=='INSPECTED' for r in members(c)),len(members(c))) for c in ('RECEPTION-1','RECENT-1','ADJUDICATION-1')}
insp_rec=[r[0] for r in members('RECEPTION-1') if r[7]=='INSPECTED']
relc=collections.Counter(r[4] for r in members('RECEPTION-1') if r[7]=='INSPECTED')
nodelist='; '.join(f"{l}={[w['id'][21:] for w in R][int(l[1:])-1]}"+('+W1581958734' if l=='N09' else '') for l in nodes)
edgelist='; '.join(f'{u} -> {v}' for u,v in E)
pct=lambda a,b: f'{100*a/b:.2f}%'
D=dict(n=n,den=den,ne=len(E),dens=pct(len(E),den),nrec=len(Erec),drec=pct(len(Erec),2450),recip=recip,citing=citing,ost_in=ost_in,refs_total=refs_total)
lead=', '.join(f'{k} {v}' for k,v in indeg.most_common(8))
# recent table rows
OST_BEYOND={'W2042478072':'Oster et al. 2010 (N45)','W2096320699':'Oster 2009 (N24)','W2100633408':'Oster 2009 (N12)'}
recent_rows=[]
for i,w in enumerate(C,1):
    sid=f'R{i:02d}'; rf=refs(w)
    beyond=[v for k,v in OST_BEYOND.items() if k in rf]
    adj=[n_ for k,n_ in ((LL,'Lin & Luoh 2008'),(O10,'Oster et al. 2010'),(DG5,'Das Gupta 2005'),(DG6,'Das Gupta 2006')) if k in rf]
    recent_rows.append((sid,w,beyond,adj))
rc_beyond=sum(bool(b) for _,_,b,_ in recent_rows); rc_LL=sum(LL in refs(w) for w in C); rc_O10=sum(O10 in refs(w) for w in C); rc_DG5=sum(DG5 in refs(w) for w in C)
COMP={k:comp(*v) for k,v in {'I15':('ADJUDICATION-1',3),'I16':('ADJUDICATION-1',5),'I17':('RECEPTION-1',3)}.items()}
sample_ids=['N07','N09','N10','N11','N20','N27','N28','N39','N40','N41','N42','N44']
kept=[s for s in sample_ids if any(r[0]==s and r[7]=='INSPECTED' for r in rows)]
open('out/build_numbers.json','w').write(json.dumps(dict(D=D,lead=lead,cov=cov,relc=relc,COMP=COMP,kept=kept,cc_all=[cc(ws,LL),cc(ws,O10),cc(ws,DG5),cc(ws,DG6),either(ws)],cc_post=[len(post),cc(post,LL),cc(post,O10),cc(post,DG5),either(post)],recent=[rc_beyond,rc_LL,rc_O10,rc_DG5],indeg=indeg.most_common(12)),indent=1,default=list))
exec(open('scripts/doc_template.py').read())
