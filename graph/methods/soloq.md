---
id: method:soloq
type: method
title: SoloQ
category: quantization
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: native FP4 forward/backward hardware training from scratch
  reason: SoloQ is calibration-free dLLM inference PTQ; Quartet-II remains NVFP4 training
  use_instead: method:quartet-ii
- when: recycle an AR post-training weight delta onto a converted dLLM
  reason: A2D is AR-delta recycle; SoloQ quantizes an existing dLLM
  use_instead: method:a2d
- when: calibration-free W+A PTQ for autoregressive LLMs (DualQuant)
  reason: DualQuant is AR W+A; SoloQ rotates dLLM activations whose mask/step stats shift
  use_instead: method:dualquant
assumptions:
- Diffusion LMs (full-sequence LLaDA/Dream and block-diffusion Fast-dLLM v2 / Nemotron-Labs-Diffusion).
  HF Daily 2026-10-12.
- Announced github.com/Intelligent-Computing-Lab-Panda/SoloQ; 404 as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:soloq
recipes:
- recipe:soloq
claims:
- benchmark: LLaDA / Dream full-sequence and Fast-dLLM v2 / Nemotron-Labs-Diffusion block-diffusion, 4-bit
    / NVFP4
  metric: accuracy retention vs calibration-based PTQ; peak memory and e2e speed with NVFP4
  value: retains accuracy at 4-bit and beats calibration-based baselines; NVFP4 up to 2.61× peak-memory
    cut and 2.24× e2e inference
  baseline: calibration-based dLLM PTQ
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.07121
  notes: HF Daily 2026-10-12. Does not retarget Quartet-II or A2D. Code 404 at ingest.
tags:
- quantization
- dllm
- nvfp4
- soloq
- active
---

# SoloQ

## Method Overview
Rotate into a basis whose marginal is known. Quantize there without calibration. For block-diffusion, quantize committed KV only; keep the live denoised block intact.

## When to Use
- Deploying a dLLM at 4-bit / NVFP4 when mask/step activation shift makes calibration sets lie.

## When NOT to Use
NVFP4 training → `method:quartet-ii`. AR-delta recycle → `method:a2d`. AR W+A PTQ → `method:dualquant`.

## Relation to Existing SOTA
Active plug-in on `task:fp4-hardware-training` with a mention on `task:diffusion-lm-ar-delta-recycle` (`sota_for: []`). Does **not** replace Quartet-II or A2D.

## Gotchas & Failure Modes
- **code: announced** Intelligent-Computing-Lab-Panda/SoloQ 404 as of 2026-10-12.
- Not AR LLM PTQ. Mask/step shift is the dLLM-specific problem.
- Block-diffusion KV quant is commit-time only.
