---
id: paper:bitnet-b158-paper
type: paper
title: "The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits"
authors:
  - "Shuming Wang"
  - "Hongyu Wang"
  - "Shaohan Huang"
  - "Furu Wei"
year: 2024
month: 2
arxiv_id: "2402.17764"
url: "https://arxiv.org/abs/2402.17764"
methods:
  - method:bitnet-b158
cites: []
tags:
  - compression
  - quantization
  - ternary
  - 1bit
---

# The Era of 1-bit LLMs: All Large Language Models are in 1.58 Bits

## Abstract Summary
BitNet b1.58 introduces a 1-bit LLM architecture where every single weight is ternary \(\{-1, 0, 1\}\). It achieves performance parity with full-precision FP16 Transformers across perplexity and zero-shot downstream tasks, while substantially reducing memory latency, throughput latency, and power consumption by eliminating floating-point matrix multiplications.

## Key Contributions
1. **BitLinear Architecture**: Formulated ternary weight and 8-bit activation quantization for linear transformations.
2. **Matrix Addition Efficiency**: Replaced expensive FP matrix multiplications with hardware addition and subtraction.
3. **Scaling Parity**: Demonstrated identical scaling law curves to FP16 Transformers starting at 3B parameters.
