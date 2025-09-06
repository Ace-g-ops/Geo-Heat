from fastapi import APIRouter
from models.schemas import Cafe
from services import cafe as cafe_service

router = APIRouter()

@router.get("/cafes")
async def list_cafes():
    return await cafe_service.get_all_cafes()


@router.post("/cafes")
async def add_cafe(payload: Cafe):
    return await cafe_service.create_cafe(payload)

@router.get("/cafes/state/{state}")
async def list_cafes_by_state(state: str):
    return await cafe_service.get_cafes_by_state(state)


@router.get("/cafes/cluster/{cluster_id}")
async def list_cafes_by_cluster(cluster_id: int):
    return await cafe_service.get_cafe_by_cluster(cluster_id)

@router.get("/cafes/city/{city}/cluster/{cluster_id}")
async def list_cafes_by_city_and_cluster(city: str, cluster_id: int):
    return await cafe_service.get_cafes_by_city_and_cluster(city, cluster_id)


@router.get("/cafes/rating/{rating}")
async def list_cafes_by_rating(rating: float):
    return await cafe_service.get_cafes_by_rating(rating)

@router.get("/cafes/address/{address}")
async def list_cafes_by_address(address: str):
    return await cafe_service.get_cafes_by_address(address)