from DHT22 import dht22
from DFRobot_VEML6075.python.raspberrypi.examples import DFRobot_VEML6075_demo
from rain import Rain
from pathlib import Path
import time
import json
import requests
file = open("ha.txt", "a+")
hum=0.0
tmp=0.0
n=0.0
d="Yes"
f=open("ha.txt", "r+")
#print(f.read())
b=""
url = "https://weatherpartner.skailine.net/data"
locationName="大安高工" # Please input your location nama or leave blank to get location from ip
weatherInfo={
        'location':locationName
}
payload = json.dumps(weatherInfo)
headers = {'Content-Type': 'application/json'}
if f.read() =="":
    # Get temperature and humidity,and set sleep time=0.5 sec
    
    
    response = requests.request("POST", url, headers=headers, data=payload)
    print(response.text)
    
    print ("100000000000")
    a=json.loads(response.text)
    b=a["uuid"]
    f.write(b)
else:
    print ("9999999999999999999")
f.close()





while True:
    
    

    d="Yes"
    


    

    

   


    result=dht22.getTmpAndHum()
    if result!="null":
        results=result.split(",")
        tmp=results[0]
        hum=results[1]
    #print(f"溫度{tmp}度")
    #print(f"濕度{hum}%")
    n=DFRobot_VEML6075_demo.getUVData()
    d=Rain.getraindata()
    



    
    weatherInfo["purple"]=str(n)
    weatherInfo["temp"]=str(tmp)
    weatherInfo["wet"]=str(hum)
    weatherInfo["water"]=d
    
    payload = json.dumps(weatherInfo)
    f=open("ha.txt", "r+")
    m=f.read()
    response = requests.request("PUT", url+"/"+m, headers=headers, data=payload)
    print(url+"/"+m)
    print(response.text)
    print(tmp)
    time.sleep(0.5)
    pass
