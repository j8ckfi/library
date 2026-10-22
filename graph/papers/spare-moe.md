---
id: paper:spare-moe
type: paper
title: 'SPARE: Sparsity Allocation via Routing Entropy for Efficient MoEs'
authors:
- 'Yifan Yang'
- 'Hanling Yi'
- 'Dongquan Yang'
- 'Feng Lin'
- 'Rong Xiao'
- 'Aijun Li'
- 'Xiaotian Yu'
year: 2026
month: 10
arxiv_id: '2610.29662'
url: https://arxiv.org/abs/2610.29662
methods:
- method:spare-moe
cites:
- paper:deepseek-v4
tags:
- moe
- pruning
- active
---

# SPARE

## Abstract Summary
SPARE is training-free: it prunes more experts in layers whose Top-K gate mass is diffuse (high routing entropy) and keeps experts where routing is peaked.

## Key Contributions
1. SPARE as an active plug-in on `task:pretrain-moe-frontier`.

## Empirical Highlights
- Qwen3-30B-A3B 57.2% to 63.8%; DeepSeek-R1 math/code/science 80.1 to 82.8. Does not retarget `method:deepseek-v4`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29662`
- Code: `none found` (`code_status: none`).
