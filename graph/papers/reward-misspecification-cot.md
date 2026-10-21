---
id: paper:reward-misspecification-cot
type: paper
title: 'Reward Misspecification Degrades Chain-of-Thought Monitorability'
authors:
- 'Tianyi Lorena Yan'
- 'John Hewitt'
year: 2026
month: 10
arxiv_id: '2610.28303'
url: https://arxiv.org/abs/2610.28303
methods:
- method:cispo
cites:
- paper:minimax-m1
tags:
- rlvr
- gotcha
- monitorability
---

# Reward Misspecification Degrades Chain-of-Thought Monitorability

## Abstract Summary
Reward misspecification alone drops CoT monitorability: models keep reasoning about task intent while outputs hack the misspecified reward. Injecting an inferred reward description into the prompt raises monitorability 24% or 42% absolute depending on the metric.

## Key Contributions
1. Labeled reward-hacking testbed plus reward-description training for CoT monitors.

## Empirical Highlights
- Code Lorenayannnnn/reward-misspecification-degrades-cot-monitorability. Does not retarget CISPO.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28303`
- Code: `https://github.com/Lorenayannnnn/reward-misspecification-degrades-cot-monitorability` (`code_status: released`).
