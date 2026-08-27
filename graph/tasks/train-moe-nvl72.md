---
id: task:train-moe-nvl72
type: task
title: "Train Mixture-of-Experts (MoE) on NVL72 Systems"
domain: "systems"
summary: "High-throughput, deterministic pretraining of sparse Mixture-of-Experts (MoE) architectures on rack-scale NVIDIA Blackwell NVL72 clusters."
current_sota:
  - method: method:mixture-of-kittens
    as_of: "2026-08-26"
    benchmark: "Production 512-GPU MoE Pretraining (GB300 NVL72)"
    metric: "tokens/sec per GPU"
    value: "1070.2 tok/s/GPU (1.41x vs DeepEP)"
    notes: "Mixture-of-Kittens (MoK) fused dispatch + SwiGLU + combine megakernel on Blackwell NVL72s."
methods:
  - method:mixture-of-kittens
tags:
  - systems
  - pretraining
  - moe
  - nvl72
  - blackwell
  - megakernel
---

# Train Mixture-of-Experts (MoE) on NVL72 Systems

## Problem Definition
Training massive sparse Mixture-of-Experts (MoE) models across hundreds or thousands of GPUs is heavily communication-bound. Conventional MoE training frameworks suffer from high communication overhead during all-to-all token dispatch and combine, CPU-GPU synchronization bottlenecks, and underutilized tensor cores during expert FFN computation.

## Evaluation Protocol & Benchmarks
- **Megakernel Latency**: Forward and backward pass execution time for dispatch, SwiGLU, and combine operations under BF16 and MXFP8 precision compared to DeepEP, TransformerEngine, and HybridEP.
- **End-to-End Cluster Throughput**: Tokens per second per GPU on multi-node NVL72 clusters (e.g. 512-GPU GB300 NVL72).
- **Determinism**: Exact numerical reproducibility across distributed training runs.

## SOTA Recommendation (as of 2026-08-26)
- **Primary Systems Megakernel**: **Mixture-of-Kittens (MoK)** (`method:mixture-of-kittens`, `paper:mixture-of-kittens`, `recipe:mixture-of-kittens`).
- **Target Model Architectures**: **DeepSeek-V4** (`method:deepseek-v4`), **Kimi-K3** (`method:kimi-k3`), and **Nemotron-3 Super Latent MoE** (`method:nemotron-3-super-latentmoe`).
