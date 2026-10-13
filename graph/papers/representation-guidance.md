---
id: paper:representation-guidance
type: paper
title: Learning Representations to Guide Pixel Diffusion Transformers
authors:
- Zihao Pan
- Mengting Chen
- Cheng Shi
- Taihang Hu
- Zhengrong Yue
- Zikang Wang
- Yuan Wang
- Wei Li
- Sibei Yang
year: 2026
month: 10
arxiv_id: '2610.12978'
url: https://arxiv.org/abs/2610.12978
methods:
- method:representation-guidance
cites:
- paper:diffusion-opsd
tags:
- diffusion
- pretraining
- representation-guidance
---

# Learning Representations to Guide Pixel Diffusion Transformers

## Abstract Summary
Representation Guidance (RG) trains a pixel-space DiT with a low-dimensional bottleneck whose predicted offset modifies the flow-matching target. ImageNet-256 FID 1.55 (XL/16), ImageNet-512 FID 1.74, GenEval 0.89, DPG-Bench 87.1. First hop on `task:pixel-diffusion-pretrain`.

## Key Contributions
1. Pixel-space DiT with a low-dim representation bottleneck.
2. Predicted offset that edits the flow-matching target.
3. ImageNet class-conditional and GenEval / DPG-Bench numbers.

## Empirical Highlights
- ImageNet-256 FID 1.55 (XL/16); L/16 1.79 at 459M.
- ImageNet-512 FID 1.74.
- GenEval 0.89; DPG-Bench 87.1.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.12978`
- Code: `https://github.com/Pan-Zihao/Representation-Guidance` (`code_status: released`; HTTP 200 as of 2026-10-13).
