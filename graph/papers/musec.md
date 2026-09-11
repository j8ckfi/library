---
id: paper:musec
type: paper
title: "Musec: MomentUm SpEctral Clipping for Stable Muon-type Training"
authors:
  - "Zhuanghua Liu"
  - "Menglian Wang"
  - "Luo Luo"
year: 2026
month: 9
arxiv_id: "2609.11655"
url: "https://arxiv.org/abs/2609.11655"
methods:
  - method:musec
cites:
  - paper:muon2
  - paper:muonclip-kimi-k2
tags:
  - pretraining
  - optimizer
  - muon
  - musec
---

# Musec: MomentUm SpEctral Clipping for Stable Muon-type Training

## Abstract Summary
Muon's spectral flattening (singular values of the momentum matrix set near 1) injects large updates into weak spectral directions and shows up as loss spikes and unbounded weights. Weight or attention-logit clipping is architecture-specific and does not cover every matrix. Musec clips singular values of the momentum above a threshold and keeps the rest of the spectrum. Soft Musec is a smooth saturation implemented with coupled Newton–Schulz iterations. The paper gives the first convergence guarantee for Muon-type methods in nonconvex nonsmooth stochastic optimization. Experiments run on the modded-nanogpt host; Soft Musec stays stable in learning-rate / scale settings where Muon variants diverge, and matches them when those runs are already well-tuned.

## Key Contributions
1. **Spectral clipping instead of flattening** as an optimizer-level, architecture-agnostic Muon update.
2. **Soft Musec**: smooth saturation via coupled Newton–Schulz (no per-step SVD required at train time).
3. **Nonconvex nonsmooth convergence** for Muon-type methods.

## Empirical Highlights
- Soft Musec remains stable where existing Muon variants diverge across learning rates and model sizes on modded-nanogpt / NanoGPT-style GPT-2 descendants.
- Under well-tuned configurations, Soft Musec matches those variants rather than beating them on loss.

## Open Source Repository & Resources
- No dedicated Musec repo as of 2026-09-11. Experiments: `https://github.com/kellerjordan/modded-nanogpt`.
