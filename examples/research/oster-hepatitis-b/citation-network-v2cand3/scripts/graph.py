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
indeg=collections.Counter(v for _,v in E); print('indeg',indeg.most_common(8))
print('nodes citing >=1 other', len({u for u,_ in E}))
S=set(E); print('reciprocal', sum(1 for u,v in S if (v,u) in S)//2)
osterN=[lab[w['id'].split('/')[-1]] for w in R if any('Oster' in a['author']['display_name'] for a in w['authorships'])]
print('oster-authored',osterN, 'in-edges to them', sum(1 for _,v in E if v in osterN))
print('EDGES', '; '.join(f"{u} -> {v}" for u,v in E))
LL='W1994568240'; O10='W2042478072'; DG05='W1982754848'; DG06='W2119714514'
for name,ws in [('REC post-2008',[w for w in R if w['publication_year']>=2009]),('RECENT',json.load(open('raw/recent1_top25.json'))['results'])]:
    for k,t in [('LinLuoh',LL),('Oster2010',O10),('DasGupta05',DG05),('DasGupta06',DG06)]:
        c=[w['id'].split('/')[-1] for w in ws if any(r.endswith(t) for r in w['referenced_works'])]
        print(name,k,f"{len(c)}/{len(ws)}",c)
    either=[w['id'].split('/')[-1] for w in ws if any(r.endswith(LL) or r.endswith(O10) for r in w['referenced_works'])]
    print(name,'either LL or O10',len(either),len(ws), 'refs-empty', sum(1 for w in ws if not w['referenced_works']))
json.dump({'nodes':lab,'edges':E},open('raw/graph_edges.json','w'),indent=0)
