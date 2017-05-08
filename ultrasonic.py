import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

TRIG = 29
ECHO = 22

#print "Distance Measurement In Progress"

GPIO.setup(TRIG,GPIO.OUT)
GPIO.setup(ECHO,GPIO.IN)

def dis():
    GPIO.output(TRIG, False)
    time.sleep(0.010)
    GPIO.output(TRIG, True)
    time.sleep(0.000011)
    GPIO.output(TRIG,False)
    while GPIO.input(ECHO)==0:
        pulse_start = time.time()
    while GPIO.input(ECHO)==1:
        pulse_end = time.time()
    pulse_duration = pulse_end - pulse_start
    distance = pulse_duration * 17150
    distance = round(distance, 2)
    return distance
print dis()
#print "Distance:",distance,"cm"


#GPIO.cleanup()
