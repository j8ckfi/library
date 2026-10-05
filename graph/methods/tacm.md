---
id: method:tacm
type: method
title: "Trained Agentic Context Management"
category: "agent-recursion"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "dumped corpus much larger than the window"
    reason: "RLM remains the dumped-prompt first hop (REPL over the corpus); TACM trains a self-call + range-read harness at 8K"
    use_instead: "method:rlm"
  - when: "GitHub issue to patch without a dumped corpus"
    reason: "mini-SWE-agent remains the SWE loop; TACM is long-document context management"
    use_instead: "method:mini-swe-agent"
  - when: "post-train gated sparse attention under a fixed budget, not a harness"
    reason: "SAS is sparse attention; TACM is a trained 8K self-call harness"
    use_instead: "method:sas"
assumptions:
  - "Finetune Qwen3.6-35B-A3B (or similar) on synthetic self-call / range-read traces. Serve at 8K per-agent context. Paper compares to GPT-5.4 1M on OOLONG-synth and RULER."
  - "Official code brycesandlund/infinite-context released as of 2026-10-05."
last_reviewed: "2026-10-05"
papers:
  - paper:tacm
recipes:
  - recipe:tacm
claims:
  - benchmark: "OOLONG-synth mean of 3 families, 40K / 80K / 160K / 320K"
    metric: "accuracy"
    value: "0.535 / 0.561 / 0.464 / 0.470"
    baseline: "GPT-5.4 1M full document 0.600 / 0.539 / 0.556 / 0.479"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02404"
    notes: "Finetuned Qwen3.6-35B-A3B at 8K per-agent context. Not an RLM REPL retarget."
  - benchmark: "RULER, finetuned 8K harness"
    metric: "RULER score"
    value: "0.949 / 0.949 / 0.929 / 0.885 / 0.868 / 0.858"
    baseline: "GPT-5.4 full document 0.954 / 0.938 / 0.954 / 0.954 / 0.929 / 0.954"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.02404"
    notes: "Stays ≥0.85 through 320K; 0.858 at 320K."
tags:
  - agents
  - long-context
  - tacm
  - active
---

# Trained Agentic Context Management

## Method Overview
TACM does not extend native context and does not hand-author a REPL harness. It finetunes the model on two tools: call itself with any prompt, and read a token range from the input. The 8K-window student is trained to recurse and page. RLM remains the dumped-corpus REPL default; this is a trained self-call policy.

## When to Use
- Long documents where you can finetune a small-window model to self-call and range-read, instead of serving a 1M native window.

## When NOT to Use
- Dumped corpus ≫ window, no finetune of a self-call harness → `method:rlm`. SWE issue-to-patch → `method:mini-swe-agent`. Sparse attention under a token budget → `method:sas`.

## Relation to Existing SOTA
- Active plug-in on `task:long-context-prompt-offload` beside RLM (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace RLM.

## Gotchas & Failure Modes
- OOLONG 40K 0.535 still trails GPT-5.4 0.600; 80K is the first length where the 8K harness leads (0.561 vs 0.539).
- Base Qwen full-document OOLONG dashes after 40K in the paper table. Do not treat TACM as a drop-in RLM code REPL.
