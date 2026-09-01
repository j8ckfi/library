---
id: method:source-unrolling
type: method
title: "SOURCE (Approximate Unrolled Differentiation)"
category: "data-attribution"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "you control the full training trajectory and need peak LDS"
    reason: "MAGIC is the exact unroll; SOURCE is a few-checkpoint approximation"
    use_instead: "method:magic"
  - when: "final checkpoint only, no intermediate snapshots"
    reason: "SOURCE needs a handful of checkpoints (paper C=6)"
    use_instead: "method:trackstar"
  - when: "mix-ratio search or replacing an open pretrain mix"
    reason: "Approximate unroll is not mix-weight search"
    use_instead: "method:olmo-3"
assumptions:
  - "Intermediate checkpoints exist. Bergson command: bergson approxunrolling."
  - "GPT-2 WikiText FT LDS 0.387 is well below MAGIC 0.983; niche, not a default."
last_reviewed: "2026-09-01"
papers:
  - paper:source-tda
  - paper:bergson
claims:
  - benchmark: "GPT-2 WikiText FT LDS (50 queries, N=400, Adam)"
    metric: "Spearman rho (LDS)"
    value: "0.387 ± 0.039"
    baseline: "MAGIC 0.983 ± 0.005 / EK-FAC 0.257 ± 0.015 / TrackStar 0.184 ± 0.015"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.11660"
    notes: "Bergson Table 1. Pearson 0.431 ± 0.048. Few-checkpoint approx unroll."
tags:
  - interpretability
  - data-attribution
  - source
  - unrolling
  - niche
---

# SOURCE (Approximate Unrolled Differentiation)

## Method Overview
SOURCE approximates unrolled differentiation with an influence-function-like formula over a small number of checkpoints (paper: C=6), so it can incorporate optimizer and multi-stage structure without storing every step. Bergson: `bergson approxunrolling`.

Status `niche`. LDS 0.387 sits between MAGIC and EK-FAC on the Bergson GPT-2 WikiText table. Does not supersede MAGIC, TrackStar, EK-FAC, or Bergson.

## When to Use
- You have a few intermediate checkpoints and cannot afford full MAGIC unroll.
- Non-converged or multi-stage runs where classical influence assumptions fail.

## When NOT to Use
- Full trajectory available -> `method:magic`.
- Final ckpt only -> `method:trackstar`.
- Mix-ratio search -> `method:olmo-3`.

## Gotchas & Failure Modes
- Intermediate checkpoints are required.
- Not the small-lab filtering default (TrackStar) and not the LDS default (MAGIC).
