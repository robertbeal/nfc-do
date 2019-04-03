from reader import Reader
from mfrc522 import SimpleMFRC522
import RPi.GPIO as GPIO
import signal


class App:
    def __init__(self):
        self.terminate = False
        signal.signal(signal.SIGINT, self.exit)
        signal.signal(signal.SIGTERM, self.exit)

    def exit(self, signum, frame):
        self.terminate = True


if __name__ == '__main__':
    reader = Reader(SimpleMFRC522.SimpleMFRC522())

    while not App().terminate:
        try:
            reader.read().execute()
        except Exception as e:
            print("Error: Unable to read card - " + str(e))
        finally:
            GPIO.cleanup()
