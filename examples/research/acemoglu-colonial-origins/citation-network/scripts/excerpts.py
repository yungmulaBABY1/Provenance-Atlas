"""Build bounded excerpt files: each excerpt is an exact substring of the pdftotext -enc UTF-8 output."""
import json, hashlib, os, unicodedata, re
RAW='/workspace/acemoglu-cn/raw'; SRC='/workspace/acemoglu-src'
OUT='/workspace/acemoglu-cn/excerpts'
def sha(b): return hashlib.sha256(b).hexdigest()
def norm(t): return re.sub(r'\s+',' ',unicodedata.normalize('NFC',t)).strip()
S={
 'AJR2001':dict(pdf=f'{SRC}/colonial-origins-of-comparative-development.pdf',txt=f'{SRC}/colonial-origins-of-comparative-development.txt',
   cite='Acemoglu, Johnson & Robinson (2001). The Colonial Origins of Comparative Development: An Empirical Investigation. AER 91(5):1369-1401. DOI 10.1257/aer.91.5.1369.',
   ex=[('AJR-E1','section','institutions to the level of Chile could, in the','times as rich as Nigeria).'),
       ('AJR-E2','section','Our 2SLS estimate, 0.94, implies that the 2.24','effect of institutionaldifferences on income per capita.'),
       ('AJR-E4','section','In any case, controllingfor malariadoes not','with a standard error of 0.25'),
       ('AJR-E3','section','McArthurand Sachs (2001) also reportspecifications','thereforedid not pursue these estimates further.')]),
 'HB2004':dict(pdf=f'{RAW}/ajr_handbook_nber_w10481.pdf',txt=f'{RAW}/ajr_handbook_nber_w10481.txt',
   cite='Acemoglu, Johnson & Robinson (2004). Institutions as the Fundamental Cause of Long-Run Growth. NBER Working Paper 10481 (later Handbook of Economic Growth vol. 1A ch. 6, 2005).',
   ex=[('HB-E1','section','In Acemoglu, Johnson and Robinson (2001) we showed, using European mortality','explanatory power for current prosperity.')]),
 'NOBELSCI':dict(pdf=f'{RAW}/nobel2024_scientific_background.pdf',txt=f'{RAW}/nobel2024_scientific_background.txt',
   cite='Committee for the Prize in Economic Sciences in Memory of Alfred Nobel (2024). Scientific Background: Acemoglu, Johnson and Robinson.',
   ex=[('NS-E1','section','The actual IV-estimate should thus be taken with a grain of salt.','that were prosperous prior to colonization.'),
       ('NS-E2','section','Another point of discussion involves the reliability of the data on settler mortality','does not come from extremely high estimates of the settler mortality rates.'),
       ('NS-E3','section','Ultimately, however, human\ncapital and institutions are both determinants of growth','independent effect on growth.')]),
 'NOBELPOP':dict(pdf=f'{RAW}/nobel2024_popular.pdf',txt=f'{RAW}/nobel2024_popular.txt',
   cite='Royal Swedish Academy of Sciences (2024). Popular science background: They provided an explanation for why some countries are rich and others poor.',
   ex=[('NP-E1','section','Acemoglu, Johnson and Robinson have uncovered a clear chain of causality.','economic freedoms and the rule of law are good for it.')]),
 'RODRIK2004':dict(pdf=f'{RAW}/rodrik2004_nber_w9305.pdf',txt=f'{RAW}/rodrik2004_nber_w9305.txt',
   cite='Rodrik, Subramanian & Trebbi (2002/2004). Institutions Rule: The Primacy of Institutions over Geography and Integration in Economic Development. NBER WP 9305 (J. Econ. Growth 9:131-165, 2004).',
   ex=[('RD-E1','section','The idea is that these two instruments, having','at the moment of unraveling the tangle of cause-and-effect relationships involved.'),
       ('RD-E3','section','In our view,\nthis distinction is not made adequately clear in AJR','Levine (2002).'),
       ('RD-E4','section','One problem is that AJR do not carry out a direct test','of the impact of colonial policies and institutions.')]),
 'GLAESER2004':dict(pdf=f'{RAW}/glaeser2004_nber_w10568.pdf',txt=f'{RAW}/glaeser2004_nber_w10568.txt',
   cite='Glaeser, La Porta, Lopez-de-Silanes & Shleifer (2004). Do Institutions Cause Growth? NBER WP 10568 (J. Econ. Growth 9:271-303, 2004).',
   ex=[('GL-E1','section','The impact of settler mortality on today','colonial but not modern mortality risk.'),
       ('GL-E2','section','Could the influence of AJR','they brought with them their know-how rather than constraints on the executive.')]),
 'SACHS2003':dict(pdf=f'{RAW}/sachs2003_nber_w9490.pdf',txt=f'{RAW}/sachs2003_nber_w9490.txt',
   cite='Sachs (2003). Institutions Don\'t Rule: Direct Effects of Geography on Per Capita Income. NBER WP 9490.',
   ex=[('SA-E1','section','The chief strength of the AJR, EL, and RST papers','variable: malaria risk.')]),
 'EL2003':dict(pdf=f'{RAW}/easterly_levine_nber_w9106.pdf',txt=f'{RAW}/easterly_levine_nber_w9106.txt',
   cite='Easterly & Levine (2002/2003). Tropics, Germs, and Crops: How Endowments Influence Economic Development. NBER WP 9106 (J. Monetary Econ. 50:3-39, 2003).',
   ex=[('EL-E1','section','We find no evidence that tropics, germs, and crops affect country incomes directly','once we control for institutions.'),
       ('EL-E2','section','SETTLER MORTALITY equals the logarithm of annualized deaths per thousand of','AJR (2001) compiles data.')]),
 'DML2018':dict(pdf=f'{RAW}/T06_chernozhukov_dml_arxiv1608.00060.pdf',txt=f'{RAW}/T06_chernozhukov_dml_arxiv1608.00060.txt',
   cite='Chernozhukov et al. (2016/2018). Double/Debiased Machine Learning for Treatment and Structural Parameters. arXiv 1608.00060 (Econometrics Journal 21(1), 2018).',
   ex=[('DML-E1','section','We use the same set of 64 country-level observations as AJR.','early European settlers.'),
       ('DML-E2','section','Finally, although the estimates are\nsomewhat smaller than the baseline estimates reported in AJR','of institutions on output.')]),
 'HW2008':dict(pdf=f'{RAW}/T12_hanushek_woessmann_nber_w12832.pdf',txt=f'{RAW}/T12_hanushek_woessmann_nber_w12832.txt',
   cite='Hanushek & Woessmann (2007/2008). The Role of Cognitive Skills in Economic Development. NBER WP 12832 (J. Econ. Lit. 46(3), 2008).',
   ex=[('HW-E1','section','While Acemoglu, Johnson, and Robinson (2001, 2002, 2005) find that geographical features do not exert an effect','(cf., e.g., McArthur and Sachs (2001)).')]),
}
manifest={}
for key,s in S.items():
    pdfb=open(s['pdf'],'rb').read(); t=open(s['txt'],encoding='utf-8').read()
    blocks=[]; header=(f"Bounded excerpts from {key}: {s['cite']}\nPDF SHA-256 {sha(pdfb)}; extraction `pdftotext -enc UTF-8` (poppler) of that PDF, text SHA-256 {sha(t.encode())}.\n"
        "Not the full document. Each excerpt body is an exact substring of the extraction output; offsets in that output and in this file are recorded in excerpts_manifest.json.\n\n")
    body=header; recs=[]
    for eid,kind,a,b in s['ex']:
        i=t.find(a); assert i>=0,(key,eid,'start'); j=t.find(b,i); assert j>=0,(key,eid,'end'); j+=len(b)
        q=t[i:j]; page=t[:i].count('\f')+1
        q=q.replace('\f','')  # page breaks inside an excerpt
        assert '\f' not in q
        pre=f"=== {eid} | {kind} | PDF page {page} ===\n"; body+=pre; st=len(body); body+=q; en=len(body); body+="\n=== end "+eid+" ===\n\n"
        recs.append(dict(id=eid,kind=kind,start=st,end=en,pdf_page=page,extraction_start=i,extraction_end=j,quote=q,normalized_sha256=sha(norm(q).encode()),formfeed_removed=(t[i:j]!=q)))
    fn=f'{key}-excerpts.txt'; open(os.path.join(OUT,fn),'w',encoding='utf-8').write(body)
    bb=body.encode('utf-8')
    for r in recs: assert body[r['start']:r['end']]==r['quote']
    manifest[key]=dict(file=fn,sha256=sha(bb),pdf=os.path.basename(s['pdf']),pdf_sha256=sha(pdfb),text_sha256=sha(t.encode()),cite=s['cite'],excerpts=recs)
json.dump(manifest,open(os.path.join(OUT,'excerpts_manifest.json'),'w'),indent=1,ensure_ascii=False)
for k,m in manifest.items(): print(k,[(r['id'],r['pdf_page'],len(r['quote']),r['formfeed_removed']) for r in m['excerpts']])
