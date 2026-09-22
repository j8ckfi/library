---
id: task:agentic-async-rl
type: task
title: "Agentic Asynchronous Reinforcement Learning"
domain: "post-training"
summary: "Asynchronous policy optimization for multi-turn agentic environments with external tools, code interpreters, and web sandbox execution."
scope: "Training a tool-use / sandbox policy with asynchronous RL. Not choosing a software-engineering harness."
out_of_scope:
  - "Building or choosing a software-engineering agent loop (mini-SWE-agent / CCA / OpenHands)"
  - "Dumped long-prompt offload (RLM)"
  - "GUI computer-use without policy training"
  - "Outcome-only long-horizon agent RL where the failure is signal starvation / policy drift, not async latency"
  - "Live-web multi-hop search-agent training (Iris SFT-RL climbing)"
  - "Production post-train engine rather than the async algorithm (Miles)"
  - "Routing-harness RSI post-train (NeoHorse-1)"
  - "Adaptive math/code sampling until ≥1 correct (NGU); that is a CISPO-host sampler, not SAO straggler replay"
  - "Privileged self-OPD then Adaptive Retirement into pure agent RL (RetireOPD / ALFWorld/WebShop)"
  - "Data/env construction for coding-agent RL from source code (CodeMidas)"
  - "Diagnosing which multi-turn tool calls are trainable (Critical-State RL)"
  - "Harness distillation into weights under a fixed target harness (Harness-Zero)"
redirects:
  - when: "build an agent rather than train a policy"
    to: "task:software-engineering-agent-harness"
  - when: "outcome-only long-horizon agent RL (coverage / anti-drift), not async stragglers"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "train a live-web multi-hop search agent (SFT-RL climbing), not async stragglers"
    to: "task:web-search-agent-rl"
  - when: "production post-train stack (SGLang / Megatron / LoRA RL / OPD), not the async algorithm"
    to: "task:frontier-rl-posttrain-stack"
  - when: "agentic RSI / routing-harness post-train, not async stragglers"
    to: "task:agentic-rsi-routing-posttrain"
  - when: "adaptive sampling until ≥1 correct on math/code prompts, not tool stragglers"
    to: "task:math-code-rl-dense"
  - when: "privileged self-OPD then retire to RL (ALFWorld/WebShop), not async stragglers"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "data/env construction for coding-agent RL from source code"
    to: "task:coding-agent-rl-environment-construction"
  - when: "diagnose which multi-turn tool calls are trainable (nested sampling / contextual bandit)"
    to: "method:critical-state-rl"
  - when: "distill optimized-harness behaviors into weights under a fixed target harness"
    to: "task:harness-distillation"
current_sota:
  - method: method:sao
    as_of: "2026-08-26"
    benchmark: "Agentic Tool-Use & Multi-Turn Sandbox Benchmarks"
    metric: "async rollout throughput & task success rate"
    value: "Default SOTA for agentic async RL"
    notes: "SAO (2607.07508) decouples environment tool execution from policy optimization with importance-corrected replay buffers."
methods:
  - method:sao
  - method:bpco
  - method:dr-grpo
  - method:grpo
  - method:pta
  - method:iris
  - method:miles
  - method:neohorse-1
  - method:t1-terminal-rl
  - method:ngu
  - method:actobs
  - method:retireopd
  - method:codemidas
  - method:critical-state-rl
  - method:harness-zero
last_reviewed: "2026-09-22"
tags:
  - post-training
  - agentic
  - async-rl
  - sao
---

# Agentic Asynchronous Reinforcement Learning

## Problem Definition
Training agentic foundation models to interact with multi-turn environments (bash shells, code execution sandboxes, web browsers) where variable environment latency causes severe worker straggler bottlenecks under synchronous group RL algorithms.

This is **policy training**. Building a software-engineering agent loop is `task:software-engineering-agent-harness` (`method:mini-swe-agent`), not this task.

## SOTA Recommendation (as of 2026-09-08)
- **Primary Method**: **SAO** (`method:sao`, 2607.07508). Unchanged.
- **Related pre-RL tool OPKD (not this async-train default)**: `method:pta` (`arXiv:2609.04773`) teacher-commits tool turns before Search-R1 / DeepEyes RL. Lookahead fills idle distill capacity; it is not SAO's straggler replay.
- **Not This Task**: sparse-outcome coverage / anti-drift on AppWorld-style agents is `task:outcome-only-long-horizon-agent-rl` (`method:canopy` / `method:draco`). Folding is `task:long-horizon-tool-agent`. Live-web search-agent climbing is `task:web-search-agent-rl` (`method:iris`). Production post-train engine is `task:frontier-rl-posttrain-stack` (`method:miles`). Routing-harness RSI post-train is `task:agentic-rsi-routing-posttrain` (`method:neohorse-1`). Terminal-MoE recipe `method:t1-terminal-rl` (`arXiv:2609.11042`) is not SAO. Adaptive math/code sampling until ≥1 correct is `method:ngu` on `task:math-code-rl-dense` (uses async refill; not SAO). Privileged self-OPD then Adaptive Retirement is `method:retireopd` on `task:outcome-only-long-horizon-agent-rl` (not SAO).
- **Optional observation-token SFT init (not this async default)**: `method:actobs` (`arXiv:2609.20715`) supervises observation tokens before GRPO and changes later exploration (Terminal-Bench / aider-polyglot). Does not replace SAO.
- **Not this task (coding-agent RL env construction)**: `method:codemidas` on `task:coding-agent-rl-environment-construction`. Source-code-only env factory, not straggler replay.
- **Optional multi-turn trainability diagnostic (not this async default)**: `method:critical-state-rl` (`arXiv:2609.24985`) nested-samples which calls are trainable, then contextual-bandit at those states. BFCL v4 miss_func ~+14 pp. No public code. Does not replace SAO, CANOPY, CISPO, or FoldGRPO.
- **Not this task (harness distillation into weights)**: `method:harness-zero` on `task:harness-distillation`.
