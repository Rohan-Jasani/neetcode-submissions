import heapq
class MedianFinder:

    def __init__(self):
        self.left = [] #max heap of smaller half
        self.right = [] #min heap of larger half
        self.n = 0
    
    def addNum(self, num: int) -> None:
        heapq.heappush( self.left, -num )
        val = -heapq.heappop(self.left)
        heapq.heappush( self.right, val )
        if self.n % 2 == 0:
            val = heapq.heappop( self.right )
            heapq.heappush( self.left, -val )
        self.n += 1

    def findMedian(self) -> float:
        if self.n & 1 : return -self.left[0]
        return ( -self.left[0] + self.right[0] )/2
        