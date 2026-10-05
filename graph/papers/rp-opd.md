---
id: paper:rp-opd
type: paper
title: "OPD Before RL: Warm-Starting Rubric-Based RL with On-Policy Distillation"
authors:
  - "Xinpeng Wang"
  - "Wei Shi"
  - "Yu-Chia Chen"
  - "Maria Zontak"
  - "Yun He"
  - "Richard Yuanzhe Pang"
year: 2026
month: 10
arxiv_id: "2610.02781"
url: "https://arxiv.org/abs/2610.02781"
methods:
  - method:rp-opd
cites:
  - paper:opd
  - paper:opd-then-rlvr
tags:
  - post-training
  - distillation
  - rubric
  - neurips
---

# OPD Before RL: Warm-Starting Rubric-Based RL with On-Policy Distillation

## Abstract Summary
Rubric-based RL scores open-ended responses after the full trajectory, so the reward does not mark which tokens mattered. RP-OPD uses the rubric as privileged teacher context for dense token-level OPD on student prefixes, then runs rubric-reward RL past the distillation plateau. NeurIPS 2026. Active plug-in beside OPD and OPD-then-RLVR for non-verifiable / rubric tasks. No public code as of 2026-10-05.

## Key Contributions
1. **Rubric-privileged teacher**: teacher sees the rubric; student does not, and matches next-token distributions at student prefixes.
2. **Then rubric RL**: outcome RL continues after the OPD plateau.
3. **Qwen2.5-7B** HealthBench / ResearchQA / RubricHub 0.673 / 0.797 / 0.829 vs SFT+RL 0.607 / 0.721 / 0.815.

## Empirical Highlights
- Qwen2.5-3B 0.632 / 0.776 / 0.735 vs SFT+RL 0.612 / 0.743 / 0.682.
- Llama-3.1-8B HealthBench 0.634 vs SFT+RL 0.526.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.02781`
- Code: none found as of 2026-10-05 (`code_status: none`).
