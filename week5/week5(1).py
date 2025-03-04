import json
import pandas as pd
from firebase_admin import db

ref = db.reference("GyroscopeData")  
data = ref.get()

if data:
    df = pd.DataFrame(data.values())
    df = df.sort_values("timestamp")  # Sort by time
    df.to_csv("gyroscope_data.csv", index=False)
    print("Data saved to gyroscope_data.csv")
else:
    print("No data found in Firebase.")
