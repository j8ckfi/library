---
id: task:budget-consumer-pretrain
type: task
title: "Budget Consumer-GPU Dense Pretraining (~1.5-2B)"
domain: "pretraining"
summary: "Train a ~1.5-2B dense language model from scratch on consumer GPUs and a tight dollar budget, not a 7B datacenter run."
current_sota:
  - method: method:puro-2b
    as_of: "2026-08-31"
    benchmark: "15-task math/code/reasoning/knowledge aggregate vs Qwen2-1.5B / Qwen2.5-1.5B"
    metric: "reproduction cost and aggregate score"
    value: "Canonical ~$6.9K / 22.5k GPU-h approaches Qwen2.5-1.5B; uniform $4.4K run beats Qwen2-1.5B"
    notes: "Puro-2B (2608.27370) on RTX 5090, 1.4T tokens, blockwise FP8, MuonH, CMA. Not the 7B default."
methods:
  - method:puro-2b
  - method:muon2
  - method:olmo-3
  - method:quartet-ii
tags:
  - pretraining
  - budget
  - consumer-gpu
  - dense-lm
  - puro-2b
---

# Budget Consumer-GPU Dense Pretraining (~1.5-2B)

## Problem Definition
Pretrain a dense ~1.5-2B decoder-only Transformer from scratch when the lab has consumer GPUs (RTX 5090 class) and a few-thousand-dollar compute budget. The 7B datacenter stack (Muon2 + KL-SOAP + OLMo-3 / Dolma-3) is the wrong first hop at this scale and cost.

## Evaluation Protocol
- **Primary Benchmarks**: Paper's 15-task math, code, reasoning, and knowledge aggregate versus Qwen2-1.5B and Qwen2.5-1.5B, with rental-equivalent RTX 5090 GPU-hour accounting.
- **Evaluation Pitfalls**: Headline cost is production Phase 1+2 accelerator hours only (excludes data prep, proxies, failed runs, post-training). Do not treat this as a 7B optimizer pick or as native NVFP4 training.

## SOTA Recommendation (as of 2026-08-31)
- **Primary Method**: **Puro-2B** (`method:puro-2b`, `paper:puro-2b` `arXiv:2608.27370`).
- **Not This Task**: `method:muon2` + `method:soap-muon-scale` remain the dense ~7B optimizer default. `method:olmo-3` remains the open 7B/instruct data recipe. `method:quartet-ii` remains native NVFP4 hardware training.
