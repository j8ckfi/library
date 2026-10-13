---
id: method:elr
type: method
title: ELR (Elastic Latent Recurrence)
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: Huginn-style dense fixed-point looping with terminal KV sharing
  reason: ELR is mixed-depth elastic recurrence, not Huginn depth-prior looping
  use_instead: method:looped-models-done-right
- when: compute-matched MoE looping of middle layers (FLOPs/params/KV matched)
  reason: SMELT loops MoE layers under a matched budget; ELR varies loop count at
    train and decode
  use_instead: method:smelt
- when: experimental CED all-token recurrence with no measured results
  reason: RLT remains the CED-recurrence experimental hop
  use_instead: method:recurrent-looped-transformer
assumptions:
- Looped LM (dense 4B or MoE 30B-A3B in the paper). Mixed loop counts per optimizer
  update. Can convert a pretrained unlooped checkpoint late.
- No public code as of 2026-10-13.
last_reviewed: '2026-10-13'
papers:
- paper:elr
recipes:
- recipe:elr
claims:
- benchmark: 4B dense / 30B-A3B MoE, 10-task avg vs matched unlooped baseline
  metric: score delta at 1 loop / 4 loops
  value: 4B −0.52 / +7.25; 30B-A3B +1.04 / +4.75
  baseline: matched-FLOPs unlooped baseline; Huginn-style / SMELT looping not the
    paper bake-off
  date: '2026-10-13'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.12582
  notes: Koi-4B AAII ~18 at 1 loop (Qwen3.5-4B class), 29 at 4 loops. Does not retarget
    SMELT or Looped Models Done Right.
tags:
- pretraining
- looped-lm
- elr
- active
---

# ELR (Elastic Latent Recurrence)

## Method Overview
One shared looped block with a gated state update and a learned step size. Each optimizer step mixes several loop counts. Loop index and remaining budget condition the block. Decode can pick 1–K loops. MoE reuses the first-loop router; KV is last-loop-only.

## When to Use
- Train or convert a looped LM that must serve several depths from one checkpoint, including a late mixed-depth conversion.

## When NOT to Use
Huginn-style fixed-point looping → `method:looped-models-done-right`. Compute-matched MoE layer looping → `method:smelt`. CED all-token recurrence → `method:recurrent-looped-transformer`.

## Relation to Existing SOTA
Active first hop on `task:elastic-depth-looped-lm` (`sota_for: []`). Does **not** replace Looped Models Done Right or SMELT.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-13.
- One-loop 4B dense is slightly below the matched unlooped baseline (−0.52). Gains appear at higher loop counts.
- First-loop MoE route reuse is a speed trick, not a quality claim versus SMELT.
