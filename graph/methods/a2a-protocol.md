---
id: method:a2a-protocol
type: method
title: "Agent2Agent Protocol (A2A) v1.0"
category: "agent-protocol"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "agent talking to tools"
    reason: "A2A is agent↔agent; MCP is agent↔tool"
    use_instead: "method:mcp"
  - when: "a single SWE agent looping in one repo"
    reason: "two-vendor negotiation is not a patch loop"
    use_instead: "method:mini-swe-agent"
assumptions:
  - "a2a-protocol.org v1.0. Only when two independent agents negotiate across vendors."
last_reviewed: "2026-09-01"
papers:
  - paper:mcp
claims:
  - benchmark: "A2A protocol v1.0"
    metric: "scope"
    value: "agent↔agent across vendors"
    baseline: "MCP agent↔tool"
    date: "2026-09"
    verified: true
    evidence_level: "self-reported"
    source_url: "https://a2a-protocol.org"
    notes: "Active, not SOTA. Spec, not a bench."
tags:
  - agents
  - agent-protocol
  - a2a
---

# Agent2Agent Protocol (A2A) v1.0

## Method Overview
A2A v1.0 (`https://a2a-protocol.org`) is agent↔agent. Use only when two independent agents negotiate across vendors. Default tool protocol remains MCP.

## When to Use
- Cross-vendor agent negotiation.

## When NOT to Use
- Tools → `method:mcp`. Single SWE loop → `method:mini-swe-agent`.
