---
id: paper:rlvr-momentum
type: paper
title: When Does Momentum Help in Reinforcement Learning with Verifiable Rewards?
authors:
- Kaifei Wang
- Zikang Shan
- Liwei Wang
- Yinyu Ye
- Han Zhong
year: 2026
month: 10
arxiv_id: '2610.20413'
url: https://arxiv.org/abs/2610.20413
methods:
- method:rlvr-momentum
cites:
- paper:minimax-m1
- paper:adam-beta-cubic
tags:
- post-training
- rlvr
- momentum
- optimizer
---

# When Does Momentum Help in RLVR

## Abstract Summary
Recent RLVR runs questioned first-moment momentum. A KL-regularized bandit analysis says increasing beta inside a safe regime accelerates exact NPG, but sampled gradients hide the gain unless beta scales with eta so eta/(1-beta) stays constant.

## Key Contributions
1. Exact-gradient acceleration vs sampled-gradient fluctuation scales.
2. Practical rule: raise beta as eta falls.
3. Qwen3-4B-Base GRPO and Qwen2.5-32B AdamW checks.

## Empirical Highlights
- Qwen2.5-32B AdamW: increasing beta1 improves mean validation accuracy by nearly 2pp over the conventional choice.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.20413`
- Code: `none found` (`code_status: none`).
