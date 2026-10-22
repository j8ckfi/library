---
id: method:ssr
type: method
title: 'SSR'
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:agent-harness-runtime'
  reason: 'SSR is an active plug-in; method:omp2-harness remains the first hop'
  use_instead: method:omp2-harness
assumptions:
- 'Harness edits from execution traces. Adaptive evidence search. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:ssr
recipes:
- recipe:ssr
claims:
- benchmark: 'Harness evolution vs existing methods as the task pool grows'
  metric: 'downstream agent score vs evidence-selection baselines'
  value: 'existing evolution methods degrade as the task pool expands; SSR adaptively searches evidence combinations at each evolution step'
  baseline: 'harness evolution that uses the full growing task pool as evidence'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28815'
  notes: 'Does not retarget method:omp2-harness.'
tags:
- harness-rsi
- active
---

# SSR

## Method Overview
SSR (Successive Scale Racing) treats harness-evolution evidence selection as a search problem: more tasks help only if the optimizer picks the right evidence combination at each step.

## When to Use
- Harness RSI / instruction-tool-control-flow evolution when adding tasks starts to hurt.

## When NOT to Use
Production kernel → `method:omp2-harness`. Failure-pattern bandit curriculum → `method:activesaddler`. Frozen-weight terminal RSI → `method:riseharness`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:omp2-harness`.

## Gotchas & Failure Modes
- No public code.
- The failure mode is evidence selection, not a lack of tasks.
