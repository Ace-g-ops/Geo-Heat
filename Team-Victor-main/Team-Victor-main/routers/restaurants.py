from fastapi import APIRouter, HTTPException
from models.schemas import Restaurants
from services import restaurants as restaurant_service  

router = APIRouter()

@router.post("/restaurants")
async def add_restaurant(payload: Restaurants):  # renamed parameter
    return await restaurant_service.create_restaurant(payload)


@router.get("/restaurants")
async def list_restaurants():
    try:
        return await restaurant_service.get_all_restaurants()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/restaurants/{cluster_id}")
async def density(cluster_id: int):
    return {
        "cluster_id": cluster_id,
        "restaurants": await restaurant_service.get_restaurants_by_cluster(cluster_id)
    }
