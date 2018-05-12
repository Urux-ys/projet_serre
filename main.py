#!/usr/bin/env python
import time, os, glob
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from sensors import sensor
from eau import arroser
from lumiere import eclairer, eteindre_lumiere
from temperature import chauffer, stoper_chauffage
wait_time = input("wait time = ")
storage_file = raw_input("storage_file = ")

data = [0]*4
main_data_file = open("data.txt", "a")
session_data_file = open(str(storage_file), "w")

main_data_file.write("\n\n ======= values from new run ======= \n\n")

while True :
	eteindre_lumiere
	for i in range (4):
		data[i]=sensor(i) 
		main_data_file.write(str(data[i]) + " ")
		session_data_file.write(str(data[i]) + " ") 
	main_data_file.write("\n")
	session_data_file.write("\n")
	if data[0] > 5000 :
		eclairer()
	if data[3] > 25000 :
		arroser()
	if data[1] < 3000 :
		chauffer()
	elif data[1] > 3000 :
		stoper_chauffage()
	time.sleep(wait_time)
main_data_file.close()
GPIO.cleanup()


