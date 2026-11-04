import json
W=lambda u:u.split('/')[-1]
ajr=json.load(open('raw/ajr2001_work.json'))
top=json.load(open('raw/top50_citers.json'))['results']
rec=json.load(open('raw/recent5y_top25.json'))
KEY={'AJR2001':['W3124166904'],'REVERSAL2002':['W3125412951','W3021593216','W1568632324'],'AJR_HANDBOOK2005':['W1580107285','W2108614304'],
 'HALLJONES1999':['W3122705141','W2128423609','W2891061867'],'WNF2012':['W4292229879','W1508296537'],
 'GLAESER2004':['W2890314743'],'SACHS2003':['W2105278501','W3125747705'],'ALBOUY2012':['W1969918011'],'AJR_REPLY2012':['W3124131699','W1550020960'],
 'RODRIK2004':['W2994756033'],'EASTERLY_LEVINE2003':['W3122513675']}
LOCK={'F1a':'W139828295','F1b':'W2088758477','F2a':'W2618788771','F2b':'W1492460295','F3a':'W3121822366','F3b':'W2035652178','F4a':'W2165144879','F4b':'W1980412904','F6a':'W3121147769','F6b':'W2010235856'}
nodes=[('N00','W3124166904',ajr['display_name'],ajr['publication_year'],ajr['cited_by_count'],[W(x) for x in ajr['referenced_works']])]
for i,w in enumerate(top,1):
    nodes.append((f'N{i:02d}',W(w['id']),w['display_name'],w['publication_year'],w['cited_by_count'],[W(x) for x in w['referenced_works']]))
ids={n[1]:n[0] for n in nodes}
edges=[]
for nid,wid,t,y,c,refs in nodes:
    for r in refs:
        if r in ids and r!=wid: edges.append((nid,ids[r]))
top_only=[e for e in edges if e[1]!='N00' and e[0]!='N00']
nz=[n for n in nodes[1:] if n[5]]
print('nodes',len(nodes),'top50 with nonempty refs',len(nz),'empty refs',[n[0] for n in nodes[1:] if not n[5]])
print('edges incl AJR',len(edges),'edges to N00',sum(1 for e in edges if e[1]=='N00'),'edges among top50',len(top_only))
outdeg={};indeg={}
for a,b in top_only: outdeg[a]=outdeg.get(a,0)+1; indeg[b]=indeg.get(b,0)+1
print('top50 nodes citing >=1 other top50',len(outdeg),' >=3',sum(1 for v in outdeg.values() if v>=3))
print('indeg top', sorted(indeg.items(),key=lambda x:-x[1])[:10])
recip=sum(1 for a,b in top_only if (b,a) in set(top_only))//2
print('reciprocal pairs',recip)
# key-work citation within top50 and recent
def cites(refs,key): return any(k in refs for k in KEY[key])
for key in KEY:
    print(key,'top50:',sum(cites(n[5],key) for n in nodes[1:]),'/',len(nz),' recent:',sum(cites([W(x) for x in w['referenced_works']],key) for w in rec['results']),'/',sum(1 for w in rec['results'] if w['referenced_works']))
ajrrefs=nodes[0][5]
print('AJR2001 refs',len(ajrrefs))
for k,v in LOCK.items():
    print(k,v,'cited by AJR2001:',v in ajrrefs,' by top50:',sum(v in n[5] for n in nodes[1:]),' by recent:',sum(v in [W(x) for x in w['referenced_works']] for w in rec['results']))
json.dump(dict(nodes=[dict(node=n[0],openalex=n[1],title=n[2],year=n[3],cited_by=n[4],n_refs=len(n[5])) for n in nodes],edges=edges),open('graph.json','w'),indent=1)
