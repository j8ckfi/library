---
id: paper:dga-muon
type: paper
title: "DGA-Muon: Decoupled Geometry-Aligned Adaptive Scaling for Muon"
authors:
  - Wenpeng Zhang
  - Runsheng Yu
year: 2026
month: 10
arxiv_id: "2610.06578"
url: "https://arxiv.org/abs/2610.06578"
methods:
  - method:dga-muon
cites:
  - paper:sf-normuon
  - paper:muon2
tags:
  - pretraining
  - optimizer
  - muon
  - dga-muon
---

# DGA-Muon: Decoupled Geometry-Aligned Adaptive Scaling for Muon

## Abstract Summary
NorMuon's row-wise adaptive scaling is mostly orthogonalization geometry, not optimization-relevant information. Exact orthogonalization collapses the scale to one global scalar on square/wide matrices; tall-matrix variation is leftover row-energy after orthogonalization. Better orthogonalization can weaken adaptivity (Orthogonalization–Adaptivity Paradox). DGA-Muon decouples scaling from orthogonalization (raw-gradient second moments) and aligns it with polar-factor geometry (row-wise for wide, column-wise for tall), plus sum-based second moments, bias correction, and adaptive clipping. Convergence guarantees; empirical superiority over NorMuon. Active plug-in beside SF-NorMuon. No public code as of 2026-10-06.

## Key Contributions
1. **Diagnosis**: NorMuon adaptivity is mostly orthogonalization geometry.
2. **Decouple + align**: scale from raw gradients; row-wise wide / column-wise tall.
3. **DGA-Muon**: sum-based second moments, bias correction, adaptive clipping; beats NorMuon in the paper.

## Empirical Highlights
- Abstract claims empirical superiority over NorMuon plus a convergence guarantee.
- No numeric table in the abstract; do not invent one.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.06578`
- Code: none found as of 2026-10-06 (`code_status: none`).
