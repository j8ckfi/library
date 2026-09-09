---
id: method:ace-moe-peft
type: method
title: "ACE (Adapter Consolidation across Experts)"
category: "peft"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "24GB quality LoRA on a dense model"
    reason: "ACE consolidates MoE expert adapters; dense quality default is vanilla LoRA + rsLoRA + LR sweep"
    use_instead: "method:lr-matters-lora"
  - when: "agent playbook / context engineering"
    reason: "method:ace is Agentic Context Engineering, a different ACE"
    use_instead: "method:ace"
  - when: "memory must fit a 4-bit stack"
    reason: "ACE is a full-precision MoE PEFT layout, not AQLoRA-Q"
    use_instead: "method:aqlora-q"
assumptions:
  - "MoE backbone with expert-wise LoRA as the naive PEFT. Paper: four MoE backbones, 12 datasets, EMNLP 2026."
  - "Slug is ace-moe-peft because method:ace is already Agentic Context Engineering."
last_reviewed: "2026-09-09"
papers:
  - paper:ace-moe-peft
recipes:
  - recipe:ace-moe-peft
claims:
  - benchmark: "12 datasets × four MoE backbones, parameter-matched PEFT"
    metric: "mean accuracy rank / wall-clock vs expert-wise LoRA"
    value: "best mean on 3/4 backbones with complete baselines; 1.31×–1.48× faster"
    baseline: "expert-wise LoRA (same PEFT budget)"
    date: "2026-09-09"
    verified: true
    evidence_level: "peer-reviewed"
    source_url: "https://arxiv.org/abs/2609.06072"
    notes: "EMNLP 2026. Peak memory not increased. Code: UbiquitousAILab/ACE."
tags:
  - peft
  - moe
  - lora
  - ace-moe-peft
  - active
---

# ACE (Adapter Consolidation across Experts)

## Method Overview
ACE groups redundant MoE experts and shares a higher-rank LoRA per group under the same adapter budget, then fuses expert-wise GEMMs into group GEMMs. It is **not** `method:ace` (Agentic Context Engineering).

Does not replace `method:lr-matters-lora` (dense 24GB quality) or `method:aqlora-q` (4-bit).

## When to Use
- PEFT on an MoE where expert-wise LoRA is slow and fragmented.

## When NOT to Use
- Dense LoRA quality → `method:lr-matters-lora`. Agent memory → `method:ace`. 4-bit → `method:aqlora-q`.

## Relation to Existing SOTA
- Active PEFT plug-in on `task:parameter-efficient-fine-tuning`. Does **not** supersede `method:lr-matters-lora` or `method:ace`.

## Gotchas & Failure Modes
- Name collision with ACE playbooks. Always use `method:ace-moe-peft`.
