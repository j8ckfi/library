---
id: recipe:bergson-trackstar
type: recipe
title: "Bergson TrackStar / LESS-style Query Scoring"
method: method:trackstar
task: task:training-data-attribution
target_hardware: "1x consumer or datacenter GPU (Pythia-14m smoke); LoRA-space for 7B-class small-lab / Abiome"
framework: "PyTorch / HuggingFace Transformers + Bergson 0.26.2"
repo_url: "https://github.com/EleutherAI/bergson"
pip_dependencies:
  - "bergson==0.26.2"
tags:
  - recipe
  - data-attribution
  - trackstar
  - bergson
  - less
  - small-lab
---

# Bergson TrackStar / LESS-style Query Scoring

Small-lab / Abiome path: compressed influence and LoRA-space `bergson score` / `bergson trackstar` for LESS-style filters. Complementary to AutoMixer mix-weight search: this ranks items for a query eval, it does not search source mix ratios.

## Hardware & Environment Setup

```bash
pip install bergson==0.26.2
```

## Quickstart Implementation

Smoke (random-projection index + query):

```bash
pip install bergson
bergson build runs/index --model EleutherAI/pythia-14m --dataset NeelNanda/pile-10k --truncation --token_batch_size 4096 --projection_dim 16
bergson query --index runs/index --unit_norm
```

LESS-style (mean-aggregated eval query, then score the train set):

```bash
bergson build runs/query --model <ckpt> --dataset <eval> --aggregation mean --unit_normalize --projection_dim 0
bergson score runs/scores --model <ckpt> --dataset <train> --query_path runs/query --projection_dim 16
```

TrackStar orchestration over a checkpoint:

```bash
bergson trackstar runs/trackstar --model EleutherAI/pythia-14m --query.dataset NeelNanda/pile-10k --data.dataset NeelNanda/pile-10k --data.truncation --token_batch_size 4096 --query.truncation --query.split "train[:20]"
```

Always `bergson metasmoothness` before trusting MAGIC. Influence-function damping still needs a sanity check before you filter a corpus.

## Critical Hyperparameters & Tuning Advice
- Filtering-shaped LDS for TrackStar is 0.803, not the random-subset 0.184.
- `projection_dim 16` is a smoke setting; paper TrackStar LDS used proj 1024/module.
- Fused MoE experts unsupported.
- Do not retarget `task:open-data-recipe` or `task:industrial-model-building`.
