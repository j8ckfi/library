---
id: paper:codeact
type: paper
title: "Executable Code Actions Elicit Better LLM Agents"
authors:
  - "Xingyao Wang"
  - "Yangyi Chen"
  - "Lifan Yuan"
  - "Yizhe Zhang"
  - "Yunzhu Li"
  - "Hao Peng"
  - "Heng Ji"
year: 2024
month: 2
arxiv_id: "2402.01030"
url: "https://arxiv.org/abs/2402.01030"
methods:
  - method:openhands-codeact
cites: []
tags:
  - agents
  - agent-harness
  - codeact
---

# Executable Code Actions Elicit Better LLM Agents

## Abstract Summary
CodeAct uses executable Python/bash as the agent action space instead of JSON tool calls. GPT-4-1106: **74.4%** M3ToolEval vs JSON 52.4. This is the action-space paper behind OpenHands; it is not a separate SOTA method.

## Key Contributions
1. Code as actions (REPL) vs JSON tool-calling.
2. M3ToolEval: CodeAct GPT-4-1106 74.4% vs JSON 52.4.

## Empirical Highlights
- M3ToolEval, GPT-4-1106: CodeAct **74.4%** vs JSON **52.4**.
