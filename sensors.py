#!/usr/bin/env python

import time
import Adafruit_ADS1x15

def sensors_values(sensor) :
    adc = Adafruit_ADS1x15.ADS1115()
    GAIN = 1
    value = adc.read_adc(sensor, gain=GAIN)
    return value


if __name__ == "__main__" :
    sensor = input()
    print sensors_values(sensor)











