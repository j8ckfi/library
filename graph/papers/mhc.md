---
id: paper:mhc
type: paper
title: "mHC: Manifold-Constrained Hyper-Connections"
authors:
  - "Zhenda Xie"
  - "Yixuan Wei"
  - "Huanqi Cao"
  - "Chenggang Zhao"
  - "Chengqi Deng"
  - "Jiashi Li"
  - "Damai Dai"
  - "Huazuo Gao"
  - "Jiang Chang"
  - "Kuai Yu"
  - "Liang Zhao"
  - "Shangyan Zhou"
  - "Zhean Xu"
  - "Zhengyan Zhang"
  - "Wangding Zeng"
  - "Shengding Hu"
  - "Yuqing Wang"
  - "Jingyang Yuan"
  - "Lean Wang"
  - "Wenfeng Liang"
year: 2025
month: 12
arxiv_id: "2512.24880"
url: "https://arxiv.org/abs/2512.24880"
methods:
  - method:mhc
cites: []
tags:
  - architecture
  - hyper-connections
  - residual-stream
  - pretraining
  - mhc
---

# mHC: Manifold-Constrained Hyper-Connections

## Abstract Summary
Manifold-Constrained Hyper-Connections (mHC) addresses the training instability and signal explosion of unconstrained Hyper-Connections (HC). By expanding the residual stream to \(n \times d\) and projecting learnable residual mixing matrices onto the Birkhoff polytope (the manifold of doubly stochastic matrices) via the Sinkhorn-Knopp algorithm, mHC preserves the identity-mapping property across arbitrary depth.

## Key Contributions
1. **Manifold Constraint on Residual Space**: Uses the Sinkhorn-Knopp algorithm to project residual mixing matrices \(\mathcal{H}_l^{\text{res}}\) onto the Birkhoff polytope, ensuring row and column sums equal 1 so the operation acts as a convex combination of features.
2. **Identity Mapping Preservation**: Maintains signal mean invariance and bounds the spectral norm by 1 across forward and backward signal propagation through deep architectures.
3. **Infrastructure & Kernel Optimization**: Implements high-performance fused kernels in TileLang, with selective recomputation and communication overlap in the DualPipe schedule to minimize memory access overhead.
4. **Adoption at Scale**: Forms a core structural foundation for deep architectures including DeepSeek-V4 (\(n=4\)).
