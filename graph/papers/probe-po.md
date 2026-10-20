---
id: paper:probe-po
type: paper
title: 'ProbePO: Sparse Probes, Redistributed Credit for Critic-Free LLM Reinforcement Learning'
authors:
- 'Diyi Hu'
- 'Ruizhong Qiu'
- 'Lin Qiu'
- 'Hanghang Tong'
- 'Hanqing Zeng'
year: 2026
month: 10
arxiv_id: '2610.24515'
url: https://arxiv.org/abs/2610.24515
methods:
- method:probe-po
cites:
- paper:minimax-m1
- paper:bpco
tags:
- rl-alignment
- rlvr
- credit
- active
---

# ProbePO

## Abstract Summary
GRPO broadcasts one group advantage to every token. ProbePO spends a limited budget on reward-free uncertain prefixes, estimates their verifier value, and redistributes GRPO credit onto segments. Highest of four methods in 16/18 comparisons; vs VinePPO higher on all six benches at 76% less time.

## Key Contributions
1. Budgeted partial-solution probes on a GRPO host.

## Empirical Highlights
- NeurIPS 2026 workshop. DeepSeekMath and Qwen 1.5B-7B.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.24515`
- Code: `none found` (`code_status: none`).
