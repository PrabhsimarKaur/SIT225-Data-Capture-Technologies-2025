from arduino_iot_cloud import ArduinoCloudClient
import threading
import time

# Your credentials for the Python device
DEVICE_ID = "11c0bc30-8a66-4bf5-9a06-d3b77b5a05ab"
SECRET_KEY = "JJKTz#uvJA8eEw5yd#So!BN7m"

# Global variables to store latest accelerometer readings
latest_x, latest_y, latest_z = 0, 0, 0

# Callback functions to handle updates from Arduino Cloud
def on_accelerometer_x_changed(client, value):
    global latest_x
    latest_x = value

def on_accelerometer_y_changed(client, value):
    global latest_y
    latest_y = value

def on_accelerometer_z_changed(client, value):
    global latest_z
    latest_z = value

# Function to return the latest accelerometer readings
def get_latest_accel_data():
    return (latest_x, latest_y, latest_z)

# Function to start the Arduino Cloud client and register variables
def start_arduino_client():

    # Create client with credentials and sync mode
    client = ArduinoCloudClient(device_id=DEVICE_ID, username=DEVICE_ID, password=SECRET_KEY, sync_mode=True)

    # Register variables and their corresponding callback handlers
    client.register("py_x", value=None, on_write=on_accelerometer_x_changed)
    client.register("py_y", value=None, on_write=on_accelerometer_y_changed)
    client.register("py_z", value=None, on_write=on_accelerometer_z_changed)

    # Start the client
    client.start()
    return client

# Function to start a background thread that continuously updates the client
def start_arduino_updater():
    def updater():
        while True:
            try:
                # Start client and keep it running
                client = start_arduino_client()
                while True:
                    client.update()
                    time.sleep(0.05)
            except Exception as e:
                # Handle disconnection and retry after delay
                print("Connection lost. Reconnecting in 5 seconds...")
                time.sleep(5)  # Wait and then reconnect
    
    # Start updater in a daemon thread so it runs in the background
    t = threading.Thread(target=updater)
    t.daemon = True
    t.start()
