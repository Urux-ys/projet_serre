from sensors import value
import time 
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import os
import glob

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def eau():
	if sensors.value(4)<1500:
		GPIO.output(11,GPIO.HIGH)

if __name__ == "__main__":
	while True :
		GPIO.output(11, GPIO.HIGH)
		time.sleep(0.1)
		GPIO.output(11, GPIO.LOW)
		time.sleep(0.1)
