---
id: paper:eden
type: paper
title: 'Beyond Policy Rollouts: Embedding-Space Directional Exploration with Anchored Noise for LLM RLVR'
authors:
- Daijiao Liu
- Huiyi Wang
- Lina Yao
- Dong Gong
year: 2026
month: 10
arxiv_id: '2610.16105'
url: https://arxiv.org/abs/2610.16105
methods:
- method:eden
cites:
- paper:exppo
- paper:minimax-m1
tags:
- rl-alignment
- exploration
- rlvr
---

# EDEN

## Abstract Summary
Small GRPO groups from the same prompt collapse to similar traces. EDEN replaces a few rollouts with generations from the prompt plus one appended, group-anchored noisy embedding. Architecture, decoding, and test-time inference stay unchanged; perturbed rollouts get downweighted advantages.

## Key Contributions
1. Anchored embedding-space noise as a rollout-source intervention.
2. Shared per-prompt anchor plus Gaussian variation.
3. Qwen2.5-0.5B / Math-1.5B / Math-7B in verl.

## Empirical Highlights
- Pass@256 avg +6.67 vs GRPO; AIME'25 Qwen2.5-Math-7B +13.33.
- More prompt groups with nonzero group-relative signal.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.16105`
- Code: `none found` (`code_status: none`).

