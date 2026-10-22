---
id: method:harness-scaling
type: method
title: 'Harness Scaling'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:agentic-rsi-routing-posttrain'
  reason: 'Harness Scaling is an active plug-in; method:neohorse-1 remains the first hop'
  use_instead: method:neohorse-1
assumptions:
- 'White-box factorized harness space at train time. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:harness-scaling
recipes:
- recipe:harness-scaling
claims:
- benchmark: 'White-box held-out harnesses and unseen black-box harnesses vs single-harness RL'
  metric: 'cross-harness generalization vs single-config RL'
  value: 'improves unseen white-box configs; transfers to unseen external black-box harnesses better than training on one complex black-box harness'
  baseline: 'single-harness agentic RL'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29458'
  notes: 'Does not retarget method:neohorse-1.'
tags:
- agentic-rl
- harness
- active
---

# Harness Scaling

## Method Overview
Harness Scaling treats harness configuration as a training axis: a factorized space, a compact factorial training subset, and RL that mixes global coverage with controlled per-task variation.

## When to Use
- Agentic RL that must survive harness swaps at deploy instead of specializing to one scaffold.

## When NOT to Use
Routing-guided OPD from harness traces → `method:neohorse-1`. Async stragglers → `method:sao`. Production kernel → `method:omp2-harness`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:neohorse-1`.

## Gotchas & Failure Modes
- No public code.
- How the factorial subset is chosen matters as much as using more than one harness.
