---
id: method:ccr
type: method
title: 'CCR'
category: rl
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'single-turn dense math/code Pass@1 RLVR (CISPO default)'
  reason: 'CISPO remains Pass@1; CCR is a short-window concurrent-problem packing plug-in'
  use_instead: method:cispo
- when: 'Pass@K / coverage / no-backward'
  reason: 'ES-reasoning remains that first hop'
  use_instead: method:es-reasoning
assumptions:
- 'GRPO-family RLVR host. Paper: 4B/8B math models; three concurrent verifiable problems in one capped completion.'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:ccr
recipes:
- recipe:ccr
claims:
- benchmark: '4B/8B math RLVR vs single-problem GRPO 32k window'
  metric: 'tokens per training step; 8k CCR window'
  value: '4B 975464→174957 (−82.1%); 8B 793832→165788 (−79.1%)'
  baseline: 'single-problem GRPO 32k (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22887'
  notes: 'Does not retarget CISPO. Reward-preserving packing, not a new Pass@1 loss.'
tags:
- rlvr
- grpo
- short-window
- active
---

# CCR

## Method Overview
Concurrent Constraint Reinforcement packs three independently verifiable problems into one capped training completion so truncated windows still keep correctness credit. A shared budget shortens useful reasoning without an explicit length penalty.

## When to Use
- Short-window RLVR where single-problem rollouts truncate before an answer and group-relative advantages vanish.

## When NOT to Use
Default Pass@1 dense RLVR → `method:cispo`.

## Relation to Existing SOTA
Active plug-in on `task:math-code-rl-dense` (`sota_for: []`). Does **not** replace CISPO.

## Gotchas & Failure Modes
- Continuation of Batched Contextual Reinforcement; not a CISPO replacement.
- Quality claims are supporting single-problem evals, not a MATH-500 bake-off against CISPO.
