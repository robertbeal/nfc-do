from reader import Reader
import pytest
import unittest


class InputReader:
    def __init__(self, value):
        self.value = value

    def read(self):
        return self.value


class TestReader(unittest.TestCase):
    def test_it_handles_null_cards(self):
        reader = Reader(InputReader(None))
        with pytest.raises(Exception):
            reader.read()

    def test_it_handles_empty_cards(self):
        reader = Reader(InputReader(''))
        with pytest.raises(Exception):
            reader.read()

    def test_it_handles_whitespace_padded_cards(self):
        reader = Reader(InputReader(' '))
        with pytest.raises(Exception):
            reader.read()

    def test_it_handles_invalid_input(self):
        reader = Reader(InputReader('localhost'))
        with pytest.raises(Exception):
            reader.read()

    def test_it_handles_invalid_hostnames(self):
        reader = Reader(InputReader('foo http://foo'))
        with pytest.raises(Exception):
            reader.read()

    def test_it_handles_invalid_file_uris(self):
        reader = Reader(InputReader('localhost foo'))
        with pytest.raises(Exception):
            reader.read()

    def test_it_reads_host_and_file_uri(self):
        reader = Reader(InputReader('localhost http://foo'))
        action = reader.read()
        self.assertEqual('127.0.0.1', action.ip)
        self.assertEqual('http://foo', action.uri)
