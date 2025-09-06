from database import db
from models.schemas import Cafe

collection = db['cafes']

async def create_cafe(payload: Cafe):
    data = payload.model_dump()
    new_cafe = await collection.insert_one(data)
    created_cafe = await collection.find_one({"_id": new_cafe.inserted_id})
    created_cafe["_id"] = str(created_cafe["_id"])  # convert ObjectId to string
    return created_cafe

async def get_all_cafes():
    cafes = []
    async for cafe in collection.find():
        cafe["_id"] = str(cafe["_id"])
        cafes.append(cafe)
    return cafes


async def get_cafes_by_state(state: str):
    cafes = []
    async for cafe in collection.find({"state": state}):
        cafe["_id"] = str(cafe["_id"])
        cafes.append(cafe)
    return cafes


async def get_cafes_by_address(address: str):
    cafes = []
    async for cafe in collection.find({"address": {"$regex": address, "$options": "i"}}):
        cafe["_id"] = str(cafe["_id"])
        cafes.append(cafe)
    return cafes

async def get_cafes_by_cluster(cluster_id: int):
    cafes = []
    async for cafe in collection.find({"cluster": cluster_id}):
        cafe["_id"] = str(cafe["_id"])
        cafes.append(cafe)
    return cafes

async def get_cafes_by_city_and_cluster(city: str, cluster_id: int):
    cafes = []
    async for cafe in collection.find({"city": city, "cluster": cluster_id}):
        cafe["_id"] = str(cafe["_id"])
        cafes.append(cafe)
    return cafes

async def get_cafe_by_id(cafe_id: str):
    cafe = await collection.find_one({"_id": cafe_id})
    if cafe:
        cafe["_id"] = str(cafe["_id"])
    return cafe

async def get_by_rating(min_rating: float):
    cafes = []
    async for cafe in collection.find({"rating": {"$gte": min_rating}}):
        cafe["_id"] = str(cafe["_id"])
        cafes.append(cafe)
    return cafes