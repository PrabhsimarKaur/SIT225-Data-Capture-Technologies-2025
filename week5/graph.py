import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("gyroscope_data.csv")

# Data Cleaning: Remove NaN or non-numeric values
df.dropna(inplace=True)

# Convert columns to appropriate types
df["timestamp"] = pd.to_datetime(df["timestamp"], unit="ms")
df["x"] = pd.to_numeric(df["x"], errors="coerce")
df["y"] = pd.to_numeric(df["y"], errors="coerce")
df["z"] = pd.to_numeric(df["z"], errors="coerce")

# Plot data
plt.figure(figsize=(10, 5))

# Individual plots
plt.subplot(3, 1, 1)
plt.plot(df["timestamp"], df["x"], label="X-axis", color="r")
plt.legend()

plt.subplot(3, 1, 2)
plt.plot(df["timestamp"], df["y"], label="Y-axis", color="g")
plt.legend()

plt.subplot(3, 1, 3)
plt.plot(df["timestamp"], df["z"], label="Z-axis", color="b")
plt.legend()

plt.tight_layout()
plt.show()

# Combined plot
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["x"], label="X-axis", color="r")
plt.plot(df["timestamp"], df["y"], label="Y-axis", color="g")
plt.plot(df["timestamp"], df["z"], label="Z-axis", color="b")
plt.legend()
plt.xlabel("Timestamp")
plt.ylabel("Gyroscope Readings")
plt.title("Gyroscope Sensor Data")
plt.show()
