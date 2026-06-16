"""Haalat Sprint 1 execution bridge.

Run this file to verify the Gemini-backed CrewAI pipeline, free local RAG
indexes, and Garden-area resource lookup using the seeded mock data.
"""

from __future__ import annotations

import os
import sys
from pathlib import Path

from crewai import Crew, Process
from dotenv import load_dotenv

from rag.knowledge_base import build_knowledge_base
from rag.prompt_builder import build_gemini_emergency_prompt
from tools import location_finder_tool


PROJECT_ROOT = Path(__file__).resolve().parent


if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")

os.environ.setdefault("PYTHONIOENCODING", "utf-8")


def _input_kind(user_input: str) -> str:
    audio_extensions = {".mp3", ".wav", ".m4a", ".aac", ".ogg"}
    suffix = Path(user_input).suffix.lower()
    return "audio" if suffix in audio_extensions else "text"


def build_crew() -> Crew:
    """Construct Haalat's sequential three-agent emergency crew."""
    from agents import (
        emergency_classifier_agent,
        language_router_agent,
        resource_locator_agent,
    )
    from tasks import (
        classification_task,
        language_detection_task,
        resource_location_task,
    )

    return Crew(
        agents=[
            language_router_agent,
            emergency_classifier_agent,
            resource_locator_agent,
        ],
        tasks=[
            language_detection_task,
            classification_task,
            resource_location_task,
        ],
        process=Process.sequential,
        verbose=False,
    )


def run_demo(
    user_input: str = "mere baap ko dil ka dorah para hai, help me fast - main Garden mein hoon",
    user_location: str = "Garden, Karachi",
) -> object:
    """Run a Sprint 1 demo through local RAG, Gemini routing, and resources."""
    print("\n[Haalat] Sprint 1 Gemini emergency intelligence demo")
    print("[1/5] Loading environment variables from .env...")
    load_dotenv(PROJECT_ROOT / ".env")

    print("[2/5] Ensuring free local RAG indexes are active...")
    build_knowledge_base()

    detected_input_kind = _input_kind(user_input)
    print(f"[3/5] Preparing input bridge. Received {detected_input_kind} input.")
    if detected_input_kind == "audio":
        print(f"      Audio path forwarded for Gemini multimodal handling: {user_input}")
    else:
        print(f"      Text forwarded for language routing: {user_input}")
    print(f"      User location: {user_location}")

    print("[4/5] Building local RAG-grounded Gemini prompt preview...")
    resource_summary = location_finder_tool.run(
        emergency_type="cardiac event",
        user_location=user_location,
    )
    gemini_prompt = build_gemini_emergency_prompt(
        user_input=user_input,
        user_location=user_location,
        resource_summary=resource_summary,
    )
    print("      Local RAG context and resource lookup assembled for Gemini.")
    print("      Prompt preview:")
    print("      " + gemini_prompt[:600].replace("\n", "\n      "))
    print("      ...")

    print("[5/5] Constructing sequential CrewAI crew with Gemini-backed agents...")
    crew = build_crew()

    print("[6/6] Starting crew.kickoff(): language route -> local RAG triage -> resource lookup")
    try:
        result = crew.kickoff(
            inputs={
                "user_input": user_input,
                "user_location": user_location,
            }
        )
    except Exception as exc:
        print("\n[Haalat] Crew execution could not complete.")
        print("Reason:", exc)
        print(
            "The app bridge, RAG collections, agents, tasks, and tool wiring loaded "
            "successfully before the live Gemini generation call failed."
        )
        return None

    print("\n[Haalat] Final output")
    print("-" * 72)
    print(result)
    print("-" * 72)
    return result


if __name__ == "__main__":
    run_demo()
