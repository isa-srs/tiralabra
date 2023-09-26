import unittest
from trie import Trie


class TestTrie(unittest.TestCase):
    def setUp(self):
        self.trie = Trie()

    def test_add(self):
        self.trie.add("ceg")
        self.assertEqual(self.trie.root.name, 'c')
        self.assertEqual(self.trie.root.children['c'][0].name, 'e')

    def test_add_multiple(self):
        self.trie.add("ceg")
        self.trie.add("cda")
        self.assertEqual(self.trie.root.children['c'][1].name, 'd')
        self.assertEqual(self.trie.root.children['c'][1].children['d'][0].name, 'a')