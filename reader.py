import os
import socket
from urllib.parse import urlparse


class Reader:
    def __init__(self, reader):
        self.__reader = reader

    def read(self):
        text = self.__reader.read()[1]

        if not text:
            raise Exception("Empty input")

        values = text.strip().split(' ')

        if(len(values) != 2):
            raise Exception("Invalid number of values")

        ip = self.__ip(values[0])
        uri = urlparse(values[1])

        if not ip:
            raise Exception("Invalid ip")

        if not uri.scheme or not uri.netloc:
            raise Exception("Invalid url")

        return Action(ip, uri.geturl())

    def __ip(self, hostname):
        try:
            return socket.gethostbyname(hostname)
        except:
            return None


class Action:
    def __init__(self, ip, uri):
        self.ip = ip
        self.uri = uri

    def execute(self):
        os.system("python dlnap.py --ip {} --play {}".format(self.ip, self.uri))
