import httpx
import asyncio
from typing import List, Dict
from fastapi import HTTPException

OVERPASS_SERVERS = [
    "https://overpass.kumi.systems/api/interpreter",
    "https://overpass-api.de/api/interpreter",
    "https://overpass.openstreetmap.ru/api/interpreter"
]

async def fetch_from_overpass(query: str) -> List[Dict]:
    data = None
    async with httpx.AsyncClient() as client:
        for server in OVERPASS_SERVERS:
            try:
                resp = await client.post(server, data={"data": query}, timeout=30.0)
                resp.raise_for_status()
                data = resp.json()
                break
            except Exception:
                continue  # try next server

    if data is None:
        raise HTTPException(status_code=502, detail="All Overpass servers failed")

    points: List[Dict] = []

    for element in data.get("elements", []):
        if "lat" in element and "lon" in element:
            points.append({
                "id": element.get("id"),
                "name": element.get("tags", {}).get("name"),
                "lat": element["lat"],
                "lon": element["lon"],
                "tags": element.get("tags", {})
            })
    return points


