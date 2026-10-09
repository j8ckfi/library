---
id: paper:grpodropout
type: paper
title: "GRPODropout: Less is More for Online Reinforcement Learning Rollouts"
authors:
  - "Hexuan Deng"
  - "Zihao Yan"
  - "Xuebo Liu"
  - "Shuo Nie"
  - "Yue Wang"
  - "Chen Wang"
  - "Zhaohua Zhang"
  - "Tianwen Jiang"
  - "Qiuyong Xiao"
  - "Jihong Zhang"
  - "Min Zhang"
year: 2026
month: 10
arxiv_id: "2610.11854"
url: "https://arxiv.org/abs/2610.11854"
methods:
  - method:grpodropout
cites:
  - paper:grpo
  - paper:eapo
tags:
  - post-training
  - rlvr
  - grpo
  - entropy
  - grpodropout
---

# GRPODropout: Less is More for Online Reinforcement Learning Rollouts

## Abstract Summary
GRPO-family RLVR collapses entropy when high-probability positive-advantage rollouts keep getting reinforced. Algorithm-level entropy bonuses and token reweighting leave the group intact. GRPODropout deletes a small number of those easy positives before the update and recenters advantages on what remains. Same sampling budget, fewer update samples, higher accuracy than GRPO. Code: hexuandeng/GRPODropout. Beside CISPO / EAPO.

## Key Contributions
1. Rollout-level entropy collapse: high-probability positive-advantage traces dominate the update.
2. Drop a small set of those rollouts, then recenter retained advantages.
3. Less-is-more: fewer update samples, higher accuracy and actor entropy vs GRPO.

## Empirical Highlights
- Higher accuracy than original GRPO at the same sampling budget while updating on fewer rollouts.
- Higher actor entropy than GRPO; complementary to token-level entropy bonuses.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.11854`
- Code: `https://github.com/hexuandeng/GRPODropout` (`code_status: released`).
