---
id: paper:orca
type: paper
title: "ORCA: The Annealed Spectral Conditioning Optimizer for Faster, Better LLM Training"
authors:
  - Yuanshi Liu
  - Boyuan Jiang
  - Liang Hou
  - Xin Tao
  - Pengfei Wan
  - Zhouchen Lin
  - Cong Fang
year: 2026
month: 10
arxiv_id: "2610.06116"
url: "https://arxiv.org/abs/2610.06116"
methods:
  - method:orca
cites:
  - paper:muon2
tags:
  - pretraining
  - optimizer
  - muon
  - orca
---

# ORCA: The Annealed Spectral Conditioning Optimizer for Faster, Better LLM Training

## Abstract Summary
Muon often yields higher effective-rank weights than Adam, but extra spectral control has been modest. Concentrated spectra can suppress coupled-matrix gradient directions, while keeping the constraint for the whole run can raise the loss floor. ORCA (Orthogonal Regularization, Cooled After) applies strong temporary soft-orthogonality early, then removes it. Across LLaMA, Qwen3, and fine-grained MoE from 130M to 8B, ORCA reports lower final validation loss than Muon; the Muon-relative reduction matches or exceeds Muon's reduction vs Adam. Active plug-in beside Muon2. No public code as of 2026-10-06.

## Key Contributions
1. **Early-shaping, later-release**: strong soft-orthogonality only in early training, then drop it.
2. **Minimal intervention**: no architecture change; claimed minimal overhead on Muon-family trainers.
3. **Scale coverage**: LLaMA / Qwen3 / fine-grained MoE, 130M–8B.

## Empirical Highlights
- Abstract: lower final validation loss than Muon; loss drop vs Muon matches or exceeds Muon's drop vs Adam.
- Do not invent a 0.02–0.04 loss delta or a 60k-vs-100k step table; those numbers are not in the abstract.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.06116`
- Code: none found as of 2026-10-06 (`code_status: none`).
