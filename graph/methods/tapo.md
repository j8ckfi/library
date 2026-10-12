---
id: method:tapo
type: method
title: TAPO
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: single-turn dense math/code Pass@1 RLVR
  reason: CISPO remains Pass@1; TAPO is a trajectory-state-distribution correction on GRPO/GSPO-style
    hosts
  use_instead: method:cispo
- when: two-branch alpha-divergence sequence kernel instead of IS clip (ReSPO)
  reason: ReSPO replaces the IS clip; TAPO corrects compounded state shift along the trajectory
  use_instead: method:respo
assumptions:
- 'Long-horizon autoregressive LLM RL. Paper: eight competition math/code benches vs GRPO/GSPO.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:tapo
recipes:
- recipe:tapo
claims:
- benchmark: Eight competition-level math and coding benchmarks vs GRPO
  metric: relative improvement over GRPO
  value: up to +48% math / +12% algorithmic coding, with improved training stability as horizon grows
  baseline: GRPO; GSPO
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13020
  notes: Paper vs GRPO/GSPO, not CISPO. Does not retarget CISPO.
tags:
- post-training
- rlvr
- tapo
- active
---

# TAPO

## Method Overview
Reweight the trajectory by a state-distribution factor from the off-policy gradient. Estimate it with a geometric mean across tokens. Widen/narrow the clip as a function of remaining length.

## When to Use
- Long-horizon math/code RLVR where GRPO/GSPO is stable early then collapses as sequences grow.

## When NOT to Use
Pass@1 default → `method:cispo`. Sequence-kernel instead of IS clip → `method:respo`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** replace CISPO. Sibling of `method:gppo` (same group, divergence view).

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Headline lifts are vs GRPO, not CISPO.
- Geometric-mean estimator is a variance tool, not a new reward.
