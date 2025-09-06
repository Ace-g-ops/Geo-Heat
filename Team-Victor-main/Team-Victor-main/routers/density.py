from fastapi import APIRouter
from database import db
import numpy as np
from sklearn.cluster import KMeans

router = APIRouter()

@router.get("/density-analysis")
async def density_analysis():
    # Fetch store data from MongoDB
    stores = await db["stores"].find().to_list(1000)

    if not stores:
        return {"message": "No stores found in database."}

    # Convert to numpy array for clustering
    coords = np.array([[s["lat"], s["lng"]] for s in stores])

    # Apply KMeans clustering
    kmeans = KMeans(n_clusters=3, random_state=42).fit(coords)
    labels = kmeans.labels_

    # Count density per cluster
    cluster_counts = {}
    for label in labels:
        cluster_counts[label] = cluster_counts.get(label, 0) + 1

    return {
        "total_stores": len(stores),
        "cluster_density": cluster_counts,
        "centroids": kmeans.cluster_centers_.tolist()
    }
