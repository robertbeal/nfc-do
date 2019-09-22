import os
import socket
import json
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO


def read_cards():
    with open("cards.json") as text:
        return json.load(text)


if __name__ == "__main__":
    cards = read_cards()
    reader = SimpleMFRC522()

    try:
        while True:
            id = reader.read()[0]

            ip = socket.gethostbyname("hifi.rb.kohi.uk")

            if id in cards:
                os.system("python3 dlnap.py --ip {} --play {}".format(ip, cards[id]))
            else:
                print("Unknown card: {}".format(id))
    except KeyboardInterrupt:
        GPIO.cleanup()
