class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len( nums )
        ans = []
        for mask in range( 0, 2**n ):
            sub = []
            for j in range( 0, n ):
                if mask & 1<<j: sub.append( nums[j] )
            ans.append( sub )
        return ans
            
        '''
        ans = []
        path = []
        def dfs( i ):
            if i == n:
                ans.append( path.copy() )
                return

            # dont pick nums[i]
            dfs( i+1 )

            # pick nums [i]
            path.append( nums[i] )
            dfs( i+1 )
            path.pop()
        dfs( 0 )
        return ans
        '''