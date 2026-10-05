---
id: paper:divergence-entropy-distillation
type: paper
title: "Divergence controls entropy in distillation"
authors:
  - "Nicolas Zucchet"
  - "Scott W. Linderman"
year: 2026
month: 10
arxiv_id: "2610.03529"
url: "https://arxiv.org/abs/2610.03529"
methods:
  - method:opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - entropy
  - kl
  - gotcha
---

# Divergence controls entropy in distillation

## Abstract Summary
The student's entropy is set more by the token-level divergence than by on- vs off-policy sampling. Forward KL inflates student entropy above the teacher (cross-entropy is the special case, matching pretrain/SFT entropy to the loss). Reverse KL deflates entropy until the student–teacher gap is too large, then can inflate it. Interpolating between the two changes entropy smoothly early and abruptly at convergence. Lower entropy in on-policy distillation comes from token-level reverse KL, not from on-policy sampling. In privileged self-distillation the divergence hyperparameters that work are those that compensate for the entropy drop from privileged conditioning. Claim note on `method:opd`. Code: `https://github.com/NicolasZucchet/Entropy-in-distillation`.

## Key Contributions
1. **Forward KL inflates, reverse KL deflates** student entropy (until the reverse-KL gap is too large).
2. **On-policy OPD's low entropy is the reverse-KL term**, not the sampling policy.
3. **Self-distillation**: pick divergence HPs that restore entropy lost to privileged context.

## Empirical Highlights
- Identity that trained LM entropy matches the cross-entropy it was trained with is verified in pretrain and SFT.
- Do not retarget OPD. Divergence choice is a gotcha on existing OPD hosts.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.03529`
- Code: `https://github.com/NicolasZucchet/Entropy-in-distillation` (`code_status: released`; HTTP 200 as of 2026-10-05).
