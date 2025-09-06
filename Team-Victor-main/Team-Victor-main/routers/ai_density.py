# routers/ai_density.py
from fastapi import APIRouter, HTTPException, Query
from typing import List
from services.ai_density import run_dbscan, fetch_points_from_osm

router = APIRouter()

@router.get("/ai/osm_density")
async def osm_density(
    collections: List[str] = Query(["hospital", "bank", "pharmacy", "restaurant", "petrol station","cafe"]),
    south: float = 6.4,
    west: float = 3.2,
    north: float = 6.7,
    east: float = 3.6,
    radius_km: float = 0.5,
    min_samples: int = 5
):
    bbox = [south, west, north, east]
    points = await fetch_points_from_osm(collections, bbox)
    return run_dbscan(points, radius_km=radius_km, min_samples=min_samples)

    
@router.get("/osm-density-geojson")
async def osm_density_geojson(
    collections: List[str] = Query(["restaurant", "hospital", "pharmacies", "bank", "fuel"]),
    bbox: str = Query(..., description="Bounding box: south,west,north,east")
):
    try:
        bbox_vals = [float(x.strip()) for x in bbox.split(",")]
    except Exception:
        raise ValueError("bbox must be a comma-separated list of 4 numbers")
    
    if len(bbox_vals) != 4:
        raise ValueError("bbox must be exactly 4 numbers: south,west,north,east")

    points = await fetch_points_from_osm(collections, bbox_vals)
    result = run_dbscan(points, radius_km=0.5, min_samples=5)

    return {
        "type": "FeatureCollection",
        "features": [
            {
                "type": "Feature",
                "geometry": {"type": "Point", "coordinates": [p["lon"], p["lat"]]},
                "properties": {"name": p.get("name"), "collection": p["collection"]},
            }
            for p in points
        ],
        "clusters": result,
    }