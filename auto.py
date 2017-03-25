#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import sys
import os,tty,termios,time
import ultrasound

rightf = 15
leftf = 16
rightb = 13
leftb = 11
righte = 40
lefte = 38

GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftb, GPIO.OUT)
GPIO.setup(leftf, GPIO.OUT)
GPIO.setup(righte, GPIO.OUT)
GPIO.setup(rightf, GPIO.OUT)
GPIO.setup(rightb, GPIO.OUT)
GPIO.setup(lefte, GPIO.OUT)

Motor1 = GPIO.PWM(righte, 1000)
Motor1.start(0)
Motor2 = GPIO.PWM(lefte, 1000)
Motor2.start(0)

sleep_time = 0.050


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


def forward(speed):
    GPIO.output(leftb, False)
    GPIO.output(leftf, True)
    GPIO.output(rightf, True)
    GPIO.output(rightb, False)
    Motor1.ChangeDutyCycle(100)
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

def automation():
    GPIO.setmode(GPIO.BOARD)
    GPIO.setup(12,GPIO.OUT)

    pwm=GPIO.PWM(12,50)
    pwm.start(3.5)
    time.sleep(1)
    frontdis = None
    rightdis = None
    leftdis = None
    while True:
        for i in [3,6,9]:
            pwm.ChangeDutyCycle(i)
            juli=ultrasound.did()
            
            time.sleep(0.3)
            
 #           print i
            
            if i==3:
  #              print i
                
                rightdis = juli
                print "rightdistance is ", rightdis
            elif i==6:
   #             print i
                frontdis = juli
                print "frontdistance is ", frontdis
                
            elif i==9:
    #            print i
                leftdis=juli
                print "Left distance is ", leftdis
            else:
                print "error....."
#                time.sleep(0.1)
            if frontdis < 10:
                backward(speed)
#                time.sleep(0.5)
                if rightdis > leftdis:
                    pivot_right(speed)
                    time.sleep(0.5)
                elif leftdis > rightdis:
                    pivot_left(speed)
                    time.sleep(0.5)
            
            else:
                forward(speed)
                time.sleep(0.5)
    pwm.stop()


while True:
    char = getch()
    speed = 100
    if(char == 'w'):
        forward(speed)
    if(char == 's'):
        backward(speed)
    if(char == 'a'):
        left(speed)
    if(char == 'd'):
        right(speed)
    if(char == 'q'):
        pivot_left(speed)
    if(char == 'e'):
        pivot_right(speed)
    if(char == 'u'):
        automation()
    #if(char == 'c'):
    #    os.system('/home/pi/camera/startstream.sh')
    #if(char == 'x'):
    #    os.system('/home/pi/camera/stopstream.sh')
    if(char == 'f'):
        print("Program Ended")
        break


Motor1.ChangeDutyCycle(0)
Motor2.ChangeDutyCycle(0)

char = ""
