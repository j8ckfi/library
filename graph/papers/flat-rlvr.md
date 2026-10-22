---
id: paper:flat-rlvr
type: paper
title: 'Flat-RLVR: Sharpness-Aware Reinforcement Learning with Verifiable Rewards for Reasoning Capacity in LLMs'
authors:
- 'Yeonbum Kim'
- 'Hyun Kyu Lee'
- 'Sung Whan Yoon'
year: 2026
month: 10
arxiv_id: '2610.29281'
url: https://arxiv.org/abs/2610.29281
methods:
- method:flat-rlvr
cites:
- paper:minimax-m1
tags:
- rlvr
- sharpness
- active
---

# Flat-RLVR

## Abstract Summary
Flat-RLVR adds sharpness-aware minimization to GRPO-family RLVR so the policy sits in flat-reward regions instead of collapsing onto peaked rare-yet-correct modes.

## Key Contributions
1. Flat-RLVR as an active plug-in on `task:math-code-rl-dense`.

## Empirical Highlights
- improved sample diversity while maintaining single-attempt accuracy vs GRPO variants. Does not retarget `method:cispo`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29281`
- Code: `none found` (`code_status: none`).
