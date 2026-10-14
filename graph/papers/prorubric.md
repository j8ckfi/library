---
id: paper:prorubric
type: paper
title: 'Scoring Higher, Answering Worse: Mitigating Reward Hacking in Rubric-Based RL via Protocol-Level Rubrics'
authors:
- Maoqi Liu
- Junwei He
- Bowen Zhang
- Feiran Li
- Wentao Ma
- Rongyi Lin
- Shuhan Zhong
- Quan Fang
year: 2026
month: 9
arxiv_id: '2609.38847'
url: https://arxiv.org/abs/2609.38847
methods:
- method:prorubric
cites:
- paper:metarubric
- paper:canopy
- paper:draco
tags:
- post-training
- rubric-rl
- reward-hacking
---

# ProRubric

## Abstract Summary
Additive rubric sums let criteria compensate, which the paper treats as reward hacking. Protocol-level grouping requires criteria to hold together. HealthBench appropriateness jumps vs Rubric-RL. HF Daily 2026-10-14.

## Key Contributions
1. Protocol grouping so a high score on one criterion cannot buy out a fail on another.
2. HealthBench 4B/8B vs Rubric-RL (single-paper).
3. Released github.com/Estrellajer/ProRubric.

## Empirical Highlights
- HealthBench 4B appropriateness 36.8 vs Rubric-RL 26.0 (+10.8); coverage 35.0 vs 32.1; untrained 54.1 / 26.6.
- 8B appropriateness 45.8 vs 29.5.
- +1.3 seven-bench avg at 4B.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.38847`
- Code: `https://github.com/Estrellajer/ProRubric` (`code_status: released`).
