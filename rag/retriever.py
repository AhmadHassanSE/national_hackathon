"""Free local retrieval helpers for Haalat.

The retriever uses the JSON TF-IDF indexes built by knowledge_base.py. No Gemini
embedding calls, Chroma vector DB calls, or paid embedding services are used.
"""

from __future__ import annotations

import json
import math
from pathlib import Path
from typing import Any

try:
    from .knowledge_base import (
        CATEGORY_COLLECTION,
        INDEX_DIR,
        PROTOCOL_COLLECTION,
        build_knowledge_base,
        tokenize,
    )
except ImportError:
    from knowledge_base import (  # type: ignore
        CATEGORY_COLLECTION,
        INDEX_DIR,
        PROTOCOL_COLLECTION,
        build_knowledge_base,
        tokenize,
    )


DEFAULT_TOP_K = 3


def _index_path(collection_name: str) -> Path:
    return INDEX_DIR / f"{collection_name}.json"


def _load_index(collection_name: str) -> dict[str, Any]:
    build_knowledge_base(quiet=True)

    path = _index_path(collection_name)
    if not path.exists():
        raise RuntimeError(f"Local retrieval index not found: {path}")

    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Local retrieval index is invalid JSON: {path}") from exc


def _score_chunk(query_terms: dict[str, int], chunk: dict[str, Any], idf: dict[str, float]) -> float:
    score = 0.0
    chunk_terms = chunk.get("term_counts", {})
    chunk_length = max(float(chunk.get("token_count", 1)), 1.0)

    for token, query_count in query_terms.items():
        if token not in chunk_terms:
            continue
        term_frequency = float(chunk_terms[token]) / chunk_length
        score += query_count * term_frequency * float(idf.get(token, 1.0))

    text = str(chunk.get("text", "")).lower()
    if text.startswith("protocol:") or text.startswith("category:"):
        heading_tokens = set(tokenize(text[:160]))
        overlap = heading_tokens.intersection(query_terms)
        score += 0.15 * len(overlap)

    return score


def _retrieve_context(collection_name: str, query: str, top_k: int = DEFAULT_TOP_K) -> list[str]:
    if not query or not query.strip():
        raise ValueError("Query must be a non-empty string.")

    index = _load_index(collection_name)
    tokens = tokenize(query)
    if not tokens:
        return []

    query_terms = {token: tokens.count(token) for token in set(tokens)}
    idf = index.get("idf", {})

    ranked = []
    for chunk in index.get("chunks", []):
        score = _score_chunk(query_terms, chunk, idf)
        ranked.append((score, chunk))

    ranked.sort(key=lambda item: item[0], reverse=True)
    matches = [chunk["text"] for score, chunk in ranked[:top_k] if score > 0]

    if matches:
        return matches

    # Fall back to the first chunks so downstream prompts still have context.
    return [chunk["text"] for chunk in index.get("chunks", [])[:top_k]]


def retrieve_category_context(query: str) -> list[str]:
    """Return top matching emergency category snippets for a query."""
    return _retrieve_context(CATEGORY_COLLECTION, query)


def retrieve_protocol_context(query: str) -> list[str]:
    """Return top matching emergency protocol snippets for a query."""
    return _retrieve_context(PROTOCOL_COLLECTION, query)
