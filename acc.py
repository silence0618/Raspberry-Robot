#!/usr/bin/env python

# 2014-08-18 hc-sr04.py
import RPi.GPIO as GPIO
import time

import pigpio

TRIGGER=18
ECHO=7
GPIO.setmode(GPIO.BOARD)
GPIO.setup(22,GPIO.OUT)
pwm=GPIO.PWM(22,50)
pwm.start(3.5)
time.sleep(1)
high_tick = None # global to hold high tick.

def cbfunc(gpio, level, tick):
   global high_tick
   if level == 0: # echo line changed from high to low.
      if high_tick is not None:
         
         echo = pigpio.tickDiff(high_tick, tick)
         cms = (echo / 1000000.0) * 34030 / 2
         print("echo was {} micros long ({:.1f} cms)".format(echo, cms))
                  
   else:
       high_tick = tick

pi = pigpio.pi() # Connect to local Pi.

pi.set_mode(TRIGGER, pigpio.OUTPUT)
pi.set_mode(ECHO, pigpio.INPUT)

cb = pi.callback(ECHO, pigpio.EITHER_EDGE, cbfunc)

start = time.time()

while (time.time()-start) < 60:
   pi.gpio_trigger(TRIGGER, 10)
   time.sleep(0.75)
   for i in [3,6,9]:
       pwm.ChangeDutyCycle(i)   
cb.cancel() # Cancel callback.
pi.stop() # Close connection to Pi
