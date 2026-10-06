---
id: paper:mend
type: paper
title: "MEND: RL For Flow Models via Proximal Velocity Matching"
authors:
  - Shreshth Saini
  - Neil Birkbeck
  - Yilin Wang
  - Balu Adsumilli
  - Alan C. Bovik
year: 2026
month: 10
arxiv_id: "2610.05954"
url: "https://arxiv.org/abs/2610.05954"
methods:
  - method:mend
cites:
  - paper:self-opd
  - paper:diffusion-opsd
tags:
  - diffusion
  - post-training
  - mend
---

# MEND: RL For Flow Models via Proximal Velocity Matching

## Abstract Summary
MEND is RL for flow models via proximal velocity matching. Caps rewards in each prompt group so already-good samples get no move. Below the cap, proposes reward-gradient moves and accepts only when capped reward gain beats a quadratic displacement price. Regresses onto those velocity targets with no KL, frozen reference, or advantage weights. 100 updates vs Flow-GRPO ~4k; wins 5/6 evaluators at the same distance to base-model images. Equal-budget protocol: beats ReFL and DiffusionNFT. No GitHub URL in the abstract (`code_status: none`). Beside DiffusionOPSD / Self-OPD.

## Key Contributions
1. **Proximal velocity matching** with a within-group reward cap.
2. **Accept/reject** a reward-gradient move by capped gain vs quadratic displacement.
3. **~100 updates vs Flow-GRPO ~4k**.

## Empirical Highlights
- 100 updates vs Flow-GRPO about 4k updates; 5 of 6 evaluators at the same distance to base-model images.
- Equal-budget: surpasses ReFL and DiffusionNFT.
- Abstract names PickScore-style evaluators without a mandatory numeric table in the API summary; do not invent 24.03 unless present. (HTML/abstract as fetched: no PickScore 24.03 in the API abstract.)

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.05954`
- Code: none found as of 2026-10-06 (`code_status: none`). Abstract says Code without a URL.
