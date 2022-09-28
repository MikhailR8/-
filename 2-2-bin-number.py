import RPi.GPIO as GPIO
from time import sleep
from random import randint
from matplotlib import pyplot 

dac = [26, 19, 13, 6, 5, 11, 9, 10]
numbers = [0] * 8
voltages = []

GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

for i in range(7):
    number = int(input())
    n = bin(number)[2:]
    print(n)
    for j in range(1, len(n) + 1):
        if j <= len(numbers):
            numbers[-j] = int(n[-j])
    print(numbers)
    GPIO.output(dac, numbers)
    inputv = input("Please, input a voltage:")
    GPIO.output(dac, 0)
    for j in range(len(numbers)):
        numbers[j] = 0
    voltages.append((number, inputv))

voltages.sort()
xs = [x for x, y in voltages]
ys = [y for x, y in voltages]
pyplot.scatter(xs, ys)
pyplot.show()



print(numbers)

GPIO.cleanup()