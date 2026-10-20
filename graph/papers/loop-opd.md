---
id: paper:loop-opd
type: paper
title: 'LOOP: Recovery-Aligned Iterative Layer Pruning via On-Policy Distillation'
authors:
- 'Liang Xu'
- 'Shufan Shen'
- 'Zhongni Hou'
- 'Yufei Zhang'
- 'Wei Lin'
- 'Guojun Yin'
- 'Shuhui Wang'
year: 2026
month: 10
arxiv_id: '2610.25679'
url: https://arxiv.org/abs/2610.25679
methods:
- method:loop-opd
cites:
- paper:opd
tags:
- distillation
- pruning
- active
---

# LOOP

## Abstract Summary
One-shot layer prune to target size makes OPD recovery harder. LOOP iterates prune and recover using reasoning contribution fused with recovery sensitivity. On Qwen3-4B-Instruct, +7.37 / +9.10 / +6.34 pp vs the strongest one-shot baseline at 15/20/25% prune.

## Key Contributions
1. Recovery-aligned iterative layer prune with interleaved OPD.

## Empirical Highlights
- Holds at 20% prune on Qwen3 1.7B-8B.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.25679`
- Code: `none found` (`code_status: none`).
