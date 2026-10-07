---
id: method:trace
type: method
title: "TRACE"
category: "quantization"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "native FP4 forward/backward hardware training from scratch"
    reason: "TRACE is RL train–rollout QAT; Quartet-II remains native FP4 pretrain"
    use_instead: "method:quartet-ii"
  - when: "direction-aware NVFP4 mismatch rebalance rather than rollout-guided QAT"
    reason: "TRIAGE is the complementary stabilizer; no head-to-head"
    use_instead: "method:triage"
  - when: "dense Pass@1 math/code RLVR loss"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "MoE LM RL with a separate rollout engine whose FP4 grid can disagree with train-side rounding. Paper: Qwen3.5-35B-A3B / 122B-A10B / Qwen3.8-Flash-Next / 2.4T-A95B."
  - "No official GitHub as of 2026-10-07."
last_reviewed: "2026-10-07"
papers:
  - paper:trace
recipes:
  - recipe:trace
claims:
  - benchmark: "FP4 RL of MoE LMs (Qwen3.5-35B-A3B / 122B-A10B / Qwen3.8-Flash-Next)"
    metric: "rollout speedup vs unaligned FP4 RL"
    value: "up to 5.4×"
    baseline: "unaligned train-side FP4 RL"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.07767"
    notes: "Caches rollout mantissa/scale. Dual-active with TRIAGE. Does not replace Quartet-II."
tags:
  - post-training
  - quantization
  - fp4
  - moe
  - trace
  - active
---

# TRACE

## Method Overview
Rollout-guided quantization-aware training for FP4 RL of MoE LMs. Align the train-side rounding grid to the rollout engine and cache mantissa/scale from the rollout side.

## When to Use
- FP4 / NVFP4 RL where train-side rounding disagrees with rollout-side quantization.

## When NOT to Use
- Native FP4 from scratch → `method:quartet-ii`. Segment-level direction rebalance → `method:triage`.

## Relation to Existing SOTA
- Dual-active first hop on `task:fp4-rl-train-rollout-alignment` (`sota_for: []`). No head-to-head vs TRIAGE. Does **not** replace Quartet-II.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-07.
- Do not treat 5.4× as a Quartet-II pretrain claim.
