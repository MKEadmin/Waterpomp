#version 4:
from machine import Timer
from utime import sleep

#import MeasureLevel_Ultrasoon as measureUltrasoon
import Measure_Pressure   as measurePressure
import MeasureLevel_Test  as measureUltrasoon
#import internetConnection as wifi 
import levelData          as lD

from flowDirection import directionEnum
import flowDirection

import WaterLevel_BlueTooth
import WaterLevel_Matrix
import WaterLevel_Neo
#import WaterLevel_LCD
import WaterLevel_MQTT

TANK_R = 1
TANK_L = 2
"""
    |          |    |          |
    |  TANK_L  |    |  TANK_R  |
    |  TANK 2  |    |  TANK 1  |
    |          |    |          |
    |          |    |          |
    ____________    ____________
"""

#tuple of functions with paramers ( (level1,direction1), (level2, direction2))
_showLevelFunctions = [None
                      ,WaterLevel_BlueTooth
                      ,WaterLevel_Matrix
                      ,WaterLevel_Neo # is done is timer...
                     #,WaterLevel_MQTT
                     #,WaterLevel_LCD
                      ]
    
_data = dict()    
def resetData():
    global _data
    _data = dict()
    
def tMeasure(timer):
    data = measureUltrasoon.getWaterLevel()
    pressure = measurePressure.getPressure()
    
    #print("Measuring new data : ", data)
    lD.addData(_data, TANK_R, lD.LEVEL_ULTRASOON, data[0])
    lD.addData(_data, TANK_L, lD.LEVEL_ULTRASOON, data[1])
    lD.addData(_data, TANK_R, lD.PRESSURE, pressure[0])
    lD.addData(_data, TANK_L, lD.PRESSURE, pressure[1])
    #print(_data)
    lD.calculateAverageLevel(_data)
    lD.calculateDirections  (_data)
    #print(_data)
    for func in _showLevelFunctions:
        if func != None:
            func.show(_data)
       
def tShowAnimation(timer):
    WaterLevel_Matrix.animateArrows(_data)
    WaterLevel_Neo.show(_data)

_timerAnimation= Timer()
_timerMeasure  = Timer()
def setTimer():
    _timerAnimation.init(period= 100, mode=Timer.PERIODIC, callback=tShowAnimation)
    _timerMeasure  .init(period=1500, mode=Timer.PERIODIC, callback=tMeasure)
def stopTimers():
    _timerAnimation.deinit()
    _timerMeasure  .deinit()
    
def run():
    needInternet = False
    for x in _showLevelFunctions:
        if x != None:
            needInternet = needInternet or x.needInternet()
    if needInternet:
        WaterLevel_MQTT.wifiConnect(maxRetries = 20, sleepRetry=8, output=WaterLevel_Matrix.debug)
        for x in _showLevelFunctions:
            if x != None and x.needInternet():
                x.connect(output=WaterLevel_Matrix.debug)
            
    resetData()
    setTimer()
   
def stop():
    print("Stop")
    resetData()
    stopTimers()
    WaterLevel_Neo.clear()  
        
if __name__ == "__main__":
    run()



