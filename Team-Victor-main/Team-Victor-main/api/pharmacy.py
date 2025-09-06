from fastapi import APIRouter
from models.schemas import Pharmacy
from services import bank as pharmacy_servces

router = APIRouter()

@router.get("/pharmacy")
async def list_pharmacy():
    return await pharmacy_servces.get_all_pharmacy()

@router.post("/pharmacy")
async def add_pharmacy(payload: Pharmacy):
    return await pharmacy_servces.create_pharmacy(payload)

@router.get("/pharmacy/cluster/{cluster_id}")
async def list_banks_by_cluster(cluster_id: int):
    return await pharmacy_servces.get_pharmacy_by_cluster(cluster_id)

@router.get("/pharmacy/city/{city}")
async def list_banks_by_city(city: str):
    return await pharmacy_servces.get_pharmacy_by_city(city)

@router.get("/pharmacy/city/{city}/cluster/{cluster_id}")
async def list_banks_by_city_and_cluster(city: str, cluster_id: int):   
    return await pharmacy_servces.get_pharmacy_by_city_and_cluster(city, cluster_id)


@router.get("/pharmacy/name/{name}")
async def list__pharmacy_by_name(name: str):
    return await pharmacy_servces.get_pharmacy_by_name(name)   


@router.get("/pharmacy/address/{address}")
async def list_pharmacy_by_address(address: str):  
    return await pharmacy_servces.get_phamarcy_by_adress(address)


    