"""Generate v2cand3/02c_citation_network_v2cand3.md for Baumeister et al. (1998) from raw/, lock/ and ledger rows.
Run from cn/: python3 scripts/build_ledger.py && python3 scripts/build_2c.py"""
import json, collections
R=json.load(open('raw/reception1_top50.json'))['results']
C=json.load(open('raw/recent1_top25.json'))['results']
TR=json.load(open('raw/target_refs.json'))['results'][0]
TRT=json.load(open('raw/target_reflist_titles.json'))['results']
rows=[tuple(r) for r in json.load(open('v2cand3/ledger_rows.json'))]
CT=json.load(open('v2cand3/ctx_ids.json')); CTX=CT['ctx']
bysid={r[0]:r for r in rows}
lab={w['id'][21:]:f'N{i:02d}' for i,w in enumerate(R,1)}
def refs(w): return {r[21:] for r in w['referenced_works']}
E=sorted({(lab[w['id'][21:]],lab[r[21:]]) for w in R for r in w['referenced_works'] if r[21:] in lab and r[21:]!=w['id'][21:]})
nodes=sorted(lab.values()); n=len(nodes); den=n*(n-1)
indeg=collections.Counter(v for u,v in E)
recip=sum(1 for u,v in E if (v,u) in E)//2
citing=len({u for u,v in E})
refs_total=sum(len(w['referenced_works']) for w in R)
F4=('Baumeister','Bratslavsky','Muraven','Tice')
def au(w): return [x['author']['display_name'] for x in w['authorships']]
FC=[lab[w['id'][21:]] for w in R if any(any(k in nm for k in F4) for nm in au(w))]
fc_in=sum(1 for u,v in E if v in FC); fc_out=sum(1 for u,v in E if u in FC and v in FC)
nonfc_to_fc=sum(1 for u,v in E if v in FC and u not in FC)
pct=lambda a,b: f'{100*a/b:.2f}%'
dens=pct(len(E),den)
lead=', '.join(f'{k} {v}' for k,v in indeg.most_common(8))
ws=R
# founding-cluster works identifiable in the corpora (beyond the target)
import glob
FCW={}
for f in ['raw/reception1_top50.json','raw/recent1_top25.json']+sorted(glob.glob('raw/adj1_Q*.json')):
    for w in json.load(open(f))['results']:
        if any(any(k in nm for k in F4) for nm in au(w)):
            sid=next((r[0] for r in rows if w['id'][21:] in r[1].split()[1:4]),'?')
            FCW[w['id'][21:]]=f"{sid} {au(w)[0].split()[-1]} {w['publication_year']}" 
CRIT={'W2499154041':'RRR 2016 (N45)','W2007393966':'Carter & McCullough 2014 (A09)','W3119325546':'Vohs et al. 2021 (A03)','W4256555852':'Vohs et al. 2021 preprint (A03)','W3014898655':'Dang et al. 2021 (A01)','W1989768409':'Carter & McCullough 2013 (A15)','W2794580436':'Friese et al. 2018 (A11)','W2588069705':'Blázquez-Rincón & Botella 2017 (A13)','W1964342261':'Lange & Eggert 2014 (A16)','W2003102314':'Chatzisarantis & Hagger 2014 (A19)'}
RIV={'W2000141755':'Inzlicht & Schmeichel 2012 (N47)','W2164682760':'Kurzban et al. 2013 (N37)','W2118108696':'Job et al. 2010 (A32)'}
HUBS={'W2113390049':'N06','W2108897328':'N09','W2134469114':'N19','W2060763381':'N16'}
recent_rows=[]
for i,w in enumerate(C,1):
    rf=refs(w); sid=f'R{i:02d}'
    recent_rows.append((sid,w,[v for k,v in FCW.items() if k in rf],[v for k,v in CRIT.items() if k in rf],[v for k,v in RIV.items() if k in rf],[v for k,v in HUBS.items() if k in rf]))
rc_fc=sum(bool(x[2]) for x in recent_rows); rc_crit=sum(bool(x[3]) for x in recent_rows); rc_riv=sum(bool(x[4]) for x in recent_rows)
rc_fc_nocrit=[x[0] for x in recent_rows if x[2] and not x[3]]
rc_hub={h:sum(k in refs(w) for w in C) for k,h in HUBS.items()}
post=[w for w in R if w['publication_year']>=2017]
post_crit=sum(bool(refs(w)&set(CRIT)) for w in post)
rec_N19=sum('W2134469114' in refs(w) for w in R); rec_N06=sum('W2113390049' in refs(w) for w in R)
def members(cid): return [r for r in rows if cid in r[2].split('+')]
def head(v): return v.split('(')[0].strip()
def comp(cid,ix):
    c=collections.Counter(head(r[ix]) for r in members(cid)); return '; '.join(f'{k}={v}' for k,v in sorted(c.items())), len(members(cid))
COMP={k:comp(*v) for k,v in {'I15':('ADJUDICATION-1',3),'I16':('ADJUDICATION-1',5),'I17':('RECEPTION-1',3)}.items()}
cov={c:(sum(r[7]=='INSPECTED' for r in members(c)),len(members(c))) for c in ('RECEPTION-1','RECENT-1','ADJUDICATION-1')}
insp_rec=[r[0] for r in members('RECEPTION-1') if r[7]=='INSPECTED']
insp_rcn=[r[0] for r in members('RECENT-1') if r[7]=='INSPECTED']
relc=collections.Counter(r[4] for r in members('RECEPTION-1') if r[7]=='INSPECTED')
relr=collections.Counter(r[4] for r in members('RECENT-1') if r[7]=='INSPECTED')
prem_r=[r[0] for r in members('RECENT-1') if r[4]=='PREMISE']
prem_n=[r[0] for r in members('RECEPTION-1') if r[4]=='PREMISE']
sample_ids=['N07','N09','N10','N11','N20','N27','N28','N39','N40','N41','N42','N44']
kept=[s for s in sample_ids if bysid[s][7]=='INSPECTED']
dl1=[r[0] for r in members('ADJUDICATION-1') if r[3].startswith('DIRECT (L1)')]
dirs=collections.Counter(r[3] for r in members('ADJUDICATION-1') if r[3].startswith('DIRECT'))
venue=collections.Counter(((w.get('primary_location') or {}).get('source') or {}).get('display_name') for w in R)
nodelist='; '.join(f"{lab[w['id'][21:]]}={w['id'][21:]}" for w in R)
edgelist='; '.join(f'{u} -> {v}' for u,v in E)
tref_ids={r[21:] for r in TR['referenced_works']}
secX=[r for r in rows if r[0][0]=='X' and 'Section E' in r[8]]
sec_cited=sum(r[1].split()[1] in tref_ids for r in secX)
c=lambda t: CTX[t]
json.dump(dict(E=len(E),dens=dens,FC=FC,fc_in=fc_in,nonfc_to_fc=nonfc_to_fc,indeg=indeg.most_common(12),cov=cov,relc=relc,relr=relr,COMP=COMP,kept=kept,rc_fc=rc_fc,rc_crit=rc_crit,rc_riv=rc_riv,rc_fc_nocrit=rc_fc_nocrit,rc_hub=rc_hub,post=len(post),post_crit=post_crit,rec_N19=rec_N19,rec_N06=rec_N06,sec_cited=sec_cited,dirs=dirs,venue=venue.most_common(6)),open('v2cand3/build_numbers.json','w'),indent=1,default=list)
exec(open('scripts/doc_template.py').read())
