---
id: paper:law
type: paper
title: 'Loopholing All the Way: Language Modeling with pure Self-Conditioning'
authors:
- 'Adrien Deschenaux'
- 'Nadezhda Ilieva'
- 'Justin Deschenaux'
- 'Manuel Madeira'
- 'Dorina Thanou'
- 'Aurelien Lucchi'
- 'Antonio Orvieto'
- 'Caglar Gulcehre'
year: 2026
month: 10
arxiv_id: '2610.30068'
url: https://arxiv.org/abs/2610.30068
methods:
- method:law
cites:
- paper:semicat
tags:
- diffusion-lm
- self-conditioning
- active
---

# LAW

## Abstract Summary
LAW (Loopholing All the Way) makes Self-Conditioning the whole generative process: it carries the expected embedding across denoise steps and decodes tokens only at the end.

## Key Contributions
1. LAW as an active plug-in on `task:continuous-diffusion-lm-pretrain`.

## Empirical Highlights
- Sudoku beats prior discrete and continuous DLMs including Loopholing Discrete Diffusion; Maze most accurate from 2 to 64 NFE. Does not retarget `method:semicat`.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.30068`
- Code: `none found` (`code_status: none`).
