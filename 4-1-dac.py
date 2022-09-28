import RPi.GPIO as GPIO
from time import sleep

dac = [26, 19, 13, 6, 5, 11, 9, 10]
GPIO.setmode(GPIO.BCM)
GPIO.setup(dac, GPIO.OUT)

def decimalToBinary(number):
    return [int(i) for i in bin(number)[2:].zfill(8)]

while True:
    try:
        num = input("Please, enter a number from 0 to 255:")
        if(num == 'q'):
            break
        intNum = int(num)
        if(intNum < 0 or intNum > 255):
            print("Please, input number FROM 0 TO 255")
            continue
        GPIO.output(dac, decimalToBinary(intNum))
        print("Target voltage: {:.4f} volts".format(3.3 / 256.0 * intNum))
        sleep(3)
    except ValueError:
        print("Please, input a WHOLE NUMBER")
    finally:
        GPIO.output(dac, 0)
GPIO.cleanup()