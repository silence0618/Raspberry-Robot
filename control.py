#!/usr/bin/python
import RPi.GPIO as GPIO
from time import sleep
import sys
import os,tty,termios,time

rightf = 11
leftf = 13
rightb = 16
leftb = 15

GPIO.setmode(GPIO.BOARD)
GPIO.setup(leftb, GPIO.OUT)
GPIO.setup(leftf, GPIO.OUT)
GPIO.setup(rightf, GPIO.OUT)
GPIO.setup(rightb, GPIO.OUT)

sleep_time = 0.03


def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch


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

while True:
    char = getch()
    speed = 100
    if(char == 'w'):
        forward()
    if(char == 's'):
        backward()
    if(char == 'a'):
        left()
    if(char == 'd'):
        right()
    if(char == 'q'):
        pivot_left()
    if(char == 'e'):
        pivot_right()
    #if(char == 'c'):
    #    os.system('/home/pi/camera/startstream.sh')
    #if(char == 'x'):
    #    os.system('/home/pi/camera/stopstream.sh')
    if(char == 'f'):
        print("Program Ended")
        break



char = ""
