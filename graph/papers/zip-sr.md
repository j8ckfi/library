---
id: paper:zip-sr
type: paper
title: "Rounding in Preconditioner Space: Redesigning 4-bit AdamW Optimizer-State Quantization"
authors:
  - "Hanyang Li"
  - "Shao Tang"
  - "Daniel Thomas Braithwaite"
  - "Gregory Dexter"
  - "Leonardo Neves"
  - "Aman Gupta"
  - "Hiroto Udagawa"
  - "Abhishek Shivanna"
  - "Daniel Silva"
  - "Rohan Ramanath"
year: 2026
month: 10
arxiv_id: "2610.12444"
url: "https://arxiv.org/abs/2610.12444"
methods:
  - method:zip-sr
cites:
  - paper:muon2
tags:
  - optimizer
  - quantization
  - adamw
  - 4bit
  - zip-sr
---

# Rounding in Preconditioner Space: Redesigning 4-bit AdamW Optimizer-State Quantization

## Abstract Summary
4-bit AdamW optimizer states save memory, but quantization error feeds the moment recurrences. ZIP-SR keeps zero in the second-moment codebook and computes stochastic-rounding probabilities in preconditioner space rather than state space. Sibling ZE-EDEN uses a zero-excluding codebook and rescales the quantized second-moment block. Both use NF4 on the first moment. Across GPT/Llama-style pretrain 130M-2.7B, both cut TorchAO 4-bit AdamW's mean val-loss gap to 32-bit AdamW at every size; largest reported gap reduction 70%. Beside Muon2 / SCALE. No official GitHub as of 2026-10-09.

## Key Contributions
1. Rounding space matters: small state error is not small next-step preconditioner error near zero.
2. ZIP-SR: zero-inclusive second-moment codebook, stochastic rounding in preconditioner space.
3. ZE-EDEN sibling: zero-excluding codebook plus block rescale.

## Empirical Highlights
- GPT- and Llama-style pretrain 130M-2.7B: both methods reduce TorchAO 4-bit AdamW val-loss gap to 32-bit AdamW at every size.
- Largest reported gap reduction 70%. Full-param SFT also closer to 32-bit AdamW than TorchAO.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.12444`
- Code: none found as of 2026-10-09 (`code_status: none`).
