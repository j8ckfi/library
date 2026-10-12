---
id: paper:gppo
type: paper
title: 'Generalized Proximal Policy Optimization: Unifying LLM RL Algorithms from the Perspective of Divergence'
authors:
- Zhicheng Cai
- Xinyuan Guo
- Hanlin Wu
- Weinan Dai
- Yuyan Zhou
- Wei-Ying Ma
- Ya-Qin Zhang
- Hao Zhou
year: 2026
month: 10
arxiv_id: '2610.13015'
url: https://arxiv.org/abs/2610.13015
methods:
- method:gppo
cites:
- paper:scalerl
- paper:minimax-m1
- paper:respo
tags:
- post-training
- rlvr
- gppo
---

# Generalized Proximal Policy Optimization: Unifying LLM RL Algorithms from the Perspective of Divergence

## Abstract Summary
PPO's clip is a geometrically degenerate trust region that cannot adapt resistance to policy shift. GPPO gives a generalized f-divergence trust-region with a monotonic improvement guarantee, plus estimator topologies beyond single-sample MC. PPO, DAPO, DPPO, and RIPO sit on a Divergence × Estimator grid. Both axes matter in the paper's bake-off.

## Key Contributions
1. f-divergence trust-region theory for LLM PPO.
2. Estimator topologies beyond single-sample MC.
3. Best instantiation up to +50% / +14% vs GRPO on math / code.

## Empirical Highlights
- See `method:gppo` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13015`
- Code: `none found` (`code_status: none`).
