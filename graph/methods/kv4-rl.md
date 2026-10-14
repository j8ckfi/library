---
id: method:kv4-rl
type: method
title: KV4-RL
category: quantization
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: FP4 RL train-side vs rollout-side quantization mismatch
  reason: TRACE / TRIAGE own NVFP4 train–rollout alignment; this is INT4 KV on rollouts
  use_instead: method:trace
- when: variable environment latency / async stragglers rather than KV memory
  reason: SAO remains the async-straggler first hop
  use_instead: method:sao
assumptions:
- GRPO-family RLVR rollouts with a long KV cache. Paper: Qwen3-4B/8B-Base, 400 iters.
- Protection: INT8 sinks s=16 plus recent window in a 144-token budget.
- No public code as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:kv4-rl
recipes:
- recipe:kv4-rl
claims:
- benchmark: Qwen3-8B-Base GRPO 400 iters; 4B/8B six-task mean
  metric: rollout / iter speedup vs BF16 KV; MATH-500 avg@8
  value: 1.80× rollout / 1.27× iter (last 50 1.97×); MATH-500 87.68 vs BF16 88.16;
    within 0.5pp six-task mean; naive INT4 −5.24pp even with TIS
  baseline: BF16 KV; naive INT4 KV + TIS (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.14448
  notes: Does not retarget TRACE / TRIAGE or SAO.
tags:
- post-training
- kv-cache
- int4
- active
---

# KV4-RL

## Method Overview
Quantize the rollout KV cache to INT4. Keep attention sinks and a recent window in INT8 so the cache does not destroy learning. TIS on the policy does not salvage naive INT4 KV.

## When to Use
- Async RLVR rollouts are KV-bound and you can spare a small INT8 protection budget.

## When NOT to Use
Train–rollout NVFP4 mismatch → `method:trace` / `method:triage`. Async stragglers → `method:sao`. Dense Pass@1 loss → `method:cispo`.

## Relation to Existing SOTA
Active plug-in on `task:fp4-rl-train-rollout-alignment` (`sota_for: []`). Mention on `task:agentic-async-rl`. Does **not** replace TRACE / TRIAGE or SAO.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-14.
- Dropping the INT8 sink/recent shield collapses MATH-500 even with TIS.
