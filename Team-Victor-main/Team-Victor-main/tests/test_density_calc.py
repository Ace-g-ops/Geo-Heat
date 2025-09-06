import pandas as pd
from sklearn.cluster import DBSCAN
import numpy as np

# Load dataset
df = pd.read_csv("restaurants.csv")

# Prepare coordinates
coords = df[['latitude', 'longitude']].to_numpy()

# DBSCAN clustering (eps ~ distance threshold, min_samples = density sensitivity)
kms_per_radian = 6371.0088
epsilon = 0.5 / kms_per_radian  # ~0.5 km radius

db = DBSCAN(eps=epsilon, min_samples=3, metric='haversine').fit(np.radians(coords))

# Assign cluster labels
df['cluster'] = db.labels_

# Save clustered data
df.to_csv("restaurants_clustered.csv", index=False)
print(df.head())
