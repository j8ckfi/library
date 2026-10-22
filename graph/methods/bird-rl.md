---
id: method:bird-rl
type: method
title: 'BIRD-RL'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:agentic-async-rl'
  reason: 'BIRD-RL is an active plug-in; method:sao remains the first hop'
  use_instead: method:sao
assumptions:
- 'Stateful SQL environments. Trajectory-scoped replica reuse rather than Kubernetes-per-rollout.'
last_reviewed: '2026-10-22'
papers:
- paper:bird-rl
recipes:
- recipe:bird-rl
claims:
- benchmark: 'BIRD-CRITIC-SQLite vs proprietary agents; spatial RL efficiency'
  metric: 'Success Rate; replica-reuse spatial efficiency'
  value: '7B 44.40% / 14B 48.00% vs Claude-Opus-4.6 Agent 48.20%; 12.8x spatial RL efficiency vs per-rollout containers'
  baseline: 'per-rollout database containers; Claude-Opus-4.6 Agent 48.20%'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29426'
  notes: 'Does not retarget method:sao.'
tags:
- agentic-rl
- sql
- active
---

# BIRD-RL

## Method Overview
BIRD-RL trains SQL/data-centric agents with a four-stage curriculum and trajectory-scoped persistent execution so database replicas can be reused without contaminating other rollouts.

## When to Use
- Agentic RL on stateful SQL / data-lake tools where a container per rollout does not fit and naive DB reuse poisons GRPO groups.

## When NOT to Use
Async straggler algorithm → `method:sao`. Source-code env factory → `method:codemidas`. Issue-to-patch loop → `method:mini-swe-agent`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:sao`.

## Gotchas & Failure Modes
- NeurIPS 2026. Code bird-bench/BIRD-RL.
- Curriculum is part of the method, not optional warmup.
