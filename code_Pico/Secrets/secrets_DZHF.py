import machine
import ubinascii

CLIENT_ID = ubinascii.hexlify(machine.unique_id())

SSID     	= "Smartlab_studenten"
PASSWORD 	= "SmartLab"