---
id: method:rpb
type: method
title: "Router Prior Bias (RPB)"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the MoE/VL RLVR loss"
    reason: "RPB is a router soft-anchor during post-train; SAPO remains the MoE/VL algorithm default"
    use_instead: "method:sapo"
  - when: "dense Pass@1 math/code RLVR"
    reason: "No MoE router to anchor; CISPO remains Pass@1"
    use_instead: "method:cispo"
  - when: "choosing the frontier MoE architecture"
    reason: "RPB does not retarget DeepSeek-V4 / Kimi-K3"
    use_instead: "method:deepseek-v4"
assumptions:
  - "Post-training an MoE whose pretrained router is already non-uniform. Paper: Moonlight-16B-A3B and Qwen3-30B-A3B-Base math post-train."
  - "Do not re-impose a uniformity load-balancing loss. Do not freeze the router as a hard assignment."
last_reviewed: "2026-09-09"
papers:
  - paper:rpb
recipes:
  - recipe:rpb
claims:
  - benchmark: "Moonlight-16B-A3B math post-training, in-domain accuracy"
    metric: "in-domain accuracy"
    value: 45.77
    baseline: "re-applied LBL 31.91 / unanchored fine-tuning 29.44"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08115"
    notes: "RPB also retains more OOD capability than LBL or unanchored FT. Active MoE post-train routing candidate; not a SAPO supersession."
  - benchmark: "Qwen3-30B-A3B-Base math post-training"
    metric: "ordering vs re-applied LBL"
    value: "RPB beats LBL (ordering reproduces)"
    baseline: "re-applied LBL"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08115"
    notes: "Anchor on weights, logits, or output distribution: no consistent ranking. Softness of the constraint is the effect."
tags:
  - post-training
  - moe
  - routing
  - rpb
  - active
---

# Router Prior Bias (RPB)

## Method Overview
RPB is **soft router anchoring** for MoE post-training. Read a prior from the frozen base router and add a training-time bias so live router logits stay near that prior while remaining trainable. Re-applying a pretrain load-balancing loss flattens inherited co-activation. Unanchored fine-tuning also loses. Hard-assigning the same prior keeps expert communities and still drops accuracy.

Active MoE post-train routing candidate beside SAPO. Does not replace SAPO, CISPO, DeepSeek-V4, or Kimi-K3.

## When to Use
- Post-training an MoE whose base router already has non-uniform expert co-activation (math SFT/RL on Moonlight- / Qwen3-class MoE).

## When NOT to Use
- MoE/VL RLVR algorithm → `method:sapo`. Dense Pass@1 → `method:cispo`. Architecture choice → `method:deepseek-v4`.

## Relation to Existing SOTA
- Active on `task:math-code-rl-moe`. Does **not** enter `current_sota`. SAPO stays the MoE/VL loss default.

## Gotchas & Failure Modes
- Claimed GitHub `naver-ai/rpb` was 404 at 2026-09-09 ingest.
- Do not treat expert-graph communities as the thing to optimize; they track the soft anchor, they are not the source.
- Uniformity LBL is the wrong post-train regularizer even if it was right at pretrain.
