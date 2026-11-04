import json
B='/workspace/acemoglu-cn'
top=json.load(open(f'{B}/top50_coded_inputs.json')); rec=json.load(open(f'{B}/recent25_coded_inputs.json'))
g=json.load(open(f'{B}/graph.json')); E=[tuple(e) for e in g['edges'] if 'N00' not in e]
N={n['node']:n for n in g['nodes']}
code={ # evidence type (Section B list wording where it fits), relation to central claim
'N01':('secondary analysis','central claim; authors\' reply re-analysing AJR data'),
'N02':('primary empirical test of the central claim','reuses AJR settler-mortality instrument'),
'N03':('primary empirical test of the central claim','critical; reuses AJR instrument, adds human-capital tests'),
'N04':('primary empirical study (not of the central claim)','financial development; background citation'),
'N05':('review article','self-authored synthesis hub (NBER WP)'),
'N06':('theoretical / conceptual paper','econometric method; re-analyses AJR 64-country data as an example'),
'N07':('unclear / needs source audit','OpenAlex record likely misattributed (book chapter)'),
'N08':('primary empirical study (not of the central claim)','product space; background citation'),
'N09':('review article','finance and growth; background citation'),
'N10':('primary empirical study (not of the central claim)','institutions x resource curse; adjacent'),
'N11':('review article','self-authored synthesis hub (Handbook chapter)'),
'N12':('review article','human capital and growth; rival R2 field'),
'N13':('review article','technology diffusion; background'),
'N14':('review article','climate-economy; geography-adjacent'),
'N15':('review article','resource curse; adjacent'),
'N16':('primary empirical study (not of the central claim)','temperature shocks; geography-adjacent'),
'N17':('primary empirical study (not of the central claim)','culture and institutions in European regions'),
'N18':('primary empirical study (not of the central claim)','historical persistence (slave trade, trust)'),
'N19':('secondary analysis','governance indicator construction; construct-adjacent'),
'N20':('review article','corruption; background'),
'N21':('primary empirical test of the central claim','reuses AJR settler-mortality series'),
'N22':('theoretical / conceptual paper','state capacity'),
'N23':('review article','civil war; background'),
'N24':('primary empirical study (not of the central claim)','economic geography; rival-adjacent'),
'N25':('primary empirical study (not of the central claim)','income and democracy (AJR team)'),
'N26':('commentary / editorial','econometric-methods essay'),
'N27':('primary empirical study (not of the central claim)','cronyism, Malaysia (Johnson co-author)'),
'N28':('theoretical / conceptual paper','poverty traps'),
'N29':('review article','culture and institutions'),
'N30':('theoretical / conceptual paper','growth theory (Acemoglu co-author)'),
'N31':('primary empirical study (not of the central claim)','volatility; reuses AJR instrument (AJR team)'),
'N32':('secondary analysis','book; redistribution US vs Europe'),
'N33':('review article','corruption'),
'N34':('theoretical / conceptual paper','quality of government; construct-defining'),
'N35':('primary empirical study (not of the central claim)','natural-disaster deaths'),
'N36':('primary empirical study (not of the central claim)','output after crises'),
'N37':('primary empirical study (not of the central claim)','cognitive skills and growth; rival R2 field'),
'N38':('primary empirical study (not of the central claim)','growth accelerations'),
'N39':('commentary / editorial','critique of IV and RCT practice in development'),
'N40':('primary empirical study (not of the central claim)','inherited trust and growth'),
'N41':('theoretical / conceptual paper','persistence of power (Acemoglu-Robinson)'),
'N42':('primary empirical study (not of the central claim)','within-India colonial land institutions; independent data origin for L3'),
'N43':('review article','climate-change damages'),
'N44':('review article','regional development and institutions'),
'N45':('primary empirical study (not of the central claim)','resource curse, Nigeria'),
'N46':('primary empirical study (not of the central claim)','ruggedness; geography x history'),
'N47':('theoretical / conceptual paper','comparative-economics framework'),
'N48':('primary empirical study (not of the central claim)','institutions and trade'),
'N49':('primary empirical study (not of the central claim)','slave trades; historical persistence'),
'N50':('primary empirical study (not of the central claim)','aid and growth'),
}
FT={'N01','N02','N03','N04','N05','N06','N08','N09','N12','N14','N21'}
WPV={'N13','N16'}
def clean(s): return (s or '').replace('|','/').replace('\n',' ')
def vstate(t):
    if t['node'] in FT: return 'FULL-TEXT-CONFIRMED (version noted in Section C)'
    if t['node'] in WPV: return 'ABSTRACT-CONFIRMED (working-paper full text retrieved does not cite AJR; version mismatch)'
    return 'ABSTRACT-CONFIRMED' if t['abstract'] else 'LOCATED'
out={}
rows=['| Node | OpenAlex ID | Year | Authors (first 3) | Title | Evidence type | Relation to central claim | Verification state of coding |','|---|---|---:|---|---|---|---|---|']
for t in top:
    c=code[t['node']]; rows.append(f"| {t['node']} | {t['id']} | {t['year']} | {clean(t['authors'])} | {clean(t['title'])[:110]} | {c[0]} | {c[1]} | {vstate(t)} |")
out['SECTION_B']='\n'.join(rows)
roles={'N01':'authors\' reply; OpenAlex identity conflated with AJR 2001','N02':'independent amplification hub ("Institutions Rule")','N03':'principal critique (human capital)','N05':'self-authored synthesis hub','N11':'self-authored synthesis hub (published)','N06':'methods paper using AJR data as worked example','N07':'likely database misattribution','N12':'rival-field review that preserves dispute','N14':'adjacent-field review; background','N09':'background in finance survey'}
rows=['| Rank | Paper | Year | Citation count | Evidence type | Role in network | Source of citation count |','|---:|---|---:|---:|---|---|---|']
for i,t in enumerate(top[:15],1):
    rows.append(f"| {i} | {clean(t['authors'])}: {clean(t['title'])[:90]} ({t['id']}) | {t['year']} | {t['cb']} | {code[t['node']][0]} | {roles.get(t['node'],code[t['node']][1])} | OpenAlex cited_by_count, query 2026-11-04T11:42Z UTC (raw/top50_citers.json) |")
out['A1']='\n'.join(rows)
rows=['| Recent paper | Year | Verification state | Cites founding cluster? | Cites hub? | Cites adjacent fields? | New evidence or recycling? |','|---|---:|---|---|---|---|---|']
nev={1:'new evidence on another question (China green innovation); AJR use not retrieved',2:'new methods evidence (gravity model); AJR use not retrieved',3:'new quasi-experimental evidence (China land titling); property-rights adjacent',4:'new cross-country evidence (women political empowerment)',5:'new cross-country evidence (economic complexity); co-cites critics',6:'new panel evidence (ecological footprint)',7:'methods guide; AJR likely an IV example (context not retrieved)',8:'new regional panel (West Africa poverty)',9:'new cross-country evidence (education quality)',10:'growth-empirics review (NBER Macro Annual)',11:'new panel (energy poverty)',12:'RETRACTED paper; excluded from inference',13:'conceptual review (informal institutions)',14:'new evidence (institutions and innovation)',15:'new panel (climate risk, TFP)',16:'new historical evidence (cultural origin, shareholder expropriation)',17:'new panel (FDI, Africa)',18:'qualitative case study (Indonesia)',19:'new firm-level evidence (China CSR)',20:'methods critique of persistence regressions (spatial noise)',21:'new panel (China carbon policy)',22:'new evidence (female entrepreneurs, institutions)',23:'new evidence (China energy risk)',24:'new aid-effectiveness evidence',25:'new panel (Africa human capital)'}
for r in rec:
    fc='yes (Reversal)' if 'RV' in r['flags'] else ('yes (handbook)' if 'HB' in r['flags'] else 'AJR 2001 only (by construction)')
    if 'RV' in r['flags'] and 'HB' in r['flags']: fc='yes (Reversal, handbook)'
    hub=[x for x,n in (('RO','Rodrik 2004'),('HB','AJR handbook')) if x in r['flags']]
    adj=[n for x,n in (('GL','Glaeser 2004'),('SA','Sachs 2003'),('AL','Albouy 2012')) if x in r['flags']]+(['locked source '+','.join(r['lock'])] if r['lock'] else [])
    vs='RECEPTION-CONFIRMED (reference list); '+('ABSTRACT-CONFIRMED' if r['abstract'] else 'LOCATED')
    rows.append(f"| R{r['rank']:02d} {clean(r['title'])[:90]} ({r['id']}) | {r['year']} | {vs} | {fc} | {', '.join(n for x,n in (('RO','Rodrik 2004'),('HB','AJR handbook')) if x in r['flags']) or 'no'} | {'; '.join(adj) or 'no'} | {nev[r['rank']]} |")
out['A3']='\n'.join(rows)
out['NODES']='; '.join(f"{t['node']}={t['id']}" for t in top)
out['EDGES']='; '.join(f"{a} -> {b}" for a,b in E)
out['GEPHI']='source,target\n'+'\n'.join(f"{a},{b}" for a,b in E)
out['N_E']=len(E)
json.dump(out,open(f'{B}/out/tables.json','w'),indent=1)
print(len(E), out['A3'][:300])
