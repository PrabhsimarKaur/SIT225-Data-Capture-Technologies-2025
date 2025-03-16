import matplotlib.pyplot as plt
from pymongo import MongoClient
import pandas as pd

# Connect to MongoDB
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "sensor_data"
COLLECTION_NAME = "gyroscope_readings"

mongo_client = MongoClient(MONGO_URI)
db = mongo_client[DATABASE_NAME]
collection = db[COLLECTION_NAME]

# Load data into Pandas DataFrame
data = list(collection.find({}, {"_id": 0}))  # Exclude MongoDB ID
df = pd.DataFrame(data)

# Plot Data
plt.figure(figsize=(10, 5))
plt.plot(df["timestamp"], df["x"], label="X-axis")
plt.plot(df["timestamp"], df["y"], label="Y-axis")
plt.plot(df["timestamp"], df["z"], label="Z-axis")
plt.xlabel("Timestamp")
plt.ylabel("Gyroscope Readings")
plt.title("Gyroscope Sensor Data Over Time")
plt.legend()
plt.xticks(rotation=45)
plt.grid()
plt.show()
