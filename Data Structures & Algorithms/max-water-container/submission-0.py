class Solution:
    def maxArea(self, h: List[int]) -> int:
        n = len( h )
        i = 0
        j = n-1
        maxArea = min( h[i],h[j] )*( j-i )
        while i < j:
            if h[i] > h[j]: j-=1
            else: i+=1

            maxArea = max( maxArea, min( h[i],h[j] )*( j-i ) )
        
        return maxArea
            