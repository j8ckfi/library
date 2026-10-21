---
id: method:r2s
type: method
title: 'R2S'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching; R2S repairs a myopic teacher scorer before agentic OPD'
  use_instead: method:opd
- when: 'success-preserving agentic OPD overshoot (SPOD)'
  reason: 'SPOD masks teacher conflict on successes; R2S fine-tunes the teacher scorer from takeovers'
  use_instead: method:spod
- when: 'outcome-only long-horizon coverage with a checker'
  reason: 'CANOPY remains coverage; R2S is reward-free teacher repair then OPD'
  use_instead: method:canopy
assumptions:
- 'Agentic OPD. Repair mines high-disagreement states, runs teacher takeovers, fine-tunes the teacher to takeover-informed scores, then freezes it for OPD.'
- 'No public GitHub as of 2026-10-21; project page tree-shu-zhao.github.io/r2s.'
last_reviewed: '2026-10-21'
papers:
- paper:r2s
recipes:
- recipe:r2s
claims:
- benchmark: 'Three environments, two teachers, four students (12 cells)'
  metric: 'success vs strongest of three agentic-OPD methods per cell'
  value: '+12.8 success points on average over the best competing agentic-OPD method in each cell; wins all 12 cells'
  baseline: 'three SOTA agentic-OPD methods'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28586'
  notes: 'Teacher takeovers from divergence states still finish the task; next-token scores do not. Reward-free repair. Does not retarget OPD or CANOPY.'
tags:
- distillation
- opd
- agentic
- teacher-repair
- active
---

# R2S

## Method Overview
Rollout-to-Scorer Distillation (R2S) treats agentic OPD failure as a myopic scorer: the teacher can finish from student-divergence states, but token scores let delaying moves through. R2S fine-tunes the teacher on takeover-informed scores, then runs ordinary OPD with that frozen scorer.

## When to Use
- Agentic OPD where the teacher can take over successfully but the student still times out under token scores.

## When NOT to Use
Text matching → `method:opd`. Success-preserving overshoot → `method:spod`. Checker coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:opd`.

## Gotchas & Failure Modes
- Repair uses consensus or an LLM judge, not a task reward.
- Compounding-error curricula do not fix the rollout-scorer gap.
