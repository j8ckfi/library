---
id: method:dijkstra
type: method
title: "Dijkstra's Algorithm (Fibonacci / Relaxed Heap)"
category: "graph-algorithms"
status: superseded
sota_for: []
supersedes: []
superseded_by: method:bmssp
papers: []
recipes: []
claims:
  - benchmark: "Directed SSSP, real non-negative weights, comparison-addition model"
    metric: "worst-case time"
    value: "O(m + n log n)"
    baseline: "Binary-heap Dijkstra O((m+n) log n)"
    date: "2026-08"
    verified: true
    notes: "Fibonacci heap (Fredman-Tarjan) / relaxed heap. Still the practical production default. Optimal if the algorithm must output the vertex order by distance (Haeupler-Hladik-Rozhon-Tarjan-Tetek, FOCS 2024). Superseded by BMSSP only for computing distances on sparse directed graphs in this model."
tags:
  - algorithms
  - graph-algorithms
  - sssp
  - dijkstra
  - baseline
---

# Dijkstra's Algorithm (Fibonacci / Relaxed Heap)

## Method Overview
Dijkstra's algorithm maintains a priority queue of the frontier of discovered vertices and repeatedly extracts the vertex \(u\) of minimum tentative distance, then relaxes outgoing edges of \(u\). With a Fibonacci heap or relaxed heap it runs in \(O(m+n\log n)\) in the comparison-addition model.

Extracting the closest frontier vertex produces a total order of vertices by distance from the source as a byproduct. That order is the source of the \(\Omega(n\log n)\) sorting barrier when the frontier is large.

## When to Use
- Practical production single-source shortest paths on graphs with non-negative weights.
- Any setting that requires the vertices in increasing-distance order.
- Typical \(n\), where BMSSP's constants dominate the \(\log^{2/3}n\) vs \(\log n\) gap.

## Gotchas & Failure Modes
- Not asymptotically optimal for *distances only* on sparse directed graphs in the comparison-addition model (`method:bmssp`).
- Negative edge weights require a different algorithm (Bellman-Ford / recent negative-weight SSSP).

## Supersession
- Superseded by `method:bmssp` for directed SSSP distances on sparse graphs in the comparison-addition model. Remains the practical default.
