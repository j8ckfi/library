---
id: paper:e2-opsd
type: paper
title: "E2-OPSD: Taming Entropy Overshoot in On-Policy Self-Distillation"
authors:
  - Yifei Liu
  - Minghao Fang
  - Xinyu Gu
  - Chengkai Yao
  - Mengdi Liu
  - Tengfei Ma
  - Jiangbin Zheng
  - Chang Yu
  - Zhangyang Gao
year: 2026
month: 10
arxiv_id: "2610.05048"
url: "https://arxiv.org/abs/2610.05048"
methods:
  - method:e2-opsd
cites:
  - paper:vista
  - paper:opsd-collapse-review
  - paper:u-opsd
tags:
  - post-training
  - distillation
  - opsd
  - e2-opsd
---

# E2-OPSD: Taming Entropy Overshoot in On-Policy Self-Distillation

## Abstract Summary
Vanilla OPSD lets student token entropy rise past the teacher's and stay there (entropy overshoot): the gold-conditioned teacher is poorly matched to student prefixes, and forward KL keeps diffusing the student. E2-OPSD replaces the current answer with a retrieved solved neighbor (exemplar-guided) and uses the student–teacher entropy gap to set each token's correction. Up to +4.3 mean@16 vs OPSD; OOD vs base up to +4.9 mean@16 / +5.5 pass@8. No extra forwards or networks. Beside VISTA / u-OPSD; link opsd-collapse-review. No public code as of 2026-10-06.

## Key Contributions
1. **Names entropy overshoot** as an OPSD failure mode.
2. **Exemplar-guided teaching** from a retrieved solved neighbor, not the current answer.
3. **Entropy-aware token correction** from the student–teacher entropy gap.

## Empirical Highlights
- Up to +4.3 mean@16 vs OPSD on math.
- OOD vs corresponding base: up to +4.9 mean@16 and +5.5 pass@8.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.05048`
- Code: none found as of 2026-10-06 (`code_status: none`).
