import RPi.GPIO as GPIO
import time
import ultrasonic as ultra
signal = 18
GPIO.setmode(GPIO.BOARD)
GPIO.setup(signal,GPIO.OUT)

pwm=GPIO.PWM(signal,50)
pwm.start(7)
time.sleep(1)
pwm.ChangeDutyCycle(4)
time.sleep(1)
pwm.ChangeDutyCycle(5)
time.sleep(1)
pwm.ChangeDutyCycle(6)
time.sleep(1)
pwm.ChangeDutyCycle(7)
time.sleep(1)
pwm.ChangeDutyCycle(8)
time.sleep(1)
pwm.ChangeDutyCycle(9)
time.sleep(1)
pwm.stop()
GPIO.cleanup()
