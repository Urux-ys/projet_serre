#!/usr/bin/env python
import os
import glob
from Adafruit_ADS1x15 import ADS1x15
from time import sleep
from sensors import sensor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(13,GPIO.OUT)

def light_on() :
	GPIO.output(13, GPIO.HIGH)

def light_off() :
	GPIO.output(13, GPIO.LOW)

