
from fastapi import APIRouter, HTTPException
from models.schemas import Bank
from services import bank as _bank_service

router = APIRouter()

@router.get("/banks")
async def list_banks():
    return await _bank_service.get_all_banks()

@router.post("/banks")
async def add_bank(payload: Bank):

    try:
        return await _bank_service.create_bank(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
  

@router.get("/banks/cluster/{cluster_id}")
async def density(cluster_id: int):   
     return {
        "cluster_id": cluster_id,
        "bank": await _bank_service.get_banks_by_cluster(cluster_id)
    }


@router.get("/banks/city/{city}")
async def list_banks_by_city(city: str):    
    return await _bank_service.get_banks_by_city(city)

@router.get("/banks/state/{state}")
async def list_banks_by_state(state: str):    
    return await _bank_service.get_banks_by_state(state)

@router.get("/banks/country/{country}")
async def list_banks_by_country(country: str):    
    return await _bank_service.get_banks_by_country(country)

@router.get("/banks/address/{address}")
async def list_banks_by_address(address: str):    
    return await _bank_service.get_banks_by_adress(address)


@router.get("/banks/city/{city}/cluster/{cluster_id}")
async def list_banks_by_city_and_cluster(city: str, cluster_id: int):   
    return await _bank_service.get_banks_by_city_and_cluster(city, cluster_id)

@router.get("/banks/name/{name}")
async def list_banks_by_name(name: str):
    return await _bank_service.get_banks_by_name(name)

@router.get("/banks/name/{name}/city/{city}")
async def list_banks_by_name_and_city(name: str, city: str):
    return await _bank_service.get_banks_by_name_and_city(name, city)


    

