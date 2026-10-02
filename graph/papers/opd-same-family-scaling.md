---
id: paper:opd-same-family-scaling
type: paper
title: "Scaling properties of same-family on-policy distillation"
authors:
  - "Yuntai Bao"
  - "Qinfeng Li"
  - "Guoqing Jiang"
  - "Liwei Chen"
  - "Zhiheng Qin"
  - "Xuanping Li"
  - "Wenqi Zhang"
  - "Xuhong Zhang"
year: 2026
month: 9
arxiv_id: "2609.32722"
url: "https://arxiv.org/abs/2609.32722"
methods:
  - method:opd
cites:
  - paper:opd
tags:
  - post-training
  - distillation
  - on-policy
  - scaling
  - opd
---

# Scaling properties of same-family on-policy distillation

## Abstract Summary
Same-family OPD (weak-to-strong, same-base, strong-to-weak) has a regular early useful-transfer regime: held-out accuracy (gold score \(G\)) rises approximately linearly in \(d=\sqrt{\mathrm{KL}(\pi_\theta\|\pi_{\mathrm{ref}})}\). Peak \(G\) and the useful-transfer slope follow power laws in student/teacher size and teacher gold score. Peak score improves with teacher scale only up to roughly the student's scale; at a matched gold score, smaller teachers transfer better. Claim note on `method:opd`. No new method slug.

## Key Contributions
1. **Useful-transfer regime**: early OPD is linear in \(\sqrt{\mathrm{KL}}\) from the student init; later dynamics split into attenuated improvement, saturation, or regression.
2. **Weak-to-strong**: in every observed pair, the student's peak gold score exceeds its teacher's own.
3. **Scale laws**: teacher score alone does not define supervision value.

## Empirical Highlights
- Qwen2.5 0.5B–14B math. Peak law extrapolates to held-out largest scales within one accuracy point.
- Bootstrapping weak-to-strong OPD along a family and Vanilla-OPD vs Delta-OPD are studied; neither is a library retarget of OPD.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.32722`
- Code: none found as of 2026-10-02 (`code_status: none`).
