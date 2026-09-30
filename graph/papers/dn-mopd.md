---
id: paper:dn-mopd
type: paper
title: "Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation"
authors:
  - "Xin Li"
  - "Hao Jiang"
  - "Xin Gao"
  - "Annan Wang"
  - "Yuchen Xie"
  - "Jinghao Guo"
  - "Xingwei Qu"
  - "Yichi Zhang"
  - "Chau Yuen"
year: 2026
month: 9
arxiv_id: "2609.35347"
url: "https://arxiv.org/abs/2609.35347"
methods:
  - method:dn-mopd
cites:
  - paper:open-mopd
  - paper:opd
tags:
  - post-training
  - distillation
  - multi-teacher
  - on-policy
  - dn-mopd
---

# Beyond Teacher Assignment: Domain-Normalized Multi-Teacher On-Policy Distillation

## Abstract Summary
Label-routed multi-teacher on-policy distillation (MOPD) decides which specialist teaches each prompt, but not how strongly that specialist's token log-ratios move the shared student. On independently trained Qwen3.5 math/code/IF pools at 9B, 4B, and 2B, label MOPD fails to beat the strongest single-teacher student and transfers little of the mathematics specialist: instruction-following log-ratios are 2.3–4.4× more dispersed than the pooled first-batch signal, mathematics about half as dispersed, and IF supplies 94% of the 4B combined gradient under equal weights. Domain-Normalized MOPD (DN-MOPD) keeps label routing and rescales each domain's distillation advantages by the clipped ratio of pooled to domain log-ratio standard deviation (clip 0.25–4). One extra operation on Uni-OPD/MOPD; no extra teacher, call, or learned router. Code: `https://github.com/LiXin97/DN-MOPD`.

## Key Contributions
1. **Feedback-scale diagnosis**: assignment alone does not transfer specialists; IF log-ratio spread dominates the shared update even with equal prompt counts.
2. **Domain normalization**: \(w_d=\mathrm{clip}(\sigma_{\mathrm{all}}/\sigma_d, 0.25, 4)\), \(\widetilde{A}_t=w_d A_t\), sign-preserving, batch-estimated; MOPD is the \(w_d=1\) special case.
3. **Not Open-MOPD**: Open-MOPD allocates budget from remaining gap / token share; DN-MOPD equalizes feedback dispersion on labeled routing.

## Empirical Highlights
- Six-task Total vs label MOPD: 9B 59.6 vs 58.4; 4B 52.5 vs 50.3; 2B 29.0 vs 26.6. 16K budget +1.17–2.36; 8K +2.47–3.08. Three-seed +1.12 / +1.97 / +2.34.
- Mathematics, lost under label routing, carries the largest recovery. Fixed weights near the measured multipliers match at 9B/4B; the gain is mostly turning IF down, not turning math up alone.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.35347`
- Code: `https://github.com/LiXin97/DN-MOPD` (`code_status: released`).
