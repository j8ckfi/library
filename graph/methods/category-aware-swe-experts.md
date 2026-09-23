---
id: method:category-aware-swe-experts
type: method
title: "Category-Aware SWE Experts"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "data/env construction for coding-agent RL from source code only"
    reason: "CodeMidas remains that env factory; this method trains category experts on already-executable SWE tasks"
    use_instead: "method:codemidas"
  - when: "variable tool latency / async stragglers"
    reason: "SAO remains the async algorithm"
    use_instead: "method:sao"
  - when: "GitHub issue to patch / SWE harness loop"
    reason: "mini-SWE-agent remains the start/eval loop"
    use_instead: "method:mini-swe-agent"
  - when: "production post-train stack (SGLang / Megatron / LoRA RL / OPD)"
    reason: "Miles remains the engine"
    use_instead: "method:miles"
assumptions:
  - "Executable SWE instances with a verifier. Categories come from SWE Labeler (repository-domain L1 → Pro-A/B/C on Pro-618)."
  - "Same-origin experts alternate Agentic-miniRL with Refresh–Repair–Expand. Integration is label-routed MOPD with ReLU-gated reward extrapolation. No external teacher trajectories."
  - "Code: alibaba/AgenticBigBang. Alibaba Logics-SWE-Qwen3.6-27B line."
last_reviewed: "2026-09-23"
papers:
  - paper:category-aware-swe-experts
recipes:
  - recipe:category-aware-swe-experts
claims:
  - benchmark: "Pro-618 mean resolution, Logics-SWE-Qwen3.6-27B line"
    metric: "resolved %"
    value: "58.04%"
    baseline: "base +5.39 pp"
    date: "2026-09-23"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.23377"
    notes: "Audit-filtered 618 of 731 SWE-bench Pro. Not a mini-SWE-agent ranking retarget. Not CodeMidas env construction."
  - benchmark: "SWE-bench Multilingual"
    metric: "resolved %"
    value: "59.00%"
    baseline: "base +2.78 pp"
    date: "2026-09-23"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.23377"
    notes: "Single student after label-routed MOPD. Expert training uses no external solution trajectories."
tags:
  - post-training
  - agentic
  - swe
  - experts
  - mopd
  - active
---

# Category-Aware SWE Experts

## Method Overview
Pooled agentic RL on heterogeneous SWE categories produces a **category see-saw**: one category's gain is another's regression, while aggregate resolution stays flat. This method splits the training distribution by observable categories, develops specialists, then integrates them.

1. **SWE Labeler** maps issue/repo evidence onto semantic and scale axes; deterministic rules yield training categories (Pro-A/B/C on Pro-618).
2. **RRE experts**: each same-origin expert alternates Agentic-miniRL with Refresh (re-score instance mastery), Repair SFT on its own verified successes, and Expand (reselect the training frontier).
3. **Label-routed MOPD**: teachers score the student's trajectories; ReLU-gated reward extrapolation keeps only the improving direction versus a reference. No external teacher trajectories.

mini-SWE-agent remains the harness. CodeMidas remains source-only env construction. SAO remains async. Miles remains the engine.

## When to Use
- Repository-level SWE RL where pooled or balanced joint RL hides opposing category movements and you can label tasks into a small set of operational categories.

## When NOT to Use
- Source-only env factory → `method:codemidas`. Async algorithm → `method:sao`. Issue → patch loop → `method:mini-swe-agent`. Production stack → `method:miles`.

## Relation to Existing SOTA
- Active first hop on `task:swe-agent-category-expert-rl` only (method status active; listed in that task's `current_sota`; `sota_for` stays empty). Does **not** retarget `method:codemidas`, `method:sao`, `method:mini-swe-agent`, `method:miles`, `method:opd`, or `method:open-mopd`.

## Gotchas & Failure Modes
- Aggregate resolution is not the objective by itself. Track \(G_{\mathrm{sim}}=\min_c\Delta_c\) and the see-saw gap.
- Repair SFT uses the expert's own verified rollouts. Importing an external teacher's trajectories is a different method.
- Pro-618 is an audit-filtered subset of SWE-bench Pro. Do not mix it with official Pro public locked-mini ranking numbers.
