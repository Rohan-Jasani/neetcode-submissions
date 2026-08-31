class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len( nums )
        path = []
        ans = []
        def dfs( start, remaining ):
            if remaining == 0:
                ans.append( path.copy() )
                return
            
            for i in range( start, n ):
                if nums[i] > remaining: break
                path.append( nums[i] )
                dfs( i, remaining - nums[i] )
                path.pop()
        
        dfs( 0, target )
        return ans