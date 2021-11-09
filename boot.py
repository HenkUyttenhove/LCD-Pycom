# boot.py -- run on boot-up
# can run arbitrary Python, but best to keep it minimal

import machine
import os
import time

from network import WLAN
wlan = WLAN()  # get current object, without changing the mode

if machine.reset_cause() != machine.SOFT_RESET:
    wlan.init(mode=WLAN.STA)

if not wlan.isconnected():
    # change the line below to match your network ssid, security and password
    wlan.connect('kawanda.be', auth=(WLAN.WPA2, 'gpz32914'), timeout=5000)
