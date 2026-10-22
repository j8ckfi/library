---
id: method:teachback
type: method
title: 'TeachBack'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:privileged-teacher-opsd'
  reason: 'TeachBack is an active plug-in; method:vista remains the first hop'
  use_instead: method:vista
assumptions:
- 'Same-size teacher sees a reference solution. Pairwise preference at each rollout refresh. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:teachback
recipes:
- recipe:teachback
claims:
- benchmark: 'Mathematical and logical reasoning OPSD vs privileged-teacher baselines'
  metric: 'student accuracy vs OPSD / related baselines'
  value: 'consistently improves student performance over existing OPSD methods while keeping teacher accuracy comparable'
  baseline: 'privileged OPSD that injects a full reference solution'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29167'
  notes: 'Does not retarget method:vista.'
tags:
- opsd
- privileged-teacher
- active
---

# TeachBack

## Method Overview
TeachBack trains a shared policy as both privileged Teacher and problem-only Student. Forward preference uses teacher traces for the student; reversed preference uses student behavior to stop the teacher from collapsing into reference-conditioned shortcuts.

## When to Use
- Privileged OPSD where gold-conditioned teacher traces are accurate but omit exploration, verification, or self-correction the student needs.

## When NOT to Use
Gold-solution privileged first hop → `method:vista`. Matching distillation → `method:opd`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:vista`.

## Gotchas & Failure Modes
- No public code.
- Reference-suffix length and prompt style are part of the method, not optional wrappers.
