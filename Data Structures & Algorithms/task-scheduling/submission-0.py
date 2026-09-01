from collections import deque, Counter
import heapq
class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter( tasks )
        heap = []
        q = deque()
        for ch, f in freq.items():
            heapq.heappush( heap, ( -f, ch ) )
        t = 0
        ans = []
        while heap or q:
            if q and q[0][0] == t:
                _, ch, f = q.popleft()
                heapq.heappush( heap, ( -f, ch ) )
            
            if heap:
                f, ch = heapq.heappop( heap )
                if f!=-1:
                    q.append( ( t + n + 1, ch, -f-1 ) )
                ans.append( ch )
            
            else:
                ans.append( '_' )

            t+=1
        # print(ans)

        return t

            
        
