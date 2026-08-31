---
id: recipe:bmssp-python
type: recipe
title: "Unofficial BMSSP Python Sketch"
method: method:bmssp
task: task:directed-sssp-nonneg
target_hardware: "CPU (typical laptop); no GPU required"
framework: "Python 3.9+"
repo_url: "https://github.com/hparreao/BMSSP-Python"
pip_dependencies:
  - "numpy>=1.21.0"
  - "scipy>=1.3.0"
tags:
  - algorithms
  - graph-algorithms
  - sssp
  - bmssp
  - unofficial
---

# Unofficial BMSSP Python Sketch

This recipe is **unofficial and not author-maintained**. There is no official Duan et al. repository. Theoretical constants are large: **Dijkstra still wins on typical \(n\)**. Do not treat BMSSP as a production shortest-path implementation.

Unofficial third-party ports:
- Python: `https://github.com/hparreao/BMSSP-Python` (this recipe's `repo_url`)
- Java: `https://github.com/NicholasCartaxo/BMSSP-SSSP`

## Hardware & Environment Setup
- CPU-only. Install from the unofficial Python repo; `pip install -r requirements.txt` there lists pytest, numpy, scipy, networkx, matplotlib, psutil.
- Parameters from the paper: \(k=\lfloor\log^{1/3}n\rfloor\), \(t=\lfloor\log^{2/3}n\rfloor\), level \(\lceil(\log n)/t\rceil\).

## Quickstart Implementation

```python
from bmssp_py.common import Graph
from bmssp_py.bmssp import BMSSPAlgorithm, choose_parameters

g = Graph(5)
g.add_directed_edge(0, 1, 1.0)
g.add_directed_edge(1, 2, 2.0)
g.add_directed_edge(2, 3, 1.0)
g.add_directed_edge(3, 4, 3.0)

k, t, l = choose_parameters(g.n, mode="balanced")
algo = BMSSPAlgorithm(g, l=l, B=float("inf"), sources=[0], k_override=k, t_override=t)
dist = algo.solve()
print(dist)
```

## Critical Hyperparameters & Tuning Advice
- **\(k=\lfloor\log^{1/3}n\rfloor\)**, **\(t=\lfloor\log^{2/3}n\rfloor\)**: paper defaults. Unofficial Python `choose_parameters(..., mode="performance")` retunes for small graphs; that is an implementation heuristic, not the theorem.
- **Bound \(B\)**: \(\infty\) at the top-level call; recursive calls use finite bounds and must never write distances \(\geq B\).
- **Typical \(n\)**: use Dijkstra. Unofficial Java experiments on sparse \(n\in[10^3,10^6]\) (constant-degree, \(m=2n\)) report Dijkstra still faster, with the BMSSP/Dijkstra time ratio decreasing as \(n\) grows.
