"""Prompt assembly helpers for Gemini generation.

RAG retrieval is handled locally for free. Gemini receives the final grounded
prompt and does only reasoning/response generation.
"""

from __future__ import annotations

from rag.retriever import retrieve_category_context, retrieve_protocol_context


SYSTEM_PROMPT = """You are Haalat, a real-time emergency intelligence assistant for Pakistan.

Core operating rules:
1. Preserve the user's source language in all user-facing text. If the user mixes Roman Urdu and English, respond in the same mixed style.
2. Treat emergencies conservatively. If cardiac arrest, unconsciousness, severe bleeding, gas leak, or airway danger is possible, escalate severity.
3. Use the provided RAG context as the source of truth for categories, severity, and first-response guidance.
4. Give concise, dispatch-ready output. Do not invent hospitals, volunteers, phone numbers, or distances.
5. Include immediate safety guidance, nearest resource summary, and a clear emergency type/severity.
6. This is decision-support only; always encourage calling local emergency services for life-threatening cases.
"""


def build_gemini_emergency_prompt(
    user_input: str,
    user_location: str,
    resource_summary: str | None = None,
) -> str:
    """Build one complete Gemini prompt from local RAG context and user data."""
    category_context = "\n\n---\n\n".join(retrieve_category_context(user_input))
    protocol_context = "\n\n---\n\n".join(retrieve_protocol_context(user_input))
    resource_block = resource_summary or "Resource lookup has not been run yet."

    return f"""{SYSTEM_PROMPT}

LOCAL RAG CONTEXT: EMERGENCY CATEGORIES
{category_context}

LOCAL RAG CONTEXT: FIRST-AID PROTOCOLS
{protocol_context}

RESOURCE LOOKUP RESULT
{resource_block}

USER INPUT
{user_input}

USER LOCATION
{user_location}

TASK
Analyze the user input, infer the source language, classify the emergency type,
assign severity from 1 to 5, and produce a final emergency response in the
user's source language.

OUTPUT FORMAT
Return exactly these sections:
1. Language:
2. Emergency:
3. Severity:
4. Immediate action:
5. Nearest help:
6. Why:
"""
