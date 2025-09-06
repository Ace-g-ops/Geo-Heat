from fastapi import APIRouter, HTTPException
from models.schemas import Hospital
from services import hospital as hospital_service

router = APIRouter()

@router.get("/hospitals")
async def list_hospitals():
    try:
        return await hospital_service.get_all_hospitals()
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/hospitals")
async def add_hospital(payload: Hospital):
    try:
        return await hospital_service.create_hospital(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.get("/hospitals/city/{city}")
async def list_hospitals_by_city(city: str):
    return await hospital_service.get_hospitals_by_city(city)

@router.get("/hospitals/state/{state}")
async def list_hospitals_by_state(state: str):
    return await hospital_service.get_hospitals_by_state(state)

@router.get("/hospitals/cluster/{cluster_id}")
async def list_hospitals_by_cluster(cluster_id: int):
    return await hospital_service.get_hospitals_by_cluster(cluster_id)

@router.get("/hospitals/city/{city}/cluster/{cluster_id}")
async def list_hospitals_by_city_and_cluster(city: str, cluster_id: int):
    return await hospital_service.get_hospitals_by_city_and_cluster(city, cluster_id)

@router.get("/hospitals/type/{type}")
async def list_hospitals_by_type(type: str):
    return await hospital_service.get_hospitals_by_type(type)

@router.get("/hospitals/rating/{rating}")
async def list_hospitals_by_rating(rating: int):
    return await hospital_service.get_hospitals_by_rating(rating)
