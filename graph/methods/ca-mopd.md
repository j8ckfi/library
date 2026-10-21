---
id: method:ca-mopd
type: method
title: 'CA-MOPD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching; CA-MOPD is capability-gap multi-teacher allocation'
  use_instead: method:opd
- when: 'multi-teacher token-share / gap-aware budget (Open-MOPD default)'
  reason: 'Open-MOPD remains the library multi-teacher bake-off; paper Open-MOPD 32.22 is not the library 83.4%'
  use_instead: method:open-mopd
assumptions:
- 'Merge RL specialists then allocate distillation strength from verifier-estimated teacher-student capability gaps.'
- 'No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:ca-mopd
recipes:
- recipe:ca-mopd
claims:
- benchmark: 'Six math / code / IF benchmarks; naive MOPD / Open-MOPD / merged init'
  metric: 'average score vs naive MOPD / Open-MOPD / merged init'
  value: '32.22 vs naive MOPD 0.86 behind / Open-MOPD 0.83 / merged init 0.74'
  baseline: 'naive MOPD; Open-MOPD (paper numbers, not library 83.4% bake-off); merged specialist init'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.26950'
  notes: 'Paper Open-MOPD is not the library 83.4% bake-off. Does not retarget Open-MOPD or OPD.'
tags:
- distillation
- mopd
- multi-teacher
- active
---

# CA-MOPD

## Method Overview
CA-MOPD merges RL specialists into a student init, then scales domain distillation with verifier-estimated capability gaps so supervision shrinks as the student catches a teacher and grows if capability regresses.

## When to Use
- Multi-teacher OPD where discrepancy-based allocation over-supervises teachers the student already matches.

## When NOT to Use
Single-teacher matching → `method:opd`. Multi-teacher default → `method:open-mopd`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:opd`.

## Gotchas & Failure Modes
- Paper Open-MOPD numbers are not the library 83.4% bake-off.
- No public code.
