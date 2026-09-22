---
id: method:code2skill
type: method
title: "Code2Skill"
category: "agent-memory"
status: active
sota_for: []
supersedes: []
do_not_use_for:
  - when: "incremental playbook with execution feedback across tasks"
    reason: "ACE remains the default agent-memory SOTA; Code2Skill is offline repository-grounded skill synthesis"
    use_instead: "method:ace"
  - when: "SWE patch loop with no persistent playbook or skill bank"
    reason: "bash ReAct does not need a million-skill bank"
    use_instead: "method:mini-swe-agent"
  - when: "long-lived persona OS-style paging"
    reason: "MemGPT is the persona/OS memory alternative"
    use_instead: "method:memgpt"
  - when: "dumped corpus much larger than the window"
    reason: "RLM offloads the prompt; Code2Skill retrieves compact skill records"
    use_instead: "method:rlm"
  - when: "System-One control plane for conversational memory ops"
    reason: "Jev-Mem is typed memory control; Code2Skill is repository-grounded skill synthesis"
    use_instead: "method:jev-mem"
assumptions:
  - "Source units from maintained GitHub repos (>500 stars in the paper pool). Records are atomic, composite, or pattern. Acceptance is LLM reconstruction-plus-judge, not a proof of program equivalence."
  - "Default eval retrieves from a 10% sample of CodeSkillBank into a draft–review–revise loop. Compact summaries retain most utility at much lower context."
  - "GitHub https://github.com/ant-intl/Code2Skill is a pre-release publication implementation as of 2026-09-21. Dataset: ant-intl/DeveloperSkills-Code2Skill."
last_reviewed: "2026-09-22"
papers:
  - paper:code2skill
recipes:
  - recipe:code2skill
claims:
  - benchmark: "72 protocol-matched evals, 9 model settings, 8 benches"
    metric: "macro-average vs matched no-skill loop"
    value: "47.90 vs 42.90 (+11.7% relative); 57/72 wins"
    baseline: "same agent loop with z_t = empty"
    date: "2026-09-21"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.05571"
    notes: "SWE / BigCode / AIME 2026 / HMMT 2025 / GPQA / TerminalBench / LongCLI / AgentBench-OS. All nine SWE-bench Verified pairs improve. ACE stays memory SOTA."
  - benchmark: "Seven shared benches vs trajectory-derived banks, DS4-Flash reasoning"
    metric: "unweighted average"
    value: 49.5
    baseline: "Trace2Skill 31.0 / ExpeL 27.9 / SkillRL-Bank 32.8"
    date: "2026-09-21"
    verified: true
    evidence_level: "preprint"
    source_url: "https://arxiv.org/abs/2609.05571"
    notes: "First on all seven. Beats the per-bench best trajectory bank by 6.6–13.3."
tags:
  - agents
  - agent-memory
  - skills
  - code2skill
  - active
---

# Code2Skill

## Method Overview
Code2Skill lifts code units into grounded skill records before the agent has interaction experience. Pipeline:

1. Rank functions, methods, CLI entry points, and file-level components for reusable procedural content.
2. Extract a typed record: atomic operation, composite workflow, or recurring pattern, with when-to-use, steps, invariants, failures, anti-goals, and source evidence.
3. Reconstruct the implementation from the record without the source body; a source-aware judge accepts or sends the case to adjudication.
4. Feature-tag and purpose-index accepted records into CodeSkillBank (~1.0M from 19,769 repos).

Retrieved records enter an agent loop at planning, generation, or post-generation review. ACE remains the default playbook/memory method. This is the repository-grounded skill bank.

## When to Use
- You want procedural skills grounded in OSS implementations *before* the agent has enough trajectories to distill a playbook.

## When NOT to Use
- Incremental execution-feedback playbook → `method:ace`. SWE bash loop with no bank → `method:mini-swe-agent`. Persona paging → `method:memgpt`. Dumped prompt → `method:rlm`. System-One conversational memory control → `method:jev-mem`.

## Relation to Existing SOTA
- Active on `task:agent-memory` alongside ACE. Does **not** enter `current_sota`. Does **not** replace `method:ace`. System-One memory control is `method:jev-mem`.

## Gotchas & Failure Modes
- The judge is an LLM consistency check, not program equivalence. Treat rejected records as unsupported, not as a verified negative.
- Generation-time prompting is less consistent than planning or post-generation critique. Compact summaries (~0.7k chars at k=3) keep most utility.
- CodeSkillBank evals used a 10% retrieval sample. Do not assume you must dump a million records into context.
- GitHub README still marks the repo as pre-release; pin a commit before depending on it.
