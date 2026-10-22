---
id: method:longzero
type: method
title: 'LongZero'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:data-free-self-evolution'
  reason: 'LongZero is an active plug-in; method:j-zero remains the first hop'
  use_instead: method:j-zero
assumptions:
- 'Model can propose verifiable long-context tasks. Zero external long-context corpus.'
last_reviewed: '2026-10-22'
papers:
- paper:longzero
recipes:
- recipe:longzero
claims:
- benchmark: 'Long-context reasoning RL from self-proposed verifiable tasks'
  metric: 'long-context reasoning vs short-context zero-data RL'
  value: 'lets an LLM improve long-context reasoning from tasks it proposes itself without external corpora or a stronger teacher'
  baseline: 'short-context zero-data RL; human-annotated long-context RL data'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.30132'
  notes: 'Does not retarget method:j-zero.'
tags:
- long-context
- rlvr
- active
---

# LongZero

## Method Overview
LongZero has the model propose long, diverse, verifiable reasoning tasks and then RL on those tasks, so long-context gains do not wait on annotated long sequences or a stronger teacher.

## When to Use
- Long-context reasoner RL when labeled long traces and stronger teachers are unavailable.

## When NOT to Use
Challenger-Solver-Judge covering unverifiable domains → `method:j-zero`. Dumped corpus offload → `method:rlm`. Pass@1 labeled math → `method:cispo`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:j-zero`.

## Gotchas & Failure Modes
- Code zhennan1/LongZero.
- Self-proposed tasks still need a verifier; this is not unlabeled consensus.
