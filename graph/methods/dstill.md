---
id: method:dstill
type: method
title: 'DStill'
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'diffusion-adapter lossless multi-token AR serving'
  reason: 'Uno remains first hop; DStill distills multi-step block-diffusion drafter refinement into one step'
  use_instead: method:uno
- when: 'causal self-recursion MTP without auxiliary heads (ECHO)'
  reason: 'ECHO is backbone MTP; DStill is block-diffusion drafter distillation'
  use_instead: method:echo-mtp
assumptions:
- 'Block-diffusion speculative decoding. Two-stage: partial-block completion then trajectory-consistency student.'
- 'No public code as of 2026-10-21. Paper: three model families vs one-step DFlash.'
last_reviewed: '2026-10-21'
papers:
- paper:dstill
recipes:
- recipe:dstill
claims:
- benchmark: 'Reasoning / math / code on three model families vs one-step DFlash and AR'
  metric: 'acceptance length and wall-clock speedup vs one-step DFlash / AR'
  value: 'up to +28% acceptance length and +25% speedup vs one-step DFlash; up to 6.45x vs AR decoding'
  baseline: 'one-step DFlash; autoregressive decoding'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.27379'
  notes: 'Does not retarget Uno or ECHO.'
tags:
- speculative-decoding
- block-diffusion
- distillation
- active
---

# DStill

## Method Overview
DStill distills a target-conditioned block-diffusion drafter's own multi-step refinement trajectories into a one-step student, using a curriculum from partial to fully masked blocks to cut factorization error without extra draft passes.

## When to Use
- Block-diffusion speculative decoding when one-step drafts are inconsistent and iterative refinement is too slow.

## When NOT to Use
AR+diffusion serving → `method:uno`. Backbone MTP → `method:echo-mtp`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:uno`.

## Gotchas & Failure Modes
- Not Uno (no AR diffusion adapters).
- Student still drafts; the target verifies.
