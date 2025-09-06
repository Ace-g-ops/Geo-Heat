from database import db
from models.schemas import Hospital


collection = db['hospitals']


async def create_hospital(payload: Hospital):
    data = payload.model_dump()
    new_hospital = await collection.insert_one(data)
    created_hospital = await collection.find_one({"_id": new_hospital.inserted_id})
    created_hospital["_id"] = str(created_hospital["_id"])  # convert ObjectId to string
    return created_hospital


async def get_all_hospitals():
    hospitals = []
    async for hospital in collection.find():
        hospital["_id"] = str(hospital["_id"])
        hospitals.append(hospital)
    return hospitals

async def get_hospitals_by_city(city: str):
    hospitals = []
    async for hospital in collection.find({"city": city}):
        hospital["_id"] = str(hospital["_id"])
        hospitals.append(hospital)
    return hospitals

async def get_hospitals_by_state(state: str):
    hospitals = []
    async for hospital in collection.find({"state": state}):
        hospital["_id"] = str(hospital["_id"])
        hospitals.append(hospital)
    return hospitals

async def get_hospitals_by_cluster(cluster_id: int):
    hospitals = []
    async for hospital in collection.find({"cluster": cluster_id}):
        hospital["_id"] = str(hospital["_id"])
        hospitals.append(hospital)
    return hospitals

async def get_hospitals_by_type(type: str):
    hospitals = []
    async for hospital in collection.find({"type": {"$regex": type, "$options": "i"}}):
        hospital["_id"] = str(hospital["_id"])
        hospitals.append(hospital)
    return hospitals

async def get_hospitals_by_rating(rating: int):
    hospitals = []
    async for hospital in collection.find({"rating": {"$gte": rating}}):
        hospital["_id"] = str(hospital["_id"])
        hospitals.append(hospital)
    return hospitals    


async def get_hospitals_by_city_and_cluster(city: str, cluster_id: int):
    hospitals = []
    async for hospital in collection.find({"city": city, "cluster": cluster_id}):
        hospital["_id"] = str(hospital["_id"])
        hospitals.append(hospital)
    return hospitals    


