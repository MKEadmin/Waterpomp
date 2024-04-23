import colorHelper
import neoPixelStrip as np
import neoPixelHelper
from flowDirection import directionEnum
import levelData

MOVES_SLEEP = 0.1
# NeoPixel Constants
HEIGHT_FULL  = 10
HEIGHT_EMPTY = 100
ALARM_TOP    = 20
ALARM_BOTTUM = 80
WARNING_TOP  = 30
WARNING_BOTTUM = 70

#get the index according of the level of water
def neoPixelGetIndex(level):
    return level * neoPixelHelper.PIXELS_STRIP // HEIGHT_EMPTY

#return the warning level colors 
def colorForLevel(level):
    if level < ALARM_TOP or level > ALARM_BOTTUM:
        return colorHelper.COLOR_RED
    if level < WARNING_TOP or level > WARNING_BOTTUM:
        return colorHelper.COLOR_ORANGE
    return colorHelper.COLOR_GREEN

def _neoPixelWaterLevel(level):
    index = neoPixelGetIndex(level)
    color = colorForLevel(level)
    return index, color

def needInternet():
    return False

#data : list of tuples (level, direction)
def show(data : dict):
    pixels = []
    for key in data.keys():
        level = levelData.getData(data, key, levelData.LEVEL_AVG)
        direction = levelData.getData(data, key, levelData.DIRECTION)
        pixels += _getPixels(key, level, direction )
    np.showPixels(pixels)
    #print("NeoPixel : ")
    
def clear():
    np.clear()
    
#data is one combination of (level, direction)
_dropPos = 0
def _getPixels(stripId: int, level : int, direction : int):
    global _dropPos
    index, color = _neoPixelWaterLevel(level)
    pixels = neoPixelHelper.getPixels(stripId, 0, index, color)
    if direction == directionEnum.UP:
        _dropPos = neoPixelHelper.animateDrop(pixels, index, _dropPos, colorHelper.COLOR_BLUE)
 
    return pixels

if __name__ == "__main__":
    for h in range(50, 100):
        for _ in range(30):
            pixels = show([(h, directionEnum.UP)])
    clear()