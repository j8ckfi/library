---
id: method:drmoet
type: method
title: "DRMoET"
category: "architecture"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the frontier MoE architecture template"
    reason: "DRMoET is a drop-in load-balancing objective; DeepSeek-V4 / Kimi-K3 remain the template"
    use_instead: "method:deepseek-v4"
  - when: "dense-to-MoE upcycling of a frozen FFN"
    reason: "MASKerade owns mask-expert upcycling; DRMoET trains an already-sparse MoE"
    use_instead: "method:maskerade"
  - when: "MoE sparsity × data-repetition overfit"
    reason: "DRMoET is a DRO balancer, not the repetition gotcha"
    use_instead: "method:moe-data-repetition"
assumptions:
  - "Sparse MoE NTP. Paper: FLAME-MoE recipe at 746M and 10.3B / 67B tokens. NeurIPS 2026."
  - "Code: MAPS-research/DRMoET (`code_status: released`)."
last_reviewed: "2026-10-07"
papers:
  - paper:drmoet
recipes:
  - recipe:drmoet
claims:
  - benchmark: "FLAME-MoE 10.3B, 67B tokens, seven-task average"
    metric: "seven-task avg"
    value: 0.6767
    baseline: "FLAME 0.6625 / aux-loss-free 0.6431"
    date: "2026-10-07"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2610.07207"
    notes: "NeurIPS 2026. 4.3% lower excess loss under mid-k misrouting. Also 746M. Does not replace DeepSeek-V4 / Kimi-K3."
tags:
  - pretraining
  - moe
  - load-balancing
  - drmoet
  - active
---

# DRMoET

## Method Overview
Drop-in distributionally robust MoE training objective. Replaces brittle load-balancing with a DRO residual that is less sensitive to mid-k misrouting.

## When to Use
- Sparse MoE pretrain where standard load-balancing or aux-loss-free still overfits expert collapse under misrouting.

## When NOT to Use
- Architecture template → `method:deepseek-v4`. Dense-to-MoE upcycling → `method:maskerade`.

## Relation to Existing SOTA
- Active plug-in on `task:pretrain-moe-frontier` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace DeepSeek-V4 / Kimi-K3.

## Gotchas & Failure Modes
- **code: released** MAPS-research/DRMoET as of 2026-10-07.
- FLAME-MoE 10.3B is not a V4 / K3 architecture bake-off.
