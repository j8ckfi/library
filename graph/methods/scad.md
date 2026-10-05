---
id: method:scad
type: method
title: "SCAD"
category: "rl-alignment"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "programmatic checker exists and sparse outcome RL is the protocol (AppWorld TGC)"
    reason: "CANOPY remains coverage / anti-drift; SCAD is structured planning/execution credit plus local-context distillation"
    use_instead: "method:canopy"
  - when: "multi-turn agent OPD at pivotal early mistakes (prevent reverse-KL + recover forward-KL)"
    reason: "PivotOPD is prevent+recover at pivotal turns; SCAD is subtask-local distill + prefix-tree planning credit"
    use_instead: "method:pivotopd"
  - when: "the problem is context folding of a long tool trajectory, not structured credit"
    reason: "FoldGRPO remains folding; SCAD isolates teacher context per subtask but is not a folding kernel"
    use_instead: "method:foldgrpo"
assumptions:
  - "Agent traces can be split into planning decisions and bounded subtask execution. Paper: Qwen3-4B text; Qwen3-VL multimodal."
  - "No public code as of 2026-10-05 (`code_status: none`)."
last_reviewed: "2026-10-05"
papers:
  - paper:scad
recipes:
  - recipe:scad
claims:
  - benchmark: "Qwen3-4B text long-horizon macro-average"
    metric: "macro-average accuracy"
    value: "46.10"
    baseline: "ATOD 41.62 / HiPER 41.49 / FoldGRPO 39.60"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.03372"
    notes: "+4.48 vs strongest training baseline. Not a CANOPY AppWorld TGC retarget."
  - benchmark: "multimodal long-horizon macro-average lift vs strongest baseline"
    metric: "percentage points"
    value: "+4.19"
    baseline: "strongest training baseline in the multimodal table"
    date: "2026-10-05"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2610.03372"
    notes: "Abstract / intro. ATOD and HiPER are not library methods."
tags:
  - post-training
  - rl-alignment
  - agentic
  - scad
  - active
---

# SCAD

## Method Overview
SCAD organizes a long-horizon trace into planning and bounded subtask execution. Execution is distilled in a local context so teacher KL does not ride a growing student history. Planning credit comes from comparing terminal returns on matched subtask–report prefixes across rollouts. Planning keeps signed terminal credit; execution keeps only the positive part plus the local teacher.

## When to Use
- Long-horizon agents where terminal outcomes hide which plan step mattered and teacher OPD dies as histories grow.

## When NOT to Use
- AppWorld coverage with a checker → `method:canopy`. Pivotal-mistake multi-turn OPD → `method:pivotopd`. Context folding kernel → `method:foldgrpo`.

## Relation to Existing SOTA
- Active plug-in on `task:outcome-only-long-horizon-agent-rl` beside CANOPY / PivotOPD (`sota_for: []`). Does **not** enter `current_sota`. Does **not** replace CANOPY.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-05.
- ATOD / HiPER are paper baselines, not library nodes.
- +4.48 text / +4.19 multimodal is not an AppWorld TGC number.
