---
id: paper:trackstar
type: paper
title: "Scalable Influence and Fact Tracing for Large Language Model Pretraining"
authors:
  - "Tyler A. Chang"
  - "Dheeraj Rajagopal"
  - "Tolga Bolukbasi"
  - "Lucas Dixon"
  - "Ian Tenney"
year: 2024
month: 10
arxiv_id: "2410.17413"
url: "https://arxiv.org/abs/2410.17413"
methods:
  - method:trackstar
cites:
  - paper:ek-fac
tags:
  - interpretability
  - data-attribution
  - trackstar
  - influence
  - fact-tracing
---

# Scalable Influence and Fact Tracing for Large Language Model Pretraining

## Abstract Summary
TrackStar is a gradient-based training-data attribution method for LLM pretraining: optimizer-state correction, a task-specific Hessian approximation, random projection, and unit-normalized encodings. The paper retrieves influential examples for an 8B model from a pretraining corpus of over 160B tokens without subsampling. It distinguishes *causal influence* (what changes the prediction) from *factual attribution* (passages that entail the fact); BM25 still wins at finding explicit fact-containing passages. Bergson ships the first public implementation.

## Key Contributions
1. **Scale path**: influence retrieval at 8B / 160B-token pretraining without corpus pre-filtering.
2. **TrackStar formula**: projected, Hessian-corrected, unit-normalized gradient dot product with optimizer second-moment correction.
3. **Influence vs attribution misalignment**: gradient influence and lexical fact tracing diverge; they align more as models and tokens scale.

## Empirical Highlights
- Bergson GPT-2 WikiText FT random-subset LDS (Table 1, Adam, proj 1024/module): Spearman 0.184 ± 0.015 / Pearson 0.206 ± 0.015.
- Sorted-subset / filtering-shaped LDS (appendix): TrackStar 0.803 (vs MAGIC 1.000, EK-FAC 0.865). Use this number for filtering; do not treat 0.18 as too noisy to filter with.
- Small-lab default in Bergson: LoRA-space `bergson score` / `bergson trackstar` for LESS-style query-conditioned ranking.
