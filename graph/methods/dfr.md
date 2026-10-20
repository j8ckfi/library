---
id: method:dfr
type: method
title: 'DFR'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'aligning text-to-image diffusion or flow models with rewards (default)'
  reason: 'DiffusionOPSD / Self-OPD remain first hops; DFR is distributional regularization on the generated samples'
  use_instead: method:diffusion-opsd
- when: 'proximal velocity matching (~100 updates)'
  reason: 'MEND is the velocity-matching plug-in'
  use_instead: method:mend
assumptions:
- 'Reward FT of diffusion/flow. Paper: SD3.5-M GenEval and OCR vs KL-tuned RAM / Flow-GRPO.'
- 'No public code as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:dfr
recipes:
- recipe:dfr
claims:
- benchmark: 'SD3.5-M GenEval / OCR vs KL-regularized RAM and Flow-GRPO'
  metric: 'matched-reward diversity and pretrained drift; wall-clock vs Flow-GRPO'
  value: 'up to +29% diversity and -12% drift at matched reward; 36-41x faster than Flow-GRPO; DFR-MMD GenEval 0.95 at +7% time vs RAM'
  baseline: 'reverse-KL / l2 velocity penalty; RAM; Flow-GRPO'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.24897'
  notes: 'MMD / Frechet / DreamSim instantiations. Does not replace DiffusionOPSD or Self-OPD.'
tags:
- diffusion
- reward-ft
- diversity
- active
---

# DFR

## Method Overview
DFR (Distributional Functional Rewards) adds a per-sample, distribution-dependent reward (MMD, Frechet, DreamSim diversity) so reward FT acts on the generated distribution instead of an l2 velocity KL penalty that only constrains sampling dynamics.

## When to Use
- Reward-tuning a flow/diffusion model where reverse-KL RAM collapses diversity.

## When NOT to Use
Default diffusion reward alignment → `method:diffusion-opsd` / `method:self-opd`.

## Relation to Existing SOTA
Active plug-in on `task:posttrain-diffusion` (`sota_for: []`). Does **not** replace DiffusionOPSD, Self-OPD, or MEND.

## Gotchas & Failure Modes
- Instantiation (MMD vs FD vs DreamSim) is task-dependent.
- Not a dLLM method.
