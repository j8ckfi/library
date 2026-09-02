---
id: task:agent-communication
type: task
title: "Agent Communication"
domain: "agents"
summary: "How to talk to agents: tools, files, protocols. MCP for agent↔tool; A2A only for agent↔agent; human AGENTS.md on disk."
scope: "Tool schemas, files on disk, and protocols. Not a SWE loop and not MAS."
out_of_scope:
  - "Choosing the SWE harness (mini-SWE-agent)"
  - "Multi-agent orchestration as a default"
  - "Training SAO"
redirects:
  - when: "building the SWE loop rather than the tool protocol"
    to: "task:software-engineering-agent-harness"
  - when: "wanting a multi-agent crew as the communication layer"
    to: "task:multi-agent-orchestration"
last_reviewed: "2026-09-02"
current_sota:
  - method: method:mcp
    as_of: "2026-07"
    benchmark: "MCP spec (stateless core)"
    metric: "protocol snapshot"
    value: "2026-07-28 stateless core (agent↔tool)"
    notes: "Spec, not a bench. Native FC if the model was trained for it; NLT niche for weak/no-FC. Human AGENTS.md; do not LLM-init."
methods:
  - method:mcp
  - method:a2a-protocol
  - method:nlt
  - method:openhands-codeact
tags:
  - agents
  - agent-protocol
  - mcp
  - a2a
  - nlt
  - agents-md
---

# Agent Communication

## Problem Definition
How agents call tools, how two agents negotiate, and how humans put instructions on disk. The Stencil Harness Playbook agrees MCP must not sit in the permanent tool grammar (discover the long tail via `dyn`/Bash); MCP remains current_sota here as the agent↔tool protocol.

## Evaluation Protocol & Benchmarks
- MCP: spec 2026-07-28, not a leaderboard.
- τ-bench gpt-4o FC 61.2% retail / 35.2% airline.
- NLT 69.1→87.5; replication +14.9pp.
- ETH AGENTS.md: LLM-generated −0.5pp Lite / −2pp CTXbench, +20% cost; developer vs LLM +7pp avg, p=0.038.

## SOTA Landscape
- **Agent↔tool SOTA**: MCP (`method:mcp`).
- **Active agent↔agent**: A2A v1.0, only across vendors.
- **Niche**: NLT for weak/no-FC.
- CodeAct is on the OpenHands card.
