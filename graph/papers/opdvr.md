---
id: paper:opdvr
type: paper
title: "On-policy Distillation with Verifiable Reward"
authors:
  - "Wenze Lin"
  - "Jiale Zhao"
  - "Xitai Jiang"
  - "Songde Rao"
  - "Yining Li"
  - "Shenzhi Wang"
  - "Bingxiang He"
  - "Gao Huang"
year: 2026
month: 8
arxiv_id: "2608.24696"
url: "https://arxiv.org/abs/2608.24696"
methods:
  - method:opdvr
cites:
  - paper:opd
  - paper:tulu3-rlvr
  - paper:verigate
  - paper:minimax-m1
  - paper:scalerl
  - paper:grpo
tags:
  - post-training
  - distillation
  - rlvr
  - reasoning
  - opdvr
---

# On-policy Distillation with Verifiable Reward

## Abstract Summary
On-policy Distillation with Verifiable Reward (OPDVR) combines on-policy distillation (OPD) with reinforcement learning with verifiable rewards (RLVR) without introducing extra balancing hyperparameters. By reformulating the implicit reward of sampled-token OPD based on trajectory correctness and applying a ReLU gating mechanism, correct trajectories receive non-negative rewards and incorrect ones receive non-positive rewards, aligning token-level teacher guidance with task-level verification.

## Key Contributions
1. **Implicit Reward Reformulation**: Analyzes sampled-token OPD through an RLVR lens, identifying that raw log-ratios can assign negative advantages to tokens on correct trajectories and positive advantages on incorrect ones.
2. **ReLU Gating Mechanism**: Standardizes reward signs via ReLU gating keyed by trajectory correctness, ensuring teacher guidance magnifies correct token updates and suppresses overconfident erroneous predictions with zero extra hyperparameters.
3. **Group Relative Policy Distillation (GRPD)**: Integrates OPDVR with group-relative policy gradient optimization (GRPO/Dr.GRPO), demonstrating consistent improvements over standard OPD across six mathematical reasoning benchmarks.

## Open Source Repository
- Implementation: `https://github.com/LeapLabTHU/OPDVR`
