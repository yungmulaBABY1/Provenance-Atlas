import json,collections
R=json.load(open('raw/reception1_top50.json'))['results']
ids=[w['id'].split('/')[-1] for w in R]; lab={i:f"N{k:02d}" for k,i in enumerate(ids,1)}
E=[];tot=0
for w in R:
    u=w['id'].split('/')[-1]; refs=[r.split('/')[-1] for r in w['referenced_works']]; tot+=len(refs)
    for v in refs:
        if v in lab and v!=u: E.append((lab[u],lab[v]))
n=len(ids); print('nodes',n,'edges',len(E),'den',n*(n-1),'density %.2f%%'%(100*len(E)/(n*(n-1))),'refs total',tot)
print('nodes with refs', sum(1 for w in R if w['referenced_works']))
indeg=collections.Counter(v for _,v in E); print('indeg',indeg.most_common(10))
print('nodes citing >=1 other', len({u for u,_ in E}))
S=set(E); print('reciprocal', sum(1 for u,v in S if (v,u) in S)//2)
bN=[lab[w['id'].split('/')[-1]] for w in R if any('Baumeister' in a['author']['display_name'] for a in w['authorships'])]
print('baumeister-coauthored',bN,'in-edges to them',sum(1 for _,v in E if v in bN),'edges among them',sum(1 for u,v in E if u in bN and v in bN))
print('EDGES', '; '.join(f"{u} -> {v}" for u,v in E))
# founding cluster beyond target: Muraven 1998 (W2134469114), Muraven & Baumeister 2000 (W2113390049), Baumeister 2007 strength model (W2108897328)
FC={'Muraven1998':'W2134469114','MuravenB2000':'W2113390049','BVT2007':'W2108897328','Gailliot2007':'W2146569853','Hagger2010':'W2060763381'}
CR={'Hagger2016RRR':'W2499154041','Carter2015':'W1907223040','CarterMcC2014':'W2007393966','Inzlicht2012':'W2000141755','Kurzban2013':'W2164682760','Vohs2021':'W3119325546','Job2010':'W2118108696'}
for name,ws in [('REC post-2016',[w for w in R if w['publication_year']>=2017]),('RECENT',json.load(open('raw/recent1_top25.json'))['results'])]:
    print(name,'n',len(ws),'refs-empty',sum(1 for w in ws if not w['referenced_works']))
    for k,t in list(FC.items())+list(CR.items()):
        c=[w['id'].split('/')[-1] for w in ws if any(r.endswith('/'+t) for r in w['referenced_works'])]
        print('  ',name,k,f"{len(c)}/{len(ws)}",c)
json.dump({'nodes':lab,'edges':E},open('raw/graph_edges.json','w'),indent=0)
