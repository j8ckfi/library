---
id: method:multimodal-data-mixtures
type: method
title: Multimodal Data-Mixture Scaling Laws
category: data-curriculum
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: open web / Dolma-3 text mix rather than native multimodal MoE mixing
  reason: OLMo-3 remains the open text recipe; this card is text/vision/audio MoE
    mixture laws
  use_instead: method:olmo-3
- when: choosing the frontier MoE architecture template
  reason: DeepSeek-V4 / Kimi-K3 remain the MoE architecture co-default
  use_instead: method:deepseek-v4
assumptions:
- Native multimodal MoE pretrain (Mistral-Nemo text tokenizer, Emu3.5 vision,
  WavTokenizer audio). Permissive CC-BY-style corpora. 268 runs.
- No public code as of 2026-10-14.
last_reviewed: '2026-10-14'
papers:
- paper:multimodal-data-mixtures
recipes:
- recipe:multimodal-data-mixtures
claims:
- benchmark: 268 MoE runs, 457M–8.3B, up to 150B tokens; text/vision/audio
  metric: Chinchilla-style exponents; repetition saturation; directional interference
  value: audio model-heavy; text/vision balanced; vision/audio saturate ~2×; vision
    interferes with audio; audio nearly inert as a source
  baseline: unimodal Chinchilla / TGL / NMM / SODA exponents in Table 1 (single-paper)
  date: '2026-10-14'
  verified: true
  evidence_level: peer-reviewed
  source_url: https://arxiv.org/abs/2610.14423
  notes: NeurIPS 2026 spotlight. Does not retarget OLMo-3 or DeepSeek-V4 / Kimi-K3.
tags:
- pretraining
- multimodal
- moe
- data-mix
- active
---

# Multimodal Data-Mixture Scaling Laws

## Method Overview
Extend Chinchilla per modality with directional cross-modal transfer, mixture-dependent MoE capacity sharing, and an exponentially decaying return-on-repetition \(\phi_m(r_m)\). Fit on a controlled MoE ladder, then predict OOD scratch and CPT mixtures.

## When to Use
- Set text/vision/audio mix ratios, unique-data vs repeats, and whether extra compute goes to parameters or tokens for a native multimodal MoE.

## When NOT to Use
Open text mix → `method:olmo-3`. Frontier MoE architecture → `method:deepseek-v4` / `method:kimi-k3`. Unique-token epoch geometry on dense text → `task:data-constrained-pretrain`.

## Relation to Existing SOTA
Active plug-in on `task:open-data-recipe` (`sota_for: []`). Mention on `task:pretrain-moe-frontier`. Does **not** replace OLMo-3 or DeepSeek-V4 / Kimi-K3.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-14.
- Text loss can spike under non-text-heavy CPT of a text-only MoE (paper Figure 1 exception).
- Vision/audio losses include text tokens from those validation sets.
