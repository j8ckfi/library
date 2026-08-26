---
id: method:mamba-2
type: method
title: "Mamba-2 & State Space Duality (SSD)"
category: "architecture"
status: sota
sota_for:
  - task:linear-time-sequence-modeling
supersedes: []
papers:
  - paper:mamba-2-paper
recipes:
  - recipe:mamba2-training
claims:
  - benchmark: "Sequence Throughput (2k-16k sequence lengths)"
    metric: "tokens/sec on H100"
    value: "2x-8x vs FlashAttention-2"
    baseline: "Standard Multi-Head Attention"
    date: "2024-05"
    verified: true
    notes: "Utilizes SSD to compute linear state-space transformations as block 1-semiseparable matrix multiplications."
tags:
  - architecture
  - linear-attention
  - state-space
---

# Mamba-2 & State Space Duality (SSD)

## Method Overview
Mamba-2 introduces **State Space Duality (SSD)**, establishing an exact theoretical and algorithmic equivalence between structured state-space models (SSMs) and linear attention mechanisms. 

In Mamba-1, selective SSM computation relied on sequential associative scan GPU kernels that did not fully leverage Tensor Core matrix multiplication units (TCs). Mamba-2 formulates the selective recurrence as a 1-semiseparable matrix transformation, enabling the core recurrence step to be computed via standard batched matrix multiplications (\(BMM\)) directly on GPU Tensor Cores.

## When to Use
- **Long-Sequence Pretraining**: Documents, genomes, audio, or codebase modeling exceeding 32k–1M context lengths.
- **Low-Latency Streaming Generation**: Requires constant \(O(1)\) recurrent state memory per token, eliminating KV cache growth.

## Gotchas & Failure Modes
- Associative recall on fine-grained in-context learning tasks can lag full softmax attention unless hybrid architectures (e.g. 10% attention layers + 90% Mamba-2 layers) are employed.
- Requires custom CUDA/Triton kernels for optimal chunked computation.
