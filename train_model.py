import pandas as pd  # type: ignore
import numpy as np  # type: ignore
from sklearn.model_selection import train_test_split  # type: ignore
from sklearn.linear_model import LogisticRegression  # type: ignore
import pickle

print(" Step 1: Generating synthetic transaction data...")
np.random.seed(42)
num_transactions = 500 

data = pd.DataFrame({
    "transaction_id": range(num_transactions),
    "amount": np.random.uniform(10, 1000, num_transactions),
    "customer_age": np.random.randint(18, 70, num_transactions),
    "transaction_type": np.random.randint(0, 2, num_transactions),
    "is_fraud": np.random.randint(0, 2, num_transactions)
})
print(" Data generated! Shape:", data.shape)

print(" Step 2: Splitting data into train/test...")
X = data[["amount", "customer_age", "transaction_type"]]
y = data["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print("Split done. Training samples:", X_train.shape[0], "Test samples:", X_test.shape[0])

print("Step 3: Training Logistic Regression model...")
model = LogisticRegression(max_iter=200, solver='liblinear')  # i used liblinear because it is best for small data (prototype)
model.fit(X_train, y_train)
print("Model trained!")

print("Step 4: Saving model to model.pkl...")
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
print("Model saved as model.pkl successfully.")
