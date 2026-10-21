---
id: method:d-pal
type: method
title: 'D-PAL'
category: architecture
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'diffusion-adapter lossless multi-token AR serving'
  reason: 'Uno remains first hop; D-PAL is an acceptance-weighted speculative-drafter loss'
  use_instead: method:uno
- when: 'trajectory consistency distillation for block-diffusion one-step drafting (DStill)'
  reason: 'DStill distills refinement trajectories; D-PAL changes the drafter objective to distribution overlap'
  use_instead: method:dstill
assumptions:
- 'Speculative decoding drafter train. Overlap (1-TV) acceptance signal; Rényi-1/2 preferred per-position loss.'
- 'Code Lucas-TY/D-PAL-SpecForge as of 2026-10-21. Paper: Qwen3-4B target, six benches.'
last_reviewed: '2026-10-21'
papers:
- paper:d-pal
recipes:
- recipe:d-pal
claims:
- benchmark: 'Six benches; Qwen3-4B target vs D-PACE; T=0 and T=1'
  metric: 'mean acceptance length and throughput vs D-PACE'
  value: 'mean acceptance length 4.50→4.57 (T=0) and 4.20→4.28 (T=1); higher throughput at both temperatures'
  baseline: 'D-PACE (point-mass target-token weights and CE)'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28355'
  notes: 'Does not retarget Uno or DStill.'
tags:
- speculative-decoding
- drafter-loss
- active
---

# D-PAL

## Method Overview
D-PAL (Dynamic Position-wise Acceptance Loss) trains a speculative drafter from the exact expected accepted length using draft-target overlap as the acceptance signal, with detached overlap weights and a Rényi-1/2 (or forward-KL) per-position loss instead of point-mass CE.

## When to Use
- Training a speculative drafter when D-PACE's point-mass target understates rejection-sampling overlap.

## When NOT to Use
AR+diffusion serving → `method:uno`. Block-diffusion one-step distill → `method:dstill`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:uno`.

## Gotchas & Failure Modes
- Not a serving architecture (Uno).
- Weights are detached; any per-position loss can plug in.
