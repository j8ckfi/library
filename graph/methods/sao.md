---
id: method:sao
type: method
title: "SAO (Synchronous-Asynchronous Policy Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:agentic-async-rl
supersedes:
  - method:grpo
  - method:dr-grpo
papers:
  - paper:sao
recipes:
  - recipe:sao
claims:
  - benchmark: "Agentic Async Trajectories & Tool-Use RL"
    metric: "async rollout throughput & reward"
    value: "Default SOTA for agentic async RL"
    baseline: "Group-GRPO"
    date: "2026-08-26"
    verified: true
    notes: "Decouples environment tool execution from policy gradient updates with importance-corrected replay buffers."
tags:
  - post-training
  - rl-alignment
  - agentic
  - async-rl
  - sao
  - sota
---

# SAO (Synchronous-Asynchronous Policy Optimization)

## Method Overview
SAO (Synchronous-Asynchronous Policy Optimization) solves the straggler bottleneck in multi-turn agent environments (tool calls, code sandboxes, external APIs):
1. **Asynchronous Trajectory Buffering**: Rollout workers run decoupled from the policy gradient optimization loop.
2. **Off-Policy Importance Correction**: Applies variance-bounded importance weights to utilize slightly off-policy asynchronous rollouts safely.

## When to Use
- Default SOTA optimizer for agentic async RL and tool-calling environments.

## Supersession
- Supersedes synchronous `method:grpo` / `method:dr-grpo` for agentic asynchronous tasks.
