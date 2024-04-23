import colorHelper

PIXELS_STRIP   = 144
TOTAL_PIXELS   = 2 * PIXELS_STRIP
MAX_PIXEL_IDEX = TOTAL_PIXELS - 1

#2 led strips used
_strips = {1:[]
          ,2:[]
          }
def _init():
    pixel = 0
    while pixel < PIXELS_STRIP:
        #print(pixel, MAX_PIXEL_IDEX - pixel)
        _strips[1].append(pixel)
        _strips[2].append(MAX_PIXEL_IDEX - pixel)
        pixel += 1
_init()

def getNumberOfStrips():
    return len(_strips)

#return all pixels
def getAllPixels():
    return _strips[1] + _strips[2]

#return the strip with the given id
def getStrip(stripId: int):
    return _strips[stripId]

#get the pixels with a given color attached to it
#returns : list of (pixelId, color)
def _getPixels(strip: list, startIndex: int, endIndex: int, color: tuple):
    pixels = []
    index = 0
    for x in strip:
        if index < startIndex or index > endIndex:
            pixels.append((x, colorHelper.COLOR_BLACK))
        else:
            pixels.append((x, color))
        index += 1
    return pixels

#get the pixelnumber of the strip with the gived index
#stripId starts at 1
def getPixel(stripId: int, index: int):
    #print(stripId, index, _strips[stripId])
    return _strips[stripId][index]

def getPixels(stripId: int, startIndex: int, endIndex: int, color: tuple):
    #print(stripId, startIndex, endIndex, color)
    return _getPixels(_strips[stripId], startIndex, endIndex, color)
    
def animateDrop(pixels: list, levelPos: int, lastPos: int, dropColor: tuple):
    if levelPos >= lastPos:
        return PIXELS_STRIP - 1
    pixels[lastPos] = (pixels[lastPos][0], colorHelper.COLOR_BLACK)
    newPos = lastPos - 1
    if pixels[newPos][1] == colorHelper.COLOR_BLACK:
        pixels[newPos] = (pixels[newPos][0], dropColor)
    return newPos

def _countColor(pixels: list, color: tuple):
    count = 0
    for p in pixels:
        if p[1] == color:
            count += 1
    return count

def _print(pixels: list):
    tekst = ""
    for x in pixels:
        if x[1] == colorHelper.COLOR_BLACK:
            tekst += "_"
        elif x[1] == colorHelper.COLOR_GREEN:
            tekst += "G"
        elif x[1] == colorHelper.COLOR_ORANGE:
            tekst += "O"
        elif x[1] == colorHelper.COLOR_RED:
            tekst += "R"
        else:
            tekst += "|"
    print(tekst)
            
if __name__ == "__main__":
    from time import sleep
    print(_strips[1])
    print(_strips[2])
    height = 100
    pixels1 = getPixels(1, 0, height, colorHelper.COLOR_RED)
    pixels2 = getPixels(2, 0, PIXELS_STRIP-height, colorHelper.COLOR_RED)
    
    print("Start tests")
    
    assert len(getAllPixels()) == TOTAL_PIXELS, "Should be TOTAL_PIXELS"
    assert len(pixels1) == PIXELS_STRIP, "Should be 144"
    assert _countColor(pixels1, colorHelper.COLOR_RED) == 101, "Should be 101"
    assert _countColor(pixels2, colorHelper.COLOR_RED) == 45,  "Should be 44"
    
    print("All tests OK")
    
    print("** Left and right **")
    _print(pixels1)
    _print(pixels2)
    
    print("** animation **")
    teller = 0
    newPos1 = PIXELS_STRIP - 1
    for _ in range(5):
        if height >= PIXELS_STRIP:
            height = 0
        if teller % 20 == 0:
            height+=1
            pixels1 = getPixels(1, 0, height, colorHelper.COLOR_RED)
        #print(newPos1)
        newPos1 = animateDrop(pixels1, height, newPos1, colorHelper.COLOR_BLUE)
        _print(pixels1)
        teller += 1
        sleep(0.1)
