import sys, json, urllib.parse
sys.path.insert(0,'/workspace/acemoglu-cn/scripts')
from fetch import getjson
Q={'F1':'malaria economic','F2':'geography economic development','F3':'human capital growth','F4':'weak instruments','F6':'institutions economic performance'}
out={}
for k,t in Q.items():
    url='https://api.openalex.org/works?filter='+urllib.parse.quote(f'title.search:{t},to_publication_date:2000-12-31,type:article')+'&sort=cited_by_count:desc&per-page=2&mailto=grokbot-audit@localhost'
    d=getjson(url,f'lock_{k}.json')
    out[k]=[dict(id=w['id'],doi=w.get('doi'),title=w['display_name'],year=w['publication_year'],cited_by=w['cited_by_count'],venue=(w.get('primary_location') or {}).get('source',{}) and w['primary_location']['source'].get('display_name') if w.get('primary_location') and w['primary_location'].get('source') else None) for w in d['results']] if d else 'FAILED'
    print(k, json.dumps(out[k],indent=0))
json.dump(out,open('lock/locked_sources.json','w'),indent=1)
