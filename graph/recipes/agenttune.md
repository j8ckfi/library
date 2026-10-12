---
id: recipe:agenttune
type: recipe
title: AgentTune Unified Tool-Agent Lifecycle
method: method:agenttune
task: task:agentic-async-rl
target_hardware: 'Tool-using agent host; paper: legal/domain demos'
framework: Python AgentTune
repo_url: https://github.com/Lexsi-Labs/AgentTune
code_status: released
pip_dependencies:
- torch>=2.5.0
tags:
- recipe
- agenttune
---

# AgentTune Unified Tool-Agent Lifecycle

## Hardware & Environment Setup
- Official: `https://github.com/Lexsi-Labs/AgentTune`.
- `code_status: released` as of 2026-10-12.

## Quickstart Implementation

```python
from __future__ import annotations

def eventlog_has_both_tiers(raw_turns: list, projection: list) -> bool:
    if not raw_turns:
        raise ValueError("empty EventLog")
    return len(projection) <= len(raw_turns)
```

Keep one log, many projections. Do not retarget SAO.
