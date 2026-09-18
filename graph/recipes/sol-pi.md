---
id: recipe:sol-pi
type: recipe
title: "SoL-Pi Pi Extension"
method: method:sol-pi
task: task:agent-harness-runtime
target_hardware: "CPU host running Pi; model calls billed to the configured provider"
framework: "Node.js 22.19+ / Pi coding agent 0.85.1"
repo_url: "https://github.com/NVlabs/SoL-Pi"
pip_dependencies: []
tags:
  - recipe
  - sol-pi
  - agent-harness
  - pi
---

# SoL-Pi Pi Extension

## Hardware & Environment Setup
- Official extension: `https://github.com/NVlabs/SoL-Pi`. Project page: `https://nvlabs.github.io/SoL-Pi/`.
- Requires Node.js 22.19+ and `@earendil-works/pi-coding-agent@0.85.1`.
- Production kernel spec stays omp². SWE loop stays mini-SWE-agent. Routing-harness post-train stays NeoHorse-1.

```bash
npm install --global @earendil-works/pi-coding-agent@0.85.1
pi install git:github.com/NVlabs/SoL-Pi
```

Config search order: `.pi/sol-pi.json` in a trusted project, else `~/.pi/agent/sol-pi.json`. Files are not merged.

## Quickstart Implementation

```python
from __future__ import annotations

from typing import Any


def conservative_sol_pi_config() -> dict[str, Any]:
    """Local mechanisms only: no extra model calls, does not stop an active run."""
    return {
        "version": 1,
        "actionFusion": True,
        "observationPack": True,
        "evidencePreservingReducer": False,
        "onlineContextCompact": False,
        "cacheWriteReadRatio": 12.5,
    }


def enable_all_sol_pi() -> dict[str, Any]:
    cfg = conservative_sol_pi_config()
    cfg["evidencePreservingReducer"] = True
    cfg["onlineContextCompact"] = True
    return cfg
```

Write the dict as `sol-pi.json`. Review `SECURITY.md` before enabling the reducer.

## Critical Hyperparameters & Tuning Advice
- Start with Action Fusion + ObservationPack. Turn on reducer/compact only after reading config + security docs.
- `cacheWriteReadRatio` is a cost knob, not a quality knob.
- Cancelling a run does not auto-continue after Online Context Compact; compact commits a new turn on success.
