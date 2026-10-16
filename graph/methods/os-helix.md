---
id: method:os-helix
type: method
title: 'OS-Helix'
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'desktop/OS GUI ranking on OSWorld 2.0 paper protocol'
  reason: 'OSWorld-Verified is not the locked ranking protocol'
  use_instead: method:claude-computer-use
- when: 'hybrid GUI+code recreation train/eval (RecreationWorld)'
  reason: 'RecreationWorld remains recreation; OS-Helix is a trained native GUI+code CUA'
  use_instead: method:recreationworld
- when: 'open generalist CUA stack / harness-to-model transfer (OpenGCUA)'
  reason: 'OpenGCUA is the open stack; OS-Helix is a trained policy'
  use_instead: method:opengcua
assumptions:
- 'Native GUI+code CUA that must be trained, not prompted. Paper: 27B / 35B-A3B.'
- 'Code: os-copilot/OS-Helix (code_status: released).'
last_reviewed: '2026-10-16'
papers:
- paper:os-helix
recipes:
- recipe:os-helix
claims:
- benchmark: 'OSWorld-Verified; WindowsAgentArena transfer'
  metric: 'success vs matched Qwen3.5 hybrid; 27B-RL success'
  value: '27B / 35B-A3B +35.0% / +33.7% relative vs hybrid baselines; 27B-RL 66.44% (NOT OSWorld 2.0)'
  baseline: 'matched Qwen3.5 hybrid GUI+code baselines (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22234'
  notes: 'Does not demote Claude computer-use. Distinct from OpenGCUA.'
tags:
- computer-use
- hybrid
- active
---

# OS-Helix

## Method Overview
Pair desktop apps with file artifacts, generate environment-grounded tasks with modality-agnostic evaluators, SFT on filtered hybrid traces, then RL with Step-balanced GSPO so long code actions do not dominate token-level IS.

## When to Use
- Training a native GUI+code CUA after seeing prompt-level code tools hurt a GUI agent.

## When NOT to Use
OSWorld 2.0 ranking → `method:claude-computer-use`. Recreation train/eval → `method:recreationworld`. Open CUA stack → `method:opengcua`.

## Relation to Existing SOTA
Active plug-in on `task:hybrid-computer-use-agent-rl` with a mention on `task:computer-use-agent` (`sota_for: []`). Does **not** demote Claude computer-use.

## Gotchas & Failure Modes
- OSWorld-Verified 66.44% is not OSWorld 2.0.
- Prompt-only code tools can regress GUI agents; the paper's point is that routing must be trained.

