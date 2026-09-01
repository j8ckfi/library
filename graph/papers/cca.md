---
id: paper:cca
type: paper
title: "Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases"
authors:
  - "Sherman Wong"
  - "Zhenting Qi"
  - "Zhaodong Wang"
  - "Nathan Hu"
  - "Samuel Lin"
  - "Jun Ge"
  - "Erwin Gao"
  - "Wenlin Chen"
year: 2025
month: 12
arxiv_id: "2512.10398"
url: "https://arxiv.org/abs/2512.10398"
methods:
  - method:cca
cites:
  - paper:mini-swe-agent
  - paper:openhands
tags:
  - agents
  - agent-harness
  - swe-bench
  - cca
---

# Confucius Code Agent: Scalable Agent Scaffolding for Real-World Codebases

## Abstract Summary
Confucius Code Agent (CCA) is a software-engineering agent scaffold with notes and context management beyond a bash-only loop. Evaluated at equal model/tools against SWE-agent and OpenHands. Use when a repo needs persistent notes, not as the default first hop (that remains mini-SWE-agent).

## Key Contributions
1. Agent-inside-container harness (facebookresearch/cca-swebench) rather than host-side runtime abstraction.
2. Equal-model/tools comparisons versus SWE-agent and OpenHands on SWE-Bench-Pro public and SWE-bench Verified.
3. Context/notes management for long-lived repo work.

## Empirical Highlights
- SWE-Bench-Pro public, Claude 4.5 Sonnet: CCA 52.7 vs SWE-agent 43.6.
- GPT-5.2 CCA 59.0 vs OpenAI proprietary 56.0 on the paper's reported split.
- SWE-bench Verified, Claude 4 Sonnet: CCA 74.6 vs OpenHands 72.8 vs SWE-agent 66.6.

## Open Source
- `https://github.com/facebookresearch/cca-swebench`
