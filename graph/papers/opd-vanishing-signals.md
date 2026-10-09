---
id: paper:opd-vanishing-signals
type: paper
title: "Why On-Policy Distillation Sometimes Fails: Vanishing Learning Signals"
authors:
  - "Lei Zhao"
  - "Qichao Zhao"
  - "Bowen Zuo"
  - "Qishi Zhan"
year: 2026
month: 10
arxiv_id: "2610.11247"
url: "https://arxiv.org/abs/2610.11247"
methods:
  - method:opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - opd
  - gotcha
  - opd-vanishing-signals
---

# Why On-Policy Distillation Sometimes Fails: Vanishing Learning Signals

## Abstract Summary
Caution/evidence paper. Larger-scale OPD teachers can plateau: average final loss reduction 25.1% after 200 updates vs 96.2% for self-RL teachers (further RL of the initial student). Training logs associate plateaus with an early decline in a gradient-based learning-signal proxy while substantial loss remains. Local recovery guarantee for teachers close to the student in a shared parameterization. Relative parameter change stays 0.025-0.098%; linear CKA >0.98. Code: leizhao7/opd-learning-signals. Does not retarget OPD.

## Key Contributions
1. Larger-scale teachers can starve OPD gradients while loss remains.
2. Self-RL (same-size, further-RL) teachers recover 96.2% loss reduction vs 25.1% for larger-scale teachers after 200 updates.
3. Small relative parameter change and high CKA; limited representation adaptation is a hypothesized cause.

## Empirical Highlights
- Code generation and math reasoning. Average final loss reduction 25.1% vs 96.2% (self-RL teachers) after 200 updates.
- Relative parameter change 0.025-0.098%; linear CKA >0.98 across layers.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.11247`
- Code: `https://github.com/leizhao7/opd-learning-signals` (`code_status: released`).
