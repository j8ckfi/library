---
id: method:mcp
type: method
title: "Model Context Protocol (MCP)"
category: "agent-protocol"
status: sota
sota_for:
  - task:agent-communication
supersedes: []
do_not_use_for:
  - when: "two independent vendor agents must negotiate"
    reason: "MCP is agent↔tool; A2A is agent↔agent"
    use_instead: "method:a2a-protocol"
  - when: "the model has weak or no native function calling"
    reason: "NLT helps open-weight / no-FC models"
    use_instead: "method:nlt"
  - when: "LLM-generating AGENTS.md as the instruction protocol"
    reason: "ETH: LLM-generated files hurt; write them as a developer"
    use_instead: "method:mini-swe-agent"
  - when: "stuffing 40 MCP servers into a SWE loop as the design"
    reason: "the winning SWE design is bash ReAct, not a tool zoo"
    use_instead: "method:mini-swe-agent"
assumptions:
  - "Spec 2026-07-28 stateless core. Vertical agent↔tool. Not a benchmark."
last_reviewed: "2026-09-01"
papers:
  - paper:mcp
  - paper:agents-md-ctxbench
  - paper:nlt
  - paper:tau-bench
recipes:
  - recipe:mcp
claims:
  - benchmark: "MCP specification snapshot"
    metric: "stateless core"
    value: "2026-07-28"
    baseline: "stateful session-oriented / per-vendor plugin transports"
    date: "2026-07"
    verified: true
    evidence_level: "self-reported"
    source_url: "https://blog.modelcontextprotocol.io"
    notes: "Spec, not a bench. evidence_level is the spec (encoded as self-reported)."
  - benchmark: "τ-bench, gpt-4o native function calling"
    metric: "pass^1"
    value: "61.2% retail / 35.2% airline"
    baseline: "text ReAct (native FC wins for FC-trained models)"
    date: "2024-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2406.12045"
    notes: "Routing: native FC if the model was trained for it; NLT for weak/no-FC."
  - benchmark: "ETH AGENTS.md (how to put instructions on disk)"
    metric: "Lite / CTXbench / cost"
    value: "LLM-generated −0.5pp Lite / −2pp CTXbench / +20% cost; developer vs LLM +7pp avg p=0.038"
    baseline: "LLM-generated AGENTS.md"
    date: "2026-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2602.11988"
    notes: "Human AGENTS.md. Do not LLM-/init. SKILL.md (agentskills.io) complementary."
tags:
  - agents
  - agent-protocol
  - mcp
  - sota
---

# Model Context Protocol (MCP)

## Method Overview
MCP is how agents talk to **tools**. Spec 2026-07-28 stateless core (`https://blog.modelcontextprotocol.io`). Vertical. Not a SWE-bench number.

**Agent↔agent:** `method:a2a-protocol` v1.0 only when two independent agents negotiate across vendors.

**Instructions on disk:** human AGENTS.md (ETH 2602.11988). Do not LLM-generate. SKILL.md progressive disclosure is complementary.

**Structured vs NL:** native function calling if the model was trained for it (τ-bench); NLT (`method:nlt`) for weak/no-FC. CodeAct lives on the OpenHands card.

## When to Use
- Default agent↔tool protocol.

## When NOT to Use
- Agent↔agent across vendors → `method:a2a-protocol`.
- Weak FC models → `method:nlt`.
- SWE design = 40 MCP servers → `method:mini-swe-agent`.

## Gotchas & Failure Modes
- Spec claim is not a leaderboard. Do not invent MCP SWE-bench numbers.
