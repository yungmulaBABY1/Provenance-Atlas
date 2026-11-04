import sys,json,time
sys.path.insert(0,'/workspace/acemoglu-cn/scripts')
from fetch import getjson
time.sleep(60); aj=getjson('https://api.semanticscholar.org/graph/v1/paper/DOI:10.1257/aer.91.5.1369?fields=paperId,title,citationCount,externalIds','s2_ajr2001.json',tries=8,base_sleep=10)
AJR=aj['paperId']; print('AJR s2',AJR,aj['citationCount'])
top=json.load(open('raw/top50_citers.json'))['results']; rec=json.load(open('raw/recent5y_top25.json'))['results']
sets=[('T',i,w) for i,w in enumerate(top[:15],1)]+[('R',i,w) for i,w in enumerate(rec,1)]
out=[]
for tag,i,w in sets:
    doi=w.get('doi'); wid=w['id'].split('/')[-1]
    ident=('DOI:'+doi.replace('https://doi.org/','')) if doi else None
    row=dict(set=tag,rank=i,openalex=wid,doi=doi,title=w['display_name'],year=w['publication_year'])
    if not ident: row['outcome']='NO_DOI_NOT_QUERIED'; out.append(row); continue
    time.sleep(1.2)
    d=getjson(f'https://api.semanticscholar.org/graph/v1/paper/{ident}/references?fields=paperId,title,contexts,intents,isInfluential&limit=1000',f's2_refs_{tag}{i:02d}_{wid}.json',tries=7,base_sleep=8)
    if d is None: row['outcome']='RETRIEVAL_FAILED'; out.append(row); continue
    data=d.get('data') or []
    hit=[x for x in data if (x.get('citedPaper') or {}).get('paperId')==AJR]
    row['n_refs_s2']=len(data)
    if not data: row['outcome']='S2_NO_REFERENCE_DATA'
    elif not hit: row['outcome']='AJR_NOT_IN_S2_REFS'
    else:
        h=hit[0]; row.update(outcome='AJR_FOUND',contexts=h.get('contexts') or [],intents=h.get('intents'),isInfluential=h.get('isInfluential'))
        if not row['contexts']: row['outcome']='AJR_FOUND_NO_CONTEXTS'
    out.append(row); print(tag,i,row['outcome'],len(row.get('contexts',[])))
json.dump(out,open('s2_contexts.json','w'),indent=1,ensure_ascii=False)
