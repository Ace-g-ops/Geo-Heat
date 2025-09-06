# helper function
def serialize_doc(doc):
    doc["_id"] = str(doc["_id"])
    return doc

# get all restaurants
async def get_all_restaurants():
    restaurants = []
    async for restaurant in collection.find():
        restaurants.append(serialize_doc(restaurant))
    return restaurants

# get restaurants by cluster
async def get_restaurants_by_cluster(cluster_id: int):
    restaurants = []
    async for restaurant in collection.find({"cluster": cluster_id}):
        restaurants.append(serialize_doc(restaurant))
    return restaurants
