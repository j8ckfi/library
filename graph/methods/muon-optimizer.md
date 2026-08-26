---
id: method:muon-optimizer
type: method
title: "Muon Optimizer (Momentum Orthogonalized by Newton-Schulz)"
category: "optimizer"
status: sota
sota_for:
  - task:llm-pretraining-optimization
supersedes:
  - method:adamw-optimizer
papers:
  - paper:muon-optimizer-paper
recipes:
  - recipe:muon-pretraining
claims:
  - benchmark: "FineWeb-Edu NanoGPT (1.5B tokens)"
    metric: "validation loss"
    value: 3.21
    baseline: "AdamW (3.28 at equal steps, 2x wallclock training time)"
    date: "2025-02"
    verified: true
    notes: "Applied strictly to 2D matrix weights (attention/MLP projections); embeddings and RMSNorm use AdamW."
tags:
  - optimizer
  - pretraining
  - second-order
  - orthogonalization
---

# Muon Optimizer (Momentum Orthogonalized by Newton-Schulz)

## Method Overview
Muon (Momentum Orthogonalized by Newton-Schulz) is an optimizer designed specifically for 2D internal weight matrices in neural networks. While standard optimizers like AdamW perform coordinate-wise scaling based on second-moment gradient statistics, Muon applies matrix-level orthogonalization to the accumulated momentum matrix \(G_t\).

The algorithm calculates the nearest orthogonal matrix \(O \approx G_t (G_t^T G_t)^{-1/2}\) using a fast, hardware-friendly Newton-Schulz polynomial iteration:
\[
X_{k+1} = \frac{1}{2} X_k (3I - X_k^T X_k)
\]
This iteration runs entirely in FP32 / BF16 tensor core matrix multiplications without explicit SVD decompositions.

## When to Use
- **Large Transformer Pretraining**: Highly recommended for transformer internal linear weights (query, key, value, output projections, and MLP gate/up/down matrices).
- **Compute-Bound Training**: When target loss must be reached with minimum GPU hours and token count.
- **Combined Hybrid Setup**: Use Muon for 2D weight matrices (\(\geq 2\) dimensions) and AdamW for 1D vectors (embeddings, biases, RMSNorm scale factors).

## Gotchas & Failure Modes
1. **1D Weights & Embeddings**: Muon must NOT be applied to 1D vectors or large embedding lookup tables. Use standard AdamW for embedding layers.
2. **Learning Rate Scaling**: Muon updates have a fixed matrix spectral norm; learning rates are typically scaled differently (e.g. 0.02–0.05 for Muon vs 1e-3 for AdamW).
3. **Newton-Schulz Stability**: Ensure inputs to the Newton-Schulz iteration are normalized by their Frobenius or spectral norm estimate to prevent divergence.
