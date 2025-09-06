from fastapi import APIRouter, HTTPException
from models.schemas import Pharmacy
from services import pharmacy as pharmacy_services


router = APIRouter()


@router.get("/pharmacy")
async def list_pharmacy():
    return await pharmacy_services.get_all_pharmacies()


@router.post("/pharmacy")
async def add_pharmacy(payload: Pharmacy):

    try:
        return await pharmacy_services.create_pharmacy(payload)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@router.get("/pharmacy/cluster/{cluster_id}")
async def density(cluster_id: int):   
     return {
        "cluster_id": cluster_id,
        "pharmacy": await pharmacy_services.get_pharmacies_by_cluster(cluster_id)
    }

@router.get("/pharmacy/city/{city}")
async def list_phamarcy_by_city(city: str):    
    return await pharmacy_services.get_pharmacies_by_city(city)

@router.get("/banks/state/{state}")
async def list_banks_by_state(state: str):    
    return await pharmacy_services.get_pharmacies_by_state(state)

@router.get("/pharmacy/address/{address}")
async def list_banks_by_address(address: str):    
    return await pharmacy_services.get_pharmacies_by_adress(address)

@router.get("/banks/city/{city}/cluster/{cluster_id}")
async def list_banks_by_city_and_cluster(city: str, cluster_id: int):   
    return await pharmacy_services.get_pharmacies_by_city_and_cluster(city, cluster_id)

@router.get("/pharmacy/name/{name}")
async def list_banks_by_name(name: str):
    return await pharmacy_services.get_pharmacies_by_name(name)

@router.get("/pharmacy/name/{name}/city/{city}")
async def list_pharmacy_by_name_and_city(name: str, city: str):
    return await pharmacy_services.get_pharmacies_by_name_and_city(name, city)