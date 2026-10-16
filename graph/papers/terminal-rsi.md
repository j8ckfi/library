---
id: paper:terminal-rsi
type: paper
title: 'Terminal-RSI: Recursive Self-Improving Terminal Agents via Recursive Self-Rewrite and Policy-Refine'
authors:
- Junyao Yang
- Zongxia Li
- Yucheng Shi
- Zhongzhi Li
- Ruhan Wang
- Ruiwen Zhou
- Haitao Mi
- Shuicheng Yan
- Leowei Liang
year: 2026
month: 10
arxiv_id: '2610.22192'
url: https://arxiv.org/abs/2610.22192
methods:
- method:terminal-rsi
cites:
- paper:rrsi
- paper:aide2
tags:
- agent-harness
- rsi
- terminal
---

# Terminal-RSI

## Abstract Summary
Terminal agents need verifier outcomes turned into policy updates and partial progress turned into completed tasks. Terminal-RSI alternates Recursive Self-Rewrite of verified trajectories with critic-inheriting Recursive Policy-Refine, plus TB-GAE, Family Dense Reward, and Success-Prioritized Reward.

## Key Contributions
1. RSR / RPR two-phase recursive refine from Qwen3.8-27B.
2. Turn-Boundary Skip-Observation GAE, FDR, SPR.
3. Terminal-Bench 2.1 / 3.0 / 4.0 / Hard plus LHTB and SWR100.

## Empirical Highlights
- Terminal-RSI-27B: TB4.0 19.84%, TB2.1 86.52%, TB3.0 16.95%, TB Hard 79.00%.
- LHTB process 0.21→0.37 and strict 0/46→5/46; SWR100 3%→6%.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22192`
- Code: `none found` (`code_status: none`).

