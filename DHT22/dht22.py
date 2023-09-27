import wiringpi
from wiringpi import GPIO

#import RPi.GPIO as GPIO
# import dht
import dht
import time
import datetime

# initialize GPIO
# PIN2 = port.PA1
# gpio.init()
wiringpi.wiringPiSetup()
# wiringpi.pinMode(1, GPIO.INPUT)

# read data using pin
# instance = dht.DHT(pin=PIN2)
instance = dht.DHT(pin=0)
tmp=0.0
hum=0.0

def getTmpAndHum():
    while True:
        result = instance.read()
        if tmp!=0 and hum!=0.0:
            print("Last valid input: " + str(datetime.datetime.now()))
            print("Temperature: {0:0.1f} C".format(tmp))
            print("Humidity: {0:0.1f} %%".format(hum))
        if result.is_valid():
            tmp=result.temperature
            hum=result.humidity
            # print("Last valid input: " + str(datetime.datetime.now()))
            # print("Temperature: {0:0.1f} C".format(tmp))
            # print("Humidity: {0:0.1f} %%".format(hum))

        time.sleep(0.5)
