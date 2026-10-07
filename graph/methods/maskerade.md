---
id: method:maskerade
type: method
title: "MASKerade"
category: "architecture"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the frontier MoE architecture template"
    reason: "MASKerade upcycles a dense FFN; DeepSeek-V4 / Kimi-K3 remain the sparse-from-scratch template"
    use_instead: "method:deepseek-v4"
  - when: "distributionally robust MoE load-balancing on an already-sparse model"
    reason: "DRMoET is a DRO objective; MASKerade learns mask experts over a frozen FFN"
    use_instead: "method:drmoet"
assumptions:
  - "A trained dense FFN. Paper: four 2:4 binary-mask experts, top-2 routing, frozen parent FFN."
  - "Code: Ming-K9/MASKerade (`code_status: released`)."
last_reviewed: "2026-10-07"
papers:
  - paper:maskerade
recipes:
  - recipe:maskerade
claims:
  - benchmark: "Dense FFN upcycled to four 2:4 mask experts, top-2"
    metric: "upcycled MoE vs dense parent / from-scratch MoE"
    value: "learned binary-mask experts over a frozen FFN"
    baseline: "dense parent; trained-from-scratch MoE"
    date: "2026-10-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.07809"
    notes: "Does not replace DeepSeek-V4 / Kimi-K3."
tags:
  - pretraining
  - moe
  - upcycling
  - maskerade
  - active
---

# MASKerade

## Method Overview
Dense-to-MoE upcycling via learned binary-mask experts over a frozen FFN. The paper's example is four 2:4 experts with top-2 routing.

## When to Use
- A dense checkpoint exists and a sparse-from-scratch run is too expensive.

## When NOT to Use
- Frontier MoE template → `method:deepseek-v4`. DRO load-balancing → `method:drmoet`.

## Relation to Existing SOTA
- Active first hop on `task:dense-to-moe-upcycling` (`sota_for: []`). Does **not** replace DeepSeek-V4 / Kimi-K3.

## Gotchas & Failure Modes
- **code: released** Ming-K9/MASKerade as of 2026-10-07.
- Frozen FFN is the contract; do not unfreeze the parent without a new bake-off.
