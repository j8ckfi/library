---
id: method:single-agent-plus-tools
type: method
title: "Single agent + tools"
category: "agent-harness"
status: sota
sota_for:
  - task:multi-agent-orchestration
supersedes: []
do_not_use_for:
  - when: "internal high-value parallel breadth research"
    reason: "Anthropic Jun 2025 orchestrator-worker +90.2% vs single Opus 4 (~15× tokens) is the MAS exception for that setting"
    use_instead: "method:anthropic-orchestrator-worker"
  - when: "SWE patches"
    reason: "MAS is theater; use the bash ReAct loop"
    use_instead: "method:mini-swe-agent"
  - when: "τ-bench policy dialog"
    reason: "native FC / MCP, not a crew"
    use_instead: "method:mcp"
  - when: "dumped long prompt"
    reason: "RLM, not a swarm"
    use_instead: "method:rlm"
  - when: "training an agent policy"
    reason: "SAO, not CrewAI"
    use_instead: "method:sao"
assumptions:
  - "Default: do not use multi-agent. Point at mini-SWE-agent / CCA. AIME is the MAS exception."
last_reviewed: "2026-09-01"
papers:
  - paper:mac-meta-agent
  - paper:illusion-mas
  - paper:mas-hybrid-gao
  - paper:meta-agent-inefficiencies
recipes:
  - recipe:mini-swe-agent
claims:
  - benchmark: "MAC meta-agent challenge"
    metric: "configs beating human baseline"
    value: "5/39"
    baseline: "human-written simple ReAct; Terminus-2 / OpenHands unbeaten by MAC artifacts"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.04455"
    notes: "Successful artifacts converge on simple ReAct loops."
  - benchmark: "Illusion of Multi-Agent Advantage"
    metric: "auto MAS vs CoT-SC"
    value: "underperforms CoT-SC, up to 10× cost"
    baseline: "CoT self-consistency"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.13003"
    notes: "Default: do not."
  - benchmark: "Gao et al. hybrid cascade"
    metric: "quality / cost"
    value: "+1.1–12pp, cost down; tokens 4–220× for naive MAS"
    baseline: "single agent; MAS edge shrinks as models strengthen"
    date: "2025-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2505.18286"
    notes: "When MAS actually wins: cascade, not CrewAI-default. AIME is the exception."
tags:
  - agents
  - multi-agent
  - single-agent
  - sota
---

# Single agent + tools

## Method Overview
The method that **wins by default** on `task:multi-agent-orchestration` is *not using multi-agent*. Use one agent plus tools: `method:mini-swe-agent` (or CCA when notes are required). MAC: 5/39 meta-agent configs beat a human baseline; winners are simple ReAct. Illusion of MAS: auto MAS underperforms CoT-SC at up to 10× cost. Gao: MAS edge shrinks as models get stronger (tokens 4–220×); hybrid cascade +1.1–12pp when you actually need it.

When MAS actually wins: Anthropic June 2025 orchestrator-worker **+90.2%** vs single Opus 4 on *internal breadth research* (~15× tokens). AIME is the other MAS exception. CrewAI-default is theater.

## When to Use
- Always, unless you have a documented breadth-research or AIME-style exception.

## When NOT to Use
- Documented high-value parallel research → `method:anthropic-orchestrator-worker`.
- Still not for SWE patches, τ-bench, or sequential one-context work.

## Gotchas & Failure Modes
- Planner-coder-tester graphs for a single patch.
- Meta-agent search as default (2510.06711: prior-design context hurts; break-even 2 datasets at n>15k).
