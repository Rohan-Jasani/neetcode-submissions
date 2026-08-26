class MyHashMap:

    def __init__(self):
        self.map_ = {}

    def put(self, key: int, value: int) -> None:
        self.map_[key] = value

    def get(self, key: int) -> int:
        return self.map_.get( key, -1 )

    def remove(self, key: int) -> None:
        self.map_.pop( key, None )


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)