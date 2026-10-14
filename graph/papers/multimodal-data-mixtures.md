---
id: paper:multimodal-data-mixtures
type: paper
title: Scaling Laws for Multimodal Data Mixtures
authors:
- Aditi Khandelwal
- Ayush K. Tarun
- Yixuan Xu
- Imanol Schlag
- Golnoosh Farnadi
- Siva Reddy
- Luke Zettlemoyer
- Antoine Bosselut
year: 2026
month: 10
arxiv_id: '2610.14423'
url: https://arxiv.org/abs/2610.14423
methods:
- method:multimodal-data-mixtures
cites:
- paper:olmo-3
tags:
- pretraining
- multimodal
- moe
- data-mix
- neurips-2026
---

# Scaling Laws for Multimodal Data Mixtures

## Abstract Summary
NeurIPS 2026 spotlight. 268 MoE pretrain runs from 457M to 8.3B parameters, up to 150B tokens, for text/vision/audio mixing. Unified law with directional transfer, mixture-dependent capacity sharing, and repetition saturation. Compute optima are modality-specific.

## Key Contributions
1. Controlled MoE suite (six scales, 457M–8.3B) covering unimodal, bimodal, three-way, and repetition ablations.
2. Audio is model-heavy; text and vision want balanced parameter/token scaling.
3. Vision/audio saturate after ~2 unique-data passes; vision interferes with audio; audio is nearly inert as a source.

## Empirical Highlights
- Vision \(\alpha=0.50,\beta=0.51\); text \(\alpha=\beta=0.34\); audio \(\alpha=0.32\) (Table 1; single-paper).
- Repeating 5B unique non-text tokens 5× underperforms ~15B unique at every model scale (Figure 2).

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.14423`
- Code: `none found` (`code_status: none`).
