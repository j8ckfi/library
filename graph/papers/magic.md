---
id: paper:magic
type: paper
title: "Magic: Near-Optimal Data Attribution for Deep Learning"
authors:
  - "Andrew Ilyas"
  - "Logan Engstrom"
year: 2025
month: 4
arxiv_id: "2504.16430"
url: "https://arxiv.org/abs/2504.16430"
methods:
  - method:magic
cites:
  - paper:ek-fac
tags:
  - interpretability
  - data-attribution
  - magic
  - unrolling
  - lds
---

# Magic: Near-Optimal Data Attribution for Deep Learning

## Abstract Summary
MAGIC (Metagradient-based Attribution via Ground-truth Influence Computation) estimates how adding or removing training data changes a specific trained model's predictions by combining classical influence with metadifferentiation through the training trajectory. In the single-model attribution setting, MAGIC nearly matches leave-k-out retrain ground truth. Bergson (`paper:bergson`) is the first public implementation.

## Key Contributions
1. **Single-model data attribution**: predict how *this* trained model would have behaved under different training data, rather than the average of a randomized learning algorithm.
2. **Unrolled metagradients**: exact (up to implementation) influence via differentiation through the optimizer steps.
3. **Near-optimal LDS** vs influence-function and TRAK-style baselines on vision and language settings in the paper; Bergson Table 1 reports GPT-2 WikiText FT Spearman 0.983 ± 0.005 (Adam).

## Empirical Highlights
- Bergson GPT-2 WikiText FT (Table 1; 50 queries, N=400 retrains, 95% CI, Adam): MAGIC Spearman 0.983 ± 0.005 / Pearson 0.979 ± 0.006 vs SOURCE 0.387 / EK-FAC 0.257 / TrackStar 0.184.
- Sorted-subset / filtering-shaped LDS (appendix): MAGIC 1.000 vs EK-FAC 0.865 vs TrackStar 0.803.
- Requires the training trajectory. Open-weight final checkpoints without a recorded run use the influence-function path only (`method:trackstar` / `method:ek-fac`).
