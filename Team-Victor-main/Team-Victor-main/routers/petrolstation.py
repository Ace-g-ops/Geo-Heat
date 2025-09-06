from fastapi import APIRouter
from models.schemas import PetrolStation
from services import petrolstation as petrolstation_service


router = APIRouter()

@router.get("/petrol_stations")
async def list_petrol_stations():
    return await petrolstation_service.get_all_petrol_stations()

@router.post("/petrol_stations")
async def add_petrol_station(payload: PetrolStation):   
    return await petrolstation_service.create_petrol_station(payload)

@router.get("/petrol_stations/cluster/{cluster_id}")
async def list_petrol_stations_by_cluster(cluster_id: int):
    return await petrolstation_service.get_petrol_stations_by_cluster(cluster_id)

@router.get("/petrol_stations/city/{city}")
async def list_petrol_stations_by_city(city: str):
    return await petrolstation_service.get_petrol_stations_by_city(city)

@router.get("/petrol_stations/city/{city}/cluster/{cluster_id}")
async def list_petrol_stations_by_city_and_cluster(city: str, cluster_id: int):   
    return await petrolstation_service.get_petrol_stations_by_city_and_cluster(city, cluster_id)

@router.get("/petrol_stations/name/{name}")
async def list_petrol_stations_by_name(name: str):
    return await petrolstation_service.get_petrol_stations_by_name(name)

@router.get("/petrol_stations/state/{state}")
async def list_petrol_stations_by_state(state: str):
    return await petrolstation_service.get_petrol_stations_by_state(state)

@router.get("/petrol_stations/address/{address}")   
async def list_petrol_stations_by_address(address: str):
    return await petrolstation_service.get_petrol_stations_by_adress(address)

