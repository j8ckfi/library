---
id: method:self-hpo
type: method
title: 'Self-HPO'
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'production harness kernel (rewind, sandbox, remote, TUI)'
  reason: 'omp2 remains the kernel; Self-HPO alternates harness proposals with policy RL'
  use_instead: method:omp2-harness
- when: 'formal Harness RSI framework + PAC admission bounds (frozen weights)'
  reason: 'Harness-RSI freezes weights; Self-HPO updates the policy under the selected harness'
  use_instead: method:harness-rsi
- when: 'recursive self-rewrite of a research-agent harness (accepted rewrite is the next incumbent)'
  reason: 'AIDE2 rewrites the harness as the agent; Self-HPO keeps a policy RL step'
  use_instead: method:aide2
assumptions:
- 'Coding agent with an editable harness and RL on the policy. Paper: Qwen3.5-35B-A3B; optional stronger external harness proposer (Opus 4.8).'
- 'No public code as of 2026-10-19.'
last_reviewed: '2026-10-19'
papers:
- paper:self-hpo
recipes:
- recipe:self-hpo
claims:
- benchmark: 'Three coding benches, Qwen3.5-35B-A3B average resolve rate'
  metric: 'average resolve rate'
  value: '57.8%→64.8%; joint gain exceeds harness-only plus policy-only'
  baseline: 'harness-only / policy-only (single-paper)'
  date: '2026-10-19'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22791'
  notes: 'Does not retarget omp2, Harness-RSI, RRSI, or AIDE2.'
tags:
- harness
- rsi
- coding-agent
- active
---

# Self-HPO

## Method Overview
Self-HPO alternates an H-step where the current policy proposes harness candidates from its failures with a P-step that RL-updates the policy under the selected harness. Hard tasks from training become the next harness search set.

## When to Use
- Coding agents where a harness tuned for one checkpoint misses the next policy's failures, and you can update both the harness and the weights.

## When NOT to Use
Production kernel → `method:omp2-harness`. Frozen-weight Harness RSI → `method:harness-rsi`.

## Relation to Existing SOTA
Active plug-in on `task:agent-harness-runtime` with a mention on `task:agentic-rsi-routing-posttrain` (`sota_for: []`). Does **not** replace omp2 or Harness-RSI.

## Gotchas & Failure Modes
- Joint gain is superadditive in the paper; pairing an optimized component with a base counterpart still keeps some gain.
- External proposer (Opus 4.8) is optional extra, not required.
