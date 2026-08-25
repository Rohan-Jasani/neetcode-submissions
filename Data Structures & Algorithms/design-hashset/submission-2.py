class MyHashSet:

    def __init__(self):
        self.val = [[] for _ in range( 0, 1000 )]

    def add(self, key: int) -> None:
        if not self.contains( key ):
            self.val[key%1000].append( key )

    def remove(self, key: int) -> None:
        if self.contains( key ):
            self.val[key%1000].remove(key)

    def contains(self, key: int) -> bool:
        return key in self.val[key%1000]


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)