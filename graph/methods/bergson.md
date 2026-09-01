---
id: method:bergson
type: method
title: "Bergson (Open Source Data Attribution Library)"
category: "data-attribution"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "replacing Dolma / OLMo-3 mix ratios or searching source weights"
    reason: "Bergson scores items for a query; it does not search mix weights. OLMo-3 remains the open-data SOTA; AutoMixer remains the factory mix-search component."
    use_instead: "method:olmo-3"
  - when: "picking a pretrain optimizer or train kernel"
    reason: "Diagnostic library, not a training optimizer"
    use_instead: "method:muon2"
  - when: "running MAGIC on a third-party final checkpoint with no training trajectory"
    reason: "MAGIC needs your trainer's trajectory; final-ckpt-only work uses the influence-function path"
    use_instead: "method:trackstar"
assumptions:
  - "pip install bergson (v0.26.2); HuggingFace Transformers/Datasets; docs at https://bergson.readthedocs.io."
  - "Fused MoE experts (gpt-oss, Mixtral, Qwen-MoE, OLMoE) are unsupported."
  - "Verified single-node scale is Appendix C (one 8×A100): grad-dot 72B, EK-FAC 7B — not a 405B off-the-shelf run."
last_reviewed: "2026-09-01"
papers:
  - paper:bergson
recipes:
  - recipe:bergson-magic-gpt2-wikitext
  - recipe:bergson-trackstar
claims:
  - benchmark: "Open-source TDA coverage"
    metric: "first public implementations"
    value: "MAGIC, SOURCE, TrackStar"
    baseline: "Kronfluence (EK-FAC) / dattri (LiSSA, TRAK, TracIn; no MAGIC/SOURCE/TrackStar)"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.11660"
    notes: "Library umbrella. Algorithm SOTA for LDS remains method:magic. bergson sota_for is empty."
  - benchmark: "Largest completed off-the-shelf attribution, one 8×A100 node (Appendix C)"
    metric: "model size"
    value: "grad-dot 72B / EK-FAC 7B"
    baseline: "Kronfluence EK-FAC 14B / grad-dot 32B on the same protocol"
    date: "2026-06"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2606.11660"
    notes: "Intro 'on the order of 405B' is a multi-node design claim, not a completed off-the-shelf run."
tags:
  - interpretability
  - data-attribution
  - bergson
  - factory-component
  - eleutherai
---

# Bergson (Open Source Data Attribution Library)

## Method Overview
Bergson is the EleutherAI MIT library for data attribution (`pip install bergson`, v0.26.2). Status `active`. `sota_for: []`. Same pattern as AutoMixer: optional factory *component* for query-conditioned item scoring, never SOTA for mix, recipe, kernel, or factory-process tasks.

It provides CLI (`bergson build|query|score|magic|trackstar|ekfac|approxunrolling|validate|metasmoothness`), on-disk gradient stores, YAML pipelines, FAISS ANN, LoRA, per-token and per-sequence scores, and a twice-differentiable trainer. Algorithms live on their own method nodes: MAGIC (`method:magic`), TrackStar (`method:trackstar`), EK-FAC (`method:ek-fac`), SOURCE (`method:source-unrolling`).

Not implemented: LoGra, LiSSA, full TRAK estimator, TracIn (TRAK projection primitive only). Fused MoE expert/router layouts are unsupported.

## When to Use
- You need OSS MAGIC / SOURCE / TrackStar / EK-FAC on a HuggingFace model you can load.
- Small lab: TrackStar / `bergson score` for LESS-style query-conditioned ranking (`recipe:bergson-trackstar`).
- You control training and want MAGIC LDS (`recipe:bergson-magic-gpt2-wikitext`). Always `bergson metasmoothness` before trusting MAGIC.

## When NOT to Use
- Replacing Dolma / OLMo-3 or searching mix weights -> `method:olmo-3` / `method:automixer`.
- Picking a train kernel -> `method:muon2` / `method:cispo`.
- MAGIC on a downloaded final checkpoint with no trajectory -> `method:trackstar`.
- Claiming 405B EK-FAC as a verified run. Appendix C verified: grad-dot 72B, EK-FAC 7B on one 8×A100.

## Relation to Existing SOTA
Does **not** supersede `method:magic` (library vs algorithm). Does **not** retarget CISPO, Muon2, OPD, OLMo-3, Poolside factory, BMSSP, OPSA, or SAE methods. Not on `task:open-data-recipe` or `task:industrial-model-building` `current_sota`.

## Gotchas & Failure Modes
- Untuned Hessian damping / low metasmoothness can drive LDS ~0.
- MAGIC ~3–5 train-run compute; EK-FAC / TrackStar ~1–2. HF Trainer callback ~17% overhead.
- Fused MoE (gpt-oss, Mixtral, Qwen-MoE, OLMoE) unsupported.
