class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        0,2,1,2,4
        for num in nums:
            prefix.append( prefix[-1] + num )
        
        ans = 0
        freq_map = Counter( prefix )
        for p in prefix:
            freq_map[p] -= 1
            ans += freq_map[ k+p ]
        return ans