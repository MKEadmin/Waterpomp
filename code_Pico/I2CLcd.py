#https://www.tomshardware.com/how-to/lcd-display-raspberry-pi-pico
import sys
sys.path.append('./Libraries')

from machine import I2C, Pin
from utime import sleep

from pico_i2c_lcd import I2cLcd

import config

HEIGHT = 2
WIDTH = 16

_i2c = I2C(0, sda=Pin(config.PIN_I2C_SDA), scl=Pin(config.PIN_I2C_SCL), freq=400000)
_lcd = I2cLcd(_i2c, config.I2C_LCD_ADDRESS, HEIGHT, WIDTH)

def clear():
    _lcd.clear()
    
def write(text, x=0, y=0):
    _lcd.move_to(x,y)
    _lcd.putstr(text)
    
def writeLn(text, lineNumer = 0):
    _lcd.move_to(0, lineNumer)
    _lcd.putstr(text)
    
def backlight(on):
    if on:
        _lcd.backlight_on()
    else:
        _lcd.backlight_off()

def showCursor(on):
    if on:
        _lcd.show_cursor()
    else:
        _lcd.hide_cursor()
        
def cursor(on):
    if on:
        _lcd.blink_cursor_on()
    else:
        _lcd.blink_cursor_off()
        
def blinkBacklight(count = 10):
    for _ in range(count):
        backlight(True)
        sleep(0.2)
        backlight(False)
        sleep(0.2)
        
def setCustomChar(index, btArray):
    _lcd.custom_char(index, btArray)

def test_main():
    #Test function for verifying basic functionality
    print("Running test_main")
    i2c = I2C(0, sda=machine.Pin(config.PIN_SDA), scl=machine.Pin(config.PIN_SCL), freq=400000)
    lcd = I2cLcd(i2c, config.I2C_LCD_ADDRESS, I2C_NUM_ROWS, I2C_NUM_COLS)    
    lcd.putstr("It Works!")
    utime.sleep(2)
    lcd.clear()
    count = 0
    while True:
        lcd.clear()
        time = utime.localtime()
        lcd.putstr("{year:>04d}/{month:>02d}/{day:>02d} {HH:>02d}:{MM:>02d}:{SS:>02d}".format(
            year=time[0], month=time[1], day=time[2],
            HH=time[3], MM=time[4], SS=time[5]))
        if count % 10 == 0:
            print("Turning cursor on")
            lcd.show_cursor()
        if count % 10 == 1:
            print("Turning cursor off")
            lcd.hide_cursor()
        if count % 10 == 2:
            print("Turning blink cursor on")
            lcd.blink_cursor_on()
        if count % 10 == 3:
            print("Turning blink cursor off")
            lcd.blink_cursor_off()                    
        if count % 10 == 4:
            print("Turning backlight off")
            lcd.backlight_off()
        if count % 10 == 5:
            print("Turning backlight on")
            lcd.backlight_on()
        if count % 10 == 6:
            print("Turning display off")
            lcd.display_off()
        if count % 10 == 7:
            print("Turning display on")
            lcd.display_on()
        if count % 10 == 8:
            print("Filling display")
            lcd.clear()
            string = ""
            for x in range(32, 32+I2C_NUM_ROWS*I2C_NUM_COLS):
                string += chr(x)
            lcd.putstr(string)
        count += 1
        utime.sleep(2)
            
if __name__ == "__main__":
    print("At address: ",hex(I2C_ADDR))
    backlight(True)
    setCustomChar(0, bytearray([0x00,0x00,0x1B,0x1F,0x1F,0x0E,0x04,0x00]))
    setCustomChar(1, bytearray([0x00,0x00,0x0A,0x00,0x11,0x0E,0x00,0x00]))
    write(chr(0)+" WELCOME "+chr(1))
    sleep(2)
    
    clear()
    write("Backlight Test")
    blinkBacklight()
    
    cursor(True)
    sleep(2)
    cursor(False)
    
    while True:
        cursor(False)
        showCursor(False)
        
        backlight(False)
        clear()
        writeLn("I2C Address:"+str(hex(I2C_ADDR)))
        writeLn("Arjan Kamberg", 1)
        backlight(True)
        sleep(2)
        
        clear()
        for i in range(WIDTH):
            write(".", i, 0)
            write(".", WIDTH-i, 1)
            sleep(0.4)
            
        test_main()
