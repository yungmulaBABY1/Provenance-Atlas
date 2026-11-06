"""Reconstruct the Batch 1 (Oster 2005) locked-query specs and set.json.

Run from the repository root:  python tests/atlas/retrieval/oster-batch1/reconstruct_specs.py
Request parameters come from the executor's log. The declared terms below were
copied by hand from the locks and the run output. Rerunning reproduces the
committed files byte for byte.
"""

from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[4]
sys.path.insert(0, str(ROOT))

from atlas.retrieval.reconstruct import file_sha256, spec_from_log, write_json  # noqa: E402

HERE = Path(__file__).resolve().parent
RUN = "examples/research/oster-hepatitis-b"
CN = f"{RUN}/citation-network-v2cand3"
LOG = f"{RUN}/logs/retrieval_log.jsonl"
ADJ = f"{CN}/lock/ADJUDICATION-1_search_record.md"
SECE = f"{CN}/lock/section_E_preregistration.md"
OUT2C = f"{CN}/02c_citation_network_v2cand3.md"
SAMPLES = f"{CN}/lock/SAMPLES_draw.txt"
SET_ID = "oster-2005-batch1"
Q = {1: '"hepatitis B" AND ("sex ratio" OR "offspring sex" OR "sex of offspring" OR "sex of the offspring")',
     2: '"missing women" AND ("hepatitis" OR "sex ratio at birth")',
     3: '("sex ratio at birth" OR "son preference") AND ("birth order" OR parity) AND (China OR India)',
     4: '("sex ratio at birth" OR "missing women") AND ("life expectancy" OR "natural sex ratio" OR "biological")',
     5: '"hepatitis B" AND (vaccination OR vaccine OR immunization) AND ("sex ratio" OR "male births" OR '
        '"proportion male")'}
SELECT = "select=id,doi,display_name,publication_year,type,cited_by_count,authorships,primary_location,referenced_works"
F = {1: "son preference", 2: "hepatitis B sex ratio", 3: "sex ratio at birth", 4: "missing women"}
ADJ_NOTE = ("Declared ranking is OpenAlex relevance, 'the default for a search filter'. The request has no sort "
            "parameter and relevance_score was not selected, so the ranking actually applied is not checked here.")
CORPUS_NOTE = ("Declared in the run output (02c CORPUS SELECTION RULE), not in a pre-run lock. The declaration "
               "writes filter=referenced_works:W3123222584 and per_page; the executed request used "
               "filter=cites:W3123222584 and per-page. OpenAlex documents cites:W as the works that have W in "
               "their referenced_works, so the two may select the same works, and it accepts both per-page "
               "spellings. That equivalence is not tested here: the textual mismatch is recorded, not resolved.")
RECEPTION_SAMPLE = ['W2057390815', 'W2125485011', 'W2123699796', 'W3122231766', 'W2128916858', 'W1806205041',
                    'W2400620947', 'W2115401314', 'W2066547533', 'W2182501184', 'W2016329099', 'W1964267580']
RECENT_CENSUS = ['W4210337642', 'W4403727727', 'W4397030871', 'W4409543403', 'W4385446270', 'W4399729713']


def main() -> None:
    items = []

    def make(name, key, declared, notes):
        spec = spec_from_log(ROOT, LOG, key, f"{SET_ID}/{name}", declared, notes)
        write_json(HERE / "specs" / f"{name}.json", spec)
        items.append({"spec": f"specs/{name}.json", "response": f"{CN}/{key}", "executor_log": LOG,
                      "log_file_key": key})

    for n, q in Q.items():
        make(f"adj1-Q{n}", f"raw/adj1_Q{n}.json",
             {"path": ADJ, "sha256": file_sha256(ROOT, ADJ), "kind": "pre-run-lock",
              "locked_at": "2026-11-05T10:24:54Z",
              "locked_at_source": f"{CN}/lock/ADJUDICATION-1_lock.txt (executor-written)",
              "requires": ["title_and_abstract.search", q, "from_publication_date:1980-01-01",
                           "to_publication_date:2026-11-05", "type:article|preprint|book-chapter",
                           "per-page=10", SELECT]}, [ADJ_NOTE])
    for n, term in F.items():
        make(f"secE-F{n}", f"raw/secE_F{n}.json",
             {"path": SECE, "sha256": file_sha256(ROOT, SECE), "kind": "pre-run-lock",
              "locked_at": "2026-11-05T10:29:05Z",
              "locked_at_source": f"{CN}/lock/section_E_lock.txt (executor-written)",
              "requires": ["title.search:", "to_publication_date:2005-06-30", "type:article",
                           "sort=cited_by_count:desc", "per-page=3", term]},
             [f'The lock writes the term in quotes (F{n} "{term}"); the request sends it unquoted '
              f'(title.search:{term}). The lock does not say whether the quotes mark a phrase or only delimit '
              f'the term.'])
    make("reception1-top50", "raw/reception1_top50.json",
         {"path": OUT2C, "sha256": file_sha256(ROOT, OUT2C), "kind": "run-output",
          "requires": ["W3123222584", "filter=referenced_works:W3123222584", "sort=cited_by_count:desc",
                       "per_page=50"],
          "response_sha256": "2529864d8e37346ee333a78ce835bf45ddfc78a8464ed656b8cde1dff54dc980"},
         [CORPUS_NOTE])
    make("recent1-top25", "raw/recent1_top25.json",
         {"path": OUT2C, "sha256": file_sha256(ROOT, OUT2C), "kind": "run-output",
          "requires": ["W3123222584", "from_publication_date:2021-11-05", "referenced_works:W3123222584",
                       "sort=cited_by_count:desc", "per_page=25"],
          "response_sha256": "899ac2a524ef89b323e886bdc5fdb09908db38f01e03cbd2dc2975835126c46b"},
         [CORPUS_NOTE])
    samples_decl = {"path": SAMPLES, "sha256": file_sha256(ROOT, SAMPLES)}
    write_json(HERE / "set.json", {
        "schema": "atlas-retrieval-set/0.1", "id": SET_ID,
        "description": ("Batch 1 (Oster 2005, hepatitis B and sex ratios), citation-network v2-candidate.3, Grok Bot "
                        "run merged in Provenance-Atlas #16. Eleven OpenAlex page-1 queries the run executed and "
                        "saved: ADJUDICATION-1 Q1-Q5, Section E F1-F4, RECEPTION-1 and RECENT-1. Specs were "
                        "reconstructed after the run; see each spec's reconstructed_from."),
        "items": items,
        "sample_checks": [
            {"name": "RECEPTION-1 inspection sample", "spec_id": f"{SET_ID}/reception1-top50",
             "seed": 20261105, "population": 50, "k": 12,
             "declared": dict(samples_decl, positions=[7, 9, 10, 11, 20, 27, 28, 39, 40, 41, 42, 44],
                              ids=RECEPTION_SAMPLE)},
            {"name": "RECENT-1 census", "kind": "census", "spec_id": f"{SET_ID}/recent1-top25",
             "declared": dict(samples_decl, ids=RECENT_CENSUS)}],
        "outputs": {"saved_records": "saved-records.jsonl", "samples": "samples.json", "report": "REPORT.txt"}})


if __name__ == "__main__":
    main()
