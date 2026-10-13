---
id: task:elastic-depth-looped-lm
type: task
title: Elastic-Depth Looped Language Models
domain: pretraining
summary: Train one looped LM whose decode-time loop count can vary, using mixed loop
  counts during optimization rather than a single fixed recurrence depth.
scope: Elastic / mixed-depth looped LM training (gated state update, mixed loop counts
  per optimizer step, loop-index/budget conditioning, late mixed-depth conversion).
  First hop is ELR. Not Huginn-style fixed-point looping, not compute-matched MoE
  layer looping, not CED all-token recurrence.
out_of_scope:
- Huginn-style dense fixed-point looped LMs (Looped Models Done Right)
- Compute-matched MoE looping of middle layers (SMELT)
- Recurrent CED all-token recurrence (RLT)
- Standard dense ~7B NTP optimizer (Muon2)
redirects:
- when: Huginn-style dense fixed-point looped LMs (learned depth prior / terminal
    KV sharing)
  to: method:looped-models-done-right
- when: compute-matched MoE looping of middle layers (FLOPs/params/KV matched)
  to: task:compute-matched-moe-looped-pretrain
- when: experimental CED all-token recurrence, not mixed-depth looping
  to: task:recurrent-encoder-decoder-lm
- when: standard dense ~7B NTP from scratch
  to: task:pretrain-dense-7b
current_sota:
- method: method:elr
  as_of: '2026-10-13'
  benchmark: 4B dense / 30B-A3B MoE 10-task avg vs matched unlooped baseline
  metric: score delta at 1 loop / 4 loops
  value: 4B −0.52 / +7.25; 30B-A3B +1.04 / +4.75
  notes: ELR (2610.12582). Method status active. Listed here as first hop; method
    sota_for stays empty. Does not replace Looped Models Done Right or SMELT.
methods:
- method:elr
- method:looped-models-done-right
- method:smelt
- method:recurrent-looped-transformer
last_reviewed: '2026-10-13'
tags:
- pretraining
- looped-lm
- elr
- elastic-depth
---

# Elastic-Depth Looped Language Models

## Problem Definition
A looped LM is usually trained at one recurrence depth. This task owns **one weight set that is trained under mixed loop counts** so decode can pick 1–K loops, including a late conversion of an unlooped checkpoint.

This is **not** Huginn-style fixed-point looping and not SMELT's compute-matched MoE layer looping.

## Evaluation Protocol
- **Primary Benchmarks**: 10-task avg vs a matched unlooped baseline at 1 loop and at 4 loops (paper: 4B dense, 30B-A3B MoE); optional AAII (Koi-4B).
- **Evaluation Pitfalls**: Do not cite SMELT FLOP-savings or Huginn KV-sharing as ELR results. One-loop 4B dense can sit slightly below the unlooped baseline.

## SOTA Recommendation (as of 2026-10-13)
- **Primary (this task only)**: **ELR** (`method:elr`, `paper:elr` `arXiv:2610.12582`). Status `active`. Listed here as first hop; method `sota_for` stays empty. No public code.
- **Not This Task**: `method:looped-models-done-right` remains Huginn-style dense looping; `method:smelt` remains compute-matched MoE looping; `method:recurrent-looped-transformer` remains experimental CED.
