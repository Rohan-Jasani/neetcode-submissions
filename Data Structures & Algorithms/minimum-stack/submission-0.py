class MinStack:

    def __init__(self):
        self.val = []

    def push(self, val: int) -> None:
        self.val.append( val )

    def pop(self) -> None:
        self.val.pop()

    def top(self) -> int:
        return self.val[-1]

    def getMin(self) -> int:
        return min( self.val )
