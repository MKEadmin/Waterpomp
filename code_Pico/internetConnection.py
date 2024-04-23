"""

SOMEHOW YOU CAN'T HAVE A SEPERATE WIFI FILE
AND A SEPERATE MQTT FILE...
SO NEXT CODE IS COPIED TO MQTT MODULE

ONLY 2.4 GHz Network
"""

import machine
import network #use micropython-firmware-pico-w-290622.uf2 firmware on Pico-W (20230120)
import utime

import config

#2.4 GHz
_firstTimeConnection = True
_wlan = network.WLAN(network.STA_IF)
_wlan.active(True)
def wifiConnect(maxRetries = 20, sleepRetry = 1, output = None):
    global _firstTimeConnection
    if _firstTimeConnection and _wlan.isconnected():
        if output != None:
            output("WiFi : " + str(_wlan.ifconfig()[0]))
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

if __name__ == "__main__":
    def debug(txt, end="/n"):
        print(txt, end=end)
    
    connect(8, 1, debug)


