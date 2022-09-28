import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BCM)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(18, GPIO.IN)
k = GPIO.input(18)

if k == 1:
    GPIO.output(14, 1)
else:
    GPIO.output(14, 0)

sleep(5)

k = GPIO.input(18)

if k == 1:
    GPIO.output(14, 1)
else:
    GPIO.output(14, 0)

sleep(5)

k = GPIO.input(18)

if k == 1:
    GPIO.output(14, 1)
else:
    GPIO.output(14, 0)

sleep(5)

k = GPIO.input(18)

if k == 1:
    GPIO.output(14, 1)
else:
    GPIO.output(14, 0)