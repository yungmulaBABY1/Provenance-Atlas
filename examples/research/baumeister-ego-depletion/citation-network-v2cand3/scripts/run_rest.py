import urllib.parse, subprocess, time, datetime, sys, os
SEL="id,doi,display_name,publication_year,type,cited_by_count,authorships,primary_location,referenced_works"
B='https://api.openalex.org/works'
def go(stage,params,out):
    if os.path.exists(out): print('skip',out); return
    params=dict(params,select=SEL,mailto='grokbot-audit@localhost')
    subprocess.run(['python3','scripts/fetch.py',stage,B+'?'+urllib.parse.urlencode(params),out]); time.sleep(8)
T='W2123817056'
go('stage2c-adj1-Q7',{'filter':'title_and_abstract.search:("decision fatigue" OR "strength model of self-control" OR "self-control strength"),from_publication_date:1998-01-01,to_publication_date:2026-11-05,type:article|preprint|book-chapter|review','per-page':10},'raw/adj1_Q7.json')
go('stage2c-target',{'filter':'ids.openalex:'+T},'raw/target_refs.json')
open('raw/reception_exec_time.txt','w').write(datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')+'\n')
go('stage2c-reception1',{'filter':'cites:'+T,'sort':'cited_by_count:desc','per-page':50},'raw/reception1_top50.json')
go('stage2c-recent1',{'filter':'cites:'+T+',from_publication_date:2021-11-05','sort':'cited_by_count:desc','per-page':25},'raw/recent1_top25.json')
for k,t in [('F1','mental fatigue'),('F2','learned helplessness'),('F3','mood persistence'),('F4','experimenter expectancy'),('F5','mental effort')]:
    go('stage2c-secE-'+k,{'filter':f'title.search:{t},to_publication_date:1998-04-30,type:article','sort':'cited_by_count:desc','per-page':3},f'raw/secE_{k}.json')
