---
id: paper:spectrally-targeted-muon
type: paper
title: "Spectrally Targeted Muon"
authors:
  - "Vishrut Goyal"
  - "Rohan Ramkumar"
year: 2026
month: 10
arxiv_id: "2610.10965"
url: "https://arxiv.org/abs/2610.10965"
methods:
  - method:spectrally-targeted-muon
cites:
  - paper:muon2
  - paper:bulkboost
tags:
  - optimizer
  - muon
  - spectral
  - spectrally-targeted-muon
---

# Spectrally Targeted Muon

## Abstract Summary
Muon sets every singular value of the update to one. Spectrally Targeted Muon orthogonalizes only singular values above or below a threshold tau, interpolating normalized SGD and Muon, using Newton-Schulz on a shifted Gram matrix (no SVD). Small momentum singular values are not noise: orthogonalizing everything except the few largest nearly matches Muon while touching a small fraction of the momentum. On language models every momentum singular value is far below one, so Muon wins by amplifying directions too small to train at raw scale. Beside Muon2 / BulkBoost / Musec. No official GitHub as of 2026-10-09.

## Key Contributions
1. Thresholded orthogonalization interpolates normalized SGD and Muon without SVD.
2. Small singular values of momentum are the trainable signal on LMs, not noise.
3. Flattening the largest singular values keeps the parameter spectrum flat but is not what drives the loss.

## Empirical Highlights
- CIFAR-10 and NanoGPT speedruns. Orthogonalizing all but the few largest nearly matches Muon.
- Top-only orthogonalization falls short even though it holds almost all of the momentum mass.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.10965`
- Code: none found as of 2026-10-09 (`code_status: none`).
