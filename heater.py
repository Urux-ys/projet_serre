#!/usr/bin/env python
import os
import glob
from Adafruit_ADS1x15 import ADS1x15
from time import sleep
from sensors import sensor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)

def heater_on() :
	GPIO.output(15, GPIO.HIGH)

def heater_off() :
	GPIO.output(15, GPIO.LOW)


