---
id: method:e2-opsd
type: method
title: "E2-OPSD"
category: "distillation"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing privileged-teacher OPSD"
    reason: "VISTA remains the privileged-teacher first hop; E2-OPSD is an entropy-overshoot fix"
    use_instead: "method:vista"
  - when: "unlabeled / no-GT self-distillation"
    reason: "u-OPSD remains the unlabeled hop; E2-OPSD still uses solved neighbors"
    use_instead: "method:u-opsd"
  - when: "survey playbook for OPSD collapse levers"
    reason: "opsd-collapse-review is the vocabulary; E2-OPSD is a trainer"
    use_instead: "method:opsd-collapse-review"
assumptions:
  - "Privileged or gold-conditioned OPSD host. Paper: math plus OOD; no extra networks."
  - "No public code as of 2026-10-06 (`code_status: none`)."
last_reviewed: "2026-10-06"
papers:
  - paper:e2-opsd
recipes:
  - recipe:e2-opsd
claims:
  - benchmark: "math mean@16 vs vanilla OPSD"
    metric: "mean@16 lift"
    value: "up to +4.3 vs OPSD"
    baseline: "vanilla OPSD"
    date: "2026-10-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.05048"
    notes: "OOD vs base up to +4.9 mean@16 / +5.5 pass@8. Does not retarget VISTA."
tags:
  - post-training
  - distillation
  - e2-opsd
  - active
---

# E2-OPSD

## Method Overview
E2-OPSD fixes OPSD entropy overshoot: the teacher is conditioned on a retrieved solved neighbor instead of the current gold answer, and each token's KL direction/strength follows the student–teacher entropy gap.

## When to Use
- Privileged OPSD where student entropy climbs past the teacher and stays there.

## When NOT to Use
- Privileged-teacher default → `method:vista`. Unlabeled consensus → `method:u-opsd`. Survey playbook → `method:opsd-collapse-review`.

## Relation to Existing SOTA
- Active plug-in on `task:privileged-teacher-opsd` beside `method:vista` / `method:u-opsd`, linked from `method:opsd-collapse-review` (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace VISTA.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-06.
- Exemplars are neighboring solved problems, not the current gold answer.
