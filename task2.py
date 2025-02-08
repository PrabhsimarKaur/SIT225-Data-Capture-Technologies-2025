import serial
import csv
import time


arduino = serial.Serial('COM14', 9600)  


with open('sensor_data.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
  
    writer.writerow(['Timestamp', 'Humidity (%)', 'Temperature (C)'])
    
    print("Starting data collection...")

    
    for i in range(100):  
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

    print("Data collection finished.")
