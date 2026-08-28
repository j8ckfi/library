---
id: paper:scalerl
type: paper
title: "The Art of Scaling Reinforcement Learning Compute for LLMs"
authors:
  - "ScaleRL Research Authors"
year: 2025
month: 10
arxiv_id: "2510.13786"
url: "https://arxiv.org/abs/2510.13786"
methods:
  - method:cispo
cites:
  - paper:minimax-m1
tags:
  - post-training
  - rl-alignment
  - cispo
  - scalerl
---

# The Art of Scaling Reinforcement Learning Compute for LLMs

## Abstract Summary
ScaleRL packages Clipped IS-weight Policy Optimization (CISPO) into an empirical scaling recipe for large language models, demonstrating superior asymptote performance over DAPO and GSPO on reasoning tasks.

## Key Contributions
1. **RL Scaling Recipe**: Integrates PipelineRL-8, forced length interrupt, prompt-average loss, batch-level advantage normalization, FP32 logits, zero-variance filtering, and filtering prompts with pass \(\ge 0.9\).
2. **Empirical Asymptote**: Validates CISPO stability and sample efficiency over DAPO and GSPO under scaled compute.

## Open Source Repository
- Implementation: `none found`
