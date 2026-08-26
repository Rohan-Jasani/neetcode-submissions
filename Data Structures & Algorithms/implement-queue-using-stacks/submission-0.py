class MyQueue:

    def __init__(self):
        self.q = []
        self.temp = []

    def push(self, x: int) -> None:
        self.q.append( x ) 
        

    def pop(self) -> int:
        while self.q:
            self.temp.append( self.q.pop() )
        val = self.temp.pop()
        while self.temp:
            self.q.append( self.temp.pop() )
        return val

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len( self.q ) == 0
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()