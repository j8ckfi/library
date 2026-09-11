---
id: method:moe-data-repetition
type: method
title: "MoE Data-Repetition Overfit"
category: "architecture"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the frontier MoE architecture"
    reason: "Gotcha on repetition × sparsity, not DeepSeek-V4 / Kimi-K3"
    use_instead: "method:deepseek-v4"
  - when: "NVL72 megakernel / dispatch"
    reason: "Mixture-of-Kittens remains that systems default"
    use_instead: "method:mixture-of-kittens"
  - when: "~7B dense optimizer"
    reason: "Dense models tolerate more repeats; Muon2 is still the 7B optimizer"
    use_instead: "method:muon2"
assumptions:
  - "MoE pretrain with repeated data. Paper: 80M–1B active, up to 8.5B total. Not a 100B+ architecture bake-off."
  - "No official code as of 2026-09-11."
last_reviewed: "2026-09-11"
papers:
  - paper:moe-data-repetition
recipes:
  - recipe:moe-data-repetition
claims:
  - benchmark: "MoE vs dense LM pretrain under data repetition, 80M–1B active"
    metric: "repetition factor where degradation starts"
    value: "MoE ~4×; dense 80M ~8× with minimal damage; MoE underperforms dense by 32×"
    baseline: "all-unique tokens; dense Transformers at matched active params"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.11917"
    notes: "Effect scales with total (not active) params / sparsity. Dropout / masking can keep MoE ahead of dense past 64× but never matches unique data."
tags:
  - pretraining
  - moe
  - data-repetition
  - niche
---

# MoE Data-Repetition Overfit

## Method Overview
Niche gotcha: MoEs overfit repeated pretrain data faster than dense models. The damage tracks **total** parameters (sparsity), not active FLOPs. Routing freezes early; expert specialization correlates with memorizing repeats. Dropout and strong masking help; unique data still wins.

Not an architecture. DeepSeek-V4 / Kimi-K3 stay the MoE defaults.

## When to Use
- Planning unique-token budget vs repeats for a sparse pretrain. Prefer fewer repeats than the dense 8× folklore, or add masking-based regularization.

## When NOT to Use
- Architecture pick → `method:deepseek-v4` / `method:kimi-k3`. NVL72 kernel → `method:mixture-of-kittens`.

## Relation to Existing SOTA
- Niche note on `task:pretrain-moe-frontier` and `task:train-moe-nvl72`. Does **not** enter `current_sota`.

## Gotchas & Failure Modes
- 80M–8.5B study. Do not treat 4× as a frontier-100B law without a re-check.
- No code. Regularization is a mitigation, not a unique-data substitute.
