---
id: paper:agenttune
type: paper
title: 'AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents'
authors:
- R E Zera Marveen Lyngkhoi
- Abhivansh Gupta
- Vidushee Vats
- Ram Mohan Rao Kadiyala
- Vinay Kumar Sankarapu
- Pratinav Seth
year: 2026
month: 10
arxiv_id: '2610.13335'
url: https://arxiv.org/abs/2610.13335
methods:
- method:agenttune
cites:
- paper:sao
- paper:miles
tags:
- agents
- tool-use
- training-systems
- agenttune
---

# AgentTune: A Unified Training Lifecycle for Tool-Using LLM Agents

## Abstract Summary
Tool-using agent stacks split build / train / eval / distill / maintain across incompatible representations. AgentTune is a source-available Python library whose two-tier EventLog keeps trajectories and projects them consistently for those stages, with a shared runtime, tool-calling RL, agentic distillation, RAG, workflows, eval, and a designed self-healing path.

## Key Contributions
1. Two-tier EventLog as the shared substrate.
2. Composable train / distill / eval / recovery interfaces.
3. Released Lexsi-Labs/AgentTune.

## Empirical Highlights
- See `method:agenttune` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13335`
- Code: `https://github.com/Lexsi-Labs/AgentTune` (`code_status: released`).
