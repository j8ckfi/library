---
id: paper:lmopd
type: paper
title: "Lexicographic Multi-Objective On-Policy Distillation"
authors:
  - "Doseok Jang"
  - "Jon Ander Campos"
  - "Youran Qi"
year: 2026
month: 10
arxiv_id: "2610.02359"
url: "https://arxiv.org/abs/2610.02359"
methods:
  - method:lmopd
cites:
  - paper:open-mopd
  - paper:corrgrpo
  - paper:dara
tags:
  - post-training
  - distillation
  - multi-teacher
  - multi-objective
---

# Lexicographic Multi-Objective On-Policy Distillation

## Abstract Summary
RLVR usually scores answer correctness; useful models also need quality reasoning and conciseness. Scalarized multi-reward RL can raise a lower-priority score by hurting a higher-priority one. LMOPD distills from reward-specialist teachers under an explicit priority order: for each student rollout, pick the specialist of the first deficient objective, then project its centered log-policy correction away from components that oppose higher-priority specialists. Evaluated on a 30B-A3B MoE. Active plug-in beside Open-MOPD; mention on `task:multi-reward-rlvr` as the priority-ordered alternative to scalarized multi-reward RL. No public code as of 2026-10-05.

## Key Contributions
1. **Lexicographic routing**: first deficient objective's specialist teaches that prefix.
2. **Projection**: remove correction components that oppose higher-priority specialists.
3. **Two-expert retained gain**: pass@1 102.9% / RQ 103.3% / Conc 46.9% avg 84.4 vs Rewarded Soup 67.1 / GDPO(25,1,1) 18.9.

## Empirical Highlights
- Four-expert retained gain pass@1 90.6 / RQ-corr 88.6 avg 39.6 vs gated RLVR 34.4.
- Raw two-expert pass@1 0.7450 vs base 0.7109 vs capability expert 0.7440.
- GDPO is a paper baseline, not a library method. Paper Open-MOPD numbers are not the library 83.4% bake-off.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02359`
- Code: none found as of 2026-10-05 (`code_status: none`).
