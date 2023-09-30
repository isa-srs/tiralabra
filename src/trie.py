class Node:
    """Luokka, joka kuvaa yksittäistä solmua trie-puussa.
    """
    def __init__(self):
        """Konstruktori, sisältää yksittäisten solmujen tiedot.
        """
        self.children = {}
        self.name = ''


class Trie:
    """Luokka, joka kuvaa trietä. Tallentaa kaiken opetusmusiikin nuottisekvensseinä.
    """
    def __init__(self):
        """Konstruktori, antaa trien juureksi Node-olion.
        """
        self.root = Node()

    def add(self, sequence: str):
        """Lisää trieen uuden nuottisekvenssin.

        Args:
            sequence (str): Merkkijonona esitetty nuottisekvenssi.
        """
        node = self.root

        for note in sequence:
            if note not in node.children:
                node.children[note] = []
                node.name = note
            node.children[note].append(Node())
            node = node.children[note][-1]
