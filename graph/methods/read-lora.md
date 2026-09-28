---
id: method:read-lora
type: method
title: "READ (Read-only Expansion of Adapter Deltas)"
category: "peft"
status: active
sota_for:
  - task:lora-skill-composition
supersedes: []
do_not_use_for:
  - when: "single-adapter quality LoRA on 24GB (rsLoRA + LR sweep)"
    reason: "lr-matters-lora remains the quality default; READ composes already-trained adapters"
    use_instead: "method:lr-matters-lora"
  - when: "memory must fit a 4-bit PEFT stack"
    reason: "AQLoRA-Q remains 4-bit PEFT; READ is a composition operator on full-precision LoRA factors"
    use_instead: "method:aqlora-q"
  - when: "instruct FT under a behavioral-drift budget / layer-selective freeze"
    reason: "DCO is drift-budget instruct FT, not multi-skill LoRA composition"
    use_instead: "method:dco"
  - when: "RLVR-stable rank-normalized LoRA A"
    reason: "NoRA normalizes a single adapter; READ does not replace that quality/stability recipe"
    use_instead: "method:nora"
assumptions:
  - "Independently trained generative-classification LoRA skills (paper: r=8, α=16, q/v projections) already exist. Each append trains only the new row/diagonal of G on the stage task union."
  - "Paper: Llama-3.2-3B-Instruct and Qwen3-4B; GLUE-6, SuperGLUE-4, Domain-3, BBH-6; 32 lineages. Fold after each append."
  - "No public GitHub as of 2026-09-28."
last_reviewed: "2026-09-28"
papers:
  - paper:read-lora
recipes:
  - recipe:read-lora
claims:
  - benchmark: "Llama-3.2-3B sequential skill add, SuperGLUE-4 / Domain-3 terminal macro"
    metric: "suite-mean official primary metrics"
    value: "0.783 / 0.887"
    baseline: "strongest published same-adapter foldable alternative 0.605 / 0.846"
    date: "2026-09-28"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.31600"
    notes: "Table 1. Does not retarget lr-matters-lora or AQLoRA-Q."
  - benchmark: "Qwen3-4B sequential skill add, GLUE-6 terminal macro"
    metric: "suite-mean official primary metrics"
    value: "0.838"
    baseline: "strongest published same-adapter foldable alternative 0.775"
    date: "2026-09-28"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.31600"
    notes: "Table 1 GLUE (the 0.838 vs 0.775 pair). Qwen SuperGLUE 0.797 vs 0.709."
  - benchmark: "Shared 32-lineage terminal-bank comparison"
    metric: "mean lift vs per-lineage strongest of 14 foldable alternatives"
    value: "+0.073"
    baseline: "per-lineage max of Soup/Fisher/Task Arithmetic/RegMean/TIES/DARE/Breadcrumbs/LoRA-LEGO/KnOTS-TIES/LoRAHub/OSRM/LoRA-Soups/Compress-then-Merge/NSC"
    date: "2026-09-28"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.31600"
    notes: "95% CI +0.047–+0.101; 24/32 wins; all 8 losses on BBH."
tags:
  - peft
  - lora
  - composition
  - read-lora
  - active
---

# READ (Read-only Expansion of Adapter Deltas)

## Method Overview
A LoRA update \(\Delta W=BA\) admits any invertible gauge \((BR)(R^{-1}A)\). That gauge is invisible while an adapter serves alone and becomes the coordinates a learned coupling sees. READ canonicalizes each skill with thin QR of \(B\) and \(A^\top\), SVD of \(R_B R_A^\top\), and balanced \(\Sigma^{1/2}\) factors so \(B^c A^c=BA\) and both sides share the same metric.

Stacked factors meet through a coupling \(G\):

\[
\Delta W=B_{\mathrm{stack}} G A_{\mathrm{stack}}.
\]

At append \(k{+}1\), copy the old \(G^{(k)}\) frozen into the upper-left block, hard-zero the write column \(G_{\le k,k+1}\), and train only the new skill's row and diagonal on the stage task union. The new skill may read old input subspaces; it must not write old output subspaces. Fold \(B_{\mathrm{stack}} G A_{\mathrm{stack}}\) into \(W_0\). No router, no extra inference path.

Single-adapter quality remains vanilla LoRA + rsLoRA + LR sweep. 4-bit PEFT remains AQLoRA-Q.

## When to Use
- Stacking independently trained LoRA skills into one folded model without an inference router.

## When NOT to Use
- Single-adapter quality → `method:lr-matters-lora`. 4-bit PEFT → `method:aqlora-q`. Drift-budget instruct freeze → `method:dco`. RLVR-stable A → `method:nora`.

## Relation to Existing SOTA
- First hop on new `task:lora-skill-composition` only. Status `active`. Does **not** replace `method:lr-matters-lora` or `method:aqlora-q`. Does **not** retarget `task:parameter-efficient-fine-tuning` or `task:lora-quality-tuning`.

## Gotchas & Failure Modes
- No public code as of 2026-09-28. Reimplement canonicalize + read-only \(G\) + fold; do not invent a LoRA quality default.
- BBH is the failure suite (8/32 lineage losses). Do not advertise a universal win.
- Append still sees old-task data in the stage union. READ is not a no-replay continual-learning claim.
- Routing (LoRAHub, LoRA-Mixer) remains the right call when each solo adapter must stay intact at serve time.
- Canonicalization is not optional: equivalent raw factorizations shifted scores 2.8 points in the paper; canonical form cut that to 0.7.
