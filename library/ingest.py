"""Interactive or programmatic ingestion helper for new nodes."""

from pathlib import Path
from typing import Dict, Any, Optional
import yaml


TEMPLATES = {
    "task": """---
id: task:{slug}
type: task
title: "{title}"
domain: "{domain}"
summary: "{summary}"
current_sota:
  - method: method:example-method
    as_of: "2026-01"
    benchmark: "BenchmarkName"
    metric: "accuracy"
    value: 95.5
    notes: "Baseline evaluation on standard test split."
methods:
  - method:example-method
tags:
  - {domain}
  - deep-learning
---

# {title}

## Problem Definition
Describe the fundamental ML optimization or modeling problem here.

## Evaluation Protocol
- **Primary Benchmarks**: List standard evaluation datasets and metrics.
- **Evaluation Pitfalls**: Common data contamination or measurement hazards.

## SOTA Landscape
Summary of current best practices and historical transitions.
""",

    "method": """---
id: method:{slug}
type: method
title: "{title}"
category: "{category}"
status: sota
sota_for:
  - task:example-task
supersedes: []
papers:
  - paper:example-paper
recipes:
  - recipe:example-recipe
claims:
  - benchmark: "StandardBench"
    metric: "score"
    value: 88.4
    baseline: "PreviousMethod (82.1)"
    date: "2026-01"
    verified: true
    notes: "Verified under standard compute budget."
tags:
  - {category}
  - optimization
---

# {title}

## Method Overview
Concise mathematical and architectural summary of how the method works.

## When to Use
- When training on ...
- If compute constraints require ...

## Gotchas & Failure Modes
- Hyperparameter sensitivity (e.g. learning rate, momentum).
- Hardware or memory limitations.
- Situations where this method underperforms baselines.
""",

    "paper": """---
id: paper:{slug}
type: paper
title: "{title}"
authors:
  - "First Author"
  - "Second Author"
year: 2026
month: 1
arxiv_id: "{arxiv_id}"
url: "https://arxiv.org/abs/{arxiv_id}"
methods:
  - method:example-method
cites: []
tags:
  - machine-learning
---

# {title}

## Abstract Summary
Key problem statement, core breakthrough, and main results.

## Key Contributions
1. First contribution.
2. Second contribution.

## Empirical Highlights
- Benchmark result 1 vs baselines.
- Compute scaling efficiency observations.
""",

    "recipe": """---
id: recipe:{slug}
type: recipe
title: "{title}"
method: method:example-method
task: task:example-task
target_hardware: "1x NVIDIA H100 80GB (or 1x RTX 4090 24GB with batch reduction)"
framework: "PyTorch 2.5+"
repo_url: "https://github.com/example/repo"
pip_dependencies:
  - "torch>=2.5.0"
  - "transformers>=4.48.0"
tags:
  - training-recipe
---

# {title}

## Hardware & Environment Setup
- Recommended GPU: 1x H100 80GB or 1x RTX 4090 (24GB VRAM).
- CUDA: >= 12.4.

## Quickstart Code

```python
import torch

# Minimal runnable example
print("Training initialized")
```

## Critical Hyperparameters
- Learning rate: 1e-4
- Warmup steps: 100
- Weight decay: 0.01
"""
}


def create_node_from_template(
    node_type: str,
    slug: str,
    title: Optional[str] = None,
    output_dir: Optional[Path] = None,
    extra_fields: Optional[Dict[str, Any]] = None
) -> Path:
    """Generates a new node file from a standard template."""
    if node_type not in TEMPLATES:
        raise ValueError(f"Unknown node type '{node_type}'. Must be one of: {list(TEMPLATES.keys())}")

    title = title or slug.replace("-", " ").title()
    extra_fields = extra_fields or {}

    domain = extra_fields.get("domain", "pretraining")
    category = extra_fields.get("category", "optimizer")
    summary = extra_fields.get("summary", "Summary of the task objective.")
    arxiv_id = extra_fields.get("arxiv_id", "2501.00000")

    content = TEMPLATES[node_type].format(
        slug=slug,
        title=title,
        domain=domain,
        category=category,
        summary=summary,
        arxiv_id=arxiv_id
    )

    if output_dir is None:
        output_dir = Path("graph") / f"{node_type}s"

    output_dir.mkdir(parents=True, exist_ok=True)
    target_file = output_dir / f"{slug}.md"

    if target_file.exists():
        raise FileExistsError(f"File already exists: {target_file}")

    target_file.write_text(content, encoding="utf-8")
    return target_file
