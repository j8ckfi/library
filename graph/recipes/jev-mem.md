---
id: recipe:jev-mem
type: recipe
title: "Jev-Mem System-One Memory Control"
method: method:jev-mem
task: task:agent-memory
target_hardware: "CPU; live runs need TypeSafe + an OpenAI-compatible answer model"
framework: "Python 3.11+"
repo_url: "https://github.com/libingzheren/Jev-Mem"
code_status: released
pip_dependencies: []
tags:
  - recipe
  - jev-mem
  - agent-memory
---

# Jev-Mem System-One Memory Control

## Hardware & Environment Setup
- Official: `https://github.com/libingzheren/Jev-Mem`. Space: Hugging Face `libingzheren/Jev-Mem`.
- ACE remains the playbook/memory default. Code2Skill remains the repository skill bank.

```bash
python3.11 -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python -m jev_mem.demo
```

The demo uses mock decisions and embeddings; no API keys. Live runs need `TYPESAFE_API_KEY` and `OPENAI_API_KEY` in `.env`. Default embedding backend `minilm` downloads on first use.

## Quickstart Implementation

```bash
python -m jev_mem --mode build --input examples/observations.json \
  --jev-config config/jev_mem.json --cache-dir ./jev_mem_cache/app

python -m jev_mem --mode query --question "What reminder does Mira prefer?" \
  --jev-config config/jev_mem.json --cache-dir ./jev_mem_cache/app
```

Input is a JSON list of strings or objects with `content`, optional ISO-8601 `timestamp`, and optional `metadata`.

## Critical Hyperparameters & Tuning Advice
- Keep original observations. Selectivity is in relations and retrieval, not irreversible discard at ingest.
- Relation insert threshold \(\theta_{\mathrm{rel}}\) and retrieval stop thresholds \(\theta_{\mathrm{suff}}\) / \(\theta_{\mathrm{cont}}\) are in `config/jev_mem.json`.
- Do not dump the full graph into System Two. Retrieval already budgets views and depth.
