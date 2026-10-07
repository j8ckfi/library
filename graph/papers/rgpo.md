---
id: paper:rgpo
type: paper
title: "Rationale-Guided Policy Optimization: Learning to Reason with Adaptive Rationale Scaffolding"
authors:
  - Hoang Phan
  - Minh Pham
  - Chau Pham
  - Chinmay Hegde
  - Trung Le
  - Qi Lei
year: 2026
month: 10
arxiv_id: "2610.07342"
url: "https://arxiv.org/abs/2610.07342"
methods:
  - method:rgpo
cites:
  - paper:mintrl
  - paper:ga-grpo
tags:
  - post-training
  - rl-alignment
  - guidance
  - rgpo
  - neurips-2026
---

# Rationale-Guided Policy Optimization: Learning to Reason with Adaptive Rationale Scaffolding

## Abstract Summary
Sparse-reward RLVR underuses ground-truth rationales. RGPO (NeurIPS 2026) adaptively scaffolds those rationales instead of dumping a fixed expert trace. Beside MInTRL / LUFFY / ExPO-style guidance. Linked theory: GA-GRPO (`paper:ga-grpo` `arXiv:2610.06861`) for optimal guidance weighting. Code VietHoang1512/rgpo. Does not replace CISPO.

## Key Contributions
1. **Adaptive GT rationale scaffolding** for sparse-reward RLVR.
2. **NeurIPS 2026**.
3. **Released code** at VietHoang1512/rgpo.

## Empirical Highlights
- Guidance family, not a CISPO Pass@1 bake-off. Pair with GA-GRPO for the λ*(T,δ,σ²) weight.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07342`
- Code: `https://github.com/VietHoang1512/rgpo` (`code_status: released`; HTTP 200 as of 2026-10-07).
