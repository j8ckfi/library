---
id: paper:rewardverse
type: paper
title: "RewardVerse: Rubric-Guided Policy Optimization for Video Reward Modeling"
authors:
  - "Zhenchen Tang"
  - "Yang Li"
  - "Songlin Yang"
  - "Bo Peng"
  - "Xiaotong Zhao"
  - "Shuai Li"
  - "Haotian Fan"
  - "Alan Zhao"
  - "Jing Dong"
year: 2026
month: 9
arxiv_id: "2609.22947"
url: "https://arxiv.org/abs/2609.22947"
methods:
  - method:rewardverse
cites:
  - paper:diffusion-opsd
  - paper:self-opd
  - paper:orarl
  - paper:grpo
tags:
  - diffusion
  - video
  - reward-model
  - rewardverse
---

# RewardVerse: Rubric-Guided Policy Optimization for Video Reward Modeling

## Abstract Summary
Video reward models that map a clip to one scalar suffer from scalar drift: scores collapse into a narrow band or shift across prompts, which makes the RM a bad RL teacher. RewardVerse inserts a dynamic rubric (themes, weights, scoring tips) as an intermediate representation between the evaluation query and the scorer. Rubric-Guided Policy Optimization (RGPO) first warms up the scorer on self-evolving seed rubrics, then jointly trains the rubric generator and scorer from only 30 preference pairs per dimension. The deployed readout is multi-theme soft-logits, not free-form floats. EvalVerse pointwise and VGRB pairwise beat non-oracle video RMs; downstream GRPO of Wan-2.2-A14B improves Imaging Quality without the VBench collapse seen under VideoReward.

## Key Contributions
1. **Rubric-as-reward for video RMs**: query-conditioned dynamic rubric as a scoring anchor.
2. **RGPO**: two-stage GRPO (scorer warm-up, then joint rubric+scorer) with 30 pairs/dimension.
3. **Soft-logits pointwise protocol**: bypasses natural-language score collapse and pairwise order bias.

## Empirical Highlights
- EvalVerse 16-D Joint RGPO: mean PLCC 0.554 / SRCC 0.446; highest PLCC on 14/16 dimensions (Logic 0.750 vs next-best 0.593).
- VGRB pairwise Acc w/o Tie: TA (unseen) 0.623 vs VisionReward 0.611; VQ (seen) 0.660 vs 0.590.
- Ablation macro PLCC 0.530 vs rubric-free trained 0.439 on the same 480-pair budget.
- Downstream Wan-2.2-A14B GRPO: Imaging Quality 0.640→0.653; VBench-Text 0.428→0.446 vs VideoReward 0.392.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.22947`
- Code: `https://github.com/2kxx/RewardVerse` (`code_status: released`).
