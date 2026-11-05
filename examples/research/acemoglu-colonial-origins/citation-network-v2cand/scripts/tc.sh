# usage: tc SECTION NOTE  -- append a tool-call record
tc(){ echo "{\"t\":\"$(date -u +%FT%TZ)\",\"section\":\"$1\",\"tool_call\":1,\"note\":\"$2\"}" >> /workspace/v2cand/worklog.jsonl; }
