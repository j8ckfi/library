---
id: paper:hierarchical-moe-routing-control
type: paper
title: "Structuring MoE Expert Selection for Agentic Reinforcement Learning"
authors:
  - Bolian Li
  - Ting-Yao Hu
  - Cheng-Yu Hsieh
  - Sanjoy Chowdhury
  - Oncel Tuzel
  - Raviteja Vemulapalli
year: 2026
month: 10
arxiv_id: "2610.07332"
url: "https://arxiv.org/abs/2610.07332"
methods:
  - method:hierarchical-moe-routing-control
cites:
  - paper:esrl
  - paper:rpb
tags:
  - post-training
  - moe
  - routing
  - agentic
  - hierarchical-moe-routing-control
---

# Structuring MoE Expert Selection for Agentic Reinforcement Learning

## Abstract Summary
Agentic RL on MoE wastes capacity when routing ignores operation type (tool call vs plan vs observation). Hierarchical routing control aligns experts with agent operation types and constrains routing during RL. >10-point success on AppWorld / AutomationBench with Qwen3-30B-A3B. Active beside ESRL / RPB. Mention on outcome-only agent RL. Does not replace SAPO, ESRL, RPB, or CANOPY.

## Key Contributions
1. **Operation-type expert alignment** for agentic MoE RL.
2. **Constrain routing during RL** rather than only at pretrain.
3. **>10-point success** on AppWorld / AutomationBench.

## Empirical Highlights
- Qwen3-30B-A3B. Not a SAPO bake-off.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07332`
- Code: none found as of 2026-10-07 (`code_status: none`).
