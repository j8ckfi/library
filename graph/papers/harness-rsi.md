---
id: paper:harness-rsi
type: paper
title: 'Self-Evolving Agent Harness'
authors:
- Chuyang Wei
- Haoxiang Guan
- Minghang Zhu
- Kexin Zhou
- Jiyan He
- Xiren Zhou
- Huanhuan Chen
- Yifei Shen
year: 2026
month: 10
arxiv_id: '2610.18813'
url: https://arxiv.org/abs/2610.18813
methods:
- method:harness-rsi
cites:
- paper:rrsi
- paper:aide2
- paper:activesaddler
tags:
- agent-harness
- rsi
---

# Harness RSI (Self-Evolving Agent Harness)

## Abstract Summary
Harness self-evolution revises prompts, memory, workflows, and executable components with weights frozen. The paper separates update targets from proposal/admission, distinguishes interpreted state from tools/code/control/plugins, and gives PAC bounds for admission on fresh validation data.

## Key Contributions
1. Formal Harness RSI framework with persistent accepted revisions.
2. Expected generalization, retention, and high-probability admission bounds.
3. Accompanying continuously updated code.

## Empirical Highlights
- Theory/framework paper; cases from prior work illustrate co-design and plugin reuse rather than a new SWE ranking.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.18813`
- Code: `https://github.com/zgcagi/Harness-RSI` (`code_status: released`).

