# DENSITY CALCULATIONS

import numpy as np
from sklearn.cluster import DBSCAN
from typing import List
from models.schemas import BusinessLocation

def calculate_restaurant_density(restaurants: List[BusinessLocation], radius: float) -> float:
    if not restaurants:
        return 0.0
    
        # Simple density calculation: number of restaurants per square kilometer
    area_km2 = (np.pi * (radius / 1000) **2)  # radius in meters to km^2
    density = len(restaurants) / area_km2

    return density
def find_hotspots(businesses: List[BusinessLocation]) -> List[dict]:
    if len(businesses) < 2:
        return []
    
    # Convert to coordinates array
    coords = np.array([[b.lat, b.lng] for b in businesses])
    
    # Cluster analysis
    clustering = DBSCAN(eps=0.01, min_samples=3).fit(coords)
    
    # Return hotspot areas
    hotspots = []
    # Process clusters...
    
    return hotspots

































































































    # if not restaurants:
    #     return 0.0

    # coords = np.array([[r.lat, r.lng] for r in restaurants])
    
    # # DBSCAN parameters
    # kms_per_radian = 6371.0088
    # epsilon = radius / 1000.0 / kms_per_radian  # Convert radius to radians

    # db = DBSCAN(eps=epsilon, min_samples=3, algorithm='ball_tree', metric='haversine').fit(np.radians(coords))
    # labels = db.labels_

    # num_clusters = len(set(labels)) - (1 if -1 in labels else 0)
    # num_noise = list(labels).count(-1)

    # if num_clusters == 0:
    #     return 0.0

    # density_score = num_clusters / (num_clusters + num_noise)
    # return density_score