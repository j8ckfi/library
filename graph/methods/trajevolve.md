---
id: method:trajevolve
type: method
title: 'TrajEvolve'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'programmatic checker AppWorld coverage / anti-drift'
  reason: 'CANOPY remains coverage; TrajEvolve evolves hindsight trajectories and binary step necessity'
  use_instead: method:canopy
- when: 'single-turn dense math/code Pass@1 RLVR'
  reason: 'CISPO remains Pass@1; TrajEvolve is long-horizon trajectory evolution'
  use_instead: method:cispo
assumptions:
- 'Hindsight edits of low-quality steps plus counterfactual binary necessity labels. NeurIPS 2026.'
- 'Code wenyiwy99/TrajEvolve as of 2026-10-21.'
last_reviewed: '2026-10-21'
papers:
- paper:trajevolve
recipes:
- recipe:trajevolve
claims:
- benchmark: 'Two long-horizon datasets (paper); NeurIPS 2026'
  metric: 'task success vs base RL that only uses model-sampled trajectories and sparse terminal rewards'
  value: 'evolved trajectories plus counterfactual necessary-step labels outperform sparse-outcome RL on both reported datasets'
  baseline: 'sparse-outcome RL on model-sampled trajectories'
  date: '2026-10-21'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28060'
  notes: 'Does not retarget CANOPY or CISPO.'
tags:
- agentic-rl
- credit-assignment
- hindsight
- active
---

# TrajEvolve

## Method Overview
TrajEvolve refines low-quality steps in historical traces into evolutionary trajectories that stay in the base model's support, and treats step credit as binary necessity obtained by counterfactual verification.

## When to Use
- Long-horizon RL that cannot sample enough successes and updates every step from a terminal reward.

## When NOT to Use
Checker coverage → `method:canopy`. Pass@1 → `method:cispo`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:canopy`.

## Gotchas & Failure Modes
- Counterfactual verification cost scales with steps.
- Not AppWorld coverage.
