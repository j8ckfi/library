---
id: paper:adana
type: paper
title: "Logarithmic-time schedules for scaling language models with momentum"
authors:
  - "Damien Ferbach"
  - "Courtney Paquette"
  - "Gauthier Gidel"
  - "Katie Everett"
  - "Elliot Paquette"
year: 2026
month: 2
arxiv_id: "2602.05298"
url: "https://arxiv.org/abs/2602.05298"
methods:
  - method:adana
cites: []
tags:
  - pretraining
  - optimizer
  - adana
  - momentum
---

# Logarithmic-time schedules for scaling language models with momentum

## Abstract Summary
Primary ADANA paper cited by the 2026-09-08 overtraining-axis study (`paper:optimizer-memory-schedules`, arXiv:2609.04577). ADANA puts DANA's growing momentum timescale into an Adam-style adaptive optimizer, with log-time weight decay whose memory window grows through training. DANA theory on power-law random features predicts an equivalent-OT exponent near $2-\kappa$ vs SGD; $\kappa=0.85$ is the transferable data-spectrum coefficient used throughout the later OT study. This node is the primary cite, not a 7B optimizer default.

## Key Contributions
1. **ADANA**: Adam-style adaptive optimizer with a log-time momentum schedule (DANA memory that grows during training).
2. **Log-time weight decay**: per-parameter WD timescale that grows with training, distinct from a constant AdamW $\lambda$.
3. **$\kappa$ as a data property**: DANA/ADANA treat $\kappa$ as transferable across model scales for a given data spectrum.

## Empirical Highlights
- Primary experimental tables live in Ferbach et al. 2602.05298. The 2026-09-08 OT paper is the cross-optimizer overtraining study (Muon / SOAP / ADANA vs AdamW, 51M–253M, OT $1\times$–$256\times$).
- OT-study treatment used throughout: $\kappa=0.85$, $\delta=8$, $g_3=8$.

## Open Source Repository & Resources
- The OT paper follows "the released PyTorch implementation used in Ferbach et al. (2026)". No separate official code recorded in this library as of 2026-09-08.
