---
id: paper:delora
type: paper
title: "DeLoRA: Decoupled Low-Rank Adaptation for Stable Fine-Tuning"
authors:
  - "ExplainableML Research"
year: 2025
month: 3
arxiv_id: "2503.18225"
url: "https://arxiv.org/abs/2503.18225"
methods:
  - method:delora
cites:
  - paper:dora-paper
tags:
  - peft
  - low-rank
  - delora
---

# DeLoRA: Decoupled Low-Rank Adaptation for Stable Fine-Tuning

## Abstract Summary
DeLoRA bounds the Frobenius norm of adapter updates across layers, providing extreme stability over long training schedules and high learning rates compared to DoRA and LoRA.

## Open Source Repository
- Implementation: `https://github.com/ExplainableML/DeLoRA` (PEFT `DeloraConfig`)
