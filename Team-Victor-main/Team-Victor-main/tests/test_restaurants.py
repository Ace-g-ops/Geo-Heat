# from fastapi.testclient import  TestClient
# from main import app
# from models.schemas import LocationRequest

# client = TestClient(app) 

# def test_restaurant_density_analysis(): 
#     # test data
#     request_data = {
#         "lat": 6.5244,
#         "lng": 3.3792,
#         "radius": 1000
#     } 

#     response = client.post("/api/v1/restaurants/density-analysis", json=request_data)
#     assert response.status_code == 200  
#     data = response.json()
#     assert "density_score" in data
#     assert "business_count" in data
#     assert isinstance(data["businesses"], list)

#     def test_invalid_location_data():
#         request_data = {
#             "lat": "invalid",
#             "lng": 3.3792,
#             "radius": 1000
#         } 

#         response = client.post("/api/v1/restaurants/density-analysis", json=request_data)
#         assert response.status_code == 422




import pandas as pd
import random

# Define some sample cuisines
cuisines = ["Italian", "Chinese", "Indian", "Mexican", "Fast Food", "Cafe"]

# Generate fake restaurant data
data = []
for i in range(50):  # 50 restaurants
    restaurant = {
        "id": i + 1,
        "name": f"Restaurant_{i+1}",
        "latitude": round(random.uniform(6.4, 6.6), 6),   # Example: Lagos coordinates
        "longitude": round(random.uniform(3.3, 3.6), 6),
        "cuisine": random.choice(cuisines),
        "rating": round(random.uniform(2.5, 5.0), 1)
    }
    data.append(restaurant)

# Convert to DataFrame
df = pd.DataFrame(data)

# Save to CSV (for training)
df.to_csv("restaurants.csv", index=False)

print("Sample data saved to restaurants.csv")
