---
id: method:spod
type: method
title: 'SPOD'
category: distillation
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'same-tokenizer single-teacher matching distillation'
  reason: 'OPD remains matching; SPOD protects successful student choices against teacher erosion'
  use_instead: method:opd
- when: 'outcome-only long-horizon coverage with a checker'
  reason: 'CANOPY remains coverage first hop; SPOD is agentic OPD overshoot'
  use_instead: method:canopy
assumptions:
- 'Multi-turn agentic OPD. Paper: two model families, three agentic benches; ALFWorld Gemma E4B vs 31B teacher.'
- 'Code Jike338/SPOD as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:spod
recipes:
- recipe:spod
claims:
- benchmark: 'Two model families, three agentic benches; ALFWorld Gemma E4B vs 31B teacher'
  metric: 'final success vs ordinary OPD; peak vs teacher; overshoot-then-regression'
  value: 'up to +15.2 pp vs ordinary OPD; up to +20.0 vs teacher; ALFWorld 16.5→82.8 peak then 73.7 without SPOD'
  baseline: 'ordinary OPD and evaluated OPD variants'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.25034'
  notes: 'Mask conflicting teacher supervision on successful student choices. Does not replace OPD or CANOPY.'
tags:
- distillation
- opd
- agentic
- overshoot
- active
---

# SPOD

## Method Overview
SPOD (Success-Preserving On-Policy Distillation) treats agentic OPD overshoot: repair of weak student decisions initially outpaces erosion of successful student choices the teacher disfavors. Continued imitation then regresses. SPOD masks conflicting teacher tokens on protected successful choices.

## When to Use
- Multi-turn agentic OPD where the student peaks above the teacher then falls.

## When NOT to Use
Plain text matching distill → `method:opd`. Checker coverage → `method:canopy`.

## Relation to Existing SOTA
Active plug-in on `task:student-distillation` (`sota_for: []`). Does **not** replace OPD or CANOPY.

## Gotchas & Failure Modes
- Stopping at the overshoot peak is not enough; unprotected imitation still erodes.
- Teacher reliability predicts where gains are fragile.
