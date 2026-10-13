---
id: paper:branchopd
type: paper
title: Branching On-Policy Distillation
authors:
- Dongyang Chen
- Shudong Liu
- Shubo Li
- Duoxun Tang
- Jinwei Liang
- Zehuan Wu
- Lewei Lu
year: 2026
month: 10
arxiv_id: '2610.13481'
url: https://arxiv.org/abs/2610.13481
methods:
- method:branchopd
cites:
- paper:opd
tags:
- post-training
- distillation
- opd
- branchopd
---

# Branching On-Policy Distillation

## Abstract Summary
BranchOPD branches student rollouts at uncertain or teacher-disagreement tokens, resamples continuations from that prefix, and applies token-level teacher KL on the main path plus branches. Protocol-boundary repair (PBR) covers agent tool turns. Beats vanilla OPD and multi-rollout OPD (n=7) with fewer student tokens. Plug-in on `task:student-distillation`; mention on `task:outcome-only-long-horizon-agent-rl`.

## Key Contributions
1. Branch at uncertain / teacher-disagreement tokens; resample student continuations from the prefix.
2. Token-level teacher KL on the trunk and the branches.
3. Protocol-boundary repair for multi-turn agents.

## Empirical Highlights
- +18.55pp math avg@16 vs vanilla OPD.
- +13.8pp ALFWorld vs vanilla OPD.
- Beats multi-rollout OPD (n=7) with ~19% / 31% fewer student tokens on ALFWorld / WebShop.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13481`
- Code: `https://github.com/chendy25/BranchOPD` (`code_status: announced`; empty stub as of 2026-10-13).
