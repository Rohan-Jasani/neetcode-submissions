import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [ -x for x in stones ]
        heapq.heapify( heap )
        
        
        while len( heap ) > 1:
            y = -heapq.heappop(heap)
            x = -heapq.heappop(heap)
            
            if y > x: heapq.heappush( heap, -( y-x ) )
        
        if len( heap ) == 0: return 0

        return -heap[0]

        