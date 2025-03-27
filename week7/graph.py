import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Load CSV file (Assuming CSV has 'Temperature' and 'Humidity' columns)
csv_file = "data.csv"  # Change this to your actual file path
df = pd.read_csv(csv_file)

# Extract temperature (X) and humidity (Y) values
X = df[['Temperature']].values  # Independent variable (reshaped for sklearn)
y = df['Humidity'].values       # Dependent variable

# Train Linear Regression model
model = LinearRegression()
model.fit(X, y)

# Generate 100 interpolated temperature values between min and max
temp_min, temp_max = X.min(), X.max()
X_test = np.linspace(temp_min, temp_max, 100).reshape(-1, 1)  # Reshape for sklearn

# Predict humidity for these values
y_pred = model.predict(X_test)

# Plot original data as scatter plot
plt.scatter(X, y, color='blue', label="Actual Data", alpha=0.5)

# Plot regression line
plt.plot(X_test, y_pred, color='red', linewidth=2, label="Regression Line")

# Labels and title
plt.xlabel("Temperature (°C)")
plt.ylabel("Humidity (%)")
plt.title("Linear Regression: Temperature vs Humidity")
plt.legend()
plt.grid()

# Show the plot
plt.show()
