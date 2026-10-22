---
id: method:uni-mem
type: method
title: 'Uni-Mem'
category: agent-memory
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:agent-memory'
  reason: 'Uni-Mem is an active plug-in; method:ace remains the first hop'
  use_instead: method:ace
assumptions:
- 'Online RL of both memory ops. Stage-Decoupled GRPO. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:uni-mem
recipes:
- recipe:uni-mem
claims:
- benchmark: 'Long-horizon agent memory construction+retrieval vs construction-only or split-supervision hosts'
  metric: 'downstream task success vs GRPO on a unified manager'
  value: 'Stage-Decoupled GRPO jointly trains construction and retrieval under one policy, avoiding confounded group comparisons of vanilla GRPO on long memory trajectories'
  baseline: 'construction-only learning; retrieval RL plus offline construction SFT; vanilla GRPO on the joint trajectory'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.29671'
  notes: 'Does not retarget method:ace.'
tags:
- agent-memory
- grpo
- active
---

# Uni-Mem

## Method Overview
Uni-Mem is one policy for memory construction and retrieval. Stage-Decoupled GRPO alternates group comparisons so long memory-management traces are not scored as a single confounded GRPO group.

## When to Use
- Learnable agent memory where construction and retrieval must co-adapt, not a frozen playbook plus an independent retriever.

## When NOT to Use
Write-time playbook → `method:ace`. System-One control plane → `method:jev-mem`. Read-time curator → `method:jitmem`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:ace`.

## Gotchas & Failure Modes
- No public code.
- Stage decoupling is required; joint GRPO on the full trace is the failure mode the paper names.
