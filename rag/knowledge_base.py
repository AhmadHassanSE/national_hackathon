"""Free local RAG index builder for Haalat.

This module intentionally avoids paid embedding APIs. It builds a small local
JSON TF-IDF style index from the seeded emergency text files using LangChain's
free text splitter and a simple tokenizer.
"""

from __future__ import annotations

import json
import math
import re
from collections import Counter
from pathlib import Path
from typing import Any

from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter


PROJECT_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = PROJECT_ROOT / "data"
INDEX_DIR = Path(__file__).resolve().parent / "local_index"

CATEGORY_COLLECTION = "emergency_categories"
PROTOCOL_COLLECTION = "emergency_protocols"

SOURCE_FILES = {
    CATEGORY_COLLECTION: DATA_DIR / "emergency_categories.txt",
    PROTOCOL_COLLECTION: DATA_DIR / "emergency_protocols.txt",
}

TOKEN_PATTERN = re.compile(r"[a-zA-Z0-9_]+")


def tokenize(text: str) -> list[str]:
    """Tokenize English/Roman Urdu emergency text without external services."""
    return TOKEN_PATTERN.findall(text.lower())


def _load_text(path: Path) -> str:
    if not path.exists():
        raise FileNotFoundError(f"Knowledge source file not found: {path}")
    return path.read_text(encoding="utf-8")


def _split_text(text: str, source_name: str) -> list[Document]:
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50,
        separators=["\n\n", "\n", ". ", " ", ""],
    )
    return splitter.create_documents([text], metadatas=[{"source": source_name}])


def _build_index_payload(collection_name: str, source_path: Path) -> dict[str, Any]:
    documents = _split_text(_load_text(source_path), source_path.name)
    if not documents:
        raise RuntimeError(f"No chunks produced for {source_path}")

    document_tokens = [tokenize(document.page_content) for document in documents]
    document_frequencies: Counter[str] = Counter()

    for tokens in document_tokens:
        document_frequencies.update(set(tokens))

    total_documents = len(documents)
    chunks = []

    for index, document in enumerate(documents):
        tokens = document_tokens[index]
        term_counts = Counter(tokens)
        chunks.append(
            {
                "id": f"{collection_name}-{index}",
                "text": document.page_content,
                "metadata": document.metadata,
                "term_counts": dict(term_counts),
                "token_count": max(len(tokens), 1),
            }
        )

    idf = {
        token: math.log((1 + total_documents) / (1 + frequency)) + 1
        for token, frequency in document_frequencies.items()
    }

    return {
        "collection": collection_name,
        "source": str(source_path),
        "retriever": "local_tfidf",
        "chunk_size": 500,
        "chunk_overlap": 50,
        "document_count": total_documents,
        "idf": idf,
        "chunks": chunks,
    }


def _index_path(collection_name: str) -> Path:
    return INDEX_DIR / f"{collection_name}.json"


def collection_exists(collection_name: str) -> bool:
    path = _index_path(collection_name)
    if not path.exists():
        return False

    try:
        payload = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return False

    return bool(payload.get("chunks"))


class HaalatKnowledgeBase:
    """Builds free local retrieval indexes for Haalat emergency knowledge."""

    def __init__(self, index_directory: Path | str = INDEX_DIR) -> None:
        self.index_directory = Path(index_directory)
        self.index_directory.mkdir(parents=True, exist_ok=True)

    def build_if_missing(self, force: bool = False, quiet: bool = False) -> None:
        for collection_name, source_path in SOURCE_FILES.items():
            if not force and collection_exists(collection_name):
                if not quiet:
                    print(f"Local index '{collection_name}' already exists. Skipping build.")
                continue
            self.build_collection(collection_name, source_path)

    def build_collection(self, collection_name: str, source_path: Path) -> None:
        payload = _build_index_payload(collection_name, source_path)
        output_path = _index_path(collection_name)
        output_path.write_text(
            json.dumps(payload, indent=2, ensure_ascii=False),
            encoding="utf-8",
        )
        print(
            f"Built local index '{collection_name}' with "
            f"{payload['document_count']} chunks."
        )


def build_knowledge_base(force: bool = False, quiet: bool = False) -> None:
    HaalatKnowledgeBase().build_if_missing(force=force, quiet=quiet)


if __name__ == "__main__":
    build_knowledge_base(force=True)
