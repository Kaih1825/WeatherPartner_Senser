
#!/usr/bin/python
# encoding:utf-8
import wiringpi
from wiringpi import GPIO
import time
def getraindata():
    p="No"
    pin_rain=2

    #initialize GPIO
    wiringpi.wiringPiSetup()
    # set pin mode
    wiringpi.pinMode(pin_rain, GPIO.INPUT)
    wiringpi.pinMode(2, GPIO.INPUT)
    wiringpi.pullUpDnControl(pin_rain, pud=GPIO.PUD_DOWN)
    
    try:
        while True:
            
            
            status=wiringpi.digitalRead(2)
           # print(wiringpi.analogRead(1))
           # status = GPIO.input(2)
            if status == True:
                p="No"    
                    
            else:
                p="Yes"    
            return p
            
    except Exception as e:
        print(e)
        pass
    

#getraindata()
