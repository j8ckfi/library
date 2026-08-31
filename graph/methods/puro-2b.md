---
id: method:puro-2b
type: method
title: "Puro-2B (Consumer-GPU Dense Pretrain Recipe)"
category: "architecture"
status: sota
sota_for:
  - task:budget-consumer-pretrain
supersedes: []
papers:
  - paper:puro-2b
recipes:
  - recipe:puro-2b
claims:
  - benchmark: "15-task math/code/reasoning/knowledge aggregate"
    metric: "rental-equivalent reproduction cost vs Qwen2.5-1.5B"
    value: "Canonical run ~$6.9K / 22,514 GPU-h / 1.4T tokens approaches Qwen2.5-1.5B"
    baseline: "Open-recipe 3B-class reproductions (SmolLM3-3B ~$719K; Llama-3.2-3B >$1.5M under paper accounting)"
    date: "2026-08-31"
    verified: true
    notes: "Phase 1 24x RTX 5090 / 438.84B tokens; Phase 2 96x RTX 5090 / 959.99B tokens. Sequence 4096, GBS 1536."
  - benchmark: "Puro Cost Scaling Law (uniform Phase 2, no CMA)"
    metric: "cost to match Qwen2-1.5B aggregate"
    value: "Uniform-data ~$4.4K checkpoint exceeds Qwen2-1.5B"
    baseline: "Qwen2-1.5B"
    date: "2026-08-31"
    verified: true
    notes: "Scale-down fit from shared Phase 1; CMA canonical run is a further 2.40x uniform-equivalent cost-efficiency gain on the paper's accounting, not a universal scaling law."
  - benchmark: "Blockwise FP8 vs BF16 at 1.7B (TPP=20 ladder)"
    metric: "throughput and quality-equivalent compute"
    value: "~1.36x median throughput; 98.0% BF16-equivalent quality"
    baseline: "Matched BF16"
    date: "2026-08-31"
    verified: true
    notes: "E4M3 GEMMs, 128 / 128x128 scales, MXFP8 path on SM120. From init, no BF16 warmup. Master weights and optimizer states stay BF16/FP32."
tags:
  - pretraining
  - budget
  - consumer-gpu
  - fp8
  - muonh
  - puro-2b
  - sota
---

# Puro-2B (Consumer-GPU Dense Pretrain Recipe)

## Method Overview
Puro-2B is an end-to-end from-scratch recipe for a dense ~2B model on RTX 5090:
1. **Architecture**: Qwen3-1.7B layout with untied embeddings / `lm_head` (~2B parameters). Sequence length 4096, global batch 1536 sequences.
2. **Hardware**: Consumer RTX 5090 cluster. Phase 1: 24 GPUs / 438.84B tokens. Phase 2: 96 GPUs / 959.99B tokens. Megatron Core v0.16 + Transformer Engine. No tensor parallelism; PP+DP only (Phase 1 PP=2 DP=12; Phase 2 PP=4 DP=24). Optional unsupported P2P/GDR driver tweaks; stock drivers still run at lower interconnect bandwidth.
3. **Blockwise FP8**: Transformer linear GEMMs in E4M3 with 128 (activations) / 128x128 (weights) scales on the Blackwell MXFP8 path. Master weights and optimizer states remain BF16/FP32. FP8 from random init, no BF16 warmup.
4. **MuonH**: Wrap scale-invariant 2D attention/MLP matrices. After each Muon step, project back to the initial Frobenius radius $R=\|W_0\|_F$ and apply $\widetilde{W}_{t+1}=W_t-\eta_t R\hat{u}_t$, then $W_{t+1}=R\cdot\mathrm{Normalize}(\widetilde{W}_{t+1})$. Embeddings, LayerNorm, `lm_head`, and the rest stay AdamW. Hyperball LR $=10\times$ base LR. Phase 1 power schedule, then Phase 2 long linear decay.
5. **Curriculum Model Averaging (CMA)**: 376 within-source quality-rank buckets, late constant-LR continuation from step 218,000, equal average of 6 late checkpoints.
6. **Data**: Proxy-guided open mix materialized by Kaiyuan-Spark.

## When to Use
- When training a ~1.5-2B dense LM from scratch on consumer GPUs or a tight dollar budget.
- When the 7B datacenter stack is out of reach and the goal is a reproducible open recipe, not a frontier 7B.

## Relation to Existing SOTA
- First-hop for `task:budget-consumer-pretrain` only. Does **not** replace `method:muon2` + `method:soap-muon-scale` as the dense ~7B optimizer default, `method:olmo-3` as the open 7B/instruct data recipe, or `method:quartet-ii` as native NVFP4 hardware training.
- MuonH is a Muon / Muon2-family wrapper used inside this recipe. It is documented on `method:muon2`; it does not change Muon2's `sota_for`.

## Gotchas & Failure Modes
- RTX 5090 P2P/GDR driver modifications are unsupported. The recipe still runs on stock drivers at lower interconnect bandwidth.
- FP8 here is blockwise E4M3 / MXFP8, **not** NVFP4 Quartet-II.
- Reported ~$6.9K / ~$4.4K figures are production pretrain GPU-hours only, not total lab spend.
- No TP: communication-limited consumer GPUs make intra-layer TP a bad fit.
