OUTPATH='/workspace/pa-v2cand/examples/research/acemoglu-colonial-origins/citation-network-v2cand/RUN_REPORT.txt'
gl=open('/workspace/pa-v2cand/examples/research/acemoglu-colonial-origins/citation-network-v2cand/checker/final_gates.txt').read().splitlines()
vl=open('/workspace/pa-v2cand/examples/research/acemoglu-colonial-origins/citation-network-v2cand/checker/final_v1.txt').read().splitlines()
GL_COV=[l.replace('\t',' ') for l in gl if l.split('\t')[0].startswith(('COVERAGE','PROVISIONAL'))]
CHK=[('v1 checker check-citation-network-output.py','"'+vl[-1]+'"',0),('v2 gate checker check-citation-network-v2-gates.py','"'+gl[-1]+'"',0)]
REV=['[v1 checker] '+l for l in vl if l.startswith('REVIEW_ITEM')]+['[gate checker] '+l for l in gl if l.startswith('REVIEW_ITEM')]
