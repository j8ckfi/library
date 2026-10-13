---
id: method:replayssm
type: method
title: ReplaySSM
category: training-systems
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: linear-time architecture from scratch (SSM / Mamba)
  reason: Mamba-2 remains the linear-time sequence-model first hop; ReplaySSM is a
    serving cache
  use_instead: method:mamba-2
- when: input-heavy agentic / KV-compressed CED serving
  reason: DeepSeek-V4.1-Flash remains CED serving; ReplaySSM is hybrid SSM state replay
  use_instead: method:deepseek-v41-flash
assumptions:
- 'Hybrid SSM (Mamba-2 / Gated DeltaNet) serving in vLLM. Paper: batch 256 decode;
  120B-class vs spec decoding.'
- 'Code: Johnny-Liou/ReplaySSM (code_status: released).'
last_reviewed: '2026-10-13'
papers:
- paper:replayssm
recipes:
- recipe:replayssm
claims:
- benchmark: vLLM Mamba-2 / Gated DeltaNet decode, batch 256; 120B-class vs spec decoding
  metric: decode throughput multiplier
  value: 1.20–1.47× vs vLLM SSM cache; ~1.8× vs vLLM speculative decoding on 120B-class
  baseline: vLLM SSM state cache; vLLM speculative decoding
  date: '2026-10-13'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13778
  notes: RL rollout throughput is the library mention, not a CISPO bake-off. Does
    not retarget Mamba-2 or V4.1-Flash.
tags:
- systems
- ssm
- replayssm
- active
---

# ReplaySSM

## Method Overview
Do not cache the full SSM state. Keep a checkpoint and a short buffer of recent inputs, then replay to reconstruct state at decode.

## When to Use
- Hybrid SSM serving (Mamba-2 / Gated DeltaNet) where state cache memory bounds batch, including RL rollouts.

## When NOT to Use
Train a linear-time architecture from scratch → `method:mamba-2`. KV-compressed CED MoE serving → `method:deepseek-v41-flash`.

## Relation to Existing SOTA
Active plug-in on `task:linear-time-sequence-modeling` with a mention on `task:input-heavy-agentic-moe-serving` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace Mamba-2 or V4.1-Flash.

## Gotchas & Failure Modes
- **code: released** Johnny-Liou/ReplaySSM as of 2026-10-13.
- Replay compute trades against state memory; tiny batches may not win.
- Not a training-algorithm change for CISPO / Miles; it is rollout serving.
