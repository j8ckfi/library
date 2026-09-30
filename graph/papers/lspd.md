---
id: paper:lspd
type: paper
title: "An RL View of OPD: Least Square Policy Distillation for Sample-Efficient LLM Reasoning"
authors:
  - "Shangzhe Li"
  - "Yuxiao Yang"
  - "Tianrun Yu"
  - "Kaixiang Zhao"
  - "Xiaoyun Wang"
  - "Taylor W. Killian"
  - "Weitong Zhang"
year: 2026
month: 9
arxiv_id: "2609.35505"
url: "https://arxiv.org/abs/2609.35505"
methods:
  - method:lspd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - on-policy
  - off-policy
  - lspd
---

# An RL View of OPD: Least Square Policy Distillation for Sample-Efficient LLM Reasoning

## Abstract Summary
Reverse-KL on-policy distillation is KL-regularized RL with a teacher-induced log-ratio reward. Least-Square Policy Distillation (LSPD) brings optimistic value-based reuse into that view: Huber quadratic matching of student and teacher log-probabilities plus explicit entropy, which supports multiple updates per rollout batch and a replay-buffer off-policy variant (LSPD-RB). Idealized optimistic LSPD has \(\widetilde{\mathcal{O}}(\log K)\) regret. Across six math benches and three teacher–student settings, LSPD gains +1.59 Avg@16 over distillation baselines and preserves Pass@k diversity; LSPD-RB matches vanilla OPD with ~25% of rollout batches / ~10 steps versus >40. UNC / BYU / NVIDIA. Code: `https://github.com/UNCSciML/LSPD`.

## Key Contributions
1. **OPD as KL-regularized RL**: reverse KL is policy optimization under \(R=\log(\pi^E/\pi^{\mathrm{ref}})\).
2. **Least-square matching + entropy**: Huber quadratic student–teacher logp residual with entropy, enabling multi-update and replay.
3. **LSPD-RB**: historical student trajectories; saturates ~10 rollout batches vs >40 one-update-per-batch.

## Empirical Highlights
- Six-bench Avg@16 31.60 (+1.59 vs baselines; +0.91 vs EOPD / +1.99 vs OPD in the measured split). Pass@16 +1.87.
- LSPD-RB 31.51 Avg@16 / 54.86 Pass@16 at ~10 steps, matching OPD with the first ~25% of rollout batches.
- Pass@k through k=64 stays stronger as k grows (diversity, not collapse).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.35505`
- Code: `https://github.com/UNCSciML/LSPD` (`code_status: released`).
