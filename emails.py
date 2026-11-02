import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix

# =====================================================
# 1. LOAD DATASET
# =====================================================
# Standard SPPU LP-III spam dataset (emails.csv or spambase.csv)
df = pd.read_csv("emails.csv")
print("Dataset Loaded Successfully. Shape:", df.shape)

# =====================================================
# 2. PREPROCESSING & CLEANING
# =====================================================
# Drop unnecessary identifier columns if present
if "Email No." in df.columns:
    df = df.drop(columns=["Email No."])

# Drop missing values
df = df.dropna()

# Separate features (word frequencies) and target ('Prediction')
# In emails.csv, the last column 'Prediction' is 1 for Spam, 0 for Not Spam
X = df.drop(columns=["Prediction"])
y = df["Prediction"]

# =====================================================
# 3. SPLIT DATA
# =====================================================
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Normalize features for distance-based models (KNN & SVM)
scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# =====================================================
# 4. K-NEAREST NEIGHBORS (KNN) MODEL
# =====================================================
print("\n--- Training K-Nearest Neighbors ---")
knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
knn_pred = knn.predict(X_test)

knn_acc = accuracy_score(y_test, knn_pred)
print(f"KNN Accuracy: {knn_acc * 100:.2f}%")
print("KNN Confusion Matrix:")
print(confusion_matrix(y_test, knn_pred))
print("KNN Classification Report:")
print(classification_report(y_test, knn_pred))

# =====================================================
# 5. SUPPORT VECTOR MACHINE (SVM) MODEL
# =====================================================
print("\n--- Training Support Vector Machine ---")
svm = SVC(kernel="linear", random_state=42)
svm.fit(X_train, y_train)
svm_pred = svm.predict(X_test)

svm_acc = accuracy_score(y_test, svm_pred)
print(f"SVM Accuracy: {svm_acc * 100:.2f}%")
print("SVM Confusion Matrix:")
print(confusion_matrix(y_test, svm_pred))
print("SVM Classification Report:")
print(classification_report(y_test, svm_pred))

# =====================================================
# 6. MODEL COMPARISON
# =====================================================
comparison = pd.DataFrame(
    {
        "Model": ["K-Nearest Neighbors (KNN)", "Support Vector Machine (SVM)"],
        "Accuracy (%)": [round(knn_acc * 100, 2), round(svm_acc * 100, 2)],
    }
)

print("\n--- Final Performance Comparison ---")
print(comparison.to_string(index=False))

