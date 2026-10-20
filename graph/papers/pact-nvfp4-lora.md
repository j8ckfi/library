---
id: paper:pact-nvfp4-lora
type: paper
title: 'PACT: NVFP4 Data-Flow LoRA Fine-Tuning on Consumer GPUs'
authors:
- 'Lei Gao'
- 'Hossein Entezari Zarch'
- 'Chaoyi Jiang'
- 'Murali Annavaram'
year: 2026
month: 10
arxiv_id: '2610.25048'
url: https://arxiv.org/abs/2610.25048
methods:
- method:pact-nvfp4-lora
cites:
- paper:aqlora
tags:
- peft
- nvfp4
- lora
- active
---

# PACT NVFP4 LoRA

## Abstract Summary
LoRA on Blackwell consumer GPUs using native NVFP4 GEMMs for frozen projections, NVFP4 saved activations, and GPTQ-adapted NVFP4 calibration. On a 16 GB RTX 5080, NVFP4 GEMMs are about 6-7x BF16 at batch 4 / seq 1024 with competitive adaptation quality.

## Key Contributions
1. NVFP4 data-flow LoRA distinct from library method:pact (Actor-then-Critic).

## Empirical Highlights
- Targets 1B-3B SLMs that fit for inference but not for BF16 LoRA training.

## Open Source Repository & Resources
- Paper: `https://arxiv.org/abs/2610.25048`
- Code: `none found` (`code_status: none`).
