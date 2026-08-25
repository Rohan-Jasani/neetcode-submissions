class MinStack:

    def __init__(self):
        self.val = []
        self.minst = [float('inf')]

    def push(self, val: int) -> None:
        self.val.append( val )
        if val <= self.minst[-1]: self.minst.append( val )

    def pop(self) -> None:
        if self.minst[-1] == self.val.pop():
            self.minst.pop()

    def top(self) -> int:
        return self.val[-1]

    def getMin(self) -> int:
        return self.minst[-1]
