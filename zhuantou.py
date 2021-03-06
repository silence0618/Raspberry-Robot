import RPi.GPIO as GPIO
import time
from time import sleep
from ultrasonic import dis
signal = 18
rightf = 11
leftf = 13
rightb = 16
leftb = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftb, GPIO.OUT)
GPIO.setup(leftf, GPIO.OUT)
GPIO.setup(rightf, GPIO.OUT)
GPIO.setup(rightb, GPIO.OUT)

sleep_time = 0.30

def forward():
    GPIO.output(leftb, False)
    GPIO.output(leftf, True)
    GPIO.output(rightf, True)
    GPIO.output(rightb, False)
    sleep(sleep_time)
    stop()
    print 'forward'
def backward():
    GPIO.output(leftb, True)
    GPIO.output(leftf, False)
    GPIO.output(rightf, False)
    GPIO.output(rightb, True)
    sleep(sleep_time)
    stop()
    print 'backward'
def left():
    GPIO.output(leftb, False)
    GPIO.output(leftf, True)
    GPIO.output(rightb, True)
    GPIO.output(rightf, True)
    sleep(sleep_time)
    stop()
    print 'left'
def right():
    GPIO.output(leftb, True)
    GPIO.output(leftf, True)
    GPIO.output(rightf, True)
    GPIO.output(rightb, False)
    sleep(sleep_time)
    stop()
    print 'right'
def pivot_left():
    GPIO.output(leftb, False)
    GPIO.output(leftf, True)
    GPIO.output(rightf, False)
    GPIO.output(rightb, True)
    sleep(sleep_time)
    stop()
    print 'pivot_left'
def pivot_right():
    GPIO.output(leftb, True)
    GPIO.output(leftf, False)
    GPIO.output(rightf, True)
    GPIO.output(rightb, False)
    sleep(sleep_time)
    stop()
    print 'pivot_right'
def stop():
    GPIO.output(leftb,False)
    GPIO.output(leftf,False)
    GPIO.output(rightf,False)
    GPIO.output(rightb,False)


GPIO.setmode(GPIO.BOARD)
GPIO.setup(signal,GPIO.OUT)
time.sleep(0.5)
pwm = GPIO.PWM(signal,50)
pwm.start(7)
list = [30,90,150,90]
while True:
    for desiredPosition in list:
        #desiredPosition = input("please input the degree:  ")
        forward()
        DC = 1./18.*(desiredPosition)+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.5)
        if dis() < 30:
            if desiredPosition == 30:
                print "should turn left"
                left()
            elif desiredPosition == 90:
                print "Too close"
                backward()
                pivot_right()
            elif desiredPosition == 150:
                print "should turn right"
                right()
        print dis()
pwm.stop()
GPIO.cleanup()
