from database import db
from models.schemas import Pharmacy




collection = db['pharmacies']


async def create_pharmacy(payload: Pharmacy):
    data = payload.model_dump()
    new_pharmacy = await collection.insert_one(data)
    created_pharmacies = await collection.find_one({"_id": new_pharmacy.inserted_id})
    created_pharmacies["_id"] = str(created_pharmacies["_id"])  # convert ObjectId to string
    return created_pharmacies


async def get_all_pharmacies(): 
    pharmacies = []
    async for pharmacy in collection.find():
        pharmacy["_id"] = str(pharmacy["_id"])
        pharmacies.append(pharmacy)
    return pharmacies

async def get_pharmacies_by_city(city: str):
    pharmacies = []
    async for pharmacy in collection.find({"city": city}):
        pharmacy["_id"] = str(pharmacy["_id"])
        pharmacies.append(pharmacy)
    return pharmacies


async def get_pharmacies_by_adress(address: str):
    pharmacies = []
    async for pharmacy in collection.find({"address": {"$regex": address, "$options": "i"}}):
        pharmacy["_id"] = str(pharmacy["_id"])
        pharmacies.append(pharmacy)
    return pharmacies


async def get_pharmacies_by_cluster(cluster_id: int):
    pharmacies = []
    async for pharmacy in collection.find({"cluster": cluster_id}):
        pharmacy["_id"] = str(pharmacy["_id"])
        pharmacies.append(pharmacy)
    return pharmacies


async def get_pharmacies_by_city_and_cluster(city: str, cluster_id: int):
    pharmacies = []
    async for pharmacy in collection.find({"city": city, "cluster": cluster_id}):
        pharmacy["_id"] = str(pharmacy["_id"])
        pharmacies.append(pharmacy)
    return pharmacies

async def get_pharmacies_by_name(name: str):
    pharmacies = []
    async for pharmacy in collection.find({"name": {"$regex": name, "$options": "i"}}):
        pharmacy["_id"] = str(pharmacy["_id"])
        pharmacies.append(pharmacy)
    return pharmacies


async def get_pharmacies_by_name_and_city(name: str, city: str):
    pharmacies = []
    async for pharmacy in collection.find({"name": {"$regex": name, "$options": "i"}, "city": city}):
        pharmacy["_id"] = str(pharmacy["_id"])
        pharmacies.append(pharmacy)
    return pharmacies


async def get_pharmacies_by_state(state: str):
    pharmacies = []
    async for pharmacy in collection.find({"state": state}):
        pharmacy["_id"] = str(pharmacy["_id"])
        pharmacies.append(pharmacy)
    return pharmacies


async def get_pharmacies_by_name_and_city(state: str):
    pharmacies = []
    async for pharmacy in collection.find({"city": state}):
        pharmacy["_id"] = str(pharmacy["_id"])
        pharmacies.append(pharmacy)
    return pharmacies









