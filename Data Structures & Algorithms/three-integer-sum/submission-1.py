from collections import Counter
class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len( nums )
        ans = []
        # -4, -1, -1, 0, 1, 2
        for i in range( 0,n ):
            if i > 0 and nums[i] == nums[i-1]: continue
            l = i + 1
            r = n - 1
            
            while l < r:
                sum3 = nums[i] + nums[l] + nums[r]
                if sum3 < 0: l+=1
                elif sum3 > 0: r-=1
                else: 
                    ans.append( [nums[i], nums[l], nums[r]] )
                    l += 1
                    r -= 1
                    # Skip duplicates
                    while l < r and nums[l] == nums[l - 1]:
                        l += 1

                    while l < r and nums[r] == nums[r + 1]:
                        r -= 1
        return ans
        '''
        freq = Counter( nums )
        ans = []
        def backtrack( path ):
            if len(path) == 3:
                if sum(path) == 0:
                    ans.append( path.copy() )
                return

            for num in nums: 
                if freq[num] == 0: continue
                path.append(num)
                freq[num] -= 1
                backtrack( path )
                freq[ path.pop() ] += 1
            return
        backtrack([])
        
        return list(set(tuple(sorted(x)) for x in ans))
        '''

    
        
        
