---
id: paper:msar
type: paper
title: Multi-Stream Attention Residuals
authors:
- Xiaohan Qin
- Xiangdong Zhang
- Tuo Dai
- Sunan Zou
- Huaijin Wu
- Yebin Yang
- Zhuo Xia
- Lin Yao
- Yuliang Liu
- Junchi Yan
year: 2026
month: 10
arxiv_id: '2610.13630'
url: https://arxiv.org/abs/2610.13630
methods:
- method:msar
cites:
- paper:attnres
- paper:mhc
- paper:muon2
tags:
- pretraining
- residuals
- msar
---

# Multi-Stream Attention Residuals

## Abstract Summary
MSAR splits the residual stream and applies attention residuals across streams. On 18B and 28B MoE pretrain it beats vanilla residuals, mHC, and AttnRes on 12 benchmarks. Iso-loss compute speedup is 1.58× vs 1.35× AttnRes and 1.30× mHC. Composes with Muon2. Single-paper baselines: no supersession of AttnRes or mHC.

## Key Contributions
1. Multi-stream attention residuals as a drop-in residual topology.
2. 18B/28B MoE bake-off vs vanilla / mHC / AttnRes on 12 benchmarks.
3. Released code at jianke0604/MSAR.

## Empirical Highlights
- 18B train loss 1.750 vs Vanilla 1.799, mHC 1.776, AttnRes 1.769.
- 28B +0.5% FLOPs / +0.3% activated params vs the vanilla residual.
- Iso-loss speedup 1.58× vs 1.35× AttnRes, 1.30× mHC.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.13630`
- Code: `https://github.com/jianke0604/MSAR` (`code_status: released`; HTTP 200 as of 2026-10-13).
