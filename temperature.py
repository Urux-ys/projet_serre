from Adafruit_ADS1x15 import ADS1x15
from time import sleep
 
# Weitere benoetigte Module werden importiert und eingerichtet
import time, signal, sys, os, math
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
 
# Benutzte Variablen werden initialisiert
delayTime = 0.2
 
# Adresszuweisung ADS1x15 ADC
 
ADS1015 = 0x00  # 12-bit ADC
ADS1115 = 0x01  # 16-bit
 
# Verstaerkung (Gain) wird ausgewaehlt
gain = 4096  # +/- 4.096V
# gain = 2048  # +/- 2.048V
# gain = 1024  # +/- 1.024V
# gain = 512   # +/- 0.512V
# gain = 256   # +/- 0.256V
 
# Abtasterate des ADC (SampleRate) wird ausgewaehlt
# sps = 8    # 8 Samples pro Sekunde
# sps = 16   # 16 Samples pro Sekunde
# sps = 32   # 32 Samples pro Sekunde
# sps = 64   # 64 Samples pro Sekunde
# sps = 128  # 128 Samples pro Sekunde
# sps = 250  # 250 Samples pro Sekunde
# sps = 475  # 475 Samples pro Sekunde
sps = 860  # 860 Samples pro Sekunde
 
# ADC-Channel (1-4) wird ausgewaehlt
adc_channel = 0    # Channel 0
# adc_channel = 1    # Channel 1
# adc_channel = 2    # Channel 2
# adc_channel = 3    # Channel 3
 
# Hier wird der ADC initialisiert - beim KY-053 verwendeten ADC handelt es sich um einen ADS1115 Chipsatz
adc = ADS1x15(ic=ADS1115)
 
#############################################################################################################
 
# ########
# Hauptprogrammschleife
# ########
# Das Programm misst mit Hilfe des ADS1115 ADC den aktuellen Spannungswert am ADC,
# berechnet daraus den aktuellen Widerstand des NTC, berechnet mit Hilfe vorab für diesen Sensor bestimmter Werte
# die Temperatur und gibt diese in die Konsole aus
 
try:
        while True:
                #Aktuelle Werte werden aufgenommen...
                voltage = adc.readADCSingleEnded(adc_channel, gain, sps)
                # ... umgerechnet ...
                temperatur = math.log((10000/voltage)*(3300-voltage))
                temperatur = 1 / (0.001129148 + (0.000234125 + (0.0000000876741 * temperatur * temperatur)) * temperatur);
                temperatur = temperatur - 273.15;
                # ... und ausgegeben
                print "Temperatur:", temperatur,"°C"
                print "---------------------------------------"
 
                # Delay
                time.sleep(delayTime)
 
 
 
except KeyboardInterrupt:
        GPIO.cleanup()
