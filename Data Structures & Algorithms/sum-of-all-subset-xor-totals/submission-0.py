class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len( nums )
        ans = 0
        for mask in range( 0, 2**n ):
            total = 0
            for j in range( 0, n ):
                if mask & ( 1<<j ):
                    total ^= nums[j]
            # print( mask, total )
            ans += total
        return ans