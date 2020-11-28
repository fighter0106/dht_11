import time  
import httplib, urllib  
import json  
import sys  
sys.path.append('/home/pi/rpi/code/Package')  
  


#**************************************************** 
# Set Pin No, MediaTek Cloud Sandbox (MCS) Key                                                                          
#**************************************************** 

sensor = 4  
blue = 0    # The Blue colored sensor.  
white = 1   # The White colored sensor.

deviceId = "D2WKWKcr"  
deviceKey = "kCHX2ZPhRJt6MIos"

#**************************************************** 
# Set MediaTek Cloud Sandbox (MCS) Connection                                                   
#**************************************************** 

def post_to_mcs(payload):  
    headers = {"Content-type": "application/json", "deviceKey": deviceKey}
    not_connected = 1
    while (not_connected):
        try:
            conn = httplib.HTTPConnection("api.mediatek.com:80")
            conn.connect()
            not_connected = 0
        except (httplib.HTTPException, socket.error) as ex:
            print "Error: %s" % ex
            time.sleep(10)  # sleep 10 seconds

    conn.request("POST", "/mcs/v2/devices/" + deviceId + "/datapoints", json.dumps(payload), headers)
    response = conn.getresponse()
    print( response.status, response.reason, json.dumps(payload), time.strftime("%c"))
    data = response.read()
    conn.close()

#**************************************************** 
# Post MediaTek Cloud Sandbox (MCS)                                                  
#**************************************************** 

while True:  
    temp=50
    humidity =77
    sw=1 
    print("temp = %.02f C humidity =%.02f%%"%(temp, humidity))


    
    payload = {"datapoints":[{"dataChnId":"Humidity","values":{"value":humidity}},{"dataChnId":"Temperature","values":{"value":temp}},{"dataChnId":"SwatchStatus","values":{"value":sw}}]}
    post_to_mcs(payload)
    time.sleep(5)

