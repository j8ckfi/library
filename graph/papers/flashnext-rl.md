---
id: paper:flashnext-rl
type: paper
title: 'FlashNext-RL: A System Optimization Study for Long-Horizon Agentic RL of Qwen3.8-Flash-Next'
authors:
- 'Zhewei Yao'
- 'Yuxiong He'
year: 2026
month: 10
arxiv_id: '2610.28998'
url: https://arxiv.org/abs/2610.28998
methods:
- method:flashnext-rl
cites:
- paper:miles
- paper:qwen38-next
tags:
- systems
- agentic-rl
- active
---

# FlashNext-RL

## Abstract Summary
FlashNext-RL is a prime-rl + vLLM stack for Qwen3.8-Flash-Next: freeze early layers / n-gram / indexer / MTP, then host-offload, MoE, sparse-attention, and gated-residual kernels so 131K SWE RL fits one 8xB200 node.

## Key Contributions
1. FlashNext-RL as an active plug-in on `task:frontier-rl-posttrain-stack`.

## Empirical Highlights
- full-model non-padding throughput 395 to 4438 tok/s/GPU (32K to 131K optimized); steps 5-15 average 22.4 min/iter at 1024 trainable rollouts / 131072 context. Does not retarget `method:miles`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28998`
- Code: `none found` (`code_status: none`).
