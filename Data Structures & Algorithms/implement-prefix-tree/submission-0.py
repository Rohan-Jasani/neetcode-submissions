class Node:
    def __init__( self ):
        self.children = {}
        self.end = 0


class PrefixTree:

    def __init__(self):
        self.root = Node()        

    def insert(self, word: str) -> None:
        node = self.root

        for ch in word:
            if ch not in node.children:
                node.children[ch] = Node()
            node = node.children[ch]
        node.end += 1

    def search(self, word: str) -> bool:
        node = self.root

        for ch in word:
            if ch not in node.children: return False
            node = node.children[ch]
        return node.end > 0
        
    def startsWith(self, prefix: str) -> bool:
        node = self.root

        for ch in prefix:
            if ch not in node.children: return False
            node = node.children[ch]
        return True
        