import character as ch
import MatrixDisplay_v4 as md
from flowDirection import directionEnum
import levelData

#matrix Constants
XPOS_TEXT_1  = 64
XPOS_ARROW_1 = 32

XPOS_TEXT_2  =  0
XPOS_ARROW_2 = 56

#show the level1 and level2 on the Matrix
#data list of (level, direction)
showValues = {levelData.TANK_R: XPOS_TEXT_1
             ,levelData.TANK_L: XPOS_TEXT_2
             }

_oldTxt = ""
def debug(txt, end="\n"):
    global _oldTxt
    if txt == None:
        txt = ""
    txt = _oldTxt + txt
    md.showText(txt)
    print(txt)
    if end == "":
        _oldTxt = txt
    if end == "\n":
        _oldTxt = ""
def needInternet():
    return False

def show(data : dict):
    md.clear(0, False)
    for key in showValues.keys():
        level = levelData.getData(data, key, levelData.LEVEL_AVG)
        txt = "{:2d}cm".format(int(level))
        md.showText(txt, x=showValues[key], show = False, clear = False)
    #md.refresh() #will be updated with the arrows
    #print("MATRIX : ")
    
#show animated scrolling arrows on matrix display
_posY = 0
def animateArrows(data : dict):
    #print(data)
    direction = levelData.getData(data, levelData.TANK_R, levelData.DIRECTION)
    #print(direction)
    if direction == None:
        direction = directionEnum.SAME
        
    if direction == directionEnum.SAME:
        md.showCharacter(ch.SAME, x=XPOS_ARROW_1)
        md.showCharacter(ch.SAME, x=XPOS_ARROW_2)
        md.display.show()
        return
    
    global _posY
    charD = ch.getScrollingChar(ch.ARROW_D,  _posY)
    charU = ch.getScrollingChar(ch.ARROW_U, -_posY)
    _posY -= 1
    
    if direction == directionEnum.UP:
        xposD = XPOS_ARROW_1
        xposU = XPOS_ARROW_2
    else:
        xposD = XPOS_ARROW_2
        xposU = XPOS_ARROW_1
    md.showCharacter(charD, x=xposD)
    md.showCharacter(charU, x=xposU)    

    md.refresh()

if __name__ == "__main__":
    debug("wifi", end="")
    debug(".", end="")
    debug(".", end="")
    debug(".", end="")
    debug(".", end="")
#     
#     data = {1: {levelData.DIRECTION : directionEnum.UP,
#                 levelData.LEVEL_AVG : 43.8
#                 },
#             2: {levelData.DIRECTION : directionEnum.DOWN,
#                 levelData.LEVEL_AVG : 56.2
#                 }
#             }
#     show(data)
#     animateArrows(data)