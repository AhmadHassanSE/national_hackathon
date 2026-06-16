"""Custom tools used by Haalat CrewAI agents."""

from __future__ import annotations

import json
import math
import re
from pathlib import Path
from typing import Any

from crewai.tools import tool

try:
    from rag.retriever import retrieve_category_context, retrieve_protocol_context
except ImportError:
    from .rag.retriever import retrieve_category_context, retrieve_protocol_context


PROJECT_ROOT = Path(__file__).resolve().parent
DATA_DIR = PROJECT_ROOT / "data"

KNOWN_LOCATIONS = {
    "garden": (24.8665, 67.0235),
    "garden karachi": (24.8665, 67.0235),
    "garden east": (24.8662, 67.0239),
    "garden west": (24.8648, 67.0207),
    "soldier bazaar": (24.8681, 67.0261),
    "civil hospital": (24.8617, 67.0129),
}

SKILL_KEYWORDS = {
    "cardiac": {"cpr", "aed", "basic_life_support"},
    "heart": {"cpr", "aed", "basic_life_support"},
    "arrest": {"cpr", "aed", "basic_life_support"},
    "dil": {"cpr", "aed", "basic_life_support"},
    "bleeding": {"bleeding_control", "trauma_support", "first_aid"},
    "blood": {"bleeding_control", "trauma_support", "first_aid"},
    "khoon": {"bleeding_control", "trauma_support", "first_aid"},
    "trauma": {"bleeding_control", "trauma_support", "first_aid"},
    "burn": {"burn_care", "first_aid", "triage"},
    "fire": {"burn_care", "first_aid", "triage"},
    "gas": {"triage", "first_aid", "basic_life_support"},
}


def _load_json(path: Path) -> list[dict[str, Any]]:
    try:
        with path.open("r", encoding="utf-8") as file:
            data = json.load(file)
    except FileNotFoundError as exc:
        raise RuntimeError(f"Required data file is missing: {path}") from exc
    except json.JSONDecodeError as exc:
        raise RuntimeError(f"Invalid JSON in data file: {path}") from exc

    if not isinstance(data, list):
        raise RuntimeError(f"Expected a JSON list in {path}")
    return data


def _clean_location(value: str) -> str:
    return re.sub(r"[^a-z0-9 ]+", " ", value.lower()).strip()


def _parse_location(user_location: str) -> tuple[float, float]:
    if not user_location or not user_location.strip():
        raise ValueError("user_location must be a non-empty location string.")

    coordinate_match = re.search(
        r"(-?\d+(?:\.\d+)?)\s*,\s*(-?\d+(?:\.\d+)?)",
        user_location,
    )
    if coordinate_match:
        return float(coordinate_match.group(1)), float(coordinate_match.group(2))

    normalized = _clean_location(user_location)
    if normalized in KNOWN_LOCATIONS:
        return KNOWN_LOCATIONS[normalized]

    for place_name, coordinates in KNOWN_LOCATIONS.items():
        if place_name in normalized:
            return coordinates

    if "karachi" in normalized:
        return KNOWN_LOCATIONS["garden karachi"]

    raise ValueError(
        "Could not resolve location. Use a Garden-area string like 'Garden, Karachi' "
        "or provide coordinates as '24.8665, 67.0235'."
    )


def _haversine_km(
    origin_lat: float,
    origin_lng: float,
    target_lat: float,
    target_lng: float,
) -> float:
    radius_km = 6371.0
    d_lat = math.radians(target_lat - origin_lat)
    d_lng = math.radians(target_lng - origin_lng)
    lat1 = math.radians(origin_lat)
    lat2 = math.radians(target_lat)

    a = (
        math.sin(d_lat / 2) ** 2
        + math.cos(lat1) * math.cos(lat2) * math.sin(d_lng / 2) ** 2
    )
    return radius_km * 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))


def _nearest_record(
    records: list[dict[str, Any]],
    origin: tuple[float, float],
) -> tuple[dict[str, Any], float]:
    if not records:
        raise RuntimeError("No matching records found.")

    lat, lng = origin
    ranked = sorted(
        (
            (
                record,
                _haversine_km(lat, lng, float(record["lat"]), float(record["lng"])),
            )
            for record in records
        ),
        key=lambda item: item[1],
    )
    return ranked[0]


def _skill_terms_for_emergency(emergency_type: str) -> set[str]:
    normalized = _clean_location(emergency_type)
    skills: set[str] = set()
    for keyword, mapped_skills in SKILL_KEYWORDS.items():
        if keyword in normalized:
            skills.update(mapped_skills)
    return skills or {"first_aid", "triage", "basic_life_support"}


def _matching_volunteers(
    volunteers: list[dict[str, Any]],
    emergency_type: str,
) -> list[dict[str, Any]]:
    needed_skills = _skill_terms_for_emergency(emergency_type)
    matches = []

    for volunteer in volunteers:
        volunteer_skills = {str(skill).lower() for skill in volunteer.get("skills", [])}
        if needed_skills.intersection(volunteer_skills):
            matches.append(volunteer)

    return matches or volunteers


def _format_snippets(snippets: list[str]) -> str:
    if not snippets:
        return "No matching RAG context found."
    return "\n\n---\n\n".join(snippet.strip() for snippet in snippets if snippet.strip())


@tool
def emergency_rag_tool(query: str) -> str:
    """Classify an emergency report using Haalat's emergency category RAG collection.

    Use this tool when an agent needs severity, category, keywords, or first-response
    classification context for a user's situation. The input should be the user's raw
    emergency description, including Urdu, Roman Urdu, or English symptoms when present.
    """
    try:
        return _format_snippets(retrieve_category_context(query))
    except Exception as exc:
        return f"Emergency category retrieval failed: {exc}"


@tool
def protocols_rag_tool(query: str) -> str:
    """Retrieve first-aid protocol guidance from Haalat's medical protocol RAG collection.

    Use this tool when an agent needs specific numbered first-aid actions, physical
    response steps, contraindications, or safety cautions for an emergency such as
    cardiac arrest, severe bleeding, burns, trauma, or similar urgent incidents.
    """
    try:
        return _format_snippets(retrieve_protocol_context(query))
    except Exception as exc:
        return f"Emergency protocol retrieval failed: {exc}"


@tool
def location_finder_tool(emergency_type: str, user_location: str) -> str:
    """Find the nearest emergency service and nearest skill-matched volunteer.

    Use this tool when an agent has an emergency type and a user location, and needs a
    concise dispatch-style summary. The location can be a Garden-area phrase such as
    'Garden, Karachi' or coordinates like '24.8665, 67.0235'. The tool reads local
    services and volunteer registries, ranks by distance, matches volunteer skills to
    the emergency type, and returns names, distances, contact numbers, and key skills.
    """
    try:
        origin = _parse_location(user_location)
        services = _load_json(DATA_DIR / "services.json")
        volunteers = _matching_volunteers(
            _load_json(DATA_DIR / "volunteers.json"),
            emergency_type,
        )

        nearest_service, service_distance = _nearest_record(services, origin)
        nearest_volunteer, volunteer_distance = _nearest_record(volunteers, origin)

        volunteer_skills = ", ".join(nearest_volunteer.get("skills", []))
        service_capabilities = ", ".join(nearest_service.get("services", []))

        return (
            f"Nearest service: {nearest_service['name']} "
            f"({nearest_service['type']}, {service_distance:.2f} km away). "
            f"Phone: {nearest_service['phone']}. Services: {service_capabilities}.\n"
            f"Nearest matching volunteer: {nearest_volunteer['name']} "
            f"({volunteer_distance:.2f} km away, area: {nearest_volunteer.get('area', 'unknown')}, "
            f"availability: {nearest_volunteer.get('availability', 'unknown')}). "
            f"Phone: {nearest_volunteer['phone']}. Skills: {volunteer_skills}."
        )
    except Exception as exc:
        return f"Location lookup failed: {exc}"
