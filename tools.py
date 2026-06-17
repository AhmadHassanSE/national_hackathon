"""Custom tools used by Haalat CrewAI agents with multi-region support."""

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
    # Karachi
    "garden": (24.8665, 67.0235),
    "garden karachi": (24.8665, 67.0235),
    "garden east": (24.8662, 67.0239),
    "garden west": (24.8648, 67.0207),
    "soldier bazaar": (24.8681, 67.0261),
    "civil hospital": (24.8617, 67.0129),
    "saddar": (24.8550, 67.0050),
    "clifton": (24.8325, 67.0430),
    "gulshan": (24.8770, 67.0412),
    "gulshan-e-iqbal": (24.9100, 67.0900),
    "north nazimabad": (24.9300, 67.0400),
    "pechs": (24.8900, 67.0450),
    "lyari": (24.8800, 66.9800),
    "korangi": (24.8300, 67.1400),
    "malir": (24.9000, 67.2000),
    "dha": (24.8100, 67.0500),
    "federal b area": (24.9200, 67.0550),
    # Islamabad
    "blue area": (33.7167, 73.0587),
    "islamabad": (33.7200, 73.0700),
    "g-8": (33.6933, 73.0586),
    "g-9": (33.6830, 73.0600),
    "f-8": (33.7200, 73.0650),
    "f-7": (33.7240, 73.0720),
    "i-8": (33.7100, 73.0500),
    "h-8": (33.6880, 73.0650),
    "g-10": (33.6720, 73.0700),
    "f-10": (33.6950, 73.0620),
    "e-7": (33.7280, 73.0800),
    "i-10": (33.6980, 73.0420),
    "shifa hospital": (33.7172, 73.0593),
    "pims": (33.6933, 73.0586),
    # Rawalpindi
    "rawalpindi": (33.6010, 73.0510),
    "rawalpindi saddar": (33.6010, 73.0510),
    "rawalpindi cantt": (33.5980, 73.0460),
    "westridge": (33.6080, 73.0380),
    "committee chowk": (33.6120, 73.0420),
    "chandni chowk": (33.6050, 73.0550),
    "satellite town": (33.6180, 73.0600),
    "dhoke choudharian": (33.5960, 73.0480),
    "lalazar": (33.6100, 73.0360),
    "islamabad international airport": (33.5490, 73.1000),
}

REGION_AREAS = {
    "karachi": [
        "Garden", "Saddar", "Clifton", "Gulshan", "Gulshan-e-Iqbal",
        "North Nazimabad", "PECHS", "Lyari", "Korangi", "Malir", "DHA",
        "Federal B Area", "Soldier Bazaar", "Garden East", "Garden West"
    ],
    "islamabad": [
        "Blue Area", "G-8", "G-9", "F-8", "F-7", "F-10", "I-8", "H-8",
        "G-10", "E-7", "I-10"
    ],
    "rawalpindi": [
        "Saddar", "Rawalpindi Cantt", "Westridge", "Committee Chowk",
        "Chandni Chowk", "Satellite Town", "Dhoke Choudharian", "Lalazar"
    ],
}

REGION_CENTERS = {
    "karachi": (24.8600, 67.0100),
    "islamabad": (33.7167, 73.0587),
    "rawalpindi": (33.6010, 73.0510),
}

SKILL_KEYWORDS = {
    "cardiac": {"cpr", "aed", "basic_life_support"},
    "heart": {"cpr", "aed", "basic_life_support"},
    "arrest": {"cpr", "aed", "basic_life_support"},
    "dil": {"cpr", "aed", "basic_life_support"},
    "chest": {"cpr", "aed", "basic_life_support"},
    "bleeding": {"bleeding_control", "trauma_support", "first_aid"},
    "blood": {"bleeding_control", "trauma_support", "first_aid"},
    "khoon": {"bleeding_control", "trauma_support", "first_aid"},
    "trauma": {"bleeding_control", "trauma_support", "first_aid"},
    "burn": {"burn_care", "first_aid", "triage"},
    "fire": {"burn_care", "first_aid", "triage"},
    "gas": {"triage", "first_aid", "basic_life_support"},
    "drowning": {"basic_life_support", "rescue", "cpr"},
    "seizure": {"basic_life_support", "first_aid"},
    "allergic": {"basic_life_support", "cpr"},
    "stroke": {"basic_life_support", "cpr"},
    "childbirth": {"maternity_care", "pediatric_care", "basic_life_support"},
    "unconscious": {"cpr", "aed", "basic_life_support"},
    "behosh": {"cpr", "aed", "basic_life_support"},
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

    # Direct match
    if normalized in KNOWN_LOCATIONS:
        return KNOWN_LOCATIONS[normalized]

    # Substring match
    for place_name, coordinates in KNOWN_LOCATIONS.items():
        if place_name in normalized:
            return coordinates

    # Fallback region centers
    for region_name, coords in REGION_CENTERS.items():
        if region_name in normalized:
            return coords

    raise ValueError(f"Could not resolve location: '{user_location}'. Try a known area.")


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


def get_services_for_region(region: str) -> list[dict[str, Any]]:
    """Get all services matching a region."""
    all_services = _load_json(DATA_DIR / "services.json")
    if region and region != "all":
        region_lower = region.lower()
        return [s for s in all_services if s.get("region", "").lower() == region_lower]
    return all_services


def get_volunteers_for_region(region: str) -> list[dict[str, Any]]:
    """Get all volunteers matching a region."""
    all_volunteers = _load_json(DATA_DIR / "volunteers.json")
    if region and region != "all":
        region_lower = region.lower()
        return [v for v in all_volunteers if v.get("region", "").lower() == region_lower]
    return all_volunteers


def generate_incident_map(
    user_location: str,
    services: list[dict[str, Any]] | None = None,
    volunteers: list[dict[str, Any]] | None = None,
    region: str = "karachi",
    lat: float | None = None,
    lng: float | None = None,
) -> str:
    """Generate an HTML map with Folium showing user position, services, and volunteers."""
    import folium
    from folium import plugins
    from folium.plugins import MarkerCluster

    if lat is not None and lng is not None:
        origin = (lat, lng)
    else:
        try:
            origin = _parse_location(user_location)
        except ValueError:
            center = REGION_CENTERS.get(region, REGION_CENTERS["karachi"])
            origin = center

    center_lat, center_lng = origin

    m = folium.Map(
        location=[center_lat, center_lng],
        zoom_start=14,
        control_scale=True,
        tiles="https://mt1.google.com/vt/lyrs=m&x={x}&y={y}&z={z}&apistyle=s.t%3A0|p.v%3Aoff",
        attr="Haalat | Google Maps",
    )

    # User marker (pulsing red) with Street View link
    streetview_url = f"https://www.google.com/maps?layer=c&cbll={center_lat},{center_lng}"
    folium.Marker(
        [center_lat, center_lng],
        popup=f"""
        <div style="font-family: Inter, sans-serif; min-width: 180px;">
            <b>📍 Your Location</b><br>
            <span style="color: #666; font-size: 11px;">Lat: {center_lat:.4f}, Lng: {center_lng:.4f}</span><br>
            <a href="{streetview_url}" target="_blank" style="color: #ff3333; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 5px;">
                <i class="fa-solid fa-street-view"></i> Open Google Street View ↗
            </a>
        </div>
        """,
        icon=folium.Icon(color="red", icon="info-sign", prefix="glyphicon"),
    ).add_to(m)

    # Accuracy circle
    folium.Circle(
        [center_lat, center_lng],
        radius=500,
        color="red",
        fill=True,
        fillColor="red",
        fillOpacity=0.08,
        weight=1,
    ).add_to(m)

    # Services layer
    if services:
        svc_cluster = MarkerCluster(name="Emergency Services").add_to(m)
        for svc in services:
            svc_lat = svc.get("lat")
            svc_lng = svc.get("lng")
            streetview_url = f"https://www.google.com/maps?layer=c&cbll={svc_lat},{svc_lng}"
            popup_html = f"""
            <div style="font-family: Inter, sans-serif; min-width: 200px;">
                <b style="color: #ff3333;">🏥 {svc.get('name', 'Service')}</b><br>
                <span style="color: #666;">Type: {svc.get('type', 'N/A')}</span><br>
                <span style="color: #666;">📞 {svc.get('phone', 'N/A')}</span><br>
                <span style="color: #666;">📍 {svc.get('area', 'N/A')}</span><br>
                <a href="{streetview_url}" target="_blank" style="color: #ff3333; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 5px;">
                    <i class="fa-solid fa-street-view"></i> Open Street View ↗
                </a>
            </div>
            """
            folium.Marker(
                [svc["lat"], svc["lng"]],
                popup=folium.Popup(popup_html, max_width=300),
                icon=folium.Icon(
                    color="blue" if svc.get("type") == "hospital" else "green",
                    icon="plus" if svc.get("type") == "hospital" else "ambulance",
                    prefix="fa" if svc.get("type") != "hospital" else "glyphicon",
                ),
            ).add_to(svc_cluster)

    # Volunteers layer
    if volunteers:
        vol_cluster = MarkerCluster(name="Volunteers").add_to(m)
        for vol in volunteers:
            status = vol.get("availability", "unknown")
            status_color = "green" if status == "available" else "orange"
            vol_lat = vol.get("lat")
            vol_lng = vol.get("lng")
            streetview_url = f"https://www.google.com/maps?layer=c&cbll={vol_lat},{vol_lng}"
            popup_html = f"""
            <div style="font-family: Inter, sans-serif; min-width: 200px;">
                <b style="color: #00cc66;">👤 {vol.get('name', 'Volunteer')}</b><br>
                <span style="color: #666;">Status: {'✅ Available' if status == 'available' else '⏰ On Call'}</span><br>
                <span style="color: #666;">📞 {vol.get('phone', 'N/A')}</span><br>
                <span style="color: #666;">📍 {vol.get('area', 'N/A')}</span><br>
                <span style="color: #666;">Skills: {', '.join(vol.get('skills', []))}</span><br>
                <a href="{streetview_url}" target="_blank" style="color: #00cc66; text-decoration: none; font-weight: bold; display: inline-block; margin-top: 5px;">
                    <i class="fa-solid fa-street-view"></i> Open Street View ↗
                </a>
            </div>
            """
            folium.Marker(
                [vol["lat"], vol["lng"]],
                popup=folium.Popup(popup_html, max_width=300),
                icon=folium.Icon(color=status_color, icon="user", prefix="fa"),
            ).add_to(vol_cluster)

    # Fullscreen & layer control
    plugins.Fullscreen(position="topright").add_to(m)
    folium.LayerControl().add_to(m)

    return m.get_root()._repr_html_()


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
    response steps, contraindications, or safety cautions for an emergency.
    """
    try:
        return _format_snippets(retrieve_protocol_context(query))
    except Exception as exc:
        return f"Emergency protocol retrieval failed: {exc}"


@tool
def location_finder_tool(emergency_type: str, user_location: str) -> str:
    """Find the nearest emergency service and nearest skill-matched volunteer.
    Use this tool when an agent has an emergency type and a user location, and needs a
    concise dispatch-style summary. The location can be any area in Karachi, Islamabad,
    or Rawalpindi, or coordinates. The tool reads local services and volunteer registries,
    ranks by distance, matches volunteer skills to the emergency type, and returns names,
    distances, contact numbers, and key skills.
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
