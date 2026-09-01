---
id: task:long-horizon-tool-agent
type: task
title: "Long-Horizon Tool Agent"
domain: "agents"
summary: "Long trajectory of tools/web/SWE with a small active context. Different from dumped-prompt RLM."
scope: "Many sequential tool steps whose history must be folded. Not dumped-prompt offload and not the SWE harness without folding."
out_of_scope:
  - "Dumped corpus prompt offload (RLM)"
  - "SWE harness without folding"
  - "Async RL training without a folding objective (SAO)"
redirects:
  - when: "dumped corpus much larger than the window"
    to: "task:long-context-prompt-offload"
  - when: "SWE harness without folding"
    to: "task:software-engineering-agent-harness"
last_reviewed: "2026-09-01"
current_sota:
  - method: method:foldgrpo
    as_of: "2025-10"
    benchmark: "BrowseComp-Plus / SWE-Bench Verified, Seed-OSS-36B 32K×10"
    metric: "score"
    value: "BrowseComp-Plus 0.620 vs ReAct 327K+GRPO 0.540 vs ReAct 32K 0.286; SWE-Bench Verified 0.580 vs ReAct 327K+GRPO 0.574; GPT-5 ReAct 0.793 / 0.718 still ahead"
    notes: "36B-class SOTA, not frontier-model SOTA."
methods:
  - method:foldgrpo
  - method:agentfold
  - method:rao
tags:
  - agents
  - agent-recursion
  - foldgrpo
  - long-horizon
---

# Long-Horizon Tool Agent

## Problem Definition
The agent takes many tool/web/SWE steps. The problem is the **trajectory**, not a dumped prompt. Keep a small active context by folding completed sub-trajectories.

## Evaluation Protocol & Benchmarks
- BrowseComp-Plus, SWE-Bench Verified at 32K×10 vs ReAct 32K and ReAct 327K+GRPO.
- Record GPT-5 ReAct as still ahead.

## SOTA Landscape
- **current_sota**: FoldGRPO (`method:foldgrpo`).
- **Active**: AgentFold (web history, 36.2% BrowseComp); RAO (trained recursion, TextCraft 24% vs 95%).
