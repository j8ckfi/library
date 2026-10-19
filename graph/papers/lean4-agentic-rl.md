---
id: paper:lean4-agentic-rl
type: paper
title: 'Lean4AgenticRL: Advancing Agentic RL with Verifiable Multi-level Process Rewards'
authors:
- 'Ruida Wang'
- 'Gerald Friedland'
- 'Tong Zhang'
- 'Chris Kong'
year: 2026
month: 10
arxiv_id: '2610.22448'
url: https://arxiv.org/abs/2610.22448
methods:
- method:lean4-agentic-rl
cites:
- paper:canopy
tags:
- agent-rl
- lean4
- process-reward
- active
---

# Lean4AgenticRL

## Abstract Summary
Enhancing the agentic capabilities of Large Language Models (LLMs) to tackle complex software engineering (SWE) and general terminal-usage problems is a pressing challenge. Current state-of-the-art LLMs often go through large-scale agentic Reinforcement Learning (RL). However, they mostly rely on high-level outcome rewards, with minimal consideration of low-level toolcall and mid-level workflow-stage rewards, which makes the training less effective. To overcome this limitation, we propose **Lean4AgenticRL**, which, to the best of our knowledge, is the first framework that grounds multi-level process rewards in the unified Lean4 formalization schema for open-ended agentic RL. **Lean4AgenticRL

## Key Contributions
1. Lean4AgenticRL grounds toolcall, workflow-stage, and outcome rewards in a unified Lean4 schema, then trains with workflow-stage-normalized GRPO so open-ended SWE/terminal agents get verifiable process credit.

## Empirical Highlights
- TB2.1 77.3%; +9.89 vs base; +5.07 vs second-best same-size

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22448`
- Code: `none found` (`code_status: none`).
