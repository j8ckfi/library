---
id: method:epic
type: method
title: 'EPIC'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:math-code-rl-dense'
  reason: 'EPIC is an active plug-in; method:cispo remains the first hop'
  use_instead: method:cispo
assumptions:
- 'Behavior-policy sampled prefixes. Exact reverse-KL coordinate, not a local quadratic trust region.'
last_reviewed: '2026-10-22'
papers:
- paper:epic
recipes:
- recipe:epic
claims:
- benchmark: 'Off-policy MoE math RL vs token-level and sequence-level clipping'
  metric: 'math-reasoning score vs GRPO / GSPO clipping'
  value: 'outperforms standard and sequence-level clipping on math benches; competitive with routing-replay alternatives at lower memory'
  baseline: 'GRPO token clip; GSPO sequence clip; routing-replay clip-higher'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29999'
  notes: 'Does not retarget method:cispo.'
tags:
- rlvr
- importance-sampling
- active
---

# EPIC

## Method Overview
EPIC treats the autoregressive prefix as the IS change of measure and clips the exact reverse-KL coordinate r-1-log r of the prefix likelihood ratio instead of a token-local PPO clip.

## When to Use
- Long-response or off-policy RLVR where token-level clips ignore prefix drift, especially sparse-MoE policies.

## When NOT to Use
Default dense Pass@1 → `method:cispo`. MoE/VL default → `method:sapo`. Target-ESS tempered IS → `method:tetpo`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:cispo`.

## Gotchas & Failure Modes
- Derived for AR prefixes, not a CISPO substitute.
- Code LiChengxi666/EPIC.
