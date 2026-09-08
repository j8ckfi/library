---
id: paper:optimizer-memory-schedules
type: paper
title: "Optimizer Memory Schedules for Outscaling the Overtraining Axis"
authors:
  - "Katie Everett"
  - "Shikai Qiu"
year: 2026
month: 9
arxiv_id: "2609.04577"
url: "https://arxiv.org/abs/2609.04577"
methods:
  - method:optimizer-memory-schedules
  - method:adana
cites:
  - paper:adana
  - paper:muon2
  - paper:soap
  - paper:adamw-paper
tags:
  - pretraining
  - optimizer
  - overtraining
  - muon
  - soap
  - adana
---

# Optimizer Memory Schedules for Outscaling the Overtraining Axis

## Abstract Summary
Relative optimizer performance and optimal hyperparameters change with the overtraining (OT) horizon $f=T/(20P)$. The paper compares Muon, SOAP, and ADANA against AdamW on 51M, 124M, and 253M models at OT $1\times$–$256\times$ (51M), $32\times$ (124M), and $8\times$ (253M), sweeping base LR at every setting. Preferred LR schedule can reverse across OT (linear decay wins at $1\times$; cosine at $8\times$/$32\times$). Best weight decay scales approximately as $\sqrt{\mathrm{OT}}$. Longer horizons favor longer fixed memory. Log-time WD and momentum cooldown help ADANA; with that treatment ADANA's equivalent-OT exponent vs AdamW is $1.15$–$1.20$, close to the DANA $2-\kappa=1.15$ prediction at $\kappa=0.85$. Muon and SOAP keep roughly constant token-efficiency advantages over AdamW; ADANA starts behind and closes at long OT. No official code as of 2026-09-08.

## Key Contributions
1. **OT as an evaluation axis**: optimizer rank and HPs are not transferable from $1\times$ Chinchilla to long OT.
2. **Schedule reversal**: linear LR decay beats cosine at $1\times$; cosine wins at $8\times$ and $32\times$ (all four optimizers).
3. **WD $\propto\sqrt{f}$**: $c_{\mathrm{uniform}}=8\sqrt{f}$, $c_{\mathrm{log}}=2\sqrt{f}$ after a joint LR×WD sweep on 51M.
4. **Memory grows with horizon**: optimal $M$ from $20$→$1280$ (AdamW), $20$→$640$ (Muon), $40$→$1280$ (SOAP) on 51M from $1\times$ to $128\times$ OT.

## Empirical Highlights
- Per-horizon memory tuning at $128\times$ OT: −3.3 mpt AdamW, −3.6 mpt Muon, −1.3 mpt SOAP vs a fixed $M=50$ setting (51M).
- Muon token multiplier vs AdamW $\approx 1.4\times$–$1.7\times$; SOAP $1.3\times$–$1.7\times$; SOAP $\approx 1.9\times$ at $128\times$ OT on 51M.
- ADANA at $2\times$ OT: $0.59\times$–$0.63\times$ vs Muon, $0.63\times$–$0.69\times$ vs SOAP; closes and can surpass Muon at the highest measured OT.
- ADANA vs AdamW equivalent-OT exponent $1.15$–$1.20$ with log-time WD + momentum cooldown.

## Open Source Repository & Resources
- No official GitHub as of 2026-09-08. ADANA follows the Ferbach et al. 2602.05298 PyTorch implementation.
