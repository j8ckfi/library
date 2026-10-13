---
id: paper:terminalhorizon
type: paper
title: Scaling Agentic Data for Long-Horizon Terminal Intelligence
authors:
- Shun Zou
- Ziyu Ma
- Yi Zou
- Yong Wang
- Lin Chen
- Zehui Chen
- Guanhua Chen
- Xiangxiang Chu
- Feng Zhao
year: 2026
month: 10
arxiv_id: '2610.13166'
url: https://arxiv.org/abs/2610.13166
methods:
- method:terminalhorizon
cites:
- paper:t1-terminal-rl
- paper:codemidas
tags:
- post-training
- terminal-agents
- environments
- terminalhorizon
---

# Scaling Agentic Data for Long-Horizon Terminal Intelligence

## Abstract Summary
TerminalHorizon is a data engine for long-horizon terminal agents: 1,535 environments, 2,852 trajectories, average 52.8 turns. It detects pre-completed work, rebuilds the env, and expands in stages. SFT of Qwen3.5-27B lifts Terminal-Bench, AutomationBench, tau2, VitaBench, and keeps math. Plug-in on `task:coding-agent-rl-environment-construction` beside CodeMidas; link `method:t1-terminal-rl`.

## Key Contributions
1. Terminal env factory that detects pre-completed work and rebuilds the sandbox.
2. Staged expansion to 1,535 envs / 2,852 trajectories (avg 52.8 turns).
3. SFT Qwen3.5-27B transfer across terminal, automation, and tau2 benches.

## Empirical Highlights
- Terminal-Bench 1.0 55.0 (+8.7); TB2.0 55.8 (+14.2); TB2.1 46.82→60.67 (+13.85).
- AutomationBench Pass 5.5→17.2 / Partial 26.4→49.7.
- tau2 Airline 79.0→84.5; Retail 84.9→87.5; VitaBench 20.5→31.8.
- MATH-500 96.9→98.9; GSM8K 96.3→97.3; AIME24 93.3→96.7; AIME25 86.7→93.3; KOR-Bench Cipher 90.1→91.2.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13166`
- Project: `https://zs1314.github.io/TerminalHorizon`
- Code: `none found` (`code_status: none`).
