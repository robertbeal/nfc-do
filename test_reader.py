from reader import Reader
import unittest


class InputReader:
    def __init__(self, value):
        self.value = value

    def read(self):
        return self.value


class TestReader(unittest.TestCase):
    def test_it_handles_empty_cards(self):
        reader = Reader(InputReader(''))

        self.assertEqual(None, reader.read().command)
