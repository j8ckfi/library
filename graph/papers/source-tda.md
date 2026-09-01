---
id: paper:source-tda
type: paper
title: "Training Data Attribution via Approximate Unrolled Differentiation"
authors:
  - "Juhan Bae"
  - "Wu Lin"
  - "Jonathan Lorraine"
  - "Roger Grosse"
year: 2024
month: 5
arxiv_id: "2405.12186"
url: "https://arxiv.org/abs/2405.12186"
methods:
  - method:source-unrolling
cites:
  - paper:ek-fac
tags:
  - interpretability
  - data-attribution
  - source
  - unrolling
  - influence
---

# Training Data Attribution via Approximate Unrolled Differentiation

## Abstract Summary
SOURCE connects implicit-differentiation influence functions with unrolled differentiation. It uses an influence-function-like formula over a small number of checkpoints (paper: C=6) to approximate unrolling without storing every optimizer step. It is motivated for non-converged models and multi-stage pipelines where classical influence assumptions fail. Bergson implements it as `bergson approxunrolling`.

## Key Contributions
1. **Approximate unroll**: unrolling benefits (optimizer, schedule, multi-stage, non-convergence) at influence-function cost, given intermediate checkpoints.
2. **Fewer checkpoints than full unroll**: a handful of snapshots rather than all T gradient updates.
3. **Counterfactual prediction**: outperforms implicit-differentiation TDA where those methods struggle.

## Empirical Highlights
- Bergson GPT-2 WikiText FT LDS (Table 1, Adam): Spearman 0.387 ± 0.039 / Pearson 0.431 ± 0.048.
- Needs intermediate checkpoints; a final open-weight checkpoint alone is not enough.
- Status in this library: `niche` relative to MAGIC (full unroll) and TrackStar (final-ckpt influence).
