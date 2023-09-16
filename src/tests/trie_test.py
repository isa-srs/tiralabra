import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_add(self):
        self.trie.add("ceg")
        self.assertEqual(self.trie.root.children['c'], )
        