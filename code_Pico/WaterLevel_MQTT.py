import sys
sys.path.append('./Libraries')

import machine
import network #use micropython-firmware-pico-w-290622.uf2 firmware on Pico-W (20230120)
import utime

import config

import MQTT_TopicData as td
from umqttsimple import MQTTClient

#import internetConnection as wifi # COPIED INTO THIS FILE

"""
    #_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#
    COPIED FROM internetConnection
    ONLY 2.4 GHz Network
"""
_firstTimeConnection = True
_wlan = network.WLAN(network.STA_IF)
_wlan.active(True)
def wifiConnect(maxRetries = 20, sleepRetry = 1, output = None):
    global _firstTimeConnection
    if _firstTimeConnection and _wlan.isconnected():
        if output != None:
            output("WiFi : " + config.SSID + " : " + str(_wlan.ifconfig()[0]))
        _firstTimeConnection = False
    
    connectCounter = 1
    while not _wlan.isconnected() and connectCounter <= maxRetries:
        if output != None:
            if connectCounter == 1:
                output("WiFi", end="")
            output(".", end="")
            
        _wlan.connect(config.SSID, config.PASSWORD)
        
        connectCounter += 1
        if connectCounter <= maxRetries:
            utime.sleep( sleepRetry )
        if output != None:
            if _wlan.isconnected():             
                output("")
                print(_wlan.ifconfig())
                output("WiFi : " + str(_wlan.ifconfig()[0]))
                
    return _wlan.isconnected()

"""
  #_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#_#
""" 
def callback_data(topic, msg):   # new
    print(topic, msg)

def needInternet():
    return True

def connect(output = None):    
    if not wifiConnect(1, 1, print):
        return
    
    client = MQTTClient(secrets.CLIENT_ID, config.MQTT_BROKER, keepalive=60)
    client.set_callback(callback_data)
    
    print("MQTT : Trying to connect.")
    if output != None:
        output("MQTT : " + config.MQTT_BROKER)
    
    client.connect()
    
    if output != None:
        output("MQTT : OK..")
    print("MQTT : OK..")
    
    return client
    
#waterlevels in the tanks
#((level1, direction), (leven2, direction))
_client = None
def show(data : dict):
    topicData = td.getTopicData(data)
    
    global _client
    try:
        if _client == None: #or not _client.isconnected():
            _client = connect()
        if _client == None:
            print("MQTT broker not found")
            return
        
        for t,d in topicData:
            print("MQTT (send) : ", t,d)
            _client.publish(t, d)
            
    except OSError as e:
        print("Error : ", e, "topics : ", topicData)
        _client.disconnect()
        _client = None
    finally:
        None
        
if __name__ == "__main__":
    import levelData
    levelSet = ((11, 89), (12, 88), (13, 87), (42, 58), (50,50), (8, 92), (50, 50), (10, 90))
    for l0,l1 in levelSet:
        print("Sending : ", l0, l1)
        data = levelData._getDummyData(l0, l1)        
        show(data)
        utime.sleep(3)
    

