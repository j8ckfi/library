---
id: method:rpo
type: method
title: 'Routing Policy Optimization (RPO)'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'aggregation-first reward tilting for diffusion RL'
  reason: 'DiffusionART tilts rewards; RPO routes attention'
  use_instead: method:diffusionart
- when: 'flow-model RL via proximal velocity matching'
  reason: 'MEND matches velocity; RPO explores via routing'
  use_instead: method:mend
- when: 'on-policy self-distillation of a diffusion generator'
  reason: 'DiffusionOPSD remains generator OPSD'
  use_instead: method:diffusion-opsd
assumptions:
- 'Online diffusion/flow RL where attention routing can be sampled at selected denoising levels.'
- 'Code: none found as of 2026-10-16. Distinct from skipped 2610.17767 root-token RPO.'
last_reviewed: '2026-10-16'
papers:
- paper:rpo
recipes:
- recipe:rpo
claims:
- benchmark: 'text-to-image and text-to-video vs Flow-GRPO-style'
  metric: 'training efficiency at matched or better quality'
  value: 'nearly 4x vs Flow-GRPO-style; dense attention restored at inference'
  baseline: 'Flow-GRPO-style score-function noise (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22282'
  notes: 'Does not retarget DiffusionART / MEND / DiffusionOPSD. Distinct from skipped 2610.17767.'
tags:
- diffusion
- routing
- rl-alignment
- active
---

# Routing Policy Optimization (RPO)

## Method Overview
At a few denoising levels, each query block either stays dense or samples extra key blocks in proportion to native attention mass. The sampled route perturbs velocity; a Gaussian likelihood around the dense velocity yields a score-function update. Two rollouts share prompt, latent, routed levels, and dense anchors.

## When to Use
- Online diffusion RL where perturbing noise is expensive and you can sample attention routes instead.

## When NOT to Use
Reward tilting → `method:diffusionart`. Proximal velocity matching → `method:mend`. Generator OPSD → `method:diffusion-opsd`.

## Relation to Existing SOTA
Active plug-in on `task:posttrain-diffusion` (`sota_for: []`). Does **not** replace DiffusionART or MEND.

## Gotchas & Failure Modes
- Distinct from the skipped root-token RPO (`arXiv:2610.17767`).
- No public GitHub as of 2026-10-16; project page only.

