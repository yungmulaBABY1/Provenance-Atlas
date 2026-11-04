# Evidence view (`atlas.view`)

One view model, two renderings. Built only from records that re-derive by
content replay. It points; you judge.

```sh
python -m atlas.view build tests/atlas/extraction/s2-run1/receipt docs/atlas/views/s2-run1
python -m atlas.view check tests/atlas/extraction/s2-run1/receipt docs/atlas/views/s2-run1
```

`build` writes `view.json` (the shared representation), `index.html` (the
reader page) and `report.txt` (plain text). If the bundle does not replay,
nothing is written. `check` re-renders in memory and requires the committed
files to be identical; CI runs it.

## Who the page is for

Someone who wants to know what the record shows about one research claim, without
knowing the instruments. The technical record sits underneath: every anchor,
every record, every fingerprint, linked from the items above it.

## Rules

1. **No paraphrase of content.** The paper's words are quoted from public
   excerpts only. Model-written text is quoted and tagged as model-written.
   Atlas-authored sentences describe the state of the records (counts, what was
   and was not done), never what the paper or a claim means.
2. **Labels are translated, not replaced.** Plain language comes from the
   declared table `atlas-plain-labels/0.1` (`atlas/view/labels.py`) and is always
   shown with the native label. A label not in the table is an error.
3. **No score, no verdict.** The page states that Atlas does not say whether
   the claim is true. Status chips describe the record (checked, limited, not
   done), not the claim.
4. **Every item resolves.** Each item in `view.json` lists the record IDs it
   comes from; building fails if one does not resolve in the verified bundles.
5. **Source-light.** Only the five quotes already public appear; the other 43
   are counted, not shown.
6. **Typography marks the layer.** Serif: the paper's own words. Sans, tagged:
   written by a model. Monospace: Atlas checks and labels.

## Limits

- One case. The page is generated for the S2 extraction bundle; other bundle
  kinds need their own view model sections.
- Static. No search, filtering, graph or timeline yet.
- Whether a non-specialist understands the evidence better with this page than
  with existing tools is untested. That needs people using it.
