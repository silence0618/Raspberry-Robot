import RPi.GPIO as GPIO
import time
import ultrasound
GPIO.setmode(GPIO.BOARD)
GPIO.setup(12,GPIO.OUT)

pwm=GPIO.PWM(12,50)
pwm.start(3.5)
time.sleep(1)
while True:
    for i in [3,6,9]:
        pwm.ChangeDutyCycle(i)
        ultrasound.did()
        time.sleep(0.75)

pwm.stop()
GPIO.cleanup()
