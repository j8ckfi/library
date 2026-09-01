---
id: method:nora
type: method
title: "NoRA (Normalized Low-Rank Adaptation)"
category: "peft"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "24GB quality LoRA is the library task and no RLVR-stability requirement is stated"
    reason: "The 24GB quality default remains vanilla LoRA + rsLoRA + LR sweep; NoRA is not a completed supersession of that protocol"
    use_instead: "method:lr-matters-lora"
  - when: "memory must fit a 4-bit stack with a mixed-precision adapter"
    reason: "NoRA is a full-precision adapter reparameterization, not a 4-bit recipe"
    use_instead: "method:aqlora-q"
  - when: "the deployed checkpoint must stay fully NF4/INT4/MXFP4 with no high-precision adapter"
    reason: "That is code-space fine-tuning, not LoRA normalization"
    use_instead: "method:gradcodes"
assumptions:
  - "Standard LoRA parameterization $\\Delta W=\\alpha B A$ with $B$ zero-init; NoRA normalizes columns of $A\\in\\mathbb{R}^{r\\times k}$ along $r$."
  - "Recommend $\\alpha=r$ (unit scaling) because column norms are 1."
  - "Paper evidence is Llama-3.2-3B SFT and DeepSeek-R1-Distill-Qwen-1.5B RLVR, not the 24GB LR-sweep protocol of 2602.04998."
last_reviewed: "2026-09-01"
papers:
  - paper:nora
recipes:
  - recipe:nora
claims:
  - benchmark: "Llama-3.2-3B SFT (GSM8K / Math / HumanEval / MBPP average)"
    metric: "average accuracy"
    value: 43.37
    baseline: "LoRA 37.93 / RSLoRA 41.28 / DoRA 38.30 / PiSSA 40.26 / MiSS 42.70"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.31036"
    notes: "Table 5. No extra params vs LoRA (48.6M). Forgetting Avg Delta +0.02 vs LoRA -0.56. Not the library LR-sweep protocol."
  - benchmark: "DeepSeek-R1-Distill-Qwen-1.5B RLVR overall average"
    metric: "mean of AIME24/25, AMC, HMMT, MATH500, Minerva"
    value: 44.4
    baseline: "LoRA 42.8 / base 41.0 / PiSSA 0.2 / MiLoRA 18.0"
    date: "2026-09-01"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2608.31036"
    notes: "Table 6. PiSSA/MiLoRA collapse under RLVR; NoRA stays stable. Recommended upgrade for RLVR-stable adapters."
tags:
  - peft
  - lora
  - nora
  - rlvr
---

# NoRA (Normalized Low-Rank Adaptation)

## Method Overview
NoRA normalizes each column of the LoRA down-projection along the rank dimension:

\[
\mathrm{Norm}(A)_{:,j}=\frac{a_j}{\max(\|a_j\|_2,\epsilon)},\qquad \Delta y=\alpha B\,\mathrm{Norm}(A)\,x
\]

This is linear in $x$ and mergeable. Two modes:

1. **NoRA**: renormalize $A$ throughout training (PEFT `use_nora=True`).
2. **NoRA-init**: normalize once after init (`use_nora="init"`). BIMI (`init_lora_weights="bimi"`) tiles $I_r$ blocks so columns are already unit-norm and orthogonal.

The intent is to put unit-norm directions in $A$ and let $B$ carry magnitude, aligning early LoRA gradient norms with full finetuning.

## When to Use
- Recommended LoRA upgrade when adapters must stay stable under RLVR, or when PiSSA/MiLoRA have already collapsed.
- Cheap SFT upgrade over vanilla LoRA with no extra parameters: `use_nora=True` and `lora_alpha=r`.
- NoRA-init when you cannot change the forward (normalize once, then standard LoRA).

## When NOT to Use
- Do not treat NoRA as a completed replacement of `method:lr-matters-lora` (vanilla LoRA + rsLoRA + LR sweep) on `task:lora-quality-tuning`. The paper beats RSLoRA on one Llama-3.2-3B SFT suite without that LR-sweep protocol.
- 4-bit mixed-precision PEFT -> `method:aqlora-q`. Fully quantized code-space FT -> `method:gradcodes`.

## Relation to Existing SOTA
- Status `active` on the PEFT shelf next to AQLoRA-Q / DoRA / vanilla+rsLoRA. **Not** a first-hop and **not** a supersession of `method:lr-matters-lora`.
- Stronger RLVR-stable alternative than spectral LoRA inits.

## Gotchas & Failure Modes
- Row-normalization (`Norm_k`) does not help; only rank-dimension column norms (`Norm_r`).
- Set $\alpha=r$ so scaling stays 1 after unit-column $A$.
- PEFT fork replaces the environment `peft` package until an upstream merge lands.
