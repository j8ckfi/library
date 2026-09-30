---
id: paper:pmopd
type: paper
title: "PMOPD: Task Ordering, Cycling, and Parameter-Update Subspace Protection in Multi-Teacher On-Policy Distillation"
authors:
  - "Youzhi Liu"
  - "Ruobing Zheng"
  - "Boyuan Tong"
  - "Tianqi Li"
  - "Pingqi Li"
  - "Hanbo Bi"
  - "Yi Yuan"
  - "Jingdong Chen"
year: 2026
month: 9
arxiv_id: "2609.34605"
url: "https://arxiv.org/abs/2609.34605"
methods:
  - method:pmopd
cites:
  - paper:open-mopd
  - paper:opd
tags:
  - post-training
  - distillation
  - multi-teacher
  - pmopd
---

# PMOPD: Task Ordering, Cycling, and Parameter-Update Subspace Protection in Multi-Teacher On-Policy Distillation

## Abstract Summary
Multi-teacher OPD sees a capability seesaw: improving one domain suppresses another because specialists pull shared parameters in different directions. Cumulative OPD block displacements concentrate in low-dimensional, task-consistent, cross-task-dissimilar subspaces. Projection-based MOPD (PMOPD) stores those subspaces and projects both the gradient and the Adafactor-preconditioned update away from protected task directions (the second projection is required because elementwise adaptive preconditioning can rotate a projected gradient back into the protected span). A lightweight conflict probe orders tasks; cycling rebuilds memories so protection tracks the current trajectory. Code→Reason→Math, four cycles in the paper. Ant Group. No public GitHub as of 2026-09-30.

## Key Contributions
1. **Geometry**: OPD block \(\Delta W\) SVD bases stabilize early, align within a task, and overlap little across tasks.
2. **Dual projection**: remove interfering components from gradients and from adaptive optimizer updates.
3. **Probe + cycling**: directional conflict ranking; rebuild subspace memory each cycle (K=16 SVD).

## Empirical Highlights
- Qwen2.5-7B three-task average 66.97 vs MOPD 64.43 (+2.54) vs their Open-MOPD 63.54. Llama-3.1-8B 41.04 vs MOPD 38.95 (+2.09). Every evaluated capability improves (not a redistribution).
- Paper Open-MOPD 63.54 is **not** the library Open-MOPD 83.4% headroom-recovery bake-off. Do not retarget `method:open-mopd`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.34605`
- Code: none found as of 2026-09-30 (`code_status: none`).
