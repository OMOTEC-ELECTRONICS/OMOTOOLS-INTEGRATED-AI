#pip install opencv-python
#Pip install pyserial

import serial
import time

arduino_ide = serial.Serial('com6', 9600) #Change the port name as per arduino port 
time.sleep(2)  # Wait for the communication to get established

print("Enter 1 to turn LED ON or 0 to turn LED OFF")

while True:
    var = input("Enter your choice: ")  # Wait for user input
    print(var)
    
    if var == '1':
        arduino_ide.write(b'1')  # Send '1' to turn LED ON
        print("LED turned Off")
    elif var == '0':
        arduino_ide.write(b'0')  # Send '0' to turn LED OFF
        print("LED turned On")
    else:
        print("Invalid input")
