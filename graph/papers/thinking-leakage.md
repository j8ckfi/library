---
id: paper:thinking-leakage
type: paper
title: The Thinking Leakage in Reinforcement Learning for LLMs
authors:
- Wenxuan Zhu
- Shuming Liu
- Bang An
- Aznaur Aliev
- Bing Li
- Yibo Yang
- Bernard Ghanem
year: 2026
month: 10
arxiv_id: '2610.14270'
url: https://arxiv.org/abs/2610.14270
methods:
- method:cispo
cites:
- paper:minimax-m1
tags:
- post-training
- reasoning-rl
- think-mode
- gotcha
---

# Thinking Leakage in RL for LLMs

## Abstract Summary
Gotcha on reasoning RL. NO-THINK-mode GRPO gains on Qwen3 1.7B/4B/8B largely reactivate THINK-mode behavior. Evaluate NO-THINK RL claims against a THINK baseline, not only against NO-THINK SFT.

## Key Contributions
1. Qwen3-8B AIME 0.17→0.43 no-think GRPO; think-mode 0.74.
2. 8D subspace G=0.222 removes 75% of the leakage.
3. NO-THINK RL is not a separate skill unless THINK is controlled.

## Empirical Highlights
- Most of the NO-THINK lift is leaked THINK, not a new no-think policy.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.14270`
- Code: `none found` (`code_status: none`).
