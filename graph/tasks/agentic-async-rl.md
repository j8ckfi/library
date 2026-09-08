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
redirects:
  - when: "build an agent rather than train a policy"
    to: "task:software-engineering-agent-harness"
  - when: "outcome-only long-horizon agent RL (coverage / anti-drift), not async stragglers"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "train a live-web multi-hop search agent (SFT-RL climbing), not async stragglers"
    to: "task:web-search-agent-rl"
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
last_reviewed: "2026-09-08"
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
- **Not This Task**: sparse-outcome coverage / anti-drift on AppWorld-style agents is `task:outcome-only-long-horizon-agent-rl` (`method:canopy` / `method:draco`). Folding is `task:long-horizon-tool-agent`. Live-web search-agent climbing is `task:web-search-agent-rl` (`method:iris`).
