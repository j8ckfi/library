---
id: paper:opd-hard-cot-selection
type: paper
title: "What Matters in On-Policy Distillation? A Perspective on Data Efficiency and Data Selection"
authors:
  - "Zhinan Hou"
  - "Jiaqi Zhang"
  - "Xunliang Cai"
  - "Keyou You"
year: 2026
month: 9
arxiv_id: "2609.05198"
url: "https://arxiv.org/abs/2609.05198"
methods:
  - method:opd-hard-cot-selection
  - method:opd
cites:
  - paper:opd
  - paper:opd-one-example
tags:
  - post-training
  - distillation
  - on-policy
  - data-selection
  - opd
---

# What Matters in On-Policy Distillation? A Perspective on Data Efficiency and Data Selection

## Abstract Summary
Data-centric mechanisms in OPD are under-explored relative to algorithm design. This paper studies 1-shot and few-shot OPD. 1-shot is consistently effective; harder examples yield larger gains. The driver is not high token entropy but the longer CoT that hard problems induce: long traces keep the student aligned with the teacher over a long horizon and teach reflection patterns (e.g. "Alternatively") missing from short CoTs. Select hard examples only. Even teacher-unsolvable items can be used. On four models from 1.5B to 7B, 8 hard examples match the DAPO-Math-17K full-set baseline. Sibling to OPD-II (`paper:opd-one-example`, 2609.04172): that paper emphasizes query *diversity vs volume*; this paper emphasizes *hard/long-CoT vs easy/short-CoT*. Neither replaces OPD.

## Key Contributions
1. **1-shot OPD works across sampled examples**; hard queries beat easy ones (best 1-shot $\pi_{973}$ avg 51.7 vs easy $\pi_5$ 48.0 vs full-set 53.7 on R1-Distill-Qwen-1.5B).
2. **Long CoT, not token entropy**, is the data mechanism. Hard problems generate longer traces with reflection.
3. **Difficulty ranking**: 16 rollouts each for student and teacher; $A_i=(S_i+T_i)/2$; Easy $A_i>0.9$, Medium $[0.1,0.9]$, Hard $A_i<0.1$.
4. **8 hard examples ≈ 17K**: $\{\pi_{874},\ldots,\pi_{997}\}$ avg 53.6 vs DAPO-Math-17K 53.7. Teacher-unsolvable hard items remain usable.

## Empirical Highlights
- R1-Distill-Qwen-1.5B <- JustRL-1.5B: 8 hard 53.6 vs 17K 53.7 vs random 1K 53.6 vs 8 easy 51.2.
- Skywork-OR1-Math-7B -> R1-Distill-Qwen-7B: 8-shot 59.5 vs full-set 59.6; 1-shot 58.4 vs student 56.3.
- Qwen3-4B -> Qwen3-1.7B-Base: 8-shot 21.3 vs full-set 22.5 vs student 6.3.
- Training: verl, batch/mini-batch 64, 8 responses/prompt, top-16 reverse KL, 279 steps (1 epoch of 17K), 8x H100.

## Open Source Repository & Resources
- No official GitHub found as of 2026-09-07. Host loop is ordinary top-$k$ OPD (`recipe:opd`). This paper only changes the query set (`recipe:opd-hard-cot-selection`).
