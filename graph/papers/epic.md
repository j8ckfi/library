---
id: paper:epic
type: paper
title: 'EPIC: Rethinking Trust Regions for Autoregressive LLM Policies via Exact-KL Prefix Importance-Ratio Clipping'
authors:
- 'Chengxi Li'
- 'Hanlin Wu'
- 'Zhicheng Cai'
- 'Huan-ang Gao'
- 'Wei-Ying Ma'
- 'Jingjing Liu'
- 'Hao Zhou'
year: 2026
month: 10
arxiv_id: '2610.29999'
url: https://arxiv.org/abs/2610.29999
methods:
- method:epic
cites:
- paper:minimax-m1
tags:
- rlvr
- importance-sampling
- active
---

# EPIC

## Abstract Summary
EPIC treats the autoregressive prefix as the IS change of measure and clips the exact reverse-KL coordinate r-1-log r of the prefix likelihood ratio instead of a token-local PPO clip.

## Key Contributions
1. EPIC as an active plug-in on `task:math-code-rl-dense`.

## Empirical Highlights
- outperforms standard and sequence-level clipping on math benches; competitive with routing-replay alternatives at lower memory. Does not retarget `method:cispo`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29999`
- Code: `https://github.com/LiChengxi666/EPIC` (`code_status: released`).
