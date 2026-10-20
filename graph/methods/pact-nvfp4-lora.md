---
id: method:pact-nvfp4-lora
type: method
title: 'PACT NVFP4 LoRA'
category: peft
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: '4-bit PEFT speed/recipe default'
  reason: 'AQLoRA-Q / AutoQRA remain the 4-bit stack default; PACT is NVFP4 data-flow LoRA on Blackwell consumer GPUs'
  use_instead: method:aqlora-q
- when: 'Actor-then-Critic token credit (library method:pact)'
  reason: 'This PACT is NVFP4 LoRA, not axiomatic token credit'
  use_instead: method:pact
assumptions:
- 'Blackwell consumer GPU with native NVFP4 GEMM. Paper: 16 GB RTX 5080, 1B-3B SLMs.'
- 'Distinct from method:pact (Actor-then-Critic). No public code as of 2026-10-20.'
last_reviewed: '2026-10-20'
papers:
- paper:pact-nvfp4-lora
recipes:
- recipe:pact-nvfp4-lora
claims:
- benchmark: '16 GB RTX 5080 LoRA FT; linear NVFP4 vs BF16 GEMM'
  metric: 'memory, step time, adaptation quality vs BF16 LoRA'
  value: 'NVFP4 GEMMs ~6-7x vs BF16 at bs=4, seq=1024; lower memory and faster LoRA with competitive accuracy'
  baseline: 'BF16 LoRA; QLoRA-style 4-bit weights with high-precision compute'
  date: '2026-10-20'
  verified: true
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.25048'
  notes: 'GPTQ-adapted NVFP4 calibration; RMSNorm reuse; gate/up activations saved in NVFP4. Does not replace AQLoRA-Q.'
tags:
- peft
- nvfp4
- lora
- active
---

# PACT NVFP4 LoRA

## Method Overview
Consumer-GPU LoRA that runs frozen projections as native NVFP4 GEMMs, reuses quantized RMSNorm outputs, stores gate/up activations in NVFP4 for backward, keeps BF16 for forward nonlinearities, and calibrates frozen weights offline with GPTQ adapted to NVFP4 scales.

## When to Use
- Fine-tuning a 1B-3B model on a Blackwell 16 GB card where BF16 LoRA activations do not fit.

## When NOT to Use
Generic 4-bit PEFT default → `method:aqlora-q`. Token-level critic PACT → `method:pact`.

## Relation to Existing SOTA
Active plug-in on `task:4bit-peft-quantization` (`sota_for: []`). Does **not** replace AQLoRA-Q or AutoQRA.

## Gotchas & Failure Modes
- Name collides with `method:pact` (Actor-then-Critic).
- Needs native NVFP4 GEMM.
