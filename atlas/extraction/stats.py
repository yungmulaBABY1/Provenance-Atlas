"""Declared evidence check: reported-statistics-consistency/1. Deterministic; stdlib only.

Scope: whether the numbers a source reports for one two-sample t test agree with
each other at their reported precision, and whether a claim restates them
faithfully. It does not reanalyse data, judge the analysis, or say whether a
non-significant result shows the absence of an effect.

Sub-checks:
  TRANSCRIPTION  each statistic in the claim equals the source passage's value;
  P_FROM_T       two-tailed p recomputed from t and df overlaps the reported p;
  T_FROM_CI      t implied by the mean difference and its 95% CI, using the t
                 critical value at df, overlaps the reported t; and the CI is
                 centred on the mean difference.
Both texts are read after nfc-whitespace/2. Every value is treated as an interval: reported value +/- half a unit in its last
decimal place. A sub-check is CONSISTENT when the intervals overlap.
"""

from __future__ import annotations

import math
import re

from ..contract import normalize

CHECK_ID = "reported-statistics-consistency/1"
MINUS = "−"
NUMBER = r"[−-]?\d*\.?\d+"
PATTERNS = {
    "mean_difference": re.compile(rf"mean difference = ({NUMBER})"),
    "ci": re.compile(rf"95% CI(?: =)? \[({NUMBER}), ({NUMBER})\]"),
    "t": re.compile(rf"t\((\d+)\) = ({NUMBER})"),
    "p": re.compile(rf"\bp = ({NUMBER})"),
    "d": re.compile(rf"d = ({NUMBER})"),
}


def betacf(a: float, b: float, x: float) -> float:
    """Continued fraction for the incomplete beta function (modified Lentz)."""
    tiny, eps = 1e-300, 1e-15
    qab, qap, qam = a + b, a + 1.0, a - 1.0
    c, d = 1.0, 1.0 - qab * x / qap
    d = 1.0 / (d if abs(d) > tiny else tiny)
    h = d
    for m in range(1, 1000):
        m2 = 2 * m
        aa = m * (b - m) * x / ((qam + m2) * (a + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        h *= d * c
        aa = -(a + m) * (qab + m) * x / ((a + m2) * (qap + m2))
        d = 1.0 + aa * d
        d = 1.0 / (d if abs(d) > tiny else tiny)
        c = 1.0 + aa / c
        c = c if abs(c) > tiny else tiny
        delta = d * c
        h *= delta
        if abs(delta - 1.0) < eps:
            return h
    raise ArithmeticError("betacf did not converge")


def betainc(a: float, b: float, x: float) -> float:
    """Regularized incomplete beta I_x(a, b)."""
    if x <= 0.0:
        return 0.0
    if x >= 1.0:
        return 1.0
    front = math.exp(math.lgamma(a + b) - math.lgamma(a) - math.lgamma(b)
                     + a * math.log(x) + b * math.log1p(-x))
    if x < (a + 1.0) / (a + b + 2.0):
        return front * betacf(a, b, x) / a
    return 1.0 - front * betacf(b, a, 1.0 - x) / b


def p_two_tailed(t: float, df: float) -> float:
    return betainc(df / 2.0, 0.5, df / (df + t * t))


def t_critical(df: float, alpha: float = 0.05) -> float:
    lo, hi = 0.0, 100.0
    for _ in range(200):
        mid = (lo + hi) / 2.0
        if p_two_tailed(mid, df) > alpha:
            lo = mid
        else:
            hi = mid
    return (lo + hi) / 2.0


def value(token: str) -> dict:
    text = token.replace(MINUS, "-")
    decimals = len(text.split(".")[1]) if "." in text else 0
    v = float(text)
    half = 0.5 * 10 ** -decimals
    return {"reported": token, "value": v, "decimals": decimals, "interval": [v - half, v + half]}


def extract(text: str) -> dict:
    """Statistics named in one test's text. Missing ones are absent, never guessed."""
    found = {}
    for name, pattern in PATTERNS.items():
        hits = pattern.findall(text)
        if len(hits) != 1:
            found[name] = {"status": "NOT_FOUND" if not hits else "AMBIGUOUS", "occurrences": len(hits)}
            continue
        hit = hits[0]
        if name == "ci":
            found[name] = {"status": "FOUND", "lower": value(hit[0]), "upper": value(hit[1])}
        elif name == "t":
            found[name] = {"status": "FOUND", "df": int(hit[0]), "t": value(hit[1])}
        else:
            found[name] = {"status": "FOUND", **value(hit)}
    return found


def overlap(a: list[float], b: list[float]) -> bool:
    return a[0] <= b[1] and b[0] <= a[1]


def transcription(claim: dict, source: dict) -> dict:
    rows = []
    for name in ("mean_difference", "ci", "t", "p", "d"):
        c, s = claim.get(name, {}), source.get(name, {})
        if c.get("status") != "FOUND" or s.get("status") != "FOUND":
            rows.append({"statistic": name, "result": "NOT_COMPARABLE",
                         "claim": c.get("status"), "source": s.get("status")})
            continue
        if name == "ci":
            same = [c["lower"]["reported"], c["upper"]["reported"]] == [s["lower"]["reported"], s["upper"]["reported"]]
            claim_text = [c["lower"]["reported"], c["upper"]["reported"]]
            source_text = [s["lower"]["reported"], s["upper"]["reported"]]
        elif name == "t":
            same = (c["df"], c["t"]["reported"]) == (s["df"], s["t"]["reported"])
            claim_text, source_text = [c["df"], c["t"]["reported"]], [s["df"], s["t"]["reported"]]
        else:
            same = c["reported"] == s["reported"]
            claim_text, source_text = c["reported"], s["reported"]
        rows.append({"statistic": name, "result": "SAME" if same else "DIFFERENT",
                     "claim": claim_text, "source": source_text})
    compared = [r for r in rows if r["result"] != "NOT_COMPARABLE"]
    result = ("NOT_CHECKABLE" if not compared else
              "CONSISTENT" if all(r["result"] == "SAME" for r in compared) else "INCONSISTENT")
    return {"sub_check": "TRANSCRIPTION", "result": result, "rows": rows,
            "basis": "Reported strings compared after reading each statistic; numerals must be identical."}


def p_from_t(source: dict) -> dict:
    t, p = source.get("t", {}), source.get("p", {})
    if t.get("status") != "FOUND" or p.get("status") != "FOUND":
        return {"sub_check": "P_FROM_T", "result": "NOT_CHECKABLE", "reason": "t or p not found once"}
    df = t["df"]
    lo, hi = sorted(abs(x) for x in t["t"]["interval"])
    recomputed = [p_two_tailed(hi, df), p_two_tailed(lo, df)]
    return {"sub_check": "P_FROM_T", "df": df, "t_interval": t["t"]["interval"],
            "recomputed_p_interval": [round(x, 6) for x in recomputed], "reported_p_interval": p["interval"],
            "result": "CONSISTENT" if overlap(recomputed, p["interval"]) else "INCONSISTENT"}


def t_from_ci(source: dict) -> dict:
    t, mean, ci = source.get("t", {}), source.get("mean_difference", {}), source.get("ci", {})
    if any(x.get("status") != "FOUND" for x in (t, mean, ci)):
        return {"sub_check": "T_FROM_CI", "result": "NOT_CHECKABLE", "reason": "t, mean difference or CI not found once"}
    df = t["df"]
    crit = t_critical(df)
    lower, upper = ci["lower"]["interval"], ci["upper"]["interval"]
    width = [upper[0] - lower[1], upper[1] - lower[0]]
    se = [width[0] / (2 * crit), width[1] / (2 * crit)]
    m = mean["interval"]
    candidates = [mv / sv for mv in m for sv in se]
    implied = [min(candidates), max(candidates)]
    centre = [(lower[0] + upper[0]) / 2, (lower[1] + upper[1]) / 2]
    centred = overlap(centre, m)
    consistent = overlap(implied, t["t"]["interval"]) and centred
    return {"sub_check": "T_FROM_CI", "df": df, "t_critical_0975": round(crit, 6),
            "implied_t_interval": [round(x, 6) for x in implied], "reported_t_interval": t["t"]["interval"],
            "ci_centre_interval": [round(x, 6) for x in centre], "mean_interval": m,
            "ci_centred_on_mean": centred, "result": "CONSISTENT" if consistent else "INCONSISTENT",
            "assumption": "Symmetric t-based 95% CI with the same df as the reported t test"}


def check(claim_text: str, source_text: str) -> dict:
    # nfc-whitespace/2 first: extracted source text breaks lines inside statistics.
    claim, source = extract(normalize(claim_text)), extract(normalize(source_text))
    subs = [transcription(claim, source), p_from_t(source), t_from_ci(source)]
    results = {s["result"] for s in subs}
    overall = ("INCONSISTENT" if "INCONSISTENT" in results else
               "NOT_CHECKABLE" if results == {"NOT_CHECKABLE"} else
               "CONSISTENT" if results == {"CONSISTENT"} else "PARTIALLY_CHECKABLE")
    return {"check": CHECK_ID, "result": overall, "claim_statistics": claim, "source_statistics": source,
            "sub_checks": subs,
            "not_checked": ["Cohen's d (group sizes are not reported in the main text)",
                            "The data, the choice of test, and the paper's interpretation"],
            "scope": __doc__.split("\n\n")[1].replace("\n", " ")}
