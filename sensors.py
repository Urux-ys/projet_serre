#!/usr/bin/env python

import time
import Adafruit_ADS1x15

def sensor(sensor) :
    adc = Adafruit_ADS1x15.ADS1115()
    GAIN = 1
    value = adc.read_adc(sensor, gain=GAIN)
    return value


if __name__ == "__main__" :
    while True :
        values = [0]*4
        for i in range (4):
            values[i]=sensor(i)
        print('| {0:>6} | {1:>6} | {2:>6} | {3:>6} |'.format(*values))
        time.sleep(0.5)















