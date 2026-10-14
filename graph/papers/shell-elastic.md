---
id: paper:shell-elastic
type: paper
title: 'ShellElastic: Scalable Elastic Pretraining with Simultaneous Maximal Updates and Hyperparameter Transfer'
authors:
- Can Jin
- Yan Kang
- Yifan Gong
- Chongjian Ge
- Mingze Xu
- Yuanjun Xiong
- Dimitris N. Metaxas
- Hongwu Peng
year: 2026
month: 10
arxiv_id: '2610.15124'
url: https://arxiv.org/abs/2610.15124
methods:
- method:shell-elastic
cites:
- paper:muon2
- paper:elr
tags:
- pretraining
- elastic
- width
- mup
---

# ShellElastic

## Abstract Summary
Nested width-elastic supernet at roughly the cost of the widest subnet. Simultaneous maximal updates (Shell) plus μP-style HP transfer (μE). HF Daily 2026-10-14.

## Key Contributions
1. Block-lower-triangular nesting so inner widths train for free inside the outer forward/backward.
2. μE hyperparameter transfer across nested widths.
3. Mean val-loss below the best baseline at three scale bands.

## Empirical Highlights
- Mean val loss 0.028 / 0.005 / 0.018 nats below best baseline at 119M–285M / 375M–906M / 675M–1.69B (Table 2; single-paper).
- Best or tied on 12/15 val-loss tiers and 14/15 5-shot tiers.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.15124`
- Code: `https://github.com/jincan333/ShellElastic` (`code_status: released`).
