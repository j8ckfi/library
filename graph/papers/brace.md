---
id: paper:brace
type: paper
title: 'Measure First, Then Allocate: Calibrated Rollout Budgets for MCP Agents in Reinforcement Learning'
authors:
- 'Hieu Tran'
- 'Zonghai Yao'
- 'Sunjae Kwon'
- 'Hong Yu'
year: 2026
month: 10
arxiv_id: '2610.28785'
url: https://arxiv.org/abs/2610.28785
methods:
- method:brace
cites:
- paper:sao
tags:
- agentic-rl
- mcp
- active
---

# BRACE

## Abstract Summary
BRACE forecasts mixed-reward GRPO groups from a historical bank, per-task uncertainty, and a correlated reward model before spending new MCP rollouts. Discord is the paired-inference harness test that only counts disagreeing outcomes.

## Key Contributions
1. BRACE as an active plug-in on `task:agentic-async-rl`.

## Empirical Highlights
- exceeds strongest plotted baseline peaks with fewer new training rollouts; leads compared methods on BFCL and NESTFUL without further training. Does not retarget `method:sao`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28785`
- Code: `none found` (`code_status: none`).
