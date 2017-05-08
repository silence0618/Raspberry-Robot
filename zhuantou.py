import RPi.GPIO as GPIO
import time
from time import sleep
from ultrasonic import dis
signal = 18
rightf = 11
leftf = 13
rightb = 16
leftb = 15
righte = 40
lefte = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftb, GPIO.OUT)
GPIO.setup(leftf, GPIO.OUT)
GPIO.setup(righte, GPIO.OUT)
GPIO.setup(rightf, GPIO.OUT)
GPIO.setup(rightb, GPIO.OUT)
GPIO.setup(lefte, GPIO.OUT)

Motor1 = GPIO.PWM(righte, 50)
Motor1.start(0)
Motor2 = GPIO.PWM(lefte, 50)
Motor2.start(0)

sleep_time = 0.50

def forward(speed):
    GPIO.output(leftb, False)
    GPIO.output(leftf, True)
    GPIO.output(rightf, True)
    GPIO.output(rightb, False)
    Motor1.ChangeDutyCycle(85)
    Motor2.ChangeDutyCycle(100)
    sleep(sleep_time)
    Motor1.ChangeDutyCycle(0)
    Motor2.ChangeDutyCycle(0)
    print 'forward'
def backward(speed):

    GPIO.output(leftb, True)
    GPIO.output(leftf, False)
    GPIO.output(rightf, False)
    GPIO.output(rightb, True)
    Motor1.ChangeDutyCycle(85)
    Motor2.ChangeDutyCycle(100)
    sleep(sleep_time)
    Motor1.ChangeDutyCycle(0)
    Motor2.ChangeDutyCycle(0)

    print 'backward'
def left(speed):
    GPIO.output(leftb, False)
    GPIO.output(leftf, True)
    GPIO.output(rightb, True)
    GPIO.output(rightf, True)
    Motor1.ChangeDutyCycle(speed)
    Motor2.ChangeDutyCycle(speed)
    sleep(sleep_time)
    Motor1.ChangeDutyCycle(0)
    Motor2.ChangeDutyCycle(0)

    print 'left'
def right(speed):
    GPIO.output(leftb, True)
    GPIO.output(leftf, True)
    GPIO.output(rightf, True)
    GPIO.output(rightb, False)
    Motor1.ChangeDutyCycle(speed)
    Motor2.ChangeDutyCycle(speed)
    sleep(sleep_time)
    Motor1.ChangeDutyCycle(0)
    Motor2.ChangeDutyCycle(0)

    print 'right'
def pivot_left(speed):
    GPIO.output(leftb, False)
    GPIO.output(leftf, True)
    GPIO.output(rightf, False)
    GPIO.output(rightb, True)
    Motor1.ChangeDutyCycle(speed)
    Motor2.ChangeDutyCycle(speed)
    sleep(sleep_time)
    Motor1.ChangeDutyCycle(0)
    Motor2.ChangeDutyCycle(0)

    print 'pivot_left'
def pivot_right(speed):
    GPIO.output(leftb, True)
    GPIO.output(leftf, False)
    GPIO.output(rightf, True)
    GPIO.output(rightb, False)
    Motor1.ChangeDutyCycle(speed)
    Motor2.ChangeDutyCycle(speed)
    sleep(sleep_time)
    Motor1.ChangeDutyCycle(0)
    Motor2.ChangeDutyCycle(0)

    print 'pivot_right'
def stop():
    Motor1.ChangeDutyCycle(0)
    Motor2.ChangeDutyCycle(0)
    GPIO.cleanup()



GPIO.setmode(GPIO.BOARD)
GPIO.setup(signal,GPIO.OUT)
time.sleep(0.5)
pwm = GPIO.PWM(signal,50)
pwm.start(7)
list = [30,90,150,90]
while True:
    for desiredPosition in list:
        #desiredPosition = input("please input the degree:  ")
        forward(100)
        DC = 1./18.*(desiredPosition)+2
        pwm.ChangeDutyCycle(DC)
        time.sleep(0.5)
        if dis() < 50:
            if desiredPosition == 30:
                print "should turn left"
                left(100)
            elif desiredPosition == 90:
                print "Too close"
                backward(100)
                pivot_right(100)
            elif desiredPosition == 150:
                print "should turn right"
                right(100)
        print dis()
pwm.stop()
GPIO.cleanup()
