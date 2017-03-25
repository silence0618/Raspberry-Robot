#!/usr/bin/python
import time
import RPi.GPIO as GPIO
def distance():
    TRIG = 18
    ECHO = 22
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BOARD)

    GPIO.setup(TRIG,GPIO.OUT)

    GPIO.setup(ECHO,GPIO.IN)

    GPIO.output(TRIG,1)
    time.sleep(0.1)
    GPIO.output(TRIG,0)
    while GPIO.input(ECHO) == 0:
        start=time.time()
    while GPIO.input(ECHO) == 1:
        stop = time.time()

    tl= stop-start
    distance = tl/0.000058
    if distance > 100:
        distance == 100
    else:
#        GPIO.cleanup()
        return distance
    print distance
print distance()
