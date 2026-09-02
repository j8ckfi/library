---
id: recipe:omp2-harness
type: recipe
title: "omp² harness kernel (journal → session DOM)"
method: method:omp2-harness
task: task:agent-harness-runtime
target_hardware: "CPU; host process plus optional sandbox/VM stub"
framework: "Rust engine + embedded Python (spec; omp² in progress)"
repo_url: "https://stencil.so/blog/harness-playbook"
pip_dependencies: []
tags:
  - recipe
  - agents
  - harness
  - omp2
  - stencil
---

# omp² harness kernel (journal → session DOM)

The playbook is the spec. omp² is still being built against it; **no public omp² repository** is linked from the post. Do not copy Pi's three-callback tool API or dual authorities. Implement journal → DOM first.

Spec: `https://stencil.so/blog/harness-playbook`

## Hardware & Environment Setup
- Host process owns policy, inference, journal, and tool routing.
- Sandbox is a bandwidth-bounded execution stub (local process, container, VM, or remote machine).
- Extensions: embedded Python (`@remote`, dependable `Eval`). Engine language in the playbook is Rust.

## Quickstart Implementation

Fold the journal into one session tree. Runtime indexes are caches of this fold, not a second authority.

```python
from dataclasses import dataclass, field
from typing import Any


@dataclass
class SessionDOM:
    nodes: dict[str, dict[str, Any]] = field(default_factory=dict)

    def apply(self, ops: list[list[Any]]) -> None:
        for op in ops:
            kind, node_id, *rest = op
            if kind == "set":
                key, value = rest
                self.nodes.setdefault(node_id, {})[key] = value
            elif kind == "create":
                self.nodes[node_id] = dict(rest[0])
            elif kind == "destroy":
                self.nodes.pop(node_id, None)
            else:
                raise ValueError(f"unknown journal op: {kind}")

    def snapshot(self) -> dict[str, dict[str, Any]]:
        return {k: dict(v) for k, v in self.nodes.items()}


def materialize(journal: list[dict[str, Any]]) -> SessionDOM:
    dom = SessionDOM()
    for event in journal:
        dom.apply(event["ops"])
    return dom
```

Rewind is a DOM diff against a prior materialization: disappeared job elements are terminated; appeared elements are spawned. Adding a stateful feature must not add a rewind/fork/resume call site.

## Critical Hyperparameters & Tuning Advice
- **Do not** implement `renderCall` / `execute` / `renderResult` as the tool contract. A call is an element with `input` / `result` / `diag` / `usage`.
- **Do not** put MCP in the permanent tool grammar. Tiny roster; long tail via `dyn` synthesized from JSON schema plus Bash/Read.
- Bound output and blocking time in the job primitive, not in each tool.
- Speculative compaction ~10% before the context limit; splice onto the live branch.
- Forced tools: soft prompt always; native `tool_choice` only if free; escalate on non-compliance.
- SWE-bench / issue → patch is `recipe:mini-swe-agent`, not this recipe.
