"""Light replication checks for AJR (2001) Table 4 and the AJR(2012)/Albouy(2012) exchange.

Inputs (authors' posted data, hashes in SOURCES_MANIFEST):
  maketable4.dta  (colonial_origins.zip, MIT data archive)
  'dataset used for final AER rebuttal Sept 11 2011.dta'  (dataset.zip, MIT)
Outputs: results.json + printed tables. Deterministic; no randomness.
Exploratory: these are reruns of posted data, not an independent data reconstruction.
"""
import json, sys, platform
from pathlib import Path
import numpy as np, pandas as pd, scipy, statsmodels, linearmodels
import statsmodels.api as sm
from scipy import stats
from linearmodels.iv import IV2SLS

DATA = Path(sys.argv[1] if len(sys.argv) > 1 else "/workspace/acemoglu-src/data")
OUT = Path(sys.argv[2] if len(sys.argv) > 2 else Path(__file__).with_name("results.json"))
res = {"environment": {"python": platform.python_version(), "numpy": np.__version__, "pandas": pd.__version__,
                       "scipy": scipy.__version__, "statsmodels": statsmodels.__version__,
                       "linearmodels": linearmodels.__version__}, "runs": []}

def cov_kw(kind, clusters):
    if kind == "unadjusted": return dict(cov_type="unadjusted", debiased=True)
    if kind == "robust": return dict(cov_type="robust", debiased=True)
    if kind == "cluster": return dict(cov_type="clustered", clusters=clusters, debiased=True)

def ols_cov(kind, clusters):
    if kind == "unadjusted": return dict(cov_type="nonrobust")
    if kind == "robust": return dict(cov_type="HC1")
    if kind == "cluster": return dict(cov_type="cluster", cov_kwds={"groups": clusters})

def ar_ci(df, y, x, z, controls, kind, clusters, level=0.95):
    """Anderson-Rubin 95% confidence set by exact analytic inversion.
    For H0: alpha=a, regress (y - a x) on [1, z, controls]; the z-coefficient is b_y - a b_x and its
    sandwich variance is V_yy - 2a V_yx + a^2 V_xx (same bread, joint meat). The set
    {a : (b_y - a b_x)^2 <= c (V_yy - 2a V_yx + a^2 V_xx)} is solved as a quadratic inequality.
    Variance flavours mirror the point-estimate SEs: unadjusted, HC1, or CR1 cluster."""
    X = sm.add_constant(df[[z] + controls], has_constant="add").to_numpy(float)
    n, k = X.shape
    j = 1  # column of z (after const)
    XtXi = np.linalg.inv(X.T @ X)
    Y = df[[y, x]].to_numpy(float)
    B = XtXi @ X.T @ Y                      # k x 2
    E = Y - X @ B                           # residuals n x 2
    if kind == "unadjusted":
        S = (E.T @ E) / (n - k)
        V = S * XtXi[j, j]
        dfd = n - k
    elif kind == "robust":
        a_row = XtXi[j] @ X.T                # influence weights for coef j, length n
        V = (a_row[:, None] * E).T @ (a_row[:, None] * E) * n / (n - k)
        dfd = n - k
    else:
        a_row = XtXi[j] @ X.T
        g = pd.Series(range(n)).groupby(clusters.to_numpy()).indices
        G = len(g)
        sums = np.array([(a_row[idx, None] * E[idx]).sum(0) for idx in g.values()])
        V = sums.T @ sums * (G / (G - 1)) * ((n - 1) / (n - k))
        dfd = G - 1
    c = stats.f.ppf(level, 1, dfd)
    by, bx = B[j, 0], B[j, 1]
    Vyy, Vyx, Vxx = V[0, 0], V[0, 1], V[1, 1]
    # (by - a bx)^2 - c(Vyy - 2a Vyx + a^2 Vxx) <= 0  ->  A a^2 + Bq a + C <= 0
    A = bx**2 - c * Vxx
    Bq = -2 * by * bx + 2 * c * Vyx
    C = by**2 - c * Vyy
    disc = Bq**2 - 4 * A * C
    fs_wald = bx**2 / Vxx
    out = {"first_stage_wald": round(float(fs_wald), 3), "crit_F": round(float(c), 3), "df_denom": int(dfd)}
    if A > 0:
        if disc < 0:
            out.update(set="EMPTY", unbounded=False)
        else:
            r = sorted([(-Bq - np.sqrt(disc)) / (2 * A), (-Bq + np.sqrt(disc)) / (2 * A)])
            out.update(set="INTERVAL", interval=[round(float(r[0]), 3), round(float(r[1]), 3)], unbounded=False)
    elif A < 0:
        if disc < 0:
            out.update(set="WHOLE_REAL_LINE", unbounded=True)
        else:
            r = sorted([(-Bq - np.sqrt(disc)) / (2 * A), (-Bq + np.sqrt(disc)) / (2 * A)])
            out.update(set="UNION_OF_TWO_RAYS", rays=[["-inf", round(float(r[0]), 3)], [round(float(r[1]), 3), "inf"]], unbounded=True)
    else:
        out.update(set="DEGENERATE", unbounded=True)
    return out

def run(label, df, y, x, z, controls=(), kind="unadjusted", cluster_var=None, note=""):
    controls = list(controls)
    df = df.dropna(subset=[y, x, z] + controls + ([cluster_var] if cluster_var else [])).copy()
    clusters = df[cluster_var] if cluster_var else None
    exog = sm.add_constant(df[controls], has_constant="add") if controls else pd.DataFrame({"const": 1.0}, index=df.index)
    iv = IV2SLS(df[y], exog, df[[x]], df[[z]]).fit(**cov_kw(kind, clusters))
    fs = sm.OLS(df[x], sm.add_constant(df[[z] + controls], has_constant="add")).fit(**ols_cov(kind, clusters))
    ols = sm.OLS(df[y], sm.add_constant(df[[x] + controls], has_constant="add")).fit(**ols_cov(kind, clusters))
    out = {"label": label, "n": int(len(df)), "se_type": kind, "cluster_var": cluster_var,
           "n_clusters": int(clusters.nunique()) if cluster_var else None, "controls": controls, "instrument": z,
           "iv_coef": round(float(iv.params[x]), 4), "iv_se": round(float(iv.std_errors[x]), 4),
           "fs_coef": round(float(fs.params[z]), 4), "fs_se": round(float(fs.bse[z]), 4),
           "fs_F": round(float(fs.tvalues[z] ** 2), 3), "fs_p": float(fs.pvalues[z]),
           "fs_r2": round(float(fs.rsquared), 3),
           "ols_coef": round(float(ols.params[x]), 4), "ols_se": round(float(ols.bse[x]), 4),
           "ar_95": ar_ci(df, y, x, z, controls, kind, clusters), "note": note}
    for c in controls:
        out.setdefault("fs_controls", {})[c] = [round(float(fs.params[c]), 4), round(float(fs.bse[c]), 4)]
    res["runs"].append(out)
    ar = out["ar_95"]
    arstr = {"INTERVAL": str(ar.get("interval")), "UNION_OF_TWO_RAYS": "rays " + str(ar.get("rays")),
             "WHOLE_REAL_LINE": "(-inf, inf)"}.get(ar["set"], ar["set"])
    print(f"{label:<62} n={out['n']:>2} {kind:<10} IV {out['iv_coef']:6.2f} ({out['iv_se']:.2f})  "
          f"FS {out['fs_coef']:6.2f} ({out['fs_se']:.2f}) F={out['fs_F']:6.2f}  AR95 {arstr}")
    return out

# ---------------- Part A: AJR 2001 Table 4 from the posted maketable4 data ----------------
t4 = pd.read_stata(DATA / "maketable4.dta")
base = t4[t4.baseco == 1].copy()
print("== Part A: Table 4 replication (maketable4.dta, baseco==1), conventional SEs as in the paper ==")
run("T4c1 base", base, "logpgp95", "avexpr", "logem4")
run("T4c2 base + latitude", base, "logpgp95", "avexpr", "logem4", ["lat_abst"])
run("T4c3 base without Neo-Europes", base[base.rich4 != 1], "logpgp95", "avexpr", "logem4")
run("T4c4 base without Neo-Europes + latitude", base[base.rich4 != 1], "logpgp95", "avexpr", "logem4", ["lat_abst"])
run("T4c5 base without Africa", base[base.africa != 1], "logpgp95", "avexpr", "logem4")
run("T4c6 base without Africa + latitude", base[base.africa != 1], "logpgp95", "avexpr", "logem4", ["lat_abst"])
base["other_cont"] = ((base.africa != 1) & (base.asia != 1) & base.shortnam.isin(["AUS", "MLT", "NZL"])).astype(float)
run("T4c7 base + continent dummies", base, "logpgp95", "avexpr", "logem4", ["africa", "asia", "other_cont"])
run("T4c8 base + continent dummies + latitude", base, "logpgp95", "avexpr", "logem4", ["africa", "asia", "other_cont", "lat_abst"])
run("T4c9 log output per worker", base, "loghjypl", "avexpr", "logem4")
run("T4c1 base, HC1-robust SEs (not in paper)", base, "logpgp95", "avexpr", "logem4", kind="robust")

# ---------------- Part B: the 2012 exchange, rebuttal dataset ----------------
d = pd.read_stata(DATA / "dataset used for final AER rebuttal Sept 11 2011.dta")
# Cluster = countries sharing an identical original mortality rate (Albouy's Moulton concern).
d["mortcluster"] = d.logmort0.round(6).astype(str)
cmp = base.merge(d, on="shortnam", how="outer", indicator=True)
res["dataset_concordance"] = {
    "maketable4_base_n": int(len(base)), "rebuttal_n": int(len(d)),
    "merge": cmp["_merge"].value_counts().to_dict(),
    "max_abs_diff_logmort": float((cmp.logem4 - cmp.logmort0).abs().max()),
    "max_abs_diff_risk": float((cmp.avexpr - cmp.risk).abs().max()),
    "max_abs_diff_gdp": float((cmp.logpgp95 - cmp.loggdp).abs().max()),
    "n_source0": int(d.source0.sum()), "n_campaign": int(d.campaign.sum()), "n_slave": int(d.slave.sum()),
    "n_mortality_clusters": int(d.mortcluster.nunique())}
print("\n== dataset concordance ==", json.dumps(res["dataset_concordance"], default=str))

print("\n== Part B: Albouy-style checks (posted rebuttal data; Albouy's own package NOT used) ==")
own = d[d.source0 == 1]
for z, zl in (("logmort0", "orig mortality"), ("logmortcap250", "capped at 250")):
    for ctrl, cl in (([], "no controls"), (["latitude"], "latitude")):
        run(f"B0 full 64 | {zl} | {cl}", d, "loggdp", "risk", z, ctrl, kind="robust")
        run(f"B1 full 64 | {zl} | {cl} | cluster by shared rate", d, "loggdp", "risk", z, ctrl, kind="cluster", cluster_var="mortcluster")
        run(f"B2 own-country rates (source0) | {zl} | {cl}", own, "loggdp", "risk", z, ctrl, kind="robust")
        run(f"B3 full 64 + campaign+laborer | {zl} | {cl}", d, "loggdp", "risk", z, ["campaign", "slave"] + ctrl, kind="cluster", cluster_var="mortcluster")
        run(f"B4 own-country + campaign+laborer | {zl} | {cl}", own, "loggdp", "risk", z, ["campaign", "slave"] + ctrl, kind="robust")
print("\n== Part C: AJR reply-style outlier checks ==")
nog = own[own.shortnam != "GMB"]
run("C1 own-country, drop Gambia | orig | no controls", nog, "loggdp", "risk", "logmort0", kind="robust")
run("C2 own-country, drop Gambia + campaign+laborer | orig", nog, "loggdp", "risk", "logmort0", ["campaign", "slave"], kind="robust")
run("C3 full 64 + AJR extended recoding campaignsj2+laborer | orig", d, "loggdp", "risk", "logmort0", ["campaignsj2", "slave"], kind="cluster", cluster_var="mortcluster")
run("C4 own-country + campaignsj2+laborer | orig", own, "loggdp", "risk", "logmort0", ["campaignsj2", "slave"], kind="robust")
run("C5 own-country + campaignsj2+laborer | capped 250", own, "loggdp", "risk", "logmortcap250", ["campaignsj2", "slave"], kind="robust")
run("C6 full 64 | naval benchmark method 2 | no controls", d, "loggdp", "risk", "logmortnaval2", kind="robust")
run("C7 full 64 | Caribbean benchmark | no controls", d, "loggdp", "risk", "logmortjam", kind="robust")

res["campaign_mean_by_group"] = d.groupby("campaign")[["risk", "loggdp", "logmort0"]].mean().round(3).to_dict()
OUT.write_text(json.dumps(res, indent=1, default=str) + "\n")
print("\nwrote", OUT)
