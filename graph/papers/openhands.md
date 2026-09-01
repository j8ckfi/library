---
id: paper:openhands
type: paper
title: "OpenHands: An Open Platform for AI Software Developers as Generalist Agents"
authors:
  - "Xingyao Wang"
  - "Boxuan Li"
  - "Yufan Song"
  - "Frank F. Xu"
  - "Xiangru Tang"
  - "Mingchen Zhuge"
  - "Jiayi Pan"
  - "Yueqi Song"
year: 2024
month: 7
arxiv_id: "2407.16741"
url: "https://arxiv.org/abs/2407.16741"
methods:
  - method:openhands-codeact
cites:
  - paper:codeact
tags:
  - agents
  - agent-harness
  - openhands
---

# OpenHands: An Open Platform for AI Software Developers as Generalist Agents

## Abstract Summary
OpenHands is the production open-source software-engineering agent platform. It uses CodeAct (code/bash as actions). Official SWE-bench JSON: OpenHands+GPT-5 **71.8%** Verified. Active alternative to mini-SWE-agent when you need a full OSS product, not the default ~100-line loop.

## Key Contributions
1. Open platform for generalist software-engineering agents.
2. CodeAct action space (executable code) rather than JSON tool schemas.
3. Production OSS used as a competitive baseline on SWE-bench Verified.

## Empirical Highlights
- Official JSON OpenHands+GPT-5: **71.8%** SWE-bench Verified.
- Equal-model CCA comparison (Claude 4 Sonnet Verified): OpenHands 72.8 vs CCA 74.6 vs SWE-agent 66.6.

## Open Source
- `https://github.com/All-Hands-AI/OpenHands`
