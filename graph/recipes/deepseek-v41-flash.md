---
id: recipe:deepseek-v41-flash
type: recipe
title: "DeepSeek-V4.1-Flash CED Serving Recipe"
method: method:deepseek-v41-flash
task: task:input-heavy-agentic-moe-serving
target_hardware: "multi-node GPU inference (HF convert.py default MP=8); production serving unspecified"
framework: "PyTorch reference inference + deepseek-recipe encoding"
repo_url: "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
code_status: partial
pip_dependencies:
  - "torch"
  - "safetensors"
  - "deepseek-recipe"
tags:
  - recipe
  - deepseek-v41-flash
  - serving
  - ced
  - kv-cache
---

# DeepSeek-V4.1-Flash CED Serving Recipe

## Hardware & Environment Setup
- Weights + tech report: `https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash` (`DeepSeek_V41_Tech_Report.pdf`).
- Reference inference (convert + generate, not a production engine): `inference/` in that repo. Convert with `--expert-dtype fp4` and tensor-parallel rank files.
- Prompts: `encoding/encoding.py` in the same repo, or `https://github.com/deepseek-ai/deepseek-recipe` (Rust + Python bindings). No Jinja chat template.
- API: model `deepseek-flash`. V4-Flash and V4-Flash-Vision-Exp retired; aliases route here. V4-Pro routes here from 2026-09-14 04:00 UTC until V4.1-Pro.
- No from-scratch pretrain trainer (`code_status: partial`).
- Sampling on the card: temperature 1.0, top_p 0.95 or 1.0, context 1M, max_tokens ≥ 256K. Reasoning effort integer 1–100.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass(frozen=True)
class CedBudget:
    backbone_params: int = 552_000_000_000
    prefill_active: int = 8_000_000_000
    decode_active: int = 16_000_000_000
    global_kv_bytes: int = 890
    shared_experts: int = 1
    routed_experts: int = 384
    activated_routed: int = 6
    encoder_layers: int = 20
    decoder_layers: int = 20


def persistent_kv_bytes(tokens: int, global_kv_bytes: int = 890) -> int:
    """Global KV only; SWA Bounded Replay does not persist SWA KV."""
    return tokens * global_kv_bytes
```

## Critical Hyperparameters & Tuning Advice
- Prefill is the encoder path; decode is ~2× active params. Size clusters for input-heavy agent traffic, not symmetric 13B-active V4-Flash.
- CSA2 modes are static per layer (Full / Reindex / Reuse). Hierarchical Sparse Indexer cost is bounded by the first Full layer's candidate pool.
- Single-Pass mHC is the residual mixer; do not drop `method:mhc` as a concept.
- DSpark is Flash's speculative decoder, not Uno and not a separate draft model you train.
- Agentic evals on the card mix DeepSeek Harness Minimal, mini-SWE, and Claude Code. Reproduce with the `evaluation/` folder rather than mixing boards.
