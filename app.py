import os
import socket
import json
import logging
import logging.handlers
import sys
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO


def read_cards():
    with open("/config/cards.json") as text:
        return json.load(text)


def logger():
    log = logging.getLogger()
    log.addHandler(
        logging.handlers.RotatingFileHandler("/data/app.log", maxBytes=3, backupCount=3)
    )
    log.addHandler(logging.StreamHandler(sys.stdout))
    log.setLevel(logging.INFO)
    return log


if __name__ == "__main__":
    log = logger()

    log.info("Reading configuration...")
    cards = read_cards()
    log.info(cards)

    log.info("Starting reader...")
    reader = SimpleMFRC522()
    log.info("Listening...")

    try:
        while True:
            id = str(reader.read_id())

            if id in cards:
                card = cards[id]
                log.info(f"Read card: {id}")

                if card.action == "dlna":
                    ip = socket.gethostbyname("hifi.rb.kohi.uk")
                    os.system(f"python3 dlnap.py --ip {ip} --play {card.file}")
            else:
                log.error(f"Unknown card: {id}")
    except KeyboardInterrupt:
        GPIO.cleanup()
