---
id: paper:minite
type: paper
title: 'miniTE: Diagnosing and Bridging the Execution Gap in Native NVFP4 Reinforcement Learning'
authors:
- 'Zhen Li'
- 'Mingfa Feng'
- 'Yiming Zhang'
- 'Yang Yu'
- 'Changhai Zhou'
- 'Pengxiang Li'
- 'Dongkuan Wu'
- 'Congkai Xie'
- 'Hongxia Yang'
year: 2026
month: 10
arxiv_id: '2610.23928'
url: https://arxiv.org/abs/2610.23928
methods:
- method:minite
cites:
- paper:trace
- paper:triage
- paper:quartet-ii
tags:
- quantization
- nvfp4
- rl
- active
---

# miniTE

## Abstract Summary
Matching NVFP4 weights and format across train and sample engines is not enough. miniTE adds execution diagnostics, cross-engine alignment, and native W4A4 GEMM. On Qwen3-30B-A3B, a B300 learner hits 33540 tok/s (1.39x BF16, 1.47x TE NVFP4) with eval close to BF16.

## Key Contributions
1. Execution-gap diagnosis plus a native NVFP4 RL learning path.

## Empirical Highlights
- Naive Transformer Engine NVFP4 loses eval quality; miniTE does not.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.23928`
- Code: `none found` (`code_status: none`).
