class Node:
    """Luokka, joka kuvaa yksittäistä solmua trie-puussa.
    """
    def __init__(self):
        """Konstruktori, määrittelee solmulla olevat lapset.
        """
        self.children = {}


class Trie:
    """Luokka, joka kuvaa trietä. Sisältää kaiken opetusmusiikin nuottisekvensseinä.
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
                node.children[note] = Node()
            node = node.children[note]

    

if __name__ == "__main__":
    t = Trie()
    t.add("ceg")