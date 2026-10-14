---
id: paper:tetpo
type: paper
title: 'Target-ESS Tempered Policy Optimization (TETPO): Smooth Variance Control via Bridge Importance Sampling'
authors:
- Shayan Mohajer Hamidi
- Kayhan Behdin
- Wenhui Zhu
- Aida Rahmattalabi
- Jincheng Cao
- Jelena Markovic-Voronov
- Alborz Geramifard
year: 2026
month: 10
arxiv_id: '2610.14440'
url: https://arxiv.org/abs/2610.14440
methods:
- method:tetpo
cites:
- paper:sao
- paper:minimax-m1
tags:
- post-training
- importance-sampling
- ess
- rlvr
---

# TETPO

## Abstract Summary
Replace the IS weight ρ by ρ^α and choose α so the batch hits a target effective sample size (ESS). Smooth variance control for off-policy / stale rollouts. Does not replace SAO or CISPO.

## Key Contributions
1. Tempering exponent α solved to a target ESS κ rather than a hard clip.
2. Dense-math eval vs M2PO / GSPO / GEPO (single-paper).
3. Same host as GRPO-family trainers; not an async-straggler kernel.

## Empirical Highlights
- k=32 avg@16 Table 1: Qwen3-Base-1.7B 44.4 vs M2PO 42.3 / GSPO 39.0.
- Llama-3.2-3B-Instruct 18.5 vs GEPO 16.2.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.14440`
- Code: `none found` (`code_status: none`).
