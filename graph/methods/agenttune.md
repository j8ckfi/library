---
id: method:agenttune
type: method
title: AgentTune
category: training-systems
status: active
sota_for: []
supersedes: []
do_not_use_for:
- when: variable environment latency / async stragglers
  reason: SAO remains the async algorithm; AgentTune is a lifecycle library
  use_instead: method:sao
- when: production post-train stack (SGLang / Megatron / LoRA RL / OPD)
  reason: Miles remains the engine; AgentTune is a Python lifecycle substrate
  use_instead: method:miles
- when: build a SWE / issue-to-patch harness
  reason: mini-SWE-agent remains that loop
  use_instead: method:mini-swe-agent
assumptions:
- Tool-using LLM agents that need one EventLog for train/eval/distill/audit. Source-available Python library.
- 'Code: Lexsi-Labs/AgentTune (code_status: released).'
last_reviewed: '2026-10-12'
papers:
- paper:agenttune
recipes:
- recipe:agenttune
claims:
- benchmark: Tool-using agent lifecycle (legal contract search and domain tasks in the paper)
  metric: shared EventLog substrate for train / eval / distill / audit
  value: two-tier EventLog with consistent projections; tool-calling RL, agentic distillation, RAG, evaluation,
    designed self-healing path
  baseline: isolated stage-specific agent toolchains
  date: '2026-10-12'
  verified: true
  evidence_level: preprint
  source_url: https://arxiv.org/abs/2610.13335
  notes: No Pass@1 bake-off vs SAO/CISPO. Does not retarget SAO or Miles.
tags:
- agents
- tool-use
- training-systems
- agenttune
- active
---

# AgentTune

## Method Overview
Log every agent turn once. Project that log into the trainer, the evaluator, and the distiller without copying pipelines. Compose tool-calling RL and agentic distillation on the same runtime.

## When to Use
- You are building a tool-using agent training loop and the stage-specific formats are the tax.

## When NOT to Use
Async straggler algorithm → `method:sao`. Production engine → `method:miles`. Issue-to-patch → `method:mini-swe-agent`.

## Relation to Existing SOTA
Active plug-in on `task:agentic-async-rl` with a mention on `task:frontier-rl-posttrain-stack` (`sota_for: []`). Does **not** replace SAO or Miles.

## Gotchas & Failure Modes
- **code: released** Lexsi-Labs/AgentTune as of 2026-10-12.
- Source-available, not a bake-off vs SAO.
- Self-healing is a designed path in the paper, not a measured AppWorld TGC.
