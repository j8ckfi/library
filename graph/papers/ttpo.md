---
id: paper:ttpo
type: paper
title: "TTPO: Test-Time Policy Optimization"
authors:
  - "Aozhe Wang"
  - "Zhengxi Lu"
  - "Jianze Wang"
  - "Shangke Lv"
  - "Ying Liu"
  - "Weiming Lu"
  - "Jun Xiao"
  - "Yueting Zhuang"
  - "Hua Yang"
  - "Qianglong Chen"
  - "Yongliang Shen"
year: 2026
month: 8
arxiv_id: "2608.27448"
url: "https://arxiv.org/abs/2608.27448"
methods:
  - method:ttpo
cites:
  - paper:opd
  - paper:minimax-m1
  - paper:scalerl
  - paper:grpo
tags:
  - test-time-training
  - reasoning
  - rl-alignment
  - distillation
  - ttpo
---

# TTPO: Test-Time Policy Optimization

## Abstract Summary
Test-Time Policy Optimization (TTPO) is a label-free test-time training (TTT) framework for mathematical reasoning that overcomes the vulnerability of majority-vote pseudo-labeling. While typical pseudo-labeling breaks when the consensus vote is erroneous (misleading every token in supervised distillation), TTPO exploits an asymmetric observation: rollouts disagreeing with the consensus vote are almost always incorrect regardless of whether the majority vote itself was right or wrong. TTPO establishes an asymmetric dual objective: it distills rollouts that agree with the consensus pseudo-answer via on-policy self-distillation (OPSD), while simultaneously penalizing disagreeing rollouts using Grouped Reinforcement Learning (RL).

## Key Contributions
1. **Asymmetric Error Principle in Test-Time Consensus**: Identifies that disagreeing trajectories carry robust negative signals even when the majority vote pseudo-label is corrupted, while agreeing trajectories provide positive distillation signals when refined.
2. **Dual Distillation and Grouped RL Objective**: Couples OPSD on agreeing completions with Grouped RL penalty on disagreeing completions, eliminating the need for ground-truth verifiers or external teacher models during test-time adaptation.
3. **Token-Level Selection Mechanism**: Refines updates by down-weighting already-converged token positions during distillation and selectively penalizing high-confidence errors during the RL update.
4. **Empirical Performance**: Matches label-supervised OPSD across five competition-level benchmarks without labels, raises Qwen3-1.7B from 38.0% to 45.2% during test-time training, and yields +25.2% to +36.4% improvements on non-thinking models.

## Open Source Repository & Resources
- Project Page: `https://zju-real.github.io/TTPO`
- Code Repository: `https://github.com/ZJU-REAL/TTPO`
