import unittest
from converter import Converter

class TestConverter(unittest.TestCase):
    def setUp(self):
        self.converter = Converter()
        self.song_file = 'src//data/testsong.txt'

    def test_read_song_file(self):
        self.converter.read_song_file(self.song_file)
        self.assertEqual(len(self.converter.converted), 4)
        self.assertEqual(self.converter.converted[0], 1)
