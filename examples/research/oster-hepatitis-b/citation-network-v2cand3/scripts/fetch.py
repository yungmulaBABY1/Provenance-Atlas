"""fetch.py SECTION URL OUTFILE -- GET with logging to ../retrieval_log.jsonl (retries 429/5xx x3).
OpenAlex URLs must carry a select= that omits abstract_inverted_index; any 'abstract' or
'abstract_inverted_index' key in a JSON response is nulled before the file is written."""
import sys, json, time, hashlib, urllib.request, urllib.error, datetime
sec, url, out = sys.argv[1:4]
LOG = "/workspace/oster/retrieval_log.jsonl"
if "api.openalex.org" in url and ("select=" not in url or "abstract" in url.split("select=")[1].split("&")[0]):
    sys.exit("refusing OpenAlex URL without abstract-free select=")
def now(): return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
def scrub(o):
    if isinstance(o, dict):
        return {k: (None if k in ("abstract", "abstract_inverted_index") else scrub(v)) for k, v in o.items()}
    if isinstance(o, list): return [scrub(x) for x in o]
    return o
for attempt in range(1, 4):
    rec = {"stage": sec, "url": url, "file": out, "attempt": attempt, "at": now()}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "grokbot-audit/1.0 (mailto:grokbot-audit@localhost)"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read(); status = r.status
        rec["raw_sha256"] = hashlib.sha256(data).hexdigest()
        try:
            data = (json.dumps(scrub(json.loads(data)), ensure_ascii=False, indent=1) + "\n").encode()
        except Exception: pass
        rec.update(status=status, bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        open(out, "wb").write(data); open(LOG, "a").write(json.dumps(rec) + "\n"); print(json.dumps(rec)); sys.exit(0)
    except urllib.error.HTTPError as e:
        rec.update(status=e.code, outcome="HTTP_ERROR")
    except Exception as e:
        rec.update(status=None, outcome="ERROR:" + type(e).__name__)
    open(LOG, "a").write(json.dumps(rec) + "\n"); print(json.dumps(rec))
    if rec.get("status") not in (429, 500, 502, 503, 504, None): break
    time.sleep(10 * attempt)
sys.exit(1)
