---
id: paper:gca
type: paper
title: 'Grounded Credit Assignment in Reinforcement Learning for Multi-Turn Search Agents'
authors:
- 'Qirui Liu'
- 'Hao Chen'
- 'Yi Wen'
- 'Weijie Shi'
- 'Yao Zhao'
- 'Xianhe Chen'
- 'Hao Zhao'
- 'Xing Tang'
- 'Weihong Luo'
- 'Yuyu Luo'
year: 2026
month: 10
arxiv_id: '2610.23148'
url: https://arxiv.org/abs/2610.23148
methods:
- method:gca
cites:
- paper:iris
tags:
- search-agent
- grpo
- credit
- active
---

# GCA

## Abstract Summary
Outcome-reward reinforcement learning such as GRPO gives every token of a search-agent rollout the same advantage, although the rollout exercises two capabilities: finding evidence and using it. We show that accuracy improves without grounding: Search-R1 raises accuracy on all seven QA benchmarks, yet on Bamboogle the evidence-supported share of correct answers falls from 84.0% to 42.9%. We attribute this to GRPO's credit assignment: rollouts that retrieve answer-bearing evidence are favoured in aggregate only in proportion to their accuracy gain over the rest, a grounding gap that answering from memory or misusing evidence shrinks or reverses. To address this, we propose Grounded Credit Ass

## Key Contributions
1. GCA splits GRPO credit using verifiable sub-outcomes: a wrong answer is blamed more than the search that found the evidence, and a correct answer that bypasses retrievable evidence is credited less. The correction is never negative on evidence-finding search and is capped at 10% of each token's advantage.

## Empirical Highlights
- +5.7 EM Qwen2.5-3B / +6.3 EM Qwen3-30B-A3B vs Search-R1; evidence-supported share 76.9%→93.4%

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23148`
- Code: `none found` (`code_status: none`).
