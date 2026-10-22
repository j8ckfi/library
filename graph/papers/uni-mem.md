---
id: paper:uni-mem
type: paper
title: 'Uni-Mem: Learning a Long-Horizon Agentic Memory Manager with Unified Online Policy Optimization'
authors:
- 'Zhiqian Xia'
- 'Jielong Tang'
- 'Ling-An Zeng'
- 'Shixiong Kai'
- 'Rong Yao'
- 'Hao Kong'
- 'Xiao Dong'
- 'Wei Wang'
year: 2026
month: 10
arxiv_id: '2610.29671'
url: https://arxiv.org/abs/2610.29671
methods:
- method:uni-mem
cites:
- paper:ace
tags:
- agent-memory
- grpo
- active
---

# Uni-Mem

## Abstract Summary
Uni-Mem is one policy for memory construction and retrieval. Stage-Decoupled GRPO alternates group comparisons so long memory-management traces are not scored as a single confounded GRPO group.

## Key Contributions
1. Uni-Mem as an active plug-in on `task:agent-memory`.

## Empirical Highlights
- Stage-Decoupled GRPO jointly trains construction and retrieval under one policy, avoiding confounded group comparisons of vanilla GRPO on long memory trajectories. Does not retarget `method:ace`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29671`
- Code: `none found` (`code_status: none`).
