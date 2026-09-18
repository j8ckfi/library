---
id: paper:bias-only-ttrl
type: paper
title: "Label-free steering: Compressing test-time reinforcement learning into bias-only subspaces"
authors:
  - "Naveen Vakada"
  - "Mingyuan Li"
  - "Shaoxiong Ji"
year: 2026
month: 9
arxiv_id: "2609.18587"
url: "https://arxiv.org/abs/2609.18587"
methods:
  - method:bias-only-ttrl
cites:
  - paper:ttpo
  - paper:u-opsd
tags:
  - test-time-training
  - ttrl
  - label-free
  - bias-only
---

# Label-free steering: Compressing test-time reinforcement learning into bias-only subspaces

## Abstract Summary
Test-time RL can improve unlabeled reasoning, but usual TTRL updates a large slice of the network. Bias-only label-free TTRL keeps the backbone frozen and trains about 100K bias parameters with majority-vote pseudo-labels as rewards. On MATH-500 it reaches 76.67%, slightly above the authors' own labeled bias-steering reproduction, while using about 76,000× fewer trainable parameters than full-parameter TTRL. The same procedure helps vision-language and audio reasoning (MathVista, AI2D, LogicVista, MMAU). Learned steering vectors transfer to 4,500 held-out MATH problems. The paper attributes this to majority-vote reliability rising with rollout consensus and to bias subspaces with higher accessible gradient energy being more trainable. Niche compression of TTRL, not a replacement of TTPO.

## Key Contributions
1. **Bias-only TTRL**: ~100K bias parameters, frozen backbone, majority-vote rewards.
2. **MATH-500 76.67%** at ~76,000× fewer trainable params than full TTRL.
3. **Transfer** of steering vectors to 4,500 held-out MATH items; VL/audio transfer reported.

## Empirical Highlights
- MATH-500: 76.67%, slightly above labeled bias-steering in the same paper.
- ~76,000× fewer trainable parameters than full-parameter TTRL.
- Also reported: MathVista, AI2D, LogicVista, MMAU.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2609.18587`
- No official GitHub as of 2026-09-18 (`recipe:bias-only-ttrl` `code_status: none`).
