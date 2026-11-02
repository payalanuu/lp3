import matplotlib.pyplot as plt
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# =====================================================
# 1. LOAD DATASET
# =====================================================
# Standard encoding for sales_data_sample.csv is 'unicode_escape' or 'latin1'
df = pd.read_csv("sales_data_sample.csv", encoding="unicode_escape")
print("Dataset Loaded Successfully. Shape:", df.shape)

# =====================================================
# 2. SELECT NUMERICAL FEATURES & PREPROCESS
# =====================================================
# Focus on key transactional features
features = ["QUANTITYORDERED", "PRICEEACH", "SALES", "MSRP"]
data = df[features].dropna()

# Normalize features
scaler = StandardScaler()
scaled_data = scaler.fit_transform(data)

# =====================================================
# 3. ELBOW METHOD TO FIND OPTIMAL K
# =====================================================
wcss = []
k_range = range(1, 11)

for k in k_range:
    kmeans = KMeans(n_clusters=k, init="k-means++", random_state=42)
    kmeans.fit(scaled_data)
    wcss.append(kmeans.inertia_)

# Plot the Elbow Graph
plt.figure(figsize=(8, 4))
plt.plot(k_range, wcss, marker="o", color="blue")
plt.title("Elbow Method for Optimal K")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("WCSS (Inertia)")
plt.grid(True)
plt.show()

# =====================================================
# 4. TRAIN FINAL K-MEANS MODEL (e.g., K = 3)
# =====================================================
optimal_k = 3
kmeans_model = KMeans(n_clusters=optimal_k, init="k-means++", random_state=42)
data["Cluster"] = kmeans_model.fit_predict(scaled_data)

print(f"\nK-Means Clustering Completed with k={optimal_k}")
print(data.head())

# Show cluster sizes
print("\nCluster Distribution:")
print(data["Cluster"].value_counts())

