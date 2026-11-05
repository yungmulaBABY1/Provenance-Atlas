import json,re
W=lambda u:u.split('/')[-1]
def ab(inv): return len(inv or {})
r1=json.load(open('raw/reception1_top50.json'))['results']
r1a={W(x['id']):ab(x['abstract_inverted_index']) for x in json.load(open('raw/reception1_abstracts.json'))['results']}
rc=json.load(open('raw/recent1_top25.json'))['results']
rca={W(x['id']):ab(x['abstract_inverted_index']) for x in json.load(open('raw/recent1_abstracts.json'))['results']}
def short(t,n=55):
    t=re.sub(r'\s+',' ',t or '').replace('|','/'); return t if len(t)<=n else t[:n].rstrip()+'…'
# --- RECEPTION-1 coding: id -> (relevance, relation, contribution, access, context, supported)
INS={
'W3124131699':('DIRECT (L1)','SUPPORTS+REUSES','REANALYSIS','FULL-TEXT (AER 2012 Reply PDF; record conflated with AJR 2001)','INSPECTED','p. 3078: answers Albouy\'s two data objections and re-estimates on the same series'),
'W2994756033':('DIRECT (L3-R1)','SUPPORTS+QUALIFIES+REUSES','REANALYSIS','FULL-TEXT (NBER WP 9305 version)','INSPECTED','RD-E1 p. 6 adopts the AJR instrument; RD-E4 p. 21 criticises the interpretive leap; also ADJ29 in ADJUDICATION-1'),
'W1977433163':('DIRECT (L3-R1)','SUPPORTS+QUALIFIES+REUSES','REANALYSIS','FULL-TEXT (NBER WP 9305; this record is that WP)','INSPECTED','RD-E1 p. 6; p. 34 uses AJR 64-country sample; duplicate record of N02'),
'W2890314743':('DIRECT (L3-R2)','CHALLENGES+REUSES','REANALYSIS','FULL-TEXT (NBER WP 10568 version)','INSPECTED','GL-E1, GL-E2 p. 24: malaria and human-capital rival channels tested on AJR instruments'),
'W2113844427':('BACKGROUND','MENTIONS','REVIEW','FULL-TEXT (NBER WP 10766; this record is that WP)','INSPECTED','p. 90: AJR in a list on endowments and institutions'),
'W1588189399':('BACKGROUND','MENTIONS','REVIEW','FULL-TEXT (NBER WP 10766 version of the chapter)','INSPECTED','p. 90 (WP version): same passage as N-Levine report; duplicate work'),
'W3123436326':('ADJACENT','SUPPORTS+REUSES','METHOD','FULL-TEXT (arXiv 1608.00060 version)','INSPECTED','DML-E1 p. 45 reuses the 64 AJR observations; DML-E2 p. 46 compares with AJR Table 4'),
'W2108614304':('ADJACENT','PREMISE+SUPPORTS','REVIEW','FULL-TEXT (NBER WP 10481; this record is that WP)','INSPECTED','HB-E1 p. 29 restates AJR 2001 magnitude; p. 28 premise for the synthesis'),
'W1580107285':('ADJACENT','PREMISE+SUPPORTS','REVIEW','FULL-TEXT (NBER WP 10481 version; published chapter not retrieved)','INSPECTED','HB-E1 p. 29 (WP version); duplicate work of N-Handbook WP'),
'W1480274481':('ADJACENT','QUALIFIES','REVIEW','FULL-TEXT (NBER WP 12832 version)','INSPECTED','HW-E1 p. 44: AJR geography finding "remains a disputed subject"'),
'W2104834906':('BACKGROUND','MENTIONS','REVIEW','FULL-TEXT (NBER WP 19578 version)','INSPECTED','p. 6: summarises the settler-mortality channel as background'),
'W3122513675':('DIRECT (L3-R1)','SUPPORTS+REUSES','REANALYSIS','FULL-TEXT (NBER WP 9106 version)','INSPECTED','EL-E1 p. 2 no direct germ effect beyond institutions; EL-E2 p. 15 settler mortality data compiled by AJR'),
'W2064927380':('BACKGROUND','MENTIONS','INDEPENDENT-DATA','FULL-TEXT (arXiv 0708.2090 version)','INSPECTED','p. 2 and p. 6: numbered citation (12,13) in a background list on institutions'),
'W3122778615':('BACKGROUND','MENTIONS','INDEPENDENT-DATA','FULL-TEXT (NBER WP 8178 version)','INSPECTED','reference list (WP p. 46): no in-text passage located; cited in the bibliography only'),
'W3125697804':('BACKGROUND','CITES-UNINSPECTED','REVIEW','FULL-TEXT (NBER WP 8573, 2001 version)','VERSION-MISMATCH','retrieved 2001 WP does not contain the AJR citation; published 2004 version not retrieved'),
'W2109890836':('BACKGROUND','CITES-UNINSPECTED','INDEPENDENT-DATA','FULL-TEXT (NBER WP 14132 version)','VERSION-MISMATCH','retrieved WP contains only an acknowledgment of Acemoglu, not the AJR 2001 citation'),
}
R1CODE={ # non-inspected ABSTRACT rows: relevance, contribution, note
'W3125412951':('ADJACENT','INDEPENDENT-DATA','AJR-team Reversal of Fortune (QJE)'),
'W3021593216':('ADJACENT','INDEPENDENT-DATA','AJR-team Reversal of Fortune (NBER record; duplicate work)'),
'W1484474409':('ADJACENT','INDEPENDENT-DATA','institutions x resource curse'),
'W4240669445':('ADJACENT','SHARED-DATA','Acemoglu-Johnson; abstract: colonial-history variation (shared instrument family)'),
'W2148534039':('ADJACENT','INDEPENDENT-DATA','culture and institutions, European regions'),
'W3123261979':('BACKGROUND','REVIEW','resource-curse survey'),
'W2145309110':('BACKGROUND','INDEPENDENT-DATA','slave trade and mistrust'),
'W3122357778':('ADJACENT','INDEPENDENT-DATA','AJR-team Rise of Europe'),
'W1934649023':('BACKGROUND','INDEPENDENT-DATA','governance indicators dataset'),
'W2155346737':('BACKGROUND','INDEPENDENT-DATA','real exchange rate and growth'),
'W2110434128':('BACKGROUND','REVIEW','corporate governance survey'),
'W3125767605':('BACKGROUND','THEORY','Acemoglu-team growth model'),
'W3023420463':('BACKGROUND','REVIEW','corruption survey'),
'W2789051288':('BACKGROUND','THEORY','state capacity model'),
'W4253884756':('BACKGROUND','REVIEW','civil war survey'),
'W2046507863':('BACKGROUND','THEORY','poverty traps'),
'W3123293195':('BACKGROUND','COMMENTARY','credibility revolution essay'),
'W2150851272':('ADJACENT','INDEPENDENT-DATA','economic geography rival (market access)'),
'W3121534672':('BACKGROUND','INDEPENDENT-DATA','AJR-team income and democracy'),
'W2591654989':('ADJACENT','REVIEW','culture and institutions review'),
'W2123148076':('BACKGROUND','THEORY','quality of government'),
'W2114854852':('BACKGROUND','REVIEW','causes of corruption review'),
'W3121354442':('BACKGROUND','INDEPENDENT-DATA','disaster death toll'),
'W3124568416':('ADJACENT','INDEPENDENT-DATA','within-country colonial institution (mita) RD design'),
'W2168966825':('BACKGROUND','INDEPENDENT-DATA','Protestant human capital'),
'W2152556759':('BACKGROUND','INDEPENDENT-DATA','output loss after crises'),
'W3125033761':('ADJACENT','THEORY','Acemoglu-Robinson persistence model'),
'W2490362664':('BACKGROUND','INDEPENDENT-DATA','redistribution US vs Europe'),
'W2556507681':(None,None,'book chapter; OpenAlex attribution of the AJR citation unverified'),
}
AJRNAMES=['Acemoğlu','Acemoglu','Simon Johnson','James A. Robinson','James Robinson']
def ajr(x): return any(any(k in (a['author']['display_name'] or '') for k in AJRNAMES) for a in x['authorships'])
rows=[]; sid={}
for i,x in enumerate(r1,1):
    w=W(x['id']); n=f'N{i:02d}'; sid[w]=n
    lab=f"{n} {w} {short(x['display_name'],48)} ({x['publication_year']})"
    mem='RECEPTION-1+ADJUDICATION-1' if w=='W2994756033' else 'RECEPTION-1'
    if w in INS:
        rel,relat,con,acc,ctx,sup=INS[w]
    else:
        has=r1a.get(w,0)>0
        acc='ABSTRACT (OpenAlex abstract)' if has else 'METADATA (OpenAlex record)'
        c=R1CODE.get(w)
        if has and c and c[0]:
            rel,con,note=c; sup=f'abstract-coded: {note}; citation present in OpenAlex refs, use not inspected'
        else:
            rel,con='UNKNOWN','UNKNOWN'; sup='metadata only; citation present in OpenAlex refs; relevance not coded'+(f' ({c[2]})' if c else '')
        relat,ctx='CITES-UNINSPECTED','NOT-INSPECTED'
    rows.append(dict(sid=n,w=w,label=lab,mem=mem,rel=rel,relat=relat,con=con,acc=acc,ctx=ctx,sup=sup,ajr=ajr(x)))
# --- RECENT-1
RINS={'W4292663674':('BACKGROUND','MENTIONS','REVIEW','FULL-TEXT (Springer JIBS PDF)','INSPECTED','p. 8: AJR in a background list of institutional-theory works; p. 11; reference list p. 20'),
      'W4391180104':('BACKGROUND','MENTIONS','INDEPENDENT-DATA','FULL-TEXT (HAL preprint version)','INSPECTED','p. 22, §4.3: cited as precedent for endogeneity; reference list p. 41')}
RREL={'W3165371825':'ADJACENT','W4376140760':'ADJACENT','W4386028756':'ADJACENT'}
SAMPLED=['W4223529822','W4292663674','W4292849668','W4319016949','W4387877962','W4391180104']
FAILNOTE={'W4223529822':'sampled; full text not retrieved (DOI HTTP 403)','W4292849668':'sampled; full text not retrieved (DOI HTTP 403)','W4319016949':'sampled; full text not retrieved (repository HTTP 403, curl fallback 403)','W4387877962':'sampled; full text not retrieved (repository HTTP 500 x3)'}
for i,x in enumerate(rc,1):
    w=W(x['id']); n=f'R{i:02d}'; sid[w]=n
    lab=f"{n} {w} {short(x['display_name'],48)} ({x['publication_year']})"
    if w in RINS:
        rel,relat,con,acc,ctx,sup=RINS[w]; sup='sampled (seed 20261104); '+sup if False else sup
    else:
        has=rca.get(w,0)>0
        acc='ABSTRACT (OpenAlex abstract)' if has else 'METADATA (OpenAlex record)'
        if has: rel=RREL.get(w,'BACKGROUND'); con='INDEPENDENT-DATA'; sup='abstract-coded; uses AJR for another question; use not inspected'
        else: rel,con='UNKNOWN','UNKNOWN'; sup='metadata only; relevance not coded'
        if w=='W4386322040': sup='RETRACTED article; abstract-coded; excluded from inference'
        if w in FAILNOTE: sup=FAILNOTE[w]+'; '+sup
        relat,ctx='CITES-UNINSPECTED','NOT-INSPECTED'
    rows.append(dict(sid=n,w=w,label=lab,mem='RECENT-1',rel=rel,relat=relat,con=con,acc=acc,ctx=ctx,sup=sup,ajr=ajr(x)))
# --- ADJUDICATION-1
txt=open('adj_dump.txt').read()
blocks=re.split(r'^### ',txt,flags=re.M)[1:]
SCR={}
for k,v in {'DIRECT (L1)':'01 02 11 03 05 06 07 39','DIRECT (L3-R1)':'09 15 17 18 24 29 30 31 36 38 41 43 33','DIRECT (L3-noSM)':'12 14 49',
 'ADJACENT':'13 16 19 20 22 23 32 35 45 47 48 51 52 53 54','BACKGROUND':'04 08 10 21 25 27 28 34 42 46 50 55 56 57 58','UNRELATED':'26 40','UNKNOWN':'37 44'}.items():
    for a in v.split(): SCR['ADJ'+a]=k
CON={'ADJ39':'METHOD','ADJ41':'METHOD','ADJ12':'INDEPENDENT-DATA','ADJ14':'INDEPENDENT-DATA','ADJ49':'INDEPENDENT-DATA','ADJ32':'REVIEW','ADJ35':'COMMENTARY','ADJ03':'REANALYSIS'}
NOTE={'ADJ01':'unreviewed Zenodo deposit; AR sets [0.71, 1.43] at baseline, unbounded under Albouy revisions','ADJ02':'Auer comment: settler-mortality data dispute','ADJ11':'Auer: second record of the same comment','ADJ03':'AJR 2005 response to Albouy','ADJ05':'Assenova-Regele revisit colonial-institutions effect','ADJ06':'Olsson comment on AJR','ADJ07':'title only: replication of institutions-development evidence',
 'ADJ09':'Bleaney-Dimico: geography matters','ADJ15':'Bleaney-Dimico: geographical influences','ADJ17':'alternative geography and institution variables','ADJ18':'Bhattacharyya: malaria matters for African underdevelopment','ADJ24':'Chakraborty: institutions matter','ADJ30':'IMF/NBER record of Institutions Rule','ADJ31':'IMF WP record of Institutions Rule','ADJ36':'Carstensen-Gundlach 2012 record','ADJ38':'Carstensen-Gundlach: direct income effects of malaria','ADJ41':'BMA for IV; malaria-institutions application','ADJ43':'Presbitero: institutions and geography','ADJ33':'Kourtellos et al.: heterogeneity in institutions vs geography','ADJ39':'distributional IV method; AJR application','ADJ12':'title only: historical malaria and institutions','ADJ14':'historical malaria instrument (dissertation)','ADJ49':'Rigobon-Rodrik: identification through heteroskedasticity'}
adjids={}
for b in blocks:
    head,rest=b.split('\n',1)
    m=re.match(r'(ADJ\d+) (W\d+) (\S+) \| (\d+)',head); a,w,q,yr=m.groups()
    cites=re.search(r'cites AJR2001\(OA refs\): (\S)',head).group(1)
    nrefs=re.search(r'nrefs (\d+)',head); nrefs=int(nrefs.group(1)) if nrefs else 0
    title=re.search(r'TITLE: (.*)',rest).group(1)
    absw=int(re.search(r'ABS\((\d+)w\)',rest).group(1)); abstext=rest
    adjids[a]=w
    if w in sid: continue
    n=a; sid[w]=n
    rel=SCR[a]; head_rel=rel.split()[0]
    if head_rel=='DIRECT': con=CON.get(a,'REANALYSIS')
    elif head_rel=='ADJACENT': con=CON.get(a,'INDEPENDENT-DATA')
    elif head_rel in('BACKGROUND','UNRELATED'): con='NONE'
    else: con='UNKNOWN'
    acc='ABSTRACT (OpenAlex abstract)' if absw>0 else 'METADATA (OpenAlex record)'
    names_ajr=bool(re.search(r'Acemoglu|AJR|Acemo',abstext))
    if cites=='Y': relat,ctx='CITES-UNINSPECTED','NOT-INSPECTED'
    elif cites=='N' and nrefs>0 and head_rel not in('DIRECT','UNKNOWN') and not names_ajr: relat,ctx='NOT-CITING','NOT-APPLICABLE'
    else: relat,ctx='UNKNOWN','NOT-INSPECTED'
    sup=('title-coded from METADATA; ' if absw==0 and head_rel!='UNKNOWN' else '')+f'{q}; screened {rel}'+(f'; {NOTE[a]}' if a in NOTE else '')
    if relat=='NOT-CITING': sup+='; OpenAlex refs (n='+str(nrefs)+') omit AJR 2001'
    rows.append(dict(sid=n,w=w,label=f'{n} {w} {short(title,48)} ({yr})',mem='ADJUDICATION-1',rel=rel,relat=relat,con=con,acc=acc,ctx=ctx,sup=sup,ajr=False))
# --- OUTSIDE
OUT=[('X01','W3124166904 AJR 2001 Colonial Origins (target)','DIRECT (L1)','NOT-CITING','INDEPENDENT-DATA','FULL-TEXT (AER 2001 PDF)','NOT-APPLICABLE','target source; AJR-E2 p. 20, AJR-E4 p. 24 used as source passages'),
('X02','W1969918011 Albouy 2012 AER Comment','DIRECT (L1)','CHALLENGES','REANALYSIS','FULL-TEXT (JSTOR mirror PDF)','INSPECTED','p. 3060: mortality rates for many of the 64 countries argued non-comparable'),
('X03','NBER w9490 Sachs 2003 Institutions don\'t rule','DIRECT (L3-R1)','CHALLENGES','REANALYSIS','FULL-TEXT (NBER WP 9490)','INSPECTED','SA-E1 p. 10: AJR-style null rejected using malaria risk'),
('X04','Nobel 2024 scientific background','ADJACENT','QUALIFIES','REVIEW','FULL-TEXT (nobelprize.org PDF)','INSPECTED','NS-E1, NS-E2, NS-E3 p. 19: grain of salt; Albouy; human capital hard to distinguish'),
('X05','Nobel 2024 popular background','ADJACENT','SUPPORTS','COMMENTARY','FULL-TEXT (nobelprize.org PDF)','INSPECTED','NP-E1 p. 4: "a clear chain of causality"'),
('X06','W139828295 Malawi household malaria cost (1994)','ADJACENT','NOT-CITING','INDEPENDENT-DATA','ABSTRACT (v1 reused)','NOT-APPLICABLE','v1 Section E locked source F1; predates target'),
('X07','W2088758477 Gambia malaria risk factors (1995)','ADJACENT','NOT-CITING','INDEPENDENT-DATA','ABSTRACT (v1 reused)','NOT-APPLICABLE','v1 Section E locked source F1; predates target'),
('X08','W2618788771 Gallup, Sachs & Mellinger (1999)','ADJACENT','NOT-CITING','INDEPENDENT-DATA','ABSTRACT (v1 reused)','NOT-APPLICABLE','v1 Section E locked source F2; predates target'),
('X09','W1492460295 Development, geography, and economic theory','ADJACENT','UNKNOWN','THEORY','ABSTRACT (v1 reused)','NOT-INSPECTED','v1 Section E locked source F2; date not re-verified'),
('X10','W3121822366 Becker, Murphy & Tamura (1990)','ADJACENT','NOT-CITING','THEORY','ABSTRACT (v1 reused)','NOT-APPLICABLE','v1 Section E locked source F3; predates target'),
('X11','W2035652178 Glomm & Ravikumar (1992)','ADJACENT','NOT-CITING','THEORY','ABSTRACT (v1 reused)','NOT-APPLICABLE','v1 Section E locked source F3; predates target'),
('X12','W2165144879 Staiger & Stock (1997)','ADJACENT','NOT-CITING','METHOD','ABSTRACT (v1 reused)','NOT-APPLICABLE','v1 Section E locked source F4; predates target'),
('X13','W1980412904 Bound, Jaeger & Baker (1995)','ADJACENT','NOT-CITING','METHOD','ABSTRACT (v1 reused)','NOT-APPLICABLE','v1 Section E locked source F4; predates target'),
('X14','W3121147769 North (1990) record, mis-typed','BACKGROUND','NOT-CITING','THEORY','ABSTRACT (v1 reused)','NOT-APPLICABLE','v1 Section E locked source F6; predates target'),
('X15','W2010235856 Knack & Keefer (1995)','ADJACENT','NOT-CITING','INDEPENDENT-DATA','ABSTRACT (v1 reused)','NOT-APPLICABLE','v1 Section E locked source F6; source of the PRS data; predates target')]
for o in OUT:
    rows.append(dict(sid=o[0],w=o[1].split()[0],label=f'{o[0]} {o[1]}',mem='OUTSIDE',rel=o[2],relat=o[3],con=o[4],acc=o[5],ctx=o[6],sup=o[7],ajr=False))
json.dump(dict(rows=rows,sid=sid,adjids=adjids),open('out/ledger.json','w'),indent=0,ensure_ascii=False)
from collections import Counter
for c in ['RECEPTION-1','RECENT-1','ADJUDICATION-1']:
    m=[r for r in rows if c in r['mem'].split('+')]
    print(c,len(m),'INSPECTED',sum(r['ctx']=='INSPECTED' for r in m),Counter(r['rel'].split()[0] for r in m),Counter(r['con'] for r in m),Counter(r['acc'].split()[0] for r in m),Counter(r['ctx'] for r in m),Counter(r['relat'] for r in m))
print(len(rows))
