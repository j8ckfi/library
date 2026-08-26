---
id: paper:muon-scalable
type: paper
title: "Scaling Laws for Momentum Orthogonalized by Newton-Schulz"
authors:
  - "Moonshot AI Team"
year: 2025
month: 2
arxiv_id: "2502.16982"
url: "https://arxiv.org/abs/2502.16982"
methods:
  - method:muon-scalable
cites:
  - paper:muon-optimizer-paper
tags:
  - optimizer
  - pretraining
  - scale-up
---

# Scaling Laws for Momentum Orthogonalized by Newton-Schulz

## Abstract Summary
This paper from Moonshot AI establishes formal scaling laws for Muon in large-scale LLM pretraining. It introduces two crucial corrections: proper weight decay formulation and per-parameter update-RMS matching, proving that Muon is ~2x more token-efficient than tuned AdamW.

## Open Source Repository
- Implementation: `https://github.com/MoonshotAI/Moonlight`
