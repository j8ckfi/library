---
id: paper:mamba-2-paper
type: paper
title: "Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality"
authors:
  - "Tri Dao"
  - "Albert Gu"
year: 2024
month: 5
arxiv_id: "2405.21060"
url: "https://arxiv.org/abs/2405.21060"
methods:
  - method:mamba-2
cites: []
tags:
  - architecture
  - state-space
  - linear-attention
---

# Transformers are SSMs: Generalized Models and Efficient Algorithms Through Structured State Space Duality

## Abstract Summary
This paper introduces Structured State Space Duality (SSD), establishing an exact mathematical duality between structured state-space models (SSMs) and linear attention. Leveraging this theoretical framework, the authors develop Mamba-2, which replaces custom scan operations with block matrix multiplications executed natively on GPU Tensor Cores. Mamba-2 delivers up to 8x throughput improvements over FlashAttention-2 at large batch and sequence sizes while maintaining competitive modeling capacity.

## Key Contributions
1. **State Space Duality (SSD)**: Unified theoretical bridge connecting continuous SSMs and discrete linear attention.
2. **Hardware-Efficient Tensor-Core Algorithm**: Formulates chunked SSD computation as standard matrix multiplications.
3. **Mamba-2 Architecture**: Hybrid multi-head SSM blocks scaling efficiently across billions of parameters.
