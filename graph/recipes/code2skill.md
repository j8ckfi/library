---
id: recipe:code2skill
type: recipe
title: "Code2Skill Grounded Skill Synthesis"
method: method:code2skill
task: task:agent-memory
target_hardware: "CPU plus an OpenAI-compatible chat endpoint"
framework: "Python stdlib / OpenAI-compatible /chat/completions"
repo_url: "https://github.com/ant-intl/Code2Skill"
code_status: partial
pip_dependencies: []
tags:
  - recipe
  - code2skill
  - agent-memory
  - skills
---

# Code2Skill Grounded Skill Synthesis

## Hardware & Environment Setup
- Official: `https://github.com/ant-intl/Code2Skill` (pre-release publication implementation as of 2026-09-21). `code_status: partial`.
- Dataset: `https://huggingface.co/datasets/ant-intl/DeveloperSkills-Code2Skill`
- Site: `https://ant-international-research.github.io/developer-skill-hubs/`
- Runtime has no third-party Python dependency. It calls an OpenAI-compatible endpoint through the standard library.
- ACE remains the playbook/memory default.

## Quickstart Implementation

```bash
python3 -m venv .venv
. .venv/bin/activate
python -m pip install -e .
cp .env.example .env
set -a
. ./.env
set +a
code2skill run /path/to/repository \
  --base-url "$CODE2SKILL_MODEL_BASE_URL" \
  --model your-model-name \
  --output-dir runs
```

## Critical Hyperparameters & Tuning Advice
- Records are `atomic`, `composite`, or `pattern`. The judge is an LLM consistency check, not program equivalence.
- Prefer planning-time or post-generation review over stuffing skills into the first-pass prompt.
- Compact summaries at \(k=3\) cut rendered context by ~89% in the paper while keeping most utility.
- Do not dump CodeSkillBank into the window. The paper's evals used a 10% retrieval sample.
