---
id: method:dualquant
type: method
title: DualQuant
category: quantization
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: native FP4 forward/backward hardware training from scratch
  reason: DualQuant is calibration-free W+A PTQ; Quartet-II remains NVFP4 training
  use_instead: method:quartet-ii
- when: FP4 W4A4 noise law / spectrum-flattening (KBBQ)
  reason: KBBQ is a noise-law transform; DualQuant is dual-scale reconstruction MSE
  use_instead: method:kbbq
- when: memory must fit a 4-bit PEFT stack
  reason: AQLoRA-Q remains 4-bit PEFT; DualQuant is inference W+A PTQ
  use_instead: method:aqlora-q
assumptions:
- W4A4 / MX / NVFP4 inference PTQ on Llama and Qwen. Paper includes a packed W4A4 path on RTX 4090 for
  Llama-3.1-8B.
- No official GitHub as of 2026-10-12.
last_reviewed: '2026-10-12'
papers:
- paper:dualquant
recipes:
- recipe:dualquant
claims:
- benchmark: Llama/Qwen WikiText-2, C4, zero-shot; packed W4A4 Llama-3.1-8B on RTX 4090
  metric: accuracy vs SmoothQuant / calibration-free baselines; memory and throughput
  value: matches or exceeds SmoothQuant on most models/formats without calibration; up to 2.61× memory
    reduction on the packed W4A4 path
  baseline: SmoothQuant; calibration-free PTQ baselines
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13767
  notes: First dual-scaling method the paper claims for MX and NV block formats. Does not retarget Quartet-II.
tags:
- quantization
- ptq
- w4a4
- dualquant
- active
---

# DualQuant

## Method Overview
Solve a non-differentiable dual-scale reconstruction problem with block coordinate descent. Reuse those scales as per-channel activation rescalings. No calibration set.

## When to Use
- W4A4 / MX / NVFP4 inference PTQ when you cannot or will not collect calibration activations.

## When NOT to Use
Native FP4 training → `method:quartet-ii`. W4A4 noise law → `method:kbbq`. 4-bit PEFT → `method:aqlora-q`.

## Relation to Existing SOTA
Active plug-in on `task:fp4-hardware-training` (`sota_for: []`), PTQ-style mention like KBBQ. Does **not** replace Quartet-II / MXFP4.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-12.
- Packed path is inference, not QAT.
- Do not skip the activation rescale; it is the by-product the method needs.
