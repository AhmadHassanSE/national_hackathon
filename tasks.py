"""CrewAI task definitions for Haalat's sequential emergency workflow."""

from __future__ import annotations

from crewai import Task

from agents import (
    emergency_classifier_agent,
    language_router_agent,
    resource_locator_agent,
)


language_detection_task = Task(
    description=(
        "Inspect the incoming user input: {user_input}\n\n"
        "Decide whether it is plain text or a path to a raw voice file. Treat values "
        "ending in .mp3, .wav, .m4a, .aac, or .ogg as audio paths. If an audio path "
        "is provided, use Gemini's multimodal audio understanding to inspect the "
        "file content directly rather than guessing from the file name.\n\n"
        "Detect the native spoken/source language exactly as one of: Urdu, Sindhi, "
        "Pashto, English, or Mixed/Unknown. State that every downstream task must "
        "preserve this exact language in user-facing output."
    ),
    expected_output=(
        "A single valid JSON block only, with no markdown fences or commentary:\n"
        "{\n"
        '  "detected_language": "Urdu|Sindhi|Pashto|English|Mixed/Unknown",\n'
        '  "input_type": "audio|text"\n'
        "}"
    ),
    agent=language_router_agent,
)


classification_task = Task(
    description=(
        "Using the original user input {user_input} and the language detection "
        "result from the previous task, understand the emergency context while "
        "preserving the user's source language.\n\n"
        "Call emergency_rag_tool with the emergency description to cross-reference "
        "Haalat's category and severity rules. Assign a severity score from 1 to 5, "
        "where 5 means immediately life-threatening. The reasoning must be concise "
        "and written in the user's detected source language."
    ),
    expected_output=(
        "A single valid JSON block only, written in the user's source language for "
        "all natural-language values:\n"
        "{\n"
        '  "type": "classified emergency type",\n'
        '  "severity": 1,\n'
        '  "reasoning": "brief source-language explanation grounded in RAG context"\n'
        "}"
    ),
    agent=emergency_classifier_agent,
    context=[language_detection_task],
)


resource_location_task = Task(
    description=(
        "Use the classified emergency event from the previous task, the user's "
        "location {user_location}, and the detected language from the language "
        "detection task context.\n\n"
        "Call location_finder_tool with the emergency type and user location. Return "
        "the closest emergency service and closest matching volunteer. The final "
        "response must be strictly in the detected source language from context. "
        "If the user wrote Roman Urdu mixed with English, do not convert it into "
        "formal English; answer in simple Roman Urdu with only unavoidable service "
        "names and phone labels kept as-is."
    ),
    expected_output=(
        "A concise final dispatch response strictly in the detected source language. "
        "For Roman Urdu input, write Roman Urdu. "
        "Include the emergency type, severity, nearest service name, service phone, "
        "service distance, nearest matching volunteer name, volunteer phone, and "
        "volunteer distance. Do not include extra analysis."
    ),
    agent=resource_locator_agent,
    context=[language_detection_task, classification_task],
)
