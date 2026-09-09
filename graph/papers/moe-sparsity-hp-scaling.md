---
id: paper:moe-sparsity-hp-scaling
type: paper
title: "Hyperparameter Scaling Laws Across MoE Sparsity"
authors:
  - "Changxin Tian"
  - "Kunlong Chen"
  - "Jia Liu"
  - "Ziqi Liu"
  - "Zhiqiang Zhang"
  - "Jun Zhou"
year: 2026
month: 9
arxiv_id: "2609.08690"
url: "https://arxiv.org/abs/2609.08690"
methods:
  - method:moe-sparsity-hp-scaling
cites: []
tags:
  - pretraining
  - moe
  - hyperparameters
  - moe-sparsity-hp-scaling
---

# Hyperparameter Scaling Laws Across MoE Sparsity

## Abstract Summary
Optimal LR and batch size for MoE shift with activation ratio and are not explained by total or activated parameter count alone. 1,800 pretrain runs, six activated-parameter scales, up to 6B non-embedding params, ~20T tokens, 200,000 H800-GPU-hours. Two regimes: at fixed sparsity, optimal batch size power-laws with tokens D while optimal LR scales with compute C (robust to size/data split); across sparsity, activation ratio A is an extra multiplicative power-law factor. Unified laws transfer; a held-out 12B total / 1/64 activated MoE stays near the predicted optima. Guidance for MoE pretrain HPs. Does not replace DeepSeek-V4 / Kimi-K3 architecture or Muon2.

## Key Contributions
1. **Sparsity-dependent HP transfer** beyond param-count laws.
2. **Two regimes**: B*(D) at fixed sparsity; η*(C); A as a multiplicative factor.
3. **Held-out 12B 1/64 MoE** near predicted optima.

## Empirical Highlights
- 1,800 runs / ~20T tokens / 200k H800-hours.
- Predicted HPs remain close to observed optima on a held-out ultra-sparse 12B.

## Open Source Repository & Resources
- No official GitHub as of 2026-09-09.
