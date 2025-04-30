import pandas as pd
import firebase_admin
from firebase_admin import credentials, db

# Fetch data from Firebase
cred = credentials.Certificate("task5-11149-firebase-adminsdk-fbsvc-e6ef2063b8.json")
firebase_admin.initialize_app(cred, {
    "databaseURL": "databaseURL": "https://task5-11149-default-rtdb.firebaseio.com/"
})

gyro_data = db.reference("GyroscopeData").get()

# Convert data to a DataFrame
df = pd.DataFrame(gyro_data.values())

# Save to CSV
df.to_csv("gyro_data.csv", index=False)
print("Data saved to gyro_data.csv")

# Clean Data: Remove NaN and non-numeric values
df.dropna(inplace=True)

# Convert x, y, z columns to numeric
df["x"] = pd.to_numeric(df["x"], errors="coerce")
df["y"] = pd.to_numeric(df["y"], errors="coerce")
df["z"] = pd.to_numeric(df["z"], errors="coerce")

df.dropna(inplace=True)  # Remove any remaining invalid rows
df.to_csv("gyro_data_clean.csv", index=False)
print("Cleaned data saved to gyro_data_clean.csv")
