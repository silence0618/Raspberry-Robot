import RPi.GPIO as GPIO
import time
import acc 
import pigpio
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

TRIGGER=18
ECHO=12

high_tick = None 

pwm=GPIO.PWM(12,50)
pwm.start(3.5)
time.sleep(1)
while True:
    for i in [3,6,9]:
        pwm.ChangeDutyCycle(i)
#        juli=dis
#        print dis
        juli = acc.sonic(18,22)
        pi = pigpio.pi()
        cb = pi.callback(ECHO, pigpio.EITHER_EDGE, juli.cbfunc)

        start = time.time()

        if time.time()-start < 60:
            pi.gpio_trigger(TRIGGER, 10)
            time.sleep(0.1)
        pwm.ChangeDutyCycle(i)
        cb.cancel() # Cancel callback.
        pi.stop() # Close connection to Pi
        time.sleep(0.75)
        print i

pwm.stop()
GPIO.cleanup()
