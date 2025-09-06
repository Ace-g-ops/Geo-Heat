from database import db
from models.schemas import PetrolStation


collection = db['petrol_stations']

async def create_petrol_station(payload: PetrolStation):
    data = payload.model_dump()
    new_petrol_station = await collection.insert_one(data)
    created_petrol_station = await collection.find_one({"_id": new_petrol_station.inserted_id})
    created_petrol_station["_id"] = str(created_petrol_station["_id"])  # convert ObjectId to string
    return created_petrol_station

async def get_all_petrol_stations(): 
    petrol_stations = []
    async for petrol_station in collection.find():
        petrol_station["_id"] = str(petrol_station["_id"])
        petrol_stations.append(petrol_station)
    return petrol_stations

async def get_petrol_stations_by_city(city: str):
    petrol_stations = []
    async for petrol_station in collection.find({"city": city}):
        petrol_station["_id"] = str(petrol_station["_id"])
        petrol_stations.append(petrol_station)
    return petrol_stations

async def get_petrol_stations_by_adress(address: str):
    petrol_stations = []
    async for petrol_station in collection.find({"address": {"$regex": address, "$options": "i"}}):
        petrol_station["_id"] = str(petrol_station["_id"])
        petrol_stations.append(petrol_station)
    return petrol_stations    

async def get_petrol_stations_by_cluster(cluster_id: int):
    petrol_stations = []
    async for petrol_station in collection.find({"cluster": cluster_id}):
        petrol_station["_id"] = str(petrol_station["_id"])
        petrol_stations.append(petrol_station)
    return petrol_stations  

async def get_petrol_stations_by_city_and_cluster(city: str, cluster_id: int):
    petrol_stations = []
    async for petrol_station in collection.find({"city": city, "cluster": cluster_id}):
        petrol_station["_id"] = str(petrol_station["_id"])
        petrol_stations.append(petrol_station)
    return petrol_stations


async def get_petrol_stations_by_name(name: str):
    petrol_stations = []
    async for petrol_station in collection.find({"name": {"$regex": name, "$options": "i"}}):
        petrol_station["_id"] = str(petrol_station["_id"])
        petrol_stations.append(petrol_station)
    return petrol_stations


async def get_petrol_stations_by_state(state: str):
    petrol_stations = []
    async for petrol_station in collection.find({"state": {"$regex": state, "$options": "i"}}):
        petrol_station["_id"] = str(petrol_station["_id"])
        petrol_stations.append(petrol_station)
    return petrol_stations

async def get_petrol_stations_by_name_and_city(name: str, city: str):
    petrol_stations = []
    async for petrol_station in collection.find({"name": {"$regex": name, "$options": "i"}, "city": city}):
        petrol_station["_id"] = str(petrol_station["_id"])
        petrol_stations.append(petrol_station)
    return petrol_stations      








