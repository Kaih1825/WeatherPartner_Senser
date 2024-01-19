import wiringpi
from wiringpi import GPIO

#import RPi.GPIO as GPIO
from . import dht
import time
import datetime

# initialize GPIO
wiringpi.wiringPiSetup()

# read data using pin
instance = dht.DHT(pin=0)


def getTmpAndHum():
    result = instance.read()
    if result.is_valid():
        tmp=result.temperature
        hum=result.humidity
        print(tmp)
        return f"{tmp},{hum}"
    else:
        return "null"
