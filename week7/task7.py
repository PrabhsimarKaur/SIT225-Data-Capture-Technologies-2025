import serial
import csv
from datetime import datetime

# Initialize serial connection (adjust 'COM3' and baud rate as needed)
ser = serial.Serial('COM16', 9600, timeout=1)

# Create/Open CSV file in append mode
with open('data.csv', 'a', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    # Write header if file is empty
    if csvfile.tell() == 0:
        csvwriter.writerow(['Timestamp', 'Temperature', 'Humidity'])

    try:
        print("Logging data... Press Ctrl+C to stop.")
        while True:
            # Read line from serial and decode
            line = ser.readline().decode('utf-8').strip()
            if line:
                data = line.split(',')
                if len(data) == 2:  # Ensure correct data format
                    # Get current timestamp
                    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                    temperature = float(data[0])
                    humidity = float(data[1])
                    print(f"{timestamp} - Temp: {temperature}C, Hum: {humidity}%")
                    # Write to CSV
                    csvwriter.writerow([timestamp, temperature, humidity])
                    csvfile.flush()  # Ensure data is written immediately
                    # Print confirmation
                    print(f"Stored: {timestamp}, {temperature}C, {humidity}%")
    except KeyboardInterrupt:
        print("Data logging stopped by user.")
    finally:
        ser.close()
