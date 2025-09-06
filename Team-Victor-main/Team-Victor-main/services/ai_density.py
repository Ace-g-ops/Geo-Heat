# services/ai_density.py
from typing import List, Dict, Any
import numpy as np
from sklearn.cluster import DBSCAN
from database import db
from utils.geo import EARTH_RADIUS_KM
import asyncio
from services.overpass import fetch_from_overpass

# keys your collections might use for coordinates
CANDIDATE_KEYS = [
    ("lat", "lng"),
    ("latitude", "longitude"),
    ("lat", "lon"),
] 

async def _load_points(collection: str, limit: int = 50000) -> List[Dict[str, Any]]:
    # fetch only the needed fields
    cursor = db[collection].find(
        {},
        {"_id": 1, "name": 1, "lat": 1, "lng": 1, "latitude": 1, "longitude": 1, "lon": 1},
    )
    docs = await cursor.to_list(length=limit)

    points: List[Dict[str, Any]] = []
    for d in docs:
        lat = lon = None
        for la_key, lo_key in CANDIDATE_KEYS:
            if la_key in d and lo_key in d:
                lat, lon = d[la_key], d[lo_key]
                break
        if lat is None or lon is None:
            continue
        points.append({
            "_id": str(d["_id"]),
            "name": d.get("name"),
            "lat": float(lat),
            "lon": float(lon),
            "collection": collection,
        })
    return points

async def fetch_points_from_osm(collections: List[str], bbox: List[float]):
    # bbox expected as [south, west, north, east]
    if not bbox or len(bbox) != 4:
        raise ValueError("bbox must be a sequence of four floats: [south, west, north, east]")
    south, west, north, east = map(float, bbox)

    queries = []
    for c in collections:
        queries.append(f"""
        [out:json][timeout:25];
        node["amenity"="{c}"]({south},{west},{north},{east});
        out body;
        """)

    results = await asyncio.gather(*[fetch_from_overpass(q) for q in queries])

    points = []
    for chunk, c in zip(results, collections):

            for el in chunk:
                points.append({
                "_id": str(el.get("id")),
                "name": el.get("tags", {}).get("name", f"Unnamed {c}"),
                "lat": float(el["lat"]),
                "lon": float(el["lon"]),
                "collection": c
            })
    return points




    # results = await asyncio.gather(*[_load_points(c) for c in collections])
    # return [p for chunk in results for p in chunk]

def run_dbscan(points: List[Dict[str, Any]], radius_km: float, min_samples: int) -> Dict[str, Any]:
  
    if not points:
        return {"clusters": [], "noise": [], "summary": {"n_points": 0, "n_clusters": 0}}

    coords = np.array([[p["lat"], p["lon"]] for p in points], dtype=float)

    # DBSCAN with haversine expects radians + eps in radians
    coords_rad = np.radians(coords)
    eps = radius_km / EARTH_RADIUS_KM

    db = DBSCAN(eps=eps, min_samples=min_samples, metric="haversine").fit(coords_rad)
    labels = db.labels_

    # Building clusters
    clusters = []
    unique_labels = set(labels)
    n_clusters = len(unique_labels) - (1 if -1 in unique_labels else 0)

    for lbl in unique_labels:
        idxs = np.where(labels == lbl)[0]
        members = [points[i] for i in idxs]

        if lbl == -1:  # noise
            noise = members
            continue

        arr = coords[idxs]
        centroid = {"lat": float(arr[:, 0].mean()), "lon": float(arr[:, 1].mean())}
        clusters.append({
            "cluster_id": int(lbl),
            "count": len(members),
            "centroid": centroid,
            "members": members,  # remove if response too large
        })

    clusters.sort(key=lambda c: c["count"], reverse=True)
    return {
        "clusters": clusters,
        "noise": noise if 'noise' in locals() else [],
        "summary": {"n_points": len(points), "n_clusters": n_clusters},
    }




def clusters_to_geojson(clusters: list, noise: list = []) -> dict:
    """
    Convert DBSCAN clusters into GeoJSON FeatureCollection
    """
    features = []

    # Add clusters
    for cluster in clusters:
        # Centroid as a point
        features.append({
            "type": "Feature",
            "properties": {
                "cluster_id": cluster["cluster_id"],
                "count": cluster["count"],
                "type": "cluster"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [cluster["centroid"]["lon"], cluster["centroid"]["lat"]]
            }
        })

        # Members as points
        for member in cluster["members"]:
            features.append({
                "type": "Feature",
                "properties": {
                    "cluster_id": cluster["cluster_id"],
                    "name": member.get("name"),
                    "collection": member.get("collection"),
                    "type": "store"
                },
                "geometry": {
                    "type": "Point",
                    "coordinates": [member["lon"], member["lat"]]
                }
            })

    # Add noise points
    for n in noise:
        features.append({
            "type": "Feature",
            "properties": {
                "cluster_id": -1,
                "name": n.get("name"),
                "collection": n.get("collection"),
                "type": "noise"
            },
            "geometry": {
                "type": "Point",
                "coordinates": [n["lon"], n["lat"]]
            }
        })

    return {
        "type": "FeatureCollection",
        "features": features
    }
