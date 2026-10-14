---
id: paper:kv4-rl
type: paper
title: 'KV4-RL: Unlocking Faster Asynchronous Rollouts for RLVR with INT4 KV Cache Quantization'
authors:
- Sihwan Park
- Sung-Yub Kim
- Doohyuk Jang
- Eunho Yang
year: 2026
month: 10
arxiv_id: '2610.14448'
url: https://arxiv.org/abs/2610.14448
methods:
- method:kv4-rl
cites:
- paper:trace
- paper:triage
- paper:sao
tags:
- post-training
- kv-cache
- int4
- async-rl
---

# KV4-RL

## Abstract Summary
INT4 KV-cache for async RLVR rollouts, with INT8 protection of attention sinks and a recent-token window. Plain INT4 KV hurts learning even with TIS. Does not replace TRACE / TRIAGE (those own train–rollout FP4 mismatch).

## Key Contributions
1. INT4 KV plus INT8 on sinks (s=16) and recent context inside a 144-token protection budget.
2. Throughput vs BF16 KV on Qwen3-8B-Base GRPO.
3. Negative result: naive INT4 KV finishes 5.24pp lower MATH-500 avg@8 even with TIS.

## Empirical Highlights
- Qwen3-8B-Base GRPO 400 iters: 1.80× rollout / 1.27× iter vs BF16; last 50 iters 1.97× (single-paper).
- MATH-500 avg@8 87.68 vs BF16 88.16; within 0.5pp of BF16 4B/8B six-task mean.
- Plain INT4 KV: −5.24pp MATH-500 avg@8 vs BF16 even with TIS.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.14448`
- Code: `none found` (`code_status: none`).
