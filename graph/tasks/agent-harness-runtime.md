---
id: task:agent-harness-runtime
type: task
title: "Agent Harness Runtime"
domain: "agents"
summary: "Architecture of a production coding-agent harness that must survive multiplexed local workspaces, remote drivers, spectators, and untrusted autonomous factory jobs."
scope: "Architecture of a production coding-agent harness that must survive multiplexed local workspaces, remote drivers, spectators, and untrusted autonomous factory jobs (the four envelope tests in the Stencil Harness Playbook)."
out_of_scope:
  - "SWE-bench eval loops and issue-to-patch start loops"
  - "Training an agent policy (SAO)"
  - "Outcome-only long-horizon agent RL (CANOPY / DRACO)"
  - "Dumped 10M-token prompts (RLM)"
  - "MCP as the product protocol (MCP stays agent-communication)"
redirects:
  - when: "issue-to-patch / locked eval"
    to: "task:software-engineering-agent-harness"
  - when: "train agent RL"
    to: "task:agentic-async-rl"
  - when: "outcome-only long-horizon agent RL (coverage / anti-drift or rubric credit)"
    to: "task:outcome-only-long-horizon-agent-rl"
  - when: "dumped long prompt"
    to: "task:long-context-prompt-offload"
  - when: "how to talk to tools/agents as a protocol"
    to: "task:agent-communication"
last_reviewed: "2026-09-02"
current_sota:
  - method: method:omp2-harness
    as_of: "2026-09-02"
    benchmark: "Pi official extension examples (Appendix A) + four envelope tests"
    metric: "journal-honest stateful examples / architecture envelope"
    value: "2 correct of 78 Pi examples (60 stateless, 17 stateful); journal covering message tree only ⇒ rewind/fork/resume lie"
    notes: "Self-reported blog architecture, not a SWE-bench number. Does not replace mini-SWE-agent, CCA, OpenHands, SAO, FoldGRPO, RLM, MAGIC, CISPO, Muon2, MCP, or ACE."
methods:
  - method:omp2-harness
tags:
  - agents
  - agent-harness
  - harness
  - omp
  - omp2
  - stencil
---

# Agent Harness Runtime

## Problem Definition
Build the **harness kernel** for a durable coding-agent engine: one authoritative session, a trusted control plane, bounded cancellable work, explicit model/provider compatibility, and views that are projections. The four envelope tests (Stencil Harness Playbook, 2026-09-02) are the architecture bar: multiplexed local workspace, remote driver, spectator, and untrusted autonomous factory (Factorio).

This is **not** the SWE-bench start/eval loop. Issue → patch / locked mini harness remains `task:software-engineering-agent-harness` (`method:mini-swe-agent`).

## Evaluation Protocol & Benchmarks
- **Envelope tests**, not SWE-bench: multiplexed workspace, remote driver, spectator, Factorio. A design that only works for the first case smuggles the controller into the TUI.
- **Journal honesty**: rewind, fork, resume, replication, and inspection must derive from one journaled session. Pi official examples: 78 total, 60 stateless, 17 stateful, 2 correct (Appendix A).
- **Hazards**: treating this card as a SWE-bench ranking scaffold; stuffing MCP into the permanent tool grammar; copying Pi's three-callback tool API (`renderCall` / `execute` / `renderResult`) or dual authorities.

## SOTA Landscape
- **Default (this task)**: **omp² harness** (`method:omp2-harness`, `paper:harness-playbook`). Spec for a production engine still being built; start with journal → session DOM.
- **Not this task**: mini-SWE-agent (issue → patch / locked eval), CCA (equal-model Pro scaffold), OpenHands/CodeAct (production OSS SWE agent), SAO (train a policy), FoldGRPO (trajectory folding), RLM (dumped long prompt), MCP (agent↔tool protocol), ACE (agent memory), MAGIC / CISPO / Muon2 (training/eval kernels).
- Related workflow, not this architecture: [prewalk](https://stencil.so/blog/prewalk) is a workflow on omp, not current_sota here.
