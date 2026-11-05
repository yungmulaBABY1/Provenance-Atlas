"""Builds the SOURCE ELIGIBILITY LEDGER rows for 02c (Baumeister et al. 1998) from raw/ and hand codes.
No abstracts are read for coding; coding is from titles/metadata, S2 excerpts (CTX-E ids) or full text.
Writes v2cand3/ledger_rows.json and v2cand3/ctx_ids.json."""
import json, collections, re
R=json.load(open('raw/reception1_top50.json'))['results']
C=json.load(open('raw/recent1_top25.json'))['results']
A={q:json.load(open(f'raw/adj1_Q{q}.json'))['results'] for q in range(1,8)}
T='W2123817056'
def wid(w): return w['id'][21:]
def short(t,n=52):
    t=' '.join(t.split()); return t if len(t)<=n else t[:n].rstrip()+'…'
M='METADATA (OpenAlex record)'
EX='EXCERPT (Semantic Scholar citation context; s2/ responses cit_0…cit_5000, sha256 fa01fc13… et seq., not committed)'
CTX={}; _n=[0]
def cx(tag):
    if tag not in CTX: _n[0]+=1; CTX[tag]=f'CTX-E{_n[0]}'
    return CTX[tag]
def meta(rel,contrib,note): return (rel,'CITES-UNINSPECTED',contrib,M,'NOT-INSPECTED',f'title-coded from METADATA; {note}; citation present in OpenAlex refs, use not inspected')
def ins(tag,rel,relation,contrib,txt): return (rel,relation,contrib,EX,'INSPECTED',f'{cx(tag)}: {txt}')
def noins(rel,contrib,note): return (rel,'CITES-UNINSPECTED',contrib,EX,'NOT-INSPECTED',f'S2 context retrieved but {note}; use not inspected')
RRR='FULL-TEXT (Hagger et al. 2016, Maastricht University CRIS repository PDF, HTTP 200; not committed)'
codes={
'N01':meta('ADJACENT','REVIEW','integrative review of emotion regulation'),
'N02':meta('BACKGROUND','THEORY','conservation-of-resources theory, culture and the nested self'),
'N03':ins('N03','BACKGROUND','MENTIONS','REVIEW','self-control rests on a system "limited in capacity and subject to fatigue-like decline" (working-memory review)'),
'N04':meta('ADJACENT','REVIEW','emotion regulation consequences review'),
'N05':ins('N05','BACKGROUND','MENTIONS','REVIEW','willpower as a resource; "this cognitive capacity is diminished with use"'),
'N06':ins('N06','ADJACENT (L3)','SUPPORTS','REVIEW','founding-cluster review: food-temptation test run "to help rule out moods as a potential explanation"'),
'N07':meta('BACKGROUND','THEORY','hope theory target article'),
'N08':ins('N08','ADJACENT','PREMISE','THEORY','"Given the severe limitations of conscious selfregulation capacity" (Baumeister et al., 1998) as premise for automaticity'),
'N09':meta('ADJACENT (L3)','REVIEW','founding-cluster strength-model review (Baumeister, Vohs & Tice 2007); also ADJUDICATION-1 (Q7)'),
'N10':meta('BACKGROUND','THEORY','emotional regulation in the workplace; S2 found no context'),
'N11':meta('BACKGROUND','METHOD','Short Grit Scale validation'),
'N12':ins('N12','BACKGROUND','PREMISE','REVIEW','"self-regulation in and of itself is a drain on resources" (COR theory review)'),
'N13':ins('N13','ADJACENT','MENTIONS','REVIEW','restates Experiment 1: radish eaters "persisted for less time on a subsequent unsolvable puzzles task" (faithful to Stage 1 field 6)'),
'N14':ins('N14','BACKGROUND','MENTIONS','REVIEW','people find it hard to "forgo benefits in the present" (sustainability review)'),
'N15':meta('BACKGROUND','REVIEW','cues to deception meta-analysis'),
'N16':('DIRECT (L2)','SUPPORTS','REVIEW',EX,'INSPECTED',f'{cx("N16")}: Baumeister and coworkers "provided initial support for the ego-depletion effect"; meta-analysis built on the dual-task paradigm "outlined by Baumeister et al. (1998)"; K1; also ADJUDICATION-1 (Q2)'),
'N17':meta('BACKGROUND','REVIEW','intention-behaviour gap review'),
'N18':ins('N18','BACKGROUND','MENTIONS','METHOD','a demanding task "has been associated with diminished performance on subsequent tasks" (ABCD imaging protocol)'),
'N19':('ADJACENT (L2)','CITES-UNINSPECTED','INDEPENDENT-DATA',M,'NOT-INSPECTED','title-coded from METADATA; founding-cluster companion paper (Muraven, Tice & Baumeister 1998); cited by the target and citing it (reciprocal pair); S2 found no context'),
'N20':meta('BACKGROUND','REVIEW','emotion-regulation strategies meta-analysis'),
'N21':meta('ADJACENT','REVIEW','executive functions and self-regulation review'),
'N22':ins('N22','BACKGROUND','PREMISE','INDEPENDENT-DATA','suppressing emotion "may use up resources that might otherwise be used for coping"'),
'N23':noins('BACKGROUND','INDEPENDENT-DATA','the returned passage does not show the citation'),
'N24':meta('BACKGROUND','INDEPENDENT-DATA','recovery and work engagement'),
'N25':ins('N25','BACKGROUND','PREMISE','REVIEW','"Emotion regulation demands can drain resources from task performance"'),
'N26':ins('N26','ADJACENT','MENTIONS','REVIEW','"evidence confirms" capacity for self-control is susceptible to previous attempts (founding-author co-written meta-analysis)'),
'N27':ins('N27','ADJACENT (R2)','QUALIFIES','THEORY','new experiments found "true choice was not depleting" contra the target\'s high-choice condition'),
'N28':meta('ADJACENT','THEORY','founding-author consumer self-control essay'),
'N29':noins('BACKGROUND','COMMENTARY','the returned passage is a reference-list fragment'),
'N30':meta('BACKGROUND','REVIEW','economics and psychology of personality traits'),
'N31':ins('N31','ADJACENT','SUPPORTS','THEORY','Baumeister and colleagues "have established the importance of selfregulatory resource[s]"'),
'N32':meta('BACKGROUND','INDEPENDENT-DATA','mindfulness at work; S2 found no context'),
'N33':ins('N33','ADJACENT (L3)','SUPPORTS','REVIEW','founding-cluster review: regulating the self "appears to depend on a limited resource"; also ADJUDICATION-1 (Q4)'),
'N34':meta('BACKGROUND','INDEPENDENT-DATA','emotion regulation and memory; S2 found no context'),
'N35':meta('BACKGROUND','INDEPENDENT-DATA','resource loss among inner-city women'),
'N36':ins('N36','ADJACENT','MENTIONS','INDEPENDENT-DATA','founding-cluster study: the target "replicated a study on ego depletion using solvable rather than unsolvable anagrams"'),
'N37':meta('ADJACENT (R2)','THEORY','opportunity-cost model of subjective effort (Kurzban et al. 2013)'),
'N38':meta('ADJACENT','INDEPENDENT-DATA','founding-cluster study of emotional distress and impulse control'),
'N39':meta('BACKGROUND','REVIEW','personality psychology and economics handbook chapter'),
'N40':noins('BACKGROUND','REVIEW','the returned passages do not show the citation'),
'N41':ins('N41','DIRECT (L3)','SUPPORTS','INDEPENDENT-DATA','founding-cluster glucose study: the depleted resource "has been a puzzle since the earliest findings"'),
'N42':ins('N42','BACKGROUND','MENTIONS','REVIEW','listed for constrained cognitive capacity (passage truncated at the citation)'),
'N43':ins('N43','BACKGROUND','PREMISE','REVIEW','"These acts of volition draw upon ego resources"'),
'N44':ins('N44','ADJACENT','MENTIONS','REVIEW','"making choices is one form of self-regulation that can result in ego-depletion"'),
'N45':('DIRECT (L2)','CHALLENGES','INDEPENDENT-DATA',RRR,'INSPECTED','RRR-E1 p. 548: Study 1 "required participants to taste radishes and resist cookies"; RRR-E2 p. 554: pooled d = 0.04 across 23 labs; K4; also ADJUDICATION-1 (Q1)'),
'N46':meta('BACKGROUND','THEORY','justification-suppression model of prejudice'),
'N47':meta('ADJACENT (R2)','THEORY','process-model revision of the resource model (Inzlicht & Schmeichel 2012); K10; also ADJUDICATION-1 (Q4)'),
'N48':meta('ADJACENT (R2)','THEORY','rational account of mental effort'),
'N49':ins('N49','ADJACENT (L4)','MENTIONS','INDEPENDENT-DATA','depletion listed across "overeating, procrastination, intellectual un-derachievement"'),
'N50':meta('BACKGROUND','METHOD','measurement of personal qualities'),
'R01':ins('R01','BACKGROUND','MENTIONS','REVIEW','attributes "displaced behavior theory" to Baumeister; self-control "a limited resource that can be drained over time"'),
'R02':ins('R02','BACKGROUND','MENTIONS','INDEPENDENT-DATA','time spent choosing used "as a proxy of service engagement" (Baumeister et al., 1998)'),
'R03':meta('ADJACENT (L3)','INDEPENDENT-DATA','neuro-metabolic account of daylong cognitive work'),
'R04':meta('BACKGROUND','INDEPENDENT-DATA','resilience and stress effects'),
'R06':ins('R06','BACKGROUND','MENTIONS','REVIEW','"Some scholars have proposed a \'strength\' or \'limited resource\' model"'),
'R07':ins('R07','BACKGROUND','PREMISE','REVIEW','victims "exhaust their limited resources" and experience ego-depletion'),
'R08':ins('R08','BACKGROUND','PREMISE','INDEPENDENT-DATA','difficult tasks leave "insufficient personal resources … under the limited strength model"'),
'R09':meta('ADJACENT','REVIEW','systematic review of self-regulation and goal-directed behaviour'),
'R10':meta('ADJACENT (R2)','REVIEW','restoration of attention by rest'),
'R11':meta('BACKGROUND','INDEPENDENT-DATA','AI in the workplace'),
'R12':meta('ADJACENT (L3)','REVIEW','origins and consequences of cognitive fatigue'),
'R13':ins('R13','BACKGROUND','PREMISE','INDEPENDENT-DATA','"All acts of self-regulation are empowered by a limited, metaphorical strength"'),
'R14':meta('BACKGROUND','REVIEW','inclusive leadership review'),
'R15':meta('ADJACENT (R3)','THEORY','metacognition and self-control framework; S2 found no context'),
'R16':ins('R16','BACKGROUND','QUALIFIES','REVIEW','review chose "to exclude ego-depletion studies" unless strong evidence was given'),
'R17':ins('R17','BACKGROUND','PREMISE','REVIEW','"striving to achieve one goal can compromise the pursuit of subsequent goals"'),
'R18':ins('R18','BACKGROUND','PREMISE','INDEPENDENT-DATA','"theoretical foundation … built on a strength model of self-control known as ego depletion theory"'),
'R19':ins('R19','ADJACENT','MENTIONS','REVIEW','ego depletion listed as one name for mental fatigue'),
'R20':meta('BACKGROUND','THEORY','emotions in competitive sports'),
'R21':ins('R21','BACKGROUND','PREMISE','INDEPENDENT-DATA','effortful behaviour can "use a significant amount of their own regulatory resources"'),
'R22':meta('BACKGROUND','INDEPENDENT-DATA','supervisor incivility and turnover'),
'R23':meta('BACKGROUND','THEORY','interdisciplinary synthesis of motivation; S2 found no context'),
'R24':noins('BACKGROUND','INDEPENDENT-DATA','the returned passages carry bracket numbers that cannot be tied to the target'),
'R25':ins('R25','BACKGROUND','MENTIONS','REVIEW','resource gains and losses as mediators (Baumeister et al., 1998 in a list)'),
}
VO='FULL-TEXT (Vohs et al. 2021, eScholarship UC repository PDF, CC BY; not committed)'
DA='FULL-TEXT (VERSION-SUBSTITUTE: PMC8186735 author manuscript HTML, pmc.ncbi.nlm.nih.gov; SPPS version not retrieved; not committed)'
EN='FULL-TEXT (Frontiers in Human Neuroscience HTML, publisher OA; not committed)'
codes['R05']=('ADJACENT (L2)','CITES-UNINSPECTED','REVIEW',M,'NOT-INSPECTED','title-coded from METADATA; founding-author status review (Baumeister et al. 2024); full text not retrieved; also ADJUDICATION-1 (Q3)')
rows=[]
recids={wid(w):f'N{i:02d}' for i,w in enumerate(R,1)}
recentids={wid(w):f'R{i:02d}' for i,w in enumerate(C,1)}
ADJ_OVER={'N45','N16','N33','N47','N09'}
for i,w in enumerate(R,1):
    sid=f'N{i:02d}'; mem=['RECEPTION-1']+(['ADJUDICATION-1'] if sid in ADJ_OVER else [])
    rows.append((sid,f"{sid} {wid(w)} {short(w['display_name'])} ({w['publication_year']})",'+'.join(mem),*codes[sid]))
for i,w in enumerate(C,1):
    sid=f'R{i:02d}'; mem=['RECENT-1']+(['ADJUDICATION-1'] if sid=='R05' else [])
    rows.append((sid,f"{sid} {wid(w)} {short(w['display_name'])} ({w['publication_year']})",'+'.join(mem),*codes[sid]))
# ---------- ADJUDICATION-1 non-overlapping works: wid -> (rel, relation, contrib, access, context, supported)
def am(rel,relation,contrib,note):
    ctx='NOT-APPLICABLE' if relation=='NOT-CITING' else 'NOT-INSPECTED'
    return (rel,relation,contrib,M,ctx,f'title-coded from METADATA; {note}')
def aex(tag,rel,relation,contrib,txt): return (rel,relation,contrib,EX,'INSPECTED',f'{cx(tag)}: {txt}')
adj={
'W3014898655':(lambda: ('DIRECT (L2)','QUALIFIES','INDEPENDENT-DATA',DA,'INSPECTED','DA-E1 Introduction: the target "reported the ego depletion effect for the first time" and is "cited over 5,000 times"; DA-E2 Results, Table 3: error-rate d = 0.10, 95% CI [0.01, 0.19] (12 labs); K6')),
'W2580798662':(lambda: am('DIRECT (R1)','NOT-CITING','REANALYSIS','Q1; extends the RRR to a research program; OpenAlex refs (14) omit the target')),
'W2476382243':(lambda: am('DIRECT (L2)','NOT-CITING','COMMENTARY','Q1; editorial introduction to the RRR; OpenAlex refs (7) omit the target')),
'W3119325546':(lambda: ('DIRECT (L2)','CHALLENGES','INDEPENDENT-DATA',VO,'INSPECTED','VO-E1 p. 1568: "The seminal article" (the target) "has had \'transformational\' impact"; VO-E2 p. 1574: d = 0.06, 95% CI [−0.02, 0.14]; VO-E3 p. 1577: depletion "not as reliable or robust as previously assumed"; founding-cluster first author (Vohs); merged with preprint record W4256555852 (Q1); K5')),
'W2780490182':(lambda: am('DIRECT (L2)','UNKNOWN','INDEPENDENT-DATA','Q1; multilab Stroop replication; one work under two records (W2780490182 2017 registration, W7160480298 2024 report); no OpenAlex refs; result not read')),
'W3157428216':(lambda: ('DIRECT (L2)','MENTIONS','COMMENTARY',EN,'INSPECTED','EN-E1 (Method summary): the e-crossing task "(… Baumeister et al., 1998) served as the initial task" in the 2021 multisite test; opinion title states "no evidence for or against"')),
'W2896535558':(lambda: am('DIRECT (L2)','UNKNOWN','INDEPENDENT-DATA','Q1; replication dataset record; no OpenAlex refs')),
'W2604293295':(lambda: aex('A-Dang2017','DIRECT (L2)','MENTIONS','REVIEW','"over 300 independent studies have replicated this effect … since it was first reported"; K7')),
'W2007393966':(lambda: am('DIRECT (R1)','CITES-UNINSPECTED','REANALYSIS','Q2; publication-bias reanalysis of the strength model (Carter & McCullough 2014); K2')),
'W2984573913':(lambda: am('ADJACENT (L2)','NOT-CITING','REVIEW','Q2; meta-analysis of depletion and physical endurance; OpenAlex refs (104) omit the target')),
'W2794580436':(lambda: am('DIRECT (R1)','CITES-UNINSPECTED','REVIEW','Q2; "Is Ego Depletion Real?" analysis of arguments (Friese et al. 2019)')),
'W2612478318':(lambda: am('ADJACENT (L2)','UNKNOWN','REVIEW','Q2; sport-performance meta-analysis; no OpenAlex refs')),
'W2588069705':(lambda: aex('A-BR2017','DIRECT (R1)','QUALIFIES','REANALYSIS','"Such convergence does not show up for the so-called ego-depletion effect"')),
'W4411356972':(lambda: am('ADJACENT (L2)','CITES-UNINSPECTED','REVIEW','Q2; athletes meta-analysis (2025)')),
'W1989768409':(lambda: aex('A-Carter2013','DIRECT (R1)','MENTIONS','REANALYSIS','defines "the so-called depletion effect" (Baumeister et al. 1998) in a commentary on overestimation')),
'W1964342261':(lambda: am('DIRECT (L3)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q3; glucose drinks "fail to counteract" depletion (title)')),
'W2779009122':(lambda: am('DIRECT (L3)','UNKNOWN','REVIEW','Q3; encyclopedia-type entry on the glucose hypothesis; no OpenAlex refs')),
'W2152858830':(lambda: aex('A-Beedie','DIRECT (L3)','MENTIONS','REVIEW','"resisting the temptation to eat chocolate (Baumeister et al., 1998, Study 1)" listed among depletion tasks')),
'W2003102314':(lambda: am('DIRECT (L3)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q3; unsuccessful replications of self-control and glucose effects (title)')),
'W1546584494':(lambda: am('ADJACENT (L3)','CITES-UNINSPECTED','REVIEW','Q3; nature of self-regulatory fatigue review')),
'W2058765236':(lambda: am('ADJACENT (R4)','CITES-UNINSPECTED','COMMENTARY','Q3; identical-tasks critique (Lange 2014)')),
'W1966401421':(lambda: aex('A-Gailliot2007','ADJACENT (L3)','SUPPORTS','REVIEW','founding-author review: "resisting the temptation to eat cookies caused participants subsequently to give up faster"')),
'W2130284887':(lambda: am('ADJACENT (L3)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q3; glucose, guilt and prosocial behaviour')),
'W2533887486':(lambda: am('ADJACENT (R2)','NOT-CITING','INDEPENDENT-DATA','Q4; motivational tuning after depletion; OpenAlex refs (83) omit the target')),
'W2058867658':(lambda: am('BACKGROUND','NOT-CITING','THEORY','Q4; philosophy of motivation; OpenAlex refs (11) omit the target')),
'W2796459004':(lambda: am('DIRECT (R2)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q4; test of a process-model implication')),
'W2538010233':(lambda: aex('A-Haynes','DIRECT (R2)','MENTIONS','INDEPENDENT-DATA','"The e-crossing task was used to manipulate ego depletion (Baumeister et al., 1998 …)"')),
'W212211297':(lambda: am('ADJACENT (R2)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q4; restraint and alcohol motivation')),
'W2513456674':(lambda: am('ADJACENT (R2)','CITES-UNINSPECTED','REVIEW','Q4; moderators of the depletion effect')),
'W2893842868':(lambda: am('ADJACENT (R3)','CITES-UNINSPECTED','REVIEW','Q5; lay theories of willpower review')),
'W2522685630':(lambda: am('ADJACENT (R3)','CITES-UNINSPECTED','REVIEW','Q5; implicit theories about willpower chapter')),
'W2118108696':(lambda: aex('A-Job2010','DIRECT (R3)','MENTIONS','INDEPENDENT-DATA','task "adopted from previous research to manipulate ego depletion (Baumeister et al., 1998 …)"; K9')),
'W1792116546':(lambda: am('ADJACENT (R3)','NOT-CITING','INDEPENDENT-DATA','Q5; willpower theories and well-being; OpenAlex refs (55) omit the target')),
'W1976771764':(lambda: aex('A-Job2015','ADJACENT (R3)','PREMISE','INDEPENDENT-DATA','strength model "posits that selfcontrol relies on a limited energy resource"')),
'W2905871268':(lambda: am('ADJACENT (R3)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q5; willpower theories as moderator at work')),
'W2270668874':(lambda: am('ADJACENT (R3)','NOT-CITING','INDEPENDENT-DATA','Q5; willpower theories and rest goals; OpenAlex refs (50) omit the target')),
'W2739641472':(lambda: aex('A-Bernecker2017','DIRECT (R3)','MENTIONS','INDEPENDENT-DATA','"We adapted a study design involving resistance to tempting food as the depletion manipulation"')),
'W2900405707':(lambda: am('ADJACENT (R3)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q5; correlates of willpower theories')),
'W2922399599':(lambda: am('ADJACENT (R3)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q5; willpower theories and bedtime procrastination')),
'W2144295133':(lambda: am('DIRECT (R4)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q6; "Ego Depletion Is Not Just Fatigue" (Vohs et al. 2011; founding-cluster member)')),
'W2035672781':(lambda: am('ADJACENT (R4)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q6; fatigue, guilt and prosocial behaviour')),
'W2110882073':(lambda: am('ADJACENT (R4)','NOT-CITING','INDEPENDENT-DATA','Q6; nature exposure after depletion; OpenAlex refs (57) omit the target')),
'W1988113868':(lambda: aex('A-Moller','ADJACENT (R2)','QUALIFIES','INDEPENDENT-DATA','"According to the Baumeister et al. (1998) model … making choices would necessarily result in ego-depletion" (tests the autonomy moderator)')),
'W3159013860':(lambda: am('DIRECT (R4)','CITES-UNINSPECTED','THEORY','Q6; depletion reconceptualised as transient cognitive fatigue')),
'W1992322615':(lambda: aex('A-Ciarocco','ADJACENT','MENTIONS','INDEPENDENT-DATA','founding-author co-written study: the target "proposed the term \'ego depletion\'"')),
'W2986926076':(lambda: am('ADJACENT (R1)','CITES-UNINSPECTED','INDEPENDENT-DATA','Q6; "The Limits of Ego Depletion"')),
'W2150495553':(lambda: aex('A-Muraven2006','ADJACENT (L3)','SUPPORTS','INDEPENDENT-DATA','founding-author study: "Consistent with Baumeister et al. (1998), the incorrect/missing solutions did not occur at random"')),
'W2313439080':(lambda: am('BACKGROUND','CITES-UNINSPECTED','REVIEW','Q7; strength-model review (Chinese journal)')),
'W2301647011':(lambda: aex('A-Englert2016','ADJACENT (L4)','MENTIONS','REVIEW','effects "not caused by … mood differences (e.g., Baumeister et al., 1998 …)" (sport review)')),
'W3170796682':(lambda: am('BACKGROUND','UNKNOWN','REVIEW','Q7; strength-model chapter; no OpenAlex refs')),
'W1608074949':(lambda: aex('A-Englert2015','ADJACENT (L4)','PREMISE','THEORY','"Like a muscle, one\'s self-control strength can become exhausted and depleted"')),
'W2170958357':(lambda: aex('A-Englert2015b','ADJACENT (L4)','PREMISE','THEORY','"We identified the strength model of selfcontrol (Baumeister et al., 1998) as a promising candidate theory"')),
'W2182110160':(lambda: am('ADJACENT (L4)','NOT-CITING','INDEPENDENT-DATA','Q7; sleep deprivation and delinquency test of the strength model; OpenAlex refs (64) omit the target')),
}
MERGE={'W4256555852':'W3119325546','W7160480298':'W2780490182'}
allw={}; order=[]
for q in range(1,8):
    for w in A[q]:
        i=wid(w); allw.setdefault(i,w); i=MERGE.get(i,i)
        if i not in [o for o,_ in order]: order.append((i,q))
k=0; amap={}
for i,q in order:
    if i==T or i in recids or i in recentids: continue
    k+=1; sid=f'A{k:02d}'; amap[i]=sid; w=allw[i]
    extra=' + W4256555852 (preprint record)' if i=='W3119325546' else (' + W7160480298 (2024 record)' if i=='W2780490182' else '')
    r=adj[i]()
    sup=r[5]
    if r[3]==M and not sup.startswith('title-coded from METADATA; Q'): pass
    rows.append((sid,f"{sid} {i}{extra} {short(w['display_name'])} ({w['publication_year']})",'ADJUDICATION-1',*r))
# target row
rows.append(('T01','T01 W2123817056 Ego depletion: Is the active self a limited resource? (1998) — target','OUTSIDE','DIRECT (L1)','NOT-CITING','INDEPENDENT-DATA','ABSTRACT (PubMed 9599441; publisher full text HTTP 403, not retrieved)','NOT-APPLICABLE','target source; not returned by ADJUDICATION-1; TA-E1 (abstract): results "suggest that the self\'s capacity for active volition is limited"; body text not read'))
# Section E locked sources (OUTSIDE)
secnote={'W2084221958':('ADJACENT (R4)','INDEPENDENT-DATA','mental fatigue and judgement'),
'W2319902335':('ADJACENT (R4)','INDEPENDENT-DATA','blocking as a principle of mental fatigue (1931)'),
'W4253912427':('BACKGROUND','INDEPENDENT-DATA','fatigue in chronic-fatigue patients; off-topic hit retained'),
'W2029487046':('ADJACENT (R3)','THEORY','learned helplessness reformulation'),
'W2022987442':('ADJACENT (R3)','INDEPENDENT-DATA','learned helplessness, depression and persistence'),
'W2139986071':('ADJACENT (R3)','INDEPENDENT-DATA','learned helplessness in humans'),
'W2119926219':('UNRELATED','NONE','off-topic hit (breastfeeding) retained, not replaced'),
'W1537717563':('ADJACENT (R4)','INDEPENDENT-DATA','mood and persistence'),
'W2012786194':('ADJACENT (R4)','INDEPENDENT-DATA','mood, goal structures and persistence in children'),
'W1981707533':('ADJACENT (R4)','REVIEW','teacher expectancy effects'),
'W2068172336':('ADJACENT (R4)','METHOD','experimenter expectancy'),
'W2059803871':('ADJACENT (R4)','METHOD','balanced-placebo design (expectancy control)'),
'W2074791822':('BACKGROUND','INDEPENDENT-DATA','invested mental effort, TV vs print'),
'W2098813016':('BACKGROUND','METHOD','mental-effort efficiency measure'),
'W2129275476':('UNRELATED','NONE','vegetative response to imagined movement; off-topic hit')}
n=0
for f in range(1,6):
    for w in json.load(open(f'raw/secE_F{f}.json'))['results'][:3]:
        n+=1; i=wid(w); rel,con,note=secnote[i]
        rows.append((f'X{n:02d}',f"X{n:02d} {i} {short(w['display_name'],60)} ({w['publication_year']})",'OUTSIDE',rel,'NOT-CITING',con,M,'NOT-APPLICABLE',f'title-coded from METADATA; Section E locked source F{f}; predates target; {note}; not in the target\'s OpenAlex reference list'))
CA='FULL-TEXT (author copy, pages.ucsd.edu faculty page PDF; not committed)'
rows+= [
('X16','X16 Carter, Kofler, Forster & McCullough 2015, A Series of Meta-Analytic Tests of the Depletion Effect (JEP:General)','OUTSIDE','DIRECT (R1)','CHALLENGES','REANALYSIS',CA,'INSPECTED','CA-E1 p. 1: "(the depletion effect; Baumeister et al., 1998)"; CA-E2 p. 16: PET and PEESE estimates "indistinguishable from zero"; K3; POST HOC (not returned by ADJUDICATION-1)'),
('X17','X17 Baumeister & Vohs 2016, comment on the RRR (APS-hosted manuscript)','OUTSIDE','DIRECT (L2)','NOT-CITING','COMMENTARY','FULL-TEXT (psychologicalscience.org PDF; not committed)','NOT-APPLICABLE','text read: no citation of the 1998 article found; BV-E1 p. 2: the RRR "did not test ego depletion" (manipulation failure); founding authors; K11; POST HOC'),
('X18','X18 Schimmack 2016, replicability analysis of ego depletion (Replicability-Index blog)','OUTSIDE','DIRECT (R1)','CHALLENGES','REANALYSIS','FULL-TEXT (replicationindex.com HTML; not committed)','INSPECTED','SC-E1 (Study 1 analysis section; Stage 1 source S2): computes Experiment 1 effect sizes from reported statistics (d = 1.80 / 2.04); POST HOC'),
('X19','X19 Baumeister 2012, LSE public lecture slides "Willpower"','OUTSIDE','ADJACENT (L4)','SUPPORTS','COMMENTARY','FULL-TEXT (lse.ac.uk PDF; not committed)','INSPECTED','LS-E1 (slide headings; Stage 1 D1/D1b): slides "Willpower is limited", "Like a Muscle"; founding author; POST HOC'),
('X20','X20 APA public page "Is Willpower a Limited Resource?"','OUTSIDE','ADJACENT (L4)','SUPPORTS','COMMENTARY','FULL-TEXT (apa.org PDF; not committed)','INSPECTED','AP-E1 (Stage 1 D2/D2b): describes the study as having "drained the subjects\' self-control"; POST HOC'),
]
PH={'N41':'; POST HOC adjudication member (known item K8, not returned by the ADJUDICATION-1 search)'}
rows=[tuple(r[:8])+(r[8]+PH.get(r[0],''),) for r in rows]
json.dump(rows,open('v2cand3/ledger_rows.json','w'),indent=0,ensure_ascii=False)
json.dump({'ctx':CTX,'amap':amap},open('v2cand3/ctx_ids.json','w'),indent=1)
print(len(rows), 'A rows',k)
mem=collections.Counter(m for r in rows for m in r[2].split('+')); print(mem)
for cid in ('RECEPTION-1','RECENT-1','ADJUDICATION-1'):
    ms=[r for r in rows if cid in r[2].split('+')]
    print(cid,len(ms),'inspected',sum(r[7]=='INSPECTED' for r in ms), collections.Counter(r[4] for r in ms))
# rule checks
for r in rows:
    if r[4] in ('SUPPORTS','CHALLENGES','QUALIFIES','PREMISE','MENTIONS'): assert r[7]=='INSPECTED' and r[6].split()[0] in ('FULL-TEXT','EXCERPT'),r[0]
    if r[4]=='NOT-CITING': assert r[7]=='NOT-APPLICABLE',r[0]
    if r[7]=='INSPECTED': assert r[4] not in ('CITES-UNINSPECTED','UNKNOWN'),r[0]
print('ctx ids',len(CTX))
