---
id: method:adampm
type: method
title: 'AdamPM'
category: optimizer
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'full-param memory-efficient pretrain via subspace projections'
  reason: 'SCALE remains first hop; AdamPM pools Adam second-moment entries'
  use_instead: method:scale
- when: 'choosing the ~7B dense pretrain optimizer'
  reason: 'Muon2 remains the 7B default'
  use_instead: method:muon2
assumptions:
- 'Adam-compatible; pool adjacent second-moment entries along row or column. Paper: LLaMA pretrain, GLUE FT, multimodal.'
- 'Code jixiaowei95/AdamPM as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:adampm
recipes:
- recipe:adampm
claims:
- benchmark: 'LLaMA pretrain / GLUE FT / multimodal; second-moment memory'
  metric: 'second-moment memory vs Adam; matched quality and step time'
  value: 'second-moment memory 1/s of Adam at group size s; paper: matched quality and speed'
  baseline: 'Adam / AdamW'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.24598'
  notes: 'Second-moment pooling is the effective design. No SCALE bake-off. Does not replace SCALE or Muon2.'
tags:
- optimizer
- memory-efficient
- adam
- active
---

# AdamPM

## Method Overview
AdamPM groups adjacent Adam second-moment entries along a row or column and stores one shared mean per group. First-moment pooling is not the recommended design. Hyperparameters transfer from Adam.

## When to Use
- AdamW pretrain or FT where optimizer-state memory is the constraint and a drop-in Adam change is preferred to a subspace optimizer.

## When NOT to Use
SCALE subspace first hop → `method:scale`. ~7B default → `method:muon2`.

## Relation to Existing SOTA
Active plug-in on `task:full-param-memory-efficient-pretrain` (`sota_for: []`). Does **not** replace SCALE or Muon2.

## Gotchas & Failure Modes
- Group size s is the memory knob.
- No SCALE bake-off.
