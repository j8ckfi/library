---
id: paper:mupace
type: paper
title: 'MuPACE: Learning to Pace Muon for LoRA Fine-Tuning'
authors:
- 'Jan Kobiolka'
- 'Christian Frey'
- 'Josif Grabocka'
year: 2026
month: 10
arxiv_id: '2610.28072'
url: https://arxiv.org/abs/2610.28072
methods:
- method:mupace
cites:
- paper:lr-matters-lora
- paper:muon2
tags:
- peft
- lora
- muon
- active
---

# MuPACE

## Abstract Summary
MuPACE leaves Muon's orthogonalized direction alone and meta-learns only the global step size with a recurrent policy that adjusts an analytic schedule from the observed LoRA trajectory.

## Key Contributions
1. Amortized Muon step-size policy for LoRA, transferred from 16-layer meta-train to 64-layer models.

## Empirical Highlights
- Wins 64-78% vs a strong shared default on 64 problems; one-shot transfer to Qwen3-32B / Qwen3.8-27B.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28072`
- Code: `none found` (`code_status: none`).
