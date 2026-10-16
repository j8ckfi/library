---
id: paper:mosaic
type: paper
title: 'Mosaic: Multi-Session Agentic Reinforcement Learning'
authors:
- Yilong Xu
- Minrui Xu
- Xinyu Zhou
- Xiang Long
- Haochen Tan
- Zhijiang Guo
year: 2026
month: 10
arxiv_id: '2610.22174'
url: https://arxiv.org/abs/2610.22174
methods:
- method:mosaic
cites:
- paper:sao
- paper:iris
tags:
- agentic
- async-rl
- multi-session
---

# Mosaic

## Abstract Summary
Context compaction and subagent forking span multiple sessions, but most agentic RL still broadcasts one trajectory advantage. Mosaic adds session-usage signals at the trajectory level and shapes each session by estimated marginal contribution.

## Key Contributions
1. Multi-session agentic RL setting (arbitrary session count per trajectory).
2. Session-aware trajectory advantage plus type-normalized session shaping.
3. BrowseComp with Qwen3.5-4B under compaction and subagent forking.

## Empirical Highlights
- Compaction: 38.86 vs broadcast 35.31, sessions 3.17→2.35 (up to 10.1% relative).
- Subagent: 32.46 vs broadcast 31.44, sessions 4.43→3.77.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22174`
- Code: `https://github.com/LARK-AI-Lab/Mosaic` (`code_status: released`).
- Project: `https://lark-ai-lab.github.io/Mosaic/`

