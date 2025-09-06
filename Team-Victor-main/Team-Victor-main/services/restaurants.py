from database import db
from models.schemas import Restaurants

collection = db['restaurants']


async def create_restaurant(payload: Restaurants):
    data = payload.model_dump()
    new_restaurant = await collection.insert_one(data)
    created_restaurant = await collection.find_one({"_id": new_restaurant.inserted_id})
    created_restaurant["_id"] = str(created_restaurant["_id"])  # convert ObjectId to string
    return created_restaurant



async def get_all_restaurants():
    restaurants = []
    async for restaurant in collection.find():
        restaurant["_id"] = str(restaurant["_id"])
        restaurants.append(restaurant)
    return restaurants

async def get_restaurants_by_cluster(cluster_id: int):
    restaurants = []
    async for restaurant in collection.find({"cluster": cluster_id}):
        restaurant["_id"] = str(restaurant["_id"])
        restaurants.append(restaurant)
    return restaurants