---
id: method:gppo
type: method
title: GPPO
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: single-turn dense math/code Pass@1 RLVR
  reason: CISPO remains Pass@1; GPPO is an f-divergence trust-region design space on PPO-family hosts
  use_instead: method:cispo
- when: trajectory-induced state-distribution gap at long horizon (TAPO)
  reason: TAPO corrects state shift; GPPO unifies clipping via f-divergence geometry
  use_instead: method:tapo
assumptions:
- 'LLM RL with a PPO-family clip. Paper: eight competition math/code benches. Recovers PPO/DAPO/DPPO/RIPO
  as special cases.'
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:gppo
recipes:
- recipe:gppo
claims:
- benchmark: Eight competition-level math and coding benchmarks vs GRPO
  metric: relative improvement of the best GPPO instantiation over GRPO
  value: up to +50% math / +14% coding
  baseline: GRPO; PPO clip; DAPO / DPPO / RIPO as special cases
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13015
  notes: Paper vs GRPO, not CISPO. Does not retarget CISPO. DAPO/DPPO/RIPO are paper special cases, not
    library SOTA.
tags:
- post-training
- rlvr
- gppo
- active
---

# GPPO

## Method Overview
Pick an f-divergence for the trust region (geometry / resistance to shift) and an estimator topology (how faithfully you estimate that divergence). The usual PPO clip is one degenerate cell of that grid.

## When to Use
- You are already on a PPO/GRPO-family trainer and the clip is killing exploration, and you can change divergence and estimator together.

## When NOT to Use
Pass@1 default → `method:cispo`. Long-horizon state-distribution correction → `method:tapo`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** replace CISPO. Sibling of `method:tapo`.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Headline lifts are vs GRPO, not CISPO.
- Changing only the estimator or only f is not the paper's claim; both dimensions are required.
