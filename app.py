import os
import socket
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO

if __name__ == "__main__":
    reader = SimpleMFRC522()

    try:
        while True:
            id = reader.read()[0]

            ip = socket.gethostbyname("hifi.rb.kohi.uk")
            cards = {8115724414: "http://server.rb.kohi.uk:8200/MediaItems/17356.mp3"}
            cards = {647582644551: "http://server.rb.kohi.uk:8200/MediaItems/17353.mp3"}

            if id in cards:
                os.system("python3 dlnap.py --ip {} --play {}".format(ip, cards[id]))
            else:
                print("Unknown card: {}".format(id))
    except KeyboardInterrupt:
        GPIO.cleanup()
