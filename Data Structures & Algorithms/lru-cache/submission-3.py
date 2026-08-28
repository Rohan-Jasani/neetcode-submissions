class ListNode:
    def __init__(self, key=-1, val=0):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.size = 0
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        self.nodes = {}
    
    def _remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def _moveFront(self, node):
        node.next = self.head.next
        node.prev = self.head
        self.head.next.prev = node
        self.head.next = node

    def get(self, key: int) -> int:
        if key in self.nodes:
            node = self.nodes[key]
            self._remove(node)
            self._moveFront(node)
            return node.val
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.nodes:
            node = self.nodes[key]
            node.val = value
            self._remove(node)
            self._moveFront(node)
        else:
            if self.size == self.capacity:
                del self.nodes[self.tail.prev.key]
                self._remove(self.tail.prev)
                self.size -= 1
            
            node = ListNode(key, value)
            self._moveFront(node)
            self.nodes[key] = node
            self.size += 1
                


