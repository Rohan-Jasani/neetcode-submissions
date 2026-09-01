import heapq
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        counter = 0
        for x, y in points:
            heap.append( ( -(x**2 + y**2)**0.5, counter, [x,y] ) )
            counter += 1
        
        heapq.heapify( heap )

        while len( heap ) > k:
            heapq.heappop( heap )
        
        return [ c for _,_,c in heap ]