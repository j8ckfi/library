---
id: method:nlt
type: method
title: "Natural Language Tools (NLT)"
category: "agent-protocol"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "the model was trained for native function calling"
    reason: "τ-bench: native FC beats text ReAct for FC-trained models; NLT gains shrink or reverse at the frontier"
    use_instead: "method:mcp"
assumptions:
  - "Niche. Not a third SOTA. 69.1→87.5 especially open-weight; replication +14.9pp."
last_reviewed: "2026-09-01"
papers:
  - paper:nlt
  - paper:tau-bench
claims:
  - benchmark: "NLT paper tool-calling"
    metric: "accuracy"
    value: 87.5
    baseline: "69.1 (+18.4pp)"
    date: "2025-10"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2510.14453"
    notes: "Especially open-weight. Frontier FC models smaller/reversed."
  - benchmark: "NLT replication (2607.03953, 14 models)"
    metric: "mean gain"
    value: "+14.9pp"
    baseline: "native FC / JSON tools"
    date: "2026-07"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2607.03953"
    notes: "Replication. Frontier FC models smaller or reversed."
tags:
  - agents
  - agent-protocol
  - nlt
  - niche
---

# Natural Language Tools (NLT)

## Method Overview
Describe tools in natural language instead of native FC JSON. Niche on `task:agent-communication`. Routing: native FC if the model was trained for it; NLT for weak/no-FC. Not a third SOTA next to MCP.

## When to Use
- Open-weight or no-FC models.

## When NOT to Use
- FC-trained frontier models → `method:mcp` / native FC.
