---
id: paper:monitorability-trainable
type: paper
title: 'Monitorability Is Trainable: Post-Training for Chain-of-Thought Monitorability'
authors:
- 'Usman Anwar'
- 'Tim Bakker'
- 'Christos Louizos'
- 'David Krueger'
year: 2026
month: 10
arxiv_id: '2610.29734'
url: https://arxiv.org/abs/2610.29734
methods:
- method:monitorability-trainable
cites:
- paper:reward-misspecification-cot
- paper:minimax-m1
tags:
- rlvr
- monitorability
- active
---

# Monitorability Post-Training

## Abstract Summary
An unsupervised post-training stage maximizes mutual information between chain-of-thought and the final output so monitors stay coupled to what the model does.

## Key Contributions
1. Monitorability Post-Training as an active plug-in on `task:math-code-rl-dense`.

## Empirical Highlights
- recovers most or all lost monitorability on three organisms; on undegraded policies improves judged monitorability and monitor/probe prediction of unsafe behavior. Does not retarget `method:cispo`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29734`
- Code: `none found` (`code_status: none`).
