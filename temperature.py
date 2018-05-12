#!/usr/bin/env python
import os
import glob
from Adafruit_ADS1x15 import ADS1x15
from time import sleep
from sensors import sensor
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
GPIO.setup(15,GPIO.OUT)

def chauffer() :
	GPIO.output(15, GPIO.HIGH)

def stoper_chauffage() :
	GPIO.output(15, GPIO.LOW)


