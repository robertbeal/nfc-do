import os
import socket
from urllib.parse import urlparse


class Reader:
    def __init__(self, reader):
        self.__reader = reader
        print("Reader listening...")

    def read(self):
        id, text = self.__reader.read()

        print("Reading card: {}".format(id))
        print("Text: {}".format(text))

        if not text:
            print("No 'text' on card")
            return

        values = text.strip().split(" ")

        if len(values) != 2:
            print("Invalid number of values")
            return

        ip = self.__ip(values[0])

        if not ip:
            return

        uri = urlparse(values[1])

        if not uri.scheme or not uri.netloc:
            print("Invalid url: {}".format(values[1]))
            return

        return Action(ip, uri.geturl())

    def __ip(self, hostname):
        try:
            return socket.gethostbyname(hostname)
        except:
            print("Unable to lookup ip for host: {}".format(hostname))
            return None


class Action:
    def __init__(self, ip, uri):
        self.ip = ip
        self.uri = uri

    def execute(self):
        os.system("python dlnap.py --ip {} --play {}".format(self.ip, self.uri))
