from database import db
from models.schemas import Bank


collection = db['banks']


async def create_bank(payload: Bank):
    data = payload.model_dump()
    new_bank = await collection.insert_one(data)
    created_bank = await collection.find_one({"_id": new_bank.inserted_id})
    created_bank["_id"] = str(created_bank["_id"])  # convert ObjectId to string
    return created_bank


async def get_all_banks():
    banks = []
    async for bank in collection.find():
        bank["_id"] = str(bank["_id"])
        banks.append(bank)
    return banks

async def get_banks_by_city(city: str):
    banks = []
    async for bank in collection.find({"city": city}):
        bank["_id"] = str(bank["_id"])
        banks.append(bank)
    return banks

async def get_banks_by_state(state: str):
    banks = []
    async for bank in collection.find({"state": state}):
        bank["_id"] = str(bank["_id"])
        banks.append(bank)
    return banks

async def get_banks_by_country(country: str):
    banks = []
    async for bank in collection.find({"country": country}):
        bank["_id"] = str(bank["_id"])
        banks.append(bank)
    return banks
async def get_banks_by_adress(address: str):
    banks = []
    async for bank in collection.find({"address": {"$regex": address, "$options": "i"}}):
        bank["_id"] = str(bank["_id"])
        banks.append(bank)
    return banks

async def get_banks_by_cluster(cluster_id: int):
    banks = []
    async for bank in collection.find({"cluster": cluster_id}):
        bank["_id"] = str(bank["_id"])
        banks.append(bank)
    return banks


async def get_banks_by_city_and_cluster(city: str, cluster_id: int):
    banks = []
    async for bank in collection.find({"city": city, "cluster": cluster_id}):
        bank["_id"] = str(bank["_id"])
        banks.append(bank)
    return banks


async def get_banks_by_name(name: str):
    banks = []
    async for bank in collection.find({"name": {"$regex": name, "$options": "i"}}):
        bank["_id"] = str(bank["_id"])
        banks.append(bank)
    return banks


async def get_banks_by_name_and_city(name: str, city: str):
    banks = []
    async for bank in collection.find({"name": {"$regex": name, "$options": "i"}, "city": city}):
        bank["_id"] = str(bank["_id"])
        banks.append(bank)
    return banks