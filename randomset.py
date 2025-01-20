import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_squared_error

# Sample data
data = {
    'size': [1500, 1600, 1700, 1800, 1900, 2000, 2100, 2200, 2300, 2400],
    'bedrooms': [3, 3, 4, 4, 5, 5, 6, 6, 7, 7],
    'price': [250000, 280000, 300000, 320000, 350000, 380000, 410000, 440000, 470000, 500000]
}
df = pd.DataFrame(data)

# Features (X) and target (y)
X = df[['size', 'bedrooms']]
y = df['price']

# Split the data with random_state=0
X_train_0, X_test_0, y_train_0, y_test_0 = train_test_split(X, y, test_size=0.2, random_state=0)

# Split the data with random_state=2
X_train_2, X_test_2, y_train_2, y_test_2 = train_test_split(X, y, test_size=0.2, random_state=2)

# Create and train the model with random_state=0
model_0 = DecisionTreeRegressor(random_state=0)
model_0.fit(X_train_0, y_train_0)
predictions_0 = model_0.predict(X_test_0)
mse_0 = mean_squared_error(y_test_0, predictions_0)

# Create and train the model with random_state=2
model_2 = DecisionTreeRegressor(random_state=2)
model_2.fit(X_train_2, y_train_2)
predictions_2 = model_2.predict(X_test_2)
mse_2 = mean_squared_error(y_test_2, predictions_2)

print(f"MSE with random_state=0: {mse_0}")
print(f"MSE with random_state=2: {mse_2}")
