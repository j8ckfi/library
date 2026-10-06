---
id: method:og-opsd
type: method
title: "OG-OPSD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing privileged-teacher OPSD"
    reason: "VISTA remains the privileged-teacher first hop; OG-OPSD is an outcome-gated divergence switch"
    use_instead: "method:vista"
  - when: "unlabeled / no-GT self-distillation"
    reason: "u-OPSD remains unlabeled; OG-OPSD uses binary outcome rewards"
    use_instead: "method:u-opsd"
  - when: "entropy overshoot without an outcome switch"
    reason: "E2-OPSD is the entropy-gap / exemplar fix; OG-OPSD switches FKL/RKL from outcome"
    use_instead: "method:e2-opsd"
assumptions:
  - "OPSD host with a binary outcome verifier. Paper: Qwen3 1.7B/4B/8B and Qwen3-VL-2B."
  - "No public code as of 2026-10-06 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:og-opsd
recipes:
  - recipe:og-opsd
claims:
  - benchmark: "Qwen3 1.7B/4B/8B and Qwen3-VL-2B math / multimodal / OOD vs vanilla OPSD"
    metric: "improvement vs vanilla OPSD (abstract; no numeric table)"
    value: "consistently improves vanilla OPSD and multiple baselines"
    baseline: "vanilla OPSD"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.05070"
    notes: "Does not retarget VISTA. Do not invent a numeric table."
tags:
  - post-training
  - distillation
  - og-opsd
  - active
---

# OG-OPSD

## Method Overview
OG-OPSD (Outcome-Guided OPSD) picks FKL vs RKL and a distillation prefix cutoff from binary outcome plus cumulative average teacher entropy, instead of a fixed divergence on every trajectory.

## When to Use
- Privileged OPSD with a verifier, where incorrect rollouts are under-penalized by a fixed KL.

## When NOT to Use
- Privileged default → `method:vista`. Unlabeled → `method:u-opsd`. Entropy overshoot / exemplars → `method:e2-opsd`.

## Relation to Existing SOTA
- Active plug-in on `task:privileged-teacher-opsd` beside `method:vista` / `method:u-opsd` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace VISTA.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06.
- Abstract has no numeric table; do not invent one.
