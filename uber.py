import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

# =====================================================
# 1. LOAD DATASET
# =====================================================
# Standard SPPU LP-III dataset file: uber.csv
df = pd.read_csv("uber.csv")
print("Dataset Loaded Successfully. Initial Shape:", df.shape)

# =====================================================
# 2. PREPROCESSING & CLEANING
# =====================================================
# Drop unnecessary identifier columns if present
drop_cols = [c for c in ["Unnamed: 0", "key"] if c in df.columns]
df = df.drop(columns=drop_cols)

# Drop missing values
df = df.dropna()


# Feature engineering: calculate distance using Haversine formula
def haversine_distance(lat1, lon1, lat2, lon2):
    r = 6371.0  # Earth's radius in kilometers
    phi1, phi2 = np.radians(lat1), np.radians(lat2)
    dphi = np.radians(lat2 - lat1)
    dlambda = np.radians(lon2 - lon1)

    a = (
        np.sin(dphi / 2.0) ** 2
        + np.cos(phi1) * np.cos(phi2) * np.sin(dlambda / 2.0) ** 2
    )
    return 2 * r * np.arcsin(np.sqrt(a))


df["distance_km"] = haversine_distance(
    df["pickup_latitude"],
    df["pickup_longitude"],
    df["dropoff_latitude"],
    df["dropoff_longitude"],
)

# Extract datetime features if pickup_datetime column exists
if "pickup_datetime" in df.columns:
    df["pickup_datetime"] = pd.to_datetime(
        df["pickup_datetime"], errors="coerce"
    )
    df["hour"] = df["pickup_datetime"].dt.hour
    df["day_of_week"] = df["pickup_datetime"].dt.dayofweek
    df = df.drop(columns=["pickup_datetime"])

# =====================================================
# 3. IDENTIFY & REMOVE OUTLIERS
# =====================================================
# Valid coordinate boundaries for realistic NYC taxi/Uber rides
df = df[
    (df["pickup_latitude"].between(-90, 90))
    & (df["dropoff_latitude"].between(-90, 90))
    & (df["pickup_longitude"].between(-180, 180))
    & (df["dropoff_longitude"].between(-180, 180))
]

# Realistic bounds for fare amount and distance traveled
df = df[(df["fare_amount"] > 0) & (df["fare_amount"] <= 100)]
df = df[(df["distance_km"] > 0) & (df["distance_km"] <= 50)]

if "passenger_count" in df.columns:
    df = df[(df["passenger_count"] > 0) & (df["passenger_count"] <= 6)]

print("Shape After Preprocessing & Outlier Removal:", df.shape)

# =====================================================
# 4. CHECK CORRELATION
# =====================================================
print("\nCorrelation with Fare Amount:")
corr_matrix = df.corr(numeric_only=True)
print(corr_matrix["fare_amount"].sort_values(ascending=False))

# =====================================================
# 5. SPLIT DATA
# =====================================================
X = df.drop("fare_amount", axis=1)
y = df["fare_amount"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# =====================================================
# 6. LINEAR REGRESSION MODEL
# =====================================================
lr = LinearRegression()
lr.fit(X_train, y_train)
lr_pred = lr.predict(X_test)

lr_rmse = np.sqrt(mean_squared_error(y_test, lr_pred))
lr_r2 = r2_score(y_test, lr_pred)

# =====================================================
# 7. RANDOM FOREST REGRESSION MODEL
# =====================================================
# n_estimators=50 and max_depth=10 to run fast during viva/demo
rf = RandomForestRegressor(n_estimators=50, max_depth=10, random_state=42)
rf.fit(X_train, y_train)
rf_pred = rf.predict(X_test)

rf_rmse = np.sqrt(mean_squared_error(y_test, rf_pred))
rf_r2 = r2_score(y_test, rf_pred)

# =====================================================
# 8. COMPARE EVALUATION METRICS (R² and RMSE)
# =====================================================
results = pd.DataFrame(
    {
        "Model": ["Linear Regression", "Random Forest Regressor"],
        "RMSE": [round(lr_rmse, 4), round(rf_rmse, 4)],
        "R2 Score": [round(lr_r2, 4), round(rf_r2, 4)],
    }
)

print("\n--- Model Comparison ---")
print(results.to_string(index=False))

