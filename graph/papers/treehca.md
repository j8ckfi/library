---
id: paper:treehca
type: paper
title: 'TreeHCA: Hindsight-Guided Exploration and Credit Assignment for Multi-Turn LLM Agents'
authors:
- Debajoy Mukherjee
- Jeremy Carleton
- Sushil Vemuri
- Srinivas Shakkottai
- Dileep Kalathil
year: 2026
month: 10
arxiv_id: '2610.12828'
url: https://arxiv.org/abs/2610.12828
methods:
- method:treehca
cites:
- paper:canopy
- paper:pact
tags:
- post-training
- agentic
- credit-assignment
- treehca
---

# TreeHCA: Hindsight-Guided Exploration and Credit Assignment for Multi-Turn LLM Agents

## Abstract Summary
GRPO smears one advantage over every token. Hindsight credit needs informative alternatives at consequential histories. TreeHCA revisits intermediate histories when reference-answer likelihood changes, samples alternative continuations (a tree of reasoning and tool calls), applies inverse-hindsight importance correction including a finite-pool identity, and backups terminals into turn-level advantages.

## Key Contributions
1. Paired hindsight-guided exploration and hindsight credit.
2. Inverse-hindsight IS with an exact finite-pool identity.
3. Normalized tree backup to turn-level advantages; best aggregate EM on seven QA benches.

## Empirical Highlights
- See `method:treehca` claims (`as_of` 2026-10-12).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.12828`
- Code: `https://github.com/TheBlackCat22/TreeHCA` (`code_status: announced`).
