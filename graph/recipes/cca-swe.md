---
id: recipe:cca-swe
type: recipe
title: "CCA SWE-bench harness"
method: method:cca
task: task:software-engineering-agent-harness
target_hardware: "Docker host + Bedrock/Anthropic (paper SWE-bench-Pro path)"
framework: "Python 3.12 / conda / facebookresearch/cca-swebench"
repo_url: "https://github.com/facebookresearch/cca-swebench"
pip_dependencies:
  - "conda"
tags:
  - recipe
  - agents
  - cca
  - swe-bench
---

# CCA SWE-bench harness

Agent runs **inside** the container. Not the default first hop (mini-SWE-agent is).

## Hardware & Environment Setup
From `https://github.com/facebookresearch/cca-swebench`:

```bash
conda create -n confucius python=3.12 -y
conda activate confucius
pip install -r requirements.txt
```

SWE-bench-Pro docker entrypoint (repo `scripts/run_sbp.sh`):

```bash
docker run --rm -e TASK_ID={} -e AWS_BEARER_TOKEN_BEDROCK=<token> \
  -v <workspace>:/data --network host --userns=host \
  --entrypoint /data/run_sbp.sh
```

PEX packaging for in-container entry (`scripts.run_swebench`) is documented in the README.

## Quickstart Implementation

```python
# CCA is launched in-container via the harness, not as a 100-line host loop.
# After pip install -r requirements.txt, follow scripts/run_swebench.py for
# SWE-bench-Pro / SWE-bench Verified instance entrypoints.
print("cca-swebench: conda env + pip install -r requirements.txt, then docker run_sbp.sh")
```

## Critical Hyperparameters & Tuning Advice
- Use when notes/context management beyond bash is required.
- Equal-model/tools vs SWE-agent is the paper protocol (Claude 4.5 Sonnet Pro 52.7 vs 43.6).
