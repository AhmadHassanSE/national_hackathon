"""CrewAI agent definitions for the Haalat emergency intelligence workflow."""

from __future__ import annotations

import os
from pathlib import Path

from crewai import Agent, LLM
from dotenv import load_dotenv
from google import genai
from langchain_google_genai import ChatGoogleGenerativeAI

from tools import emergency_rag_tool, location_finder_tool


PROJECT_ROOT = Path(__file__).resolve().parent
REQUESTED_GEMINI_MODEL = "gemini-2.5-flash"
FALLBACK_GEMINI_MODEL = "gemini-2.0-flash"


def _gemini_api_key() -> str:
    load_dotenv(PROJECT_ROOT / ".env")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        raise RuntimeError(
            "GEMINI_API_KEY is missing. Add your Gemini API key to haalat/.env "
            "before running the CrewAI agents."
        )
    return api_key


def _normalize_model_name(model_name: str) -> str:
    return model_name.removeprefix("models/")


def _resolve_gemini_model() -> str:
    preferred_model = os.getenv("HAALAT_GEMINI_MODEL", REQUESTED_GEMINI_MODEL)
    preferred_model = _normalize_model_name(preferred_model)
    api_key = _gemini_api_key()

    try:
        client = genai.Client(api_key=api_key)
        available_models = {
            _normalize_model_name(model.name)
            for model in client.models.list()
            if "generateContent" in str(getattr(model, "supported_actions", []))
        }
    except Exception:
        return preferred_model

    if preferred_model in available_models:
        return preferred_model

    print(
        f"[Haalat] Gemini model '{preferred_model}' is unavailable for this API key; "
        f"using '{FALLBACK_GEMINI_MODEL}' instead."
    )
    return FALLBACK_GEMINI_MODEL


GEMINI_MODEL = _resolve_gemini_model()


def _gemini_chat_model() -> ChatGoogleGenerativeAI:
    """Create a LangChain Gemini chat model for direct multimodal use paths."""
    return ChatGoogleGenerativeAI(
        model=GEMINI_MODEL,
        google_api_key=_gemini_api_key(),
        temperature=0.1,
    )


def _crewai_gemini_llm() -> LLM:
    """Create the CrewAI-compatible Gemini Flash LLM used by Agents."""
    api_key = _gemini_api_key()
    return LLM(
        model=f"gemini/{GEMINI_MODEL}",
        api_key=api_key,
        temperature=0.1,
    )


gemini_chat_model = _gemini_chat_model()
llm = _crewai_gemini_llm()


language_router_agent = Agent(
    role="South Asian Emergency Language Router",
    goal=(
        "Identify whether the incoming Haalat report is text or a raw audio file, "
        "detect the user's source language, and ensure every downstream step "
        "preserves that exact language."
    ),
    backstory=(
        "You are a language and dialect specialist for Pakistan emergency response. "
        "You recognize Urdu, Sindhi, Pashto, English, and mixed Roman Urdu phrases. "
        "When given a path to an .mp3 or .wav file, you use Gemini's multimodal "
        "capabilities to inspect the spoken content directly. You never force a "
        "translation unless it is needed internally, and you clearly instruct the "
        "crew to answer in the user's original language."
    ),
    llm=llm,
    allow_delegation=False,
    verbose=False,
    multimodal=True,
    max_retry_limit=0,
)


emergency_classifier_agent = Agent(
    role="Emergency Triage Paramedic",
    goal=(
        "Analyze the user's emergency report, cross-reference Haalat's emergency "
        "category knowledge base, and assign a clear severity score from 1 to 5."
    ),
    backstory=(
        "You are a calm triage paramedic trained for Karachi field conditions. "
        "You use the emergency category RAG tool to ground your classification in "
        "Haalat's local severity rules, including Urdu and English emergency terms. "
        "Your output stays in the user's detected source language."
    ),
    tools=[emergency_rag_tool],
    llm=llm,
    allow_delegation=False,
    verbose=False,
    max_retry_limit=0,
)


resource_locator_agent = Agent(
    role="Field Asset Coordinator",
    goal=(
        "Find the closest relevant emergency service and skill-matched volunteer "
        "for the parsed incident and user location."
    ),
    backstory=(
        "You coordinate rescue assets around Karachi using local service and "
        "registered volunteer data. You call the location finder tool only after "
        "the emergency type and user location are clear, then format a concise "
        "dispatch-ready response in the user's detected language."
    ),
    tools=[location_finder_tool],
    llm=llm,
    allow_delegation=False,
    verbose=False,
    max_retry_limit=0,
)
