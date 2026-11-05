# Evidence view (`atlas.view`)

One view model, two renderings. Built only from records that re-derive by
content replay. It points; you judge.

```sh
python -m atlas.view build-all      # every page in docs/atlas/views/views.json
python -m atlas.view check-all      # CI: committed pages must be a fresh render
```

The committed pages are declared in `docs/atlas/views/views.json`. Each page names
its receipt and output folder. A question page may link a member's audit record to
another page. A paper page may name its question, which adds a breadcrumb with the
question's declared denominator and changes nothing else on the page. Each page
writes `view.json` (the shared representation), `index.html` (the reader page) and
`report.txt` (plain text). If any receipt does not replay, nothing is written.
`build`/`check RECEIPT OUT` still render one extraction bundle on its own, without
a breadcrumb.

Pages today:

- `docs/atlas/views/power-posing/`: one question over four sources
  ([question.md](question.md)).
- `docs/atlas/views/s2-run1/`: the S2 testosterone claim, reached from the
  question.

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
   declared table `atlas-plain-labels/0.2` (`atlas/view/labels.py`) and is always
   shown with the native label. A label not in the table is an error.
3. **No score, no verdict.** The page states that Atlas does not say whether
   the claim is true. Status chips describe the record (checked, limited, not
   done), not the claim.
4. **Every item resolves.** Each item in `view.json` lists the record IDs it
   comes from; building fails if one does not resolve in the verified bundles.
5. **Source-light.** On the S2 page only the five quotes already public appear;
   the other 43 are counted, not shown. The question page shows no source text.
6. **Typography marks the layer.** Serif: the paper's own words. Sans, tagged:
   written by a model. Monospace: Atlas checks and labels.

7. **Drill-down keeps the corpus.** A page reached from a question says which
   declared source it is and out of how many, and links back.

8. **No source text, even inside model text.** Model-written text that quotes 8 or
   more consecutive words of a source passage is withheld on the page, with a
   notice naming the passage, while the passages are not reviewed for public
   release (audit pages).

## Audit pages (kind `audit`)

`docs/atlas/views/ajr2001/` is a paper page for one imported audit, Grok's AJR 2001
citation-network run. It is rendered from two verified bundles: map links
(`tests/atlas/maplink/ajr2001/receipt`) and challenges
(`tests/atlas/challenge/ajr2001/receipt`). Both are content-replayed before rendering,
and each replay re-verifies what it pins. Both must pin the same import
(`AUDIT_RECEIPTS_DISAGREE`).

It shows, in this order:
- at a glance: what was checked, what is limited, what was not done;
- the audit on record;
- the claim under audit, in each of its wordings;
- the seven findings, with the run's own labels and how each lines up with the map;
- the three review items, with every challenger's outcome and a notice where they
  disagree;
- the sources, with read states and passage counts;
- what is not established.

No research question record exists for AJR 2001 yet. `atlas.question` is built around
the power-posing packet, and extending it would rebuild that merged receipt, so the
page says it is a paper page.

Label table `atlas-plain-labels/0.3` adds the labels this page needs (additions only).
Meanings of the run's own labels come from the instrument's definitions
(`prompts/research-analysis/2-citation-network.txt`). Bare bundle IDs are now named by
kind in refs: `import`, `claim links`, `map links`, `challenges`. This changed one
ref's text on the power-posing page from "run" to "import".

## Limits

- Three page kinds: extraction bundles, research questions and imported audits. Other
  bundle kinds need their own view model sections.
- Static. No search, filtering, graph or timeline yet.
- Whether a non-specialist understands the evidence better with this page than
  with existing tools is untested. That needs people using it.
