---
id: method:bmssp
type: method
title: "BMSSP (Bounded Multi-Source Shortest Path)"
category: "graph-algorithms"
status: sota
sota_for:
  - task:directed-sssp-nonneg
supersedes:
  - method:dijkstra
papers:
  - paper:sorting-barrier-sssp
recipes:
  - recipe:bmssp-python
claims:
  - benchmark: "Directed SSSP, real non-negative weights, comparison-addition model"
    metric: "worst-case time"
    value: "O(m log^{2/3} n)"
    baseline: "Dijkstra O(m + n log n) on sparse directed graphs"
    date: "2026-08"
    verified: true
    notes: "Theorem 1.1 of arXiv:2504.17033. First break of Dijkstra on sparse directed graphs. First deterministic break of that bound even on undirected graphs (DMSY23 was randomized). Computes distances, not the vertex order. Not a practical production shortest-path algorithm."
tags:
  - algorithms
  - graph-algorithms
  - sssp
  - directed-graphs
  - comparison-addition
  - bmssp
  - sota
---

# BMSSP (Bounded Multi-Source Shortest Path)

## Method Overview
BMSSP is a deterministic divide-and-conquer algorithm for directed single-source shortest paths with real non-negative weights in the comparison-addition model. It computes distances \(d(v)\), not a total order of vertices by distance.

The Dijkstra frontier can contain \(\Theta(n)\) vertices; repeatedly extracting the closest vertex maintains a total order and costs \(\Omega(n\log n)\). BMSSP shrinks that frontier and recurses on bounded multi-source subproblems:

1. **Parameters**: \(k=\lfloor\log^{1/3}n\rfloor\), \(t=\lfloor\log^{2/3}n\rfloor\). Recursion depth is \(O((\log n)/t)\).
2. **FindPivots**: from a frontier \(S\) and bound \(B\), run \(k\) Bellman-Ford-like relaxations. Vertices whose shortest path uses fewer than \(k\) in-bound vertices become complete. Remaining incomplete vertices depend on roots of shortest-path trees of size \(\geq k\); those roots are the pivots \(P\subseteq S\) with \(|P|\leq |\widetilde{U}|/k\).
3. **BMSSP recursion**: at level \(l\), shrink \(S\) to pivots, then make recursive calls on level \(l-1\) with a partial-sorting heap (Insert / BatchPrepend / Pull) until the bound \(B\) is reached or the completed set \(U\) hits \(\Theta(k\,2^{lt})\).
4. **Top-level call**: \(\mathrm{BMSSP}(\lceil(\log n)/t\rceil, B=\infty, S=\{s\})\) yields all distances in \(O(m\log^{2/3}n)\) time.

The paper reduces to constant in-/out-degree via a classical cycle transformation that preserves shortest-path distances and uses \(O(m)\) vertices and edges.

## When to Use
- Theoretical SOTA for directed SSSP *distances* on sparse graphs with real non-negative weights in the comparison-addition model.
- Do **not** use as a production shortest-path algorithm. Dijkstra remains the practical default on typical \(n\).
- Do **not** use for ML training (dense/MoE pretrain, CISPO, Muon, OLMo, LoRA, distillation).

## Gotchas & Failure Modes
- **Distances, not order**: Haeupler–Hladík–Rozhoň–Tarjan–Tětek (FOCS 2024) show Dijkstra is optimal if the algorithm must output the order of vertices by distance. This method does not produce that sort.
- **Constants**: unofficial implementations remain slower than Dijkstra on graphs of typical size. The asymptotic win is for sparse directed graphs in the comparison-addition model, not wall-clock on ordinary instances.
- **Model**: comparison-addition, non-negative real weights. Not a RAM/integer-weight algorithm (Thorup and related integer-weight results are a different model). Does not handle negative weights.
- **No official code**: author-maintained repository is not published. Third-party ports exist and are unofficial.

## Supersession
- Supersedes `method:dijkstra` as the comparison-addition SOTA for directed SSSP *distances* on sparse graphs. Dijkstra stays the practical default and is still optimal when the vertex order is required.
