import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import joblib
import json
import os

# Create dummy dataset (since dataset not provided)
from sklearn.datasets import make_regression

X, y = make_regression(n_samples=1000, n_features=5, noise=0.1)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
preds = model.predict(X_test)

# Metrics
mse = mean_squared_error(y_test, preds)
r2 = r2_score(y_test, preds)

# Print metrics (IMPORTANT for Jenkins console)
print(f"MSE: {mse}")
print(f"R2: {r2}")

# Save outputs
os.makedirs("outputs", exist_ok=True)

joblib.dump(model, "outputs/model.pkl")

metrics = {
    "mse": mse,
    "r2": r2
}

with open("outputs/metrics.json", "w") as f:
    json.dump(metrics, f, indent=4)