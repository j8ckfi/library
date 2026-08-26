---
id: paper:bitnet-b158
type: paper
title: "The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits (BitNet Scaling & Architecture)"
authors:
  - "Shuming Wang"
  - "Hongyu Wang"
  - "Shaohan Huang"
  - "Furu Wei"
year: 2025
month: 4
arxiv_id: "2504.12285"
url: "https://arxiv.org/abs/2504.12285"
methods:
  - method:bitnet-b158
cites:
  - paper:bitnet-b158-paper
tags:
  - compression
  - quantization
  - ternary
  - 1bit
  - bitnet
---

# The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits (BitNet Scaling & Architecture)

## Abstract Summary
This comprehensive work (arXiv:2504.12285, building on the 2402.17764 architecture) details the 1.58-bit ternary language modeling framework. Ternary BitLinear models trained natively from scratch match full-precision FP16 Transformer performance across perplexity and zero-shot downstream tasks, while substantially reducing memory latency, throughput latency, and energy consumption.

## Open Source Repository
- Implementation: `https://github.com/microsoft/BitNet`
- Inference Engine: `bitnet.cpp`
