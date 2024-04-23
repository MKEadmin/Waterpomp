import sys
sys.path.append('./Secrets')
import secrets_DZHF as secrets 
#import secrets_HOME as secrets

CLIENT_ID 	= secrets.CLIENT_ID
SSID     	= secrets.SSID
PASSWORD		= secrets.PASSWORD

MQTT_BROKER = "192.168.1.124"

#I2C
PIN_I2C_SDA = 0
PIN_I2C_SCL = 1

#NeoPixel
PIN_NEOPIXEL_DIN = 28

#print("I2C devices : ", _i2c.scan())
I2C_LCD_ADDRESS = 0x3f

#HCSR04 - Ultrasoon
PIN_HCSR04_TRIGGER_0 = 21
PIN_HCSR04_ECHO_0    = 20
PIN_HCSR04_TRIGGER_1 = 19
PIN_HCSR04_ECHO_1    = 18

#MAX7219 Matrix display
MAX7219_NUMBER_OF_MODULES : int = 12 #3 x 4
PSI_MAX7219_CHANNEL = 0
PIN_MAX7219_SCK 		= 2
PIN_MAX7219_MOSI 	= 3
PIN_MAX7219_CS 		= 5

