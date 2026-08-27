---
id: method:gated-deltanet-2
type: method
title: "Gated DeltaNet 2"
category: "architecture"
status: active
papers:
  - paper:gated-deltanet-2
recipes:
  - recipe:gated-deltanet-2
claims:
  - benchmark: "Long-Sequence Associative Recall"
    metric: "recall accuracy & throughput"
    value: "Closes gap with full attention at O(N) training compute"
    baseline: "Mamba-2 / DeltaNet"
    date: "2026-08-26"
    verified: true
    notes: "Dynamic associative delta memory updates with hardware-efficient chunkwise formulation."
tags:
  - architecture
  - linear-attention
  - recurrent
  - gated-deltanet
---

# Gated DeltaNet 2

## Method Overview
Gated DeltaNet 2 incorporates an enhanced dynamic delta memory rule into linear recurrent networks, updating associative memory matrices via fast chunkwise matrix multiplications on GPU tensor cores.

## When to Use
- Ultra-long context sequence processing with linear training complexity and constant generation memory.
