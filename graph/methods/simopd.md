---
id: method:simopd
type: method
title: 'SimOPD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains token matching; SimOPD matches teacher similarity distributions'
  use_instead: method:opd
- when: 'distilling RL gains via representation residuals rather than logits'
  reason: 'RIDE extrapolates hidden-state residuals; SimOPD is relational similarity'
  use_instead: method:ride
assumptions:
- 'Paired memory banks of student-generated responses. Same- and cross-architecture teacher-student.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:simopd
recipes:
- recipe:simopd
claims:
- benchmark: 'Same- and cross-architecture OPD vs strongest paper baselines'
  metric: 'overall average'
  value: '+2.6 same-arch / +3.1 cross-arch vs strongest baselines'
  baseline: 'strongest paper OPD/hidden-state baselines (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.23306'
  notes: 'Does not retarget OPD or RIDE. Avoids cross-model projection.'
tags:
- distillation
- opd
- similarity
- active
---

# SimOPD

## Method Overview
SimOPD stores student-generated responses in paired memory banks, reads teacher internal representations as similarity distributions, and matches those distributions in the student's own representation space.

## When to Use
- OPD when token probabilities underuse teacher internals and hidden-state matching would force a feature-space shift, including cross-architecture pairs.

## When NOT to Use
Default matching → `method:opd`. Same-init residual extrapolation → `method:ride`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD.

## Gotchas & Failure Modes
- Needs a response memory bank.
- Not a library OPD bake-off.
