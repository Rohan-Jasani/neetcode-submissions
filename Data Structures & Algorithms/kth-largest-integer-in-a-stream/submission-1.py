import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = []
        self.k = k
        if len( nums ) != 0: self._build( k, nums )

    def _build( self, k, nums ):
        self.heap = nums[:k]
        heapq.heapify(self.heap)
        for num in nums[k:]:
            heapq.heappush( self.heap, num )
            heapq.heappop( self.heap )
        
    def add(self, val: int) -> int:
        heapq.heappush( self.heap, val )
        if len( self.heap ) > self.k:
            heapq.heappop( self.heap )
        return self.heap[0]
