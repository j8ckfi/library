---
id: method:mixture-of-kittens
type: method
title: "Mixture-of-Kittens (MoK)"
category: "systems"
status: sota
sota_for:
  - task:train-moe-nvl72
supersedes: []
papers:
  - paper:mixture-of-kittens
recipes:
  - recipe:mixture-of-kittens
claims:
  - benchmark: "Kernel-Level MoE Dispatch + SwiGLU + Combine (MXFP8)"
    metric: "forward / backward speedup vs DeepEP/TE/HybridEP/NCCL"
    value: "2.37x fwd / 1.78x bwd"
    baseline: "DeepEP / TransformerEngine / HybridEP / NCCL"
    date: "2026-08-26"
    verified: true
    notes: "Deterministic fused megakernel on Blackwell GB300 NVL72."
  - benchmark: "Kernel-Level MoE Dispatch + SwiGLU + Combine (BF16)"
    metric: "forward / backward speedup vs DeepEP/TE/HybridEP/NCCL"
    value: "1.92x fwd / 1.58x bwd"
    baseline: "DeepEP / TransformerEngine / HybridEP / NCCL"
    date: "2026-08-26"
    verified: true
    notes: "Deterministic fused megakernel on Blackwell GB300 NVL72."
  - benchmark: "Production 512-GPU End-to-End Training (GB300 NVL72)"
    metric: "training throughput (tok/s/GPU)"
    value: "1070.2 tok/s/GPU (1.41x vs 760.9 prior DeepEP stack)"
    baseline: "Prior DeepEP stack (760.9 tok/s/GPU)"
    date: "2026-08-26"
    verified: true
    notes: "Production 512-GPU Composer training on GB300 NVL72 racks."
tags:
  - systems
  - megakernel
  - moe
  - nvl72
  - blackwell
  - mxfp8
  - bf16
  - mok
  - mixture-of-kittens
  - sota
---

# Mixture-of-Kittens (MoK)

## Method Overview
Mixture-of-Kittens (MoK) is a deterministic training systems megakernel engineered for large-scale Mixture-of-Experts (MoE) architectures on NVIDIA Blackwell NVL72 systems. Rather than executing separate communication (All-to-All dispatch/combine) and compute (SwiGLU GEMM) phases, MoK fuses the entire lifecycle into a unified GPU megakernel.

Key architectural mechanics:
- **Fused Megakernel Pipeline**: Integrates token dispatch, expert FFN evaluation (SwiGLU), and token combine into a single execution stream.
- **Asynchronous Pull Dispatch & Push Combine**: Replaces bulk collective synchronization with fine-grained point-to-point peer communication across NVLink fabrics, reducing synchronization latency from 103 µs to 18 µs.
- **Ring Token Buffer**: Manages token routing without CPU-GPU synchronization, avoiding pipeline stalls and preventing dropped tokens under load imbalance.
- **Precision Support**: Native execution for BF16 and micro-scaled FP8 (MXFP8) weights and activations.
- **Hardware Primitives**: Implemented with ThunderKittens tile abstractions targeting Blackwell SM100 and SM103 architectures.

## Target Architectures & Templates
MoK is designed to train DeepSeek-V3/V4-style MoE architectures featuring shared and fine-grained routed experts:
- **DeepSeek-V4** (`method:deepseek-v4`): Frontier fine-grained MoE architecture.
- **Kimi-K3** (`method:kimi-k3`): High-throughput MoE architecture template.
- **Nemotron-3 Super Latent MoE** (`method:nemotron-3-super-latentmoe`): Latent-routed MoE models.

## When to Use
- Pretraining or continuous pretraining of large-scale sparse MoE models on NVL72 rack-scale systems (Blackwell GB200/GB300 NVL72).
- Eliminating communication bubbles and kernel launch overheads in MoE dispatch and combine layers.

## Hardware Requirements & Constraints
- **Hardware Floor**: Requires NVIDIA Blackwell NVL72-class clusters (SM100/SM103) with symmetric memory support; not intended for single-node or consumer GPUs.
- **Software Stack**: PyTorch 2.10+, CUDA 13.0+, ThunderKittens.
