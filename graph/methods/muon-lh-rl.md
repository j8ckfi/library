---
id: method:muon-lh-rl
type: method
title: Long-Horizon RL Needs Muon
category: rl-alignment
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: variable environment latency / async stragglers rather than the SWE optimizer recipe
  reason: SAO remains the async-straggler first hop
  use_instead: method:sao
- when: GitHub issue to patch / SWE harness rather than training a policy
  reason: mini-SWE-agent is the loop; this is a single-rollout trainer recipe
  use_instead: method:mini-swe-agent
- when: single-turn dense math/code Pass@1 RLVR
  reason: CISPO remains Pass@1; this recipe is long-horizon SWE
  use_instead: method:cispo
assumptions:
- Async single-rollout SPO/SPO++ host. Paper: MiniCPM5-2B / Qwen3.5-4B, R2E-Gym, Claude Code harness 2.1.118.
- Hidden matrices Muon; embeddings / head / norms / vectors AdamW. TIS C=2.
- No public code as of 2026-10-15.
last_reviewed: '2026-10-15'
papers:
- paper:muon-lh-rl
recipes:
- recipe:muon-lh-rl
claims:
- benchmark: MiniCPM5-2B / Qwen3.5-4B R2E-Gym issue resolution, selected SPO/SPO++ runs
  metric: training success vs Adam SPO baselines under Muon + token-avg loss + truncated IS (C=2) + length/tool-error penalties
  value: full recipe higher training success than SPO baselines in the selected runs from both families
  baseline: Adam SPO / SPO++ without the full Muon recipe (single-paper)
  date: '2026-10-15'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.20256
  notes: Does not retarget SAO or mini-SWE-agent.
tags:
- post-training
- muon
- async-rl
- swe
- active
---

# Long-Horizon RL Needs Muon

## Method Overview
Async single-rollout SWE RL. Combine Muon on hidden matrices with token-averaged policy loss, truncated importance sampling (C=2), and length plus tool-error penalties. One rollout per issue so the learner does not wait for a group.

## When to Use
- Repository-level issue RL with variable-length tool traces and async collection.

## When NOT to Use
Async stragglers as the algorithm → `method:sao`. Issue-to-patch harness → `method:mini-swe-agent`. Dense Pass@1 → `method:cispo`.

## Relation to Existing SOTA
Active plug-in on `task:agentic-async-rl` (`sota_for: []`). Does **not** replace SAO.

## Gotchas & Failure Modes
- **code: none** as of 2026-10-15.
- Selected-run training success, not a locked SWE-Bench ranking.
