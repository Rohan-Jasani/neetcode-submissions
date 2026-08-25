class Solution:
    @staticmethod
    def next_smallest( heights ) -> list[int]:
        n = len(heights)
        stack = [ ( -float('inf'), 0 ) ] 
        next_s = [n]*n
        for i, h in enumerate( heights ):
            while h < stack[-1][0]:
                _, idx = stack.pop()
                next_s[idx] = i
            stack.append( ( h, i ) )
        return next_s

    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        next_s = Solution.next_smallest( heights )
        prev_s = [ n -1 - i for i in Solution.next_smallest( list(reversed( heights ) ) ) ]
        prev_s.reverse()
        area = [ (j - i - 1)*h for i, j, h in zip( prev_s, next_s, heights ) ]
        
        # print( next_s )
        # print( prev_s )
        # print( area )

        return max( area )
        