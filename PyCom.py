from numpy import array
import serial
from serial import Serial
from tables import DataTypeWarning

ser = Serial('YOUR COMM HERE', 115200)
if not ser.isOpen():
    ser.open()
print('COM4 is open', ser.isOpen())


while True:
    action = input("r=read,  w=write,  q=quit: ")

    if(action == 'r'):

        values = bytearray([1, 0, 1, 0, 5])
        ser.write(values)
        data = ser.readline(5)
        print(list(data))

    elif(action == 'w'):
        values = bytearray([1, 1, 0, 0, 57])
        ser.write(values)
        
    elif(action == 'q'):
        print("quit: so long, partner!")
        exit()
