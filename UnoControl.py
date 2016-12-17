import serial
import re
import time


while 1:
    ttyi = 0
    while ttyi < 10:
        try:
            ser = serial.Serial("/dev/ttyACM" + str(ttyi), 9600)
            print("/dev/ttyACM" + str(ttyi))
            while 1:
                try:
                    print(ser.readline().decode("utf-8"), end='')
                except Exception:
                    pass


        except serial.SerialException:
            ttyi += 1
    print("No Arduino")
    time.sleep(0.1)