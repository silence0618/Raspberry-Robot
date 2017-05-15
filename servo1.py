import RPi.GPIO as GPIO
import time

signal = 18

GPIO.setmode(GPIO.BOARD)
GPIO.setup(signal,GPIO.OUT)

pwm = GPIO.PWM(signal,50)
pwm.start(7)
time.sleep(0.5)
for i in range(0,20):
    desiredPosition = input("please input the degree:  ")
    DC = 1./18.*(desiredPosition)+2
    pwm.ChangeDutyCycle(DC)
pwm.stop()
GPIO.cleanup()
