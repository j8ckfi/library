---
id: method:trackstar
type: method
title: "TrackStar (Compressed Influence and Fact Tracing)"
category: "data-attribution"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "you control the trainer and need peak random-subset LDS"
    reason: "MAGIC is the LDS SOTA (0.983); TrackStar is the scale / final-ckpt / small-lab filtering path"
    use_instead: "method:magic"
  - when: "mix-ratio search or replacing an open pretrain mix"
    reason: "Item scoring for a query is not mix-weight search"
    use_instead: "method:olmo-3"
assumptions:
  - "A loadable checkpoint is enough (no full training trajectory). LoRA-space scoring is the small-lab path."
  - "Random-subset LDS and sorted-subset / filtering-shaped LDS are different protocols; cite both."
last_reviewed: "2026-09-01"
papers:
  - paper:trackstar
  - paper:bergson
recipes:
  - recipe:bergson-trackstar
claims:
  - benchmark: "GPT-2 WikiText FT random-subset LDS (50 queries, N=400, Adam, proj 1024/module)"
    metric: "Spearman rho (LDS)"
    value: "0.184 ± 0.015"
    baseline: "MAGIC 0.983 ± 0.005 / SOURCE 0.387 ± 0.039 / EK-FAC 0.257 ± 0.015"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.11660"
    notes: "Bergson Table 1. Pearson 0.206 ± 0.015. Do not describe 0.18 as too noisy to filter with."
  - benchmark: "Sorted-subset / filtering-shaped LDS (appendix)"
    metric: "Spearman rho (LDS)"
    value: 0.803
    baseline: "MAGIC 1.000 / EK-FAC 0.865"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.11660"
    notes: "Cite this number for LESS-style filtering, not the random-subset 0.184."
tags:
  - interpretability
  - data-attribution
  - trackstar
  - influence
  - fact-tracing
---

# TrackStar (Compressed Influence and Fact Tracing)

## Method Overview
TrackStar is a compressed influence / fact-tracing method: optimizer-state correction, Hessian approximation, random projection, and unit-normalized gradient encodings. Influence is a corrected gradient dot product between query and training examples. Bergson: `bergson trackstar` and LoRA-space `bergson score`.

Status `active`. Small-lab default for filtering. Not `sota` for `task:training-data-attribution` (MAGIC holds the random-subset LDS claim). Does not supersede MAGIC, EK-FAC, SOURCE, or Bergson.

Chang et al. retrieve influential pretraining examples for an 8B model from >160B tokens. Causal influence and lexical fact tracing are misaligned; BM25 still wins at finding passages that explicitly contain a fact.

## When to Use
- Final checkpoint only, or you cannot afford MAGIC's 3–5× train compute.
- LESS-style query-conditioned ranking (`recipe:bergson-trackstar`).
- Fact tracing / scale path on dense transformers (not fused MoE experts).

## When NOT to Use
- Peak random-subset LDS with a recorded trajectory -> `method:magic`.
- Mix-ratio search -> `method:olmo-3`.

## Gotchas & Failure Modes
- Random-subset LDS 0.184 is not the filtering number; sorted-subset LDS is 0.803.
- Fused MoE experts unsupported in Bergson.
- Untuned Hessian damping can still collapse influence quality; check metasmoothness on MAGIC runs, and inversion hyperparameters on influence runs.
