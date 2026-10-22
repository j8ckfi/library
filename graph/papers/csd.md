---
id: paper:csd
type: paper
title: 'CSD: Common-Support Distillation for Cross-Tokenizer Knowledge Transfer'
authors:
- 'Mingyu Yang'
- 'Sharath Turuvekere Sreenivas'
- 'Adithyakrishna Venkatesh Hanasoge'
- 'Nima Tajbakhsh'
- 'Ashwath Aithal'
- 'Pavlo Molchanov'
year: 2026
month: 10
arxiv_id: '2610.28895'
url: https://arxiv.org/abs/2610.28895
methods:
- method:csd
cites:
- paper:cross-tokenizer-opd
- paper:opd
tags:
- distillation
- cross-tokenizer
- active
---

# CSD

## Abstract Summary
CSD aligns teacher and student next-token distributions on a dynamically constructed common support of chunk continuations instead of restricting to a shared vocabulary subset or a single observed chunk.

## Key Contributions
1. CSD as an active plug-in on `task:cross-tokenizer-opd`.

## Empirical Highlights
- Llama-3.1-8B up to +4.2 vs strongest baseline; highest average vs X-Token 0.66-5.38 and ALM 1.33-3. Does not retarget `method:cross-tokenizer-opd`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.28895`
- Code: `https://github.com/NVIDIA-NeMo/RL` (`code_status: announced`).
