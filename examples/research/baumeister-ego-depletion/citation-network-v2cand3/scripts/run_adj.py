import urllib.parse, subprocess, time, datetime
SEL="id,doi,display_name,publication_year,type,cited_by_count,authorships,primary_location,referenced_works"
Q={'Q1':'"ego depletion" AND (replication OR "registered replication" OR "multilab" OR "multi-site" OR preregistered)',
'Q2':'"ego depletion" AND ("meta-analysis" OR "publication bias" OR "small-study")',
'Q3':'("ego depletion" OR "self-control") AND glucose',
'Q4':'"ego depletion" AND (motivation OR "process model" OR "opportunity cost")',
'Q5':'("ego depletion" OR willpower) AND ("implicit theories" OR "lay theories" OR beliefs)',
'Q6':'"ego depletion" AND (fatigue OR frustration OR mood OR "manipulation check")',
'Q7':'("decision fatigue" OR "strength model of self-control" OR "self-control strength")'}
open('raw/adj1_exec_time.txt','w').write(datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')+'\n')
for k,q in Q.items():
    f=f'title_and_abstract.search:{q},from_publication_date:1998-01-01,to_publication_date:2026-11-05,type:article|preprint|book-chapter|review'
    url='https://api.openalex.org/works?'+urllib.parse.urlencode({'filter':f,'per-page':10,'select':SEL,'mailto':'grokbot-audit@localhost'})
    subprocess.run(['python3','scripts/fetch.py','stage2c-adj1-'+k,url,f'raw/adj1_{k}.json'])
    time.sleep(3)
