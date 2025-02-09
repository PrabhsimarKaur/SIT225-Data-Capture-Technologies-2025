import serial
import csv
import time

arduino = serial.Serial('COM20', 9600)
time.sleep(2)  


with open('sensor_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
 
    writer.writerow(['Timestamp', 'Humidity (%)', 'Temperature (C)'])
    
    print("Starting data collection...")


    end_time = time.time() + 1800 

    
    while time.time() < end_time:
        if arduino.in_waiting > 0:
            line = arduino.readline().decode('utf-8').strip()
            timestamp = time.time() 
            
           
            data = line.split(",")
            if len(data) == 2:  
                humidity = data[0]
                temperature = data[1]
                
                
                writer.writerow([timestamp, humidity, temperature])
                
             
                print(f"Timestamp: {timestamp}, Humidity: {humidity}%, Temperature: {temperature}C")
        

        time.sleep(1)  

    print("Data collection finished.")
