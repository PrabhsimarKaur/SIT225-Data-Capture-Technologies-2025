import serial
import json
import firebase_admin
from firebase_admin import credentials, db
import time

# Firebase setup
cred = credentials.Certificate("task5-11149-firebase-adminsdk-fbsvc-e6ef2063b8.json")
firebase_admin.initialize_app(cred, {"databaseURL": "https://task5-11149-default-rtdb.firebaseio.com/"})

ref = db.reference("GyroscopeData")  # Firebase database reference

# Open serial port (adjust COM port accordingly)
ser = serial.Serial("COM16", 115200, timeout=1)

try:
    while True:
        line = ser.readline().decode("utf-8").strip()
        if line:
            try:
                # Split CSV data
                timestamp, x, y, z = line.split(",")
                data = {
                    "timestamp": int(timestamp),
                    "x": float(x),
                    "y": float(y),
                    "z": float(z)
                }

                # Upload data to Firebase
                ref.push(data)
                print(f"Uploaded: {data}")

            except ValueError:
                print("Invalid data format, skipping...")
except KeyboardInterrupt:
    print("Stopping data collection.")
    ser.close()
