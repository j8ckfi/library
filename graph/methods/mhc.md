---
id: method:mhc
type: method
title: "mHC (Manifold-Constrained Hyper-Connections)"
category: "architecture"
status: active
papers:
  - paper:mhc
recipes:
  - recipe:mhc
claims:
  - benchmark: "Deep Architecture Scaling & Residual Stability"
    metric: "training stability & convergence"
    value: "Preserves identity mapping in n×d widened residual stream via doubly stochastic Sinkhorn projection"
    baseline: "Unconstrained Hyper-Connections"
    date: "2026-08-26"
    verified: true
    notes: "Projects residual mixing matrices onto Birkhoff polytope via Sinkhorn-Knopp; adopted in DeepSeek-V4 (n=4)."
tags:
  - architecture
  - hyper-connections
  - residual-stream
  - pretraining
  - mhc
---

# mHC (Manifold-Constrained Hyper-Connections)

## Method Overview
Manifold-Constrained Hyper-Connections (mHC) generalizes the standard residual stream by expanding its feature dimension from \(d\) to \(n \times d\) (with stream expansion rate \(n\), e.g., \(n=4\) in DeepSeek-V4) and enabling learnable inter-stream mixing matrices constrained to the Birkhoff polytope.

In standard Hyper-Connections (HC), unconstrained mixing across parallel streams destroys the identity-mapping property of residual connections, causing unbounded signal amplification or attenuation across deep layers. mHC resolves this by projecting the residual mixing matrix \(\mathcal{H}_l^{\text{res}} \in \mathbb{R}^{n \times n}\) to the manifold of doubly stochastic matrices using the Sinkhorn-Knopp algorithm.

Because row and column sums of doubly stochastic matrices equal 1:
- \(\mathcal{H}_l^{\text{res}} \mathbf{x}_l\) functions as a convex combination of stream representations.
- Global feature mean is conserved and spectral norms are bounded by 1.
- Matrix multiplication of doubly stochastic matrices is closed, preserving identity mapping across arbitrary depth \(L - l\).

Single-layer propagation is defined as:
\[
\mathbf{x}_{l+1} = \mathcal{H}_l^{\text{res}} \mathbf{x}_l + \mathcal{H}_l^{\text{post}\,\top} \mathcal{F}(\mathcal{H}_l^{\text{pre}} \mathbf{x}_l, \mathcal{W}_l)
\]
where \(\mathcal{H}_l^{\text{pre}} \in \mathbb{R}^{1 \times n}\) down-projects the \(n \times d\) stream to \(d\) for layer computation \(\mathcal{F}\), and \(\mathcal{H}_l^{\text{post}} \in \mathbb{R}^{1 \times n}\) maps the output back onto the stream.

## Distinction from AttnRes
- **mHC (`paper:mhc`, `2512.24880`)**: Widens the residual stream to \(n \times d\) and uses doubly stochastic static/learned manifold projections (Birkhoff polytope via Sinkhorn) to mix streams.
- **AttnRes (`paper:attnres`, `2603.15031`)**: Employs content-dependent dynamic attention mechanisms over prior layer activation histories.

## When to Use
- Pretraining deep transformer and MoE architectures (such as DeepSeek-V4) where widened residual topologies provide increased expressivity without destabilizing gradient flow.
- Mitigating gradient explosion or representation collapse in ultra-deep networks with multi-stream connections.
