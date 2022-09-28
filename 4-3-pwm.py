import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)
GPIO.setup(22, GPIO.OUT)
GPIO.setup(25, GPIO.OUT)

p = GPIO.PWM(22, 1000)
p1 = GPIO.PWM(25, 1000)
p.start(0)
p1.start(0)

try:
    while True:
        num = int(input("Please, input duty cycle(from 0 to 100):"))
        if num == -1:
            break
        print("Target voltage: {:.4f} volts".format(3.3 * num / 100))
        p.stop()
        p1.stop()
        p.start(num)
        p1.start(num)
finally:
    p.stop()
    p1.stop()
    GPIO.cleanup()