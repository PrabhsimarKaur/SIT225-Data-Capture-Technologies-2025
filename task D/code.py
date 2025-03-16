import paho.mqtt.client as mqtt
from pymongo import MongoClient
import json
import ssl

# MQTT Configuration
MQTT_BROKER = "0780d8e6b2414b3ea5be0f41d018441b.s1.eu.hivemq.cloud"  # HiveMQ Cloud Broker
MQTT_PORT = 8883  # Secure MQTT port
MQTT_TOPIC = "gyro/data"
MQTT_USER = "hivemq.webclient.1742109140513"  # Replace with your HiveMQ username
MQTT_PASSWORD = "5@>93HDb8RhTJaf:P%xr"  # Replace with your HiveMQ password

# MongoDB Configuration
MONGO_URI = "mongodb://localhost:27017/"
DATABASE_NAME = "sensor_data"
COLLECTION_NAME = "gyroscope_readings"

# Connect to MongoDB
try:
    mongo_client = MongoClient(MONGO_URI)
    db = mongo_client[DATABASE_NAME]
    collection = db[COLLECTION_NAME]
    print("✅ Connected to MongoDB")
except Exception as e:
    print(f"❌ Failed to connect to MongoDB: {e}")
    exit()

# Callback when the client connects
def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("✅ Connected to MQTT Broker!")
        client.subscribe(MQTT_TOPIC)
    else:
        print(f"❌ Connection failed with error code {rc}")

# Callback when a message is received
def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())  # Convert to JSON
        print(f"📩 Received Data: {data}")

        # Ensure data is valid before inserting
        if isinstance(data, dict):
            collection.insert_one(data)
            print("✅ Data Inserted into MongoDB")
        else:
            print("⚠️ Received data is not a valid JSON object.")

    except json.JSONDecodeError:
        print("❌ Error decoding JSON from MQTT message")
    except Exception as e:
        print(f"❌ Error inserting into MongoDB: {e}")

# Setup MQTT Client with TLS
mqtt_client = mqtt.Client()
mqtt_client.username_pw_set(MQTT_USER, MQTT_PASSWORD)

# Configure TLS for secure connection
mqtt_client.tls_set(cert_reqs=ssl.CERT_NONE)

mqtt_client.on_connect = on_connect
mqtt_client.on_message = on_message

# Connect to MQTT Broker
try:
    print("🔄 Connecting to MQTT broker...")
    mqtt_client.connect(MQTT_BROKER, MQTT_PORT, 60)
except Exception as e:
    print(f"❌ Failed to connect to MQTT broker: {e}")
    exit()

# Start listening for messages (non-blocking)
mqtt_client.loop_start()

try:
    while True:
        pass  # Keep the script running
except KeyboardInterrupt:
    print("\n🛑 Stopping script...")
    mqtt_client.loop_stop()
    mqtt_client.disconnect()
    print("✅ Disconnected from MQTT Broker.")
def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())  # Convert to JSON
        print(f"📩 Received Data: {data}")

        # Store in MongoDB
        result = collection.insert_one(data)
        print(f"✅ Data Inserted into MongoDB with ID: {result.inserted_id}")

    except Exception as e:
        print(f"❌ Error inserting into MongoDB: {e}")
