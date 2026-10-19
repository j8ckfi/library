---
id: method:looped-models-done-right
type: method
title: "Looped Models Done Right"
category: "architecture"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "compute-matched MoE looping of middle layers (FLOPs/params/KV matched)"
    reason: "SMELT loops MoE layers; this card is Huginn-style dense fixed-point looping"
    use_instead: "method:smelt"
  - when: "experimental CED all-token recurrence with no measured results"
    reason: "RLT remains the CED-recurrence experimental first hop; this card has 100M–1.6B measurements on Huginn-style loops"
    use_instead: "method:recurrent-looped-transformer"
  - when: "standard dense ~7B NTP from scratch"
    reason: "Muon2 remains the 7B optimizer; this is a looped architecture recipe"
    use_instead: "method:muon2"
  - when: "elastic mixed-depth looped LM (gated state update / mixed loop counts)"
    reason: "This card is Huginn-style dense fixed-point looping; ELR trains one weight set under mixed loop counts"
    use_instead: "method:elr"
assumptions:
  - Huginn-style fixed-point looped LM (shared recurrent block), 100M–1.6B in the paper. Not SMELT MoE layer looping and not RLT CED.
  - "Code: ifm-ai/xllm-loop (`code_status: released`)."
last_reviewed: '2026-10-19'
papers:
  - paper:looped-models-done-right-i
  - paper:looped-models-done-right
recipes:
  - recipe:looped-models-done-right
claims:
  - benchmark: "730M Huginn vs Ouro; 8BA0.8B MoE / 500B tokens (Part I)"
    metric: "ten-bench win; MoE knowledge/reasoning/coding"
    value: "730M/336B tokens Huginn beats Ouro on all ten benches; 8BA0.8B/500B Huginn beats Ouro on nearly all benches; 75% fewer resident params than 112-layer FF MoE at matched FLOPs"
    baseline: "Ouro / 112-layer feedforward MoE (single-paper)"
    date: "2026-10-19"
    verified: true
    evidence_level: preprint
    source_url: "https://arxiv.org/abs/2610.23036"
    notes: "Part I of the same Huginn-style card. Does not retarget RLT or SMELT."
  - benchmark: "1.6B looped LM downstream average, 3x smaller KV vs fixed-depth full cache"
    metric: "downstream average at matched quality"
    value: "3x smaller KV matches fixed-depth full-cache average"
    baseline: "fixed-depth training with the full KV cache / Huginn depth prior"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.06833"
    notes: "Does not retarget RLT (no measurements) or SMELT (MoE loop). Distilled prefill up to 1.79x; RL saved-state grads 2x."
tags:
  - pretraining
  - architecture
  - looped-models-done-right
  - active
---

# Looped Models Done Right

## Method Overview
Trains Huginn-style looped LMs toward fixed points: a learned depth prior plus orthogonal input injection. Near fixed points, truncated BPTT, terminal KV sharing, distilled prefill, and RL from saved rollout states get cheaper without a new decoder family.

## When to Use
- Dense looped / Huginn-style recurrence where you want measured KV sharing and cheaper RL, not a CED sketch and not SMELT MoE looping.

## When NOT to Use
- CED all-token recurrence experimental hop → `method:recurrent-looped-transformer`. Compute-matched MoE looping → `method:smelt`. Dense 7B NTP optimizer → `method:muon2`.

## Relation to Existing SOTA
- Active plug-in on `task:recurrent-encoder-decoder-lm` beside `method:recurrent-looped-transformer` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace RLT or SMELT.

## Gotchas & Failure Modes
- **code: released** `https://github.com/ifm-ai/xllm-loop` as of 2026-10-06.
- Part I (`paper:looped-models-done-right-i`, 2610.23036) isolates topology/injection/state and transfers Huginn-style to 8BA0.8B MoE. Part II remains the fixed-point cheap-path card. Same code ifm-ai/xllm-loop.
- Do not cite RLT's empty measurement card as this paper's 1.6B numbers.
