---
id: paper:flash-opd
type: paper
title: "Flash-OPD: Fast On-Policy Distillation"
authors:
  - Wei Chen
  - Junle Chen
  - Yitong Yang
  - Zhaoyang Xu
  - Jiaxin Lin
  - Yuxuan Liang
  - Xiaofang Zhou
  - Kai Wang
  - Rui Chen
year: 2026
month: 10
arxiv_id: "2610.06105"
url: "https://arxiv.org/abs/2610.06105"
methods:
  - method:flash-opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - opd
  - flash-opd
---

# Flash-OPD: Fast On-Policy Distillation

## Abstract Summary
Long OPD rollouts are expensive; a single horizon mismatches heterogeneous reliable lengths. Flash-OPD treats the reliability boundary as the first-passage of accumulated low teacher–student compatibility events, interleaves cached generation with teacher verification, and stops each trajectory independently. The recent event rate only schedules the next check; the stop decision uses the exact cumulative count. 2.2x–7.5x vs standard OPD while maintaining or improving accuracy. Code: https://github.com/Onedean/Flash-OPD. Beside OPD.

## Key Contributions
1. **First-passage stop**: reliability boundary from accumulated low-compatibility events.
2. **Schedule vs decide**: event rate schedules the next verification; stop uses the exact count.
3. **2.2x–7.5x** vs standard OPD with maintained or improved accuracy.

## Empirical Highlights
- 2.2×–7.5× speedups over standard OPD while maintaining or improving accuracy across datasets and teacher–student settings.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.06105`
- Code: `https://github.com/Onedean/Flash-OPD` (`code_status: released`; HTTP 200 as of 2026-10-06). Site: `https://onedean.github.io/Flash-OPD-Site`.
