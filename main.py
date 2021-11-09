######################################
# main.py -- put your code here!
#  Developed by Henk Uyttenhove
#  Date: 16 Nov 2017
#  Based upon Pycom Wipy
#
#  No license, free to copy decode
#
######################################

import socket     # import the IP stack
import struct
import time       # required to support the delay
from LCD import CharLCD
import utime
#Pin.setmode(Pin.BCM)

lcd = CharLCD()
lcd.message('Hello', 2)
lcd.set_line(1)
lcd.message('World!', 2)
time.sleep(5.0)
lcd.clear()
lcd.set_cursor(0, 0)
lcd.message("The year:", 0)
lcd.set_cursor(10, 0)
lcd.message(str(utime.localtime()[0]), 0)
lcd.set_line(1)
lcd.message("happy newyear", 0)
