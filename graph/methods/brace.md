---
id: method:brace
type: method
title: 'BRACE'
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'the locked first hop on task:agentic-async-rl'
  reason: 'BRACE is an active plug-in; method:sao remains the first hop'
  use_instead: method:sao
assumptions:
- 'MCP tool environments. Reward disagreement is the allocation signal. No public code as of 2026-10-22.'
last_reviewed: '2026-10-22'
papers:
- paper:brace
recipes:
- recipe:brace
claims:
- benchmark: 'Live MCP RL at three Qwen3-VL scales; BFCL / NESTFUL transfer'
  metric: 'peak vs strongest plotted baseline at matched new-rollout budget'
  value: 'exceeds strongest plotted baseline peaks with fewer new training rollouts; leads compared methods on BFCL and NESTFUL without further training'
  baseline: 'uniform group allocation; historical-bank collection counted separately'
  date: '2026-10-22'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.28785'
  notes: 'Does not retarget method:sao.'
tags:
- agentic-rl
- mcp
- active
---

# BRACE

## Method Overview
BRACE forecasts mixed-reward GRPO groups from a historical bank, per-task uncertainty, and a correlated reward model before spending new MCP rollouts. Discord is the paired-inference harness test that only counts disagreeing outcomes.

## When to Use
- MCP / tool-using RLVR where most groups are all-success or all-fail and uniform allocation wastes rollouts.

## When NOT to Use
Async environment-latency algorithm → `method:sao`. Silent-group prompt prior → `method:thinkprior`. Adaptive sampling until one correct → `method:ngu`.

## Relation to Existing SOTA
Active plug-in (`sota_for: []`). Does **not** replace `method:sao`.

## Gotchas & Failure Modes
- No public code.
- Historical-bank collection is not free even when new-rollout counts drop.
