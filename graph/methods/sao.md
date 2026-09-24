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
  - when: "train a live-web multi-hop search agent (SFT-RL climbing), not async stragglers"
    reason: "Iris owns that search-agent recipe; SAO remains straggler replay"
    use_instead: "method:iris"
  - when: "build an agent rather than train a policy"
    reason: "SAO trains a policy; the harness default is mini-SWE-agent"
    use_instead: "method:mini-swe-agent"
  - when: "diagnose which multi-turn tool calls are trainable (nested sampling / contextual bandit)"
    reason: "SAO is async straggler replay; Critical-State RL selects which turns receive gradient"
    use_instead: "method:critical-state-rl"
  - when: "distill optimized-harness behaviors into weights under a fixed target harness"
    reason: "SAO is async RL; Harness-Zero is agent-as-harness SFT"
    use_instead: "method:harness-zero"
  - when: "multi-stage agent capability stacking / continual learning"
    reason: "SAO is async straggler replay; ACLArena stacks sequential post-train stages"
    use_instead: "task:agent-continual-learning"
  - when: "category see-saw on heterogeneous SWE RL"
    reason: "SAO is the async algorithm; Category-Aware SWE Experts split and reintegrate categories"
    use_instead: "task:swe-agent-category-expert-rl"
  - when: "Actor-then-Critic IS-aligned critic rather than async stragglers"
    reason: "SAO remains async first hop; PACT's SWE lift does not retarget SAO"
    use_instead: "method:pact"
last_reviewed: "2026-09-24"
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
- Pre-RL tool OPKD with persistent lookahead (`method:pta`) is not this shelf: lookahead fills idle distill capacity under a fixed teacher; SAO owns async policy-train stragglers.
- Multi-turn trainability diagnostic (`method:critical-state-rl`) selects which calls receive gradient; it does not replace SAO. Harness distillation into weights is `method:harness-zero`.
- Multi-stage agent continual learning is `method:aclarena`. Category-aware SWE expert RL is `method:category-aware-swe-experts`. Neither replaces SAO.
- Actor-then-Critic IS (`method:pact`) is a token-level critic recipe. SWE-Verified +3.8 vs SAO is mention-only and does not retarget this async first hop.

## Supersession
- Supersedes synchronous `method:grpo` / `method:dr-grpo` for agentic asynchronous tasks.
