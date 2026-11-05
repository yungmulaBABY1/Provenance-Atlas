import json,hashlib
W=lambda u:u.split('/')[-1]
r1=json.load(open('raw/reception1_top50.json'))['results']; rc=json.load(open('raw/recent1_top25.json'))['results']
ids=[W(x['id']) for x in r1]; idx={w:f'N{i:02d}' for i,w in enumerate(ids,1)}
edges=[]; nref=0; noref=[]
for x in r1:
    refs=set(W(r) for r in x.get('referenced_works') or []); nref+=len(refs)
    if not refs: noref.append(idx[W(x['id'])])
    for r in refs:
        if r in idx and r!=W(x['id']): edges.append((idx[W(x['id'])],idx[r]))
n=len(ids); E=len(edges)
indeg={}; [indeg.__setitem__(b,indeg.get(b,0)+1) for a,b in edges]
AJRAUTH={'A5037524418','A5017474418'}  # placeholder, recomputed below by name
def ajr(x): return any(any(k in (a['author']['display_name'] or '') for k in ['Acemoğlu','Acemoglu','Simon Johnson','James A. Robinson','James Robinson']) for a in x['authorships'])
team=[idx[W(x['id'])] for x in r1 if ajr(x)]
toteam=sum(1 for a,b in edges if b in team)
FC={'W3125412951','W3021593216','W1568632324','W1580107285','W2108614304','W3124131699','W1550020960'}
rec=[]
for x in rc:
    refs=set(W(r) for r in x.get('referenced_works') or [])
    rec.append((W(x['id']),len(refs),sorted(refs&FC),('W2994756033' in refs or 'W1977433163' in refs),('W2890314743' in refs),('W1969918011' in refs)))
out=dict(n=n,E=E,density=E/(n*(n-1)),noref=noref,total_refs=nref,team=team,edges_to_team=toteam,indeg=sorted(indeg.items(),key=lambda t:-t[1])[:10],edges=edges,
 node_list={v:k for k,v in idx.items()},recent=rec)
json.dump(out,open('graph_v2cand.json','w'),indent=0)
print({k:out[k] for k in ['n','E','density','noref','total_refs','team','edges_to_team','indeg']})
print('recent with FC beyond target:',sum(1 for r in rec if r[2]),'/',len(rec),' noref:',[r[0] for r in rec if r[1]==0])
for r in rec: print(r)
