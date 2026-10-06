---
id: paper:clean
type: paper
title: "Clean: Second-order LLM Training at Linear Memory Cost via Nyström Sketching"
authors:
  - Beheshteh T. Rakhshan
  - Sahar Rajabi
  - Maziar Sargordi Shikai Fang
  - Guillaume Rabusseau
  - Sirisha Rambhatla
year: 2026
month: 10
arxiv_id: "2610.04204"
url: "https://arxiv.org/abs/2610.04204"
methods:
  - method:clean
cites:
  - paper:soap
  - paper:soap-muon-scale
  - paper:muon2
tags:
  - pretraining
  - optimizer
  - soap
  - clean
---

# Clean: Second-order LLM Training at Linear Memory Cost via Nyström Sketching

## Abstract Summary
SOAP keeps full curvature at quadratic optimizer-state memory. Clean Nyström-sketches SOAP's left and right preconditioners to linear memory and reintegrates off-subspace curvature. Q-Clean is a low-precision state variant: over 50% optimizer memory vs Muon on LLaMA-1.3B with competitive quality. Clean's optimizer-state footprint is smaller than AdamW and reaches AdamW's final performance 26% faster in wall-clock. The methods uniquely enable 13B pretraining on one 80GB GPU. Active plug-in beside SOAP / KL-SOAP. No public code as of 2026-10-06.

## Key Contributions
1. **Nyström SOAP**: linear-memory left/right preconditioners plus off-subspace reintegration.
2. **Q-Clean**: low-precision optimizer states; >50% optimizer memory vs Muon on LLaMA-1.3B.
3. **Single-GPU 13B**: paper claims 13B pretrain on one 80GB GPU.

## Empirical Highlights
- Q-Clean: over 50% optimizer-memory cut vs Muon on LLaMA-1.3B.
- Clean: smaller optimizer state than AdamW; AdamW final performance 26% faster wall-clock.
- 13B on a single 80GB GPU.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.04204`
- Code: none found as of 2026-10-06 (`code_status: none`).
