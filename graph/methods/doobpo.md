---
id: method:doobpo
type: method
title: 'DoobPO'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:posttrain-diffusion'
  reason: 'DoobPO is an active plug-in; method:diffusion-opsd remains the first hop'
  use_instead: method:diffusion-opsd
assumptions:
- 'Intractable action likelihoods. Two-stage ratio then drift distill. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:doobpo
recipes:
- recipe:doobpo
claims:
- benchmark: 'Diffusion and flow policies vs PPO/GRPO-style likelihood RL'
  metric: 'policy improvement without tractable action likelihoods'
  value: 'separates a lightweight ratio-model improvement from generative distillation via conditional drift matching; NeurIPS 2026'
  baseline: 'PPO / GRPO on diffusion policies that need action likelihoods'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28990'
  notes: 'Does not retarget method:diffusion-opsd.'
tags:
- diffusion
- flow
- active
---

# DoobPO

## Method Overview
DoobPO fine-tunes diffusion/flow policies without action likelihoods: a ratio model represents the desired update, then a Doob h-transform distills the ratio-tilted target into the generator as conditional drift.

## When to Use
- Flow or diffusion control policies where PPO/GRPO cannot score actions.

## When NOT to Use
Text/image DiffusionOPSD → `method:diffusion-opsd`. Teacher-free flow matching → `method:self-opd`. Proximal velocity matching → `method:mend`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:diffusion-opsd`.

## Gotchas & Failure Modes
- NeurIPS 2026. No public code.
- Control/robotic generative policies, not T2I reward FT by default.
