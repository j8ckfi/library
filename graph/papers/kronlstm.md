---
id: paper:kronlstm
type: paper
title: 'Kronecker Delta Rule for Long Context Linear Attention'
authors:
- 'Anamaria-Roberta Hartl'
- 'Levente Zólyomi'
- 'Michael List'
- 'Günter Klambauer'
- 'Sebastian Böck'
- 'Sepp Hochreiter'
year: 2026
month: 10
arxiv_id: '2610.26834'
url: https://arxiv.org/abs/2610.26834
methods:
- method:kronlstm
cites:
- paper:mamba-2-paper
tags:
- linear-attention
- xlstm
- active
---

# Kronecker Delta Rule for Long Context Linear Attention

## Abstract Summary
KronLSTM revises associative memory along a single matrix-space direction (Kronecker Delta Rule), reducing interference versus delta-rule writes and keeping expected memory norm bounded without extra normalizers.

## Key Contributions
1. Kronecker Delta Rule for xLSTM-family linear attention. Previously skipped as an LSTM.

## Empirical Highlights
- Competitive with and often better than (Gated) DeltaNet-family models, especially on long context.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.26834`
- Code: `https://github.com/NX-AI/KronLSTM` (`code_status: released`).
