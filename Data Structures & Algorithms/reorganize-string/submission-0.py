from collections import deque, Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = Counter( s )
        q = deque()
        heap = []

        for ch, f in freq.items():
            heapq.heappush( heap, ( -f, ch ) )
        
        t = 0
        ans = ''
        while heap or q:
            print( ans, heap, q )
            if q and q[0][0] == t:
                _, ch, f = q.popleft() 
                heapq.heappush( heap, ( -f, ch ) )
            
            if heap:
                f, ch = heapq.heappop( heap )
                ans += ch
                if f != -1:
                    q.append( (t+2, ch, -f-1) )
            else: return ''
            t += 1
        return ans