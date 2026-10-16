---
id: method:training-free-opd
type: method
title: 'Training-Free On-Policy Distillation'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains gradient matching; this is forward-only fusion of same-base specialists'
  use_instead: method:opd
- when: 'relative policy-difference transfer of OPD (expert-minus-reference log-ratio residuals)'
  reason: 'RPD-OPD is residual transfer, not least-squares fusion'
  use_instead: method:rpd-opd
- when: 'privileged same-size gold teacher OPSD'
  reason: 'VISTA remains scoring-teacher OPSD'
  use_instead: method:vista
assumptions:
- 'Specialists that share a base checkpoint and linear layers. Paper: Olmo 3 7B math and code specialists.'
- 'Code: none found as of 2026-10-16.'
last_reviewed: '2026-10-16'
papers:
- paper:training-free-opd
recipes:
- recipe:training-free-opd
claims:
- benchmark: 'Olmo 3 7B seven math/code benches; AIME25 vs task arithmetic'
  metric: 'specialist-gain retention; AIME25 vs task arithmetic after dropping looped answers'
  value: 'forward-only fusion keeps most specialist gains; dropping repetition-loop answers lifts AIME25 from task-arithmetic to specialist level'
  baseline: 'task arithmetic; gradient OPD (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22236'
  notes: 'Does not retarget OPD. No public code as of 2026-10-16.'
tags:
- distillation
- opd
- merge
- active
---

# Training-Free On-Policy Distillation

## Method Overview
For same-base specialists, each fused linear layer must reproduce every specialist's outputs on that specialist's inputs. Solve least squares from second moments collected by one forward pass over a few hundred on-policy rollouts. Drop repetition-loop answers before collecting moments.

## When to Use
- Merging same-base math/code specialists without a distillation trainer.

## When NOT to Use
Gradient matching → `method:opd`. Residual Δπ transfer → `method:rpd-opd`. Privileged gold teacher → `method:vista`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD.

## Gotchas & Failure Modes
- Same-base linear layers only.
- A few looped answers can dominate token mass; filter them.

