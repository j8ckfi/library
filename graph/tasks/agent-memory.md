---
id: task:agent-memory
type: task
title: "Agent Memory"
domain: "agents"
summary: "Persistent agent context: incremental playbooks, not rewrite, not recursive summary as long-context."
scope: "How an agent stores and updates strategies across tasks. Not dumped-prompt RLM and not a SWE loop."
out_of_scope:
  - "Recursive summary as the only long-context strategy"
  - "SWE patch loops with no playbook need"
  - "Dumped 10M-token prompt"
redirects:
  - when: "dumped corpus ≫ window"
    to: "task:long-context-prompt-offload"
  - when: "SWE issue-to-patch without a playbook"
    to: "task:software-engineering-agent-harness"
last_reviewed: "2026-09-01"
current_sota:
  - method: method:ace
    as_of: "2025-10"
    benchmark: "AppWorld, DeepSeek-V3.1"
    metric: "success %"
    value: "ACE 59.4 vs ReAct 42.4 (+17); vs GEPA latency −82%"
    notes: "Incremental bullets. Without feedback ACE/DC can degrade. Dynamic Cheatsheet collapse 18282 tok @66.7 → 122 tok @57.1."
methods:
  - method:ace
  - method:memgpt
tags:
  - agents
  - agent-memory
  - ace
  - memgpt
---

# Agent Memory

## Problem Definition
Agents need memory that accumulates strategies without collapsing under rewrite. Recursive summary is not this task (and fails as long-context).

## Evaluation Protocol & Benchmarks
- AppWorld (ACE vs ReAct / GEPA).
- DMR for MemGPT. Sleep-time compute as a persona-agent complement.

## SOTA Landscape
- **current_sota**: ACE (`method:ace`).
- **Active**: MemGPT for long-lived persona agents.
- **do_not_use**: recursive summary as the only long-context strategy.
