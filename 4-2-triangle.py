import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)
dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setup(dac, GPIO.OUT)

def decimalToBinary(number):
    return [int(i) for i in bin(number)[2:].zfill(8)]

try:
    while True: 
        n = int(input("Please, enter period:"))
        t = n / 512
        for i in range(256):
            GPIO.output(dac, decimalToBinary(i))
            sleep(t)
        for i in range(255, -1, -1):
            GPIO.output(dac, decimalToBinary(i))
            sleep(t)
finally:
    GPIO.output(dac, 0)
    GPIO.cleanup()