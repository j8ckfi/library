---
id: paper:dr-grpo
type: paper
title: "Understanding R1-Zero-Like Training: A Critical Perspective"
authors:
  - "SAIL & Singapore Research"
year: 2025
month: 3
arxiv_id: "2503.20783"
url: "https://arxiv.org/abs/2503.20783"
methods:
  - method:dr-grpo
cites:
  - paper:deepseek-math-paper
tags:
  - rl-alignment
  - reasoning
  - de-biasing
---

# Understanding R1-Zero-Like Training: A Critical Perspective

## Abstract Summary
Dr. GRPO analyzes R1-Zero-like training dynamics and identifies that length-normalization (1/|o|) and sample standard-deviation scaling introduce severe biases, causing models to favor unnecessarily verbose outputs. Removing these normalizations recovers stable, de-biased group advantage estimation.

## Open Source Repository
- Implementation: `https://github.com/sail-sg/understand-r1-zero`
