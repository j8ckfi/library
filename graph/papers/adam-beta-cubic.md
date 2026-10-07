---
id: paper:adam-beta-cubic
type: paper
title: "Early Memory Selection for Balanced Adam"
authors:
  - Alberto Fernández-Hernández
  - Cristian Pérez-Corral
  - Jose I. Mestre
  - Manuel F. Dolz
  - Enrique S. Quintana-Ortí
year: 2026
month: 10
arxiv_id: "2610.08624"
url: "https://arxiv.org/abs/2610.08624"
methods:
  - method:adam-beta-cubic
cites:
  - paper:adamw-paper
tags:
  - optimizer
  - adam
  - hyperparameters
  - adam-beta-cubic
---

# Early Memory Selection for Balanced Adam

## Abstract Summary
Adam's shared beta (β1=β2=β) can be picked from a 200-update pilot plus gradient probes instead of a default 0.95. A cubic rule on those probes yields 40.7% lower mean relative val gap vs β=0.95 on 11 workloads, and 32.3% vs the best constant β. Code AlbertoFdezHdez/Adam_beta_rule_cubic. Active HP recipe beside AdamW. Does not retarget Muon2 or AdamW as the layer default.

## Key Contributions
1. **200-update pilot + 16 probes at 4 checkpoints** to pick shared β.
2. **Cubic rule** on the probe statistics.
3. **40.7% lower mean relative val gap** vs β=0.95 on 11 workloads.

## Empirical Highlights
- 32.3% vs best constant β.
- 11 workloads; not a 7B FineWeb bake-off vs Muon2.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.08624`
- Code: `https://github.com/AlbertoFdezHdez/Adam_beta_rule_cubic` (`code_status: released`; HTTP 200 as of 2026-10-07).
