---
id: paper:rao
type: paper
title: "Recursive Agent Optimization"
authors:
  - "Apurva Gandhi"
  - "Satyaki Chakraborty"
  - "Xiangjun Wang"
  - "Aviral Kumar"
  - "Graham Neubig"
year: 2026
month: 5
arxiv_id: "2605.06639"
url: "https://arxiv.org/abs/2605.06639"
methods:
  - method:rao
cites: []
tags:
  - agents
  - agent-recursion
  - rao
---

# Recursive Agent Optimization

## Abstract Summary
RAO *trains* a recursive agent (root + children). TextCraft-Synth 8K: single-agent **24%** vs recursive **95%**. This is trained recursion, not a drop-in RLM replacement and not FoldGRPO context-folding.

## Key Contributions
1. Train-time recursive agent (root + children) rather than inference-only REPL offload.
2. TextCraft-Synth 8K: 24% single-agent vs 95% recursive.

## Empirical Highlights
- TextCraft-Synth 8K: single-agent **24%** vs recursive **95%**.
