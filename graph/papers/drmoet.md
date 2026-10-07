---
id: paper:drmoet
type: paper
title: "Distributionally Robust Mixture-of-Experts Training"
authors:
  - Xin Teng
  - Muxiao Li
  - Hongyi Wen
year: 2026
month: 10
arxiv_id: "2610.07207"
url: "https://arxiv.org/abs/2610.07207"
methods:
  - method:drmoet
cites:
  - paper:deepseek-v4
tags:
  - pretraining
  - moe
  - load-balancing
  - drmoet
  - neurips-2026
---

# Distributionally Robust Mixture-of-Experts Training

## Abstract Summary
Standard MoE load-balancing is brittle under mid-k misrouting. DRMoET is a drop-in distributionally robust training objective (NeurIPS 2026) on the FLAME-MoE recipe. FLAME-MoE 10.3B 67B tokens seven-task avg 0.6767 vs 0.6625 FLAME vs 0.6431 aux-loss-free; 4.3% lower excess loss under mid-k misrouting. Also 746M. Code MAPS-research/DRMoET. Active on MoE pretrain. Does not replace DeepSeek-V4 / Kimi-K3.

## Key Contributions
1. **Drop-in DRO objective** for MoE load-balancing.
2. **746M / 10.3B** FLAME-MoE recipe.
3. **4.3% lower excess loss** under mid-k misrouting.

## Empirical Highlights
- 10.3B seven-task avg 0.6767 vs FLAME 0.6625 vs aux-loss-free 0.6431.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.07207`
- Code: `https://github.com/MAPS-research/DRMoET` (`code_status: released`; HTTP 200 as of 2026-10-07). Site: `https://drmoet.github.io`.
