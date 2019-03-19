#!/usr/bin/env python

import signal

class App:
    def __init__(self):
        self.terminate = False
        signal.signal(signal.SIGINT, self.exit)
        signal.signal(signal.SIGTERM, self.exit)

    def exit(self,signum, frame):
        self.terminate = True

import RPi.GPIO as GPIO
import SimpleMFRC522
import os
import socket

if __name__ == '__main__':
    reader = SimpleMFRC522.SimpleMFRC522()

    while not App().terminate:
        try:
            id, text = reader.read()

            if not text:
                print("Error: Card has no text")
                continue

            values = text.split(' ')
            ip = socket.gethostbyname(values[0])
            uri = values[1]

            os.system("python dlnap.py --ip {} --play {}".format(ip, uri))
        except:
            print("Error: Unable to read card")
        finally:
            GPIO.cleanup()
