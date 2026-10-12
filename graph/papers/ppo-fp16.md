---
id: paper:ppo-fp16
type: paper
title: Structure-Aware Numerical Stabilization for Half-Precision Proximal Policy Optimization
authors:
- Linxuan Wu
- Liang Chen
year: 2026
month: 10
arxiv_id: '2610.13306'
url: https://arxiv.org/abs/2610.13306
methods:
- method:ppo-fp16
cites:
- paper:efficienttdmpc
- paper:dream-mpc
tags:
- control
- ppo
- fp16
- ppo-fp16
---

# Structure-Aware Numerical Stabilization for Half-Precision Proximal Policy Optimization

## Abstract Summary
Naive FP16 PPO is unstable because errors feed back through policy updates and data collection, and PPO constantly compares current vs behavior policies. PPO-FP16 keeps the PPO objective and budget and protects three structures: global scalars, policy-change residuals, and persistent optimizer/parameter writeback. Six continuous-control tasks.

## Key Contributions
1. Global scalar protection, policy-change residual protection, persistent-update protection.
2. No HP retune vs FP32 PPO.
3. Best return-AUC rank with 1.16–2.03× updates and ~72–75% optimizer-state cut.

## Empirical Highlights
- See `method:ppo-fp16` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13306`
- Code: `none found` (`code_status: none`).
