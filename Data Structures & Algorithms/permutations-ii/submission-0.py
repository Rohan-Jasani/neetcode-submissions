class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        n = len( nums )
        ans = []
        path = []
        # nums.sort()
        seen = set()
        def dfs( ):
            if len( path ) == n:
                ans.append( path.copy() )
                return
            
            seen_rec = set()
            for i in range(0, n):
                if i in seen or nums[i] in seen_rec: continue
                path.append( nums[i] )
                seen_rec.add( nums[i] )
                seen.add( i )
                dfs()
                seen.remove( i )
                path.pop()
        
        dfs()
        return ans
