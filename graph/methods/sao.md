---
id: method:sao
type: method
title: "SAO (Single-Rollout Asynchronous Optimization)"
category: "rl-alignment"
status: sota
sota_for:
  - task:agentic-async-rl
supersedes:
  - method:grpo
  - method:dr-grpo
do_not_use_for:
  - when: "sparse-outcome coverage / anti-drift on a small revisited task pool, not async latency"
    reason: "SAO is the async straggler default; CANOPY/DRACO own outcome-only long-horizon agent RL"
    use_instead: "task:outcome-only-long-horizon-agent-rl"
  - when: "build an agent rather than train a policy"
    reason: "SAO trains a policy; the harness default is mini-SWE-agent"
    use_instead: "method:mini-swe-agent"
last_reviewed: "2026-09-04"
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

# SAO (Single-Rollout Asynchronous Optimization)

## Method Overview
SAO (Single-Rollout Asynchronous Optimization) solves the straggler bottleneck in multi-turn agent environments (tool calls, code sandboxes, SWE benchmarks):
1. **Single Rollout per Prompt**: Uses 1 rollout per prompt coupled with a learned value model, avoiding costly multi-sample synchronization under variable execution latency.
2. **Double-Sided Token Clipping**: Applies symmetric token-level clipping bounds for stable asynchronous updates.
3. **Agentic Async Scale**: Successfully adopted in large-scale agentic training (e.g. GLM-5.2). Does not replace dense math/code optimizers like CISPO.

## When to Use
- Default SOTA optimizer for agentic async RL and tool-calling environments.

## Relation to Existing SOTA
- Remains SOTA for `task:agentic-async-rl`. Does **not** own outcome-only long-horizon coverage (`method:canopy`) or outcome-blind rubric credit (`method:draco`).

## Supersession
- Supersedes synchronous `method:grpo` / `method:dr-grpo` for agentic asynchronous tasks.
