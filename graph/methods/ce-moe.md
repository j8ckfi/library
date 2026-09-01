---
id: method:ce-moe
type: method
title: "CE-MoE (Communication-Efficient Mixture-of-Experts Layout)"
category: "architecture"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the frontier MoE architecture template"
    reason: "CE-MoE is a layer-layout niche under expert parallelism, not a replacement of DeepSeek-V4 or Kimi-K3"
    use_instead: "method:deepseek-v4"
  - when: "NVL72 fused dispatch+SwiGLU+combine megakernel"
    reason: "Layout changes do not replace Mixture-of-Kittens"
    use_instead: "method:mixture-of-kittens"
assumptions:
  - "Training with expert parallelism where all-to-all dispatch/combine is a large fraction of step time."
  - "Matched total and activated parameter budget vs a full-MoE baseline on a 2B-31.5B ladder."
  - "No public training code as of 2026-09-01."
last_reviewed: "2026-09-01"
papers:
  - paper:ce-moe
claims:
  - benchmark: "31.5B matched-parameter MoE pretrain"
    metric: "GPU-hours vs full-MoE"
    value: "33.3% fewer GPU-hours"
    baseline: "Full-MoE interleaved experts after every token-mixing layer, matched total and activated params"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.28511"
    notes: "Abstract. Also reports better average downstream score and inference throughput at that scale. Ladder 2B-31.5B matches validation loss of full-MoE."
tags:
  - architecture
  - moe
  - communication
  - ce-moe
  - niche
---

# CE-MoE (Communication-Efficient Mixture-of-Experts Layout)

## Method Overview
CE-MoE is a heterogeneous layer pattern, not a new router. Conventional MoE interleaves a routed expert FFN after every token-mixing layer (attention or Mamba-2), so all-to-all volume scales with depth. CE-MoE concentrates expert capacity in a few routed MoE layers and restores depth with extra token-mixing and dense-FFN layers. Token-mixing depth and channel-mixing depth are decoupled; total and activated parameter counts stay matched to the full-MoE baseline.

## When to Use
- Optional `task:pretrain-moe-frontier` layout when expert-parallel all-to-all dominates step time and you can retile MoE vs dense FFN depth at matched params.

## When NOT to Use
- Do not replace `method:deepseek-v4` / `method:kimi-k3` as the MoE architecture default.
- Do not use as an NVL72 megakernel (`method:mixture-of-kittens`).

## Relation to Existing SOTA
- Layout niche beside DeepSeek-V4 / Kimi-K3. No supersession.

## Gotchas & Failure Modes
- Gains are communication-layout gains under expert parallelism; they do not automatically transfer to tensor-parallel-only dense FFNs.
- No public recipe; reimplement from the paper's layer re-configuration, do not invent a router.
