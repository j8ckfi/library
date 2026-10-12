---
id: paper:cbpo
type: paper
title: 'Cross-Behavior Policy Optimization: Unified Learning from Offline Demonstrations and On- and Off-Policy
  Rollouts via a Shared Regression Target'
authors:
- Du Cheng
- Junyu Lu
- Jingfan Zhang
- Yuzhuo Zhang
- Haoxuan Jia
- Shichao Weng
year: 2026
month: 10
arxiv_id: '2610.12830'
url: https://arxiv.org/abs/2610.12830
methods:
- method:cbpo
cites:
- paper:minimax-m1
- paper:opd
tags:
- post-training
- rlvr
- cbpo
---

# Cross-Behavior Policy Optimization: Unified Learning from Offline Demonstrations and On- and Off-Policy Rollouts via a Shared Regression Target

## Abstract Summary
SFT then RL splits offline demos from rollouts. CBPO puts positive/negative offline completions, references, and current/historical rollouts on one fixed-reference regression target. The generating policy does not enter the target, so no IS, stored behavior logps, or critic. Restricting sources gives offline / on-policy / off-policy variants; Unified combines them.

## Key Contributions
1. Shared regression target across offline, on-policy, and off-policy records.
2. No behavior log-probs, IS, or critic.
3. Qwen3-1.7B Unified +2.33 / +4.44 vs SFT+DAPO; history replay helps.

## Empirical Highlights
- See `method:cbpo` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.12830`
- Code: `none found` (`code_status: none`).
