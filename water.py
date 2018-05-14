#!/usr/bin/env python
from sensors import sensor
import time 
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
import os
import glob

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)

def water_on():
	GPIO.output(11, GPIO.HIGH)
def water_off() :		
	GPIO.output(11, GPIO.LOW)

'''
if __name__ == "__main__":
	while True :
		tmp = float(sensor(2))/5000
		print sensor(2)
		GPIO.output(11, GPIO.HIGH)	
		time.sleep(tmp)
		GPIO.output(11, GPIO.LOW)
		time.sleep(tmp)	
'''	
