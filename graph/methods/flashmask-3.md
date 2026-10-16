---
id: method:flashmask-3
type: method
title: 'FlashMask-3'
category: training-systems
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'choosing the ~7B dense pretrain optimizer'
  reason: 'Muon2 remains the optimizer; FlashMask-3 is a mask-aware attention kernel'
  use_instead: method:muon2
- when: 'post-train gated sparse attention under a fixed budget'
  reason: 'SAS is post-train sparsification, not a distributed kernel'
  use_instead: method:sas
assumptions:
- 'Long-context training with structured masks and context parallelism on Hopper.'
- 'Code: PaddlePaddle/FlashMask (code_status: released).'
last_reviewed: '2026-10-16'
papers:
- paper:flashmask-3
recipes:
- recipe:flashmask-3
claims:
- benchmark: 'H100 12 masks 4K-128K; CP 4-32; 118B-A14B MoE 128K on 128 H100'
  metric: 'achieved TFLOPs; CP throughput; e2e tokens/s'
  value: '+45-141% TFLOPs vs FlashMask; CP 1.80-3.71x vs Megatron ring; e2e +7.3-11.0%'
  baseline: 'FlashMask / FlexAttention / MagiAttention / Megatron-Core CP (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.17901'
  notes: 'Does not retarget Muon2. Systems plug-in for mask-aware attention.'
tags:
- training-systems
- attention
- active
---

# FlashMask-3

## Method Overview
Keep FlashMask's O(n) column-wise mask. Localize per rank with clip-shift-max (no mask all-gather). Run a Hopper warp-specialized kernel and prune communication from the mask.

## When to Use
- Long-context pretrain/FT with document / prefix-LM / sliding-window / block-sparse masks on Hopper CP.

## When NOT to Use
~7B optimizer choice → `method:muon2`. Post-train gated sparse attention → `method:sas`.

## Relation to Existing SOTA
Active plug-in on `task:llm-pretraining-optimization` (`sota_for: []`). Does **not** replace Muon2.

## Gotchas & Failure Modes
- Hopper-oriented; Ampere FlashMask is the prior kernel.

