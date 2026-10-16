---
id: paper:scope-t2i
type: paper
title: 'SCOPE: Semantic Bounded Credit Optimization for Prompt Engineering in Text-to-image Generation'
authors:
- Yufei Jiao
- Jinfa Huang
- Zeyue Xue
- Tianyu Xie
- Yuexiao Ma
- Rongrong Ji
- Xiawu Zheng
- Jiebo Luo
year: 2026
month: 10
arxiv_id: '2610.22264'
url: https://arxiv.org/abs/2610.22264
methods:
- method:scope-t2i
cites:
- paper:diffusion-opsd
- paper:self-opd
tags:
- diffusion
- rl-alignment
- t2i
- credit-assignment
---

# SCOPE (T2I prompt rewriting)

## Abstract Summary
GRPO prompt rewriters apply one image-level advantage to every subword, even though objects, counts, attributes, and relations are spans. SCOPE pools policy-logp shifts inside the rewriter's own semantic partition and shares one coefficient per span.

## Key Contributions
1. Span-pooled GRPO credit for T2I prompt rewriting.
2. No extra span rewards or extra image renders.
3. Qwen-Image, SD3, FLUX.1-dev.

## Empirical Highlights
- Average relative gains vs vanilla GRPO: +9.48% GeneVal, +7.62% T2I-CompBench.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.22264`
- Code: `https://github.com/MAC-AutoML/SCOPE` (`code_status: released`).

