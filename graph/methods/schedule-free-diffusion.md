---
id: method:schedule-free-diffusion
type: method
title: 'Schedule-Free Diffusion'
category: diffusion
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'pixel-space DiT / flow-matching image pretrain (Representation Guidance)'
  reason: 'RG remains pixel DiT first hop; this card is the optimizer/EMA schedule'
  use_instead: method:representation-guidance
- when: 'aligning text-to-image diffusion or flow models with rewards'
  reason: 'DiffusionOPSD / Self-OPD remain reward alignment; Schedule-Free transfers to ReFL/DMD'
  use_instead: method:diffusion-opsd
assumptions:
- 'Large diffusion pretrain with constant LR+EMA as the usual baseline. Theory: averaging a constant-step trajectory has a stationarity limit; LR decay and Schedule-Free do not.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:schedule-free-diffusion
recipes:
- recipe:schedule-free-diffusion
claims:
- benchmark: 'Large diffusion pretrain plus ReFL and generator-side DMD'
  metric: 'fixed-evaluation objective / generation quality vs constant-LR EMA'
  value: 'Schedule-Free beats constant-LR EMA across stages; LR decay+EMA is complementary but aggressive decay+EMA weakens continued optimization'
  baseline: 'constant LR + EMA (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22945'
  notes: 'Does not retarget Representation Guidance or DiffusionOPSD. Stronger stabilization is not always better.'
tags:
- diffusion
- optimizer
- ema
- active
---

# Schedule-Free Diffusion

## Method Overview
Schedule-Free (and LR decay) replace or complement EMA on large diffusion models: averaging a constant-step trajectory has an inherent optimization limit, while Schedule-Free reduces parameter variability without freezing late-stage progress.

## When to Use
- Large diffusion pretrain (and ReFL / generator-side DMD) still running constant LR + EMA.

## When NOT to Use
Pixel DiT architecture first hop → `method:representation-guidance`. Reward alignment → `method:diffusion-opsd`.

## Relation to Existing SOTA
Active plug-in on `task:pixel-diffusion-pretrain` with a mention on `task:posttrain-diffusion` (`sota_for: []`). Does **not** replace Representation Guidance or DiffusionOPSD.

## Gotchas & Failure Modes
- Lowest checkpoint variability (aggressive decay+EMA) can hurt continued optimization.
- Not an ImageNet FID bake-off against Representation Guidance.
