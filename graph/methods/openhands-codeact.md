---
id: method:openhands-codeact
type: method
title: "OpenHands (CodeAct)"
category: "agent-harness"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "default first hop / locked SWE-bench mini harness"
    reason: "mini-SWE-agent is the locked ranking scaffold"
    use_instead: "method:mini-swe-agent"
  - when: "dumped long prompt"
    reason: "OpenHands is a repo agent, not RLM"
    use_instead: "method:rlm"
  - when: "training async agent RL"
    reason: "OpenHands is a product scaffold"
    use_instead: "method:sao"
assumptions:
  - "Production OSS. CodeAct action space (2402.01030) plus OpenHands platform (2407.16741)."
last_reviewed: "2026-09-01"
papers:
  - paper:openhands
  - paper:codeact
claims:
  - benchmark: "M3ToolEval, GPT-4-1106"
    metric: "success %"
    value: 74.4
    baseline: "JSON tool-calling 52.4"
    date: "2024-02"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2402.01030"
    notes: "CodeAct paper. Action space, not SWE-bench."
  - benchmark: "SWE-bench Verified (official JSON)"
    metric: "resolved %"
    value: 71.8
    baseline: "mini+Claude 4.5 Opus (high) official JSON 76.8"
    date: "2026-02"
    verified: true
    evidence_level: "unofficial-repro"
    source_url: "https://www.swebench.com/"
    notes: "OpenHands+GPT-5. Production OSS, not the locked mini default."
tags:
  - agents
  - agent-harness
  - openhands
  - codeact
---

# OpenHands (CodeAct)

## Method Overview
OpenHands is the production open-source software-engineering agent. Actions are CodeAct (executable code/bash) rather than JSON schemas. Active alternative when you need a full OSS product. Default first hop remains mini-SWE-agent.

## When to Use
- Deployable OSS coding agent with a code-as-action interface.
- Comparisons that explicitly name OpenHands as the scaffold.

## When NOT to Use
- Locked-harness model ranking → `method:mini-swe-agent`.
- Dumped corpus → `method:rlm`. Train policy → `method:sao`.
