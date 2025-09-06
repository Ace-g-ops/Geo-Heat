import asyncio
from database import db


dummy_store = [

    {"name": "Shop A", "lat": "3.3792", "lng": "3.3892"},
    {"name": "Shop B", "lat": "3.098", "lng": "3.9082"},
    {"name": "Shop C", "lat": "3.3642", "lng": "3.0987"},
    {"name": "Shop D", "lat": "3.4653", "lng": "3.6745"},
]

async def seed():
    await db["stores"].insert_many(dummy_store)

asyncio.run(seed())    