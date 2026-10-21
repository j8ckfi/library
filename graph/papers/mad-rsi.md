---
id: paper:mad-rsi
type: paper
title: 'MaD-RSI: Model-as-Data for Recursive Self-Improvement of Agent Harnesses'
authors:
- 'Yu Cui'
- 'Hong He'
- 'Ruiqing Yue'
- 'Sicheng Pan'
- 'Zhuoyu Sun'
- 'Yifei Liu'
- 'Ting Li'
- 'Wenzhuo Zhu'
- 'Baohan Huang'
- 'Haibin Zhang'
- 'Cong Zuo'
year: 2026
month: 10
arxiv_id: '2610.28201'
url: https://arxiv.org/abs/2610.28201
methods:
- method:mad-rsi
cites:
- paper:harness-playbook
tags:
- agent-harness
- rsi
- active
---

# MaD-RSI

## Abstract Summary
MaD-RSI trains one shared harness on failure trajectories from several heterogeneous LLMs, treating model differences as training evidence rather than a post-hoc transfer test.

## Key Contributions
1. Model-as-data harness RSI plus two cross-model evaluation metrics.

## Empirical Highlights
- Improves cross-model generalization and cuts training cost vs single-model RSI.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28201`
- Code: `https://github.com/cuiyu-ai/MaD-RSI` (`code_status: released`).
