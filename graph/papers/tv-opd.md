---
id: paper:tv-opd
type: paper
title: "TV-Regulated OPD: Direction Matters in On-Policy Distillation"
authors:
  - "Han Xiao"
  - "Yifan Niu"
  - "Dongyi Liu"
  - "Chang Luo"
  - "Jia Li"
year: 2026
month: 9
arxiv_id: "2609.08341"
url: "https://arxiv.org/abs/2609.08341"
methods:
  - method:tv-opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - on-policy
  - tv-opd
---

# TV-Regulated OPD: Direction Matters in On-Policy Distillation

## Abstract Summary
Sampled OPD uses the unbounded teacher–student log-ratio as a token coefficient. Controlled ablations on JustRL-DeepSeek-1.5B show that keeping only the sign of that coefficient (Sign-TV) matches or beats raw magnitude: two-benchmark trajectory average 36.29 vs Raw 35.40; per-seed best AIME 2024 50.00±1.18 vs Raw 47.50. Fine-grained token-wise magnitude (including permutation within sign) does not help. Sign-TV estimates conditional total-variation descent. TV-OPD restores a shared global scale from an estimated TV so updates shrink as teacher and student converge, without restoring per-token |Δ|. Late-stage JustRL AIME 2024 49.58 vs Sign-TV 47.92 vs Raw 46.11; LateMean 43.06±0.10 vs Raw 40.87±0.83, PeakDrop 2.36 vs 3.51.

## Key Contributions
1. **Sign is enough**: token-wise magnitude allocation is not load-bearing on the measured pair.
2. **TV identity**: sign-weighted sampled update estimates −2 ∇ D_TV(p, q_θ).
3. **Shared TV regulator**: global scale decays with discrepancy; coefficients stay bounded in {−c, 0, +c}.
4. **Late-stage stability** without a new teacher or trajectory filter.

## Empirical Highlights
- Sign vs Raw (JustRL diagnostic): AIME 2024 best 50.00±1.18 vs 47.50; AIME 2025 37.50 vs 35.83.
- Late AIME 2024: TV-OPD 49.58 / Sign-TV 47.92 / Raw 46.11 (steps 500–625).
- Two-benchmark LateMean 43.06±0.10 vs Raw 40.87±0.83.

## Open Source Repository & Resources
- No official GitHub as of 2026-09-09.
