"""Build the atlas-adapter/0.1 context for the AJR 2001 citation-network run.
Paths are relative to the repository root. Usage: build_atlas_context.py <repo_root> <imported_at>"""
import json, hashlib, sys
from pathlib import Path
root = Path(sys.argv[1]); imported_at = sys.argv[2]
D = "examples/research/acemoglu-colonial-origins/citation-network"
CN = Path("/workspace/acemoglu-cn")
sha = lambda p: hashlib.sha256((root / p).read_bytes()).hexdigest()
man = json.load(open(root / D / "sources/excerpts_manifest.json"))
log = [json.loads(l) for l in open(CN / "raw/retrieval_log.jsonl")]
at = {e["file"]: e["at"] for e in log if e.get("status") == 200}
INSTRUMENT_BLOB = "7ac79f0da337c4d52e39e1490088d06c82a9d42b"

W = {  # key: (work_id, title, identity_basis, version, version_basis, confidence, uri, origin)
 "AJR2001": ("doi:10.1257/aer.91.5.1369", "The Colonial Origins of Comparative Development: An Empirical Investigation",
   "DOI printed on the article; OpenAlex W2011474190 (baseline identity check, Section A).",
   "PUBLISHER_PDF_AUTHOR_HOSTED (JSTOR-stamped)", "Typeset AER article with JSTOR cover page, hosted on economics.mit.edu; journal page = PDF page + 1367. accessed_at is approximate: SOURCES_MANIFEST.json records retrieval approx. 02:30-03:10 PST in the earlier stage; the earliest bound is used.",
   "BYTES_PINNED_PUBLISHER_PDF_AUTHOR_HOSTED",
   "https://economics.mit.edu/sites/default/files/publications/colonial-origins-of-comparative-development.pdf", "2026-11-04T10:30:00Z"),
 "HB2004": ("doi:10.1016/s1574-0684(05)01006-3", "Institutions as a Fundamental Cause of Long-Run Growth",
   "OpenAlex N11 (handbook chapter) and N05 (NBER w10481) records; working paper is the chapter's prior version.",
   "NBER_WORKING_PAPER w10481", "NBER working paper version, not the published Handbook of Economic Growth chapter (published chapter NOT_RETRIEVED).",
   "BYTES_PINNED_WORKING_PAPER", "https://www.nber.org/system/files/working_papers/w10481/w10481.pdf", None),
 "NOBELSCI": ("url:https://www.nobelprize.org/uploads/2024/10/advanced-economicsciencesprize2024.pdf",
   "Scientific Background to the Sveriges Riksbank Prize in Economic Sciences 2024", "Publisher URL (nobelprize.org).",
   "PUBLISHER_PDF", "Official PDF retrieved from nobelprize.org.", "BYTES_PINNED_PUBLISHER_PDF",
   "https://www.nobelprize.org/uploads/2024/10/advanced-economicsciencesprize2024.pdf", None),
 "NOBELPOP": ("url:https://www.nobelprize.org/uploads/2024/10/popular-economicsciencesprize2024.pdf",
   "Popular Science Background: Explaining Prosperity Differences between Nations (Nobel 2024)", "Publisher URL (nobelprize.org).",
   "PUBLISHER_PDF", "Official PDF retrieved from nobelprize.org.", "BYTES_PINNED_PUBLISHER_PDF",
   "https://www.nobelprize.org/uploads/2024/10/popular-economicsciencesprize2024.pdf", None),
 "RODRIK2004": ("doi:10.1023/b:joeg.0000031425.72248.85", "Institutions Rule: The Primacy of Institutions over Geography and Integration in Economic Development",
   "OpenAlex N02 record DOI.", "NBER_WORKING_PAPER w9305", "NBER working paper version, not the Journal of Economic Growth article.",
   "BYTES_PINNED_WORKING_PAPER", "https://www.nber.org/system/files/working_papers/w9305/w9305.pdf", None),
 "GLAESER2004": ("doi:10.1023/b:joeg.0000038933.16398.ed", "Do Institutions Cause Growth?",
   "OpenAlex N03 record DOI.", "NBER_WORKING_PAPER w10568", "NBER working paper version, not the Journal of Economic Growth article.",
   "BYTES_PINNED_WORKING_PAPER", "https://www.nber.org/system/files/working_papers/w10568/w10568.pdf", None),
 "SACHS2003": ("doi:10.3386/w9490", "Institutions Don't Rule: Direct Effects of Geography on Per Capita Income",
   "NBER working paper number w9490 (Section E post hoc directly-adjudicating row).", "NBER_WORKING_PAPER w9490",
   "NBER working paper; this is the cited work itself.", "BYTES_PINNED_WORKING_PAPER",
   "https://www.nber.org/system/files/working_papers/w9490/w9490.pdf", None),
 "EL2003": ("doi:10.1016/s0304-3932(02)00200-3", "Tropics, Germs, and Crops: How Endowments Influence Economic Development",
   "OpenAlex N21 record DOI.", "NBER_WORKING_PAPER w9106", "NBER working paper version, not the Journal of Monetary Economics article.",
   "BYTES_PINNED_WORKING_PAPER", "https://www.nber.org/system/files/working_papers/w9106/w9106.pdf", None),
 "DML2018": ("doi:10.1111/ectj.12097", "Double/Debiased Machine Learning for Treatment and Structural Parameters",
   "OpenAlex N06 record DOI.", "ARXIV_PREPRINT 1608.00060", "arXiv preprint (latest version served at retrieval), not the Econometrics Journal article.",
   "BYTES_PINNED_PREPRINT", "https://arxiv.org/pdf/1608.00060", None),
 "HW2008": ("doi:10.1257/jel.46.3.607", "The Role of Cognitive Skills in Economic Development",
   "OpenAlex N12 record DOI.", "NBER_WORKING_PAPER w12832", "NBER working paper version, not the Journal of Economic Literature article.",
   "BYTES_PINNED_WORKING_PAPER", "https://www.nber.org/system/files/working_papers/w12832/w12832.pdf", None),
}
works, sources, passages = [], [], []
for key, (wid, title, basis, ver, vbasis, conf, uri, acc) in W.items():
    m = man[key]
    works.append({"id": wid, "title": title, "kind": "research", "identity_basis": basis})
    svid = f"{wid}/version/pdf-sha256-{m['pdf_sha256'][:16]}"
    comps = [{"id": e["id"], "kind": e["kind"], "start": e["start"], "end": e["end"]} for e in m["excerpts"]]
    sources.append({"id": svid, "work_id": wid, "version": f"{ver}; PDF SHA-256 {m['pdf_sha256']}",
        "version_basis": vbasis, "version_confidence": conf, "source_uri": uri,
        "accessed_at": acc or at[m["pdf"]], "access_outcome": "AVAILABLE",
        "rights": "BOUNDED_EXCERPTS_ONLY; NOT_REVIEWED_FOR_PUBLIC_RELEASE",
        "extraction": {"engine": "plain-utf8", "version": "1", "configuration": {}},
        "text_artifact": {"path": f"{D}/sources/{m['file']}", "sha256": sha(f"{D}/sources/{m['file']}")},
        "components": comps, "requested_components": [c["id"] for c in comps],
        "warnings": [f"Text artifact holds bounded excerpts copied from pdftotext output of the retrieved PDF (SHA-256 {m['pdf_sha256']}). The adapter verifies the excerpt bytes only, not PDF rendering or extraction fidelity. PDF not committed (rights)."],
        "failed_components": [], "origin_id": uri})
    for e in m["excerpts"]:
        passages.append({"id": e["id"], "source_version_id": svid, "component_id": e["id"], "start": e["start"],
            "end": e["end"], "quote": e["quote"], "normalized_sha256": e["normalized_sha256"],
            "pdf_page": e["pdf_page"], "label": f"{m['cite']} PDF p. {e['pdf_page']}"})
# Retrieval failures for downstream sources named in Artifact 4.
for wid, title, uri, status, when in [
    ("doi:10.1111/j.1468-0297.2006.01045.x", "Institutions and the Resource Curse (Mehlum, Moene, Torvik 2006)",
     "https://www.sv.uio.no/econ/personer/vit/kmoene/InstitutionsResourceCurse.pdf", "HTTP 404", "T10_mehlum_moene_torvik_oslo.pdf"),
    ("doi:10.1257/jel.49.2.366", "Natural Resources: Curse or Blessing? (van der Ploeg 2011)",
     "https://ora.ox.ac.uk/objects/uuid:9ee86a44-e6c5-4337-9aac-b3c66bbbfd1a/files/m30d52f1b3c27c7b0c75ebaa4b6e2df8d", "HTTP 500 x3 (gave up)", "T15_vanderploeg_oxcarre.pdf")]:
    works.append({"id": wid, "title": title, "kind": "research", "identity_basis": "OpenAlex top-50 citer record DOI."})
    t = max(e["at"] for e in log if e["file"] == when)
    sources.append({"id": f"{wid}/version/not-retrieved", "work_id": wid, "version": "UNKNOWN",
        "version_basis": "No copy retrieved; edition unknown.", "version_confidence": "UNKNOWN", "source_uri": uri,
        "accessed_at": t, "access_outcome": "RETRIEVAL_FAILED", "rights": "NOT_REVIEWED_FOR_PUBLIC_RELEASE",
        "extraction": {"engine": "plain-utf8", "version": "1", "configuration": {}}, "text_artifact": None,
        "components": [], "requested_components": ["citing_passages"],
        "warnings": [f"{status} on {t}; no workaround attempted."], "failed_components": [], "origin_id": "UNKNOWN"})
sv = {p["id"]: p["source_version_id"] for p in passages}
def chk(cid, kind, scope, basis, pids):
    reqs = {}
    for p in pids: reqs.setdefault(sv[p], []).append(p)
    return {"id": cid, "kind": kind, "scope": scope, "mapping_basis": basis,
            "requirements": [{"source_version_id": s, "component_ids": ps, "passage_ids": ps} for s, ps in reqs.items()]}
F = lambda n, ev: f"Finding {n} Evidence: '{ev}'"
checks = [
 chk("RD-shared-instruments", "content", "Rodrik et al. on reuse of AJR's instruments", F(2, "RD-E1, EL-E2, DML-E1, DML-E2"), ["RD-E1"]),
 chk("EL-settler-mortality-variable", "content", "Easterly-Levine's settler-mortality variable definition", F(2, "RD-E1, EL-E2, DML-E1, DML-E2"), ["EL-E2"]),
 chk("DML-reuses-AJR-data", "content", "DML reuses AJR's 64-country data and compares estimates", F(2, "RD-E1, EL-E2, DML-E1, DML-E2"), ["DML-E1", "DML-E2"]),
 chk("AJR-upper-bound", "content", "AJR 2001 own magnitude interpretation", F(3, "AJR-E2 ... and HB-E1"), ["AJR-E2"]),
 chk("HB-restatement", "content", "Handbook restatement of AJR 2001", F(3, "AJR-E2 ... and HB-E1"), ["HB-E1"]),
 chk("NP-causal-chain-wording", "content", "Nobel popular background wording", F(4, "NP-E1; NS-E1; NS-E2; NS-E3"), ["NP-E1"]),
 chk("NS-qualifiers", "content", "Nobel scientific background qualifiers", F(4, "NP-E1; NS-E1; NS-E2; NS-E3"), ["NS-E1", "NS-E2", "NS-E3"]),
 chk("NS-data-critique", "content", "Nobel scientific background on settler-mortality data reliability", F(5, "... NS-E2"), ["NS-E2"]),
 chk("AJR-malaria-control", "content", "AJR 2001 malaria control result", F(6, "AJR-E4; SA-E1; GL-E1; GL-E2; NS-E3"), ["AJR-E4"]),
 chk("SA-null-hypothesis", "content", "Sachs 2003 framing of the null", F(6, "AJR-E4; SA-E1; GL-E1; GL-E2; NS-E3"), ["SA-E1"]),
 chk("GL-rival-channel", "content", "Glaeser et al. 2004 malaria / human-capital rival tests", F(6, "AJR-E4; SA-E1; GL-E1; GL-E2; NS-E3"), ["GL-E1", "GL-E2"]),
 chk("NS-hard-to-disentangle", "content", "Nobel scientific background on disentangling channels", F(6, "AJR-E4; SA-E1; GL-E1; GL-E2; NS-E3"), ["NS-E3"]),
]
finding_checks = {
 "1": [],  # database/graph evidence only; no text passages to anchor
 "2": ["RD-shared-instruments", "EL-settler-mortality-variable", "DML-reuses-AJR-data"],
 "3": ["AJR-upper-bound", "HB-restatement"],
 "4": ["NP-causal-chain-wording", "NS-qualifiers"],
 "5": ["NS-data-critique"],
 "6": ["AJR-malaria-control", "SA-null-hypothesis", "GL-rival-channel", "NS-hard-to-disentangle"],
 "7": [],  # graph-structure evidence only
}
events = [{"source": e["file"], "requested_url": e["url"], "final_url": e.get("final_url", e["url"]),
           "retrieved_at": e["at"], "http_status": e["status"],
           "outcome": "AVAILABLE" if e["status"] == 200 else ("RETRIEVAL_FAILED" if e.get("outcome") == "GAVE_UP" else "HTTP_ERROR_RETRIED_OR_ABANDONED")}
          for e in log]
output_path = f"{D}/02c_citation_network.md"
declared = [f"{D}/sources/{man[k]['file']}" for k in W] + [f"{D}/sources/excerpts_manifest.json",
    f"{D}/lock/section_E_preregistration.md", f"{D}/lock/locked_sources.json", f"{D}/lock/section_E_lock_time.txt",
    f"{D}/retrieval/retrieval_log.jsonl"]
ctx = {"schema_version": "atlas-adapter/0.1",
 "run": {"id": "urn:atlas:import:ajr2001-citation-network:1", "target_work_id": "doi:10.1257/aer.91.5.1369",
   "imported_at": imported_at, "origin": "LIVE_EXECUTION_THIS_RUN",
   "model": {"identity": "Grok Bot (executor subagent)", "verification": "SELF_REPORTED_NOT_INDEPENDENTLY_VERIFIED"},
   "runner": {"identity": "Grok Bot audit run on branch audit/acemoglu-colonial-origins (main ce028e1)", "verification": "SELF_REPORTED_NOT_INDEPENDENTLY_VERIFIED"},
   "historical_instrument": {"identity": INSTRUMENT_BLOB, "verification": "VERIFIED"},
   "exposure": {"prior_outputs_seen": "YES: the same session produced 01_claim_extraction, 02a, 02b, 03_counter_audit and 05_final_assessment before this stage",
     "independence": "NOT_INDEPENDENT_OF_PRIOR_AUDIT_STAGES",
     "basis": "Runner authored the earlier stages; instrument identity checked by git blob hash of prompts/research-analysis/2-citation-network.txt at commit ce028e1 against atlas/baseline.json before execution."}},
 "output": {"path": output_path, "sha256": sha(output_path)},
 "works": works, "sources": sources, "passages": passages, "checks": checks, "finding_checks": finding_checks,
 "null_check_ids": [],
 "corpus": {"id": "ajr2001-citation-network-openalex-50", "boundary":
   "OpenAlex top-50 citers of AJR 2001 (union of W2011474190 and conflated W3124131699 records) with their OpenAlex reference lists; 10 locked adjacent-field sources (Section E LOCKED QUERY); recent citers since 2021-11-04 (2,695) for co-citation counts; bounded excerpts from 10 retrieved full texts.",
   "selection": "Top-50 by OpenAlex cited_by_count; adjacent-field lock by preregistered query; excerpts chosen after drafting findings to test their Evidence fields, so excerpt selection is not blind.",
   "retrieval_events": events,
   "limitations": ["Instrument validated only on supplied packets (<=26 sources, <=70 edges); this open-retrieval run is outside its validation boundary.",
     "Semantic Scholar citation contexts: HTTP 429 repeatedly; citing-passage coverage 13/50 top citers and 0/25 sampled recent citers.",
     "Mehlum et al. 2006 (404) and van der Ploeg 2011 (500 x3) not retrieved.",
     "OpenAlex conflates AJR 2001 with the 2012 Reply and truncates AJR's own reference list (13 indexed).",
     "Most full texts are working-paper or preprint versions, not the published versions."]},
 "declared_inputs": [{"path": p, "sha256": sha(p)} for p in declared],
 "reviews": []}
json.dump(ctx, sys.stdout, indent=1, ensure_ascii=False); print()
