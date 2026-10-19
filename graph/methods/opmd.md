---
id: method:opmd
type: method
title: 'OPMD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains output matching; OPMD transfers student-compatible intermediate computation'
  use_instead: method:opd
- when: 'distilling RL gains via representation residuals rather than logits'
  reason: 'RIDE extrapolates RL hidden-state residuals; OPMD builds a student-usable teacher mechanism'
  use_instead: method:ride
- when: 'representation-level (hidden-state) multi-teacher OPD'
  reason: 'Latent-MOPD is multi-teacher hidden-state matching; OPMD is mechanism compatibility'
  use_instead: method:latent-mopd
assumptions:
- 'HF Daily 2026-10-16 tail. Constructs a student-compatible teacher that maps teacher representations into states the student''s downstream computation can use, then internalizes them on-policy.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:opmd
recipes:
- recipe:opmd
claims:
- benchmark: 'Three teacher-student settings plus multi-teacher and cross-family SFT'
  metric: 'average accuracy among evaluated distillation baselines'
  value: 'highest average in all three teacher-student settings; generalizes to multi-teacher and cross-family SFT'
  baseline: 'output-space OPD / representation matching (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.14022'
  notes: 'Does not retarget OPD, RIDE, or Latent-MOPD. HF 10-16 tail.'
tags:
- distillation
- opd
- mechanism
- active
---

# OPMD

## Method Overview
OPMD first builds a student-compatible teacher that transforms teacher representations into intermediate states the student's downstream layers can use, then internalizes those states from on-policy trajectories.

## When to Use
- OPD when output supervision does not move the student's inner computation, and naive hidden-state matching is geometrically incompatible.

## When NOT to Use
Default matching → `method:opd`. Same-init residual → `method:ride`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD.

## Gotchas & Failure Modes
- Extra student-compatible teacher transform.
- Paper averages are not the library Open-MOPD 83.4% bake-off.
