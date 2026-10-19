---
id: paper:multiagent-opd
type: paper
title: 'MultiAgent-OPD: End-to-End Training of Hierarchical Multi-Agent Systems with On-Policy Distillation'
authors:
- 'Yuhan Sun'
- 'Jiaxin Zhao'
- 'Yongdong Luo'
- 'Yibo Hu'
- 'Meiguang Jin'
- 'Junfeng Ma'
- 'Weixun Wang'
- 'Weihang Pan'
- 'Zhongan Bi'
year: 2026
month: 10
arxiv_id: '2610.23234'
url: https://arxiv.org/abs/2610.23234
methods:
- method:multiagent-opd
cites:
- paper:opd
tags:
- distillation
- opd
- multi-agent
- active
---

# MultiAgent-OPD

## Abstract Summary
In a hierarchical multi-agent system, a Leader assigns tasks and subagents carry them out. Jointly training the Leader and the subagents is difficult because a final answer gives only indirect feedback to the subagents. An LLM judge can score the performance of the subagents, but these scores depend on the judge's own assessment of the quality of subagents' responses. We present MultiAgent-OPD, which combines on-policy distillation with reinforcement learning to jointly train a shared-parameter Leader-Searcher-Answerer team end to end. We first train a Teacher in a Searcher-Answerer workflow using answer correctness. During team training, the frozen Teacher scores student-generated search an

## Key Contributions
1. MultiAgent-OPD jointly trains a shared-parameter Leader-Searcher-Answerer team: a frozen Teacher trained on Searcher-Answerer correctness scores student search and summary tokens while the Leader learns from team success.

## Empirical Highlights
- 38.68%; +4.06 vs Prompted Critic; +2.61 vs C-MAS + RL

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23234`
- Code: `none found` (`code_status: none`).
