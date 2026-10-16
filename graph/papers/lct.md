---
id: paper:lct
type: paper
title: 'LCT: Losslessly Compressed Tensors with GPU friendly execution for Training'
authors:
- Max Zhu
- Bohang Sun
- Pietro Lio
- Jialin Yu
year: 2026
month: 10
arxiv_id: '2610.22179'
url: https://arxiv.org/abs/2610.22179
methods:
- method:lct
cites:
- paper:scale
tags:
- efficiency
- memory
---

# LCT

## Abstract Summary
Lossless tensor compression only helps training if encode/decode is cheap on every step. LCT uses Huffman with precomputed codebooks on GPU for weights, activations, and optimizer states, and characterizes storage under magnitude shifts.

## Key Contributions
1. GPU Huffman tensors for the train loop.
2. Up to 1.455x compression.
3. NanoGPT from-scratch and Qwen3-4B FT.

## Empirical Highlights
- NanoGPT 162M: -24.6% memory, +7.2% step-time.
- Qwen3-4B FT: -23.8% peak, enabling 3.5x context on the same GPU.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22179`
- Code: `none found` (`code_status: none`).

