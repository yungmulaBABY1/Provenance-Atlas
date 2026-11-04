# Map links (`atlas.maplink`) — M1 Increment E

Deterministic, offline linking of an imported audit's findings to a **separately
produced Stage-1 claim map**. It points; you judge.

`atlas.claims` reads the claim map an audit output carries itself. A citation-network
output run in full-sequence mode carries none. It relies on an upstream Stage-1 output
instead, so `atlas.claims` records `CLAIM MAP ABSENT` and nothing can be linked. This
package supplies that upstream map as a pinned input and records what can be said about
it by text alone.

It does not run an audit, call a model, read the source paper, or decide whether two
differently worded statements are the same claim. That is always
`UNRESOLVED_REQUIRES_REVIEW`.

## Run it

```sh
python -m atlas.maplink build tests/atlas/maplink/ajr2001/context.json --out .atlas/maplink
python -m atlas.maplink show tests/atlas/maplink/ajr2001/receipt/records.jsonl     # verified view
python -m atlas.maplink replay tests/atlas/maplink/ajr2001/receipt/manifest.json \
    tests/atlas/maplink/ajr2001/receipt/records.jsonl --level content
```

`show` replays the bundle at content level and renders only if every record
re-derives. That replay includes the claim-link receipt the bundle depends on.

## What it reads

- **One claim-link receipt** (`atlas.claims`), pinned by hash. It is content-replayed
  in every build (`CLAIM_LINK_RECEIPT_NOT_VERIFIED` if it does not re-derive), and its
  import bundle is loaded from the receipt's own pins. Its claim map must be `ABSENT`.
  An output that carries its own map is out of scope for 0.1
  (`OUTPUT_HAS_ITS_OWN_MAP`).
- **One upstream Stage-1 output**, pinned by hash and parsed with the strict reader
  `atlas-claim-extraction-output/1` (`atlas.extraction.output`).
- **The claim-extraction instrument**, pinned. It must be the same contract the
  claim-link receipt checked against (`CONTRACT_PIN_MISMATCH`).
- **Declared provenance of the map**: producer kind and identity and who declares
  them. 0.1 covers maps with **no run prompt and no run receipt** only. A receipted
  Stage-1 run belongs in `atlas.extraction` (`RECEIPTED_RUN_NOT_SUPPORTED`).

The map must be about the audit's target work (`UPSTREAM_MAP_TARGET_MISMATCH`).

## What it records

| Record | Contents |
|---|---|
| `UpstreamMap` | Origin `UPSTREAM_STAGE_1_OUTPUT`; provenance with `run_prompt: NOT_RECORDED`, `run_receipt: NONE`. Also: the map's own preflight line compared with the pinned instrument's blob and SHA-256; whether the map names the target DOI; whether the **audit output names the map's path** (`PATH_NAMED_IN_AUDIT_OUTPUT` = documented, otherwise `NOT_NAMED_LINK_DECLARED_IN_CONTEXT_ONLY`); field states, section hashes and an anchor count, with `NOT_VERIFIED_IN_ATLAS` for the quotes. |
| `MapStatement` | Each table field (1–6), the Field 6 section statement (designated) and the one-line summary, at exact offsets in the pinned file. Each is attributed to the declared producer. Each carries the producer's own verification column as `producer_verification_state`, which Atlas does not check. |
| `Reconciliation` | The audit output's restatement of map fields 1, 3 and 6, compared as text with the map's own text. The instrument requires reconciliation before an audit is combined with others; this is only its text level. |
| `TargetAlignment` | One per finding: its target against the map's Field 6, with the claim-link label carried unchanged as `claim_link_identity`. |
| `TextComparison` | Exact and `nfc-whitespace/2` comparisons. No semantic judgment. |

### Claim identity labels

| Label | When |
|---|---|
| `SAME_TEXT` / `SAME_TEXT_AFTER_NORMALIZATION` | The finding's target text equals the map's Field 6 section statement, exactly or after normalization. A backing comparison is required. |
| `DECLARED_BY_REFERENCE` | The target is a bare "claim map field 6" reference. |
| `DECLARED_NOT_FIELD_6` | The target uses the instrument's form "MAP GAP: this finding targets [claim], not map field 6." |
| `DECLARED_NOT_ON_MAP` | The target uses the form "MAP GAP: this finding concerns [claim], which does not appear on the claim map." |
| `UNRESOLVED_REQUIRES_REVIEW` | Different wording, a qualified reference, or MAP GAP wording that differs from both instrument forms (`WORDING_DIFFERS_FROM_INSTRUMENT_FORMS`). |
| `NO_TARGET_STATED` | No target claim. |

`atlas.claims` 0.1 records every MAP GAP as `DECLARED_NOT_ON_MAP`, which is
accurate when no map exists. With the upstream map present, the two instrument
forms can be told apart. The original label is kept in `claim_link_identity`.

A mention of another field inside a MAP GAP ("targets map field 4 public
wording") is recorded as `MENTIONED_IN_DECLARED_TARGET; not resolved as the
target`. A mention is never a link.

## The AJR 2001 case (`tests/atlas/maplink/ajr2001/`)

Inputs:
- Grok's citation-network claim-link receipt.
- Grok's Stage-1 map `examples/research/acemoglu-colonial-origins/01_claim_extraction.md`.

What the receipt records:
- **Link to the map:** the audit output names the map's path at line 5, so the link is
  documented by the output.
- **Instrument:** the map's preflight names the pinned instrument's blob and SHA-256.
- **Reconciliation:** fields 1, 3 and 6 all differ as text. The citation stage reworded
  the map instead of pasting it, so all three are `UNRESOLVED_REQUIRES_REVIEW`.
- **The map's own Field 6:** it is worded three ways (section, table cell, summary), and
  none of them match.
- **Findings:**

  | Findings | Label | Why |
  |---|---|---|
  | 1, 2, 4, 6 | `DECLARED_NOT_FIELD_6` | Finding 4 also mentions map field 4. |
  | 3 | `UNRESOLVED_REQUIRES_REVIEW` | It ends "not map field 6 itself.", which is not an instrument form. |
  | 5, 7 | `UNRESOLVED_REQUIRES_REVIEW` | Their target is the audit's restatement, which differs from the map's Field 6 text. |

## Limits

- **Producer identity is self-reported.** The map has no run prompt, no run receipt
  and no independent record of how it was made.
- **Quotes are not checked.** The map's quotes (18 source anchors) are not verified
  against AJR 2001, because the source text is not committed. Grok's scratch anchor
  probe is not imported as verification.
- **Rights not reviewed.** The receipt copies the map's table text, which includes
  short quoted fragments of AJR 2001 and one sentence of the 2024 Nobel press release.
  It does not copy the source-anchor quotes. The rights review of the map file applies
  to this receipt too.
- **Depends on PR #7.** The receipt pins files under
  `examples/research/acemoglu-colonial-origins/`.
