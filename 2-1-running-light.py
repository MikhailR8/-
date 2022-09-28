import RPi.GPIO as GPIO
from time import sleep

leds = [21, 20, 16, 12, 7, 8, 25, 24]
GPIO.setmode(GPIO.BCM)

GPIO.setup(leds, GPIO.OUT)

for i in range(3): 
    for j in range(len(leds)):
         GPIO.output(leds[j], 1)
         sleep(0.2)
         GPIO.output(leds[j], 0)

GPIO.output(leds, 0)
GPIO.cleanup()
