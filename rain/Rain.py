
#!/usr/bin/python
# encoding:utf-8
import wiringpi
from wiringpi import GPIO
import time
def getraindata():
    P=""
    pin_rain=1

    # initialize GPIO
    wiringpi.wiringPiSetup()
    # set pin mode
    wiringpi.pinMode(pin_rain, GPIO.INPUT)
    wiringpi.pinMode(2, GPIO.INPUT)
    wiringpi.pullUpDnControl(pin_rain, pud=GPIO.PUD_DOWN)
    wiringpi.pullUpDnControl(2, pud=GPIO.PUD_UP)
    try:
        while True:
            
            
                status=wiringpi.digitalRead(1)
                # print(wiringpi.analogRead(2))
                #status = GPIO.input(1)
                if status == True:
                    p="No"    
                    print('我是雨滴模组，没有检测到雨滴，一切正常！')
                else:
                    p="Yes"    
                    print('我是雨滴模组，检测到雨滴，激活监控')
                return p
            
    except Exception as e:
        print(e)
        pass
    
