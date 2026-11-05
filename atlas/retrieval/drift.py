"""Compare two records of the same locked query: what entered, left or moved."""

from __future__ import annotations

from ..contract import ContractError
from . import DRIFT_SCHEMA


def _when(record: dict) -> str | None:
    if record["mode"] == "live":
        ok = [a for a in record.get("attempts", []) if a.get("outcome") == "OK"]
        return ok[-1]["at"] if ok else None
    log = record.get("executor_log") or {}
    return log.get("last_success_at")


def compare(before: dict, after: dict) -> dict:
    if before["id"] != after["id"] or before["spec_sha256"] != after["spec_sha256"]:
        raise ContractError("DRIFT_MISMATCH: records are not of the same spec")
    base = {"schema": DRIFT_SCHEMA, "id": before["id"],
            "before": {"mode": before["mode"], "at": _when(before)},
            "after": {"mode": after["mode"], "at": _when(after)}}
    if not before.get("response") or not after.get("response"):
        return dict(base, status="NOT_COMPARED",
                    reason="a record has no successful response")
    then = [r["id"] for r in before["response"]["ranked"]]
    now = [r["id"] for r in after["response"]["ranked"]]
    titles = {r["id"]: r["title"] for r in before["response"]["ranked"] + after["response"]["ranked"]}
    common = set(then) & set(now)
    if then == now:
        status = "UNCHANGED"
    elif set(then) == set(now):
        status = "REORDERED"
    else:
        status = "CHANGED"
    base["before"].update(count=before["response"]["meta"]["count"], n=len(then))
    base["after"].update(count=after["response"]["meta"]["count"], n=len(now))
    return dict(base, status=status,
                overlap=len(common),
                entered=[{"id": i, "rank": now.index(i) + 1, "title": titles[i]}
                         for i in now if i not in common],
                left=[{"id": i, "rank": then.index(i) + 1, "title": titles[i]}
                      for i in then if i not in common],
                moved=[{"id": i, "before": then.index(i) + 1, "after": now.index(i) + 1}
                       for i in then if i in common and then.index(i) != now.index(i)],
                results_digest_equal=(before["response"]["results_digest"]
                                      == after["response"]["results_digest"]))


def render(drifts: list[dict]) -> str:
    lines = ["DRIFT REPORT: saved executor responses vs a code-run replay",
             "Rank and membership only. A change is an observation about the index or its",
             "ranking over time. It says nothing about whether the audit was right.", ""]
    for d in drifts:
        b, a = d["before"], d["after"]
        lines.append(f"{d['id']}: {d['status']}  ({b['mode']} {b['at']} -> {a['mode']} {a['at']})")
        if d["status"] == "NOT_COMPARED":
            lines.append(f"  {d['reason']}")
            continue
        lines.append(f"  count {b['count']} -> {a['count']}; top {b['n']} vs {a['n']}; overlap {d['overlap']}")
        for e in d["entered"]:
            lines.append(f"  + rank {e['rank']}: {e['id']} {e['title']}")
        for e in d["left"]:
            lines.append(f"  - was rank {e['rank']}: {e['id']} {e['title']}")
        for m in d["moved"]:
            lines.append(f"  ~ {m['id']} rank {m['before']} -> {m['after']}")
    return "\n".join(lines) + "\n"
