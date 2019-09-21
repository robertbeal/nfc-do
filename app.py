import os
import socket
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
from urllib.parse import urlparse

if __name__ == "__main__":
    reader = SimpleMFRC522()

    try:
        while True:
            id = reader.read()[0]

            ip = socket.gethostbyname("hifi.rb.kohi.uk")
            cards = {"8115724414": "http://server.rb.kohi.uk:8200/MediaItems/17356.mp3"}

            os.system("python dlnap.py --ip {} --play {}".format(ip, cards[id]))
    except KeyboardInterrupt:
        GPIO.cleanup()
