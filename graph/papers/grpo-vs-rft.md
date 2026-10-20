---
id: paper:grpo-vs-rft
type: paper
title: 'Is it RL or Data? A Controlled Comparison of GRPO and Rejection-Sampling Fine-Tuning'
authors:
- 'Lakshya Chaudhry'
year: 2026
month: 10
arxiv_id: '2610.25812'
url: https://arxiv.org/abs/2610.25812
methods:
- method:cispo
cites:
- paper:minimax-m1
tags:
- rlvr
- gotcha
---

# GRPO vs RFT

## Abstract Summary
On Bauer et al.'s procedural counting task with Qwen3-4B-Base LoRA, GRPO beats 27-run-tuned RFT at every prompt set: +10.9 pp on curated held-out, +8.4 / +9.2 on easy/mixed at matched rollouts. Mixed-difficulty helps RFT (+3.7); iterated RFT recovers about 30% of the gap. Curating prompts does not help RFT (-2.7).

## Key Contributions
1. GRPO's mixed-difficulty gain is not just the data; RFT given the same prompts still lags.

## Empirical Highlights
- Does not retarget CISPO. Small procedural task.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.25812`
- Code: `none found` (`code_status: none`).
