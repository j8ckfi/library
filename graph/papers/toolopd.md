---
id: paper:toolopd
type: paper
title: 'ToolOPD: Credit-Aware On-Policy Distillation for Tool-Use Agents'
authors:
- 'Chu Zhao'
- 'Lei Tang'
- 'Yanming Wang'
- 'Jianzhe Zhao'
- 'Guibing Guo'
- 'Zhengzong Chen'
- 'Yuanyuan Zhao'
- 'Fei Huang'
year: 2026
month: 10
arxiv_id: '2610.25693'
url: https://arxiv.org/abs/2610.25693
methods:
- method:toolopd
cites:
- paper:opd
- paper:slca-grpo
tags:
- distillation
- opd
- tool-use
- active
---

# ToolOPD

## Abstract Summary
Uniform OPD over a long tool trajectory misassigns credit. ToolOPD induces outcome-conditioned hindsight skills, scores action-level relevance asymmetrically, and jointly optimizes action-token OPD with GRPO.

## Key Contributions
1. Outcome-asymmetric action-token OPD for tool-use agents.

## Empirical Highlights
- Even with a fixed trajectory, reversing the final outcome reallocates credit across turns.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.25693`
- Code: `https://github.com/MagicAgent-Search/ToolOPD` (`code_status: released`).
