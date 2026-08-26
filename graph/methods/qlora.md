---
id: method:qlora
type: method
title: "QLoRA (Quantized 4-bit Low-Rank Adaptation)"
category: "peft"
status: sota
sota_for:
  - task:parameter-efficient-fine-tuning
supersedes: []
papers:
  - paper:qlora
  - paper:qlora-paper
recipes:
  - recipe:qlora-peft
claims:
  - benchmark: "Vicuna Benchmark / MMLU"
    metric: "99.3% recovery of full 16-bit performance"
    value: 99.3
    baseline: "16-bit Full Fine-Tuning"
    date: "2023-05"
    verified: true
    notes: "Utilizes 4-bit NormalFloat (NF4), Double Quantization, and Paged Optimizers."
tags:
  - peft
  - quantization
  - memory-efficient
---

# QLoRA (Quantized 4-bit Low-Rank Adaptation)

## Method Overview
QLoRA reduces the memory footprint of fine-tuning large models to fit onto a single consumer GPU (e.g. 33B model on a 24GB RTX 4090). 

It introduces three core innovations:
1. **NF4 (4-bit NormalFloat)**: An information-theoretically optimal quantile quantization data type for normally distributed weights.
2. **Double Quantization (DQ)**: Quantizing the quantization constants themselves, saving ~0.37 bits per parameter.
3. **Paged Optimizers**: Utilizing CUDA Unified Memory to automatically page optimizer states between GPU and CPU RAM during gradient spikes.

## When to Use
- **Consumer Hardware Fine-Tuning**: Fine-tuning 8B–70B parameter models when multi-node or 80GB H100 clusters are unavailable.
- **High-Throughput Adapter Training**: Training dozens of task-specific adapters simultaneously on a single host.

## Gotchas & Failure Modes
1. **Wall-Clock Slowdown**: On-the-fly dequantization of NF4 weights to FP16/BF16 adds 20–30% compute overhead compared to unquantized 16-bit LoRA.
2. **Quantization Precision Loss on Small Models**: Models under 3B parameters can suffer noticeable degradation when quantized to 4-bit compared to 16-bit base models.
