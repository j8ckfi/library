---
id: task:fp4-rl-train-rollout-alignment
type: task
title: "FP4 RL Train–Rollout Quantization Alignment"
domain: "post-training"
summary: "Stabilize native FP4 / NVFP4 reinforcement learning when the train-side rounding grid disagrees with rollout-side quantization, especially on MoE LMs."
scope: "Low-precision RL train–rollout mismatch. Dual-active first hops are TRACE (rollout-guided QAT that caches mantissa/scale) and TRIAGE (direction-aware mismatch stabilization). Not native FP4 pretrain from scratch, not the Pass@1 loss, not the production RL engine."
out_of_scope:
  - "Native FP4 forward/backward hardware training from scratch (Quartet-II / MXFP4)"
  - "Dense math/code Pass@1 RLVR loss (CISPO)"
  - "MoE/VL RLVR algorithm (SAPO)"
  - "Frontier RL post-train engine (Miles)"
  - "W4A4 PTQ noise law (KBBQ)"
redirects:
  - when: "native FP4 forward/backward hardware training from scratch, not RL train–rollout mismatch"
    to: "task:fp4-hardware-training"
  - when: "single-turn dense math/code Pass@1 RLVR"
    to: "task:math-code-rl-dense"
  - when: "MoE/VL RLVR loss rather than FP4 train–rollout alignment"
    to: "task:math-code-rl-moe"
  - when: "production post-train stack rather than FP4 RL numerics"
    to: "task:frontier-rl-posttrain-stack"
current_sota:
  - method: method:trace
    as_of: "2026-10-07"
    benchmark: "Qwen3.5-35B-A3B / 122B-A10B / Qwen3.8-Flash-Next FP4 RL"
    metric: "rollout speedup vs unaligned FP4 RL"
    value: "up to 5.4× rollout speedup"
    notes: "TRACE (2610.07767). Dual-active with TRIAGE. Method status active. Does not replace Quartet-II."
  - method: method:triage
    as_of: "2026-10-07"
    benchmark: "Qwen3-4B / Qwen3-30B-A3B native NVFP4 RL, >34500 GPU-h B300"
    metric: "rollout throughput vs BF16"
    value: "up to 2.3×"
    notes: "TRIAGE (2610.07043). Dual-active with TRACE. Method status active. No head-to-head vs TRACE."
methods:
  - method:trace
  - method:triage
  - method:quartet-ii
  - method:mxfp4-mi355x
  - method:sapo
  - method:cispo
last_reviewed: "2026-10-07"
tags:
  - post-training
  - quantization
  - fp4
  - nvfp4
  - rl-alignment
  - moe
---

# FP4 RL Train–Rollout Quantization Alignment

## Problem Definition
Native FP4 / NVFP4 RL is not the same problem as training from scratch in FP4. The train-side rounding grid can disagree with rollout-side quantization; MoE routing amplifies the mismatch. This task owns **aligning or stabilizing that grid**, not the kernel of Pass@1 RLVR and not Quartet-II pretrain.

This is **not** native FP4 hardware training from scratch.

## Evaluation Protocol
- **Primary Benchmarks**: MoE LM RL rollouts under FP4/NVFP4 (Qwen3.5-35B-A3B / 122B-A10B; Qwen3-4B / 30B-A3B); rollout throughput and end-to-end step time versus unaligned FP4 RL.
- **Evaluation Pitfalls**: TRACE and TRIAGE have **no head-to-head**. TRACE caches rollout mantissa/scale into QAT; TRIAGE rebalances amplifying negative-advantage/negative-gap updates. Do not retarget Quartet-II.

## SOTA Recommendation (as of 2026-10-07)
- **Primary (rollout-guided QAT, this task only)**: **TRACE** (`method:trace`, `paper:trace` `arXiv:2610.07767`). Status `active`. Dual-active with TRIAGE.
- **Primary (direction-aware NVFP4 mismatch, this task only)**: **TRIAGE** (`method:triage`, `paper:triage` `arXiv:2610.07043`). Status `active`. Dual-active with TRACE.
- **Not This Task**: `method:quartet-ii` remains native FP4 hardware training; `method:cispo` / `method:sapo` remain the RL losses.
