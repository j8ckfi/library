---
id: method:opengcua
type: method
title: 'OpenGCUA'
category: agent-harness
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: 'desktop/OS GUI ranking on OSWorld 2.0 paper protocol'
  reason: 'OpenGCUA reports OSWorld-v2 partial/steps, not the locked OSWorld 2.0 protocol'
  use_instead: method:claude-computer-use
- when: 'hybrid GUI+code recreation train/eval (RecreationWorld)'
  reason: 'RecreationWorld remains hybrid recreation train/eval'
  use_instead: method:recreationworld
- when: 'GitHub issue to patch / SWE harness'
  reason: 'mini-SWE-agent remains issue-to-patch'
  use_instead: method:mini-swe-agent
assumptions:
- 'Open generalist CUA stack with code execution and harness-to-model transfer. Not a locked OSWorld 2.0 bake-off.'
- 'Code: Tongyi-MAI/OpenGCUA (code_status: released).'
last_reviewed: '2026-10-16'
papers:
- paper:opengcua
recipes:
- recipe:opengcua
claims:
- benchmark: 'OSWorld-v2 eight-model mean partial and steps vs batched GUI-only'
  metric: 'mean partial; relative steps'
  value: '+19.6 partial; -53.0% steps vs batched GUI-only (includes GPT-6 Astra / Claude Opus 5)'
  baseline: 'batched GUI-only execution (single-paper)'
  date: '2026-10-16'
  verified: false
  evidence_level: preprint
  source_url: 'https://arxiv.org/abs/2610.22200'
  notes: 'Does not demote Claude computer-use on OSWorld 2.0 paper protocol.'
tags:
- computer-use
- harness
- active
---

# OpenGCUA

## Method Overview
Let the model choose visual vs programmatic interfaces. Move selected harness decisions (what to observe, how to organize work) into the model. Code execution is in the action space. Restore a real-device harness and cross-device SDK.

## When to Use
- Building an open generalist CUA stack rather than ranking OSWorld 2.0.

## When NOT to Use
OSWorld 2.0 ranking → `method:claude-computer-use`. Hybrid recreation train/eval → `method:recreationworld`. Issue-to-patch → `method:mini-swe-agent`.

## Relation to Existing SOTA
Active harness note on `task:computer-use-agent` (`sota_for: []`). Does **not** demote Claude computer-use.

## Gotchas & Failure Modes
- OSWorld-v2 partial/steps is not the library OSWorld 2.0 protocol.
- Real-device token cost can dwarf closed systems (19.4x in the reported macOS check).

