---
id: paper:lambda-rlm
type: paper
title: "The Y-Combinator for LLMs: Solving Long-Context Rot with λ-Calculus"
authors:
  - "Amartya Roy"
  - "Rasul Tutunov"
  - "Xiaotong Ji"
  - "Matthieu Zimmer"
  - "Haitham Bou-Ammar"
year: 2026
month: 3
arxiv_id: "2603.20105"
url: "https://arxiv.org/abs/2603.20105"
methods:
  - method:lambda-rlm
cites:
  - paper:rlm
tags:
  - agents
  - agent-recursion
  - lambda-rlm
---

# The Y-Combinator for LLMs: Solving Long-Context Rot with λ-Calculus

## Abstract Summary
λ-RLM is a niche recursive offload variant on the RLM shelf. It does not replace `method:rlm` as the dumped-prompt default. Depth >1 is still not the working setting.

## Key Contributions
1. λ-calculus / Y-combinator framing of recursive LM calls for long-context rot.
2. Niche alternative on `task:long-context-prompt-offload`.

## Empirical Highlights
- Niche status; RLM remains current_sota. No additional numbers recorded beyond the RLM card.
