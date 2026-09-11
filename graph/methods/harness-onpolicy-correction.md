---
id: method:harness-onpolicy-correction
type: method
title: "Harness On-Policy Expert Correction"
category: "agent-harness"
status: niche
sota_for: []
supersedes: []
do_not_use_for:
  - when: "choosing the SWE issue-to-patch harness"
    reason: "This is a co-evolution gotcha + turn-rewrite recipe, not the bash ReAct loop"
    use_instead: "method:mini-swe-agent"
  - when: "production harness kernel (rewind, sandbox, remote, TUI)"
    reason: "omp2 remains that architecture"
    use_instead: "method:omp2-harness"
  - when: "routing-harness RSI post-train"
    reason: "NeoHorse-1 remains that first hop"
    use_instead: "method:neohorse-1"
  - when: "frontier RL post-train engine"
    reason: "Miles remains the stack"
    use_instead: "method:miles"
  - when: "expert full-trajectory SFT after model-specific harness evolution"
    reason: "That imitation is the failure mode (−4 to −30 pts on all seven tasks)"
    use_instead: "method:harness-onpolicy-correction"
assumptions:
  - "Enterprise agent tasks with an evolvable harness (system prompt, tools, hooks, context scaffolding) and a stronger expert model. Paper: Qwen3-Coder-30B-A3B and Gemma-4-26B-A4B, LoRA-SFT."
  - "No official code as of 2026-09-11. Pipeline is automated by a meta-level MLE agent in the paper."
last_reviewed: "2026-09-11"
papers:
  - paper:harness-onpolicy-correction
recipes:
  - recipe:harness-onpolicy-correction
claims:
  - benchmark: "Seven enterprise agent tasks, LoRA-SFT on full expert trajectories after harness evolution"
    metric: "task score change vs evolved-harness baseline"
    value: "−4 to −30 points on all seven tasks"
    baseline: "same imitation under the unevolved harness (helps); evolved harness without weight updates"
    date: "2026-09-11"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.09134"
    notes: "Reproduced on Qwen3-Coder and Gemma 4. On-policy expert rewrite of the failing student turn is the proposed fix."
tags:
  - agents
  - agent-harness
  - sft
  - on-policy
  - niche
---

# Harness On-Policy Expert Correction

## Method Overview
Harness evolution around a weaker model, then full expert-trajectory LoRA-SFT under that harness, **regresses**. The student copies the expert plan without the competence to execute it and no longer matches the harness that was evolved for its native style. The same SFT helps under the baseline harness.

Fix: run the student, localize the first failing turn, ask the expert to rewrite **only that turn**, train on the corrected on-policy prefix. Preserves planning style so harness evolution and weight updates compose.

Niche gotcha + recipe. Does not replace mini-SWE-agent, Miles, or NeoHorse-1.

## When to Use
- You evolved a model-specific harness and now want a light weight update. Do not dump expert traces.

## When NOT to Use
- SWE harness pick → `method:mini-swe-agent`. Production kernel → `method:omp2-harness`. RSI routing post-train → `method:neohorse-1`. Stack → `method:miles`.

## Relation to Existing SOTA
- Niche on `task:software-engineering-agent-harness`, `task:agent-harness-runtime`, and `task:agentic-rsi-routing-posttrain`. Does **not** enter `current_sota`.

## Gotchas & Failure Modes
- No official repo. Implement the turn-local rewrite; do not invent a new SWE loop.
- Imitation under an **unevolved** harness is a different setting — the paper's warning is specifically post-evolution.
