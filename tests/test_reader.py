from reader import Reader, NoAction
import unittest


class InputReader:
    def __init__(self, value):
        self.value = value

    def read(self):
        return self.value


class TestReader(unittest.TestCase):
    def test_it_handles_null_cards(self):
        reader = Reader(InputReader(None))
        self.assertIsInstance(reader.read(), NoAction)

    def test_it_handles_empty_cards(self):
        reader = Reader(InputReader(''))
        self.assertIsInstance(reader.read(), NoAction)

    def test_it_handles_whitespace_padded_cards(self):
        reader = Reader(InputReader(' '))
        self.assertIsInstance(reader.read(), NoAction)

    def test_it_handles_invalid_input(self):
        reader = Reader(InputReader('localhost'))
        self.assertIsInstance(reader.read(), NoAction)

    def test_it_handles_invalid_hostnames(self):
        reader = Reader(InputReader('foo http://foo'))
        self.assertIsInstance(reader.read(), NoAction)

    def test_it_handles_invalid_file_uris(self):
        reader = Reader(InputReader('localhost foo'))
        self.assertIsInstance(reader.read(), NoAction)

    def test_it_reads_host_and_file_uri(self):
        reader = Reader(InputReader('localhost http://foo'))
        action = reader.read()
        self.assertEqual('127.0.0.1', action.ip)
        self.assertEqual('http://foo', action.uri)
