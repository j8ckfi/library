---
id: paper:tapo
type: paper
title: 'Trajectory-Aware Policy Optimization: Closing the State Distribution Gap in Long-Horizon LLM RL'
authors:
- Zhicheng Cai
- Weinan Dai
- Yuyan Zhou
- Wei-Ying Ma
- Ya-Qin Zhang
- Hao Zhou
year: 2026
month: 10
arxiv_id: '2610.13020'
url: https://arxiv.org/abs/2610.13020
methods:
- method:tapo
cites:
- paper:scalerl
- paper:minimax-m1
tags:
- post-training
- rlvr
- tapo
---

# Trajectory-Aware Policy Optimization: Closing the State Distribution Gap in Long-Horizon LLM RL

## Abstract Summary
Token- or sequence-level mismatch control (GRPO/GSPO) misses trajectory-induced state-distribution shift that compounds over long rollouts. TAPO puts the off-policy state-distribution correction into the LLM RL objective, uses a geometric-mean estimator for variance, and length-aware dynamic clipping so late tokens are not over-updated.

## Key Contributions
1. State-distribution correction derived from the off-policy policy gradient.
2. Geometric-mean estimator + length-aware clip.
3. Up to +48% / +12% vs GRPO on math / code; less collapse at long horizon.

## Empirical Highlights
- See `method:tapo` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13020`
- Code: `none found` (`code_status: none`).
