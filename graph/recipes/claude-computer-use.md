---
id: recipe:claude-computer-use
type: recipe
title: "Claude computer-use on OSWorld 2.0 protocol"
method: method:claude-computer-use
task: task:computer-use-agent
target_hardware: "desktop VM / OSWorld 2.0 environment; Anthropic API"
framework: "Anthropic computer-use API"
repo_url: "https://github.com/anthropics/anthropic-quickstarts"
pip_dependencies:
  - "anthropic"
tags:
  - recipe
  - agents
  - computer-use
  - osworld
---

# Claude computer-use on OSWorld 2.0 protocol

Paper protocol SOTA is **20.6% binary / 54.8% partial** (Opus 4.8 max think + batched tools). Do not cite aggregator 70.6%.

## Hardware & Environment Setup
- OSWorld 2.0 environment from `https://arxiv.org/abs/2606.29537`.
- Anthropic API with computer-use tool; max thinking; batched tools.

## Quickstart Implementation

```python
import anthropic

client = anthropic.Anthropic()
response = client.beta.messages.create(
    model="claude-opus-4-8",
    max_tokens=8192,
    tools=[{"type": "computer_20250124", "name": "computer"}],
    messages=[{"role": "user", "content": "Complete the OSWorld 2.0 task. Verify constraints before finishing."}],
    betas=["computer-use-2025-01-24"],
)
print(response.stop_reason)
```

## Critical Hyperparameters & Tuning Advice
- **Protocol**: OSWorld 2.0, not OSWorld-Verified, not aggregator boards.
- **Failure mode**: lost constraints and skipped verification — force a verify step.
- **Not SWE**: GitHub issue → patch is mini-SWE-agent.
