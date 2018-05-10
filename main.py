#!/usr/bin/env python
import time, os, glob
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from sensors import sensor
from eau import arroser
#from lumiere import eclairer, eteindre_lumiere
#from temperature import chauffer, stoper_chauffage

data = [0]*4
data_file = open("data.txt", "a")
while True :
#	eteindre_lumiere
	for i in range (4):
		data[i]=sensor(i) 
	data_file.write('{0:>6}  {1:>6}  {2:>6}  {3:>6}'.format(*data))
	data_file.write("\n")
#	if data[0] > 5000 :
#		eclairer()
	if data[3] > 25000 :
		arroser(0.05)
#	if data[1] < 3000 :
#		chauffer()
#	elif data[1] > 3000 :
#		stoper_chauffage()
	
data_file.close()
