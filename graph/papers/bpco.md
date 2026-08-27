---
id: paper:bpco
type: paper
title: "Best Practice Critic Optimization"
authors:
  - "Penghui Qi"
  - "Xiangxin Zhou"
  - "Wee Sun Lee"
year: 2026
month: 8
arxiv_id: "2608.23566"
url: "https://arxiv.org/abs/2608.23566"
methods:
  - method:bpco
cites:
  - paper:sao
  - paper:grpo
  - paper:dapo
  - paper:dr-grpo
tags:
  - post-training
  - rl-alignment
  - actor-critic
  - bpco
---

# Best Practice Critic Optimization

## Abstract Summary
Best Practice Critic Optimization (BPCO) establishes a robust actor-critic training recipe for large language models that estimates token-level advantages from a single response per prompt. By resolving core instabilities in critic-based LLM training—combining DPPO clipping, value predictions bounded to the known reward range, Monte Carlo value targets, unnormalized policy advantages, length-adaptive GAE, and privileged training-only critic inputs—BPCO matches or exceeds group-relative baselines (such as GRPO) across mathematical reasoning tasks from 1.5B to 30B-A3B MoE models while sampling only one rollout per prompt.

## Key Contributions
1. **Diagnosis of Critic Instabilities**: Identifies critical failure modes in standard PPO for LLMs, including unbounded linear value head predictions, variance-amplifying advantage normalization, and fixed-GAE horizon mismatch on variable-length responses.
2. **Integrated BPCO Recipe**: Assembles DPPO probability-shift clipping, reward-bounded value heads, unbiased Monte Carlo value targets, raw unnormalized advantages, and length-adaptive GAE.
3. **Privileged Critic Conditioning**: Supplies the training-only critic with reward-defining reference answers, solutions, or evaluation rubrics hidden from the deployed policy.

## Open Source Repository
- Implementation: `https://github.com/QPHutu/golden_critic`
