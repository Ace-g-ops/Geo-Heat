# test_free_restaurants.py
import requests
import json

def get_restaurants_osm(lat, lng, radius=1000):
    url = "https://overpass-api.de/api/interpreter"
    query = f"""
    [out:json][timeout:10];
    (
      node["amenity"="restaurant"](around:{radius},{lat},{lng});
      way["amenity"="restaurant"](around:{radius},{lat},{lng});
    );
    out center;
    """
    
    try:
        response = requests.post(url, data=query)
        data = response.json()
        restaurants = []
        
        for element in data.get('elements', []):
            if element.get('tags', {}).get('name'):
                restaurants.append({
                    'name': element['tags']['name'],
                    'lat': element.get('lat') or element.get('center', {}).get('lat'),
                    'lng': element.get('lon') or element.get('center', {}).get('lon'),
                    'cuisine': element['tags'].get('cuisine', 'unknown')
                })
        
        return restaurants
    
    except Exception as e:
        print(f"Error: {e}")
        return []

def test_lagos_areas():
    areas = {
        "Victoria Island": (6.4281, 3.4219),
        "Lekki": (6.4474, 3.4713), 
        "Ikeja": (6.5833, 3.3500),
        "Surulere": (6.5039, 3.3593)
    }
    
    for area_name, (lat, lng) in areas.items():
        print(f"\n--- {area_name} ---")
        restaurants = get_restaurants_osm(lat, lng)
        print(f"Found {len(restaurants)} restaurants")
        
        if restaurants:
            print("Sample restaurants:")
            for i, rest in enumerate(restaurants[:3]):
                print(f"  {i+1}. {rest['name']} - {rest['cuisine']}")

if __name__ == "__main__":
    test_lagos_areas()