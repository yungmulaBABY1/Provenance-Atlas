"""Reconstruct the Batch 2 (Baumeister 1998) locked-query specs and set.json.

Run from the repository root:  python tests/atlas/retrieval/baumeister-batch2/reconstruct_specs.py
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
RUN = "examples/research/baumeister-ego-depletion"
CN = f"{RUN}/citation-network-v2cand3"
LOG = f"{RUN}/logs/retrieval_log.jsonl"
ADJ = f"{CN}/lock/ADJUDICATION-1_search_record.md"
SECE = f"{CN}/lock/section_E_preregistration.md"
OUT2C = f"{CN}/02c_citation_network_v2cand3.md"
SAMPLES = f"{CN}/lock/SAMPLES_draw.txt"
SET_ID = "baumeister-1998-batch2"
Q = {1: '"ego depletion" AND (replication OR "registered replication" OR "multilab" OR "multi-site" OR preregistered)',
     2: '"ego depletion" AND ("meta-analysis" OR "publication bias" OR "small-study")',
     3: '("ego depletion" OR "self-control") AND glucose',
     4: '"ego depletion" AND (motivation OR "process model" OR "opportunity cost")',
     5: '("ego depletion" OR willpower) AND ("implicit theories" OR "lay theories" OR beliefs)',
     6: '"ego depletion" AND (fatigue OR frustration OR mood OR "manipulation check")',
     7: '("decision fatigue" OR "strength model of self-control" OR "self-control strength")'}
SELECT = "select=id,doi,display_name,publication_year,type,cited_by_count,authorships,primary_location,referenced_works"
F = {1: "mental fatigue", 2: "learned helplessness", 3: "mood persistence", 4: "experimenter expectancy",
     5: "mental effort"}
ADJ_NOTE = ("Declared ranking is OpenAlex relevance, 'the default for a search filter'. The request has no sort "
            "parameter and relevance_score was not selected, so the ranking actually applied is not checked here.")
RECEPTION_SAMPLE = ['W1968689002', 'W2108897328', 'W2022472850', 'W2093761921', 'W2058490785', 'W1976788357',
                    'W2100482303', 'W3122622199', 'W2105985103', 'W2146569853', 'W2122634808', 'W2081900501']
RECENT_CENSUS = ['W4385606438', 'W4214866453', 'W4291001390', 'W3217148206', 'W4402300076', 'W4283313664',
                 'W4291535426', 'W4323652556', 'W4310804025', 'W4220818821', 'W4402676278', 'W4409103534',
                 'W4281731168', 'W4390011768', 'W4311667985', 'W4311640673', 'W3211993193', 'W4205581247',
                 'W4321368994', 'W4200151748', 'W4308964018', 'W4302307858', 'W4285800368', 'W4280566821',
                 'W4366496226']


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
              "locked_at": "2026-11-05T11:28:23Z",
              "locked_at_source": f"{CN}/lock/ADJUDICATION-1_lock.txt (executor-written)",
              "requires": ["title_and_abstract.search", q, "from_publication_date:1998-01-01",
                           "to_publication_date:2026-11-05", "type:article|preprint|book-chapter|review",
                           "per-page=10", SELECT]}, [ADJ_NOTE])
    for n, term in F.items():
        make(f"secE-F{n}", f"raw/secE_F{n}.json",
             {"path": SECE, "sha256": file_sha256(ROOT, SECE), "kind": "pre-run-lock",
              "locked_at": "2026-11-05T11:28:40Z",
              "locked_at_source": f"{CN}/lock/section_E_lock.txt (executor-written)",
              "requires": ["title.search:", "to_publication_date:1998-04-30", "type:article",
                           "sort=cited_by_count:desc", "per-page=3", term]},
             [f'The lock writes the term in quotes (F{n} "{term}"); the request sends it unquoted '
              f'(title.search:{term}). The lock does not say whether the quotes mark a phrase or only delimit '
              f'the term.'])
    make("reception1-top50", "raw/reception1_top50.json",
         {"path": OUT2C, "sha256": file_sha256(ROOT, OUT2C), "kind": "run-output",
          "requires": ["filter=cites:W2123817056", "sort=cited_by_count:desc", "per-page=50"],
          "response_sha256": "dc54ce7c6ef2fb6440b0a4bf9ac0b54acd48cc57b823c8f6c0160cd602916a25"},
         ["Declared in the run output (02c CORPUS SELECTION RULE), not in a pre-run lock."])
    make("recent1-top25", "raw/recent1_top25.json",
         {"path": OUT2C, "sha256": file_sha256(ROOT, OUT2C), "kind": "run-output",
          "requires": ["cites:W2123817056", "from_publication_date:2021-11-05", "sort=cited_by_count:desc",
                       "per-page=25"],
          "response_sha256": "7101107597f4ebf092df16ef755aca5e216fe786ea4efa52c664a7e38cec6c60"},
         ["Declared in the run output (02c CORPUS SELECTION RULE), not in a pre-run lock."])
    samples_decl = {"path": SAMPLES, "sha256": file_sha256(ROOT, SAMPLES)}
    write_json(HERE / "set.json", {
        "schema": "atlas-retrieval-set/0.1", "id": SET_ID,
        "description": ("Batch 2 (Baumeister et al. 1998), citation-network v2-candidate.3, Grok Bot run merged in "
                        "Provenance-Atlas #15. Fourteen OpenAlex page-1 queries the run executed and saved: "
                        "ADJUDICATION-1 Q1-Q7, Section E F1-F5, RECEPTION-1 and RECENT-1. Specs were "
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
