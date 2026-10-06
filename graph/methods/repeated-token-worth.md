---
id: method:repeated-token-worth
type: method
title: "Repeated-Token Worth"
category: "data-curriculum"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "open multi-trillion-token web / Dolma mix with unique data not binding"
    reason: "OLMo-3 remains the open mix; this card is unique-data-constrained epoch geometry"
    use_instead: "method:olmo-3"
  - when: "MoE sparsity x data-repetition overfit"
    reason: "MoE data-repetition is a sparsity gotcha; this card is dense multi-epoch pricing"
    use_instead: "method:moe-data-repetition"
  - when: "selecting a shortlist of repetition counts across model scales on mixed target/generic data"
    reason: "That is repetition-count-selection on the same task"
    use_instead: "method:repetition-count-selection"
assumptions:
  - Unique pretrain data, not compute, is the binding constraint.
  - "Paper: pricing vs one epoch on the same data and vs fresh data at equal compute."
  - "No public code as of 2026-10-06 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:repeated-token-worth
recipes:
  - recipe:repeated-token-worth
claims:
  - benchmark: "multi-epoch pretrain, unique data fixed"
    metric: "epochs at which a repeated token is half as valuable as a fresh token; size trend at fixed U"
    value: "second epoch nearly as valuable as fresh; half-value at a critical epoch; ~15 epochs at 127M to ~4 at 2B"
    baseline: "one epoch on the same data / fresh data at equal compute"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.05591"
    notes: "Dual-active with repetition-count-selection. Does not retarget OLMo-3."
tags:
  - pretraining
  - data-curriculum
  - repeated-token-worth
  - active
---

# Repeated-Token Worth

## Method Overview
Prices repeated tokens against one epoch on the same data and against fresh data at equal compute. Cost follows extra epochs divided by unique tokens per parameter. With unique data fixed, compute-optimal runs grow model size and epochs together until a critical epoch; larger models then take fewer epochs (~15 at 127M to ~4 at 2B).

## When to Use
- Unique pretrain tokens are the bottleneck and you need an epoch / replay schedule, not a new mix recipe.

## When NOT to Use
- Open unique-data mix → `method:olmo-3`. MoE sparsity × repeats → `method:moe-data-repetition`. Scale-dependent repetition-count shortlists → `method:repetition-count-selection`.

## Relation to Existing SOTA
- Dual-active first hop on `task:data-constrained-pretrain` with `method:repetition-count-selection`. Method `sota_for` stays empty. Does **not** replace OLMo-3, Muon2, or MoE data-repetition.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06.
- Consecutive shard replay is not the same as shuffled repeats (up to +0.46 bits/byte).
- Size trend reverses if unique data grow with the model.
