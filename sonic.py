#!/usr/bin/python
import time
import RPi.GPIO as GPIO
import timeit
class sonic:
    def __init__(self,TRIG,ECHO):
        self.TRIG = TRIG
        self.ECHO = ECHO
        GPIO.setmode(GPIO.BOARD)
        GPIO.setwarnings(False)
        GPIO.setup(TRIG,GPIO.OUT)
        GPIO.setup(ECHO,GPIO.IN)
        
    def distance(self):
	time.sleep(0.5)        
        GPIO.output(self.TRIG,1)
        time.sleep(0.00001)
        GPIO.output(self.TRIG,0)
        start=None
        stop=None
        tl=None
        while GPIO.input(self.ECHO) == 0:
            start=time.time()
            
        while GPIO.input(self.ECHO) == 1:
            stop=time.time()

        if start==None or stop==None:
            print "wrong"
            return 0
        tl= stop-start
       
        distance = tl/0.000058
                
        if distance > 100:
            distance = 100
            return distance
        else:
            return distance
if __name__ == "__main__":
    juli=sonic(18,7)
    print(juli.distance())    
