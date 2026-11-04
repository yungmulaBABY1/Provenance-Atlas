"""Logged, cached HTTP GET with backoff. Every request is appended to raw/retrieval_log.jsonl."""
import json, time, hashlib, os, urllib.request, urllib.error, datetime
BASE='/workspace/acemoglu-cn/raw'
LOG=os.path.join(BASE,'retrieval_log.jsonl')
UA='ProvenanceAtlasAudit/0.1 (mailto:grokbot-audit@localhost)'
def now(): return datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
def get(url, name, tries=6, base_sleep=2.0, binary=False):
    path=os.path.join(BASE,name)
    if os.path.exists(path):
        return open(path,'rb').read()
    last=None
    for i in range(tries):
        req=urllib.request.Request(url,headers={'User-Agent':UA,'Accept':'*/*'})
        try:
            with urllib.request.urlopen(req,timeout=60) as r:
                data=r.read(); status=r.status; final=r.geturl()
            open(path,'wb').write(data)
            rec=dict(url=url,final_url=final,file=name,status=status,bytes=len(data),sha256=hashlib.sha256(data).hexdigest(),at=now(),attempt=i+1)
            open(LOG,'a').write(json.dumps(rec)+'\n')
            return data
        except urllib.error.HTTPError as e:
            last=e.code
            open(LOG,'a').write(json.dumps(dict(url=url,file=name,status=e.code,at=now(),attempt=i+1,outcome='HTTP_ERROR'))+'\n')
            if e.code in (429,500,502,503,504):
                time.sleep(base_sleep*(2**i)); continue
            return None
        except Exception as e:
            last=str(e)
            open(LOG,'a').write(json.dumps(dict(url=url,file=name,status=None,error=str(e)[:200],at=now(),attempt=i+1,outcome='ERROR'))+'\n')
            time.sleep(base_sleep*(2**i))
    open(LOG,'a').write(json.dumps(dict(url=url,file=name,status=last,at=now(),outcome='GAVE_UP'))+'\n')
    return None
def getjson(url,name,**kw):
    d=get(url,name,**kw)
    return json.loads(d) if d else None
