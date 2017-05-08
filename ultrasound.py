##
# 2015-05-16 - Ultrasound code - Reliable
# Maarten Pater (www.mirdesign.nl)
#
# Based on work of Keith Hekker and Matt Hawkins
# Keith: http://khekker.blogspot.nl/2013/03/raspberry-pi-and-monitoring-sump-pump.html
# Matt: http://www.raspberrypi-spy.co.uk/2012/12/ultrasonic-distance-measurement-using-python-part-1/
#
# Buy the device here: http://www.dx.com/p/314393
#
# Example usage at the bottom!
#
##
import RPi.GPIO as GPIO
import time
import datetime

# Pin settings
PIN_ULTRA_SWITCH_ON = GPIO.HIGH
PIN_ULTRA_SWITCH_OFF = GPIO.LOW
PIN_ULTRA_TRIGGER = 29
PIN_ULTRA_ECHO = 22

# Device settings
ULTRA_SLEEP_AFTER_TRIGGER = 0.00001
ULTRA_SLEEP_AFTER_READ_SAPLE = 0.05

# Bad sample settings
BAIL_OUT_THRESHOLD_WAITING_FOR_ECHO = 200	
BAIL_OUT_THRESHOLD_RECEIVING_ECHO = 2500
BAIL_OUT_THRESHOLD_ACCEPT_FAILED_READS = 0

# GPIO initialisation
GPIO.setmode(GPIO.BOARD)
GPIO.setup(PIN_ULTRA_TRIGGER, GPIO.OUT)
GPIO.setup(PIN_ULTRA_ECHO, GPIO.IN)
GPIO.output(PIN_ULTRA_TRIGGER, PIN_ULTRA_SWITCH_OFF)

def GetDistance(NumberOfSamples = 10):
	dDistances = 0
	dCount = 0
	distanceAvg = -1
	
	# Reading samples 
	for x in range(0,NumberOfSamples):
		distance = ReadValue()
		if (distance != -1): # -1 means: No successful run
			dDistances = dDistances + distance
			dCount = dCount + 1
		time.sleep(ULTRA_SLEEP_AFTER_READ_SAPLE) # Give the device some rest

	if (dCount > 0):
		distanceAvg = dDistances / dCount

	return distanceAvg
	
def Diagnose():
	while True:
		distance = ReadValue()
		print "Distance : %.1f (final)" % distance
		
def ReadValue(NumberOfSamples = 10):

	dDistance = 0
	bailOutCount = 0
	
	for x in range(0,NumberOfSamples):
		start = time.time()
		stop = start
	
		# Send 10us pulse to trigger
		GPIO.output(PIN_ULTRA_TRIGGER, PIN_ULTRA_SWITCH_ON)
		time.sleep(ULTRA_SLEEP_AFTER_TRIGGER)
		GPIO.output(PIN_ULTRA_TRIGGER, PIN_ULTRA_SWITCH_OFF)
	
		# We are going to bail out if device takes 
		# to long to provide expected answer
		bailedOut = False
		waitCount = 0
		
		# Wait until the devices is ready send
		# 8 samples on 40khz
		while GPIO.input(PIN_ULTRA_ECHO)==0:
			waitCount = waitCount + 1
			
			# Bail out if we are waiting to long for the 8 signals to end
			if (waitCount > BAIL_OUT_THRESHOLD_WAITING_FOR_ECHO):
				bailOutCount = bailOutCount + 1
				bailedOut = True
				break
			start = time.time()
			stop = start
	
		if (bailedOut == False):
			waitCount = 0
			while GPIO.input(PIN_ULTRA_ECHO)==1:
				waitCount = waitCount + 1
				
				# Bail out if we are waiting to long for the 8 signals to echo
				if (waitCount > BAIL_OUT_THRESHOLD_RECEIVING_ECHO):
					bailOutCount = bailOutCount + 1
					bailedOut = True
					break
				stop = time.time()
			
			if (bailedOut == False):
				elapsed = stop-start
				distance = elapsed * 34300 / 2 # Speed of sound / back and forth

				if x > 0 and distance > 0:
					dDistance = dDistance + distance

	retVal = -1
	
	# Only return a distance if we didn't exceed the number of failed samples
	if(bailOutCount <= BAIL_OUT_THRESHOLD_ACCEPT_FAILED_READS):
		divideBy = (NumberOfSamples-1-bailOutCount)
		if(divideBy > 0):
			retVal = dDistance / divideBy
		
	return retVal

# To show unlimited reads
Diagnose()

# To show just 1 read
print GetDistance()

# Clean up
GPIO.cleanup()
