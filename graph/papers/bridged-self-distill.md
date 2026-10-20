---
id: paper:bridged-self-distill
type: paper
title: 'Bridged Self-Distillation for On-Policy Learning'
authors:
- 'Runsheng Chen'
- 'Yihong Liu'
- 'Raoyuan Zhao'
- 'Michael A. Hedderich'
- 'Hinrich Schütze'
- 'Matthias Grabmair'
year: 2026
month: 10
arxiv_id: '2610.26397'
url: https://arxiv.org/abs/2610.26397
methods:
- method:bridged-self-distill
cites:
- paper:opd
- paper:cross-tokenizer-opd
tags:
- distillation
- opd
- cross-tokenizer
- active
---

# Bridged Self-Distillation

## Abstract Summary
BSD turns an external teacher's reasoning trace into privileged context for a same-model self-teacher, then distills onto student rollouts. Works for shared-tokenizer, cross-tokenizer, and closed-API teachers without teacher token probabilities.

## Key Contributions
1. Trace-conditioned self-teacher as a bridge when teacher logp is missing.

## Empirical Highlights
- One recipe across three teacher-access settings.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.26397`
- Code: `https://github.com/TUMLegalTech/Bridged-Self-Distillation` (`code_status: released`).
