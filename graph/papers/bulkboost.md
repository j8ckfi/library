---
id: paper:bulkboost
type: paper
title: "Does Muon Need Fine-Grained Spectral Shaping?"
authors:
  - Meher Chaitanya
  - Tianyi Zhou
  - Aristides Gionis
year: 2026
month: 10
arxiv_id: "2610.07497"
url: "https://arxiv.org/abs/2610.07497"
methods:
  - method:bulkboost
cites:
  - paper:muon2
tags:
  - optimizer
  - muon
  - spectral
  - bulkboost
---

# Does Muon Need Fine-Grained Spectral Shaping?

## Abstract Summary
Fine-grained spectral maps on Muon momentum are unnecessary. BulkBoost is two-band, Marchenko–Pastur noise-calibrated spectral reweighting. 0.073–0.147% loss reduction vs Muon flat vs Freon 0.022% on Pythia 14M–410M. Active beside Muon variants (Musec / ORCA). Does not replace Muon2.

## Key Contributions
1. **Two-band MP-calibrated reweight** instead of a fine-grained spectral map.
2. **Fine-grained maps are unnecessary** in the paper's regime.
3. **0.073–0.147% loss reduction** vs Muon flat.

## Empirical Highlights
- Pythia 14M–410M. Freon 0.022% is the weaker fine-grained baseline in the paper.
- Not a 7B FineWeb bake-off vs Muon2.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07497`
- Code: none found as of 2026-10-07 (`code_status: none`).
