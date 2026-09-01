"""Search, ranking, and SOTA discovery engine for training agents."""

import re
from dataclasses import dataclass
from typing import List, Dict, Any, Optional, Tuple
from library.graph import KnowledgeGraph, Node


@dataclass
class SearchResult:
    node: Node
    score: float
    reasons: List[str]
    sota_status: str
    direct_path: Optional[List[str]] = None


def tokenize(text: str) -> List[str]:
    """Tokenize and lowercase text for indexing and search."""
    return [t.lower() for t in re.findall(r"[a-zA-Z0-9_-]+", text) if len(t) > 1]


class QueryEngine:
    """Ranks knowledge graph nodes for training agent queries."""

    def __init__(self, graph: KnowledgeGraph):
        self.graph = graph

    def query(
        self,
        query_str: str,
        top_k: int = 10,
        node_type: Optional[str] = None,
        domain: Optional[str] = None,
        sota_only: bool = False
    ) -> List[SearchResult]:
        query_tokens = set(tokenize(query_str))
        if not query_tokens:
            return []

        results: List[SearchResult] = []

        for node in self.graph.nodes.values():
            if node_type and node.type != node_type:
                continue

            if domain and node.domain and node.domain.lower() != domain.lower():
                continue

            if sota_only and not node.is_sota:
                continue

            score = 0.0
            reasons: List[str] = []

            # Match ID
            id_tokens = set(tokenize(node.id))
            id_matches = query_tokens.intersection(id_tokens)
            if id_matches:
                match_weight = len(id_matches) * 20.0
                score += match_weight
                reasons.append(f"matched ID tokens: {', '.join(id_matches)}")

            # Match Title
            title_tokens = set(tokenize(node.title))
            title_matches = query_tokens.intersection(title_tokens)
            if title_matches:
                match_weight = len(title_matches) * 15.0
                score += match_weight
                reasons.append(f"matched title tokens: {', '.join(title_matches)}")

            # Match Tags
            tags_tokens = set()
            for tag in node.tags:
                tags_tokens.update(tokenize(tag))
            tag_matches = query_tokens.intersection(tags_tokens)
            if tag_matches:
                match_weight = len(tag_matches) * 10.0
                score += match_weight
                reasons.append(f"matched tags: {', '.join(tag_matches)}")

            # SOTA Status Boost
            if node.type == "method" and node.status == "sota":
                score += 8.0
                reasons.append("current SOTA status")
            elif node.type == "task" and node.metadata.get("current_sota"):
                score += 5.0

            # Match Summary / Abstract
            summary_text = node.metadata.get("summary", "") or node.metadata.get("abstract_summary", "")
            if summary_text:
                sum_tokens = set(tokenize(summary_text))
                sum_matches = query_tokens.intersection(sum_tokens)
                if sum_matches:
                    score += len(sum_matches) * 4.0
                    reasons.append(f"matched summary tokens: {', '.join(sum_matches)}")

            # Match Claims
            claims = node.metadata.get("claims", [])
            for c in claims:
                if isinstance(c, dict):
                    c_text = f"{c.get('benchmark', '')} {c.get('metric', '')} {c.get('notes', '')}"
                    c_tokens = set(tokenize(c_text))
                    c_matches = query_tokens.intersection(c_tokens)
                    if c_matches:
                        score += len(c_matches) * 5.0
                        reasons.append(f"matched claim benchmarks: {', '.join(c_matches)}")

            # Match Markdown Body
            body_tokens = set(tokenize(node.body))
            body_matches = query_tokens.intersection(body_tokens)
            if body_matches:
                score += min(len(body_matches) * 1.5, 15.0)

            if score > 0:
                sota_desc = "SOTA" if node.is_sota else (node.status or "active")
                results.append(SearchResult(
                    node=node,
                    score=score,
                    reasons=reasons,
                    sota_status=sota_desc
                ))

        results.sort(key=lambda x: x.score, reverse=True)
        return results[:top_k]

    def sota(self, task_or_query: str) -> List[Dict[str, Any]]:
        """Finds SOTA resolutions matching the task name or domain."""
        # 1. Check exact task match
        direct_task = self.graph.get_node(task_or_query)
        if direct_task and direct_task.type == "task":
            return self.graph.get_sota_path_for_task(direct_task.id)

        # 2. Search for tasks matching query
        task_results = self.query(task_or_query, top_k=5, node_type="task")
        sota_paths: List[Dict[str, Any]] = []
        seen_methods = set()

        for res in task_results:
            paths = self.graph.get_sota_path_for_task(res.node.id)
            for p in paths:
                m_id = p["method"].id
                if m_id not in seen_methods:
                    seen_methods.add(m_id)
                    sota_paths.append(p)

        # 3. If no task found, query methods directly for SOTA
        if not sota_paths:
            method_results = self.query(task_or_query, top_k=5, node_type="method", sota_only=True)
            for res in method_results:
                m = res.node
                # Gather papers and recipes
                papers = [self.graph.get_node(p_id) for p_id in m.get("papers", []) if self.graph.get_node(p_id)]
                recipes = [self.graph.get_node(r_id) for r_id in m.get("recipes", []) if self.graph.get_node(r_id)]
                target_tasks = [self.graph.get_node(t_id) for t_id in m.get("sota_for", []) if self.graph.get_node(t_id)]

                sota_paths.append({
                    "task": target_tasks[0] if target_tasks else None,
                    "method": m,
                    "papers": papers,
                    "recipes": recipes,
                    "claims": m.get("claims", [])
                })

        return sota_paths

    def _score_task(
        self,
        node: Node,
        query_tokens: set,
        query_norm: str,
    ) -> Tuple[float, List[str]]:
        score = 0.0
        reasons: List[str] = []

        id_tokens = set(tokenize(node.id))
        id_matches = query_tokens.intersection(id_tokens)
        if id_matches:
            score += len(id_matches) * 20.0
            reasons.append(f"matched ID tokens: {', '.join(sorted(id_matches))}")

        title_tokens = set(tokenize(node.title))
        title_matches = query_tokens.intersection(title_tokens)
        if title_matches:
            score += len(title_matches) * 15.0
            reasons.append(f"matched title tokens: {', '.join(sorted(title_matches))}")

        title_norm = " ".join(tokenize(node.title))
        if query_norm and query_norm in title_norm:
            score += 30.0
            reasons.append("phrase match in title")
        id_norm = " ".join(tokenize(node.id))
        if query_norm and query_norm in id_norm:
            score += 28.0
            reasons.append("phrase match in id")

        tags_tokens = set()
        for tag in node.tags:
            tags_tokens.update(tokenize(tag))
        tag_matches = query_tokens.intersection(tags_tokens)
        if tag_matches:
            score += len(tag_matches) * 10.0
            reasons.append(f"matched tags: {', '.join(sorted(tag_matches))}")

        for field, weight, label in (
            ("summary", 4.0, "summary"),
            ("scope", 8.0, "scope"),
        ):
            text = node.metadata.get(field) or ""
            if not text:
                continue
            matches = query_tokens.intersection(set(tokenize(text)))
            if matches:
                score += len(matches) * weight
                reasons.append(f"matched {label} tokens: {', '.join(sorted(matches))}")

        for item in node.metadata.get("out_of_scope") or []:
            matches = query_tokens.intersection(set(tokenize(str(item))))
            if matches:
                score += len(matches) * 2.0
                reasons.append(f"near-miss out_of_scope: {item}")

        if node.metadata.get("current_sota"):
            score += 5.0

        return score, reasons

    def route(self, query_str: str, top_k: int = 8) -> List[SearchResult]:
        """Rank candidate tasks with scope/redirects. Never returns an empty list if tasks exist."""
        tasks = self.graph.get_nodes_by_type("task")
        if not tasks:
            return []

        query_tokens = set(tokenize(query_str or ""))
        query_norm = " ".join(tokenize(query_str or ""))
        scored: Dict[str, SearchResult] = {}

        for node in tasks:
            score, reasons = self._score_task(node, query_tokens, query_norm)
            scored[node.id] = SearchResult(
                node=node,
                score=score,
                reasons=reasons,
                sota_status="SOTA" if node.metadata.get("current_sota") else (node.status or "task"),
            )

        for node in tasks:
            for redirect in node.metadata.get("redirects") or []:
                if not isinstance(redirect, dict):
                    continue
                when = str(redirect.get("when") or "")
                target_id = redirect.get("to")
                if not target_id or target_id not in scored:
                    continue
                when_tokens = set(tokenize(when))
                when_norm = " ".join(tokenize(when))
                overlap = query_tokens.intersection(when_tokens)
                phrase = bool(query_norm and query_norm in when_norm)
                if not overlap and not phrase:
                    continue
                bonus = 25.0 + 4.0 * len(overlap)
                target = scored[target_id]
                target.score += bonus
                target.reasons.append(f"redirect from {node.id} when {when}")
                source = scored[node.id]
                source.reasons.append(f"redirects to {target_id} when {when}")

        ranked = sorted(scored.values(), key=lambda r: (-r.score, r.node.id))
        positive = [r for r in ranked if r.score > 0]
        if positive:
            results = positive[:top_k]
            if len(results) < min(3, len(ranked)):
                for extra in ranked:
                    if extra in results:
                        continue
                    extra.reasons.append("near-miss padding")
                    results.append(extra)
                    if len(results) >= min(3, len(ranked)):
                        break
            return results

        fallback = ranked[: max(top_k, 3)]
        for item in fallback:
            item.reasons.append("no lexical match; near-miss first-hop task")
        return fallback

