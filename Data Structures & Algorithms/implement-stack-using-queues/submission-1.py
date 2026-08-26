from collections import deque
class MyStack:

    def __init__(self):
        self.stack = deque()
        # self.q1 = deque()

    def push(self, x: int) -> None:
        self.stack.append( x )

    def pop(self) -> int:
        L = len(self.stack)
        for idx in range(L):
            popped_ele = self.stack.popleft()
            if idx == L - 1:
                return popped_ele
            else:
                self.push(popped_ele)

        # while True:
        #     val = self.stack.popleft()
        #     if self.empty(): break
        #     self.q1.append( val )
        # ans = val
        # self.stack = self.q1
        # self.q1 = deque()
        # return ans
        
    def top(self) -> int:
        val = self.pop()
        self.push(val)
        return val


    def empty(self) -> bool:
        return len(self.stack) == 0
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()