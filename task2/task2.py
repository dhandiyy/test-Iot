import serial
import time

# ganti 'COM5' dengan Port yang sesuai
baudRate = 115200
ser = serial.Serial('COM5', baudRate)

def led_on():
    ser.write(b'1') 

def led_off():
    ser.write(b'0')

# perulangan akan terjadi 10 kali
countLooping = 10;
for x in range(countLooping):
  led_on()
  time.sleep(2)
  led_off()
  time.sleep(1)