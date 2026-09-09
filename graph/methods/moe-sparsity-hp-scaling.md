---
id: method:moe-sparsity-hp-scaling
type: method
title: "MoE Sparsity Hyperparameter Scaling"
category: "architecture"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the frontier MoE architecture"
    reason: "HP transfer laws, not DeepSeek-V4 / Kimi-K3"
    use_instead: "method:deepseek-v4"
  - when: "choosing the ~7B dense optimizer"
    reason: "Muon2 remains the dense default; this is MoE sparsity HPs"
    use_instead: "method:muon2"
  - when: "overtraining-axis optimizer memory / LR / WD for dense models"
    reason: "That is optimizer-memory-schedules"
    use_instead: "method:optimizer-memory-schedules"
assumptions:
  - "MoE pretrain. Paper: up to 6B non-embedding, held-out 12B 1/64. Not a 100B+ architecture bake-off."
last_reviewed: "2026-09-09"
papers:
  - paper:moe-sparsity-hp-scaling
recipes:
  - recipe:moe-sparsity-hp-scaling
claims:
  - benchmark: "1,800 MoE pretrain runs, held-out 12B total 1/64 activated"
    metric: "predicted vs observed optimal LR / batch"
    value: "predicted HPs remain close to observed optima; A is a multiplicative power-law factor"
    baseline: "param-count-only HP laws; conflicting prior LR/batch advice"
    date: "2026-09-09"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.08690"
    notes: "~20T tokens, 200k H800-hours. Does not retarget DeepSeek-V4 / Kimi-K3."
tags:
  - pretraining
  - moe
  - hyperparameters
  - moe-sparsity-hp-scaling
  - active
---

# MoE Sparsity Hyperparameter Scaling

## Method Overview
Unified LR/batch scaling laws that include activation ratio A. At fixed sparsity, B* ~ D^α and η* ~ C^β; across sparsity, A is a multiplicative factor. Active pretrain guidance. Does not replace DeepSeek-V4 / Kimi-K3 or Muon2.

## When to Use
- Transferring LR/batch across MoE sparsity, including ultra-sparse (1/64) models.

## When NOT to Use
- Architecture default → `method:deepseek-v4` / `method:kimi-k3`. Dense optimizer → `method:muon2`.

## Relation to Existing SOTA
- Active on `task:pretrain-moe-frontier`. Does **not** enter `current_sota`.

## Gotchas & Failure Modes
- Paper scale is 6B (held-out 12B), not frontier 100B+. Treat as HP transfer, not an architecture win.
