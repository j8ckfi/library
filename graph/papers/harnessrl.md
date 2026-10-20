---
id: paper:harnessrl
type: paper
title: 'HarnessRL: Co-Evolving Policies with a Just-in-Time Training Harness for Open-Ended RL'
authors:
- 'Xiaoqiang Wang'
- 'Ting-En Lin'
- 'Yuchuan Wu'
- 'Pinyi Zhang'
- 'Caixin Kang'
- 'Ling Li'
- 'Bingxue Qiu'
- 'Jieping Ye'
- 'Yongbin Li'
- 'Bang Liu'
year: 2026
month: 10
arxiv_id: '2610.26426'
url: https://arxiv.org/abs/2610.26426
methods:
- method:harnessrl
cites:
- paper:self-hpo
- paper:harness-playbook
tags:
- agent-harness
- rubric-rl
- active
---

# HarnessRL

## Abstract Summary
Static rubric GRPO hits non-discriminative or spurious rewards (61.6% of pairs in the 4B run). HarnessRL co-evolves prompt, guidance, and criteria with the policy. On Rubric-Mix-10k, Qwen3.5-4B scores 64.5 / 49.8 OOD, +3.0 / +2.8, and nearly halves steps to the best checkpoint.

## Key Contributions
1. Just-in-time training harness with memory and an evolver.

## Empirical Highlights
- Work in progress; code under Tongyi-ConvAI/Qwen-Character/HarnessRL.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.26426`
- Code: `https://github.com/Tongyi-ConvAI/Qwen-Character/tree/main/HarnessRL` (`code_status: released`).
