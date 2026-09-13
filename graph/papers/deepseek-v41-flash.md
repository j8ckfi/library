---
id: paper:deepseek-v41-flash
type: paper
title: "DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression"
authors:
  - "DeepSeek-AI"
year: 2026
month: 9
arxiv_id: ""
url: "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
methods:
  - method:deepseek-v41-flash
cites:
  - paper:deepseek-v4
  - paper:mhc
tags:
  - architecture
  - moe
  - serving
  - kv-cache
  - ced
  - deepseek-v41-flash
---

# DeepSeek-V4.1-Flash: Pushing the Limits of KV Cache Compression

## Abstract Summary
DeepSeek-V4.1-Flash is a 552B-backbone multimodal MoE with up to 1M context. It uses a Causal Encoder-Decoder (CED): 20-layer causal encoder plus 20-layer decoder (40 total). Decoder global KV is projected from final encoder hidden states rather than each decoder layer's own states, so prefill activates about 8B parameters per token and decode about 16B. Compressed Sparse Attention 2 (CSA2) assigns Full / Reindex / Reuse modes with a Hierarchical Sparse Indexer and FP4 main KV (~890 bytes/token global KV, about 1/4 of V4-Flash). SWA Bounded Replay rebuilds the last \(n_{\mathrm{win}}\) tokens so persistent KV is about 1/8 of V4-Flash. Additional pieces: Single-Pass mHC, Engram conditional memory (196B, token lookup), DSpark speculative decoding. MoE: 1 shared + 384 routed experts, activate 6. Pretrained on 45T multimodal tokens. Post-train is standard SFT → RL → OPD; the data pipeline is what changed.

## Key Contributions
1. **CED serving architecture** for input-heavy agentic workloads (asymmetric 8B prefill / 16B decode).
2. **CSA2 + FP4 main KV** to 890 bytes/token global KV.
3. **SWA Bounded Replay** to cut persistent KV without storing SWA KV on SSD.
4. **Open weights** and a reference inference / encoding stack on Hugging Face.

## Empirical Highlights
- Instruct, max reasoning effort (vendor card): Terminal-Bench 2.1 90.6 vs V4-Flash 82.7 vs V4-Pro 87.9; DeepSWE v1.1 74.2 vs 54.4 / 62.7; AutomationBench 54.8; Agent's Last Exam 31.8.
- Base vs V4-Flash-Base / V4-Pro-Base on internal evals (same framework): MMLU-Pro 74.1 vs 68.3 / 73.5; HumanEval 79.4 vs 69.5 / 76.8.
- API news (2026-09-10): `deepseek-flash` live; V4-Flash and V4-Flash-Vision-Exp retired (compat aliases route to V4.1-Flash); V4-Pro phased out (requests route to V4.1-Flash from 2026-09-14 04:00 UTC until V4.1-Pro).

## Open Source Repository & Resources
- Weights + tech report: `https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash` (`DeepSeek_V41_Tech_Report.pdf`)
- Prompt encoding toolkit: `https://github.com/deepseek-ai/deepseek-recipe`
- News: `https://www.deepseek.com/en/news/deepseek-v4-1-flash/`
- No from-scratch pretrain trainer (`recipe:deepseek-v41-flash` `code_status: partial`).
