---
id: paper:soap-muon-scale
type: paper
title: "Large-Scale Second-Order Optimization in Megatron-LM"
authors:
  - "NVIDIA NeMo Team"
year: 2026
month: 7
arxiv_id: "2607.20548"
url: "https://arxiv.org/abs/2607.20548"
methods:
  - method:soap-muon-scale
cites:
  - paper:soap
  - paper:muon-optimizer-paper
tags:
  - optimizer
  - megatron
  - large-batch
---

# Large-Scale Second-Order Optimization in Megatron-LM

## Abstract Summary
This July 2026 NVIDIA study analyzes optimizer scaling in Megatron-LM across batches up to 100M tokens, establishing that KL-SOAP outperforms Muon at large batch sizes when memory allows the additional optimizer state.

## Open Source Repository
- Implementation: `https://github.com/NVIDIA-NeMo/Emerging-Optimizers`
