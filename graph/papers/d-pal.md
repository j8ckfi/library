---
id: paper:d-pal
type: paper
title: 'Beyond the Point Mass: Acceptance-Derived Weights and Distributional Losses for Speculative Decoding'
authors:
- 'Tianyu Wu'
- 'Zhuohan Wang'
- 'Jonathan Geuter'
- 'Yu Yao'
- 'Weifan Jiang'
- 'Chengxi Zhang'
- 'Ju Li'
- 'Minlan Yu'
year: 2026
month: 10
arxiv_id: '2610.28355'
url: https://arxiv.org/abs/2610.28355
methods:
- method:d-pal
cites:
- paper:uno
tags:
- speculative-decoding
- active
---

# Beyond the Point Mass

## Abstract Summary
D-PAL trains speculative drafters from exact expected accepted length using draft-target overlap (1-TV) as the acceptance signal and Rényi-1/2 or forward KL as the per-position loss instead of point-mass CE.

## Key Contributions
1. Overlap-based position weights and distributional drafter losses. Reduces to D-PACE for a point-mass target.

## Empirical Highlights
- Qwen3-4B six-bench mean acceptance 4.50→4.57 (T=0) and 4.20→4.28 (T=1) vs D-PACE.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28355`
- Code: `https://github.com/Lucas-TY/D-PAL-SpecForge` (`code_status: released`).
