import os
import socket
import json
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO


def read_cards():
    with open("cards.json") as text:
        return json.load(text)


if __name__ == "__main__":
    print("Reading configuration...")
    cards = read_cards()
    print(cards)

    print("Starting reader...")
    reader = SimpleMFRC522()
    print("Listening...")

    try:
        while True:
            id = str(reader.read()[0])

            ip = socket.gethostbyname("hifi.rb.kohi.uk")

            if id in cards:
                os.system("python3 dlnap.py --ip {} --play {}".format(ip, cards[id]))
            else:
                print("Unknown card: {}".format(id))
    except KeyboardInterrupt:
        GPIO.cleanup()
