import sys, json, urllib.parse
sys.path.insert(0,'/workspace/acemoglu-cn/scripts')
from fetch import getjson
M='&mailto=grokbot-audit@localhost'
OA='https://api.openalex.org/works'
SEL='id,doi,display_name,publication_year,publication_date,cited_by_count,type,authorships,primary_location,referenced_works,ids'
def q(filt, sort=None, per=50, sel=SEL, page=1):
    u=OA+'?filter='+urllib.parse.quote(filt)+(('&sort='+sort) if sort else '')+f'&per-page={per}&page={page}'+('&select='+sel if sel else '')+M
    return u
getjson(OA+'/W3124166904?'+M[1:],'ajr2001_work.json')
getjson(q('cites:W3124166904','cited_by_count:desc',50),'top50_citers.json')
getjson(q('cites:W3124166904,from_publication_date:2021-11-04','cited_by_count:desc',25),'recent5y_top25.json')
getjson(OA+'?filter=cites:W3124166904&group_by=publication_year'+M,'citers_by_year.json')
getjson(OA+'?filter=cites:W3124166904,cites:W1969918011&group_by=publication_year'+M,'citers_also_albouy_by_year.json')
getjson(OA+'?filter=cites:W1969918011&group_by=publication_year'+M,'albouy_citers_by_year.json')
getjson(OA+'/W1969918011?'+M[1:],'albouy2012_work.json')
getjson(OA+'/W3124131699?'+M[1:],'ajr2012reply_work.json')
for g in ['authorships.author.id','authorships.institutions.id','primary_location.source.id','grants.funder']:
    getjson(OA+'?filter=cites:W3124166904&group_by='+g+M,'citers_groupby_'+g.replace('.','_')+'.json')
print('done')
