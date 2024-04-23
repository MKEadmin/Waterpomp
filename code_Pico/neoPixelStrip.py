from machine import Pin

import neopixel
import neoPixelHelper as helper
import colorHelper
import config

_np = neopixel.NeoPixel(Pin(config.PIN_NEOPIXEL_DIN), helper.TOTAL_PIXELS)

#set all pixels on black
def clear():
    for index in helper.getAllPixels():
        _np[index] = colorHelper.COLOR_BLACK
    _np.write()

#firstStrip is boolean
#index is the index of that strip
def showPixel(stripId: int, index: int, color: tuple):
    index = helper.getPixel(stripId, index)
    #print(index, color)
    _np[index] = color
    _np.write()
    
#pixels is a list of tuples (index, color)
def showPixels(pixels: list):
    for pixel in pixels:
        _np[pixel[0]] = pixel[1]
    _np.write()
       
clear()

if __name__ == "__main__":
    import random     
    while True:
        x = random.choice(helper.getStrip(0))
        #print(x, helper.getStrip(0))
        color = colorHelper.getRandomColor()        
        showPixel(0, x, color)
        showPixel(0, x, colorHelper.COLOR_BLACK)

