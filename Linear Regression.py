#use colab for execution
# LINEAR REGRESSION

import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
np.random.seed(0)
X = 2 * np.random.rand(100, 1)
y = 4 + 3 * X + np.random.rand(100, 1)

model = LinearRegression()

model.fit(X, y)

X_new = np.array([[2.5]]) 
y_pred = model.predict(X_new)

print(f"Intercept (theta_0): {model.intercept_}")
print(f"Coefficient (theta_1): {model.coef_}")

plt.scatter(X, y, label='Sample Data')
plt.plot(X, model.predict(X), color='red', label='Linear Regression')
plt.scatter(X_new, y_pred, color='green', marker='x', s=100, label='Predicted Value')
plt.legend()
plt.xlabel("Feature (X)")
plt.ylabel("Target (y)")
plt.title("Linear Regression Example")
plt.show()
