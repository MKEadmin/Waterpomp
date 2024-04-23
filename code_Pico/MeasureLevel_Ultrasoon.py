import sys
sys.path.append('./Libraries')

from hcsr04 import HCSR04
from utime import sleep

from flowDirection import flowDirection
import config

_sensors = [HCSR04(trigger_pin=config.PIN_HCSR04_TRIGGER_0, echo_pin=config.PIN_HCSR04_ECHO_0, echo_timeout_us=10000)
           ,HCSR04(trigger_pin=config.PIN_HCSR04_TRIGGER_1, echo_pin=config.PIN_HCSR04_ECHO_1, echo_timeout_us=10000)
           ]

def _measure(sensor):
    return int(sensor.distance_cm())
       
def _measureLevel(idx : int):
    return _measure(_sensors[idx])

def getWaterLevel():
    level1 = _measureLevel(0)
    level2 = _measureLevel(1)
    
    return (level1,level2)
    
if __name__ == "__main__":    
    while True:
        result = getWaterLevel()
        print(result)
        sleep(1)

    # test with one : PIN_TRIGGER = 21, PIN_ECHO    = 20
    _sensor = HCSR04(trigger_pin=config.PIN_HCSR04_TRIGGER_0, echo_pin=config.PIN_HCSR04_ECHO_0, echo_timeout_us=10000)
    print('Distance:', measure(_sensor), 'cm')


