#!/usr/bin/env python

import os
import glob
import time
import RPi.GPIO as GPIO

os.system('modprobe w1-gpio')
os.system('modprobe w1-therm')

toto = '/sys/bus/w1/devices/'
tata = glob.glob(toto + '10*')[0]
device_file = tata + '/w1_slave'
GPIO.cleanup()
GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
GPIO.setup(13,GPIO.OUT)
GPIO.setup(12,GPIO.IN, pull_up_down = GPIO.PUD_DOWN)

cap = GPIO.PWM(13,5)
derg_temp = 0.0

def but (channel) :
    print ( 'votre temperature est de : %.02f degres \n trop chaud de %.02f degres'%( derg_temp,derg_temp - 23.5))

GPIO.add_event_detect (12, GPIO.RISING, callback = but, bouncetime = 300 )

while True:
    f = open(device_file , 'r')
    lines = f.readlines()
    f.close()
    if lines[0].strip()[-3:] != 'YES' :
       # print('capteur non connecte')
        cap.start(50)
        GPIO.output(11,GPIO.LOW)
    else :
        cap.stop()
        temp = lines[1].find('t=')
        if temp != -1 :
            val_temp = lines[1][temp+2:]
            derg_temp = float(val_temp) / 1000.0
            if derg_temp > 23.5 :
                #print ('trop chaud de %.02f degres' %(derg_temp - 23.5) )
                GPIO.output(11,GPIO.HIGH)
            else :
                 GPIO.output(11,GPIO.LOW)
                
    time.sleep(1)
