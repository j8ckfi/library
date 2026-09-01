---
id: task:multi-agent-orchestration
type: task
title: "Multi-Agent Orchestration"
domain: "agents"
summary: "Default: do not. Single agent plus tools. MAS is an exception for high-value parallel research and AIME, not SWE patches."
scope: "Whether to use more than one agent. Default is single agent + tools (mini-SWE-agent / CCA). Not training SAO."
out_of_scope:
  - "SWE patches"
  - "τ-bench policy dialog"
  - "Sequential one-context work"
  - "CrewAI-default theater"
  - "Training SAO"
redirects:
  - when: "GitHub issue to patch"
    to: "task:software-engineering-agent-harness"
  - when: "train asynchronous RL for a tool-use policy"
    to: "task:agentic-async-rl"
last_reviewed: "2026-09-01"
current_sota:
  - method: method:single-agent-plus-tools
    as_of: "2026-06"
    benchmark: "MAC / Illusion of MAS / Gao cascade"
    metric: "default recommendation"
    value: "do not; 5/39 MAC configs beat human; auto MAS underperforms CoT-SC up to 10× cost"
    notes: "When MAS wins: Anthropic Jun 2025 orchestrator-worker +90.2% vs single Opus 4 on internal breadth research (~15× tokens); Gao hybrid cascade +1.1–12pp. AIME is the MAS exception."
methods:
  - method:single-agent-plus-tools
  - method:anthropic-orchestrator-worker
  - method:mini-swe-agent
  - method:cca
tags:
  - agents
  - multi-agent
  - orchestration
---

# Multi-Agent Orchestration

## Problem Definition
Should you use multiple agents? **Default: no.** Use one agent plus tools. This task exists so "build a multi-agent system" does not skip the negative knowledge in MAC, Illusion of MAS, Gao, and ETH AGENTS.md.

## Evaluation Protocol & Benchmarks
- MAC 5/39; Illusion of MAS vs CoT-SC; Gao tokens 4–220×.
- Exception: Anthropic orchestrator-worker +90.2% on *internal breadth research*; Gao cascade +1.1–12pp; AIME.

## SOTA Landscape
- **current_sota**: `method:single-agent-plus-tools` (points at mini-SWE-agent / CCA).
- **Niche**: `method:anthropic-orchestrator-worker` for high-value parallel research only.
- **do_not_use_for**: SWE patches, τ-bench, sequential one-context work. CrewAI-default is theater.
