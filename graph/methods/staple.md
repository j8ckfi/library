---
id: method:staple
type: method
title: STAPLE
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: dense-to-MoE upcycling via learned binary-mask experts over a frozen FFN
  reason: MASKerade remains mask-expert upcycling; STAPLE adds residual token-indexed embeddings
  use_instead: method:maskerade
- when: choosing the frontier MoE architecture template
  reason: DeepSeek-V4 / Kimi-K3 remain that hop
  use_instead: method:deepseek-v4
assumptions:
- 'Pretrained dense checkpoint. Paper: OLMo-2 1B and 7B; host-offloaded embeddings with ~5% hottest on
  GPU.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:staple
recipes:
- recipe:staple
claims:
- benchmark: OLMo-2 1B continued training vs dense; vs STEM / Engram-style / MoE upcycling
  metric: HumanEval / MBPP / GSM8K / DROP lifts vs continued dense
  value: +4.27 HumanEval / +2.80 MBPP / +2.27 GSM8K / +1.65 DROP; 2× faster decode than the MoE-upcycle
    baseline with <½ GPU memory in the paper's throughput eval
  baseline: continued dense training; STEM; Engram-style; MoE upcycling
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.12599
  notes: Static sparse memory, not routed experts. Does not retarget MASKerade or V4/K3.
tags:
- pretraining
- sparsity
- upcycling
- staple
- active
---

# STAPLE

## Method Overview
Keep the dense FFN. Add a token-indexed embedding residual (STEM-style memory) that is mostly host-resident. Train the residual; do not destroy pretrained compute.

## When to Use
- You want extra parametric capacity on a dense checkpoint without routed experts or a sparse pretrain.

## When NOT to Use
Mask-expert MoE upcycle → `method:maskerade`. Frontier MoE from scratch → `method:deepseek-v4`.

## Relation to Existing SOTA
Active plug-in on `task:dense-to-moe-upcycling` beside `method:maskerade` (`sota_for: []`). Does **not** replace MASKerade or DeepSeek-V4 / Kimi-K3.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Not an MoE. Token-indexed embeddings, not experts.
- Host-offload is required once capacity is billions of extra parameters.
