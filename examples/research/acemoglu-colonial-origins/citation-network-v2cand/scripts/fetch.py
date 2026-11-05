"""fetch.py SECTION URL OUTFILE -- GET with logging to raw/retrieval_log.jsonl (retries 429/5xx x3)."""
import sys, json, time, hashlib, urllib.request, urllib.error, datetime
sec, url, out = sys.argv[1:4]
LOG = "/workspace/v2cand/raw/retrieval_log.jsonl"
def now(): return datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
for attempt in range(1, 4):
    rec = {"section": sec, "url": url, "file": out, "attempt": attempt, "at": now()}
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "grokbot-audit/1.0 (mailto:grokbot-audit@localhost)"})
        with urllib.request.urlopen(req, timeout=60) as r:
            data = r.read(); rec.update(status=r.status, final_url=r.geturl(), bytes=len(data), sha256=hashlib.sha256(data).hexdigest())
        open(out, "wb").write(data); open(LOG, "a").write(json.dumps(rec) + "\n"); print(json.dumps(rec)); sys.exit(0)
    except urllib.error.HTTPError as e:
        rec.update(status=e.code, outcome="HTTP_ERROR")
    except Exception as e:
        rec.update(status=None, outcome="ERROR:" + type(e).__name__)
    open(LOG, "a").write(json.dumps(rec) + "\n"); print(json.dumps(rec))
    if rec.get("status") not in (429, 500, 502, 503, 504, None): break
    time.sleep(3 * attempt)
sys.exit(1)
