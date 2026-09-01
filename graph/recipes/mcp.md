---
id: recipe:mcp
type: recipe
title: "MCP stateless tool server"
method: method:mcp
task: task:agent-communication
target_hardware: "CPU; local stdio or HTTP transport"
framework: "Python / MCP SDK"
repo_url: "https://github.com/modelcontextprotocol/python-sdk"
pip_dependencies:
  - "mcp"
tags:
  - recipe
  - agents
  - mcp
---

# MCP stateless tool server

Spec: 2026-07-28 stateless core. This is agent↔tool, not a SWE harness and not A2A.

## Hardware & Environment Setup
- `pip install mcp`
- Write AGENTS.md by hand. Do not LLM-init (ETH 2602.11988).

## Quickstart Implementation

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("demo")


@mcp.tool()
def echo(text: str) -> str:
    return text


if __name__ == "__main__":
    mcp.run()
```

## Critical Hyperparameters & Tuning Advice
- **Native FC** if the model was trained for it; **NLT** for weak/no-FC.
- Do not stuff 40 MCP servers into mini-SWE-agent.
- Agent↔agent across vendors → A2A, not MCP.
