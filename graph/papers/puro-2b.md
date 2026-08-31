---
id: paper:puro-2b
type: paper
title: "Puro-2B: Poor Lab's Qwen2-1.5B Trained on RTX 5090 within $5090"
authors:
  - "Kairong Luo"
  - "Jiarui Cui"
  - "Yaorui Yin"
  - "Shengqi Chen"
  - "Yiming Yang"
  - "Linxiang Gao"
  - "Yanmohan Wang"
  - "Chengxia Li"
  - "Mingzhe Zhang"
  - "Kaifeng Lyu"
  - "Wenguang Chen"
year: 2026
month: 8
arxiv_id: "2608.27370"
url: "https://arxiv.org/abs/2608.27370"
methods:
  - method:puro-2b
cites:
  - paper:muon-optimizer-paper
  - paper:olmo-3
  - paper:deepseek-v3
tags:
  - pretraining
  - budget
  - consumer-gpu
  - fp8
  - muonh
  - puro-2b
---

# Puro-2B: Poor Lab's Qwen2-1.5B Trained on RTX 5090 within $5090

## Abstract Summary
Open-weight and open-recipe models still leave small labs unable to reproduce pretraining: even Llama-3.2-3B is estimated over $1.5M and SmolLM3-3B over $700K under the paper's rental accounting. Puro-2B trains a dense ~2B Qwen3-1.7B-architecture model (untied embed / lm_head) from scratch on up to 1.4T tokens with blockwise FP8 on consumer RTX 5090 GPUs. The canonical curriculum run costs about $6.9K (22,514 GPU-hours) and approaches Qwen2.5-1.5B under the paper protocol. A uniform-data Phase 2 run at about $4.4K exceeds Qwen2-1.5B. Efficiency comes from hardware choice, blockwise FP8, Muon with Hyperball (MuonH), curriculum model averaging, and a proxy-guided open data mix.

## Key Contributions
1. **Affordable from-scratch 2B recipe**: RTX 5090 cluster, Megatron Core v0.16, PP+DP only, two-phase 1.4T-token schedule, Apache-2.0 code, data, and weights.
2. **Co-designed efficiency stack**: Blockwise E4M3/MXFP8 from init (~1.36x throughput, 98% BF16-equivalent quality), MuonH on attention/MLP matrices, CMA (376 within-source buckets, constant-LR from step 218k, average of 6 late ckpts), Kaiyuan-Spark proxy mix.
3. **Puro Cost Scaling Law**: Recipe-specific scale-down fit of aggregate score versus rental cost on uniform Phase 2; the $4.4K uniform checkpoint crosses Qwen2-1.5B.

## Empirical Highlights
- Canonical: Phase 1 24 GPUs / 438.84B tokens / $1.84K; Phase 2 96 GPUs / 959.99B tokens / $5.05K; total 22,514 GPU-h, ~$6.89K.
- Uniform $4.4K run (shared Phase 1, 480B Phase 2 tokens) exceeds Qwen2-1.5B without CMA.
- Seq 4096, GBS 1536. Hyperball LR $=10\times$ base LR.

## Open Source Repository & Resources
- Training code: `https://github.com/thu-pacman/Puro-Megatron`
- Data processing: `https://github.com/thu-pacman/Kaiyuan-Spark`
- Weights and data: `https://huggingface.co/collections/thu-pacman/puro-2b`
