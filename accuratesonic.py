#!/usr/bin/env python

# 2014-08-18 hc-sr04.py

import time

import pigpio

TRIGGER=18
ECHO=7

high_tick = None # global to hold high tick.

class sonic:
    def __init__(self,TRIG,ECHO):
        self.TRIGGER=TRIGGER
        self.ECHO=ECHO
        self.high_tick = high_tick
        pi = pigpio.pi() # Connect to local Pi.

        pi.set_mode(self.TRIGGER, pigpio.OUTPUT)
        pi.set_mode(self.ECHO, pigpio.INPUT)

    def cbfunc(self,gpio, level, tick):
        print(gpio,level,tick)
        
        global high_tick        
        
        tick
        if level == 0: # echo line changed from high to low.
            if high_tick is not None:
                self.echo = pigpio.tickDiff(self.high_tick, tick)
                print(self.echo)
                cms = (self.echo / 1000000.0) * 34030 / 2
                print("echo was {} micros long ({:.1f} cms)".format(self.echo, cms))
#                return cms

            else:
                high_tick = tick
                print "error"

'''
pi = pigpio.pi() # Connect to local Pi.

pi.set_mode(TRIGGER, pigpio.OUTPUT)
pi.set_mode(ECHO, pigpio.INPUT)
'''
if __name__ =="__main__":
    juli = sonic(18,7)
    pi = pigpio.pi()
    cb = pi.callback(ECHO, pigpio.EITHER_EDGE, juli.cbfunc)
    start=time.time()
#    juli.cbfunc(18,0,start)    
    

    while (time.time()-start) < 60:
        pi.gpio_trigger(TRIGGER, 10)
        time.sleep(0.1)

    cb.cancel() # Cancel callback.
    pi.stop() # Close connection to Pi

