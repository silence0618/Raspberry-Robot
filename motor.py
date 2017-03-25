#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)

GPIO.setup(16, GPIO.OUT)  # N4 right forward
GPIO.setup(11, GPIO.OUT)  # N3 right back
GPIO.setup(40, GPIO.OUT)  # PWM right
GPIO.setup(13, GPIO.OUT)  # N2 left back
GPIO.setup(15, GPIO.OUT)  # N1 left forward
GPIO.setup(38, GPIO.OUT)  # PWM left

Motor1 = GPIO.PWM(40, 50)
Motor1.start(0)
Motor2 = GPIO.PWM(38, 50)
Motor2.start(0)

def forward(speed):
    GPIO.output(16, True)
    GPIO.output(11, False)
    GPIO.output(15, True)
    GPIO.output(13, False)
    Motor1.ChangeDutyCycle(speed)
    Motor2.ChangeDutyCycle(speed)
    print 'forward'
def backward(speed):
    GPIO.output(16, False)
    GPIO.output(11, True)
    GPIO.output(15, False)
    GPIO.output(13, True)
    Motor1.ChangeDutyCycle(speed)
    Motor2.ChangeDutyCycle(speed)
    print 'backward'
def left(speed):
    GPIO.output(16, True)
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(13, False)
    Motor1.ChangeDutyCycle(speed)
    Motor2.ChangeDutyCycle(speed)
    print 'left'
def right(speed):
    GPIO.output(16, False)
    GPIO.output(11, False)
    GPIO.output(15, True)
    GPIO.output(13, False)
    Motor1.ChangeDutyCycle(speed)
    Motor2.ChangeDutyCycle(speed)
    print 'right'
def pivot_left(speed):
    GPIO.output(16, True)
    GPIO.output(11, False)
    GPIO.output(15, False)
    GPIO.output(13, True)
    Motor1.ChangeDutyCycle(speed)
    Motor2.ChangeDutyCycle(speed)
    print 'pivot_left'
def pivot_right(speed):
    GPIO.output(16, False)
    GPIO.output(11, True)
    GPIO.output(15, True)
    GPIO.output(13, False)
    Motor1.ChangeDutyCycle(speed)
    Motor2.ChangeDutyCycle(speed)
    print 'pivot_right'


def stop():
    Motor1.ChangeDutyCycle(0)
    Motor2.ChangeDutyCycle(0)
    GPIO.cleanup()



pivot_left(100)
sleep(1)
pivot_right(100)
sleep(1)
forward(100)
sleep(1)
backward(100)
sleep(1)
left(100)
sleep(1)
right(100)
sleep(1)
stop()
