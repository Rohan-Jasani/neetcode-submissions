class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        n = len( nums )
        path = []
        ans = []
        
        nums.sort()
        def dfs( start ):
            ans.append( path.copy() )
            
            seen_rec = set()
            for i in range(start,len( nums )):
                if i > start and nums[i] in seen_rec: continue
                path.append( nums[i] )
                seen_rec.add( nums[i] )
                dfs( i+1 )
                path.pop()
        dfs( 0 )
        return ans