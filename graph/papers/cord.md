---
id: paper:cord
type: paper
title: 'CORD: Conflict-Aware Optimization for Joint RL and Distillation in Agents'
authors:
- 'Wenhao Yu'
- 'Zhengcheng Wang'
- 'Jiahong Liu'
- 'Zexuan Qiu'
- 'Minda Hu'
- 'Shaohang Wei'
- 'Jiafei Lyu'
- 'Junyan Lyu'
year: 2026
month: 10
arxiv_id: '2610.29965'
url: https://arxiv.org/abs/2610.29965
methods:
- method:cord
cites:
- paper:opd
tags:
- distillation
- agent-rl
- active
---

# CORD

## Abstract Summary
CORD combines RL and distillation gradients once per optimizer mini-batch, projecting away the component that fights a chosen protected objective when a gate fires.

## Key Contributions
1. CORD as an active plug-in on `task:student-distillation`.

## Empirical Highlights
- ALFWorld +1.5 to +15.9 pp across three recipes; WebShop SDAR 60.7% to 64.6% on two of three pairs. Does not retarget `method:opd`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29965`
- Code: `https://github.com/LvAoAo/CORD-release` (`code_status: released`).
