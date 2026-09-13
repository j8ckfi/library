---
id: method:recurrent-looped-transformer
type: method
title: "Recurrent Looped Transformer (RLT)"
category: "architecture"
status: experimental
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the ~7B dense NTP pretrain optimizer"
    reason: "RLT is an experimental CED recurrence architecture, not an optimizer"
    use_instead: "method:muon2"
  - when: "choosing the frontier MoE pretrain template"
    reason: "DeepSeek-V4 / Kimi-K3 remain the MoE co-default; RLT is not an MoE recipe"
    use_instead: "method:deepseek-v4"
  - when: "input-heavy agentic / KV-compressed CED serving"
    reason: "V4.1-Flash is the serving CED; RLT has no measured serving numbers"
    use_instead: "method:deepseek-v41-flash"
  - when: "latent-space / next-concept LM"
    reason: "NCP-ArchPreview is the latent-space first hop"
    use_instead: "method:ncp-archpreview"
  - when: "GitHub issue to patch / SWE harness"
    reason: "Architecture card, not a harness"
    use_instead: "method:mini-swe-agent"
  - when: "compute-matched looped MoE (middle layers twice)"
    reason: "SMELT loops MoE layers under FLOPs/params/KV matching; RLT is all-token CED recurrence"
    use_instead: "method:smelt"
assumptions:
  - "Causal encoder builds global KV; recurrent decoder carries H_t=(s_t, C_t^D) across every prompt and response token with no boundary reset."
  - "Reference config 48 encoder + 48 decoder layers; compatible attention/FFN weights may be shared across stages."
  - "Report dated 2026-09-12. No measured efficiency, scaling, or RL results. GitHub has PDFs and a site, not a trainer."
last_reviewed: "2026-09-12"
papers:
  - paper:recurrent-looped-transformer
recipes:
  - recipe:recurrent-looped-transformer
claims:
  - benchmark: "RLT technical report (mechanisms)"
    metric: "measured efficiency or scaling"
    value: "none reported"
    baseline: "not a bake-off; report develops mechanisms only"
    date: "2026-09-12"
    verified: false
    evidence_level: "self-reported"
    source_url: "https://github.com/yifanzhang-pro/recurrent-looped-tranformer"
    notes: "Author states reasoning gains, hardware speedups, and RL scaling remain to be established. Do not treat as SOTA metrics."
  - benchmark: "Reference depth"
    metric: "encoder / decoder layers"
    value: "48 / 48"
    baseline: "n/a (configuration, not a result)"
    date: "2026-09-12"
    verified: false
    evidence_level: "self-reported"
    source_url: "https://yifanzhang-pro.github.io/recurrent-looped-tranformer/"
    notes: "Temporal path traverses 48t decoder blocks after t tokens. Per-token logical blocks = 96; decoder cross-attention means FLOPs are not 1:1 with encoder blocks."
tags:
  - architecture
  - recurrent
  - encoder-decoder
  - rlt
  - experimental
---

# Recurrent Looped Transformer (RLT)

## Method Overview
A causal encoder \(E_\theta\) encodes observed tokens in parallel into prefix-restricted global KV memory \(M_{\le t}\). A recurrent decoder \(D_\phi\) of \(L_D\) layers updates complete state

\[
H_t=(s_t,C_t^D),\qquad H_0=(s_\star,\varnothing)
\]

\[
(s_t,C_t^D)=D_\phi\!\left(\operatorname{Merge}(e_t,s_{t-1});M_{\le t},C_{t-1}^D,t\right)
\]

with next-token logits from \(\mathrm{RMSNorm}(s_t)\). Orange path in the report's Figure 1 carries \(H_t\) across the prompt–response boundary without reset; only \(s_t\) enters the merge, while each SWA layer reads its own cached KV. Encoder memory is available before decoder replay and grows as tokens arrive.

"Infinite temporal depth" is path length \(t \times L_D\) at fixed blocks per token. The same transition is used for pretrain, SFT, sample, and exact current-policy RL replay (rebuild history, including SWA KV, under current weights). Full BPTT includes paths through recurrent outputs, decoder KV, and encoder memory; detaching any of these changes the gradient.

YOCO, Feedback Transformer, and Recurrent Transformer appear as prose priors in the report; they are not library nodes.

## When to Use
- You want an experimental recurrent CED LM (encoder memory + all-token decoder recurrence + shared train/sample/replay semantics).

## When NOT to Use
- 7B optimizer → `method:muon2`. Frontier MoE pretrain → `method:deepseek-v4` / `method:kimi-k3`. KV-compressed agentic serving → `method:deepseek-v41-flash`. Latent-space LM → `method:ncp-archpreview`. SWE harness → `method:mini-swe-agent`. Compute-matched MoE looping → `method:smelt`.

## Relation to Existing SOTA
- Experimental first hop on `task:recurrent-encoder-decoder-lm` only. Conceptual sibling of DeepSeek-V4.1-Flash CED (encoder memory, SWA decoder) without Flash's measured KV/agentic numbers and without Flash's MoE serving stack. Does **not** retarget CISPO, Muon2, OPD/VISTA, OPSA, CANOPY, SAO, Miles, NeoHorse-1, mini-SWE-agent, Iris, Poolside, MAGIC, Nemotron IMO Gold, NCP-ArchPreview, or DeepSeek-V4 / Kimi-K3.

## Gotchas & Failure Modes
- No trainer. Recipe is a transition stub pointing at the GitHub (note the "tranformer" spelling).
- Shared transitions remove structural prompt-boundary mismatch; they do not guarantee kernel parity or unbiased off-policy IS.
- Optional stage-wise weight sharing is a configuration, not a measured win.
