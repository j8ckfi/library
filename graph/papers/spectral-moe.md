---
id: paper:spectral-moe
type: paper
title: 'Spectral-MoE: Heterogeneous Per-Layer Expert Utilization in Dense-to-MoE Conversion'
authors:
- Zachary Broveak
- Christian Kubicka
- Thierry Tambe
year: 2026
month: 10
arxiv_id: '2610.19232'
url: https://arxiv.org/abs/2610.19232
methods:
- method:spectral-moe
cites:
- paper:maskerade
tags:
- architecture
- moe
- upcycling
---

# Spectral-MoE

## Abstract Summary
Analytic and learned dense-to-MoE converters fix the same expert utilization in every layer. Spectral-MoE allocates that budget per layer, statically or per token, on top of both converter families.

## Key Contributions
1. Utilization as a separate axis from how experts are cut.
2. Static per-layer and dynamic per-token allocators.
3. Llama-2-7B / Llama-3-8B / Qwen2.5-7B WikiText-2 and six-task checks.

## Empirical Highlights
- 25% FFN: dynamic learned PPL -1.04/-2.96/-2.71; analytic -2.45/-6.26/-2.17 vs uniform.
- Six-task +1.5/+4.2/+3.6 at 12.5/25/50% on the learned base.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.19232`
- Code: `https://github.com/ZacharyBroveak/Spectral-MoE` (`code_status: announced`; README-only as of 2026-10-15).
