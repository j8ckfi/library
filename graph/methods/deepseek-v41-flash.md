---
id: method:deepseek-v41-flash
type: method
title: "DeepSeek-V4.1-Flash (Causal Encoder-Decoder)"
category: "architecture"
status: sota
sota_for:
  - task:input-heavy-agentic-moe-serving
supersedes: []
do_not_use_for:
  - when: "choosing the frontier MoE pretrain architecture template"
    reason: "V4.1-Flash CED is an input-heavy serving family, not a silent replacement of the V4 MoE pretrain template"
    use_instead: "method:deepseek-v4"
  - when: "GitHub issue to patch / SWE harness"
    reason: "This is a model + KV architecture; the harness default stays mini-SWE-agent"
    use_instead: "method:mini-swe-agent"
  - when: "frontier RL post-train engine"
    reason: "Miles remains the production post-train stack"
    use_instead: "method:miles"
  - when: "lossless multi-token / diffusion-augmented AR serving"
    reason: "DSpark is Flash's speculative path; Uno remains the diffusion-augmented AR first hop"
    use_instead: "method:uno"
  - when: "recurrent all-token CED LM with exact RL replay semantics (experimental)"
    reason: "RLT is the experimental recurrence report; Flash does not claim all-token train/replay identity"
    use_instead: "method:recurrent-looped-transformer"
  - when: "Pass@1 labeled math/code RLVR algorithm"
    reason: "Post-train recipe is SFT→RL→OPD; CISPO remains the dense Pass@1 kernel"
    use_instead: "method:cispo"
assumptions:
  - "552B backbone MoE, 1 shared + 384 routed experts, activate 6. Prefill ~8B active/token; decode ~16B. Context up to 1M. Pretrained on 45T multimodal tokens (sparse attention at 64K; 1M extension at 34T)."
  - "CED: 20-layer causal encoder + 20-layer decoder. Decoder global KV from final encoder states. CSA2 Full/Reindex/Reuse + Hierarchical Sparse Indexer. FP4 main KV (E2M1, one E4M3 scale per 16 channels)."
  - "Weights and reference inference live on Hugging Face. No public from-scratch trainer. API model deepseek-flash. V4-Flash / V4-Flash-Vision-Exp retired (compat aliases). V4-Pro routed to V4.1-Flash from 2026-09-14 04:00 UTC until V4.1-Pro."
last_reviewed: "2026-09-12"
papers:
  - paper:deepseek-v41-flash
recipes:
  - recipe:deepseek-v41-flash
claims:
  - benchmark: "Instruct DeepSeek-V4.1-Flash vs V4-Flash / V4-Pro, max reasoning effort"
    metric: "Terminal-Bench 2.1 Pass@1 / DeepSWE v1.1 Resolved"
    value: "90.6 / 74.2"
    baseline: "V4-Flash 82.7 / 54.4; V4-Pro 87.9 / 62.7; Opus-5.0 TB2.1 89.1 / DeepSWE 74.0"
    date: "2026-09-10"
    verified: true
    evidence_level: "self-reported"
    source_url: "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
    notes: "Vendor card. DeepSWE uses mini-SWE harness in the official setup; TB2.1 uses DeepSeek Harness Minimal, 1M context. Not a mini-SWE-agent retarget."
  - benchmark: "Global KV cache vs DeepSeek-V4-Flash"
    metric: "bytes per token"
    value: "890"
    baseline: "V4-Flash ~4× larger; persistent KV ~1/8 of V4-Flash after SWA Bounded Replay"
    date: "2026-09-10"
    verified: true
    evidence_level: "self-reported"
    source_url: "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
    notes: "CSA2 + FP4 main KV → ~890 B/token global KV. SWA Bounded Replay reconstructs last n_win tokens so SWA KV is not persisted to SSD."
  - benchmark: "CED activation"
    metric: "active parameters per token"
    value: "8B prefill / 16B decode"
    baseline: "V4-Flash-Base 13B activated (single figure on the card)"
    date: "2026-09-10"
    verified: true
    evidence_level: "self-reported"
    source_url: "https://huggingface.co/deepseek-ai/DeepSeek-V4.1-Flash"
    notes: "552B backbone. Decoder global KV projected from final encoder states, not per-decoder-layer hidden states."
tags:
  - architecture
  - moe
  - serving
  - kv-cache
  - ced
  - deepseek-v41-flash
  - sota
---

# DeepSeek-V4.1-Flash (Causal Encoder-Decoder)

## Method Overview
Causal Encoder-Decoder (CED) for a 552B multimodal MoE. A 20-layer causal encoder writes global memory. A 20-layer decoder reads that memory and keeps local SWA. Decoder **global** KV is a projection of the *final encoder* states, so prefill can run the encoder path (~8B active) and decode the heavier path (~16B).

Components kept on this card (not separate graph methods):
- **CSA2**: each attention layer is statically Full, Reindex, or Reuse (share main KV and indexer K; reuse Top-K indices). Hierarchical Sparse Indexer restricts later indexer layers to a candidate pool from the first Full layer.
- **SWA Bounded Replay**: replay the last \(n_{\mathrm{win}}\) tokens instead of persisting SWA KV.
- **Single-Pass mHC**: residual-stream mixing with a Mega-mHC kernel; see `method:mhc` for the original Sinkhorn mHC. This is a serving-kernel revision, not a supersession of mHC.
- **Engram**: 196B conditional memory via token lookup.
- **DSpark**: semi-autoregressive draft with confidence-scheduled verification (not Uno).

MoE: 1 shared + 384 routed, activate 6. Vision: DeepSeek-ViT from scratch + 2-layer MLP projector, joint with text from the start of pretrain. Post-train: SFT → RL → OPD with a larger agent-task data pipeline and a 1–100 reasoning-effort knob.

## When to Use
- Input-heavy agentic or long-context MoE serving where KV HBM/SSD and prefill FLOPs dominate, and you can consume `deepseek-ai/DeepSeek-V4.1-Flash` (or the `deepseek-flash` API).

## When NOT to Use
- Pretrain-template choice → `method:deepseek-v4` / `method:kimi-k3`. SWE loop → `method:mini-swe-agent`. Post-train engine → `method:miles`. Diffusion-augmented AR → `method:uno`. Experimental all-token recurrence → `method:recurrent-looped-transformer`.

## Relation to Existing SOTA
- First hop on `task:input-heavy-agentic-moe-serving` only. Does **not** supersede `method:deepseek-v4` or `method:kimi-k3`. Cross-link `method:recurrent-looped-transformer` as an experimental conceptual sibling (encoder memory + SWA decoder) without Flash's KV measurements. Cross-link `method:mhc` for Single-Pass mHC. No `method:deepseek-v4-flash` node existed to supersede; V4-Flash is a retired API alias in the news post.

## Gotchas & Failure Modes
- Agentic numbers are vendor-reported and harness-specific (DSH Minimal vs mini-SWE vs Claude Code). Do not mix boards.
- Compat routing: `deepseek-v4-flash` and `deepseek-v4-flash-vision-exp` currently point at V4.1-Flash; V4-Pro follows on 2026-09-14 until V4.1-Pro.
- No public pretrain code. Inference folder is a readable reference, not a production engine.
- Engram adds 196B lookup parameters on top of the 552B backbone; do not quote 552B as the only stored size if you are sizing disks.
