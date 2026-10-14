---
id: paper:two-clocks-rlvr
type: paper
title: 'Two Clocks: Why Larger Rollout Batches Learn Slower but Fail on Schedule in Reinforcement Learning with Verifiable Rewards'
authors:
- Yuante Li
- Junwei Quan
- Kai Qiu
- Kate Zhang
- Yicheng Tao
year: 2026
month: 10
arxiv_id: '2610.18853'
url: https://arxiv.org/abs/2610.18853
methods:
- method:cispo
cites:
- paper:minimax-m1
tags:
- post-training
- rlvr
- batch-size
- gotcha
---

# Two Clocks (RLVR rollout batch vs sqrt-LR)

## Abstract Summary
Caution/evidence paper on dense RLVR. Sqrt-LR scaling preserves drift per sample but not progress. There is an LR-dependent critical rollout batch. The failure clock is invariant along the sqrt rule. Does not retarget CISPO.

## Key Contributions
1. Two clocks: progress vs failure, not a single step clock.
2. Qwen2.5-Math-1.5B 16× batch: 4096 fails at 56–80 steps / 512 after 648, both after 30–50k samples.
3. Announced repo WinstonLiyt/two-clocks-rlvr 404 as of 2026-10-14.

## Empirical Highlights
- Larger rollout batches fail on schedule even when per-sample drift is preserved by sqrt-LR.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.18853`
- Code: `https://github.com/WinstonLiyt/two-clocks-rlvr` (`code_status: announced`; 404 as of 2026-10-14).
