"""Compare AJR (2001) Appendix Table A2 (pdftotext -layout of the published PDF) with posted maketable4.dta."""
import re, json, math, pandas as pd, sys
lay=open("/workspace/acemoglu-src/colonial-origins-of-comparative-development.layout.txt",encoding="utf-8").read()
blk=lay[lay.index("APPENDIXTABLEA2"):lay.index("REFERENCES")]
rows=re.findall(r"\b([A-Z]{3})\s+(\d+\.\d+)\s+(\d+\.\d+)\s+(\d+(?:\.\d+)?)",blk)
a2=pd.DataFrame(rows,columns=["shortnam","gdp","risk","mort"]).astype({"gdp":float,"risk":float,"mort":float})
t4=pd.read_stata("/workspace/acemoglu-src/data/maketable4.dta"); b=t4[t4.baseco==1]
m=a2.merge(b,on="shortnam",how="outer",indicator=True)
m["d_gdp"]=(m.gdp-m.logpgp95).round(3); m["d_risk"]=(m.risk-m.avexpr).round(3)
m["posted_mort"]=m.logem4.apply(lambda v: round(math.exp(v),2)); m["d_logmort"]=(m.mort.apply(math.log)-m.logem4).round(3)
flag=m[(m._merge!="both")|(m.d_gdp.abs()>0.006)|(m.d_risk.abs()>0.006)|(m.d_logmort.abs()>0.001)]
print("parsed rows:",len(a2)); print(flag[["shortnam","gdp","logpgp95","risk","avexpr","mort","posted_mort","_merge"]].to_string())
json.dump({"parsed_rows":len(a2),"mismatches":flag[["shortnam","gdp","logpgp95","risk","avexpr","mort","posted_mort"]].astype(str).to_dict("records")},open("tableA2_vs_posted.json","w"),indent=1)
