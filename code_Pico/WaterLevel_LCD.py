import I2CLcd as lcd
import character as ch
import levelData

lcd.setCustomChar(0, ch.getCharaterbyteArray(ch.ARROW_D_LCD))
lcd.setCustomChar(1, ch.getCharaterbyteArray(ch.ARROW_U_LCD))
lcd.setCustomChar(2, ch.getCharaterbyteArray(ch.SAME_LCD))

def _showPressure(pressure, x, y):
    if pressure == None:
        return
    lcd.write("{:1.2f}mbar".format(pressure), x, y)

def needInternet():
    return False

#level1 and level2 are the waterlevels in the tank
#direction1 and direction2 are for interfacing
def show(data : dict):
    level1 = levelData.getData(data, levelData.TANK_R, levelData.LEVEL_AVG)
    level2 = levelData.getData(data, levelData.TANK_L, levelData.LEVEL_AVG)
    dir1   = levelData.getData(data, levelData.TANK_R, levelData.DIRECTION)
    pressure1 = levelData.getData(data, levelData.TANK_R, levelData.PRESSURE)
    pressure2 = levelData.getData(data, levelData.TANK_L, levelData.PRESSURE)
    
    lcd.cursor(False)
    lcd.showCursor(False)
    lcd.backlight(True)
    #lcd.clear()
    #lcd.writeLn("1:{:3d}cm  2:{:3d}cm".format(level1, level2))
    lcd.writeLn("1:{:3d}cm 2:{:3d}cm".format(level1, level2))
    if dir1 == directionEnum.UP:
        lcd.write(chr(0),7)
        lcd.write(chr(1),15)
    elif dir1 == directionEnum.DOWN:
        lcd.write(chr(1),7)
        lcd.write(chr(0),15)
    else: #directionEnum.SAME
        lcd.write(chr(2),7)
        lcd.write(chr(2),15)
    
    _showPressure(pressure1, 0, 1)
    _showPressure(pressure2, 8, 1)
    
    #lcd.backlight(True)
