#!/usr/bin/env python
import time, os, glob
import Adafruit_ADS1x15
import RPi.GPIO as GPIO
from sensors import sensor
from water import arroser
from light import light_on, light_off
from heater import heater_on, heater_off

# setting up GPIO 
GPIO.setmode(GPIO.BOARD) # using GPIO with board number
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(15,GPIO.OUT)

SETTINGS = {
	"light_threshold": 		5000,
	"heater_threshold": 		3000,
	"humidity_threshold": 		30000, 
	"wait_time":			60,
	"main_storage_file":		"log.txt",
	"session_storage_file":		"data",
}

os.system("clear")
SETTINGS["session_storage_file"] = raw_input("storage_file = ")
SETTINGS["wait_time"] = input("wait time = ")

data = [0]*4
main_data_file = open("data.txt", "a")
session_data_file = open(str(storage_file), "w")
main_data_file.write("\n\n ======= values from new run ======= \n\n")

while True :

	for i in range (4):
		data[i]=sensor(i) 
		main_data_file.write(str(data[i]) + " ")
		session_data_file.write(str(data[i]) + " ") 
	main_data_file.write("\n")
	session_data_file.write("\n")

	print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*data))		


	if data[0] > SETTINGS["light_threshold"] :
		light_on()
	else :
		light_off()	
	if data[1] < SETTINGS["heater_threshold"] :
		heater_on()
	else :
		heater_off()
	if data[3] > SETTINGS["humidity_threshold"] :
		water_on()
	else :
		water_off


	time.sleep(SETTINGS["wait_time"])


main_data_file.close()
GPIO.cleanup()


