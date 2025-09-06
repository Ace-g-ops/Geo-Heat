# Pydantic Model(requests, response)

from pydantic import BaseModel
from typing import List, Optional

class Restaurants(BaseModel):
    name: str
    lat: float
    lng: float
    cuisine: str
    rating: Optional[float] = None
    cluster: Optional[int] = None

class Cafe(BaseModel):
    name: str
    lat: float
    lng: float
    rating: Optional[float] = None
    cluster: Optional[int] = None
    state:str
    address:str



class LocationRequest(BaseModel):
    lat: float
    lng: float
    radius: int = 1000

class Bank(BaseModel):
    name: str
    lat: float
    city: str
    state: str
    country: str
    address: str    
    lng: float
    cluster: Optional[int] = None


class Hospital(BaseModel):
    name: str
    lat: float
    lng: float
    state: str
    cluster: Optional[int] = None
    rating: Optional[float] = None
    type: str    
    


class BusinessLocation(BaseModel):
    name: str
    lat: float
    Ing: float
    rating: Optional[float]
    price_level: Optional[int]
    business_type: str    


    business_type: str   

class Pharmacy(BaseModel):
    name: str
    lat: float
    lng: float
    cluster: Optional[int] = None
    address: str 
    city: str


class PetrolStation(BaseModel):
    name: str
    lat: float
    lng: float
    cluster: Optional[int] = None
    city: str
    address: str
    state: str


class DensityResponse(BaseModel):
    density_score: float
    business_count: int
    businesses: List[BusinessLocation]
    insights: List[str]     

class MarketGapResponse(BaseModel):
    cuisine_type: str
    competitor_count: int
    market_saturation: float
    opportunity_score: float
    recommendations: List[str]
    target_areas: List[dict]