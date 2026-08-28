# from collections import deque
class LRUCache:

    def __init__(self, capacity: int):
        self.val = {}
        self.capacity = capacity        

    def get(self, key: int) -> int:
        if key in self.val.keys():
            val = self.val[key]
            self.put( key, val )
            return val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        keys = list( self.val.keys() )
        if key in keys:
            del self.val[key]
        if len( self.val ) == self.capacity:
            del self.val[keys[0]] 
        self.val[key] = value
        

