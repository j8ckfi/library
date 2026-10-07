---
id: method:triage
type: method
title: "TRIAGE"
category: "quantization"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "native FP4 forward/backward hardware training from scratch"
    reason: "TRIAGE is NVFP4 RL mismatch stabilization; Quartet-II remains native FP4 pretrain"
    use_instead: "method:quartet-ii"
  - when: "rollout-guided QAT that caches mantissa/scale, not direction-aware rebalance"
    reason: "TRACE is the complementary QAT path; no head-to-head"
    use_instead: "method:trace"
  - when: "dense Pass@1 math/code RLVR loss"
    reason: "CISPO remains Pass@1"
    use_instead: "method:cispo"
assumptions:
  - "Native NVFP4 RL. Paper: Qwen3-4B / 30B-A3B; >34500 GPU-h B300."
  - "No official GitHub as of 2026-10-07."
last_reviewed: "2026-10-07"
papers:
  - paper:triage
recipes:
  - recipe:triage
claims:
  - benchmark: "Native NVFP4 RL, Qwen3-4B / Qwen3-30B-A3B"
    metric: "rollout throughput vs BF16"
    value: "up to 2.3×"
    baseline: "BF16 rollout"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.07043"
    notes: "Segment-level diagnosis of amplifying negative-advantage/negative-gap updates. Dual-active with TRACE."
tags:
  - post-training
  - quantization
  - nvfp4
  - triage
  - active
---

# TRIAGE

## Method Overview
Direction-aware mismatch stabilization for native NVFP4 RL. Diagnose at segment level and rebalance updates that amplify negative-advantage / negative-gap directions.

## When to Use
- Native NVFP4 RL that diverges because mismatch and negative advantages compound.

## When NOT to Use
- Native FP4 from scratch → `method:quartet-ii`. Rollout-guided QAT cache → `method:trace`.

## Relation to Existing SOTA
- Dual-active first hop on `task:fp4-rl-train-rollout-alignment` (`sota_for: []`). No head-to-head vs TRACE. Does **not** replace Quartet-II.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-07.
- >34500 GPU-h B300 is the paper budget, not a library bake-off vs TRACE.
