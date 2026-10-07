---
id: task:dense-to-moe-upcycling
type: task
title: "Dense-to-MoE Upcycling"
domain: "pretraining"
summary: "Turn a trained dense FFN into a routed Mixture-of-Experts without training a sparse model from scratch."
scope: "Dense-to-MoE upcycling of an existing dense checkpoint. First hop is MASKerade: learned binary-mask experts over a frozen FFN. Not the frontier MoE pretrain template, not MoE RLVR, not communication-efficient expert layout."
out_of_scope:
  - "Frontier MoE architecture from scratch (DeepSeek-V4 / Kimi-K3)"
  - "MoE/VL RLVR loss (SAPO)"
  - "Communication-efficient expert layout (CE-MoE)"
  - "Compute-matched looped MoE (SMELT)"
redirects:
  - when: "choosing the frontier MoE architecture template rather than upcycling a dense FFN"
    to: "task:pretrain-moe-frontier"
  - when: "MoE/VL RLVR loss rather than dense-to-MoE conversion"
    to: "task:math-code-rl-moe"
  - when: "communication-efficient expert layout rather than mask-expert upcycling"
    to: "method:ce-moe"
current_sota:
  - method: method:maskerade
    as_of: "2026-10-07"
    benchmark: "dense FFN upcycled to four 2:4 mask experts, top-2 routing"
    metric: "upcycled MoE quality vs dense and vs trained-from-scratch MoE"
    value: "learned binary-mask experts over a frozen FFN (four 2:4 experts, top-2)"
    notes: "MASKerade (2610.07809). Method status active. Does not replace DeepSeek-V4 / Kimi-K3."
methods:
  - method:maskerade
  - method:deepseek-v4
  - method:kimi-k3
  - method:ce-moe
  - method:drmoet
last_reviewed: "2026-10-07"
tags:
  - pretraining
  - moe
  - upcycling
  - sparsity
---

# Dense-to-MoE Upcycling

## Problem Definition
A dense FFN already encodes useful computation. Sparse pretrain from scratch discards it. This task owns **routing learned binary masks over a frozen dense FFN** to obtain an MoE without a full sparse run.

This is **not** the V4 / K3 architecture template.

## Evaluation Protocol
- **Primary Benchmarks**: upcycled MoE vs the dense parent and vs a trained-from-scratch MoE at matched active parameters (paper: four 2:4 experts, top-2).
- **Evaluation Pitfalls**: Do not treat mask experts as CE-MoE layout or as SAPO.

## SOTA Recommendation (as of 2026-10-07)
- **Primary (this task only)**: **MASKerade** (`method:maskerade`, `paper:maskerade` `arXiv:2610.07809`). Status `active`. Listed here as first hop; method `sota_for` stays empty. Code Ming-K9/MASKerade.
- **Not This Task**: `method:deepseek-v4` / `method:kimi-k3` remain the frontier MoE pretrain co-default.
