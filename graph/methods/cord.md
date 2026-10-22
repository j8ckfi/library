---
id: method:cord
type: method
title: 'CORD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:student-distillation'
  reason: 'CORD is an active plug-in; method:opd remains the first hop'
  use_instead: method:opd
assumptions:
- 'Two-objective agent training. Closed-form nearest-point projection before optimizer transforms.'
last_reviewed: '2026-10-22'
papers:
- paper:cord
recipes:
- recipe:cord
claims:
- benchmark: 'ALFWorld / WebShop vs three joint RL+distill recipes'
  metric: 'success rate vs unprojected joint training'
  value: 'ALFWorld +1.5 to +15.9 pp across three recipes; WebShop SDAR 60.7% to 64.6% on two of three pairs'
  baseline: 'GRPO+OPSD / SDAR / Skill-SD without projection'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29965'
  notes: 'Does not retarget method:opd.'
tags:
- distillation
- agent-rl
- active
---

# CORD

## Method Overview
CORD combines RL and distillation gradients once per optimizer mini-batch, projecting away the component that fights a chosen protected objective when a gate fires.

## When to Use
- Joint RL + on-policy distillation where mixing weights still let the two gradients cancel.

## When NOT to Use
Matching-only distill → `method:opd`. Outcome-only agent RL without a teacher → `method:canopy`. OPD-then-RLVR stacking → `method:opd-then-rlvr`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:opd`.

## Gotchas & Failure Modes
- Protection direction and projection gate must be chosen together.
- Code LvAoAo/CORD-release.
