# GOOGLE API CALLS

import requests
import os
from typing import List
from models.schemas import BusinessLocation

class GooglePlacesService:
    def __init__(self):
        self.api_key = os.getenv('GOOGLE_PLACES_API_KEY')
        self.base_url = "https://maps.googleapis.com/maps/api/place/nearbysearch/json"
    
    def get_restaurants(self, lat: float, lng: float, radius: int) -> List[BusinessLocation]:
        params = {
            'location': f'{lat},{lng}',
            'radius': radius,
            'type': 'restaurant',
            'key': self.api_key
        }
        
        response = requests.get(self.base_url, params=params)
        data = response.json()
        
        restaurants = []
        for place in data.get('results', []):
            restaurants.append(BusinessLocation(
                name=place['name'],
                lat=place['geometry']['location']['lat'],
                lng=place['geometry']['location']['lng'],
                rating=place.get('rating'),
                price_level=place.get('price_level'),
                business_type='restaurant'
            ))
        
        return restaurants

    def get_banks(self, lat: float, lng: float, radius: int) -> List[BusinessLocation]:
        # Similar logic for banks
        pass