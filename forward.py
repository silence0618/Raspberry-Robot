import RPi.GPIO as GPIO
import time

rightf = 11
leftf = 13
rightb = 16
leftb = 15


GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftb, GPIO.OUT)
GPIO.setup(leftf, GPIO.OUT)
GPIO.setup(rightf, GPIO.OUT)
GPIO.setup(rightb, GPIO.OUT)


sleep_time = 1

GPIO.output(leftf,False)
GPIO.output(leftb,True)
time.sleep(sleep_time)
GPIO.cleanup()
