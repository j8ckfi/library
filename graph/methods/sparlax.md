---
id: method:sparlax
type: method
title: 'SpaRLax'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'single-turn dense math/code Pass@1 with CISPO as the loss'
  reason: 'CISPO remains discrete-token Pass@1; SpaRLax is sparse-relaxed soft-CoT RL'
  use_instead: method:cispo
assumptions:
- 'Soft-CoT tokens as differentiable intermediates, not MDP actions. Entmax sparsity.'
- 'Nine reasoning benches. No public code as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:sparlax
recipes:
- recipe:sparlax
claims:
- benchmark: 'Nine reasoning benchmarks vs soft-CoT RL baselines'
  metric: 'average score vs prior soft-CoT RL that treats soft tokens as MDP actions'
  value: 'highest average among compared soft-CoT RL methods on nine reasoning benches'
  baseline: 'soft-CoT RL that does not backprop across soft tokens'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.27220'
  notes: 'Does not retarget CISPO.'
tags:
- rlvr
- soft-cot
- active
---

# SpaRLax

## Method Overview
SpaRLax trains soft-CoT by backpropagating through differentiable mixed-token steps and using entmax to truncate confident long tails while keeping several candidates under uncertainty.

## When to Use
- Soft-CoT RLVR where prior methods treat mixture tokens as discrete actions and drop cross-step gradients.

## When NOT to Use
Discrete-token Pass@1 → `method:cispo`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:cispo`.

## Gotchas & Failure Modes
- Not discrete-token CISPO.
- Entmax temperature/sparsity still needs a sweep.
