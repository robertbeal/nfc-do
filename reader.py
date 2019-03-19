import os
import socket


class Reader:
    def __init__(self, reader):
        self.__reader = reader

    def read(self):
        text = self.__reader.read()

        if not text:
            return Action()

        values = text.split(' ')
        ip = socket.gethostbyname(values[0])
        uri = values[1]

        return Action("python dlnap.py --ip {} --play {}".format(ip, uri))
        #os.system("python dlnap.py --ip {} --play {}".format(ip, uri))


class Action:
    def __init__(self, command=None):
        self.command = command
