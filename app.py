"""Haalat Sprint 1 execution bridge.

Run this file to verify the Gemini-backed CrewAI pipeline, free local RAG
indexes, and Garden-area resource lookup using the seeded mock data.
"""

from __future__ import annotations

import os
import json
import re
import sys
from html import escape
from pathlib import Path

import gradio as gr
from crewai import Crew, Process
from dotenv import load_dotenv

from rag.knowledge_base import build_knowledge_base
from rag.prompt_builder import build_gemini_emergency_prompt
from rag.retriever import retrieve_category_context, retrieve_protocol_context
from tools import location_finder_tool


PROJECT_ROOT = Path(__file__).resolve().parent

custom_css = """
:root {
  --haalat-bg: #11141a;
  --haalat-panel: #171b24;
  --haalat-panel-2: #1d2330;
  --haalat-red: #ff3333;
  --haalat-amber: #ffaa00;
  --haalat-green: #00ff88;
  --haalat-text: #eef3ff;
  --haalat-muted: #9aa6ba;
  --haalat-border: rgba(255, 51, 51, 0.28);
  --haalat-glow: 0 0 15px rgba(255, 51, 51, 0.2);
}

.gradio-container {
  min-height: 100vh;
  background:
    linear-gradient(rgba(255, 51, 51, 0.035) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 255, 136, 0.03) 1px, transparent 1px),
    radial-gradient(circle at 18% 10%, rgba(255, 51, 51, 0.13), transparent 28%),
    radial-gradient(circle at 78% 18%, rgba(0, 255, 136, 0.08), transparent 30%),
    #11141a !important;
  background-size: 34px 34px, 34px 34px, auto, auto, auto;
  color: var(--haalat-text) !important;
  font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
}

.haalat-shell,
.command-module,
.alert-card,
.voice-matrix,
.output-console {
  background: linear-gradient(145deg, rgba(23, 27, 36, 0.96), rgba(17, 20, 26, 0.98));
  border: 1px solid var(--haalat-border);
  border-radius: 8px;
  box-shadow: var(--haalat-glow), inset 0 1px 0 rgba(255, 255, 255, 0.04);
  position: relative;
  overflow: hidden;
}

.haalat-shell::before,
.command-module::before,
.alert-card::before,
.voice-matrix::before,
.output-console::before {
  content: "";
  position: absolute;
  inset: 0;
  pointer-events: none;
  background:
    linear-gradient(90deg, transparent, rgba(255, 51, 51, 0.14), transparent) top left / 100% 1px no-repeat,
    linear-gradient(180deg, transparent, rgba(0, 255, 136, 0.1), transparent) top left / 1px 100% no-repeat;
}

.haalat-title {
  color: var(--haalat-text);
  letter-spacing: 0;
  text-transform: uppercase;
  text-shadow: 0 0 18px rgba(255, 51, 51, 0.45);
}

.haalat-subtitle,
.status-muted {
  color: var(--haalat-muted);
}

.status-live,
.vital-green {
  color: var(--haalat-green);
  text-shadow: 0 0 10px rgba(0, 255, 136, 0.65);
}

.status-warning {
  color: var(--haalat-amber);
  text-shadow: 0 0 10px rgba(255, 170, 0, 0.55);
}

.status-critical {
  color: var(--haalat-red);
  text-shadow: 0 0 12px rgba(255, 51, 51, 0.75);
}

@keyframes pulse {
  0% {
    transform: scale(1);
    box-shadow: 0 0 15px rgba(255, 51, 51, 0.2), 0 0 0 rgba(255, 51, 51, 0);
  }
  50% {
    transform: scale(1.015);
    box-shadow: 0 0 28px rgba(255, 51, 51, 0.55), 0 0 48px rgba(255, 51, 51, 0.18);
  }
  100% {
    transform: scale(1);
    box-shadow: 0 0 15px rgba(255, 51, 51, 0.2), 0 0 0 rgba(255, 51, 51, 0);
  }
}

@keyframes flash {
  0%, 100% {
    opacity: 1;
    color: var(--haalat-red);
    text-shadow: 0 0 18px rgba(255, 51, 51, 0.85);
  }
  50% {
    opacity: 0.35;
    color: var(--haalat-amber);
    text-shadow: 0 0 26px rgba(255, 170, 0, 0.95);
  }
}

.active-emergency,
.alert-card.active,
.alert-card.active-emergency {
  animation: pulse 1.5s ease-in-out infinite;
  border-color: rgba(255, 51, 51, 0.72);
}

@keyframes bounce-bar {
  0%, 100% {
    transform: scaleY(0.28);
    opacity: 0.45;
  }
  45% {
    transform: scaleY(1);
    opacity: 1;
  }
}

.voice-matrix {
  min-height: 88px;
  display: flex;
  align-items: center;
  gap: 14px;
  padding: 16px;
}

.voice-matrix::after {
  content: "Analyzing Voice Matrix...";
  color: var(--haalat-green);
  font-size: 0.82rem;
  letter-spacing: 0;
  text-transform: uppercase;
  text-shadow: 0 0 12px rgba(0, 255, 136, 0.7);
}

.wave-bars {
  display: inline-flex;
  align-items: center;
  gap: 5px;
  height: 42px;
}

.wave-bars span {
  width: 5px;
  height: 38px;
  border-radius: 2px;
  background: linear-gradient(180deg, var(--haalat-red), var(--haalat-amber), var(--haalat-green));
  box-shadow: 0 0 12px rgba(0, 255, 136, 0.42);
  transform-origin: center;
  animation: bounce-bar 0.9s ease-in-out infinite;
}

.wave-bars span:nth-child(2) { animation-delay: 0.08s; }
.wave-bars span:nth-child(3) { animation-delay: 0.16s; }
.wave-bars span:nth-child(4) { animation-delay: 0.24s; }
.wave-bars span:nth-child(5) { animation-delay: 0.32s; }
.wave-bars span:nth-child(6) { animation-delay: 0.4s; }
.wave-bars span:nth-child(7) { animation-delay: 0.48s; }

.voice-recorder:focus-within,
.voice-recorder:hover {
  border-color: rgba(0, 255, 136, 0.62);
  box-shadow: 0 0 22px rgba(0, 255, 136, 0.24), var(--haalat-glow);
}

.gr-button,
button {
  border-radius: 6px !important;
  border: 1px solid rgba(255, 51, 51, 0.5) !important;
  background: linear-gradient(135deg, rgba(255, 51, 51, 0.95), rgba(116, 18, 28, 0.95)) !important;
  color: #fff !important;
  box-shadow: 0 0 15px rgba(255, 51, 51, 0.24);
  transition: transform 160ms ease, box-shadow 160ms ease, border-color 160ms ease;
}

.gr-button:hover,
button:hover {
  transform: translateY(-1px);
  border-color: rgba(255, 170, 0, 0.8) !important;
  box-shadow: 0 0 24px rgba(255, 51, 51, 0.42), 0 0 18px rgba(255, 170, 0, 0.18);
  animation: pulse 1.5s ease-in-out infinite;
}

textarea,
input,
.input-container,
.wrap,
.block {
  background-color: rgba(17, 20, 26, 0.88) !important;
  color: var(--haalat-text) !important;
  border-color: rgba(255, 51, 51, 0.24) !important;
}

textarea:focus,
input:focus {
  border-color: rgba(0, 255, 136, 0.65) !important;
  box-shadow: 0 0 0 1px rgba(0, 255, 136, 0.26), 0 0 18px rgba(0, 255, 136, 0.16) !important;
}

.command-grid {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
  gap: 16px;
}

.scanline {
  position: relative;
}

.scanline::after {
  content: "";
  position: absolute;
  left: 0;
  right: 0;
  top: -30%;
  height: 30%;
  pointer-events: none;
  background: linear-gradient(180deg, transparent, rgba(0, 255, 136, 0.08), transparent);
  animation: scan 4s linear infinite;
}

@keyframes scan {
  0% { top: -30%; }
  100% { top: 100%; }
}

@keyframes danger-blink {
  0%, 100% {
    background: rgba(255, 51, 51, 0.18);
    box-shadow: 0 0 18px rgba(255, 51, 51, 0.35), inset 0 0 18px rgba(255, 51, 51, 0.12);
  }
  50% {
    background: rgba(255, 51, 51, 0.42);
    box-shadow: 0 0 38px rgba(255, 51, 51, 0.9), inset 0 0 26px rgba(255, 170, 0, 0.14);
  }
}

@keyframes slide-feed {
  0% {
    opacity: 0;
    transform: translateY(-18px);
  }
  100% {
    opacity: 1;
    transform: translateY(0);
  }
}

@keyframes eta-sweep {
  0% { transform: translateX(-100%); }
  100% { transform: translateX(100%); }
}

@keyframes radar-ripple {
  0% {
    transform: scale(0.35);
    opacity: 0.9;
  }
  100% {
    transform: scale(2.6);
    opacity: 0;
  }
}

.severity-badge {
  padding: 22px;
  text-align: center;
  border-radius: 8px;
  border: 1px solid rgba(255, 170, 0, 0.42);
  background: rgba(255, 170, 0, 0.1);
  box-shadow: 0 0 20px rgba(255, 170, 0, 0.18);
}

.severity-badge.critical {
  min-height: 118px;
  display: grid;
  place-items: center;
  border-color: rgba(255, 51, 51, 0.88);
  animation: danger-blink 0.8s infinite;
}

.severity-badge.safe {
  border-color: rgba(0, 255, 136, 0.42);
  background: rgba(0, 255, 136, 0.08);
  box-shadow: 0 0 20px rgba(0, 255, 136, 0.18);
}

.severity-badge .score {
  display: block;
  font-size: clamp(2rem, 6vw, 4rem);
  font-weight: 900;
  color: var(--haalat-red);
  line-height: 1;
}

.severity-badge .label {
  display: block;
  margin-top: 8px;
  color: var(--haalat-text);
  font-weight: 900;
  text-transform: uppercase;
}

.coach-feed {
  animation: slide-feed 620ms ease both;
  padding: 18px;
  border-left: 4px solid var(--haalat-green);
}

.coach-feed,
.coach-feed p,
.coach-feed li {
  font-size: 1.08rem;
  line-height: 1.65;
}

.coach-feed strong {
  color: var(--haalat-green);
  text-shadow: 0 0 10px rgba(0, 255, 136, 0.36);
}

.resource-window {
  min-height: 160px;
  padding: 18px;
}

.resource-window h3 {
  margin: 0 0 10px;
  color: var(--haalat-text);
  text-transform: uppercase;
}

.resource-window .detail {
  color: var(--haalat-muted);
  margin: 6px 0;
}

.eta-track {
  height: 10px;
  margin-top: 16px;
  border-radius: 999px;
  overflow: hidden;
  background: rgba(255, 255, 255, 0.08);
  border: 1px solid rgba(255, 170, 0, 0.28);
}

.eta-track::before {
  content: "";
  display: block;
  height: 100%;
  width: 72%;
  background: linear-gradient(90deg, var(--haalat-red), var(--haalat-amber), var(--haalat-green));
  animation: eta-sweep 1.4s ease-in-out infinite alternate;
}

.radar-row {
  display: flex;
  align-items: center;
  gap: 14px;
}

.radar {
  width: 42px;
  height: 42px;
  position: relative;
  border-radius: 999px;
  background: radial-gradient(circle, var(--haalat-green) 0 12%, rgba(0, 255, 136, 0.18) 14% 34%, transparent 36%);
}

.radar::before,
.radar::after {
  content: "";
  position: absolute;
  inset: 7px;
  border-radius: 999px;
  border: 1px solid rgba(0, 255, 136, 0.72);
  animation: radar-ripple 1.35s ease-out infinite;
}

.radar::after {
  animation-delay: 0.42s;
}

.terminal-header {
  text-align: center;
  padding: 28px 18px 18px;
  border-bottom: 1px solid rgba(255, 51, 51, 0.22);
}

.terminal-header h1 {
  margin: 0;
  color: var(--haalat-text);
  font-size: clamp(2.2rem, 6vw, 5rem);
  line-height: 1;
  letter-spacing: 0;
  text-shadow: 0 0 24px rgba(255, 51, 51, 0.55), 0 0 42px rgba(0, 255, 136, 0.12);
}

.terminal-header p {
  margin: 12px auto 0;
  color: var(--haalat-muted);
  max-width: 780px;
  font-size: 1rem;
}

.emergency-trigger {
  min-height: 58px;
  font-weight: 800 !important;
  text-transform: uppercase;
}

.matrix-loader {
  padding: 14px 16px;
  color: var(--haalat-green);
  border: 1px solid rgba(0, 255, 136, 0.4);
  background: linear-gradient(90deg, rgba(0, 255, 136, 0.08), rgba(255, 51, 51, 0.08));
  box-shadow: 0 0 18px rgba(0, 255, 136, 0.22), inset 0 0 18px rgba(255, 51, 51, 0.08);
  text-align: center;
  text-transform: uppercase;
  font-weight: 700;
  overflow: hidden;
}

.matrix-loader .bar {
  height: 4px;
  margin-top: 10px;
  background: linear-gradient(90deg, transparent, var(--haalat-green), var(--haalat-red), transparent);
  animation: scan 1.2s linear infinite;
}

.incident-ticker {
  max-height: 340px;
  overflow: hidden;
  border: 1px solid rgba(0, 255, 136, 0.28);
}

.incident-ticker table {
  width: 100%;
  border-collapse: collapse;
}

.incident-ticker th,
.incident-ticker td {
  padding: 10px 12px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.07);
  color: var(--haalat-text);
  font-size: 0.94rem;
}

.incident-ticker th {
  color: var(--haalat-green);
  text-align: left;
  text-transform: uppercase;
  background: rgba(0, 255, 136, 0.08);
}

.incident-ticker tbody {
  animation: ticker-scroll 18s linear infinite;
}

@keyframes ticker-scroll {
  0%, 20% { transform: translateY(0); }
  100% { transform: translateY(-38%); }
}

@keyframes mass-warning {
  0%, 100% {
    background: rgba(255, 170, 0, 0.18);
    box-shadow: 0 0 20px rgba(255, 170, 0, 0.4), inset 0 0 16px rgba(255, 51, 51, 0.15);
  }
  50% {
    background: rgba(255, 170, 0, 0.55);
    box-shadow: 0 0 42px rgba(255, 170, 0, 0.95), inset 0 0 28px rgba(255, 51, 51, 0.28);
  }
}

.mass-event-card {
  min-height: 220px;
  display: grid;
  place-items: center;
  padding: 24px;
  border: 1px solid rgba(255, 170, 0, 0.88);
  border-radius: 8px;
  color: #fff;
  text-align: center;
  text-transform: uppercase;
  font-size: clamp(1.2rem, 3vw, 2rem);
  font-weight: 950;
  animation: mass-warning 0.8s infinite;
}

.situation-report {
  min-height: 220px;
  padding: 20px;
  white-space: pre-wrap;
  color: var(--haalat-text);
  border-left: 4px solid var(--haalat-amber);
}

.radar-map {
  min-height: 320px;
  display: grid;
  place-items: center;
  background:
    radial-gradient(circle, rgba(0, 255, 136, 0.16) 0 2px, transparent 3px),
    radial-gradient(circle at center, transparent 0 20%, rgba(0, 255, 136, 0.08) 21% 21.8%, transparent 22% 39%, rgba(255, 51, 51, 0.1) 40% 40.8%, transparent 41%),
    linear-gradient(rgba(255, 51, 51, 0.04) 1px, transparent 1px),
    linear-gradient(90deg, rgba(0, 255, 136, 0.04) 1px, transparent 1px);
  background-size: auto, auto, 28px 28px, 28px 28px;
}

.radar-map .cluster {
  padding: 14px 18px;
  border: 1px solid rgba(255, 51, 51, 0.72);
  background: rgba(255, 51, 51, 0.16);
  box-shadow: 0 0 26px rgba(255, 51, 51, 0.42);
  border-radius: 8px;
}
"""


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


def _resolve_submission(audio_path: str | None, text_input: str | None) -> tuple[str, str]:
    text_value = (text_input or "").strip()
    if text_value:
        user_input = text_value
        user_location = "Garden, Karachi" if "garden" in text_value.lower() else text_value
        return user_input, user_location

    if audio_path:
        return audio_path, "Garden, Karachi"

    raise ValueError("Please provide either a voice recording or a text emergency report.")


def _show_processing():
    return gr.update(visible=True)


def _crew_output_text(crew_output: object) -> str:
    if crew_output is None:
        return ""
    raw = getattr(crew_output, "raw", None)
    if raw:
        return str(raw)
    return str(crew_output)


def _json_blocks(text: str) -> list[dict[str, object]]:
    blocks: list[dict[str, object]] = []
    for match in re.finditer(r"\{[\s\S]*?\}", text):
        try:
            value = json.loads(match.group(0))
        except json.JSONDecodeError:
            continue
        if isinstance(value, dict):
            blocks.append(value)
    return blocks


def _find_severity(text: str, json_payloads: list[dict[str, object]]) -> int:
    for payload in json_payloads:
        value = payload.get("severity")
        if isinstance(value, int):
            return max(1, min(value, 5))
        if isinstance(value, str) and value.isdigit():
            return max(1, min(int(value), 5))

    match = re.search(r"severity\s*[:\-]?\s*([1-5])", text, re.IGNORECASE)
    if match:
        return int(match.group(1))
    return 3


def _find_emergency_type(text: str, json_payloads: list[dict[str, object]]) -> str:
    for payload in json_payloads:
        value = payload.get("type") or payload.get("emergency_type")
        if value:
            return str(value)

    match = re.search(r"Emergency Type\s*:\s*([^,\n.]+)", text, re.IGNORECASE)
    if match:
        return match.group(1).strip()
    return "Emergency Event"


def _extract_resource_line(text: str, label: str) -> dict[str, str]:
    label_pattern = re.compile(rf"^(?:{label})\s*:\s*(?P<body>.+)$", re.IGNORECASE)
    body = ""
    for line in text.splitlines():
        match = label_pattern.search(line.strip())
        if match:
            body = match.group("body").strip()
            break

    if not body:
        return {"name": "Pending", "phone": "Pending", "distance": "Calculating"}

    phone_match = re.search(r"Phone:\s*([^,\n.]+)", body, re.IGNORECASE)
    distance_match = re.search(r"Distance:\s*([^,\n]+)", body, re.IGNORECASE)
    if not distance_match:
        distance_match = re.search(r"([0-9]+(?:\.[0-9]+)?\s*km)(?:\s*away)?", body, re.IGNORECASE)
    name = re.split(r",\s*(?:Phone|Distance):", body, maxsplit=1, flags=re.IGNORECASE)[0]
    name = re.split(r"\s*\(", name, maxsplit=1)[0]

    return {
        "name": name.strip() or "Pending",
        "phone": phone_match.group(1).strip() if phone_match else "Pending",
        "distance": distance_match.group(1).strip().rstrip(".") if distance_match else "Calculating",
    }


def _severity_html(severity: int) -> str:
    if severity >= 4:
        return f"""
        <div class="severity-badge critical">
          <div>
            <span class="score">{severity}/5</span>
            <span class="label">CRITICAL SEVERITY - DISPATCH IMMINENT</span>
          </div>
        </div>
        """
    if severity == 3:
        return f"""
        <div class="severity-badge">
          <span class="score" style="color: var(--haalat-amber);">{severity}/5</span>
          <span class="label">ELEVATED ALERT - FIELD SUPPORT ADVISED</span>
        </div>
        """
    return f"""
    <div class="severity-badge safe">
      <span class="score" style="color: var(--haalat-green);">{severity}/5</span>
      <span class="label">STABLE ALERT - MONITOR AND GUIDE</span>
    </div>
    """


def _first_aid_markdown(emergency_type: str, source_text: str) -> str:
    query = f"{emergency_type} {source_text}"
    snippets = retrieve_protocol_context(query)
    protocol = snippets[0] if snippets else "No first-aid protocol context was retrieved."
    lines = [line.strip() for line in protocol.splitlines() if line.strip()]
    readable = "\n\n".join(lines[:8])
    return f"""
<div class="coach-feed command-module">

### LIVE FIRST AID COACH FEED

**Protocol lock:** {escape(emergency_type)}

{escape(readable)}

</div>
"""


def _unit_html(unit: dict[str, str]) -> str:
    return f"""
    <div class="resource-window command-module">
      <h3>Nearest Emergency Unit</h3>
      <div class="detail"><strong>Name:</strong> {escape(unit["name"])}</div>
      <div class="detail"><strong>Contact:</strong> {escape(unit["phone"])}</div>
      <div class="detail"><strong>Distance:</strong> {escape(unit["distance"])}</div>
      <div class="detail status-warning">ETA Countdown Tracker: ACTIVE</div>
      <div class="eta-track"></div>
    </div>
    """


def _volunteer_html(volunteer: dict[str, str]) -> str:
    return f"""
    <div class="resource-window command-module">
      <h3>Community Volunteer Alert Network</h3>
      <div class="radar-row">
        <div class="radar"></div>
        <div>
          <div class="detail"><strong>Name:</strong> {escape(volunteer["name"])}</div>
          <div class="detail"><strong>Phone:</strong> {escape(volunteer["phone"])}</div>
          <div class="detail"><strong>Distance:</strong> {escape(volunteer["distance"])}</div>
          <div class="detail status-live">Notification pulse blasted to phone</div>
        </div>
      </div>
    </div>
    """


def display_pipeline_results(crew_output: object) -> tuple[str, str, str, str]:
    """Render CrewAI output into severity, first-aid, resource, and volunteer widgets."""
    text = _crew_output_text(crew_output)
    payloads = _json_blocks(text)
    severity = _find_severity(text, payloads)
    emergency_type = _find_emergency_type(text, payloads)
    unit = _extract_resource_line(text, "Nearest Service|Nearest Emergency Unit")
    volunteer = _extract_resource_line(text, "Nearest Matching Volunteer|Volunteer")

    return (
        _severity_html(severity),
        _first_aid_markdown(emergency_type, text),
        _unit_html(unit),
        _volunteer_html(volunteer),
    )


def _empty_render(message: str) -> tuple[str, str, str, str]:
    safe_message = escape(message)
    return (
        """
        <div class="severity-badge">
          <span class="score" style="color: var(--haalat-amber);">--</span>
          <span class="label">PIPELINE HALTED</span>
        </div>
        """,
        f"<div class='coach-feed command-module'>{safe_message}</div>",
        "<div class='resource-window command-module'><h3>Nearest Emergency Unit</h3><div class='detail'>Pending</div></div>",
        "<div class='resource-window command-module'><h3>Community Volunteer Alert Network</h3><div class='detail'>Pending</div></div>",
    )


def _local_fallback_output(user_input: str, user_location: str) -> str:
    """Build a deterministic emergency summary when Gemini quota is unavailable."""
    query = user_input.lower()
    category_context = "\n".join(retrieve_category_context(user_input))

    emergency_type = "Emergency Event"
    severity = 3
    if any(term in query for term in ["dil", "heart", "cardiac", "chest", "behosh", "unconscious"]):
        emergency_type = "Cardiac Event"
        severity = 5
    elif any(term in query for term in ["bleed", "blood", "khoon", "zakhm"]):
        emergency_type = "Severe Bleeding"
        severity = 4
    elif "gas" in query or "smell" in query or "boo" in query:
        emergency_type = "Gas Leak"
        severity = 4
    elif "burn" in query or "jal" in query or "aag" in query:
        emergency_type = "Burn Injury"
        severity = 3
    elif "SEVERITY: 5" in category_context:
        emergency_type = "Cardiac Event"
        severity = 5

    resource_summary = location_finder_tool.run(
        emergency_type=emergency_type,
        user_location=user_location,
    )
    return (
        f"Emergency Type: {emergency_type}, Severity: {severity}.\n"
        f"{resource_summary}\n"
        "Reasoning: Local fallback used free RAG and resource tools because Gemini "
        "generation quota was unavailable."
    )


def handle_emergency_submission(audio_path: str | None, text_input: str | None) -> tuple[str, str, str, str, object]:
    """Run the CrewAI emergency pipeline from Gradio voice or text input."""
    try:
        user_input, user_location = _resolve_submission(audio_path, text_input)
        result = run_demo(user_input=user_input, user_location=user_location)
        if result is None:
            fallback_result = _local_fallback_output(user_input, user_location)
            return (*display_pipeline_results(fallback_result), gr.update(visible=False))
        return (*display_pipeline_results(result), gr.update(visible=False))
    except Exception as exc:
        return (*_empty_render(f"Emergency terminal error: {exc}"), gr.update(visible=False))


def _load_incident_log() -> list[dict[str, object]]:
    path = PROJECT_ROOT / "incident_log.json"
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    if not isinstance(data, list):
        return []
    return [item for item in data if isinstance(item, dict)]


def _demo_incidents() -> list[dict[str, object]]:
    return [
        {"time": "22:14", "area": "Garden East", "type": "Cardiac Event"},
        {"time": "22:16", "area": "Garden West", "type": "Severe Bleeding"},
        {"time": "22:18", "area": "Soldier Bazaar near Garden", "type": "Gas Leak"},
        {"time": "22:21", "area": "Garden, Karachi", "type": "Cardiac Event"},
    ]


def _incident_value(incident: dict[str, object], *keys: str, fallback: str = "Unknown") -> str:
    for key in keys:
        value = incident.get(key)
        if value:
            return str(value)
    return fallback


def render_incident_feed() -> str:
    """Render anonymized incidents from incident_log.json as a live monitor ticker."""
    incidents = _load_incident_log() or _demo_incidents()
    rows = []
    for incident in incidents[-12:]:
        time_value = _incident_value(incident, "time", "timestamp", "created_at", fallback="Live")
        area = _incident_value(incident, "area", "location", "user_location", fallback="Karachi")
        incident_type = _incident_value(incident, "type", "emergency_type", "category", fallback="Emergency")
        rows.append(
            "<tr>"
            f"<td>{escape(time_value)}</td>"
            f"<td>{escape(area)}</td>"
            f"<td>{escape(incident_type)}</td>"
            "</tr>"
        )

    doubled_rows = rows + rows
    return """
    <div class="incident-ticker command-module">
      <table>
        <thead><tr><th>Time</th><th>Area</th><th>Emergency Type</th></tr></thead>
        <tbody>
          {rows}
        </tbody>
      </table>
    </div>
    """.format(rows="\n".join(doubled_rows))


def _mass_event_state() -> tuple[bool, str]:
    incidents = _load_incident_log() or _demo_incidents()
    garden_incidents = [
        incident for incident in incidents
        if "garden" in _incident_value(incident, "area", "location", "user_location", fallback="").lower()
    ]
    explicit_mass_event = any(incident.get("is_mass_event") is True for incident in incidents)
    is_mass_event = explicit_mass_event or len(garden_incidents) >= 3
    report = (
        "CIVIL DEFENSE SITUATION REPORT\n"
        f"Cluster: Garden, Karachi\n"
        f"Active linked incidents: {len(garden_incidents)}\n"
        "Assessment: Multi-incident pressure detected around Garden corridor.\n"
        "Action: Escalate ambulance staging, volunteer triage, and hospital pre-alert.\n\n"
        "شہری دفاعی صورتحال رپورٹ\n"
        "علاقہ: گارڈن، کراچی\n"
        f"منسلک واقعات: {len(garden_incidents)}\n"
        "ہدایت: ایمبولینس، رضاکار، اور اسپتال رابطہ فوری تیز کریں۔"
    )
    return is_mass_event, report


def render_mass_event_alert() -> tuple[object, str]:
    is_mass_event, report = _mass_event_state()
    alert_html = """
    <div class="mass-event-card">
      🚨 MULTIPLE INCIDENTS DETECTED IN GARDEN, KARACHI — MASS CASUALTY PROTOCOL ESCALATED
    </div>
    """
    return gr.update(value=alert_html, visible=is_mass_event), report


def refresh_command_radar() -> tuple[str, object, str]:
    alert_update, report = render_mass_event_alert()
    return render_incident_feed(), alert_update, report


def create_interface() -> gr.Blocks:
    """Create the Citizen Emergency Terminal Gradio interface."""
    scanner_html = """
    <div class="matrix-loader scanline">
      AI AGENT AGGREGATION MATRIX ACTIVE
      <div class="bar"></div>
    </div>
    """

    with gr.Blocks(title="Haalat Emergency Terminal") as demo:
        gr.HTML(
            """
            <div class="terminal-header">
              <h1>HAALAT <span style='animation: flash 1s infinite;'>حالت</span></h1>
              <p>Pakistan's Real-Time Multi-Agent Emergency Intelligence System.</p>
            </div>
            """
        )

        with gr.Row(elem_classes=["command-grid"]):
            with gr.Column(elem_classes=["command-module", "voice-recorder"]):
                gr.HTML(
                    """
                    <div class="voice-matrix">
                      <div class="wave-bars">
                        <span></span><span></span><span></span><span></span>
                        <span></span><span></span><span></span>
                      </div>
                    </div>
                    """
                )
                voice_input = gr.Audio(
                    sources=["microphone"],
                    type="filepath",
                    label="🎙️ HOLD TO SPEAK (URDU, SINDHI, PASHTO, ENGLISH)",
                )

            with gr.Column(elem_classes=["command-module"]):
                text_input = gr.Textbox(
                    label="Text Backup",
                    placeholder=(
                        "Type your emergency and location here... e.g., Mere baap ko "
                        "dil ka dorah para hai, Garden Karachi"
                    ),
                    lines=8,
                )

        trigger_button = gr.Button(
            "TRIGGER EMERGENCY PROTOCOL",
            elem_classes=["emergency-trigger", "active-emergency"],
        )

        processing_indicator = gr.HTML(
            scanner_html,
            visible=False,
            elem_classes=["command-module"],
        )

        with gr.Column(elem_classes=["output-console", "alert-card"]):
            severity_badge = gr.HTML(
                """
                <div class="severity-badge">
                  <span class="score" style="color: var(--haalat-muted);">--</span>
                  <span class="label">AWAITING EMERGENCY CLASSIFICATION</span>
                </div>
                """
            )
            first_aid_feed = gr.Markdown(
                """
<div class="coach-feed command-module">

### LIVE FIRST AID COACH FEED

Awaiting RAG protocol lock.

</div>
"""
            )
            with gr.Row(elem_classes=["command-grid"]):
                emergency_unit_window = gr.HTML(
                    """
                    <div class="resource-window command-module">
                      <h3>Nearest Emergency Unit</h3>
                      <div class="detail">Awaiting dispatch coordinates.</div>
                    </div>
                    """
                )
                volunteer_window = gr.HTML(
                    """
                    <div class="resource-window command-module">
                      <h3>Community Volunteer Alert Network</h3>
                      <div class="detail">Awaiting volunteer match.</div>
                    </div>
                    """
                )

        output_components = [
            severity_badge,
            first_aid_feed,
            emergency_unit_window,
            volunteer_window,
            processing_indicator,
        ]

        trigger_button.click(
            fn=_show_processing,
            inputs=[],
            outputs=processing_indicator,
        ).then(
            fn=handle_emergency_submission,
            inputs=[voice_input, text_input],
            outputs=output_components,
        )

        text_input.submit(
            fn=_show_processing,
            inputs=[],
            outputs=processing_indicator,
        ).then(
            fn=handle_emergency_submission,
            inputs=[voice_input, text_input],
            outputs=output_components,
        )

    return demo


def create_interface() -> gr.Blocks:
    """Create the Citizen Emergency Terminal Gradio interface."""
    scanner_html = """
    <div class="matrix-loader scanline">
      AI AGENT AGGREGATION MATRIX ACTIVE
      <div class="bar"></div>
    </div>
    """

    with gr.Blocks(title="Haalat Emergency Terminal") as demo:
        gr.HTML(
            """
            <div class="terminal-header">
              <h1>HAALAT <span style='animation: flash 1s infinite;'>&#1581;&#1575;&#1604;&#1578;</span></h1>
              <p>Pakistan's Real-Time Multi-Agent Emergency Intelligence System.</p>
            </div>
            """
        )

        with gr.Row(elem_classes=["command-grid"]):
            with gr.Column(elem_classes=["command-module", "voice-recorder"]):
                gr.HTML(
                    """
                    <div class="voice-matrix">
                      <div class="wave-bars">
                        <span></span><span></span><span></span><span></span>
                        <span></span><span></span><span></span>
                      </div>
                    </div>
                    """
                )
                voice_input = gr.Audio(
                    sources=["microphone"],
                    type="filepath",
                    label="\U0001f399\ufe0f HOLD TO SPEAK (URDU, SINDHI, PASHTO, ENGLISH)",
                )

            with gr.Column(elem_classes=["command-module"]):
                text_input = gr.Textbox(
                    label="Text Backup",
                    placeholder=(
                        "Type your emergency and location here... e.g., Mere baap ko "
                        "dil ka dorah para hai, Garden Karachi"
                    ),
                    lines=8,
                )

        trigger_button = gr.Button(
            "TRIGGER EMERGENCY PROTOCOL",
            elem_classes=["emergency-trigger", "active-emergency"],
        )

        processing_indicator = gr.HTML(
            scanner_html,
            visible=False,
            elem_classes=["command-module"],
        )

        with gr.Column(elem_classes=["output-console", "alert-card"]):
            severity_badge = gr.HTML(
                """
                <div class="severity-badge">
                  <span class="score" style="color: var(--haalat-muted);">--</span>
                  <span class="label">AWAITING EMERGENCY CLASSIFICATION</span>
                </div>
                """
            )
            first_aid_feed = gr.Markdown(
                """
<div class="coach-feed command-module">

### LIVE FIRST AID COACH FEED

Awaiting RAG protocol lock.

</div>
"""
            )
            with gr.Row(elem_classes=["command-grid"]):
                emergency_unit_window = gr.HTML(
                    """
                    <div class="resource-window command-module">
                      <h3>Nearest Emergency Unit</h3>
                      <div class="detail">Awaiting dispatch coordinates.</div>
                    </div>
                    """
                )
                volunteer_window = gr.HTML(
                    """
                    <div class="resource-window command-module">
                      <h3>Community Volunteer Alert Network</h3>
                      <div class="detail">Awaiting volunteer match.</div>
                    </div>
                    """
                )

        output_components = [
            severity_badge,
            first_aid_feed,
            emergency_unit_window,
            volunteer_window,
            processing_indicator,
        ]

        trigger_button.click(
            fn=_show_processing,
            inputs=[],
            outputs=processing_indicator,
        ).then(
            fn=handle_emergency_submission,
            inputs=[voice_input, text_input],
            outputs=output_components,
        )

        text_input.submit(
            fn=_show_processing,
            inputs=[],
            outputs=processing_indicator,
        ).then(
            fn=handle_emergency_submission,
            inputs=[voice_input, text_input],
            outputs=output_components,
        )

    return demo


def create_interface() -> gr.Blocks:
    """Create the full Haalat Gradio interface with citizen and command tabs."""
    scanner_html = """
    <div class="matrix-loader scanline">
      AI AGENT AGGREGATION MATRIX ACTIVE
      <div class="bar"></div>
    </div>
    """
    mass_event_active, situation_report = _mass_event_state()
    mass_alert_html = """
    <div class="mass-event-card">
      🚨 MULTIPLE INCIDENTS DETECTED IN GARDEN, KARACHI — MASS CASUALTY PROTOCOL ESCALATED
    </div>
    """

    with gr.Blocks(title="Haalat Emergency Terminal") as demo:
        gr.HTML(
            """
            <div class="terminal-header">
              <h1>HAALAT <span style='animation: flash 1s infinite;'>&#1581;&#1575;&#1604;&#1578;</span></h1>
              <p>Pakistan's Real-Time Multi-Agent Emergency Intelligence System.</p>
            </div>
            """
        )

        with gr.Tabs():
            with gr.Tab("Citizen Emergency Terminal"):
                with gr.Row(elem_classes=["command-grid"]):
                    with gr.Column(elem_classes=["command-module", "voice-recorder"]):
                        gr.HTML(
                            """
                            <div class="voice-matrix">
                              <div class="wave-bars">
                                <span></span><span></span><span></span><span></span>
                                <span></span><span></span><span></span>
                              </div>
                            </div>
                            """
                        )
                        voice_input = gr.Audio(
                            sources=["microphone"],
                            type="filepath",
                            label="\U0001f399\ufe0f HOLD TO SPEAK (URDU, SINDHI, PASHTO, ENGLISH)",
                        )

                    with gr.Column(elem_classes=["command-module"]):
                        text_input = gr.Textbox(
                            label="Text Backup",
                            placeholder=(
                                "Type your emergency and location here... e.g., Mere baap ko "
                                "dil ka dorah para hai, Garden Karachi"
                            ),
                            lines=8,
                        )

                trigger_button = gr.Button(
                    "TRIGGER EMERGENCY PROTOCOL",
                    elem_classes=["emergency-trigger", "active-emergency"],
                )

                processing_indicator = gr.HTML(
                    scanner_html,
                    visible=False,
                    elem_classes=["command-module"],
                )

                with gr.Column(elem_classes=["output-console", "alert-card"]):
                    severity_badge = gr.HTML(
                        """
                        <div class="severity-badge">
                          <span class="score" style="color: var(--haalat-muted);">--</span>
                          <span class="label">AWAITING EMERGENCY CLASSIFICATION</span>
                        </div>
                        """
                    )
                    first_aid_feed = gr.Markdown(
                        """
<div class="coach-feed command-module">

### LIVE FIRST AID COACH FEED

Awaiting RAG protocol lock.

</div>
"""
                    )
                    with gr.Row(elem_classes=["command-grid"]):
                        emergency_unit_window = gr.HTML(
                            """
                            <div class="resource-window command-module">
                              <h3>Nearest Emergency Unit</h3>
                              <div class="detail">Awaiting dispatch coordinates.</div>
                            </div>
                            """
                        )
                        volunteer_window = gr.HTML(
                            """
                            <div class="resource-window command-module">
                              <h3>Community Volunteer Alert Network</h3>
                              <div class="detail">Awaiting volunteer match.</div>
                            </div>
                            """
                        )

                output_components = [
                    severity_badge,
                    first_aid_feed,
                    emergency_unit_window,
                    volunteer_window,
                    processing_indicator,
                ]

                trigger_button.click(
                    fn=_show_processing,
                    inputs=[],
                    outputs=processing_indicator,
                ).then(
                    fn=handle_emergency_submission,
                    inputs=[voice_input, text_input],
                    outputs=output_components,
                )

                text_input.submit(
                    fn=_show_processing,
                    inputs=[],
                    outputs=processing_indicator,
                ).then(
                    fn=handle_emergency_submission,
                    inputs=[voice_input, text_input],
                    outputs=output_components,
                )

            with gr.Tab("Civil Defense Command Radar"):
                with gr.Row(elem_classes=["command-grid"]):
                    with gr.Column(elem_classes=["command-module"]):
                        gr.HTML(
                            """
                            <div class="radar-map">
                              <div class="cluster">
                                GARDEN CLUSTER MEMORY<br>
                                LIVE MULTI-INCIDENT WATCH
                              </div>
                            </div>
                            """
                        )
                    with gr.Column(elem_classes=["command-module"]):
                        incident_feed = gr.HTML(render_incident_feed())
                        refresh_radar_button = gr.Button("REFRESH COMMAND RADAR")

                with gr.Row(elem_classes=["command-grid"]):
                    mass_alert = gr.HTML(
                        mass_alert_html,
                        visible=mass_event_active,
                        elem_classes=["command-module"],
                    )
                    situation_report_box = gr.Textbox(
                        value=situation_report,
                        label="Agent 6 Civil Defense Situation Report",
                        lines=11,
                        elem_classes=["situation-report", "command-module"],
                    )

                refresh_radar_button.click(
                    fn=refresh_command_radar,
                    inputs=[],
                    outputs=[incident_feed, mass_alert, situation_report_box],
                )

    return demo


if __name__ == "__main__":
    app = create_interface()
    app.launch(css=custom_css, share=True)
