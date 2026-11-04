"""Check two cross-file discrepancies found in the posted data:
 TZA mortality: maketable4.dta logem4=ln(280) vs AJR 2001 Appendix Table A2 = 145 (ln 4.977)
 IDN log GDP:   rebuttal dataset loggdp=7.33 vs AJR 2001 Table A2 / maketable4 = 8.07
Re-estimates Table 4 col 1 and the rebuttal-data baseline with each value."""
import json, numpy as np, pandas as pd
from linearmodels.iv import IV2SLS
import statsmodels.api as sm
D="/workspace/acemoglu-src/data/"
def iv(df,y,x,z):
    r=IV2SLS(df[y],pd.DataFrame({'c':1.0},index=df.index),df[[x]],df[[z]]).fit(cov_type='unadjusted',debiased=True)
    f=sm.OLS(df[x],sm.add_constant(df[[z]])).fit()
    return {"iv":round(float(r.params[x]),4),"se":round(float(r.std_errors[x]),4),"fs":round(float(f.params[z]),4),"fs_se":round(float(f.bse[z]),4),"F":round(float(f.tvalues[z]**2),3)}
out={}
t4=pd.read_stata(D+"maketable4.dta"); b=t4[t4.baseco==1].copy()
out["maketable4 as posted (TZA=ln280)"]=iv(b,"logpgp95","avexpr","logem4")
b2=b.copy(); b2["logem4"]=b2.logem4.astype(float); b2.loc[b2.shortnam=="TZA","logem4"]=np.log(145)
out["maketable4 with TZA=ln145 (Table A2 value)"]=iv(b2,"logpgp95","avexpr","logem4")
d=pd.read_stata(D+"dataset used for final AER rebuttal Sept 11 2011.dta")
out["rebuttal as posted (IDN loggdp=7.33, TZA=ln145)"]=iv(d,"loggdp","risk","logmort0")
d2=d.copy(); d2["loggdp"]=d2.loggdp.astype(float); d2.loc[d2.shortnam=="IDN","loggdp"]=8.07
out["rebuttal with IDN loggdp=8.07"]=iv(d2,"loggdp","risk","logmort0")
for k,v in out.items(): print(f"{k:<50} {v}")
json.dump(out,open("discrepancy_check.json","w"),indent=1)
