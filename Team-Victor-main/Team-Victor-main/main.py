
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello World"}

# from fastapi import FastAPI
# from routers.restaurants import router as restaurant_router

# app = FastAPI()

# # Include the restaurant router
# app.include_router(restaurant_router, prefix="/api/v1/restaurants", tags=["restaurants"])

# @app.get("/")
# def read_root():
#     return {"message": "Hello World"}


from fastapi import FastAPI
from routers import restaurants
from routers import bank
from routers import hospital
from routers import store
from routers import density
from routers import pharmacy
from routers import petrolstation
from routers import ai_density

app = FastAPI()

app.include_router(restaurants.router)
app.include_router(pharmacy.router)
app.include_router(bank.router)
app.include_router(hospital.router) 
app.include_router(store.router, prefix="/api/v1/stores", tags=["stores"])
app.include_router(density.router)
app.include_router(petrolstation.router)
app.include_router(ai_density.router)
@app.get("/")
def read_root():    
    return {"message": "Api is working"}
# @app.get("/test-db")
# async def test_db():
#     try:
#         count = await db["restaurants"].count_documents({})
#         return {"restaurant_count": count}
#     except Exception as e:
#         return {"error": str(e)}



