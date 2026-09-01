import heapq
from collections import deque
class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = [ ( -a, 'a' ), ( -b, 'b' ), ( -c, 'c') ]
        heap = [ ( f, ch ) for f, ch in heap if f!=0 ]
        heapq.heapify( heap )
        q = deque()
        ans = ''
        i = 0
        while heap:
            # print( i, ans, heap, q )
            
            if heap:
                f, ch = heapq.heappop(heap)
                if i > 0 and ch == ans[-1] and f!=-1:
                    q.append( ( i+2, ch, -f-1 ) )
                elif f!=-1: heapq.heappush( heap, ( f+1, ch ) )
                ans +=  ch 
            i += 1
            if q and q[0][0] == i:
                _, ch, f = q.popleft()
                heapq.heappush( heap, ( -f, ch ) )
        
        return ans
