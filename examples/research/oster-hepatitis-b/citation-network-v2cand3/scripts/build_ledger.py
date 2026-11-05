"""Builds the SOURCE ELIGIBILITY LEDGER rows for 02c (Oster 2005) from raw/ and hand codes.
No abstracts are read; coding is from titles/metadata, S2 excerpts (CTX-E ids) or full text."""
import json, collections
R=json.load(open('raw/reception1_top50.json'))['results']
C=json.load(open('raw/recent1_top25.json'))['results']
A={q:json.load(open(f'raw/adj1_Q{q}.json'))['results'] for q in range(1,6)}
T='W3123222584'; TP='W3126094291'
def wid(w): return w['id'][21:]
def short(t,n=48):
    t=' '.join(t.split()); return t if len(t)<=n else t[:n].rstrip()+'…'
# ---------- RECEPTION-1 / RECENT-1 hand codes: id -> (relevance, relation, contribution, access, context, supported)
M='METADATA (OpenAlex record)'
def meta(rel,contrib,note): return (rel,'CITES-UNINSPECTED',contrib,M,'NOT-INSPECTED',f'title-coded from METADATA; {note}; citation present in OpenAlex refs, use not inspected')
EX='EXCERPT (Semantic Scholar citation context; s2/ response sha256 c570ae9f…, not committed)'
codes={
'N01':meta('ADJACENT (R1)','INDEPENDENT-DATA','sex-specific earnings and sex imbalance (QJE)'),
'N02':meta('DIRECT (R1)','INDEPENDENT-DATA','one-child policy and missing girls'),
'N03':('BACKGROUND','MENTIONS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E1: lists Oster 2005 as "greater incidence of female-biased diseases" (mechanism misdescribed)'),
'N04':('ADJACENT (L3)','MENTIONS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E2: "a recent debate on the effect of Hepatitis B on sex ratios" (cites Lin & Luoh, Oster et al.); K7'),
'N05':('ADJACENT','QUALIFIES','REVIEW',EX,'INSPECTED','CTX-E3: Oster 2005 used as an example of critiques and replication (Das Gupta 2006; Lin & Luoh 2008; Oster et al. 2010)'),
'N06':meta('BACKGROUND','REVIEW','handbook chapter on kinship networks'),
'N07':('DIRECT (R1)','QUALIFIES','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E4: "raised the possibility" HBV accounts for "about 70%" of China\'s missing women; "Das Gupta (2005) questioned"'),
'N08':meta('DIRECT (R1)','INDEPENDENT-DATA','birth-order evidence on missing women (K1); full text not retrieved'),
'N09':meta('BACKGROUND','INDEPENDENT-DATA','fertility incentives; one work under two records (N09 REStat 2013, N35 NBER WP 2007)'),
'N10':meta('BACKGROUND','INDEPENDENT-DATA','sex ratios and savings (uses sex ratios for another question)'),
'N11':('ADJACENT (R1)','MENTIONS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E5, CTX-E6: HBV "can partly explain" high boy-birth shares; "around 75%" China vs "around 17%" India'),
'N12':('ADJACENT','SUPPORTS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E7: author self-citation, HBV "responsible for around 20% of the (historical) gender imbalance in India"'),
'N13':('ADJACENT (L1)','SUPPORTS','REVIEW',EX,'INSPECTED','CTX-E8: Chahnazarian et al. summarised the work "and the result confirmed by Oster (2005)"'),
'N14':meta('DIRECT (R1)','INDEPENDENT-DATA','dynamic model of sex selection in China'),
'N15':('DIRECT (R1)','QUALIFIES','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E9: HBV level hypothesis cited "although see Oster forthcoming"; trends rule out level explanations'),
'N16':('ADJACENT (R1)','MENTIONS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E10: rising SRB attributed to "biological factors, as Oster (…)" or to behaviour (passage truncated by S2)'),
'N17':('BACKGROUND','MENTIONS','REVIEW',EX,'INSPECTED','CTX-E11: HBV "may offer a supplemental biological mechanism" for regional sex-ratio patterns'),
'N18':meta('BACKGROUND','INDEPENDENT-DATA','birth-weight structural model'),
'N19':('UNRELATED','CITES-UNINSPECTED','NONE',M,'NOT-INSPECTED','title-coded from METADATA; income inequality and CO2; the OpenAlex citation link to the target is implausible (RECORD QUALITY); also RECENT-1 member R01'),
'N20':meta('DIRECT (R1)','INDEPENDENT-DATA','one-child policy, ethnic minorities and male-biased sex ratios'),
'N21':meta('ADJACENT','REVIEW','Annual Review of Sociology review of skewed sex ratios; possible review hub'),
'N22':meta('BACKGROUND','REVIEW','health handbook chapter'),
'N23':meta('DIRECT (R1)','INDEPENDENT-DATA','legal ban on sex-selective abortion, India'),
'N24':meta('DIRECT (R1)','INDEPENDENT-DATA','Oster-authored decomposition of India\'s sex imbalance'),
'N25':('DIRECT (R1)','CHALLENGES','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E12: the model "ignores the suggestion by Blumberg" that immunity moves the sex ratio the other way; also ADJUDICATION-1 (Q2)'),
'N26':meta('BACKGROUND','INDEPENDENT-DATA','sex ratios and entrepreneurship (a different work from N10)'),
'N27':('ADJACENT (R1)','MENTIONS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E13: "prevalence of Hepatitis B (Oster, 2005)" in a list of sex-ratio factors'),
'N28':meta('BACKGROUND','REVIEW','World Bank book on work and family'),
'N29':('BACKGROUND','MENTIONS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E14: results "not necessarily incompatible with the potential effect of the hepatitis B virus"'),
'N30':meta('BACKGROUND','INDEPENDENT-DATA','prenatal investment by child sex'),
'N31':('DIRECT (R2)','CHALLENGES','INDEPENDENT-DATA','FULL-TEXT (VERSION-SUBSTITUTE: author working-paper version 2008, homepage.ntu.edu.tw; AER version not retrieved)','INSPECTED','LL-E1 p. 1: effect "ranges only from 0.0010 to 0.0025"; LL-E2 p. 14: HBV has no effect on SRB; CTX-E15 restates "roughly half"; K2; also ADJUDICATION-1 (Q2)'),
'N32':meta('ADJACENT (R1)','INDEPENDENT-DATA','patrilocality and missing women; also ADJUDICATION-1 (Q2)'),
'N33':('ADJACENT','MENTIONS','THEORY',EX,'INSPECTED','CTX-E16: "argument by Oster (2005) that hepatitis B infection raises the probability of having a boy"'),
'N34':('ADJACENT (L2)','MENTIONS','COMMENTARY',EX,'INSPECTED','CTX-E17: "Oster (2005) argues that hepatitis B may result in excessive male births"'),
'N36':('ADJACENT','MENTIONS','REVIEW',EX,'INSPECTED','CTX-E18: Drew et al. and Oster "contend that medical studies indicate" HBV mothers have fewer girls (2015; no refutation in passage)'),
'N37':('BACKGROUND','MENTIONS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E19: footnote list of sex-ratio studies incl. Oster 2005, Lin & Luoh 2008, Oster et al. 2008'),
'N38':('ADJACENT','MENTIONS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E20: whether there is "a biological dimension" (Das Gupta 2006; Oster 2005)'),
'N39':meta('BACKGROUND','REVIEW','JEP essay on biology and family economics'),
'N40':('BACKGROUND','CITES-UNINSPECTED','INDEPENDENT-DATA',EX,'NOT-INSPECTED','S2 returned a truncated context that does not show the citation; use not inspected'),
'N41':meta('BACKGROUND','INDEPENDENT-DATA','gender discrimination, Pakistan'),
'N42':meta('ADJACENT','INDEPENDENT-DATA','sex-specific fetal loss in mice; citation plausibly genuine (mechanism)'),
'N43':meta('DIRECT (R1)','INDEPENDENT-DATA','ultrasonography and sex ratios in China'),
'N44':('UNRELATED','CITES-UNINSPECTED','NONE',M,'NOT-INSPECTED','title-coded from METADATA; prenatal smoking and the 1998 Master Settlement; the OpenAlex citation link to the target is implausible (RECORD QUALITY)'),
'N45':('DIRECT (R2)','CHALLENGES','INDEPENDENT-DATA','FULL-TEXT (VERSION-SUBSTITUTE: NBER WP w13971, 2008; Economics Letters 2010 version not retrieved)','INSPECTED','OC-E1 p. 7: offspring of carrier vs non-carrier fathers 51.06% vs 51.56% male; OC-E2 p. 8: HBV carrier rates "cannot explain" China\'s male-biased sex ratios; K3; Oster co-author'),
'N46':('DIRECT (L3)','CHALLENGES','COMMENTARY',EX,'INSPECTED','CTX-E21: restates "75 percent of the \'missing women\' in China" before contesting it (title: Response to Oster); K5'),
'N47':meta('DIRECT (R1)','INDEPENDENT-DATA','abortion legalisation and sex ratios at birth, Taiwan'),
'N48':('ADJACENT (R1)','MENTIONS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E22: HBV "biological explanation" listed beside the socio-economic explanation'),
'N49':('BACKGROUND','QUALIFIES','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E23: "her evidence, at least for China, has been widely criticized"'),
'N50':('BACKGROUND','MENTIONS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E24: Oster 2005 cited for Nepal being at risk of anti-girl bias'),
'R02':meta('ADJACENT (R1)','INDEPENDENT-DATA','pensions and son preference, rural China'),
'R03':('DIRECT (R2)','CHALLENGES','INDEPENDENT-DATA','FULL-TEXT (PMC11137505, Europe PMC full-text XML; not committed)','INSPECTED','BA-E1 §1: restates "about 75 %" China and "about 20 %" South Asia; BA-E2 §4: no association between maternal HBsAg and offspring sex'),
'R04':('ADJACENT (R1)','MENTIONS','INDEPENDENT-DATA',EX,'INSPECTED','CTX-E25: Oster (2005) "reported that women infected with … HBV are more likely to give birth to boys" (2025; no refutation in passage)'),
'R05':meta('BACKGROUND','INDEPENDENT-DATA','dissertation on culture and institutions'),
'R06':meta('BACKGROUND','THEORY','dissertation on family, fertility and health models'),
}
rows=[]  # (sid, label, membership, rel, relation, contrib, access, context, supported)
recids={wid(w):f'N{i:02d}' for i,w in enumerate(R,1)}
for i,w in enumerate(R,1):
    sid=f'N{i:02d}'
    if sid=='N35': continue
    mem=['RECEPTION-1']
    if sid in ('N08','N25','N31','N32'): mem.append('ADJUDICATION-1')
    if sid=='N19': mem.append('RECENT-1')
    label=f"{sid} {wid(w)}"+(" + W1581958734 (N35 record)" if sid=='N09' else '')+f" {short(w['display_name'])} ({w['publication_year']})"
    rows.append((sid,label,'+'.join(mem),*codes[sid]))
for i,w in enumerate(C,1):
    sid=f'R{i:02d}'
    if sid=='R01': continue
    rows.append((sid,f"{sid} {wid(w)} {short(w['display_name'])} ({w['publication_year']})",'RECENT-1',*codes[sid]))
# ---------- ADJUDICATION-1 (non-overlapping works)
adj={  # wid: (label_extra, rel, relation, contrib, access, context, supported)
'W2089286174':('ADJACENT (L1)','UNKNOWN','REVIEW','Q1; Blumberg essay on HBV, sex ratio and demography; OpenAlex refs (7) omit the target but are incomplete'),
'W63810618':('DIRECT (L1)','NOT-CITING','INDEPENDENT-DATA','Q1; reprint (2000) of Drew et al. 1982 Kar Kar island family study; predates target (cited by target as Drew et al. 1982)'),
'W195581690':('DIRECT (L1)','NOT-CITING','INDEPENDENT-DATA','Q1; Greenland family study (1986); predates target; Section E locked source F2; cited by target'),
'W2391923276':('DIRECT (L1)','UNKNOWN','INDEPENDENT-DATA','Q1; Chinese retrospective study of maternal HBV and offspring sex ratio (2010); result not read (no full text; abstracts not used)'),
'W2415116130':('ADJACENT (L1)','NOT-CITING','COMMENTARY','Q1; HBV, sex ratio and H-Y antigen (1980); predates target'),
'W2129626017':('DIRECT (L1)','NOT-CITING','INDEPENDENT-DATA','Q1 and Q5; four-population comparison (1988); predates target; K8; Section E locked source F2; cited by target'),
'W1969795863':('DIRECT (L1)','NOT-CITING','INDEPENDENT-DATA','Q1; offspring sex ratio of HBV mothers (2000); predates target; not in the target bibliography; result not read'),
'W2166552078':('ADJACENT (L1)','UNKNOWN','THEORY','Q1; James 2007 hypothesis note on HBV carriers\' offspring sex ratios'),
'W4235601100':None,  # merged with Drew 1978 (X row)
'W2355691234':('DIRECT (L1)','UNKNOWN','INDEPENDENT-DATA','Q1; HBV in pregnant women and offspring sex ratio (2007, Chinese journal); result not read'),
'W2964809941':('ADJACENT (R1)','UNKNOWN','INDEPENDENT-DATA','Q2; one-child policy and sex ratio at birth (SSRN 2019)'),
'W2978580588':('ADJACENT (L3)','UNKNOWN','REVIEW','Q2; Klasen chapter "Missing Women" (2009); possibly K6 (not counted as returned)'),
'KIM':('ADJACENT (R1)','UNKNOWN','INDEPENDENT-DATA','Q2; baby bonus, fertility and missing women; one work under two records (SSRN preprint and JHR article)'),
'W2147178406':('DIRECT (R1)','NOT-CITING','INDEPENDENT-DATA','Q3; provincial son preference and SRB in China (1997); predates target'),
'W2552766914':('DIRECT (R1)','UNKNOWN','INDEPENDENT-DATA','Q3; SRB decomposition by birth order, China'),
'W3162357794':('ADJACENT (R1)','UNKNOWN','INDEPENDENT-DATA','Q3; recent SRB in China'),
'W2355836375':('DIRECT (R1)','UNKNOWN','INDEPENDENT-DATA','Q3; parity-intensification effect, China'),
'W3009429537':('DIRECT (R1)','UNKNOWN','INDEPENDENT-DATA','Q3; son preference and SRB by birth order, India'),
'W2912981086':('ADJACENT (R1)','UNKNOWN','REVIEW','Q3; review of China\'s SRB imbalance; OpenAlex refs (47) omit the target but are incomplete'),
'W2020683083':('DIRECT (R1)','UNKNOWN','INDEPENDENT-DATA','Q3; SRB in India by birth order and sex of previous children'),
'W2753884747':('BACKGROUND','NOT-CITING','INDEPENDENT-DATA','Q3; birth order, son preference and child height; OpenAlex refs (64) omit the target'),
'W2043906799':('ADJACENT (R1)','UNKNOWN','INDEPENDENT-DATA','Q3; daughter discrimination and future SRB, India'),
'W961876696':('DIRECT (R1)','UNKNOWN','INDEPENDENT-DATA','Q3; parity structure and SRB imbalance, China'),
'W2021092087':('ADJACENT (R4)','UNKNOWN','REVIEW','Q4; behavioural and biological determinants of SRB (James 2010)'),
'W2026289855':('ADJACENT (R1)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q4; skewed SRB in India; OpenAlex refs contain the target; use not inspected'),
'W2116894238':('ADJACENT (R1)','UNKNOWN','INDEPENDENT-DATA','Q4; rising SRB in Viet Nam'),
'W2087034505':('ADJACENT (R4)','UNKNOWN','METHOD','Q4; model-based SRB'),
'W2901780678':('BACKGROUND','UNKNOWN','INDEPENDENT-DATA','Q4; SRB trends in Slovenia; no OpenAlex refs'),
'W2792316282':('ADJACENT (R4)','UNKNOWN','INDEPENDENT-DATA','Q4; SRB and health or socio-economic indicators'),
'W2795258545':('BACKGROUND','UNKNOWN','INDEPENDENT-DATA','Q4; infanticide and SRB in Italy; OpenAlex refs (1) too sparse to code'),
'W2016338915':('ADJACENT (R4)','UNKNOWN','INDEPENDENT-DATA','Q4; SRB negatively related to mortality'),
'W4407172282':('ADJACENT (R1)','UNKNOWN','INDEPENDENT-DATA','Q4; prenatal care, son preference and SRB (2025)'),
'W2393854264':('ADJACENT (R4)','UNKNOWN','INDEPENDENT-DATA','Q4; multifactor analysis of SRB (Chinese journal)'),
'W2875903878':('UNRELATED','UNKNOWN','NONE','Q5; HBV immunisation in kidney disease; no OpenAlex refs'),
'W2890595746':('UNRELATED','NOT-CITING','NONE','Q5; post-vaccine HBV immunity, Burkina Faso; OpenAlex refs (8) omit the target'),
'W4405823174':('UNRELATED','UNKNOWN','NONE','Q5; HBV vaccine response in dialysis; no OpenAlex refs'),
'W7117136974':('UNRELATED','NOT-CITING','NONE','Q5; HBV prevalence and vaccination among HIV patients, Chad; OpenAlex refs (9) omit the target'),
'W2185955083':('BACKGROUND','NOT-CITING','NONE','Q5; HBV and primary hepatic carcinoma (2000 reprint of a Blumberg paper); predates target'),
'W4226002143':('UNRELATED','NOT-CITING','NONE','Q5; HBV vaccination timeliness in children; OpenAlex refs (9) omit the target'),
'W7163756956':('UNRELATED','UNKNOWN','NONE','Q5; HBV vaccination in haemodialysis; no OpenAlex refs'),
'W7114766517':('UNRELATED','NOT-CITING','NONE','Q5; HBV vaccine response in kidney failure; OpenAlex refs (5) omit the target'),
}
seen=set(); k=0; adjrows=[]
allw={}
for q in range(1,6):
    for w in A[q]:
        allw.setdefault(wid(w),w)
order=[]
for q in range(1,6):
    for w in A[q]:
        i=wid(w)
        if i in ('W3133548684','W4403147335'): i='KIM'
        if i in order: continue
        order.append(i)
for i in order:
    if i in (T,TP) or i in recids or adj.get(i,0) is None: continue
    k+=1; sid=f'A{k:02d}'
    rel,relation,contrib,note=adj[i]
    if i=='KIM':
        w=allw['W4403147335']; label=f"{sid} W4403147335 + W3133548684 {short(w['display_name'])} (2024)"
    else:
        w=allw[i]; label=f"{sid} {i} {short(w['display_name'])} ({w['publication_year']})"
    ctx='NOT-APPLICABLE' if relation=='NOT-CITING' else 'NOT-INSPECTED'
    rows.append((sid,label,'ADJUDICATION-1',rel,relation,contrib,M,ctx,f'title-coded from METADATA; {note}'))
# target row (returned by Q2 and Q5)
rows.append(('T01','T01 W3123222584 + W3126094291 (RePEc preprint record) Hepatitis B and the Case of the Missing Women (2005) — target','ADJUDICATION-1','DIRECT (L1)','NOT-CITING','INDEPENDENT-DATA','FULL-TEXT (JPE 113(6) PDF, institutional access copy; not committed)','NOT-APPLICABLE','target source returned by Q2 and Q5; JP-E1 p. 1172, JP-E2 p. 1179, JP-E3 p. 1201, JP-E4 and JP-E5 p. 1203, JP-E6 p. 1189 used as source passages'))
# Drew 1978 merged row
rows.append(('X01','X01 W2023743440 + W4235601100 (2000 reprint record) Hepatitis B Virus and Sex Ratio of Offspring (Drew, London, Lustbader 1978)','ADJUDICATION-1','DIRECT (L1)','NOT-CITING','INDEPENDENT-DATA',M,'NOT-APPLICABLE','title-coded from METADATA; Science 1978 family study and its 2000 reprint (Q1); predates target; Section E locked source F2; cited by target'))
X=[
('X02','X02 Slate 2005, "Where did 100 million missing women go?" (Landsburg)','OUTSIDE','ADJACENT (L3)','SUPPORTS','COMMENTARY','FULL-TEXT (slate.com HTML, HTTP 200; not committed)','INSPECTED','SL-E1: if the results are "extremely compelling", her work "has established the fate of roughly 50 million" missing women (conditional)'),
('X03','X03 Klasen 2005, "Comments on Paper by Emily Oster" (Göttingen working note, 8 July 2005)','OUTSIDE','DIRECT (R4)','QUALIFIES','COMMENTARY','FULL-TEXT (uni-goettingen.de PDF, HTTP 200; not committed)','INSPECTED','KL-E1 p. 1: with a life-expectancy-adjusted SRB benchmark the total would "end up close to" Coale\'s 60 million'),
]
sec={'F1':[('W1992232430','Mothers and Sons: Preference Formation and Female Labor Force Dynamics (Fernández, Fogli & Olivetti 2004)','BACKGROUND','INDEPENDENT-DATA','off-topic hit for "son preference"; retained, not replaced'),
           ('W2139821597','Why is son preference so persistent in East and South Asia? (Das Gupta et al. 2003)','ADJACENT (R1)','REVIEW','not cited by target'),
           ('W2074655452','Son preference and sex composition of children: evidence from India (Clark 2000)','ADJACENT (R1)','INDEPENDENT-DATA','not cited by target')],
     'F3':[('W1973842394','Maternal dominance, breeding success and birth sex ratios in red deer (Clutton-Brock et al. 1984)','BACKGROUND','INDEPENDENT-DATA','animal sex-ratio biology; not cited by target'),
           ('W2249723975','Causes and implications of the recent increase in the reported sex ratio at birth in China (Zeng Yi et al. 1993)','DIRECT (R1)','INDEPENDENT-DATA','cited by target as Yi et al. 1993 (JP-E1)'),
           ('W2083763800','Evidence that mammalian sex ratios at birth are partially controlled by parental hormone levels (James 1996)','ADJACENT (L1)','THEORY','not cited by target (James 1987a, 1987b cited instead)')],
     'F4':[('W2081758747','Missing Women: Revisiting the Debate (Klasen & Wink 2003)','DIRECT (R4)','INDEPENDENT-DATA','not cited by target'),
           ('W3124113130','A Turning Point in Gender Bias in Mortality? (Klasen & Wink 2002)','DIRECT (R4)','INDEPENDENT-DATA','cited by target (JP-E4, n. 26)'),
           ('W2031660749','"Missing Women" Reconsidered (Klasen 1994)','DIRECT (R4)','INDEPENDENT-DATA','cited by target')]}
n=3
for f,lst in sec.items():
    for w,t,rel,con,note in lst:
        n+=1
        X.append((f'X{n:02d}',f'X{n:02d} {w} {t}','OUTSIDE',rel,'NOT-CITING',con,M,'NOT-APPLICABLE',f'title-coded from METADATA; Section E locked source {f}; predates target; {note}'))
rows+=X
PH={'N04':'; POST HOC adjudication member (known item K7, not returned by the ADJUDICATION-1 search)',
'N45':'; POST HOC adjudication member (known item K3, not returned by the ADJUDICATION-1 search)',
'N46':'; POST HOC adjudication member (known item K5, not returned by the ADJUDICATION-1 search)',
'R03':'; POST HOC adjudication member (located via RECENT-1, not by the ADJUDICATION-1 search)'}
rows=[tuple(r[:8])+(r[8]+PH.get(r[0],''),) for r in rows]
json.dump(rows,open('out/ledger_rows.json','w'),indent=0,ensure_ascii=False)
print(len(rows))
mem=collections.Counter()
for r in rows:
    for m in r[2].split('+'): mem[m]+=1
print(mem)
for cid in ('RECEPTION-1','RECENT-1','ADJUDICATION-1'):
    ms=[r for r in rows if cid in r[2].split('+')]
    print(cid,len(ms),'inspected',sum(r[7]=='INSPECTED' for r in ms))
    for col,ix in (('relevance',3),('contribution',5)):
        c=collections.Counter(r[ix].split('(')[0].strip() for r in ms); print(' ',col,dict(sorted(c.items())))
