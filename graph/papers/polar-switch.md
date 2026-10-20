---
id: paper:polar-switch
type: paper
title: 'Polar Switch: Fast Muon Orthogonalization with Polynomial Circuits'
authors:
- 'Zhehang Du'
- 'Weijie Su'
year: 2026
month: 10
arxiv_id: '2610.26742'
url: https://arxiv.org/abs/2610.26742
methods:
- method:polar-switch
cites:
- paper:muon2
tags:
- optimizer
- muon
- active
---

# Polar Switch

## Abstract Summary
Muon differs from spectral gradient descent mainly in its GPU-friendly Newton-Schulz polynomial for the polar factor. Polar Switch uses polynomial circuits so a given high degree costs fewer FLOPs than quintic iterations. Recommended circuits cut Polar Express runtime 15.5-18.7% on squares and Gram NS 8.6-16.2% on rectangular aspect ratios, with similar pretrain val loss.

## Key Contributions
1. Polynomial-circuit polar orthogonalization for Muon, with designed coefficients and a GPU cost model.

## Empirical Highlights
- NanoGPT #91 / Qwen3-0.6B / Gemma 3-1B match established polar methods at lower ortho runtime.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.26742`
- Code: `https://github.com/zhehangdu/polar-switch` (`code_status: released`).
