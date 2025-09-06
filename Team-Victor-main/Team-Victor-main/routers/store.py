from fastapi import APIRouter, HTTPException, Query

router = APIRouter()

# Dummy dataset for now (later you can link it to MongoDB)
stores_data = [
    {"id": 1, "name": "Shop A", "location": "Ikeja"},
    {"id": 2, "name": "Shop B", "location": "Ikeja"},
    {"id": 3, "name": "Shop C", "location": "Yaba"},
    {"id": 4, "name": "Shop D", "location": "Yaba"},
    {"id": 5, "name": "Shop E", "location": "Yaba"},
]

@router.get("/density")
async def get_store_density(location: str = Query(..., description="Enter location e.g., Ikeja, Yaba"), area_size: float = Query(..., description="Area size in km²")):
    """
    Calculate store density for a given location.
    Density = (Number of stores in location) / (Area size in km²)
    """
    try:
        # Count stores in the given location
        count = sum(1 for store in stores_data if store["location"].lower() == location.lower())
        
        if count == 0:
            raise HTTPException(status_code=404, detail=f"No stores found in {location}")

        density = count / area_size
        return {
            "location": location,
            "total_stores": count,
            "area_size_km2": area_size,
            "density_per_km2": round(density, 2)
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
