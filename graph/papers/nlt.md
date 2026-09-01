---
id: paper:nlt
type: paper
title: "Natural Language Tools: A Natural Language Approach to Tool Calling In Large Language Agents"
authors:
  - "Reid T. Johnson"
  - "Michelle D. Pain"
  - "Jordan D. West"
year: 2025
month: 10
arxiv_id: "2510.14453"
url: "https://arxiv.org/abs/2510.14453"
methods:
  - method:nlt
  - method:mcp
cites: []
tags:
  - agents
  - agent-protocol
  - nlt
  - tool-calling
---

# Natural Language Tools: A Natural Language Approach to Tool Calling In Large Language Agents

## Abstract Summary
NLT describes tools in natural language rather than native function-calling schemas. **69.1 → 87.5 (+18.4pp)**, especially for open-weight models. Replication 2607.03953: **+14.9pp**; frontier FC-trained models show smaller or reversed gains. Routing: native function calling if the model was trained for it; NLT for weak/no-FC. Niche, not a third SOTA next to MCP.

τ-bench (2406.12045) gpt-4o: function-calling **61.2%** retail / **35.2%** airline; native FC beats text ReAct for FC-trained models.

## Key Contributions
1. Natural-language tool descriptions as an alternative to native FC JSON.
2. Large gains on weak/no-FC open-weight models; smaller/reversed on frontier FC models.
3. Routing rule encoded on `method:nlt` / `method:mcp`.

## Empirical Highlights
- NLT: 69.1 → **87.5** (+18.4pp).
- Replication 2607.03953: +14.9pp. Source: https://arxiv.org/abs/2607.03953
- τ-bench gpt-4o FC: 61.2% retail / 35.2% airline (https://arxiv.org/abs/2406.12045).
