# nfc-do

https://raw.githubusercontent.com/pimylifeup/MFRC522-python/master/MFRC522.py
https://raw.githubusercontent.com/pimylifeup/MFRC522-python/master/SimpleMFRC522.py

deps:
spidev = "*"
RPi.GPIO = "*"

#!/usr/bin/env python

import RPi.GPIO as GPIO
import SimpleMFRC522

reader = SimpleMFRC522.SimpleMFRC522()

try:
        id, text = reader.read()
        print(id)
        print(text)
finally:
        GPIO.cleanup()