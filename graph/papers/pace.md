---
id: paper:pace
type: paper
title: 'PACE: Periodic and Channel-Aligned Encoding of Four-Bit Recurrent States'
authors:
- 'Patrick Haller'
- 'Filipe Laitenberger'
- 'Alan Akbik'
year: 2026
month: 10
arxiv_id: '2610.29545'
url: https://arxiv.org/abs/2610.29545
methods:
- method:pace
cites:
- paper:mamba-2-paper
tags:
- ssm
- quantization
- active
---

# PACE

## Abstract Summary
PACE stores linear-attention recurrent state in four bits but rounds only every few generated tokens, keeping the intervening tokens in a small buffer the way chunked prefill kernels already do.

## Key Contributions
1. PACE as an active plug-in on `task:linear-time-sequence-modeling`.

## Empirical Highlights
- mixed 4/8-bit heads competitive with 8-bit DAMP at about two thirds the memory on the three larger models; 4-bit throughout beats Q-Mamba at equal memory. Does not retarget `method:mamba-2`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.29545`
- Code: `none found` (`code_status: none`).
