import serial
import random
import time

ser = serial.Serial('COM13', 9600)  

while True:
  num = random.randint(1, 10)  

  print(f"Sending {num} to Arduino at {time.strftime('%Y-%m-%d %H:%M:%S')}")

  ser.write(str(num).encode()) 
  
  time.sleep(1)  

  arduino_num = ser.readline().decode().strip()

  print(f"Received {arduino_num} from Arduino at {time.strftime('%Y-%m-%d %H:%M:%S')}")

  time.sleep(int(arduino_num) / 1000)  

  print(f"Wait was over at {time.strftime('%Y-%m-%d %H:%M:%S')}")
