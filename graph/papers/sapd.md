---
id: paper:sapd
type: paper
title: "SAPD: Step-Aligned Privileged Distillation"
authors:
  - "Tianle Wang"
  - "Jiayu Liu"
  - "Ruizhi Zhao"
  - "Ning Miao"
year: 2026
month: 10
arxiv_id: "2610.09665"
url: "https://arxiv.org/abs/2610.09665"
methods:
  - method:sapd
cites:
  - paper:vista
  - paper:opd
tags:
  - post-training
  - distillation
  - privileged
  - sapd
---

# SAPD: Step-Aligned Privileged Distillation

## Abstract Summary
On-policy post-training needs costly rollouts. SAPD is rollout-free self-distillation that turns a known reference solution into step-aligned distributional supervision: each reasoning transition gets targeted privileged guidance instead of undifferentiated gold context. Beats SFT and label smoothing on math averages; competitive with on-policy RL and self-distillation; about 2x training-loop speedups vs on-policy baselines. Code: Miaow-Lab/SAPD. Beside VISTA.

## Key Contributions
1. Fixed demonstrations can compete with on-policy RL if supervision is step-aligned and distributional.
2. Associate each reasoning transition with targeted privileged guidance from the known solution progression.
3. Rollout-free; about 2x training-loop speedups vs on-policy baselines.

## Empirical Highlights
- Math reasoning: outperforms SFT and label smoothing on average; competitive with on-policy RL and self-distillation.
- Largely preserves OOD coding. About 2x training-loop speedups vs on-policy baselines.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.09665`
- Code: `https://github.com/Miaow-Lab/SAPD` (`code_status: released`).
