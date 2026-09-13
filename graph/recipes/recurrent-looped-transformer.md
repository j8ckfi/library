---
id: recipe:recurrent-looped-transformer
type: recipe
title: "Recurrent Looped Transformer Stub"
method: method:recurrent-looped-transformer
task: task:recurrent-encoder-decoder-lm
target_hardware: "unspecified (report only; no trainer)"
framework: "none (mechanisms report)"
repo_url: "https://github.com/yifanzhang-pro/recurrent-looped-tranformer"
code_status: partial
pip_dependencies: []
tags:
  - recipe
  - rlt
  - recurrent
  - encoder-decoder
---

# Recurrent Looped Transformer Stub

## Hardware & Environment Setup
- GitHub (spelling is `tranformer`): `https://github.com/yifanzhang-pro/recurrent-looped-tranformer`
- Site: `https://yifanzhang-pro.github.io/recurrent-looped-tranformer/`
- English report: `Recurrent_Looped_Transformer.pdf` in that repo. No training or inference code as of 2026-09-12 (`code_status: partial`).
- Reference depth: 48 encoder + 48 decoder layers. Optional sharing of compatible attention/FFN weights across stages.

## Quickstart Implementation

```python
from dataclasses import dataclass


@dataclass
class DecoderState:
    hidden: object
    swa_kv: object


def rlt_step(encoder_token, prev: DecoderState, encoder_memory, decoder, merge, t: int) -> DecoderState:
    """One token: merge encoder token with previous hidden; decoder reads prefix KV and layerwise SWA."""
    merged = merge(encoder_token, prev.hidden)
    hidden, swa_kv = decoder(merged, encoder_memory, prev.swa_kv, t)
    return DecoderState(hidden=hidden, swa_kv=swa_kv)
```

## Critical Hyperparameters & Tuning Advice
- Do not reset `DecoderState` at the prompt–response boundary.
- Exact current-policy replay rebuilds encoder memory and SWA KV under current weights before scoring actions.
- Full BPTT includes hidden, decoder KV, and encoder memory. Detaching any of these is an approximation.
- This is not DeepSeek-V4.1-Flash serving and not SMELT looping.
