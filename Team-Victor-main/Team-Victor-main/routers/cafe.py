from fastapi import APIRouter, HTTPException
from models.schemas import Cafe
from services import cafe as cafe_services

router = APIRouter()

@router.get("/cafe")
async def list_cafes():
    return await cafe_services.get_all_cafes()

@router.post("/cafe")
async def add_cafe(payload: Cafe):
    try:
        return await cafe_services.create_cafe(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    
@router.get("/cafe/cluster/{cluster_id}")
async def density(cluster_id: int):   
     return {
        "cluster_id": cluster_id,
        "cafes": await cafe_services.get_cafes_by_cluster(cluster_id)
    }

@router.get("/cafe/state/{state}")
async def list_cafes_by_state(state: str):    
    return await cafe_services.get_cafes_by_state(state)

@router.get("/cafe/address/{address}")
async def list_cafes_by_address(address: str):
    return await cafe_services.get_cafes_by_address(address)

@router.get("/cafe/state/{state}/cluster/{cluster_id}")
async def list_cafes_by_state_and_cluster(state: str, cluster_id: int):   
    return await cafe_services.get_cafes_by_state_and_cluster(state, cluster_id)  

@router.get("/cafe/name/{name}")
async def list_cafes_by_name(name: str):
    return await cafe_services.get_cafes_by_name(name)

@router.get("/cafe/cluster/{cluster_id}/name/{name}")
async def list_cafes_by_cluster_and_name(cluster_id: int, name: str):
    return await cafe_services.get_cafes_by_cluster_and_name(cluster_id, name)

@router.get("/cafe/rating/{rating}")
async def list_cafes_by_rating(rating: float):
    return await cafe_services.get_cafes_by_rating(rating)







