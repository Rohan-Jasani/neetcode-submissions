class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        seen = set()
        path = []
        ans = []
        def dfs( ):
            if len( path ) == n:
                ans.append( path.copy() )
                return
            
            for i in range( n ):
                if nums[i] in seen: continue
                path.append( nums[i] )
                seen.add( nums[i] )
                dfs()
                path.pop()
                seen.remove( nums[i] )
        dfs()
        return ans