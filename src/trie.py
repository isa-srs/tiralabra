class Node:
    """Luokka, joka kuvaa yksittäistä solmua trie-puussa.
    """
    def __init__(self):
        """Määritellään sanakirjan solmulla olevat lapset.
        """
        self.children = {}


class Trie:
    """Luokka, joka esittää trie-tietokantaa.
    """
    def __init__(self):
        """Juureksi annetaan Node-olio.
        """
        self.root = Node()
    
    def add(self, sequence: str):
        """Lisää trieen uuden nuottisekvenssin alkaen juuresta. 

        Args:
            sequence (str): Merkkijonona esitetty nuottisekvenssi, esim. "ceg".
        """
        node = self.root

        for note in sequence:
            if note not in node.children:
                node.children[note] = Node()
            node = node.children[note]
        